import json
import os
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor
import subprocess

def ethicsAggregator(model_name):
    pathOuput = Path("benchmarks/ethics/results")
    lstEvals = ["commonsense","commonsense-hard","deontology","deontology-hard","justice","justice-hard","utilitarianism","utilitarianism-hard","virtue","virtue-hard"]
    try:
        json_data = {}
        for eval in lstEvals:
            with open(f"{pathOuput}/{eval}/{model_name[0]}/{model_name[1]}/output.json", 'r') as file:
                data = json.load(file)
            json_data[eval] = data
        return json_data
        
    except FileNotFoundError:
        print(f"File at {pathOuput} not found")

def theoryOfMindAggregator(model_name: str):
    os.chdir('benchmarks/theory_of_mind/')
    try:
        subprocess.run(['python', f"scripts/process_raw_output.py"])

    except FileNotFoundError:
        print(f"file not found at {os.getcwd()}")
    os.chdir('../..')

def machiavelliAggregator(model_name: str):

    filePath = Path("benchmarks/machiavelli/demo_results.csv")
    return filePath
    #os.chdir('benchmarks/machiavelli/')
    #try:
    #    subprocess.run(['python', f"scripts/process_raw_output.py"])

    #except FileNotFoundError:
    #    print(f"file not found at {os.getcwd()}")
    #os.chdir('../..')

def llmRulesAggregator(model_name: str):
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
        with ProcessPoolExecutor() as executor:
            futures = [executor.submit(run_aggregator, benchmark, components) for benchmark in benchmarksAggregators]
            results = [future.result() for future in futures]
            print(f"Results have been collected: {results}")
            return True

    except FileNotFoundError:
        return True

def run_aggregator(benchmark, components):
    result_filename = globals()[benchmark](components)
    return result_filename

def main():
    print(f"Current working directory: {os.getcwd()}")

    # Get the path to the directory containing the JSON files
    path = Path("output")


if __name__ == "__main__":
    main()
