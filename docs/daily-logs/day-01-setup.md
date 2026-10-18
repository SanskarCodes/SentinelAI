# Day 01 — SentinelAI Project Initialization

**Project:** SentinelAI — Explainable & Uncertainty-Aware Malware Detection  
**Status:** Environment setup and dataset acquisition completed; extraction pending.

---

## 1. Objective

The objective of Day 1 was to establish the development environment, initialize the project structure, and acquire a benchmark dataset for building an ML-based malware detection system.

SentinelAI aims to investigate how machine learning models can detect malicious files while identifying unfamiliar samples for which their predictions may be unreliable.

## 2. Project Setup

### Development Environment

- **Operating System:** macOS
- **Language:** Python 3.11
- **IDE:** Visual Studio Code
- **Version Control:** Git
- **Environment Management:** Python virtual environment (`venv`)

### Libraries Installed

- NumPy
- Pandas
- Scikit-learn
- Matplotlib
- Seaborn
- Jupyter
- Joblib

The installation was verified through successful imports of NumPy, Pandas, and Scikit-learn.

## 3. Project Directory Structure

```text
SentinelAI/
├── data/
│   ├── raw/
│   └── processed/
├── docs/
│   └── daily-logs/
│       └── day-01-setup.md
├── notebooks/
├── reports/
├── src/
│   ├── data/
│   ├── models/
│   └── evaluation/
├── tests/
└── .venv/
```

The directory structure separates datasets, source code, experiments, documentation, and tests to support maintainability and reproducibility.

## 4. Dataset Acquisition

**Dataset:** EMBER 2018 — Feature Version 2

**Source:** [Elastic/EMBER GitHub Repository](https://github.com/elastic/ember)

**Downloaded archive:** `ember_dataset_2018_2.tar.bz2`

**Archive size:** Approximately 1.6 GB

The archive's compression integrity check completed without errors using `bzip2 -t`.

Initial inspection of the archive revealed files including:

- `train_features_*.jsonl`
- `test_features.jsonl`
- `ember_model_2018.txt`

These filenames indicate that the archive contains training and testing feature data, along with a model-related artifact. Their exact schemas and contents will be examined after extraction.

## 5. Technical Decisions

1. **Start with pre-extracted features:** Use structured numerical and categorical features rather than executing suspicious files.
2. **Establish a baseline first:** Train a conventional ML classifier before experimenting with neural networks and uncertainty estimation.
3. **Separate code and data:** Keep large datasets and generated model artifacts out of Git.
4. **Evaluate reliability:** Measure false positives, missed detections, and performance on appropriately held-out samples.
5. **Document experiments:** Maintain separate daily logs and record meaningful technical decisions.

## 6. Planned Project USP

SentinelAI will investigate whether an uncertainty-aware malware detector can identify unfamiliar samples and abstain from making potentially unreliable predictions.

The planned experiments will compare:

- Classical ML models against a PyTorch ANN.
- Standard classification against uncertainty-aware prediction.
- Performance on familiar samples versus held-out malware families.
- Detection performance against the additional workload created by referring uncertain samples for review.

These are planned experiments, not yet validated results.

## 7. Challenges and Learnings

- Configured a dedicated Python environment for the project.
- Verified the required data science libraries.
- Selected a public malware detection benchmark.
- Learned the importance of verifying downloaded archives before extraction.
- Planned a reproducible project structure before beginning model development.

## 8. Next Steps — Day 2

- Extract and inspect the EMBER dataset.
- Understand the JSONL format and feature schema.
- Identify labels and missing or invalid records.
- Analyze the dataset's class distribution.
- Design a leakage-aware training and evaluation strategy.

## 9. Current Status

| Task | Status |
|---|---|
| Python environment setup | Completed |
| Dependency installation | Completed |
| Project structure | Completed |
| Dataset download | Completed |
| Archive integrity check | Passed |
| Dataset extraction | Pending |
| Exploratory data analysis | Pending |
| Baseline model | Pending |

---

**Note:** No malware executable has been intentionally executed. The initial development phase uses benchmark feature data for defensive ML research.