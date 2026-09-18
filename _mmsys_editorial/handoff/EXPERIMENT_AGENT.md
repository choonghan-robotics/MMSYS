# 실험결과 담당 에이전트 인계서

## 작업 목표와 기준 파일

`main.tex`를 기준으로 **기존 실험 기록의 확인과 결과 반영만** 수행한다. 이전 `MMSys27_revised_manuscript.tex`로 되돌아가지 않는다. 제목, 서론, 문헌 검토의 틀, 문단 분리, 주장 범위, 표 분리, 캡션의 논리 교정, 그림 외부 배치 코드는 이미 편집했다.

현재 숫자와 판정은 제공된 원고의 보고값을 보존한 것이며, 원시 결과의 독립 재검증을 뜻하지 않는다. 표시가 모순된 곳은 데이터가 틀렸다고 단정하지 말고 원래 evaluation script·manifest·로그에서 해소한다. 새 실험/재학습/새 baseline은 자동으로 실행하지 않는다. 기존 증거로 해결되지 않으면 OPEN으로 남겨 부족한 증거를 적는다.

## 수정 권한

원고의 `% EXP-EDIT-BEGIN: ...`와 `% EXP-EDIT-END: ...` 사이만 수정한다. 29개 구간에는 결과에 따라 바뀔 수 있는 Abstract·기여·Methods의 실제 구현 정의·표·Results·캡션·Conclusion·Limitations도 포함되어 있다. **구간 전체가 재작성 허가는 아니다.** 근거가 바뀐 사실, 값, 판정, 그에 직접 의존하는 해석 문장만 최소한으로 고친다. 문체와 문단 배치를 다시 손대지 않는다.

원본 그림 생성 코드가 실제 프로젝트에 있으면 E09/E13의 데이터·통계량·단위·모델 라벨을 바꾸고 해당 생성 코드로 다시 만든다. 임의로 내부 그래프를 새로 그리거나 다른 논문의 그림으로 대체하지 않는다. 본문의 두 패널 wrapper는 그대로 유지한다. GitHub `choonghan-robotics/MMSYS`의 `main`에는 `fig/arch.tex`, `fig/path_a.tex`, `fig/trade.tex`, `fig/quad_cam.png`, `references.bib`가 존재한다. 이 저장소 자산을 기준으로 사용한다. 세 `fig/*.tex`는 생성 파일이며 파일 머리말이 `tools/rbq_fig_*.py`와 `experiments/.../FIGURES_R1.json`을 가리키지만, 현재 저장소 루트에는 `tools/`와 해당 `experiments/` 경로가 없다. 생성 원본이 다른 저장소/아카이브에 있으면 그것을 찾아 근거로 사용한다.

## 시작 순서

1. 실제 저장소의 현재 commit을 기록하고 원본 로그·모델·그림 생성 코드를 찾는다. GitHub `main`에서 `fig/arch.tex`, `fig/path_a.tex`, `fig/trade.tex` 생성물을 직접 확인했다. 현재 blob SHA는 각각 `e2e63f2c51d6bbe526f49375639edc77c927988d`, `6e8d1964e38b97a019630ac028d960aec958677a`, `5094f1299482c5147fbda9ee04b9ddea950d1a14`이다. 생성 Python과 records JSON은 현재 저장소에서 확인되지 않았으므로 별도 원본 위치를 찾는다.
2. E01/E02/E04/E05를 먼저 확인하여 gate, oracle, 시간, disparity 단위를 고정한다. E03/E06/E07/E08/E09/E10/E11은 그 정의에 맞춰 재계산/대조한다.
3. 모든 변경을 `resolutions.json`에 남긴다. 수치 하나마다 campaign, artifact hash, precision, decoder/preprocessing hash, population, statistic, unit, denominator, run IDs를 식별한다.
4. E12/E13에서 본문·표·그림·Abstract·Conclusion의 일치 여부를 확인한다. 서로 다른 artifact의 정확도와 runtime을 합치지 않는다.
5. scope 검사 → 실제 자산 preflight → 원래 TeX toolchain 전체 compile → PDF 육안 점검 순서로 끝낸다.

## 반드시 보존할 구분

