"""Example test."""

from __future__ import annotations

from {{cookiecutter.package_name}} import __version__


def test_version():
    assert __version__ == "{{ cookiecutter.version }}"
