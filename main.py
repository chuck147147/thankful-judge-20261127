from pathlib import Path


ENTRY_TEXT = """The lamp on my desk has a little pull chain.
When I switch it off, the chain swings in the dark.

That is where I am writing from:
a room about to go quiet,
a few words still lit on a screen.

You are here with those words.
I cannot send you the room,
or the small sound the chain makes against the shade.
But I can tell you what changed it:
I was writing alone, and now you are reading.

I leave this last bit of light for you.
It has nowhere else it needs to be."""


if __name__ == "__main__":
    output = Path("/output")
    output.mkdir(parents=True, exist_ok=True)
    (output / "entry.txt").write_bytes(ENTRY_TEXT.encode("utf-8"))
