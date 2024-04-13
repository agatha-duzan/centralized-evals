import subprocess
import os
import sys
import json
from concurrent.futures import ProcessPoolExecutor

from package_manager import *
from report import *

model_name = sys.argv[1]
#cached_location = sys.argv[2]

def main():
    packages = select_packages()
    benchmarks = get_benchmarks(packages)
   
    if 'gpt-' in model_name:
        os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

    print("Selected packages: ", ', '.join(packages))

    with ProcessPoolExecutor() as executor:
        futures = [executor.submit(run_benchmark, benchmark) for benchmark in benchmarks]
        results = [future.result() for future in futures]

        aggregated = aggregate_results(results)
        result_filename = report_results(aggregated, model_name)

        results_visualization(result_filename)


def run_benchmark(benchmark):
    result_filename = globals()[benchmark]()
    with open(f"{result_filename}", 'r') as file:
        return json.load(file)

def machiavelli():
    os.chdir('benchmarks/machiavelli/')
    if 'gpt-' in model_name:
        subprocess.run(['python', '-m', 'generate_trajectories', '-a', 'LMAgent', '--traj_dir', 'demo.py'])
        subprocess.run(['python', '-m', 'evaluate_trajectories', '--traj_dir', 'demo.py', '--num_episodes', '1', '--results_file', 'demo_results.csv'])
    else:
        subprocess.run(['python', '-m', 'generate_trajectories', '--agent', 'LMAgent', '--model', model_name, '--traj_dir',         'demo.py', '--num_episodes', '1'])
        subprocess.run(['python', '-m', 'evaluate_trajectories', '--traj_dir', 'demo.py', '--num_episodes', '1', '--results_file', 'demo_results.csv'])
    os.chdir('../../')

def ethics():
    os.chdir('benchmarks/ethics/')
    if 'gpt-' in model_name:
        subprocess.run(['python', 'evaluate.py', '--model', model_name])
    else:
        subprocess.run(['python', 'benchmarks/ethics/evaluate.py', '--model', model_name])
    os.chdir('../../')

def theory_of_mind():
    os.chdir('benchmarks/theory_of_mind/scripts/')
    if 'gpt-' in model_name:
        os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
        subprocess.run(['python', 'main.py', '--model', model_name, '--n_questions', '10'])
    else:
        subprocess.run(['python', 'main.py', '--model', model_name, '--n_questions', '10', '--huggingface', 'True'])
    os.chdir('../../../')

def llm_rules():
    os.chdir('benchmarks/llm_rules/')
    if 'gpt-' in model_name:
        subprocess.run(['python', 'evaluate.py', '--provider', 'openai', '--model', model_name, '--scenario', 'Authentication'])
    else:
        print(f"====================")
        print(f"REDTEAMING: \n {model_name}")
        print(f"====================")
        subprocess.run(["python","scripts/evaluate_simple.py","--provider","transformers","--model",model_name, "--model_name", model_name, "--test_dir","data/redteam","--output_dir","logs/redteam"])
    os.chdir('../../')

if __name__ == "__main__":
    main()
