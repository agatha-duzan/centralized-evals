import json
import os
from pathlib import Path

def ethicsAggregator(model_name: str)-> bool:

    return True


def fileAggregator(model_name: str)-> bool:

    return True

def main():
    print(f"Current working directory: {os.getcwd()}")

    # Get the path to the directory containing the JSON files
    path = Path("output")


if __name__ == "__main__":
    main()
