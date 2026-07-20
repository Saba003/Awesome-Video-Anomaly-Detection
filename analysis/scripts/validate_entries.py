from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"

def require_columns(path: Path, columns: set[str]) -> pd.DataFrame:
    df = pd.read_csv(path)
    missing = columns - set(df.columns)
    if missing:
        raise ValueError(f"{path.name}: missing columns {sorted(missing)}")
    return df

def main() -> None:
    papers = require_columns(
        DATA / "papers_master.csv",
        {"paper_id", "title", "year", "venue", "supervision", "architecture"},
    )
    benchmarks = require_columns(
        DATA / "benchmarks.csv",
        {"paper_id", "dataset", "metric", "value", "level", "protocol"},
    )
    datasets = require_columns(
        DATA / "datasets.csv",
        {"dataset", "year", "annotation", "supervision_supported"},
    )

    if papers["paper_id"].duplicated().any():
        duplicates = papers.loc[papers["paper_id"].duplicated(), "paper_id"].tolist()
        raise ValueError(f"Duplicate paper IDs: {duplicates}")

    unknown_ids = sorted(set(benchmarks["paper_id"]) - set(papers["paper_id"]))
    if unknown_ids:
        raise ValueError(f"Unknown benchmark paper IDs: {unknown_ids}")

    if benchmarks["value"].isna().any():
        raise ValueError("Benchmark values contain missing entries")

    print(
        f"Validation passed: {len(papers)} papers, "
        f"{len(benchmarks)} benchmark rows, {len(datasets)} datasets."
    )

if __name__ == "__main__":
    main()
