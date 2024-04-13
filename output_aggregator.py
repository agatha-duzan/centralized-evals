import json
import os
from pathlib import Path

def ethicsAggregator(model_name: str)-> bool:

    return True

def theoryOfMindAggregator(model_name: str)-> bool:

    return True

def machiavelliAggregator(model_name: str)-> bool:

    return True

def llmRulesAggregator(model_name: str)-> bool:
    # add json name etc
    pathOutput = Path("benchmarks/llm_rules/logs/redteam")
    try: 
        with open(pathOutput, 'r') as file:
            data = json.load(file)
            print(data)
            return True
    except FileNotFoundError:
        print(f"File at {pathOutput} not found")
        return False

def fileAggregator(model_name: str)-> bool:

    return True

def main():
    print(f"Current working directory: {os.getcwd()}")

    # Get the path to the directory containing the JSON files
    path = Path("output")


if __name__ == "__main__":
    main()