- HWGT128 T2L은 2×2, speed-line T2L은4×1이다.
- HWGT128 joint pass는 synchronized replay에서의 관측이다. staggered p99를25ms+p99로 확정하지 않는다.
- speed-line runtime에는 latency verdict gate가 없다. 다른 캠페인의40ms로원래pass를바꾸지 않는다.
- S5 T2L은1window의보조관측이다.3window pass/fail이아니다.
- mean, median, p99, per-pair, per-invocation, source-pixel units를 섞지 않는다.
- count 누락을0으로채우지 않는다. OPEN/미측정/실패는 다르다.
- sampling 무결성 검사를 전수검사로, repeat equality를독립oracle정확성으로바꾸지 않는다.
- fail-closed는qualification중단규칙이지 실제운용의모든오류검출보증이아니다.
- development exposure, seed waiver, 미개봉sealed sets, 미평가secondary reports를숨기지 않는다.

## 결과 증거 레코드

`resolutions.json`의 각 항목을 갱신한다. `evidence_files`는 다음 모양의 객체 목록이다.

```json
{"path":"repository-relative/path/to/result.json", "sha256":"실제 파일의 64자리 SHA-256", "role":"raw_log|evaluation_code|protocol|derived_summary|model|figure_source"}
```

`status`는 `OPEN`, `VERIFIED`, `QUALIFIED`만 사용한다. VERIFIED는 질문이원증거로해결된경우, QUALIFIED는증거부족을정직한범위제한/주장삭제로처리한경우다. QUALIFIED도무엇을제한했는지와근거가필요하다. 단순히주석을지웠다고해결로표시하지않는다.

최종 산출물은 변경된 `.tex`, 필요한 원본 `.tex/.py` 그림 파일, 근거 연결된 `resolutions.json`, diff, 실제 자산으로 컴파일한 PDF이다. 논문용 결과를 보완하지 않은 내부 테스트 PDF는 제출 PDF로 내보내지 않는다.

## 검사 명령

패키지 루트에서:

```bash
python tools/check_handoff.py scope --tex main.tex
python tools/check_handoff.py preflight --project-root /path/to/full/project --tex /path/to/full/project/main.tex
python tools/check_handoff.py evidence --release --project-root /path/to/full/project
```

`scope`는편집보호구간변경을검출한다. `preflight`는실제그림및BibTeX자산과교차참조를확인한다. `evidence --release`는OPEN항목이남아있으면실패한다. 스크립트는논문의수치정확성을증명하지않고인계규약만검사한다.


## E01 — Runtime 판정식·표 집계 방식

9개 predicate의 실제 필드와 두 캠페인의 gate를 연결하고 FPS/stream·범위·replacement 분모를 명시한다. 1798 outputs/10s와 C6 29.900은 min/mean 구분 문제일 수 있다.

**필요 증거:** 원래 frozen gate manifest와 revision/commit; run 및 stream-window별 gate flags와 raw counters; 시작·종료 timestamp와 rounding 구현

**완료 산출:** 각 gate의 이름, 수식, threshold, 적용 단위, 결측 처리; 두 표의 각 열이 min/mean/range 중 무엇인지 명시; runtime pass, accuracy pass, campaign completion을 분리

**금지:** S5에 HWGT128 40-ms gate를 사후 적용해 기존 verdict 바꾸기; S5 T2L 한 window를 sustained pass 또는 fail로 승격; 9를 prose 항목 수로 임의 대체

**수정 구간:** `ABSTRACT_RESULTS`, `CONTRIBUTION_RESULTS`, `PROTOCOL_RESULTS`, `VERIFIED_EVIDENCE_SUMMARY`, `TABLE_COMMON`, `COMMON_RUNTIME`, `TABLE_SPEED`, `S11_RESULTS`, `CONCLUSION_RESULTS`


## E02 — Oracle 종류·무결성 검사 범위·계측 비용

full-tensor oracle 비교, repeat equality, timed 64-element probe, physical 사후 48-frame replay를 artifact별로 분리한다. 반복 일치는 독립 참조 정확성과 다르다.

**필요 증거:** oracle 생성 코드 및 reference hash; artifact별 raw tensor shape/element count; probe 선택 규칙·seed·비교 frame/element 수; 비교 작업의 timed-path 포함 여부와 실행 시점

**완료 산출:** campaign/artifact × check mode × oracle × sample size × cost inclusion 표; HWGT128 실제 전수검사 여부; 216000 / 215856 / 215904 timed probe 및 physical 48-frame 분모 대응; 검사 범위를 Abstract/Results/Conclusion에 동일 반영

**금지:** 64-element probe만으로 모든 원소의 bitwise equality 주장; NPU self-repeat를 CPU oracle 비교로 바꾸기; 원고의 exhaustive admission requirement를 몰래 sampled criterion으로 약화

