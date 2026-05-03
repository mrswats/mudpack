import socket
import sys
from types import TracebackType

if sys.version_info.minor <= 10:  # pragma: no cover
    from typing_extensions import Self
else:
    from typing import Self


class Client:
    """Simple UDP Client for Python.

    Args:
        * hostname: string -> Hostname of the UDP server
        * port: int -> Port for the UDP server
    """

    def __init__(self, hostname: str, port: int) -> None:
        self.hostname = hostname
        self.port = port
        self._connected = False
        self._socket = self._get_socket()

    def _get_socket(self) -> socket.socket:
        return socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

    def _connect(self) -> None:
        if not self._connected:
            self._socket.connect((self.hostname, self.port))
            self._connected = True

    def _close(self) -> None:
        self._socket.close()
        self._connected = False

    def _send(self, message: bytes) -> int:
        return self._socket.send(message)

    def send(self, message: str | bytes) -> int:
        self._connect()

        if isinstance(message, str):
            message = message.encode()

        return self._send(message)

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None = None,
        exc_value: BaseException | None = None,
        traceback: TracebackType | None = None,
    ) -> None:
        self._close()

    def __del__(self) -> None:
        self._close()


def send(hostname: str, port: int, message: str | bytes) -> None:
    with Client(hostname=hostname, port=port) as client:
        client.send(message)
