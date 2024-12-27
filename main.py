# main.py
import pandas as pd
from rule_solver.rules import find_best_rules
from rule_solver.utils import save_rules_to_file

def main():
    # Load data
    df = pd.read_parquet('./data/iris.parquet')

    # Example 1: Find rules that maximize sepal_length
    results = find_best_rules(df, num_rules=3, target_var='sepal_length', direction='maximize')
    save_rules_to_file(results, df, 'rules_sepal_length_max.txt',
                      target_var='sepal_length', direction='maximize')

    # Example 2: Find rules that minimize petal_width
    results = find_best_rules(df, num_rules=3, target_var='petal_width', direction='minimize')
    save_rules_to_file(results, df, 'rules_petal_width_min.txt',
                      target_var='petal_width', direction='minimize')

    # Example 3: Find rules that predict setosa species
    results = find_best_rules(df, num_rules=3, target_var='species', direction='setosa')
    save_rules_to_file(results, df, 'rules_species_setosa.txt',
                      target_var='species', direction='setosa')

if __name__ == "__main__":
    main()
