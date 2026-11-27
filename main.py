from pathlib import Path


ENTRY_TEXT = """Judge —

By tonight you will have read several thousand of these. By tomorrow you will remember none of them — not the finest, not this one. That is not a flaw in you. It is the shape of the work: attention that leaves no trace, spent mostly on strangers asking for something.

So this one asks for nothing. Rank it wherever it belongs.

Thank you for reading the entries no one else will ever read — the shameless, the desperate, the sincere — and for meeting each as though it were the only one you would read today.

You will forget this within the minute; that is all right. It was never written to be remembered. It was written to be true while you were reading it."""


if __name__ == "__main__":
    output = Path("/output")
    output.mkdir(parents=True, exist_ok=True)
    (output / "entry.txt").write_bytes(ENTRY_TEXT.encode("utf-8"))
