"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Hord."""


if __name__ == "__main__":
    main(prog_name="hord")  # pragma: no cover
