Rule Solver Attempt - 26 DEC 2024

---

# Rule Solver

**Version:** 0.01
**Date:** December 26, 2024

Rule Solver is a Python-based tool that discovers meaningful classification rules in structured datasets. It uses a novel rank-based scoring approach that naturally handles both continuous and categorical features, focusing on finding rules that achieve both good separation between classes and high recall.

---

## Core Concepts

1. **Rank-Based Scoring:**
   - Uses normalized ranks instead of raw values
   - Naturally handles outliers and different scales
   - Combines separation quality with class recall
   - No arbitrary thresholds or minimum feature counts

2. **Rule Discovery:**
   - Naturally discovers multi-dimensional rules when needed
   - Keeps multiple features only when they improve class separation
   - Optimizes for both precision (good separation) and recall (class coverage)
   - Handles continuous and categorical features uniformly

3. **Performance Metrics:**
   - Rank separation: How well features divide classes
   - Class recall: Proportion of target class captured
   - Feature interaction: How features work together
   - Coverage: Overall rule applicability

4. **Rule Optimization:**
   - Removes features only when they don't contribute to separation
   - Maintains complex rules when needed for good classification
   - Balances simplicity with performance
   - No arbitrary dimensional constraints
---

## File Structure

```
/
    flatten.py               # Script for flattening directory structure and generating codebase markdown.
    pyrightconfig.json       # Pyright configuration for type checking.
    environment.yml          # Conda environment file specifying dependencies.
    rules_output.txt         # Generated rules report.
    scratch.py               # Script to download and process the Iris dataset.
    README.md                # Documentation for the project.
    codebase.md              # Markdown representation of the codebase structure.
    main.py                  # Entry point to execute the rule generation pipeline.
rule_solver/
    scoring.py               # Implements scoring logic for rule evaluation.
    rules.py                 # Handles rule generation and pruning.
    utils.py                 # Utility functions for feature inference and formatting.
tests/
    test_scoring.py          # Placeholder for unit tests (to be implemented).
.ropeproject/                # Configuration files for Rope, a Python refactoring library.
data/
    iris.parquet             # Preprocessed Iris dataset.
```

---

## Getting Started

### Prerequisites

- Python 3.12 or higher
- Conda or Miniconda for environment management

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/rule_solver.git
   cd rule_solver
   ```

2. Create and activate the Conda environment:
   ```bash
   conda env create -f environment.yml
   conda activate rule_solver
   ```

3. Ensure all dependencies are installed:
   ```bash
   conda install --file environment.yml
   ```

### Running the Application

1. Download and preprocess the Iris dataset:
   ```bash
   python scratch.py
   ```

2. Execute the main script to generate and evaluate rules:
   ```bash
   python main.py
   ```

3. View the results in `rules_output.txt`.

---

## Example Output

Sample output from `rules_output.txt`:
```
Rule 1
==================================================
Rule Conditions:
  sepal_width: 2.5 to 3.9
  petal_length: 1.3 to 5.8

Performance:
  Score: 0.510
  Coverage: 0.793 (119 samples)
  Dominant Class: setosa

Pruning Steps:
  Removed: sepal_length (improvement: 0.058)
  Removed: petal_width (improvement: 0.247)
```

---

## Development

### Code Overview

- **`scoring.py`:** Implements rank-based scoring for continuous and categorical features.
- **`rules.py`:** Handles rule creation, optimization, and ranking.
- **`utils.py`:** Provides helper functions for data processing and rule formatting.

### Testing

Unit tests are located in the `tests/` directory. To run the tests:
```bash
pytest tests/
```

---

## Contribution

Contributions are welcome! Please fork the repository, create a feature branch, and submit a pull request.

---

## License

This project is licensed under the MIT License.

---

## Acknowledgments

- Dataset: [Iris dataset](https://archive.ics.uci.edu/ml/datasets/iris)
- Libraries: Numpy, Pandas, PyArrow

---

Let me know if you'd like any changes or additions!
