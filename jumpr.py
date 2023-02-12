import json
from pathlib import Path
import sys
from typing import Dict
import argparse

config_file = Path(Path.home()).joinpath('.jumpr.json')

config: Dict[str, str] = {}

if config_file.exists():
    config = json.loads(config_file.read_text())


def save_config():
    jsonText = json.dumps(config, indent=4)
    config_file.write_text(jsonText)


def list_aliases():
    if not config:
        print('No aliases found')
        return 0

    for alias, path in config.items():
        print(f'{alias} -> {path}')


def set_alias(alias):
    config[alias] = str(Path.cwd()).strip()
    save_config()


def remove_alias(alias):
    if alias not in config:
        print(f'Alias "{alias}" does not exist')
        return 1

    del config[alias]
    save_config()


def get_alias(alias):
    if alias not in config:
        print(f'Alias "{alias}" does not exist')
        return 1

    path = config[alias]

    if not Path(path).exists():
        print(f'Path "{path}" does not exist')
        return 2

    print(path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-l', '--list', action='store_true', help='List all aliases'
    )
    parser.add_argument(
        '-g', '--get', help='Get path for alias', metavar='ALIAS'
    )
    parser.add_argument(
        '-s', '--set', help='Set path for alias', metavar='ALIAS'
    )
    parser.add_argument(
        '-r', '--remove', help='Remove alias', metavar='ALIAS'
    )
    args = parser.parse_args()

    if args.list:
        sys.exit(list_aliases() or 0)
    elif args.remove:
        sys.exit(remove_alias(args.remove) or 0)
    elif args.get:
        sys.exit(get_alias(args.get) or 0)
    elif args.set:
        sys.exit(set_alias(args.set) or 0)
    else:
        parser.print_help()
