#! /usr/bin/env python
from __future__ import annotations

import argparse
from typing import Sequence

import mudpack


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("message", type=str, nargs="*")
    parsed_args = parser.parse_args(argv)

    mudpack.send("127.0.0.1", 10_000, " ".join(parsed_args.message))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
