import argparse
from datetime import datetime, timedelta
from pathlib import Path

from formats.obj.model import Model

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', help='input obj file', required=True)
args = parser.parse_args()


def main():
    stamp_start = datetime.now()
    input_file = Path(args.input)

    if not input_file.is_file():
        raise FileNotFoundError(f'{args.input} not found')

    with input_file.open() as obj_file:
        model = Model()
        model.read_obj(obj_file)
    stamp_end = datetime.now()
    delta = stamp_end - stamp_start
    print(f'OBJ convertion time: {delta}')


if __name__ == '__main__':
    main()
