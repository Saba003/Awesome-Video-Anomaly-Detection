from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]

def main() -> None:
    path = ROOT / "data" / "papers_master.csv"
    df = pd.read_csv(path)
    df.columns = [column.strip().lower() for column in df.columns]
    df = df.drop_duplicates(subset=["paper_id"])
    df.to_csv(path, index=False)
    print(f"Cleaned {path}")

if __name__ == "__main__":
    main()
