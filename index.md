# Paper Index

논문 PDF의 파일명, 원제, 공개 링크, 분류, 태그, 우선순위, 읽기 노트 링크를 관리하는 인덱스

## Field Guide

| Field | Meaning |
|---|---|
| `ID` | 폴더 prefix와 번호를 조합한 관리 ID |
| `File Name` | 실제 PDF 파일명 |
| `Full Title` | 논문 원제 |
| `Year` | 게재 또는 공개 연도 |
| `Folder` | PDF가 들어 있는 주 폴더 |
| `Link` | arXiv, ACL Anthology, DOI, publisher page 등 원문 인터넷 링크 |
| `Tags` | 보조 주제, 방법론, 데이터, 도메인 |
| `Priority` | High, Medium, Low 등 읽기 우선순위 |
| `Reading Note` | 개별 읽기 노트 파일 링크 |
| `Note` | 연도 기준, 파일명 변경 이유, 특이사항 |

## ID Prefix

| Prefix | Meaning |
|---|---|
| `FT` | Fine Tuning |
| `INB` | Inbox |
| `RAG` | Retrieval-Augmented Generation |
| `ML` | Machine Learning |
| `APP` | Application |
| `MD` | Models |

## Index

| ID | File Name | Full Title | Year | Folder | Link | Tags | Priority | Reading Note | Note |
|---|---|---|---:|---|---|---|---|---|---|
| INB001 | `Large Language Models as Realistic Microservice Trace Generators.pdf` | Large Language Models as Realistic Microservice Trace Generators | 2025 | `00_Inbox` | https://aclanthology.org/2025.emnlp-main.4/ | LLM, Trace generation, Microservice | Low | [note](./99_Meta/reading_notes/INB001_Microservice_Trace_Generators.md) | 분류 전 Inbox 항목. |
| FT001 | `2022_LoRA_ICLR.pdf` | LoRA: Low-Rank Adaptation of Large Language Models | 2022 | `01_Fine_Tuning` | https://arxiv.org/abs/2106.09685 | LoRA, PEFT, Fine-tuning | High | [note](./99_Meta/reading_notes/FT001_LoRA.md) | arXiv first posted in 2021. |
| FT002 | `2025_SFT_LoRA_ICL_DataScarce.pdf` | A Comparative Analysis of LLM Adaptation: SFT, LoRA, and ICL in Data-Scarce Scenarios | 2025 | `01_Fine_Tuning` | https://arxiv.org/abs/2511.00130 | SFT, LoRA, ICL, Data-scarce adaptation | High | [note](./99_Meta/reading_notes/FT002_SFT_LoRA_ICL_DataScarce.md) |  |
| RAG001 | `2025_Ko_LongRAG.pdf` | A Korean Long-Context RAG Benchmark Built with a Retrieval-Free Approach | 2025 | `02_RAG` | https://aclanthology.org/2025.findings-emnlp.938/ | Korean, Long-context, RAG, Benchmark | High | [note](./99_Meta/reading_notes/RAG001_Ko_LongRAG.md) |  |
| RAG002 | `2025_MultiDocFusion.pdf` | Hierarchical and Multimodal Chunking Pipeline for Enhanced RAG on Long Industrial Documents | 2025 | `02_RAG` | https://aclanthology.org/2025.emnlp-main.1062/ | Chunking, Multimodal, Industrial documents, RAG | High | [note](./99_Meta/reading_notes/RAG002_MultiDocFusion.md) |  |
| RAG003 | `2026_NLP_OLC_Search_Methodology.pdf` | 자연어처리기반 운전제한조건 검색 방법론 | 2026 | `02_RAG` | https://koasas.kaist.ac.kr/handle/10203/308660 | NLP, Search, OLC, Nuclear operation | Medium | [note](./99_Meta/reading_notes/RAG003_NLP_OLC_Search_Methodology.md) | 초록은 OCR 또는 수동 확인 필요. |
| ML001 | `2023_GBM_Benchmark.pdf` | Benchmarking State-of-the-Art Gradient Boosting Algorithms for Classification | 2023 | `03_ML` | https://arxiv.org/abs/2305.17094 | GBM, XGBoost, LightGBM, CatBoost, Classification | Medium | [note](./99_Meta/reading_notes/ML001_GBM_Benchmark.md) |  |
| APP001 | `2022_NPP_RL_HeatUp_Control.pdf` | Control Automation in the Heat-Up Mode of a Nuclear Power Plant using Reinforcement Learning | 2022 | `04_Application` | https://www.sciencedirect.com/science/article/abs/pii/S0149197021004595 | NPP, Reinforcement learning, Control automation | Medium | [note](./99_Meta/reading_notes/APP001_NPP_RL_HeatUp_Control.md) |  |
| APP002 | `2024_NPP_Safety_Event_Classification_LLM.pdf` | Classification of Safety Events at Nuclear Sites using Large Language Models | 2024 | `04_Application` | https://arxiv.org/abs/2409.00091 | NPP, LLM, Safety event classification | High | [note](./99_Meta/reading_notes/APP002_NPP_Safety_Event_Classification_LLM.md) |  |
| APP003 | `2025_NPP_Human_Error_Detection_AI.pdf` | Enhancing Safety of Nuclear Power Plant by Human Error Detection and Identification through AI Techniques | 2025 | `04_Application` | https://www.sciencedirect.com/science/article/pii/S2590123025026854 | NPP, Human error, Fault detection, LightGBM | Medium | [note](./99_Meta/reading_notes/APP003_NPP_Human_Error_Detection_AI.md) |  |
| APP004 | `2025_NPP_LLM_Agent_Operation.pdf` | Large Language Model Agent for Nuclear Reactor Operation Assistance | 2025 | `04_Application` | https://www.sciencedirect.com/science/article/pii/S1738573325004103 | NPP, LLM Agent, RAG, Tool use, Operation support | High | [note](./99_Meta/reading_notes/APP004_NPP_LLM_Agent_Operation.md) |  |
| MD001 | `2019_DeepONet.pdf` | DeepONet: Learning nonlinear operators for identifying differential equations based on the universal approximation theorem of operators | 2019 | `05_Models` | https://arxiv.org/abs/1910.03193 | DeepONet, Neural operator, Operator learning | Low | [note](./99_Meta/reading_notes/MD001_DeepONet.md) | arXiv first posted in 2019. |
| MD002 | `2017_Transformer.pdf` | Attentin is all you need | 2017 | `05_Models` | https://arxiv.org/abs/1706.03762 | Attention, Transformer | Low | [note](./99_Meta/reading_notes/MD001_DeepONet.md) | NeurIPS 2017 |

