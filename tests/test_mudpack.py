import socket
from unittest import mock

import pytest

import mudpack


@pytest.fixture
def m_socket():
    with mock.patch("mudpack.socket.socket") as m_socket:
        yield m_socket


@pytest.fixture
def client(m_socket):
    return mudpack.Client(hostname="localhost", port=10_000)


def test_mudpack_client_creates_udp_socket(m_socket, client):
    m_socket.assert_called_with(socket.AF_INET, socket.SOCK_DGRAM, 0)


def test_mudpack_client_send_connects_to_the_socket(m_socket, client):
    client.send("foo")
    m_socket().connect.assert_called_with(("localhost", 10_000))


def test_mudpack_client_send_multiple_messages_calls_connect_once(m_socket, client):
    client.send("foo")
    client.send("foo")

    m_socket().connect.assert_called_once()


def test_mudpack_client_send(m_socket, client):
    client.send("foo")
    m_socket().send.assert_called_with(b"foo")


def test_mudpack_client_send_bytes(m_socket, client):
    client.send(b"foo")
    m_socket().send.assert_called_with(b"foo")


def test_mudpack_client_as_context_manager(m_socket):
    with mudpack.Client(hostname="localhost", port=10_000) as mp:
        mp.send("foo")

    m_socket().send.assert_called_with(b"foo")


def test_mudpack_send(m_socket):
    mudpack.send(hostname="localhost", port=10_000, message="foo")
    m_socket().send.assert_called_with(b"foo")
