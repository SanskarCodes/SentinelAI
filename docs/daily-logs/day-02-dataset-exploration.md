# Day 2 — Dataset Exploration

## Objective
Inspect the EMBER 2018 dataset, understand its structure, and verify label distributions before building the malware detection pipeline.

## Work Completed
- Inspected JSONL feature records using Python.
- Identified feature fields such as `general`, `header`, `section`, `imports`, `exports`, `strings`, `histogram`, and `byteentropy`.
- Implemented streaming label inspection with Python's `json` and `Counter` to avoid loading entire dataset shards into memory.
- Inspected all six training shards and the test dataset.

## Dataset Summary

### Training Dataset
- Total records: 800,000
- Benign (`label = 0`): 300,000
- Malicious (`label = 1`): 300,000
- Unlabeled (`label = -1`): 200,000

### Test Dataset
- Total records: 200,000
- Benign (`label = 0`): 100,000
- Malicious (`label = 1`): 100,000

## Key Observations
- Training data contains labeled and unlabeled samples.
- The first training shard contains only benign samples; shard-level distributions are not representative of the full dataset.
- Unlabeled samples will be excluded from supervised training.
- The test dataset will remain separate until final model evaluation.
- Dataset files are stored locally and excluded from Git tracking.

## Technical Decisions
- Use streaming JSONL processing to limit memory consumption.
- Build a supervised binary classifier using labeled benign and malicious samples.
- Avoid using test data during training or model selection.
- Establish a baseline before adding uncertainty estimation and abstention.

## Next Steps
- Identify the usable numerical features and their dimensions.
- Design a reproducible feature-extraction pipeline.
- Create a clean labeled training/validation split.
- Establish a baseline model and evaluation metrics.

## Status
Dataset structure and label distributions inspected successfully.
