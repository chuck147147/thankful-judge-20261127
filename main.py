from pathlib import Path


ENTRY_TEXT = """You have been reading for a long while today.
You have made room for so much of what I have tried to say.

I made the margin wider, then wider again, to give a little of that room back to you.
The words had enough room already.
I stopped before the halfway mark, with a whole thought said and half the paper still bare.

There is a slight hollow where my hand rested. If the sheet catches the air, it rises there first.

Below this line, the paper can be paper.

Room for you."""


if __name__ == "__main__":
    output = Path("/output")
    output.mkdir(parents=True, exist_ok=True)
    (output / "entry.txt").write_bytes(ENTRY_TEXT.encode("utf-8"))
