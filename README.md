# AI_Paper_Review

논문 링크, 주제별 폴더, 읽기 노트, 실험 아이디어를 관리하기 위한 저장소입니다.

PDF 파일은 로컬에만 보관하고 Git에서는 제외하였습니다.  
GitHub 저장소에는 논문 메타데이터, 공개 링크, 읽기 노트, 실험 아이디어, 자동화 스크립트만 관리합니다.

자세한 운영 규칙은 가이드 문서에 정리되어 있습니다.

> [`99_Meta/guide.md`](99_Meta/guide.md)

## Structure

```text
.
├── 00_Inbox/
├── 01_Fine_Tuning/
├── 02_RAG/
├── 03_ML/
├── 04_Application/
├── 05_Models/
├── 99_Meta/
├── src/
├── index.md
├── main.py
└── README.md
```

자세한 폴더 설명은 [Guide 2. Repository Structure](99_Meta/guide.md#2-repository-structure)를 참고합니다.

## Folder Metadata

각 주제 폴더에는 GitHub에서 빠르게 확인할 수 있는 `*_meta.md` 파일이 있으며 전체 논문 목록의 원본은 다음 파일에서 확인할 수 있습니다 :

```text
index.md
```

논문을 추가하거나 수정할 때는 먼저 `index.md`를 수정한 뒤, 스크립트를 실행해 각 폴더의 `*_meta.md`를 다시 생성하면 됩니다.

메타데이터 파일의 역할은 [Guide 7. Metadata Files](99_Meta/guide.md#7-metadata-files)를 참고합니다.

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

### Codespaces Quick Start

GitHub Codespaces 또는 로컬 터미널에서 다음 순서로 실행합니다.

```bash
python main.py --check
python main.py
```

새 논문을 터미널 입력으로 추가하려면 다음 명령어를 사용합니다.

```bash
python main.py --add-paper
```

실행하면 먼저 폴더를 번호로 선택합니다. 선택한 폴더에 맞춰 ID가 자동으로 정해지고, priority는 `Low`, `Medium`, `High` 중에서 고릅니다.

```text
Select Folder
[0] 00_Inbox
[1] 01_Fine_Tuning
[2] 02_RAG
[99] Add New Folder

ID: FT003

Priority
[1] Low
[2] Medium
[3] High
```

새 폴더가 필요하면 폴더 선택 화면에서 `[99] Add New Folder`를 고르면 됩니다.

한 줄 명령으로 추가할 수도 있습니다.

```bash
python main.py --add-paper --id {FT003} --file-name {2026_Example.pdf} --title "Example Paper" --year {2026} --folder {01_Fine_Tuning} --link {https://example.com}
```

등록한 논문을 삭제하려면 ID를 지정합니다.

```bash
python main.py --del-paper {FT003}
```

ID 없이 실행하면 폴더를 먼저 고른 뒤, 해당 폴더의 논문 중에서 삭제할 항목을 선택합니다.

```bash
python main.py --del-paper
```

새 주제 폴더를 만들고 싶으면 다음처럼 실행합니다.

```bash
python main.py --add-folder {06_Agents}
```

기본 작업 순서는 [Guide 4. Standard Workflow](99_Meta/guide.md#4-standard-workflow)를 참고합니다. 새 논문 추가는 [Guide 7. Metadata Files](99_Meta/guide.md#7-metadata-files), 폴더 추가/삭제는 [Guide 5. Folder Management](99_Meta/guide.md#5-folder-management)를 참고합니다.

## Main Files

| Path                        | Purpose                    |
| --------------------------- | -------------------------- |
| [`index.md`](index.md)            | 전체 논문 목록을 관리하는 메인 인덱스      |
| [`99_Meta/guide.md`](99_Meta/guide.md)     | 저장소 관리 규칙과 작업 흐름           |
| [`99_Meta/reading_notes/`](99_Meta/reading_notes/)    | 논문별 읽기 노트 템플릿 및 메모         |
| [`99_Meta/experiment_ideas/`](99_Meta/experiment_ideas/) | 실험 아이디어 템플릿 및 메모           |
| [`src/`](src/)                      | 폴더별 `*_meta.md` 자동 생성 스크립트 |


## Notes
- PDF 파일은 `.gitignore`로 Git에서 제외합니다.
- 각 폴더의 `*_meta.md`는 [`index.md`](index.md)를 기준으로 자동 생성합니다.
- 논문 분류 기준은 [Guide 6. Paper Intake and Classification](99_Meta/guide.md#6-paper-intake-and-classification)를 참고합니다.
- Git 관리 정책은 [Guide 9. Git Policy](99_Meta/guide.md#9-git-policy)를 참고합니다.
