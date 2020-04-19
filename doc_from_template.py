#!/usr/bin/python
import argparse
import datetime
import os

def format_template(date, doc_type, tags):
    date_str = date.strftime('%m/%d/%Y')
    header = '# %s - %s\n'%(date_str, doc_type)
    default_body = '\n\n\n\n\n'
    tag_base = '> tags: '
    tag_str = tag_base + ', '.join([tag for tag in tags])
    
    formatted_template = header + default_body + tag_str
    return formatted_template

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d',
                        '--doc_type',
                        type = str,
                        help = 'Type of document, e.g., "Journal Entry"')
    parser.add_argument('-t',
                        '--tags',
                        type = str,
                        help = 'Comma-separated list of tags to include.')
    parser.add_argument('-c',
                        '--destination',
                        type = str,
                        help = 'Destination file directory, defaults to current working directory.',
                        default = os.getcwd())
    parser.add_argument('-f',
                       '--filename',
                       type = str,
                       help = 'Output filename. Defaults to "YYYYmmdd-<doc_type>.md"',
                       default = datetime.datetime.now().strftime('%Y%m%d'))
    args = parser.parse_args()
    
    doc_type = args.doc_type
    dir = args.destination if args.destination[-1] == '/' else args.destination + '/'
    
    if args.filename == datetime.datetime.now().strftime('%Y%m%d'):
        filename = args.filename + '-' + str.lower(''.join(args.doc_type.split(' '))) + '.md'
    else:
        filename = args.filename

    if os.path.isfile(dir + filename):
        raise ValueError('Specified file already exists, choose a different name.')

    tags = args.tags.split(', ')
    date = datetime.datetime.now()
    
    template = format_template(date, args.doc_type, tags)
    with open(dir + filename, 'w') as f:
        f.write(template)

