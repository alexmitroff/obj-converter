import argparse
from pathlib import Path
from formats.obj.model import Model

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', help='input obj file', required=True)
args = parser.parse_args()


def main():
    input_file = Path(args.input)

    if not input_file.is_file():
        raise FileNotFoundError(f'{args.input} not found')

    with input_file.open() as obj_file:
        model = Model()
        model.read_obj(obj_file)


if __name__ == '__main__':
    main()
