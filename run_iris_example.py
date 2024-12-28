# example_usage.py

import pandas as pd
from rule_solver.main import RuleDiscoverer

def run_iris_example():
    """Example using the Iris dataset to discover rules."""

    # Load Iris dataset
    print("Loading Iris dataset...")
    df = pd.read_parquet("./data/iris.parquet")
    print(f"Loaded dataset with shape: {df.shape}")

    # Example 1: Find rules to maximize sepal_length
    print("\n=== Example 1: Maximizing sepal_length ===")
    discoverer = RuleDiscoverer(
        df=df,
        target_var="sepal_length",
        direction="maximize",
        min_samples=10
    )

    result = discoverer.discover_rules(
        num_rules=3,      # Return top 3 rules
        num_pairs=50,     # Sample 50 pairs
        max_iterations=3  # Maximum optimization iterations
    )

    print("\nDiscovered Rules for Maximizing sepal_length:")
    for i, (rule, score) in enumerate(zip(result.rules, result.scores), 1):
        print(f"\nRule {i}:")
        print(f"Score: {score:.4f}")
        print("Conditions:")
        for feature, condition in rule.items():
            if isinstance(condition, tuple):
                print(f"  {feature}: [{condition[0]:.2f}, {condition[1]:.2f}]")
            else:
                print(f"  {feature}: {condition}")

    # Example 2: Find rules to predict 'setosa' species
    print("\n=== Example 2: Predicting 'setosa' species ===")
    species_discoverer = RuleDiscoverer(
        df=df,
        target_var="species",
        direction="setosa",
        min_samples=10
    )

    species_result = species_discoverer.discover_rules(
        num_rules=2,
        num_pairs=50
    )

    print("\nDiscovered Rules for Identifying setosa:")
    for i, (rule, score) in enumerate(zip(species_result.rules, species_result.scores), 1):
        print(f"\nRule {i}:")
        print(f"Score: {score:.4f}")
        print("Conditions:")
        for feature, condition in rule.items():
            if isinstance(condition, tuple):
                print(f"  {feature}: [{condition[0]:.2f}, {condition[1]:.2f}]")
            else:
                print(f"  {feature}: {condition}")

        # Get metrics for this rule
        metrics = species_result.metrics[i-1]
        print(f"Coverage: {metrics.coverage:.2%}")
        print(f"Support: {metrics.support} samples")
        print(f"Target improvement: {metrics.target_improvement:.2%}")

if __name__ == "__main__":
    run_iris_example()
