#!/usr/bin/env python3
"""Count tokens in arbitrary text, a UTF-8 file, or UTF-8 stdin."""
import argparse
import json
import sys
from importlib.metadata import version
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group()
    source.add_argument('--text', help='Text to tokenize')
    source.add_argument('--file', type=Path, help='UTF-8 file; otherwise read UTF-8 stdin')
    parser.add_argument('--encoding', default='o200k_base',
                        help='Named tiktoken encoding (default: o200k_base)')
    args = parser.parse_args()
    try:
        import tiktoken
    except ImportError:
        parser.exit(2, 'Missing tiktoken. Install it in your environment:\n'
                       '  python -m pip install tiktoken\n')
    try:
        if args.text is not None:
            text = args.text
        elif args.file is not None:
            text = args.file.read_bytes().decode('utf-8')
        else:
            text = sys.stdin.buffer.read().decode('utf-8')
    except (OSError, UnicodeError) as error:
        parser.exit(2, f'Cannot read UTF-8 text: {error}\n')
    try:
        encoding = tiktoken.get_encoding(args.encoding)
    except Exception as error:
        parser.exit(2, f'Cannot load encoding {args.encoding}: {error}\n'
                       'The first load may need network access to tokenizer data.\n')
    # Preserve whitespace/newlines; special-token-looking strings are literal text.
    tokens = len(encoding.encode(text, disallowed_special=()))
    print(json.dumps({'tokens': tokens, 'tokenizer': 'tiktoken',
                      'version': version('tiktoken'), 'encoding': encoding.name}))


if __name__ == '__main__':
    main()
