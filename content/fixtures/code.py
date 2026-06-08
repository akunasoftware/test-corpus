from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ReviewNote:
    section: str
    owner: str
    message: str


def build_release_notes(notes: list[ReviewNote]) -> list[str]:
    return [
        f"{note.section}: {note.owner} confirmed {note.message}"
        for note in notes
        if note.owner
    ]


def main() -> None:
    notes = [
        ReviewNote("inventory", "Mina", "cycle counts are balanced"),
        ReviewNote("quality", "Owen", "extraction fixture marker: shared code sample"),
    ]

    for line in build_release_notes(notes):
        print(line)


if __name__ == "__main__":
    main()
