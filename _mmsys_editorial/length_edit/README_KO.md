# 본문 분량 편집본과 최종 빌드

이 디렉터리는 사용자가 전달받은 `MMSYS_length_edited.zip`의 분량 편집본을 원격에 반영한 기록이다. `LENGTH_EDIT_AUDIT_KO.md`와 `source_checks.json`의 '원격 변경 없음'은 로컬 편집 패키지 생성 당시의 기록이다. 이번 커밋은 사용자의 별도 푸시 요청으로 그 편집본을 반영한다.

## 반영 범위

- 루트 `main.tex`: 사용자에게 전달한 축약본과 동일한 내용.
- `LENGTH_EDIT_AUDIT_KO.md`: 편집 및 내부 지면 검사 기록.
- `source_checks.json`: 기준 버전, 소스 해시, 표·인용·배치 보존 검사.
- `check_build.py`: 실제 프로젝트 자산으로 빌드하고 본문 끝 페이지를 검사.
- 변경 diff는 이 커밋/PR의 Git diff에서 확인한다. 전체 문단 전후 기록은 전달된 ZIP에도 있다.

기준 commit: `9e9439c7213b5af16eaea79b91d96b6eab2a619c`
편집된 main.tex Git blob: `c1054f9969e8c3bcbf7073822e611b215eb39180`
편집된 main.tex SHA-256: `d74cb201792c16aea30897918aa3b412f9f9eb4ce7e3f1455024357b58419896`

기존 `fig/`, `references.bib`, `latexmkrc`, ACM 클래스, 실험 증거 및 검증 상태 장부는 변경하지 않는다.

## 아직 필요한 최종 빌드

이번 푸시는 실제 원본 자산을 모두 사용한 제출 PDF 빌드 완료를 뜻하지 않는다. 기존 `handoff/FINAL_BUILD_AUDIT.md`는 축약 전 원고의 기록이며, 그 PDF 해시를 이번 축약본에 재사용하면 안 된다.

원래 프로젝트의 빌드 방법을 쓰거나 다음을 실행한다. 위치는 사용자가 지정한다.

```bash
python3 _mmsys_editorial/length_edit/check_build.py \
  --project /사용자가_지정한/main.tex가_있는_폴더 \
  --output /사용자가_지정한/새_빌드_출력폴더
```

출력 폴더는 새 경로여야 한다. 도구는 새 실험·재학습·clone·push를 하지 않는다.

AI disclosure 끝의 비인쇄 `mmsys:body-end` label로 실제 본문 끝 페이지를 확인한다. References 시작 페이지만 보고 본문 분량을 판단하지 않는다. 원본 그림과 참고문헌으로 빌드한 PDF·마지막 로그·새 PDF SHA-256을 보관하고 그림, 표, 익명성을 확인한다.

## 저장소 지정 정책

향후 에이전트가 작업할 논문 저장소와 기준 브랜치는 사용자가 지정한다. 이 문서의 역사적 source commit이나 evidence 저장소를 다음 작업의 대상 저장소로 자동 선택하지 않는다.
