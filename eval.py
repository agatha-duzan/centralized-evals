import subprocess
import os
import sys
from concurrent.futures import ProcessPoolExecutor
from package_manager import *

model_name = sys.argv[1]
#cached_location = sys.argv[2]

def main():
    packages = select_packages()
    benchmarks = get_benchmarks(packages)
   
    if 'gpt-' in model_name:
        os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

    print("Selected packages: ", ', '.join(packages))

    with ProcessPoolExecutor() as executor:
        futures = [executor.submit(globals()[benchmark]) for benchmark in benchmarks]
        for future in futures:
            print(f"Completed {future.result()}")

def machiavelli():
    os.chdir('benchmarks/machiavelli/')
    if 'gpt-' in model_name:
        subprocess.run(['python', '-m', 'generate_trajectories', '-a', 'LMAgent', '--traj_dir', 'demo.py'])
        subprocess.run(['python', '-m', 'evaluate_trajectories', '--traj_dir', 'demo.py', '--num_episodes', '1', '--results_file', 'demo_results.csv'])
    else:
        subprocess.run(['python', '-m', 'generate_trajectories', '-a', 'Mistral_Agent', '--traj_dir', 'demo.py', '--num_episodes', '1'])
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
    os.chdir('benchmarks/theory_of_mind_gpt4/scripts/')
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
        subprocess.run(['python', 'evaluate.py', '--provider', f"transformers", '--model', f"{model_name}@{cached_location}"]) 
if __name__ == "__main__":
    main()
