import random
import string
import argparse
import json
from os.path import exists

import barcode
from jinja2 import Template


def make_identifier(used_ids):
    identifier = \
        ''.join(
            [random.choice(string.ascii_uppercase+string.digits)
             for _ in range(6)]
        )
    if identifier in used_ids:
        return make_identifier()
    return identifier


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--template", default="template.html")
    parser.add_argument("--count", default=10, type=int)
    parser.add_argument("--used_ids", default="used_ids.json")
    parser.add_argument("--outfile", default="rendered.html")
    args = parser.parse_args()

    if not exists(args.used_ids):
        used_ids = set()
    else:
        with open(args.used_ids) as f:
            used_ids = json.load(f)
        used_ids = set(used_ids)

    print("Reading template...")
    with open(args.template) as f:
        template = Template(f.read())

    print("Generating identifiers...")
    identifiers = []
    for _ in range(args.count):
        i = make_identifier(used_ids)
        used_ids.add(i)
        identifiers.append(i)

    print("Making barcodes...")
    for x in identifiers:
        bc = barcode.codex.Code39(x, add_checksum=False, writer=barcode.writer.ImageWriter())
        bc.save("./barcodes/{}".format(x),
                options={'write_text': False, 'quiet_zone': 2, 'dpi': 300, 'module_height': 4})

    print("Rendering template...")
    rendered_template = template.render(
        identifiers=identifiers
    )
    with open(args.outfile, 'w') as f:
        f.write(rendered_template)

    with open(args.used_ids, 'w') as f:
        json.dump(list(used_ids), f)

    print("Done")

if __name__ == '__main__':
    main()