**수정 구간:** `ABSTRACT_RESULTS`, `CONTRIBUTION_RESULTS`, `PROTOCOL_RESULTS`, `MODEL_IO`, `VALIDATION_SCOPE`, `ORG_RESIDENCY`, `VERIFIED_EVIDENCE_SUMMARY`, `COMMON_ACCURACY`, `TABLE_COMMON`, `COMMON_RUNTIME`, `SPECIALIZED`, `BFP_RESULTS`, `R6_COMPARATOR`, `TABLE_SPEED`, `SPEED_SCREEN`, `S5_RESULTS`, `S11_RESULTS`, `PHYSICAL_RESULTS`, `CONCLUSION_RESULTS`, `LIMITATIONS_RESULTS`


## E03 — FP→QAT→export 단계와 정확도 연결

8/8 FP pass, 8/8 export eligibility, 0/8 quantized accuracy와 bad3 19.988–36.355→11.410–13.838의 단계·population·aggregation을 연결한다.

**필요 증거:** 8개 candidate ID와 FP/QAT initial/QAT terminal/export checkpoint hash; 동일 data/mask/aggregation의 EPE 및 bad3; comparator snapshot 및 rescue-arm 기록

**완료 산출:** 후보별 phase comparison 표; 초기 bad3 범위가 FP인지 초기 quantized인지 명시; export drift 0.0113 px/0.2673 pp의 population 구분; 확정된 counts와 contribution을 일치시킴

**금지:** 숫자를 뒤집어 손실처럼 보이게 만들기; KITTI mean과 macro-median 혼합; 고정 recipe 실패를 format 자체의 필연적 실패로 일반화

**수정 구간:** `CONTRIBUTION_RESULTS`, `SPECIALIZED`, `S5_RESULTS`, `CONCLUSION_RESULTS`


## E04 — Queue 및 response timestamp 정의

latest-only 1-slot 설명과 234–242-ms mean host wait를 연결한다. scheduled-arrival lag인지 실제 queue residence인지 확인한다.

**필요 증거:** producer/IPC/worker/session queue 코드와 capacity; t_scheduled,t_enqueued,t_selected,t_submitted,t_returned,t_decoded 로그; T1/T2L 동일 host allocation 및 arrival schedule; T3 replacement 부근의 event trace

**완료 산출:** 각 시간지표의 정확한 차분 식과 start/end 의미; one-slot과 추가 buffer의 실제 경로; Fig. 3(a) pooled means와 대기값 재생성; 충분한 trace가 없으면 원인 단정을 보류하고 관찰치만 유지

**금지:** 234–242를 불가능하다고 삭제; p99 성분을 합산해 response p99 구성; 25-ms 최대 대기+동기 replay p99만으로 비동기 failure 확정; 다른 artifact S5/S11 비교를 동일 모델 slack intervention으로 설명

**수정 구간:** `PROTOCOL_RESULTS`, `VALIDATION_SCOPE`, `ORG_T1`, `ORG_T2L`, `COMMON_RUNTIME`, `S5_RESULTS`, `CAPTION_PATH`, `S11_RESULTS`


## E05 — Disparity 단위·mask·resize·정확도 비교

spatial resizing과 disparity-value scaling을 분리한다. 본문 convention은 device grid width 640, disparity unit width 1280이다.

**필요 증거:** device configuration snapshot/firmware 및 decoder; neural decoder의 disparity unit 정의; source native sizes 및 horizontal scaling 코드; GT valid mask, device-invalid 처리, density 코드

**완료 산출:** 모델별 d_source=(W_source/W_unit)*Resize(d_output) 대응과 실제 구현 확인; baseline과 neural output 단위 명세; same-population mean/median·EPE/bad3 구분; 추가 공통유효영역 분석이 이미 있으면 보조로만 보고

**금지:** 출력폭640을 disparity unit 폭으로 간주해 scale2배 적용; 새 mask나 tuned baseline으로 primary gate 사후 교체; 미측정 근거리 distance accuracy 생성

**수정 구간:** `MODEL_IO`, `EVAL_SCOPE`, `VERIFIED_EVIDENCE_SUMMARY`, `COMMON_ACCURACY`, `R6_SETUP`, `R6_COMPARATOR`, `GEOMETRIC_DIAGNOSTICS`, `S5_RESULTS`, `S11_RESULTS`


## E06 — 84 calls와 80-output 분모

R6 output 1×4×128×208은 call당106496 elements. 8519680은80회, 84회 전체는8945664이다. 원고는 두 집계를 분리했으나 제외 원인은 아직 미확인이다.

