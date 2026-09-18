# Manuscript language and sentence structure

The author requested this writing standard on 2026-09-07. Apply it to the
English abstract, main text, captions, and subsequent revisions.

## Reference

Choonghan Lee and Woosoon Yim, *Development of pre-magnetized
magnetorheological elastomer for bidirectionally variable stiffness
applications*, Smart Materials and Structures 33 (2024), 095042,
DOI: 10.1088/1361-665X/ad7003.

The supplied PDF was inspected, including the abstract, introduction,
principles, fabrication procedure, experimental methods, results, and
conclusions. Its SHA-256 is
`6e375935dcf3998e3270ef61c44788c7e22452daeba42f4f56973389847a8714`.
The reference is for language and explanatory structure, not a technical
source for NPU or stereo claims. Do not add it to the scientific bibliography
solely because it informed the prose. Do not redistribute the reference PDF
with the manuscript or include this guide in the submitted PDF.

## Writing standard

- Use formal engineering English at the reference's vocabulary and sentence
  complexity level. Retain necessary technical terms, define them at first
  use, and explain their role with a complete subject and predicate.
- Introduce a component and its purpose before describing its parameters or
  reporting measurements. Prefer explicit relationships to stacked compound
  nouns and internal implementation labels.
- Organize experimental paragraphs as purpose or condition, procedure,
  observation, and interpretation. State an explanation as a hypothesis when
  the measurements do not identify the cause.
- Use present tense for definitions and system operation. Use past tense for
  completed procedures and observations. Passive constructions are suitable
  for methods; active constructions are suitable when the acting component
  or author decision matters.
- Use connected, moderately developed sentences. Split a sentence when it
  contains several independent conditions or caveats. Avoid both a sequence
  of compressed status fragments and unnecessarily nested sentences.
- Connect findings with terms such as "however", "therefore", and
  "consequently" only when the stated contrast or inference is supported.
  Refer directly to the relevant table, measurement, or equation.
- Preserve technical precision. For example, explain "runtime" as the
  software that receives frames and executes the processing steps; explain
  "full offload" as executing all neural-model operations on the NPU.
  Define "oracle regret" before using it in the prediction evaluation.
- Adapt general prose features, not distinctive sentences, figures, or
  claims from the reference. Do not reproduce grammatical errors or add
  unsupported claims of novelty or superiority.

The request concerns language level and sentence structure. It does not
require matching the reference's page count or changing the ACM template.

## Evidence that editing must preserve

The author's later priority decision makes T1 sequential processing, T2L
process-isolated logical partitioning, and T3 joint independent-camera
processing the primary comparison. Physical partitioning is an optional
extension. Historical result identifiers named T2 still denote physical
experiments; do not relabel them as successful T2L results. Logical streams,
processes, and multiple DPU subgraphs are not evidence of physical partitions
or six physical cameras.

Do not change model definitions, units, measured values, failed-run status,
the no-CPU-model-fallback requirement, or the distinction between development
and final accuracy. Keep the final eighty-scene split sealed until its
admission checks pass. A passing short test must not erase a later failure.

The R5 language revision preserves the R4 numerical results and scientific
limitations. It does not introduce new experiments, establish final accuracy,
or turn the working manuscript into a submission-ready paper.
