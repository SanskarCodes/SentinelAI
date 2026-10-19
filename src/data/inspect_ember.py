
import json
from collections import Counter
from pathlib import Path

DATA_DIR = Path("data/raw/ember2018")


def inspect_labels(file_path):
    counts = Counter()
    total = 0

    with file_path.open("r", encoding="utf-8") as file:
        for line in file:
            record = json.loads(line)
            counts[record.get("label", "missing")] += 1
            total += 1

    print(f"\nFile: {file_path.name}")
    print(f"Total records: {total:,}")

    for label, count in sorted(
        counts.items(), key=lambda item: str(item[0])
    ):
        pct = count / total * 100 if total else 0
        print(f"  Label {label}: {count:,} ({pct:.2f}%)")


if __name__ == "__main__":
    files = [
        *sorted(DATA_DIR.glob("train_features_*.jsonl")),
        DATA_DIR / "test_features.jsonl",
    ]

    for file_path in files:
        if file_path.exists():
            inspect_labels(file_path)
        else:
            print(f"Missing file: {file_path}")
