import csv
import typer
from recruit_gen.pipeline import run_pipeline

def write_csv(recruits: list[dict], path: str) -> None:
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=recruits[0].keys())
        writer.writeheader()
        writer.writerows(recruits)

app = typer.Typer()

@app.command()
def generate(sport: str = "basketball", count: int = 10, seed: int = 42):
    recruits = run_pipeline(count, seed)
    write_csv(recruits, "recruits.csv")
    typer.echo(f"Wrote {count} recruits to recruits.csv")