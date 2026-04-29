# Guide

이 문서는 `AI Paper Archive`를 관리하기 위한 내부 규칙입니다. 방문자용 설명은 [`README.md`](../README.md)를 기준으로 하고, 실제 운영 기준은 이 문서를 기준으로 합니다.

## Table of Contents

- [1. Overview](#1-overview)
- [2. Repository Structure](#2-repository-structure)
- [3. Folder Guide](#3-folder-guide)
- [4. Source of Truth](#4-source-of-truth)
- [5. Standard Workflow](#5-standard-workflow)
- [6. Paper Intake and Classification](#6-paper-intake-and-classification)
- [7. Folder Management](#7-folder-management)
- [8. Metadata Files](#8-metadata-files)
- [9. Notes and Ideas](#9-notes-and-ideas)
- [10. Git Policy](#10-git-policy)
- [11. Summary](#11-summary)

## 1. Overview

이 저장소는 AI/ML 논문을 주제별로 정리하고, 논문별 메타데이터와 읽기 노트를 관리하기 위한 개인 아카이브입니다.

PDF 파일은 로컬에만 보관합니다. GitHub에는 논문 원문 파일이 아니라 `index.md`, 폴더별 `*_meta.md`, 읽기 노트, 실험 아이디어, 관리 스크립트만 올립니다.

## 2. Repository Structure

```text
.
├── 00_Inbox/
├── 01_Survey/
├── 02_Training/
├── 03_Retrieval/
├── 04_Evaluation/
├── 05_Systems/
├── 06_ML/
├── 07_Agents/
├── 08_Domain/
├── 99_Meta/
├── src/
├── index.md
├── main.py
└── README.md
```

| Folder | ID Prefix | Role |
|---|---|---|
| `00_Inbox` | `INB` | 미분류 논문 임시 보관 |
| `01_Survey` | `SUR` | Survey, review, taxonomy |
| `02_Training` | `TRN` | Fine-tuning, PEFT, instruction tuning, adaptation |
| `03_Retrieval` | `RET` | Search, retrieval, RAG, reranking |
| `04_Evaluation` | `EVA` | Benchmark, metric, dataset, evaluation protocol |
| `05_Systems` | `SYS` | Pipeline, workflow, document processing, data generation system |
| `06_ML` | `ML` | ML methods, architectures, baseline models |
| `07_Agents` | `AGT` | LLM agents, tool use, planning |
| `08_Domain` | `DOM` | Domain applications |
| `99_Meta` | - | Guide, reading notes, experiment ideas |

## 3. Folder Guide

폴더는 논문의 **주 기여**를 기준으로 하나만 고릅니다. 겹치는 주제는 `Tags`에 기록합니다.

### 3.1 `00_Inbox`

아직 분류하지 않은 논문을 임시로 둡니다.

넣는 경우:
- 새로 받은 논문
- 초록을 아직 확인하지 않은 논문
- 어느 폴더가 맞는지 애매한 논문

오래 보관하지 않습니다. 초록과 contribution을 확인한 뒤 정식 폴더로 옮깁니다.

### 3.2 `01_Survey`

분야를 넓게 정리하거나 여러 방법을 비교하는 논문을 둡니다.

넣는 경우:
- Survey, review, tutorial, taxonomy
- 특정 분야의 research landscape 정리
- 여러 방법론을 비교하는 개관 논문

예:
- Instruction tuning survey
- RAG survey
- Agent survey
- Neural operator review

### 3.3 `02_Training`

모델을 학습, 적응, 정렬하는 방법론 논문을 둡니다.

넣는 경우:
- SFT, LoRA, PEFT, adapter, prompt tuning
- Instruction tuning, ICL, data-scarce adaptation
- Alignment, RLHF, DPO, preference optimization
- Continual learning, catastrophic forgetting 완화

헷갈리는 경우:
- 개관 논문이면 `01_Survey`
- 특정 도메인 적용이 핵심이면 `08_Domain`

### 3.4 `03_Retrieval`

검색 또는 RAG의 검색 로직이 핵심인 논문을 둡니다.

넣는 경우:
- Search, retrieval, reranking
- Dense/sparse/hybrid retrieval
- Query rewriting, evidence selection
- RAG 중 검색 전략이 핵심인 논문
- 문서에서 조건, 절차, 규정 등을 찾는 방법론

헷갈리는 경우:
- 평가 벤치마크 구축이 핵심이면 `04_Evaluation`
- OCR, chunking, layout parsing 같은 처리 흐름이 핵심이면 `05_Systems`

### 3.5 `04_Evaluation`

모델이나 시스템을 평가하기 위한 데이터셋, 벤치마크, 지표 논문을 둡니다.

넣는 경우:
- Benchmark dataset
- Evaluation metric
- Leaderboard, test suite
- Human evaluation protocol
- RAG, agent, long-context, model evaluation

헷갈리는 경우:
- 특정 모델/알고리즘 자체가 핵심이면 `06_ML`
- 평가를 포함하지만 end-to-end 시스템 제안이 핵심이면 `05_Systems`

### 3.6 `05_Systems`

여러 컴포넌트를 연결한 시스템, 파이프라인, 데이터 처리 workflow 논문을 둡니다.

넣는 경우:
- Pipeline architecture
- OCR, layout parsing, chunking, document processing
- Data generation system
- Logging, monitoring, tracing, serving workflow
- Retrieval, LLM, evaluator, tool을 연결한 end-to-end system

헷갈리는 경우:
- 검색 알고리즘 자체가 핵심이면 `03_Retrieval`
- agent의 planning/tool use가 핵심이면 `07_Agents`
- 도메인 문제 해결이 핵심이면 `08_Domain`

### 3.7 `06_ML`

일반 ML 방법론, 모델 구조, baseline 모델 논문을 둡니다.

넣는 경우:
- Gradient boosting, random forest, classical ML
- XGBoost, LightGBM, CatBoost
- Transformer, attention, neural architecture
- DeepONet, neural operator, surrogate model
- Classification, anomaly detection, regression baseline

헷갈리는 경우:
- LLM fine-tuning 방법이면 `02_Training`
- 평가 benchmark가 핵심이면 `04_Evaluation`

### 3.8 `07_Agents`

LLM agent의 추론, 계획, 도구 사용, memory, multi-agent 구조가 핵심인 논문을 둡니다.

넣는 경우:
- Tool use, function calling
- Planning, reflection, self-correction
- Memory, autonomous agent
- Multi-agent, agent orchestration
- Operator assistant 구조

헷갈리는 경우:
- 특정 도메인 적용이 중심이면 `08_Domain`
- agent 평가 벤치마크가 중심이면 `04_Evaluation`

### 3.9 `08_Domain`

특정 산업, 과학, 의료, 원전, 서비스 도메인 적용이 핵심인 논문을 둡니다.

넣는 경우:
- Nuclear power plant, industrial AI, medical AI
- Safety event classification
- Fault detection, operation support
- 도메인 데이터 기반 classification, detection, decision support

헷갈리는 경우:
- agent 구조 자체가 핵심이면 `07_Agents`
- 도메인 문서 처리 pipeline이 핵심이면 `05_Systems`
- 도메인 검색 방법론이 핵심이면 `03_Retrieval`

## 4. Source of Truth

[`index.md`](../index.md)가 전체 논문 목록의 단일 원본입니다.

각 폴더의 `*_meta.md`는 `index.md`를 기준으로 자동 생성합니다. 특별한 이유가 없으면 `*_meta.md`를 직접 수정하지 않습니다.

## 5. Standard Workflow

논문 추가 또는 수정 절차:

1. PDF를 적절한 폴더에 둡니다.
2. [`index.md`](../index.md)에 논문 정보를 추가하거나 수정합니다.
3. 인덱스를 검사합니다.

```bash
python main.py --check
```

4. 폴더별 메타 파일을 다시 생성합니다.

```bash
python main.py
```

5. 변경 내용을 확인하고 Git에 반영합니다.

```bash
git add .
git commit -m "Update paper archive"
git push
```

## 6. Paper Intake and Classification

### 6.1 Inbox Rule

분류가 확실하지 않은 논문은 먼저 `00_Inbox`에 둡니다.

- Inbox 안에서는 파일명이 임시 상태여도 됩니다.
- 초록과 contribution을 확인한 뒤 정식 폴더로 옮깁니다.
- 정식 폴더로 옮길 때 파일명을 `Year_ShortName.pdf` 형식으로 정리합니다.
- 이동한 논문은 `index.md`에 등록합니다.

### 6.2 Naming Rule

PDF 파일명은 짧고 일관되게 작성합니다.

```text
Year_ShortName.pdf
```

예:

```text
2022_LoRA_ICLR.pdf
2025_Ko_LongRAG.pdf
2025_MultiDocFusion.pdf
2024_NPP_Safety_Event_Classification_LLM.pdf
```

### 6.3 Year Rule

- `Year`는 공식 게재 연도를 우선 사용합니다.
- 정식 게재 정보가 없으면 preprint 공개 연도를 사용합니다.
- arXiv 최초 공개 연도와 공식 게재 연도가 다르면 `Note`에 기록합니다.

### 6.4 Classification Rule

분류 원칙:

1. 하나의 논문은 하나의 주 폴더에만 둡니다.
2. 폴더는 논문의 주 기여 기준으로 선택합니다.
3. 겹치는 성격은 `Tags`에 기록합니다.
4. 같은 PDF를 여러 폴더에 복사하지 않습니다.

예:
- `Ko-LongRAG`는 RAG 논문이지만 benchmark 구축이 핵심이므로 `04_Evaluation`.
- `MultiDocFusion`은 RAG를 다루지만 문서 처리/chunking pipeline이 핵심이므로 `05_Systems`.
- `Large Language Model Agent for Nuclear Reactor Operation Assistance`는 원전 논문이지만 agent 구조와 tool use가 핵심이면 `07_Agents`.

## 7. Folder Management

주제 폴더를 추가하거나 삭제할 때는 가능하면 CLI를 사용합니다.

### 7.1 Add Folder

```bash
python main.py --add-folder 09_New_Topic
```

동작:
- 폴더 생성
- `{FolderNameWithoutNumber}_meta.md` 생성
- `src/config.py`의 `TARGET_FOLDERS` 갱신
- 전체 `*_meta.md` 재생성

### 7.2 Remove Folder

```bash
python main.py --remove-folder 09_New_Topic
```

동작:
- `src/config.py`의 `TARGET_FOLDERS`에서 제거
- 폴더가 비어 있거나 generated meta 파일만 있으면 폴더 삭제
- PDF나 다른 파일이 있으면 폴더는 유지
- `index.md`에서 참조 중이면 중단

참조 중인 폴더를 강제로 등록 해제하려면:

```bash
python main.py --remove-folder 09_New_Topic --force
```

폴더 이름은 `NN_Name` 형식을 사용합니다.

```text
04_Evaluation
05_Systems
07_Agents
```

## 8. Metadata Files

### 8.1 `index.md`

`index.md`는 사람이 직접 관리하는 메인 인덱스입니다.

기본 컬럼:

```markdown
| ID | File Name | Full Title | Year | Folder | Link | Tags | Priority | Reading Note | Note |
|---|---|---|---:|---|---|---|---|---|---|
```

컬럼 의미:

| Column | Meaning |
|---|---|
| `ID` | 논문 고유 ID. 예: `TRN001`, `RET001`, `SYS001` |
| `File Name` | 로컬 PDF 파일명 |
| `Full Title` | 논문 전체 제목 |
| `Year` | 공식 게재 연도 또는 공개 연도 |
| `Folder` | 논문이 속한 주 폴더 |
| `Link` | 원문 인터넷 링크 |
| `Tags` | 보조 주제 |
| `Priority` | 읽기 우선순위 |
| `Reading Note` | 읽기 노트 링크 |
| `Note` | 기타 메모 |

CLI로 논문을 추가할 수 있습니다.

```bash
python main.py --add-paper
```

대화형 입력은 폴더를 먼저 고르고, 선택한 폴더의 prefix로 ID를 자동 제안합니다.

```text
Select Folder
[0] 00_Inbox
[1] 01_Survey
[2] 02_Training
[3] 03_Retrieval
[4] 04_Evaluation
[5] 05_Systems
[6] 06_ML
[7] 07_Agents
[8] 08_Domain
[99] Add New Folder
```

```text
ID: TRN003
```

`Priority`는 번호로 선택합니다.

```text
Priority
[1] Low
[2] Medium
[3] High
```

비대화식 예:

```bash
python main.py --add-paper --id TRN003 --file-name 2026_Example.pdf --title "Example Paper" --year 2026 --folder 02_Training --link https://example.com
```

논문 삭제:

```bash
python main.py --del-paper TRN003
```

ID 없이 실행하면 폴더를 먼저 선택한 뒤 해당 폴더의 논문 중에서 삭제할 항목을 고릅니다.

```bash
python main.py --del-paper
```

### 8.2 Folder Metadata

`*_meta.md`는 각 폴더의 논문 목록을 빠르게 보기 위한 자동 생성 파일입니다.

규칙:
- 각 주제 폴더에는 `*_meta.md`를 하나씩 둡니다.
- 예: `02_Training/Training_meta.md`, `05_Systems/Systems_meta.md`
- `*_meta.md`는 직접 수정하지 않습니다.
- `index.md`의 `Link`가 있으면 markdown 링크로 표시됩니다.
- `Link`가 비어 있거나 `-`, `tbd`, `none`, `링크_추가`이면 텍스트만 표시됩니다.

## 9. Notes and Ideas

### 9.1 Reading Notes

논문별 읽기 노트는 [`99_Meta/reading_notes/`](reading_notes/) 아래에 작성합니다.

파일명은 `ID_ShortName.md` 형식을 사용합니다.

```text
TRN001_LoRA.md
SYS001_MultiDocFusion.md
AGT001_NPP_LLM_Agent_Operation.md
```

기본 구조:

```markdown
# PAPER_ID - SHORT_NAME

> Metadata: see `../../index.md`

## Summary
-

## Key Idea
-

## Contribution
-

## Note
-
```

### 9.2 Experiment Ideas

실험 아이디어는 [`99_Meta/experiment_ideas/`](experiment_ideas/) 아래에 작성합니다.

파일명은 `EXP번호_짧은제목.md` 형식을 사용합니다.

```text
EXP001_LoRA_vs_SFT_for_NPP_QA.md
EXP002_Hierarchical_Chunking_for_NPP_Guidelines.md
```

기본 구조:

```markdown
# EXP000 - Title

## 1. Related Papers
-

## 2. Motivation
-

## 3. Idea
-

## 4. Next Step
-
```

## 10. Git Policy

PDF 파일은 GitHub에 올리지 않습니다.

`.gitignore`에서 PDF와 OS/캐시 파일을 제외합니다.

```text
*.pdf
.DS_Store
Thumbs.db
__pycache__/
*.py[cod]
```

GitHub에는 다음을 중심으로 관리합니다.

- `index.md`
- 각 폴더의 `*_meta.md`
- `99_Meta/guide.md`
- `99_Meta/reading_notes/`
- `99_Meta/experiment_ideas/`
- `src/`
- `main.py`

## 11. Summary

- `index.md`가 단일 원본입니다.
- `*_meta.md`는 자동 생성 파일입니다.
- PDF는 로컬에만 보관합니다.
- 논문은 하나의 주 폴더에만 둡니다.
- 폴더는 주 기여 기준으로 고릅니다.
- 겹치는 주제는 `Tags`로 관리합니다.
- 폴더는 넓은 범주를 우선 사용하고, 필요할 때만 추가합니다.
