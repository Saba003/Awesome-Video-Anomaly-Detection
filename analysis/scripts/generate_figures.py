from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"
OUT = ROOT / "analysis" / "outputs" / "figures"
OUT.mkdir(parents=True, exist_ok=True)

def main() -> None:
    papers = pd.read_csv(DATA / "papers_master.csv")
    counts = papers.groupby("year").size().sort_index()

    fig, ax = plt.subplots(figsize=(8, 5))
    counts.plot(kind="bar", ax=ax)
    ax.set_title("Included VAD Papers by Year")
    ax.set_xlabel("Year")
    ax.set_ylabel("Number of papers")
    fig.tight_layout()
    fig.savefig(OUT / "papers_by_year.png", dpi=200)
    plt.close(fig)

    print(f"Generated figures in {OUT}")

if __name__ == "__main__":
    main()
