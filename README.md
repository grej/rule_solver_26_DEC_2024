# Rule Solver

**Version:** 0.02
**Date:** December 27, 2024

Rule Solver is a Python-based pattern discovery system that finds interpretable rules that drive variables in desired directions. It can identify conditions that maximize/minimize continuous variables or predict categorical outcomes, using adaptive rule generation and rank-based scoring.

## Core Features

1. **Directional Pattern Discovery:**
   - Find rules that maximize or minimize numeric variables
   - Discover predictive patterns for categorical outcomes
   - Automatically balance between improvement magnitude and rule coverage

2. **Intelligent Rule Generation:**
   - Percentile-based range exploration
   - Density-aware sampling in feature space
   - Adaptive margin determination
   - Feature combination discovery

3. **Rich Visualization:**
   - Distribution comparisons with unicode histograms
   - Impact analysis for each rule
   - Feature-by-feature breakdowns
   - Detailed pruning history

4. **Performance Metrics:**
   - Direction score: Measures effectiveness in driving target variable
   - Coverage score: Ensures rules apply to meaningful subsets
   - Spread analysis: Evaluates tightness of patterns
   - Improvement tracking during pruning

## Example Output

For continuous targets:
```
Rule Impact Analysis
==================================================
Matching Samples: 45 (30.0% of data)

petal_width Distribution:
Matching samples median: 0.20

Matching samples:
  0.10 | █████                          |   5
  0.20 | ██████████████████████████████ |  26
  0.25 | ██████                         |   6

Non-matching samples median: 1.50
Improvement: +86.7%

Feature Distributions (Matching Samples):
petal_length:
  1.00 | ██                             |   1
  1.36 | ██████████████████████████████ |  12
  1.54 | █████████████████              |   7
```

For categorical targets:
```
species Distribution:
Matching samples:
setosa       | ████████████████████ | 100.0%

Non-matching samples:
versicolor   | █████████            | 47.6%
virginica    | █████████            | 47.6%

Target class improvement: +95.2%
```

## Getting Started

### Prerequisites
- Python 3.12+
- Conda or Miniconda

### Installation

1. Clone and setup:
```bash
git clone https://github.com/grej/rule_solver.git
cd rule_solver
conda env create -f environment.yml
conda activate rule_solver
```

2. Run example:
```bash
python main.py
```

### Usage Examples

```python
import pandas as pd
from rule_solver.rules import find_best_rules

# Load data
df = pd.read_parquet('./data/iris.parquet')

# Find rules that maximize a continuous variable
results = find_best_rules(df,
                         num_rules=3,
                         target_var='sepal_length',
                         direction='maximize')

# Find rules that minimize a continuous variable
results = find_best_rules(df,
                         num_rules=3,
                         target_var='petal_width',
                         direction='minimize')

# Find rules that predict a specific category
results = find_best_rules(df,
                         num_rules=3,
                         target_var='species',
                         direction='setosa')
```

## Project Structure

```
/
├── main.py                 # Entry point showing example usage
├── rule_solver/
│   ├── rules.py           # Rule generation and optimization
│   ├── scoring.py         # Directional scoring metrics
│   └── utils.py           # Visualization and formatting
└── data/
    └── iris.parquet       # Example dataset
```

## Development Status

Current focus areas:
- Expanding rule generation strategies
- Optimizing scoring for different variable types
- Enhancing visualization capabilities
- Adding more comprehensive testing

## Contributing

Contributions welcome! Key areas for improvement:
- Additional scoring methods
- Performance optimization for large datasets
- Extended visualization options
- Additional rule generation strategies

## License

This project is licensed under the MIT License.

## Acknowledgments

- Dataset: [Iris dataset](https://archive.ics.uci.edu/ml/datasets/iris)
- Libraries: Numpy, Pandas, PyArrow
