import typer
from typing import Optional
from pizzachili.download import download_dataset

app = typer.Typer(help="CLI tool to download Pizza&Chili datasets.")

@app.command()
def download(
    typed: bool = typer.Option(
        True,
        "--non-repetitive/--repetitive",
        "-nrep/-rep",
        help="Download non-repetitive (-nrep) or repetitive (-rep) datasets"
    ),
    subtype: Optional[str] = typer.Option(None, "--subtype", "-st", help="Subtype to download. Options: sources, pitches, proteins, dna, english, dblp.xml"),
    size: Optional[str] = typer.Option(None, "--size", "-s", help="Size of dataset. Options: 50MB, 100MB, 200MB. Leave empty for full file"),
    gunzip: bool = typer.Option(False, "--gunzip", "-gz", help="Decompress downloaded files"),
):
    download_dataset(type=typed, subtype=subtype, size=size, gunzip=gunzip)

if __name__ == "__main__":
    app()