**필요 증거:** 84-call event manifest; finite/nonnegative check 대상 call IDs; 출력 shape와 checker counter

**완료 산출:** total calls, counted calls, excluded calls, exclusion reason; finite-value check denominator를 정확히 명시

**금지:** 빠진4회를 근거 없이 warm-up으로 이름 붙이기; counted elements를 임의로84회분으로 증액

**수정 구간:** `R6_COMPARATOR`


## E07 — BFP 회복량·대조군·산술 예측

표시값 차이는8.843 pp이고 원고 회복량은8.844 pp다. 미반올림값이면 설명 가능하다. 98.0%는 R6 synthetic Bad-1 increase에 한정된다.

**필요 증거:** parent/FP/permuted unrounded metrics, same population hashes; 17 random permutation evaluator와 on/off-silicon execution flags; 32-frame selection objective/budget/registration; measured and predicted score provenance

**완료 산출:** 미반올림 loss/recovered/residual/recovery-percent 계산; 실측과 emulated random controls를 구분; rank1/18의 해석과 선택 후보 수 확인; Abstract, BFP prose, figure, Conclusion 동시 갱신

**금지:** 8.844를 원자료 없이 오기라고 확정; 98%를 정확도98% 또는 전지표 향상으로 표현; 17개 random control을 silicon measured로 표시

**수정 구간:** `ABSTRACT_RESULTS`, `CONTRIBUTION_RESULTS`, `BFP_RESULTS`, `CONCLUSION_RESULTS`


## E08 — R6 level-3 측정과 preparation admission

17.677-ms inference와1093-s compile/900-s limit의 run provenance를 확인한다. 문장 교정은 둘의 평가 상태를 동일시하지 않는다.

**필요 증거:** 각 compile 및 inference run ID; SDK/runtime/model hash; phase별 preparation stop rule와 acceptance record; Fig.3(b) R6 latency를 가져온 corpus/measurement

**완료 산출:** diagnostic 측정과 registered qualification의 관계; 17.677 및18.936의 dataset/session 차이; preparation fail과 measured latency의 분리 표기

**금지:** 제한 초과 후 진단을 했다고 임의 시나리오 추가; characterization 값을 다른 organization의 sustained result로 사용

**수정 구간:** `R6_RUNTIME`, `SPEED_SCREEN`


## E09 — ONNX boundary·variant·그림 구조 데이터

24/26 및 96/104 node count, HWGT128 8 inputs vs speed-line 4 input ports를 모델별 packing/boundary로 확인한다. 다른 variant의 동일성을 주장하면 안 된다. 현재 `fig/arch.tex`는 하단에서 S5와 `S11d`(direct-readout, did not learn)를 명시하고 S11 자체를 표시하지 않으므로, S11과 S11d를 같은 artifact로 취급하지 않는다.

**필요 증거:** S5/S11/R6/HWGT128 ONNX exports와 hashes; graph node/operator/boundary/initializer dump; screened vs trained 같은variant 비교; 원본 fig/arch.tex 및 생성 script

**완료 산출:** artifact,precision,layout,input count/shapes,output count/shapes,packing,node count 표; 그림의 모델명과 각 통계를 대응; finite camera-isolation checks의 실제 변경 input과 비교 범위; architecture figure 안의 실험연동 숫자만 수정

**금지:** four input을 근거 없이eight로 바꾸기; HWGT128 그림으로 S5/S11 graph 사용; finite draws를 모든 입력의 independence proof로 칭하기

**수정 구간:** `MODEL_IO`, `ORG_T2L`, `ORG_T3`, `ORG_RESIDENCY`, `R6_SETUP`, `BFP_RESULTS`, `SPEED_SCREEN`, `CAPTION_ARCH`, `S11_RESULTS`


## E10 — 통계·seed·comparison family

Holm은 전체 family의 raw p와 순서가 필요하다. 45/256 raw p≈7.028e−27와 보고p_Holm 관계를 확인한다. source에는 drive 독립성·teacher lineage 제한이 있다.

**필요 증거:** scene/frame별 paired metrics, ties, scene/drive IDs; raw p 및 Holm family membership; seed/checkpoint lineage 및 stopping-rule logs; bootstrap seed와 resampling unit

**완료 산출:** 같은family의 raw/adjusted p 및 win counts 표; sign test/bootstrap sample unit과 independence limitation 유지; seed-0 posthoc vsseed1/2 prespecified endpoint 구분

