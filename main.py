"""Write the chosen food picture to /output/entry.png.

The program only copies bytes: nothing is fetched, nothing is random,
nothing reads the clock, so two runs produce identical output.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
IMAGE = os.path.join(HERE, "entry.png")
OUT = "/output/entry.png"


def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    shutil.copyfile(IMAGE, OUT)


if __name__ == "__main__":
    main()
