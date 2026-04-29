# AI Paper Archive

AI/ML 논문의 공개 링크, 분류, 읽기 노트, 실험 아이디어를 관리하는 개인 논문 아카이브입니다.

PDF 파일은 로컬에만 보관하고 Git에서는 제외합니다. GitHub에는 논문 메타데이터, 공개 링크, 읽기 노트, 실험 아이디어, 자동화 스크립트만 올립니다.

자세한 운영 규칙은 [`99_Meta/guide.md`](99_Meta/guide.md)에 정리되어 있습니다.

## Structure

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

| Folder | Purpose |
|---|---|
| `00_Inbox` | 아직 분류하지 않은 논문 |
| `01_Survey` | Survey, review, taxonomy 논문 |
| `02_Training` | Fine-tuning, PEFT, instruction tuning, adaptation |
| `03_Retrieval` | Search, retrieval, RAG, reranking |
| `04_Evaluation` | Benchmark, metric, dataset, evaluation protocol |
| `05_Systems` | Pipeline, workflow, document processing, data generation system |
| `06_ML` | Machine learning methods, model architectures, baseline models |
| `07_Agents` | LLM agents, tool use, planning |
| `08_Domain` | Nuclear, industrial, medical, service 등 도메인 적용 |
| `99_Meta` | Guide, reading notes, experiment ideas |

## Metadata

전체 논문 목록의 원본은 [`index.md`](index.md)입니다.

각 주제 폴더에는 GitHub에서 빠르게 확인할 수 있는 `*_meta.md` 파일이 자동 생성됩니다. `*_meta.md`는 직접 수정하지 않고, `index.md`를 수정한 뒤 스크립트로 다시 생성합니다.

## Usage

자주 쓰는 명령은 다음과 같습니다.

| Task | Command |
|---|---|
| 인덱스 검사 | `python main.py --check` |
| 폴더별 메타 파일 재생성 | `python main.py` |
| 새 논문 추가 | `python main.py --add-paper` |
| 논문 삭제 | `python main.py --del-paper` |
| 주제 폴더 추가 | `python main.py --add-folder {NN_Folder_Name}` |
| 주제 폴더 삭제 | `python main.py --remove-folder {NN_Folder_Name}` |

### Quick Start

```bash
python main.py --check
python main.py
```

새 논문을 터미널 입력으로 추가합니다.

```bash
python main.py --add-paper
```

실행하면 먼저 폴더를 번호로 선택합니다. 선택한 폴더에 맞춰 ID가 자동으로 제안되고, priority는 `Low`, `Medium`, `High` 중에서 고릅니다.

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

ID: TRN003

Priority
[1] Low
[2] Medium
[3] High
```

한 줄 명령으로 추가할 수도 있습니다.

```bash
python main.py --add-paper --id TRN003 --file-name 2026_Example.pdf --title "Example Paper" --year 2026 --folder 02_Training --link https://example.com
```

등록한 논문을 삭제하려면 ID를 지정합니다.

```bash
python main.py --del-paper TRN003
```

ID 없이 실행하면 폴더를 먼저 고른 뒤, 해당 폴더의 논문 중에서 삭제할 항목을 선택합니다.

```bash
python main.py --del-paper
```

## Main Files

| Path | Purpose |
|---|---|
| [`index.md`](index.md) | 전체 논문 목록을 관리하는 메인 인덱스 |
| [`99_Meta/guide.md`](99_Meta/guide.md) | 저장소 관리 규칙과 분류 기준 |
| [`99_Meta/reading_notes/`](99_Meta/reading_notes/) | 논문별 읽기 노트 |
| [`99_Meta/experiment_ideas/`](99_Meta/experiment_ideas/) | 실험 아이디어 메모 |
| [`src/`](src/) | 폴더별 `*_meta.md` 자동 생성 스크립트 |

## Notes

- PDF 파일은 `.gitignore`로 Git에서 제외합니다.
- 각 폴더의 `*_meta.md`는 [`index.md`](index.md)를 기준으로 자동 생성합니다.
- 폴더는 논문의 주 기여를 기준으로 하나만 선택하고, 겹치는 성격은 `Tags`에 기록합니다.
- 자세한 분류 기준은 [Guide 6. Paper Intake and Classification](99_Meta/guide.md#6-paper-intake-and-classification)을 참고합니다.
