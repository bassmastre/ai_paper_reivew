# Experiment Ideas

논문을 읽으면서 떠오른 아이디어를 정리한다.  

## Template

### EXP000 - Title

#### 1. Related Papers
-

#### 2. Motivation
-

#### 3. Idea
-

#### 4. Next Step
-

---

## Example

```markdown
## EXP001 - LoRA vs SFT for NPP QA

### 1. Related Papers
- FT001 - LoRA
- FT002 - SFT/LoRA/ICL Data-Scarce

### 2. Motivation
- NPP 문서 기반 QA에서 전체 SFT보다 LoRA가 더 적은 비용으로 안정적인 성능을 낼 수 있는지 확인할 필요가 있다.

### 3. Idea
- 동일한 QA 데이터셋과 동일 base model을 사용해 SFT, LoRA, ICL을 비교한다.
- 먼저 RAG 없이 fine-tuning 단독 성능을 비교하고, 이후 RAG + LoRA 조합을 평가한다.

### 4. Next Step
- NPP guideline 기반 QA 샘플 50~100개를 먼저 만든다.