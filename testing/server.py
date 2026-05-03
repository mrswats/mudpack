#! /usr/bin/env python
from __future__ import annotations

import argparse
import socket
from datetime import datetime
from typing import NoReturn
from typing import Sequence


def udp_server(hostname: str, port: int) -> NoReturn:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((hostname, port))

    print(f"Listening on {hostname}:{port}")

    while True:
        msg = sock.recv(1024)

        print(f"Received [{datetime.now().isoformat()}]: {msg.decode()}")


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--hostname, -H",
        default="127.0.0.1",
        type=str,
        required=False,
        dest="hostname",
    )
    parser.add_argument(
        "--port, -p",
        default="10000",
        type=int,
        required=False,
        dest="port",
    )
    parsed_args = parser.parse_args(argv)

    udp_server(parsed_args.hostname, parsed_args.port)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
