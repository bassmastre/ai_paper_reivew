# Guide

이 문서는 `AI_Paper_Review` 저장소의 내부 관리 규칙을 정리한 문서입니다.

방문자용 개요는 [`README.md`](../README.md)를 참고합니다.

## Table of Contents

- [1. Overview](#1-overview)
- [2. Repository Structure](#2-repository-structure)
- [3. Source of Truth](#3-source-of-truth)
- [4. Standard Workflow](#4-standard-workflow)
- [5. Folder Management](#5-folder-management)
  - [5.1 Add Folder](#51-add-folder)
  - [5.2 Remove Folder](#52-remove-folder)
  - [5.3 Documentation Checklist](#53-documentation-checklist)
- [6. Paper Intake and Classification](#6-paper-intake-and-classification)
  - [6.1 Inbox Rule](#61-inbox-rule)
  - [6.2 Naming Rule](#62-naming-rule)
  - [6.3 Year Rule](#63-year-rule)
  - [6.4 Classification Rule](#64-classification-rule)
- [7. Metadata Files](#7-metadata-files)
  - [7.1 `index.md` Rule](#71-indexmd-rule)
  - [7.2 Folder Metadata Rule](#72-folder-metadata-rule)
- [8. Notes and Ideas](#8-notes-and-ideas)
  - [8.1 Reading Notes](#81-reading-notes)
  - [8.2 Experiment Ideas](#82-experiment-ideas)
- [9. Git Policy](#9-git-policy)
- [10. Current Policy Summary](#10-current-policy-summary)

## 1. Overview

이 저장소는 논문 PDF 자체보다 논문 메타데이터, 공개 링크, 읽기 노트, 실험 아이디어, 자동화 스크립트를 관리하는 용도입니다.

PDF 파일은 로컬에만 보관하고 GitHub에는 업로드하지 않습니다.

## 2. Repository Structure

```text
.
├── 00_Inbox/
│   └── Inbox_meta.md
├── 01_Fine_Tuning/
│   └── Fine_Tuning_meta.md
├── 02_RAG/
│   └── RAG_meta.md
├── 03_ML/
│   └── ML_meta.md
├── 04_Application/
│   └── Application_meta.md
├── 05_Models/
│   └── Models_meta.md
├── 99_Meta/
│   ├── guide.md
│   ├── reading_notes/
│   │   └── _template.md
│   └── experiment_ideas/
│       └── _template.md
├── src/
├── index.md
├── main.py
└── README.md
```

| Folder | Purpose |
|---|---|
| [`00_Inbox`](../00_Inbox/) | 아직 분류하지 않은 논문을 임시로 보관 |
| [`01_Fine_Tuning`](../01_Fine_Tuning/) | SFT, LoRA, PEFT, ICL, instruction tuning 등 LLM 적응 방법 |
| [`02_RAG`](../02_RAG/) | retrieval, chunking, reranking, compression, long-context QA, RAG evaluation |
| [`03_ML`](../03_ML/) | gradient boosting, classical ML, classifier, anomaly detection, baseline model |
| [`04_Application`](../04_Application/) | NPP, industrial AI, domain application, operation support |
| [`05_Models`](../05_Models/) | Deep learning models, neural network architectures, foundation model components, model design, and generative model methods |
| [`99_Meta`](../99_Meta/) | 관리 규칙, 읽기 노트 템플릿, 실험 아이디어 템플릿 |

## 3. Source of Truth

[`index.md`](../index.md)가 전체 논문 목록의 단일 원본입니다.

각 폴더의 `*_meta.md`는 [`index.md`](../index.md)를 기준으로 자동 생성됩니다. 따라서 특별한 이유가 없으면 각 폴더의 `*_meta.md`는 직접 수정하지 않습니다.

## 4. Standard Workflow

논문을 추가하거나 수정할 때는 다음 순서를 따릅니다.

1. [`index.md`](../index.md)에 논문 정보를 추가하거나 수정합니다.
2. 인덱스 형식을 확인합니다.

```bash
python main.py --check
```

3. 각 폴더의 `*_meta.md`를 생성하거나 갱신합니다.

```bash
python main.py
```

4. 새 논문을 터미널 입력으로 추가하려면 다음 명령어를 사용할 수 있습니다.

```bash
python main.py --add-paper
```

5. 생성된 `*_meta.md` 파일을 확인합니다.
6. 변경 내용을 Git에 반영합니다.

```bash
git add .
git commit -m "Update index"
git push
```

## 5. Folder Management

주제 폴더를 추가하거나 삭제할 때는 `src/config.py`를 직접 수정하지 않고 CLI를 사용합니다.

### 5.1 Add Folder

```bash
python main.py --add-folder 06_Agents
```

동작:

- `06_Agents/` 폴더를 생성합니다.
- `06_Agents/Agents_meta.md`를 생성합니다.
- `src/config.py`의 `TARGET_FOLDERS`에 새 폴더를 등록합니다.
- 전체 `*_meta.md` 파일을 다시 생성합니다.

### 5.2 Remove Folder

```bash
python main.py --remove-folder 06_Agents
```

동작:

- `src/config.py`의 `TARGET_FOLDERS`에서 폴더를 제거합니다.
- 폴더가 비어 있거나 `*_meta.md`만 있으면 실제 폴더도 삭제합니다.
- 폴더 안에 다른 파일이 있으면 실제 폴더는 삭제하지 않습니다.
- `index.md`에서 해당 폴더를 참조 중이면 기본적으로 중단합니다.

참조 중인 폴더를 강제로 등록 해제하려면 다음 옵션을 사용합니다.

```bash
python main.py --remove-folder 06_Agents --force
```

폴더 이름은 `NN_Name` 형식을 사용합니다.

```text
05_Models
06_Agents
07_Evaluation
```

### 5.3 Documentation Checklist

폴더를 추가하거나 삭제하면 CLI가 `src/config.py`와 `*_meta.md`는 자동으로 갱신합니다. 다만 설명 문서인 `99_Meta/guide.md`와 방문자용 `README.md`의 구조 예시는 사람이 확인해야 합니다.

폴더를 추가한 경우:

1. `README.md`의 `Structure` 목록에 새 폴더를 추가합니다.
2. 이 문서의 `Repository Structure` 목록에 새 폴더와 `{NN_를 제외한 폴더명}_meta.md`를 추가합니다.
3. 이 문서의 폴더 설명 표에 새 폴더의 목적을 한 줄로 설명합니다.
4. 이 문서의 `Git Policy` 섹션에서 관리 대상 `*_meta.md` 목록에 새 폴더를 추가합니다.
5. 필요하면 `index.md`의 `ID Prefix` 또는 태그 규칙을 보완합니다.

폴더를 삭제한 경우:

1. `README.md`의 `Structure` 목록에서 삭제한 폴더를 제거합니다.
2. 이 문서의 `Repository Structure` 목록에서 삭제한 폴더를 제거합니다.
3. 이 문서의 폴더 설명 표에서 삭제한 폴더 설명을 제거합니다.
4. 이 문서의 `Git Policy` 섹션에서 삭제한 폴더의 `*_meta.md` 항목을 제거합니다.
5. `index.md`에 삭제한 폴더를 참조하는 행이 남아 있지 않은지 확인합니다.

## 6. Paper Intake and Classification

### 6.1 Inbox Rule

[`00_Inbox`](../00_Inbox/)는 새로 다운로드했거나 아직 분류하지 않은 논문을 임시로 두는 폴더입니다.

- 새 논문은 먼저 [`00_Inbox`](../00_Inbox/)에 둡니다.
- [`00_Inbox`](../00_Inbox/) 안의 파일명은 최종 파일명 규칙을 따르지 않아도 됩니다.
- 제목과 초록을 확인한 뒤 가장 적절한 주제 폴더로 이동합니다.
- 정식 주제 폴더로 이동할 때는 `Year_ShortName.pdf` 규칙에 맞게 파일명을 수정합니다.
- 이동한 논문은 [`index.md`](../index.md)에 등록합니다.
- [`00_Inbox`](../00_Inbox/)는 장기 보관용으로 사용하지 않습니다.

### 6.2 Naming Rule

PDF 파일명은 짧고 일관되게 작성합니다.

```text
Year_ShortName.pdf
```

예시:

```text
2022_LoRA_ICLR.pdf
2025_Ko_LongRAG.pdf
2025_MultiDocFusion.pdf
2024_NPP_Safety_Event_Classification_LLM.pdf
```

### 6.3 Year Rule

- `Year`는 기본적으로 학회, 저널, 또는 공식 게재 연도를 사용합니다.
- arXiv 최초 공개 연도와 공식 게재 연도가 다르면 [`index.md`](../index.md)의 `Note`에 기록합니다.
- 정식 게재 정보가 없고 preprint만 존재하는 경우, 최초 공개 preprint 연도를 사용합니다.

### 6.4 Classification Rule

논문 PDF는 하나의 주 폴더에만 둡니다.

여러 주제에 걸치는 논문은 다음 기준으로 분류합니다.

1. 논문을 읽는 주된 목적을 기준으로 폴더를 선택합니다.
2. 보조 주제는 `index.md`의 `Tags`에 기록합니다.
3. 같은 PDF를 여러 폴더에 복사하지 않습니다.

예시:

`Large Language Model Agent for Nuclear Reactor Operation Assistance`는 RAG와 agent를 모두 다루지만, 원전 운전 지원 응용 사례로 읽는 목적이 크므로 `04_Application`에 둡니다.

## 7. Metadata Files

### 7.1 `index.md` Rule

`index.md`는 사람이 직접 수정하는 메인 인덱스입니다.

기본 컬럼은 다음 형식을 따릅니다.

```markdown
| ID | File Name | Full Title | Year | Folder | Link | Tags | Priority | Reading Note | Note |
|---|---|---|---:|---|---|---|---|---|---|
```

각 컬럼의 의미는 다음과 같습니다.

| Column | Meaning |
|---|---|
| `ID` | 논문 고유 ID. 예: `FT001`, `RAG001`, `ML001`, `APP001` |
| `File Name` | 로컬 PDF 파일명 |
| `Full Title` | 논문 전체 제목 |
| `Year` | 공식 게재 연도 또는 preprint 공개 연도 |
| `Folder` | 논문이 속한 주 폴더 |
| `Link` | arXiv, ACL Anthology, DOI, publisher page 등 원문 인터넷 링크 |
| `Tags` | 논문의 보조 주제 |
| `Priority` | 읽기 또는 적용 우선순위 |
| `Reading Note` | 읽기 노트 링크 |
| `Note` | arXiv 선공개 연도, 읽기 상태, 기타 메모 |

예시:

```markdown
| FT001 | `2022_LoRA_ICLR.pdf` | LoRA: Low-Rank Adaptation of Large Language Models | 2022 | `01_Fine_Tuning` | https://arxiv.org/abs/2106.09685 | LoRA, PEFT, Fine-tuning | High | [note](./99_Meta/reading_notes/FT001_LoRA.md) | arXiv first posted in 2021. |
```

CLI로 새 행을 추가할 수도 있습니다.

```bash
python main.py --add-paper
```

대화형 모드에서는 먼저 폴더를 선택합니다.

```text
Select Folder
[0] 00_Inbox
[1] 01_Fine_Tuning
[2] 02_RAG
[3] 03_ML
[4] 04_Application
[5] 05_Models
[99] Add New Folder
```

폴더를 고르면 해당 폴더의 prefix를 기준으로 다음 ID가 자동으로 정해집니다.

```text
ID: FT003
```

해당 폴더에 기존 ID prefix가 없으면 기본 제안 ID가 표시되고, 필요하면 직접 수정할 수 있습니다.

새 폴더가 필요하면 폴더 선택 화면에서 `[99] Add New Folder`를 선택합니다. 이 경우 `NN_Name` 형식의 폴더명을 입력하면 폴더 등록과 `*_meta.md` 생성이 함께 처리됩니다.

`Priority`는 번호로 선택합니다.

```text
Priority
[1] Low
[2] Medium
[3] High
```

비대화식으로 입력하려면 필요한 값을 옵션으로 넘깁니다.

```bash
python main.py --add-paper --id FT003 --file-name 2026_Example.pdf --title "Example Paper" --year 2026 --folder 01_Fine_Tuning --link https://example.com
```

`--add-paper`는 `index.md`에 새 행을 추가하고, 읽기 노트 파일이 없으면 기본 템플릿으로 생성한 뒤, 각 폴더의 `*_meta.md`를 다시 생성합니다.

논문을 인덱스에서 삭제하려면 다음 명령을 사용합니다.

```bash
python main.py --del-paper FT003
```

ID를 생략하면 삭제할 논문을 번호로 선택할 수 있습니다.

```bash
python main.py --del-paper
```

ID를 생략한 경우에는 폴더를 먼저 선택하고, 그 폴더에 들어 있는 논문 목록 중에서 삭제할 항목을 고릅니다.

`--del-paper`는 `index.md`의 해당 행을 삭제하고, 각 폴더의 `*_meta.md`를 다시 생성합니다. 이미 만들어진 읽기 노트 파일은 자동 삭제하지 않습니다.

### 7.2 Folder Metadata Rule

`*_meta.md`는 각 주제 폴더의 논문을 빠르게 확인하기 위한 링크 목록입니다. 전체 메타데이터는 [`index.md`](../index.md)에서만 관리합니다.

- 각 주제 폴더에는 `{NN_를 제외한 폴더명}_meta.md`를 하나씩 둡니다.
- 예: `01_Fine_Tuning/Fine_Tuning_meta.md`, `02_RAG/RAG_meta.md`
- `*_meta.md`는 직접 수정하지 않고 스크립트로 생성합니다.
- 표시 텍스트는 `ID: FileNameWithoutExtension` 형식을 사용합니다.
- `index.md`의 `Link` 컬럼에 원문 인터넷 링크를 입력하면 `*_meta.md`에는 자동으로 markdown 링크가 생성됩니다.
- `Link`가 비어 있거나 `-`, `tbd`, `none`, `링크_추가`이면 링크 없이 텍스트만 생성됩니다.
- 분류 전 논문은 [`00_Inbox/Inbox_meta.md`](../00_Inbox/Inbox_meta.md)에 표시합니다.
- 정식 주제 폴더로 이동한 논문은 [`index.md`](../index.md)에 등록한 뒤, 스크립트로 `*_meta.md`를 갱신합니다.

## 8. Notes and Ideas

### 8.1 Reading Notes

논문별 읽기 노트는 [`99_Meta/reading_notes/`](reading_notes/) 아래에 작성합니다.

파일명은 [`index.md`](../index.md)의 ID와 short name을 사용합니다.

```text
FT001_LoRA.md
RAG002_MultiDocFusion.md
APP004_NPP_LLM_Agent_Operation.md
```

읽기 노트는 최소 구조만 유지합니다.

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

### 8.2 Experiment Ideas

실험 아이디어는 [`99_Meta/experiment_ideas/`](experiment_ideas/) 아래에 작성합니다.

파일명은 `EXP번호_핵심제목.md` 형식을 사용합니다.

```text
EXP001_LoRA_vs_SFT_for_NPP_QA.md
EXP002_Hierarchical_Chunking_for_NPP_Guidelines.md
```

실험 아이디어는 다음 최소 구조를 따릅니다.

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

## 9. Git Policy

PDF 파일은 GitHub에 업로드하지 않습니다.

`.gitignore`에서 PDF 파일을 제외합니다.

```text
*.pdf
.DS_Store
Thumbs.db
```

GitHub에는 다음 파일들을 중심으로 관리합니다.

- [`index.md`](../index.md)
- 각 폴더의 `*_meta.md`
  - `00_Inbox/Inbox_meta.md`
  - `01_Fine_Tuning/Fine_Tuning_meta.md`
  - `02_RAG/RAG_meta.md`
  - `03_ML/ML_meta.md`
  - `04_Application/Application_meta.md`
  - `05_Models/Models_meta.md`
- `99_Meta/guide.md`
- `99_Meta/reading_notes/`
- `99_Meta/experiment_ideas/`
- `src/`
- `main.py`

## 10. Current Policy Summary

- [`index.md`](../index.md)를 단일 원본으로 관리합니다.
- 각 폴더의 `*_meta.md`는 자동 생성합니다.
- PDF 파일은 로컬에만 보관하고 GitHub에는 올리지 않습니다.
- 폴더 구조는 얕게 유지합니다.
- 논문은 하나의 주 폴더에만 둡니다.
- 겹치는 주제는 `Tags`로 관리합니다.
- 논문이 많아져 탐색이 불편해질 때만 하위 폴더를 추가합니다.
