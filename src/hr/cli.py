from argparse import ArgumentParser

def create_parser():
    parser = ArgumentParser(description='''
    HR CLI user export utility
    ''')
    parser.add_argument('--format', choices=['json', 'csv'], type=str.lower, help='json or csv', default='json')
    parser.add_argument('--path', help='where to store the file')
    return parser

def main():
    import sys
    from hr import export
    from hr import users as usrs

    args = create_parser().parse_args()
    users = usrs.get_users()
    if args.path:
        file = open(args.path, 'w')
    else:
        file = sys.stdout

    if args.format == 'csv':
        export.export_csv(file, users)        
    else:
        export.export_json(file, users)