#!/usr/bin/env python3

import sys
import argparse

def first_last(first="john", last="doe"):
    return f"{first}.{last}"

def f_last(first="john", last="doe"):
    return f"{first[0]}.{last}"

def firstlast(first="john", last="doe"):
    return f"{first}{last}"

def flast(first="john", last="doe"):
    return f"{first[0]}{last}"

def first_l(first="john", last="doe"):
    return f"{first}.{last[0]}"

def firstl(first="john", last="doe"):
    return f"{first}{last[0]}"

def last_first(first="john", last="doe"):
    return f"{last}.{first}"

def l_first(first="john", last="doe"):
    return f"{last[0]}.{first}"

def lastfirst(first="john", last="doe"):
    return f"{last}{first}"

def lfirst(first="john", last="doe"):
    return f"{last[0]}{first}"

def last_f(first="john", last="doe"):
    return f"{last}.{first[0]}"

def lastf(first="john", last="doe"):
    return f"{last}{first[0]}"

fn_handlers = {
    'john.doe': first_last,
    'j.doe': f_last,
    'johndoe': firstlast,
    'jdoe': flast,
    'john.d': first_l,
    'johnd': firstl,
    'doe.john': last_first,
    'd.john': l_first,
    'doejohn': lastfirst,
    'djohn': lfirst,
    'doe.j': last_f,
    'doej': lastf,
}

def main(args):
    names = []
    results = []

    with open(args.file, 'r') as f:
        names = [line.strip() for line in f.readlines()]

    if names == []:
        print("[-] No names loaded")
        exit(1)

    for ix, name in enumerate(names, 1):
        _name = name.lower()
        _name = _name.split(' ')

        if len(_name) != 2:
            sys.stderr.write(f'[-] Wrong format "{name}" at line:{ix} (SKIPPED).\n')
            continue

        first, last = _name

        for fmt in args.format:
            fn = fn_handlers.get(fmt)
            if fn == None:
                sys.stderr.write('[-] Should not be reachable (SKIPPED).\n')
                continue
            r = fn(first, last)
            results.append(r)
    results.append('')

    with open(args.output, 'w') as f:
        f.write( f'{args.suffix}\n'.join(results) )
        f.flush()

if __name__ == '__main__':

    available_formats = fn_handlers.keys() 

    parser = argparse.ArgumentParser(
        prog = 'name-mangler',
        description = 'generate combinations',
    )

    parser.add_argument(
        '-o',
        '--output',
        default = '/dev/stdout',
        required = False,
        help = 'Output file'
    )

    parser.add_argument(
        '-f',
        '--file',
        default = '/dev/stdin',
        required = False,
        help = 'File that contains full names'
    )

    parser.add_argument(
        '--format',
        default = ['john.doe'],
        choices = available_formats,
        required = False,
        nargs = '*',
        help = 'Format of the generated output'
    )

    parser.add_argument(
        '--all-formats',
        default = False,
        action = 'store_true',
        required = False,
        help = 'Select all available formats'
    )

    parser.add_argument(
        '-s',
        '--suffix',
        default = '',
        required = False,
        help = 'Add a suffix'
    )

    args = parser.parse_args()

    if args.all_formats:
        args.format = available_formats 

    main(args)