**금지:** pixels나 shared-parent seed-scene60개를 독립 sample로 사용; raw p에 무조건 family size 곱하기; 개발노출 결과를 held-out/generalization으로 재명명; 작은p만으로 power나 실용적 중요성 주장

**수정 구간:** `EVAL_SCOPE`, `VERIFIED_EVIDENCE_SUMMARY`, `COMMON_ACCURACY`, `SPECIALIZED`, `BFP_RESULTS`, `R6_COMPARATOR`, `GEOMETRIC_DIAGNOSTICS`, `S5_RESULTS`, `S11_RESULTS`, `LIMITATIONS_RESULTS`


## E11 — Thermal threshold·attempt/run/window accounting

95°C와100°C는 phase/campaign/sensor가 다를 수 있다. four attempts/six-run budget/eight runs/extra passing windows의 단위를 연결한다.

**필요 증거:** attempt→compile/session→window 계층의 run manifest; phase별 sensor ID,threshold,peak,abort cause; counted/voided/extra flag와 frozen protocol

**완료 산출:** 각 attempt/window를 한 행으로 정리; inference와 preparation의 적용 threshold 분리; 선정6개 physical windows 및 제외 기록 대응

**금지:** 완료하지 못한 run을 pass로 처리; 여러 threshold를 하나로 통일하기 위해 숫자 변경; startup ordering 수정을 threshold 변경 없음으로 전캠페인 일반화

**수정 구간:** `R6_RUNTIME`, `TABLE_SPEED`, `PHYSICAL_RESULTS`, `LIMITATIONS_RESULTS`


## E12 — 실험 범위·프로토콜 완료상태·물리 입력

runtime/accuracy/study completion을 분리한다. physical은 S5/S11, HWGT128은replay이고 일부 historical live tests는1camera 복제다. unopened sealed sets/mandatory4reports/teacher/waivers를 보존한다.

**필요 증거:** model/session/decoder/precision hash별 evidence inventory; gate와 secondary obligations 원본; physical timestamp semantics, clock-domain mapping, projector/config records; 원래 preregistration 및 waiver trail

**완료 산출:** 각 campaign의 completion matrix; 미평가 secondary4개 이름과runtime admission 연관; closed-loop/near-range/synchronization 미검증 범위 명시; 18 OAK stream-windows와 device-specific response origin 확인

**금지:** S5/S11 physical throughput과HWGT128 accuracy를 하나의artifact로 결합; 48-frame replay를 실시간 online detector로 표현; SDK 버전을편집상통일; 현재자료에없는실험완료를추정

**수정 구간:** `ABSTRACT_RESULTS`, `CONTRIBUTION_RESULTS`, `PROTOCOL_RESULTS`, `EVAL_SCOPE`, `COMMON_ACCURACY`, `COMMON_RUNTIME`, `R6_SETUP`, `GEOMETRIC_DIAGNOSTICS`, `TABLE_SPEED`, `S5_RESULTS`, `S11_RESULTS`, `PHYSICAL_RESULTS`, `CONCLUSION_RESULTS`, `LIMITATIONS_RESULTS`


## E13 — 그림의 수치·집계·참조선 연동

Fig.3(a)의 pooled mean과 off-scale wait, Fig.3(b)의 512-pair macro와 4 classical-profile band의 집계·corpus를 맞춘다. GitHub `main`의 `fig/path_a.tex`와 `fig/trade.tex` 생성물은 확보되었으나, 이 파일들이 가리키는 생성 Python과 records JSON은 현재 저장소에 없다.

**필요 증거:** fig/path_a.tex,fig/trade.tex 및 tools/rbq_fig_*.py 원본; 원래 사용한 per-frame logs/accuracy summaries; reference line/band 생성 및aggregation 코드; R6와S5/S11 isolated latency corpus provenance

**완료 산출:** 표와그림의동일한dataset/precision/statistic/unit; T2L4×1 및S5 one-window 표기; T3 per-invocation=4pairs와per-pair 비용 차이명시; band가range인지paired aggregate인지정확히표시;필요하면같은population별 baseline 생성; 원래(a)/(b)표기 존재 확인;동일표기중복금지

**금지:** min/max band를confidence interval 또는공통gate로표시; 서로다른dataset worst/best를임의평균해서 reference 생성; 평균그림을p99근거로사용; rawplot값과본문값따로수동관리

**수정 구간:** `R6_RUNTIME`, `CAPTION_ARCH`, `CAPTION_PATH`, `S11_RESULTS`
