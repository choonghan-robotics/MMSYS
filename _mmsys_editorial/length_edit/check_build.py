#!/usr/bin/env python3
"""Build the user-selected local paper project; do not select, clone, or push a repository.

Requires latexmk, the project's real assets, and its LaTeX dependencies.
No machine-learning experiments are run. A mechanical pass is not a visual audit.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project', required=True, type=Path,
                        help='User-selected local project directory containing main.tex')
    parser.add_argument('--output', type=Path,
                        help='New output directory (must not already exist)')
    args = parser.parse_args()
    root = args.project.expanduser().resolve()
    required = ['main.tex', 'references.bib', 'fig/quad_cam.png',
                'fig/arch.tex', 'fig/path_a.tex', 'fig/trade.tex']
    missing = [name for name in required if not (root / name).is_file()]
    if missing:
        parser.error('Required original assets missing: ' + ', '.join(missing))
    if shutil.which('latexmk') is None:
        parser.error('latexmk is not installed; build this project with its original TeX toolchain.')
    marker = r'\label{mmsys:body-end}'
    if marker not in (root / 'main.tex').read_text(encoding='utf-8'):
        parser.error('The nonprinting body-end marker is missing from main.tex.')
    if args.output:
        out = args.output.expanduser().resolve()
        if out.exists():
            parser.error('--output must be a new directory; existing build files are not overwritten.')
        out.mkdir(parents=True)
    else:
        out = Path(tempfile.mkdtemp(prefix='mmsys-length-build-'))
    env = dict(os.environ)
    env['TEXINPUTS'] = f'.:{root}//:' + env.get('TEXINPUTS', '')
    env['BIBINPUTS'] = f'.:{root}//:' + env.get('BIBINPUTS', '')
    env['BSTINPUTS'] = f'.:{root}//:' + env.get('BSTINPUTS', '')
    command = ['latexmk', '-pdf', '-halt-on-error', '-interaction=nonstopmode',
               f'-outdir={out}', 'main.tex']
    try:
        run = subprocess.run(command, cwd=root, env=env, stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT, timeout=900, check=False)
    except (OSError, subprocess.TimeoutExpired) as exc:
        print(f'Build did not complete: {exc}', file=sys.stderr)
        return 2
    (out / 'build-console.log').write_bytes(run.stdout)
    log_path = out / 'main.log'
    aux_path = out / 'main.aux'
    pdf_path = out / 'main.pdf'
    log = log_path.read_text(errors='replace') if log_path.exists() else ''
    aux = aux_path.read_text(errors='replace') if aux_path.exists() else ''
    hit = re.search(r'\\newlabel\{mmsys:body-end\}\{\{[^}]*\}\{(\d+)\}', aux)
    body_page = int(hit.group(1)) if hit else None
    metrics = {
        'latex_errors': len(re.findall(r'^!', log, re.M)),
        'undefined_citations': len(re.findall(r'Citation[^\n]*undefined', log)),
        'undefined_references': len(re.findall(r'Reference[^\n]*undefined', log)),
        'duplicate_label_warnings': len(re.findall(r'multiply[- ]defined', log, re.I)),
        'overfull_hboxes': log.count(r'Overfull \hbox'),
        'overfull_vboxes': log.count(r'Overfull \vbox'),
        'missing_characters': log.count('Missing character:'),
    }
    info = ''
    if pdf_path.exists() and shutil.which('pdfinfo'):
        proc = subprocess.run(['pdfinfo', str(pdf_path)], stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT, text=True, check=False)
        info = proc.stdout
        (out / 'pdfinfo.txt').write_text(info)
    n = re.search(r'^Pages:\s+(\d+)', info, re.M)
    report = {
        'project_path_user_supplied': str(root),
        'command': command,
        'latexmk_returncode': run.returncode,
        'source_sha256': sha256(root / 'main.tex'),
        'input_asset_sha256': {p: sha256(root / p) for p in required},
        'body_end_page_from_aux': body_page,
        'body_within_10_pages': body_page is not None and body_page <= 10,
        'total_pdf_pages': int(n.group(1)) if n else None,
        'pdf_sha256': sha256(pdf_path) if pdf_path.exists() else None,
        'bibliography_generated': (out / 'main.bbl').is_file(),
        'final_pass_log_checks': metrics,
        'visual_review_completed': False,
        'note': 'The body-end marker is after the AI disclosure, before the bibliography. '
                'The reference-start page is not used to infer body length. '
                'Inspect the actual PDF and metadata before submission.',
    }
    mechanical = (run.returncode == 0 and pdf_path.exists() and
                  report['bibliography_generated'] and report['body_within_10_pages'] and
                  not any(metrics.values()))
    report['mechanical_checks_passed'] = mechanical
    (out / 'LENGTH_BUILD_REPORT.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))
    print(f'Build artifacts: {out}')
    return 0 if mechanical else 1


if __name__ == '__main__':
    sys.exit(main())
