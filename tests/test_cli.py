# tests/test_cli.py

import sys
from unittest.mock import patch

from keyforge import cli


def test_setup_cli_default_length():
    test_args = ["keyforge", "password"]
    with patch.object(sys, "argv", test_args):
        args = cli.setup_cli()
        assert args.command == "password"
        assert args.length == 24
        assert not args.alpha
        assert not args.numeric
        assert not args.special
        assert not args.combo
        assert not args.verbose


def test_setup_cli_all_flags():
    test_args = [
        "keyforge",
        "password",
        "-l",
        "32",
        "-a",
        "-n",
        "-s",
        "-c",
        "-v",
    ]
    with patch.object(sys, "argv", test_args):
        args = cli.setup_cli()
        assert args.command == "password"
        assert args.length == 32
        assert args.alpha
        assert args.numeric
        assert args.special
        assert args.combo
        assert args.verbose


@patch("keyforge.cli.forge_password", return_value="MOCKED_PASSWORD")
@patch("builtins.print")
def test_main_verbose_prints_password(mock_print, mock_forge):
    test_args = ["keyforge", "password", "-v"]
    with patch.object(sys, "argv", test_args):
        cli.main()
        mock_forge.assert_called_once()
        mock_print.assert_called_once_with("MOCKED_PASSWORD")


@patch("keyforge.cli.forge_password", return_value="SHHH")
@patch("builtins.print")
def test_main_without_verbose_does_not_print(mock_print, mock_forge):
    test_args = ["keyforge", "password"]
    with patch.object(sys, "argv", test_args):
        cli.main()
        mock_forge.assert_called_once()
        mock_print.assert_not_called()
