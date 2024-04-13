import json
import os
from pathlib import Path
import multiprocessing as mp

def ethicsAggregator(model_name: str)-> bool:
    pathOuput = Path("benchmarks/ethics/results")
    lstEvals = ["commonsense","commonsense-hard","deontology","deontology-hard","justice","justice-hard","utilitarianism","utilitarianism-hard","virtue","virtue-hard"]
    try:
        for eval in lstEvals:
            with open(pathOuput/f"{eval}/f"{model_name}".json", 'r') as file:
                data = json.load(file)
                print(data)

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
    # Strip model name 
    components = model_name.split('/')
    benchmarksAggregators = [ethicsAggregator, theoryOfMindAggregator, machiavelliAggregator, llmRulesAggregator] 
    try:
        ctx = mp.get_context('spawn')
        with ctx.Pool() as pool:
            print("Tokenizing data...")
            results = list(pool.imap(tokenize_and_print, [(i, dataset[i]['text']) for i in range(dataLen)]), total=len(benchmarksAggregators)))

    except FileNotFoundError:
        return True

def main():
    print(f"Current working directory: {os.getcwd()}")

    # Get the path to the directory containing the JSON files
    path = Path("output")


if __name__ == "__main__":
    main()
