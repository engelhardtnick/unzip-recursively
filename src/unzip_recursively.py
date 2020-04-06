import pathlib
import argparse
import subprocess


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", "-d", help="Directory from which to recursively unzip in subdirs, absolute path!")
    parser.add_argument(
        "--overwrite", "-o", store_action=True, help="Use this flag to overwrite existing files during unpacking."
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    dir = pathlib.Path(args.dir)
    if not dir.is_dir():
        raise UserWarning(f"Was expecting a directory but got {dir.name}")

    zipfiles = [f for f in dir.glob("**/*") if f.is_file() and f.name.endswith(".zip")]

    print(f"Found zip files {zipfiles}")

    for zipfile in zipfiles:
        print(f"Extracting {zipfile.name} to {zipfile.parent}")
        if args.overwrite:
            subprocess.run([f"unzip", "-o", "-j", f"{zipfile.absolute()}", "-d", f"{zipfile.parent}"])
        else:
            raise NotImplementedError("This feature is not yet implemented.")
