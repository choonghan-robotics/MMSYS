# 그림 원본 코드 점검 — GitHub 동기화 기준

검토 저장소: `choonghan-robotics/MMSYS`, branch `main`

## 실제 확인 자산
- `fig/arch.tex` — `e2e63f2c51d6bbe526f49375639edc77c927988d`
- `fig/path_a.tex` — `6e8d1964e38b97a019630ac028d960aec958677a`
- `fig/trade.tex` — `5094f1299482c5147fbda9ee04b9ddea950d1a14`
- `fig/quad_cam.png` — `9e5aa16385af2ed7a34dc046bfe3c68cbbf36081`
- `references.bib` — `e9ff1ead81f0a7fa33f36b6c243b615b863df769`

세 TikZ 파일은 생성물이라고 명시하며 `tools/rbq_fig_*.py`와
`experiments/mmsys2027_rbq_retarget_20260914/paper_figures_20260915/FIGURES_R1.json`
을 참조한다. 현재 GitHub `main`에는 그 생성 Python/records 경로가 없다.

## 확인된 수정점
1. `fig/arch.tex`는 S5와 **S11d**를 표시한다. S11d는 direct-readout, did-not-learn screen variant이며 본문의 학습된 soft-argmax S11과 다르다. `main.tex`은 둘을 구분하도록 수정했다.
2. `fig/path_a.tex`의 T2L 라벨은 단순 `T2L`이다. speed-line 본문에서 S5/S11 T2L은 모두 four-process `4×1`; 캡션과 Description에 이 의미를 명시했다.
3. `path_a.tex`에는 `(a)`, `trade.tex`에는 `(b)`가 이미 포함되어 있다. 외부 중복 라벨을 추가하지 않는다.
4. `trade.tex`의 classical-profile band는 descriptive range로 취급하며 confidence interval이나 공통 gate로 부르지 않는다.
5. 그림의 수치·좌표는 생성 원본이 없으므로 이번 동기화에서 손으로 수정하지 않았다.

## 남은 확인
- S5/S11/S11d/R6 ONNX hash와 graph dump 대조
- Fig. 3(a) queue timestamp와 pooled mean 재생성
- Fig. 3(b) latency corpus 및 classical-profile band 재생성
- 생성 Python/records 원본 위치 확보
- 실제 PDF의 글자 크기·bounding box 확인
