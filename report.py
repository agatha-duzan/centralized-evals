import pandas as pd
import csv

def aggregate_results(results):
    aggregated = {}
    for result in results:
        aggregated.update(result)
    return aggregated

def report_results(aggregated, model_name):
    filename = f'results_{model_name}.csv'
    
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(aggregated.keys())
        writer.writerows(zip(*aggregated.values()))

    print(f"Results saved to {result_filename}")    
    return filename

def results_visualization(result_filename):
    df = pd.read_csv(result_filename)
    # TODO: create beautiful viz for the benchmarks later
    print(df)