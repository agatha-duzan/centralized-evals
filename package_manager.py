import csv
import pandas as pd

def select_packages(file_name = 'packages.csv'):
    df = pd.read_csv(file_name)
    packages_list = list(df['package'].unique())
    selected = []

    print("Select packages: ")
    for i, package_name in enumerate(packages_list):
        if input(f"{i+1}. {package_name} [y/n]: ").lower() in ('y', 'yes'):
            selected.append(package_name)

    return selected

def init_packages(data, file_name = 'packages.csv'):
    columns = ['package', 'name', 'benchmark', 'parallel']
    df = pd.DataFrame(data)
    df.to_csv(file_name, index=False)
    return

def get_benchmarks(packages, file_name = 'packages.csv'):
    df = pd.read_csv(file_name)
    benchmarks = df[df['package'].isin(packages)]['benchmark'].tolist()
    return benchmarks

def add_benchmark(package, name, benchmark, parallel = False, file_name = 'packages.csv'):
    fieldnames = ['package', 'name', 'benchmark', 'parallel']
    new_data = {'package': package, 'name': name, 'benchmark': benchmark, 'parallel': parallel}

    with open(file_name, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(new_data)

    return