# Papers Meta

이 저장소는 `papers/` 아래의 논문 PDF와 메타 문서를 관리하기 위한 작업 공간이다.

PDF 자체는 주제별 폴더에 두고, 아직 분류하지 않은 논문은 `00_Inbox`에 임시 보관한다. 논문 목록, 읽기 메모, 실험 아이디어, 관리 규칙은 `99_Meta`에서 관리한다.

## Directory Structure

```text
papers/
├── 00_Inbox
│   └── paper_list.md
├── 01_Fine_Tuning
│   └── paper_list.md
├── 02_RAG
│   └── paper_list.md
├── 03_ML
│   └── paper_list.md
├── 04_Application
│   └── paper_list.md
├── 99_Meta
│   ├── meta_guide.md
│   ├── paper_index.md
│   ├── reading_notes/
│   │   └── _template.md
│   └── experiment_ideas/
│       └── _template.md
└── README.md
```

## Folder Rules

| Folder           | Purpose                                                                        |
| ---------------- | ------------------------------------------------------------------------------ |
| `00_Inbox`       | 아직 분류하지 않은 논문 PDF를 임시로 보관                                           |
| `01_Fine_Tuning` | SFT, LoRA, PEFT, ICL, instruction tuning 등 LLM 적응 방법                        |
| `02_RAG`         | retrieval, chunking, reranking, compression, long-context QA, RAG evaluation   |
| `03_ML`          | gradient boosting, classical ML, classifier, anomaly detection, baseline model |
| `04_Application` | NPP, industrial AI, domain application, operation support                      |
| `99_Meta`        | 논문 인덱스, 읽기 메모, 실험 아이디어, 관리 규칙                                     |


## Inbox Rule

00_Inbox는 새로 다운로드한 논문을 임시로 넣어두는 폴더이다.

새 논문은 먼저 00_Inbox/에 넣는다.
00_Inbox/ 안에서는 파일명을 꼭 정리하지 않아도 된다.
제목과 초록을 확인한 뒤 적절한 주제 폴더로 이동한다.
정식 폴더로 옮길 때는 Year_ShortName.pdf 규칙에 맞게 파일명을 수정한다.
이동한 논문은 99_Meta/paper_index.md에 등록한다.
00_Inbox/에는 장기 보관하지 않는다.


## Naming Rule

PDF 파일명은 짧고 일관되게 작성한다.

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

## Year Rule

- `Year`는 기본적으로 학회, 저널, 또는 공식 게재 연도를 사용한다.
- arXiv 최초 공개 연도와 공식 게재 연도가 다르면 `paper_index.md`의 `Note`에 기록한다.
- 정식 게재 정보가 없고 preprint만 있으면 arXiv 최초 공개 연도를 사용한다.

## Classification Rule

논문 PDF는 하나의 주 폴더에만 둔다.

여러 주제에 걸치는 논문은 다음 기준으로 분류한다.

1. 논문의 주된 목적을 기준으로 폴더를 고른다.
2. 보조 주제는 `paper_index.md`의 `Tags`에 기록한다.
3. 같은 PDF를 여러 폴더에 복사하지 않는다.

예를 들어 `Large Language Model Agent for Nuclear Reactor Operation Assistance`는 RAG와 agent를 모두 다루지만, 원전 운전 지원 응용이 중심이므로 `04_Application`에 둔다.


## Meta Files

| File | Purpose |
|---|---|
| `paper_index.md` | 전체 논문 목록, 원제, 연도, 태그, 우선순위, 읽기 노트 링크 관리 |
| `reading_notes/` | 논문별 개별 읽기 메모 작성 |
| `experiment_ideas/` | 실험 아이디어별 개별 메모 작성 |

## `paper_list.md` Rule

각 주제 폴더에는 GitHub에서 바로 확인할 수 있는 공개용 논문 목록인 `paper_list.md`를 둔다.

`paper_list.md`는 해당 폴더에 속한 논문들의 간단한 링크 목록이다. 자세한 메타데이터는 `papers/99_Meta/paper_index.md`에서 관리한다.

역할 구분은 다음과 같다.

| File | Role |
|---|---|
| `paper_list.md` | GitHub에서 빠르게 보는 폴더별 논문 링크 목록 |
| `papers/99_Meta/paper_index.md` | ID, 파일명, 원제, 연도, 태그, 우선순위, 읽기 노트 링크를 관리하는 전체 인덱스 |

작성 규칙:

- 각 주제 폴더마다 `paper_list.md`를 하나씩 둔다.
- 링크 텍스트는 `ID: ShortName` 또는 `ShortName` 형식으로 짧게 쓴다.
- 가능한 경우 arXiv, ACL Anthology, DOI, publisher page 등 공개 링크를 연결한다.
- 아직 분류하지 않은 논문은 `00_Inbox/paper_list.md`에 임시로 적는다.
- 정식 주제 폴더로 이동한 논문은 해당 폴더의 `paper_list.md`와 `papers/99_Meta/paper_index.md`를 함께 갱신한다.

## Current Policy Summary

- 폴더 구조는 얕게 유지한다.
- PDF 파일명은 짧고 검색하기 쉽게 유지한다.
- 논문은 하나의 주 폴더에만 둔다.
- 겹치는 주제는 태그로 관리한다.
- 논문이 많아져 검색이 불편해질 때만 하위 폴더를 추가한다.
