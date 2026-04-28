# Reading Notes

논문별 읽기 노트를 개별 파일로 관리한다.

## Naming

```text
PAPERID_ShortName.md
```

예시:

```text
FT001_LoRA.md
RAG002_MultiDocFusion.md
APP004_NPP_LLM_Agent_Operation.md
```


## Template
~~~
## PAPER_ID - SHORT_NAME

> Metadata: see `../../index.md`

### Summary
- 

### Key Idea
-

### Contribution
-

### Note
-
~~~

## Example

```markdown
## FT001 - LoRA

> Metadata: see `../../index.md`

### Summary
- 대규모 언어모델 전체를 fine-tuning하지 않고, 기존 weight는 고정한 채 low-rank adapter만 학습하는 방법을 제안한다.
- 학습 파라미터 수와 GPU 메모리 사용량을 줄이면서도 full fine-tuning과 비슷한 성능을 목표로 한다.

### Key Idea
- Transformer layer의 weight update를 low-rank decomposition 형태로 제한한다.
- 기존 weight는 freeze하고, 작은 trainable matrix만 학습한다.

### Contribution
- Full fine-tuning 대비 학습 비용과 저장 비용을 크게 줄이는 효율적 adaptation 방법을 제안했다.
- Adapter 방식과 달리 inference latency를 추가하지 않는다는 장점을 보였다.

### Note
- NPP QA 데이터가 많지 않을 경우 full SFT보다 LoRA가 현실적일 수 있음.
- RAG 없이 LoRA만 적용한 경우와 RAG + LoRA 조합을 비교해볼 만함.
```
