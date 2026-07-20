from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"
OUT = ROOT / "analysis" / "outputs" / "tables"
OUT.mkdir(parents=True, exist_ok=True)

def main() -> None:
    papers = pd.read_csv(DATA / "papers_master.csv")
    benchmarks = pd.read_csv(DATA / "benchmarks.csv")

    papers.to_markdown(OUT / "papers.md", index=False)
    benchmarks.sort_values(["dataset", "metric", "value"], ascending=[True, True, False]).to_markdown(
        OUT / "benchmarks.md", index=False
    )
    print(f"Generated Markdown tables in {OUT}")

if __name__ == "__main__":
    main()
