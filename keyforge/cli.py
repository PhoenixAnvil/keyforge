import argparse

from keyforge.forge import forge_password


def parse_length(value):
    return None if value.lower() == "none" else int(value)


def setup_cli():
    parser = argparse.ArgumentParser(
        prog="KeyForge",
        description="Secure Password Generator CLI Tool",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    key_parser = subparsers.add_parser(
        "password", help="Generate a secure password"
    )
    key_parser.add_argument(
        "-l",
        "--length",
        type=parse_length,
        default=None,
        help="The length of the new password",
    )
    key_parser.add_argument(
        "-a",
        "--alpha",
        action="store_true",
        help="Use alpha (letters) only",
    )
    key_parser.add_argument(
        "-n", "--numeric", action="store_true", help="Use numeric only"
    )
    key_parser.add_argument(
        "-s", "--special", action="store_true", help="Use special only"
    )
    key_parser.add_argument(
        "-c",
        "--combo",
        action="store_true",
        help="Use combination of all",
    )
    key_parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Show verbose output (this will show the generated keys)",
    )

    return parser.parse_args()


def main():
    args = setup_cli()

    if args.command == "password":
        key = forge_password(
            length=args.length,
            alpha=args.alpha,
            numeric=args.numeric,
            special=args.special,
            combo=args.combo,
        )

        if args.verbose:
            print(key)


if __name__ == "__main__":
    main()
