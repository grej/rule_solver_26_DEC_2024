# main.py
import pandas as pd
from rule_solver.rules import find_best_rules
from rule_solver.utils import save_rules_to_file

def main():
    # Load data
    df = pd.read_parquet('./data/iris.parquet')

    # Find rules
    results = find_best_rules(df, num_rules=5, target_column='species')

    # Save formatted results
    save_rules_to_file(results)
    print("Rules have been saved to rules_output.txt")

if __name__ == "__main__":
    main()
