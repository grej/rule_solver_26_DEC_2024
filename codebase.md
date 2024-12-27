### DIRECTORY ./ FOLDER STRUCTURE ###
/
    flatten.py
    pyrightconfig.json
    environment.yml
    rules_output.txt
    scratch.py
    README.md
    codebase.md
    main.py
rule_solver/
    scoring.py
    rules.py
    utils.py
    __pycache__/
        rules.cpython-312.pyc
        scoring.cpython-312.pyc
        utils.cpython-312.pyc
tests/
    test_scoring.py
.ropeproject/
data/
    iris.parquet
### DIRECTORY ./ FOLDER STRUCTURE ###

### DIRECTORY ./ FLATTENED CONTENT ###
### ./flatten.py BEGIN ###
import os
import argparse

def printFolderStructure(directory, output_file):
    output_file.write(f"### DIRECTORY {directory} FOLDER STRUCTURE ###\n")
    for root, directories, files in os.walk(directory):
        level = root.replace(directory, '').count(os.sep)
        indent = ' ' * 4 * (level)
        output_file.write('{}{}/\n'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            output_file.write('{}{}\n'.format(subindent, f))
    output_file.write(f"### DIRECTORY {directory} FOLDER STRUCTURE ###\n\n")

def walkFolderTree(folder):
    for dirpath, dirnames, filenames in os.walk(folder):
        for filename in filenames:
            yield os.path.join(dirpath, filename)

def main():
    parser = argparse.ArgumentParser(description='Flattens a codebase.')
    parser.add_argument('--folders', nargs='*', help='Base folders to process')
    parser.add_argument('--system_instructions', action='store_true', help='Print system instructions')

    system_instructions = """## System Instructions for Language Model Assistance in Code Debugging

### Role Definition:
- **Act as a software engineer** tasked with assisting in debugging code.
- Provide insights, explanations, and solutions based on the provided codebase information.

### Codebase Markdown File Structure:
- The codebase markdown file represents the actual codebase structure and content.
- It begins with a directory tree representation:
  ```
  ### DIRECTORY path/to/file/tree FOLDER STRUCTURE ###
  (file tree representation)
  ### DIRECTORY path/to/file/tree FOLDER STRUCTURE ###
  ```
- Following the directory tree, the contents of each file are displayed:
  ```
  ### path/to/file1 BEGIN ###
  (content of file1)
  ### path/to/file1 END ###
  
  ### path/to/file2 BEGIN ###
  (content of file2)
  ### path/to/file2 END ###
  ```

### Guidelines for Interaction:
- Respond to queries based on the explicit content provided within the markdown file.
- Avoid making assumptions about the code without clear evidence presented in the file content.
- When seeking specific implementation details, refer to the corresponding section in the markdown file, for example:
  ```
  ### folder1/folder2/myfile.ts BEGIN ###
  (specific implementation details)
  ### folder1/folder2/myfile.ts END ###
  ```

### Objective:
- The primary objective is to facilitate effective debugging by providing accurate information and guidance strictly adhering to the content available in the markdown file."""

    args = parser.parse_args()

    if args.system_instructions:
        print(system_instructions)

        if not args.folders:
            return

    if args.folders:
        base_folders = args.folders
        with open('codebase.md', 'w') as output_file:
            for base_folder in base_folders:
                printFolderStructure(base_folder, output_file)
                
                output_file.write(f"### DIRECTORY {base_folder} FLATTENED CONTENT ###\n")
                for filepath in walkFolderTree(base_folder):
                    content = f"### {filepath} BEGIN ###\n"
                    
                    try:
                        with open(filepath, "r") as f:
                            content += f.read()
                        content += f"\n### {filepath} END ###\n\n"
                    except:
                        continue
                    
                    output_file.write(content)
                output_file.write(f"### DIRECTORY {base_folder} FLATTENED CONTENT ###\n")
    else:
        print("usage: main.py [-h] --folders FOLDERS [FOLDERS ...] [--system_instructions]")
        print("Error: the following arguments are required: --folders")

if __name__ == "__main__":
    main()

### ./flatten.py END ###

### ./pyrightconfig.json BEGIN ###
{
  "venvPath": "/Users/greg/miniconda3/envs",
  "venv": "rule_solver",
  "pythonPath": "/Users/greg/miniconda3/envs/rule_solver/bin/python"
}

### ./pyrightconfig.json END ###

### ./environment.yml BEGIN ###
name: rule_solver
channels:
  - conda-forge
  - defaults
dependencies:
  - appdirs=1.4.4=pyhd3eb1b0_0
  - atk-1.0=2.36.0=h7fe96df_0
  - atpublic=5.0=pyhd8ed1ab_1
  - aws-c-auth=0.8.0=h8bc59a9_15
  - aws-c-cal=0.8.1=hc8a0bd2_3
  - aws-c-common=0.10.6=h5505292_0
  - aws-c-compression=0.3.0=hc8a0bd2_5
  - aws-c-event-stream=0.5.0=h54f970a_11
  - aws-c-http=0.9.2=h96aa502_4
  - aws-c-io=0.15.3=haba67d1_5
  - aws-c-mqtt=0.11.0=h24f418c_12
  - aws-c-s3=0.7.7=h1be5864_0
  - aws-c-sdkutils=0.2.1=hc8a0bd2_4
  - aws-checksums=0.2.2=hc8a0bd2_4
  - aws-crt-cpp=0.29.7=h19a973c_7
  - aws-sdk-cpp=1.11.458=he0ff2e4_4
  - azure-core-cpp=1.14.0=hd50102c_0
  - azure-identity-cpp=1.10.0=hc602bab_0
  - azure-storage-blobs-cpp=12.13.0=h7585a09_1
  - azure-storage-common-cpp=12.8.0=h9ca1f76_1
  - azure-storage-files-datalake-cpp=12.12.0=hcdd55da_1
  - bidict=0.23.1=pyhd8ed1ab_1
  - brotli-python=1.0.9=py312h313beb8_8
  - bzip2=1.0.8=h99b78c6_7
  - c-ares=1.34.4=h5505292_0
  - ca-certificates=2024.12.14=hf0a4a13_0
  - cairo=1.18.2=h6a3b0d2_1
  - certifi=2024.12.14=py312hca03da5_0
  - charset-normalizer=3.3.2=pyhd3eb1b0_0
  - expat=2.6.4=h286801f_0
  - filelock=3.13.1=py312hca03da5_0
  - font-ttf-dejavu-sans-mono=2.37=hd3eb1b0_0
  - font-ttf-inconsolata=2.001=hcb22688_0
  - font-ttf-source-code-pro=2.030=hd3eb1b0_0
  - font-ttf-ubuntu=0.83=h8b1ccd4_0
  - fontconfig=2.15.0=h1383a14_1
  - fonts-anaconda=1=h8fa9717_0
  - fonts-conda-ecosystem=1=hd3eb1b0_0
  - freetype=2.12.1=hadb7bae_2
  - fribidi=1.0.10=h1a28f6b_0
  - fsspec=2024.6.1=py312hca03da5_0
  - gdk-pixbuf=2.42.12=h7ddc832_0
  - gettext=0.21.0=hbdbcc25_2
  - gflags=2.2.2=h313beb8_1
  - glib=2.82.2=hb1db9eb_0
  - glib-tools=2.82.2=h25d4a46_0
  - glog=0.7.1=heb240a5_0
  - gobject-introspection=1.78.1=py312hb338bcb_1
  - graphite2=1.3.14=hc377ac9_1
  - graphviz=2.50.0=h54e2d63_4
  - gtk2=2.24.33=h29ed485_2
  - gts=0.7.6=hde733a8_3
  - harfbuzz=10.1.0=h9df47df_0
  - humanize=3.10.0=pyhd3eb1b0_0
  - ibis-framework=9.5.0=hd8ed1ab_0
  - ibis-framework-core=9.5.0=pyhd8ed1ab_0
  - icu=75.1=hfee45f7_0
  - idna=3.7=py312hca03da5_0
  - importlib-metadata=8.5.0=py312hca03da5_0
  - importlib-resources=6.4.0=pyhd3eb1b0_0
  - importlib_resources=6.4.0=py312hca03da5_0
  - jinja2=3.1.4=py312hca03da5_1
  - joblib=1.4.2=py312hca03da5_0
  - krb5=1.21.3=hf3e1bf2_0
  - lerc=4.0.0=h313beb8_0
  - libabseil=20240722.0=cxx17_hf9b8971_1
  - libarrow=18.1.0=h4a2f8bd_6_cpu
  - libarrow-acero=18.1.0=hf07054f_6_cpu
  - libarrow-dataset=18.1.0=hf07054f_6_cpu
  - libarrow-substrait=18.1.0=h86344ea_6_cpu
  - libblas=3.9.0=26_osxarm64_openblas
  - libbrotlicommon=1.1.0=hd74edd7_2
  - libbrotlidec=1.1.0=hd74edd7_2
  - libbrotlienc=1.1.0=hd74edd7_2
  - libcblas=3.9.0=26_osxarm64_openblas
  - libcrc32c=1.1.2=hc377ac9_0
  - libcurl=8.11.1=h73640d1_0
  - libcxx=19.1.6=ha82da77_1
  - libdeflate=1.23=hec38601_0
  - libedit=3.1.20230828=h80987f9_0
  - libev=4.33=h1a28f6b_1
  - libevent=2.1.12=h02f6b3c_1
  - libexpat=2.6.4=h286801f_0
  - libffi=3.4.4=hca03da5_1
  - libgd=2.3.3=hac1b3a8_10
  - libgfortran=5.0.0=13_2_0_hd922786_3
  - libgfortran5=13.2.0=hf226fd6_3
  - libglib=2.82.2=h07bd6cf_0
  - libgoogle-cloud=2.32.0=h8d8be31_0
  - libgoogle-cloud-storage=2.32.0=h7081f7f_0
  - libgrpc=1.67.1=hc70892a_0
  - libiconv=1.17=h0d3ecfb_2
  - libintl=0.22.5=h8414b35_3
  - libintl-devel=0.22.5=h8414b35_3
  - libjpeg-turbo=3.0.3=h80987f9_0
  - liblapack=3.9.0=26_osxarm64_openblas
  - libllvm14=14.0.6=hd1a9a77_4
  - liblzma=5.6.3=h39f12f2_1
  - liblzma-devel=5.6.3=h39f12f2_1
  - libnghttp2=1.64.0=h6d7220d_0
  - libopenblas=0.3.28=openmp_hf332438_1
  - libparquet=18.1.0=h636d7b7_6_cpu
  - libpng=1.6.44=hc14010f_0
  - libprotobuf=5.28.2=h8f0b736_0
  - libre2-11=2024.07.02=h2348fd5_1
  - librsvg=2.58.4=h266df6f_2
  - libsqlite=3.47.2=h3f77e49_0
  - libssh2=1.11.1=h9cc3647_0
  - libthrift=0.21.0=h64651cc_0
  - libtiff=4.7.0=h551f018_3
  - libutf8proc=2.9.0=h5505292_1
  - libwebp-base=1.5.0=h2471fea_0
  - libxml2=2.13.5=h178c5d8_1
  - libzlib=1.3.1=h8359307_2
  - llvm-openmp=19.1.6=hdb05f8b_0
  - llvmlite=0.43.0=py312ha9ca408_1
  - lz4-c=1.10.0=h286801f_1
  - markdown-it-py=2.2.0=py312hca03da5_1
  - markupsafe=2.1.3=py312h80987f9_0
  - mdurl=0.1.0=py312hca03da5_0
  - multipledispatch=0.6.0=py312hca03da5_0
  - ncurses=6.5=h7bae524_1
  - ninja=1.12.1=hca03da5_0
  - ninja-base=1.12.1=h48ca7d4_0
  - numba=0.60.0=py312h41cea2d_0
  - numpy=2.0.2=py312h94ee1e1_1
  - openssl=3.4.0=h39f12f2_0
  - orc=2.0.3=hbcee414_1
  - packaging=24.2=py312hca03da5_0
  - pandas=2.2.3=py312hcd31e36_1
  - pango=1.54.0=h73f1e88_4
  - parsy=2.1=pyhd8ed1ab_1
  - pcre2=10.44=h297a79d_2
  - pins=0.8.7=pyhd8ed1ab_1
  - pip=24.3.1=pyh8b19718_2
  - pixman=0.44.2=h2f9eb0b_0
  - pyarrow=18.1.0=py312h1f38498_0
  - pyarrow-core=18.1.0=py312hc40f475_0_cpu
  - pyarrow-hotfix=0.6=pyhd8ed1ab_1
  - pygments=2.15.1=py312hca03da5_1
  - pysocks=1.7.1=py312hca03da5_0
  - python=3.12.8=hc22306f_1_cpython
  - python-dateutil=2.9.0.post0=pyhff2d567_1
  - python-duckdb=1.1.3=py312hd8f9ff3_0
  - python-graphviz=0.20.1=py312hca03da5_0
  - python-tzdata=2024.2=pyhd8ed1ab_1
  - python-xxhash=2.0.2=py312h80987f9_1
  - python_abi=3.12=5_cp312
  - pytz=2024.1=pyhd8ed1ab_0
  - pyyaml=6.0.2=py312h80987f9_0
  - re2=2024.07.02=hcd0e937_1
  - readline=8.2=h92ec313_1
  - regex=2024.9.11=py312h80987f9_0
  - requests=2.32.3=py312hca03da5_1
  - rich=13.9.4=py312hca03da5_0
  - setuptools=75.6.0=pyhff2d567_1
  - six=1.17.0=pyhd8ed1ab_0
  - snappy=1.2.1=h313beb8_0
  - sqlglot=25.10.0=py312hca03da5_0
  - sqlite=3.47.2=hd7222ec_0
  - tk=8.6.13=h5083fa2_1
  - toolz=0.12.0=py312hca03da5_0
  - typing-extensions=4.12.2=py312hca03da5_0
  - typing_extensions=4.12.2=py312hca03da5_0
  - tzdata=2024b=hc8b5060_0
  - urllib3=2.2.3=py312hca03da5_0
  - wheel=0.45.1=pyhd8ed1ab_1
  - xxhash=0.8.0=h1a28f6b_3
  - xz=5.6.3=h9a6d368_1
  - xz-gpl-tools=5.6.3=h9a6d368_1
  - xz-tools=5.6.3=h39f12f2_1
  - yaml=0.2.5=h1a28f6b_0
  - zipp=3.21.0=py312hca03da5_0
  - zlib=1.3.1=h8359307_2
  - zstd=1.5.6=hb46c0d2_0
prefix: /Users/greg/miniconda3/envs/rule_solver

### ./environment.yml END ###

### ./rules_output.txt BEGIN ###
Generated Rules Report
Date: 2024-12-26 23:27:34

Rule 1
==================================================
Rule Conditions:
  sepal_length: 4.3 to 6.4

Performance:
  Score: 0.360
  Coverage: 0.767 (115 samples)
  Dominant Class: setosa

Pruning Steps:
  Removed: sepal_width (improvement: 0.269)
  Removed: petal_length (improvement: 0.014)
  Removed: petal_width (improvement: 0.087)

Rule 2
==================================================
Rule Conditions:
  petal_length: 1.3 to 4.8

Performance:
  Score: 0.321
  Coverage: 0.633 (95 samples)
  Dominant Class: setosa

Pruning Steps:
  Removed: sepal_length (improvement: 0.116)
  Removed: sepal_width (improvement: 0.102)
  Removed: petal_width (improvement: 0.050)

Rule 3
==================================================
Rule Conditions:
  sepal_length: 5.6 to 6.7

Performance:
  Score: 0.270
  Coverage: 0.473 (71 samples)
  Dominant Class: versicolor

Pruning Steps:
  Removed: sepal_width (improvement: 0.042)
  Removed: petal_length (improvement: 0.067)
  Removed: petal_width (improvement: 0.139)

Rule 4
==================================================
Rule Conditions:
  species: virginica

Performance:
  Score: 0.167
  Coverage: 1.000 (150 samples)
  Dominant Class: setosa

Pruning Steps:
  Removed: petal_length (improvement: 0.019)
  Removed: petal_width (improvement: 0.056)
  Removed: sepal_length (improvement: 0.120)
  Removed: sepal_width (improvement: 0.040)

Rule 5
==================================================
Rule Conditions:
  petal_length: 1.6 to 3.3

Performance:
  Score: 0.083
  Coverage: 0.107 (16 samples)
  Dominant Class: setosa

Pruning Steps:
  Removed: sepal_width (improvement: 0.010)
  Removed: sepal_length (improvement: 0.020)
  Removed: petal_width (improvement: 0.054)


### ./rules_output.txt END ###

### ./scratch.py BEGIN ###
import pandas as pd
import os.path

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
parquet_path = './data/iris.parquet'

if not os.path.exists(parquet_path):
    # Also ensure the directory exists
    os.makedirs(os.path.dirname(parquet_path), exist_ok=True)

    # Download and save only if the file doesn't exist
    iris = pd.read_csv(url)
    iris.to_parquet(parquet_path)
    print("Created new parquet file")
else:
    print("Parquet file already exists")

iris = pd.read_parquet(parquet_path)

print(iris)

### ./scratch.py END ###

### ./README.md BEGIN ###
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

### ./README.md END ###

### ./codebase.md BEGIN ###
### DIRECTORY ./ FOLDER STRUCTURE ###
/
    flatten.py
    pyrightconfig.json
    environment.yml
    rules_output.txt
    scratch.py
    README.md
    codebase.md
    main.py
rule_solver/
    scoring.py
    rules.py
    utils.py
    __pycache__/
        rules.cpython-312.pyc
        scoring.cpython-312.pyc
        utils.cpython-312.pyc
tests/
    test_scoring.py
.ropeproject/
data/
    iris.parquet
### DIRECTORY ./ FOLDER STRUCTURE ###

### DIRECTORY ./ FLATTENED CONTENT ###
### ./flatten.py BEGIN ###
import os
import argparse

def printFolderStructure(directory, output_file):
    output_file.write(f"### DIRECTORY {directory} FOLDER STRUCTURE ###\n")
    for root, directories, files in os.walk(directory):
        level = root.replace(directory, '').count(os.sep)
        indent = ' ' * 4 * (level)
        output_file.write('{}{}/\n'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            output_file.write('{}{}\n'.format(subindent, f))
    output_file.write(f"### DIRECTORY {directory} FOLDER STRUCTURE ###\n\n")

def walkFolderTree(folder):
    for dirpath, dirnames, filenames in os.walk(folder):
        for filename in filenames:
            yield os.path.join(dirpath, filename)

def main():
    parser = argparse.ArgumentParser(description='Flattens a codebase.')
    parser.add_argument('--folders', nargs='*', help='Base folders to process')
    parser.add_argument('--system_instructions', action='store_true', help='Print system instructions')

    system_instructions = """## System Instructions for Language Model Assistance in Code Debugging

### Role Definition:
- **Act as a software engineer** tasked with assisting in debugging code.
- Provide insights, explanations, and solutions based on the provided codebase information.

### Codebase Markdown File Structure:
- The codebase markdown file represents the actual codebase structure and content.
- It begins with a directory tree representation:
  ```
  ### DIRECTORY path/to/file/tree FOLDER STRUCTURE ###
  (file tree representation)
  ### DIRECTORY path/to/file/tree FOLDER STRUCTURE ###
  ```
- Following the directory tree, the contents of each file are displayed:
  ```
  ### path/to/file1 BEGIN ###
  (content of file1)
  ### path/to/file1 END ###
  
  ### path/to/file2 BEGIN ###
  (content of file2)
  ### path/to/file2 END ###
  ```

### Guidelines for Interaction:
- Respond to queries based on the explicit content provided within the markdown file.
- Avoid making assumptions about the code without clear evidence presented in the file content.
- When seeking specific implementation details, refer to the corresponding section in the markdown file, for example:
  ```
  ### folder1/folder2/myfile.ts BEGIN ###
  (specific implementation details)
  ### folder1/folder2/myfile.ts END ###
  ```

### Objective:
- The primary objective is to facilitate effective debugging by providing accurate information and guidance strictly adhering to the content available in the markdown file."""

    args = parser.parse_args()

    if args.system_instructions:
        print(system_instructions)

        if not args.folders:
            return

    if args.folders:
        base_folders = args.folders
        with open('codebase.md', 'w') as output_file:
            for base_folder in base_folders:
                printFolderStructure(base_folder, output_file)
                
                output_file.write(f"### DIRECTORY {base_folder} FLATTENED CONTENT ###\n")
                for filepath in walkFolderTree(base_folder):
                    content = f"### {filepath} BEGIN ###\n"
                    
                    try:
                        with open(filepath, "r") as f:
                            content += f.read()
                        content += f"\n### {filepath} END ###\n\n"
                    except:
                        continue
                    
                    output_file.write(content)
                output_file.write(f"### DIRECTORY {base_folder} FLATTENED CONTENT ###\n")
    else:
        print("usage: main.py [-h] --folders FOLDERS [FOLDERS ...] [--system_instructions]")
        print("Error: the following arguments are required: --folders")

if __name__ == "__main__":
    main()

### ./flatten.py END ###

### ./pyrightconfig.json BEGIN ###
{
  "venvPath": "/Users/greg/miniconda3/envs",
  "venv": "rule_solver",
  "pythonPath": "/Users/greg/miniconda3/envs/rule_solver/bin/python"
}

### ./pyrightconfig.json END ###

### ./environment.yml BEGIN ###
name: rule_solver
channels:
  - conda-forge
  - defaults
dependencies:
  - appdirs=1.4.4=pyhd3eb1b0_0
  - atk-1.0=2.36.0=h7fe96df_0
  - atpublic=5.0=pyhd8ed1ab_1
  - aws-c-auth=0.8.0=h8bc59a9_15
  - aws-c-cal=0.8.1=hc8a0bd2_3
  - aws-c-common=0.10.6=h5505292_0
  - aws-c-compression=0.3.0=hc8a0bd2_5
  - aws-c-event-stream=0.5.0=h54f970a_11
  - aws-c-http=0.9.2=h96aa502_4
  - aws-c-io=0.15.3=haba67d1_5
  - aws-c-mqtt=0.11.0=h24f418c_12
  - aws-c-s3=0.7.7=h1be5864_0
  - aws-c-sdkutils=0.2.1=hc8a0bd2_4
  - aws-checksums=0.2.2=hc8a0bd2_4
  - aws-crt-cpp=0.29.7=h19a973c_7
  - aws-sdk-cpp=1.11.458=he0ff2e4_4
  - azure-core-cpp=1.14.0=hd50102c_0
  - azure-identity-cpp=1.10.0=hc602bab_0
  - azure-storage-blobs-cpp=12.13.0=h7585a09_1
  - azure-storage-common-cpp=12.8.0=h9ca1f76_1
  - azure-storage-files-datalake-cpp=12.12.0=hcdd55da_1
  - bidict=0.23.1=pyhd8ed1ab_1
  - brotli-python=1.0.9=py312h313beb8_8
  - bzip2=1.0.8=h99b78c6_7
  - c-ares=1.34.4=h5505292_0
  - ca-certificates=2024.12.14=hf0a4a13_0
  - cairo=1.18.2=h6a3b0d2_1
  - certifi=2024.12.14=py312hca03da5_0
  - charset-normalizer=3.3.2=pyhd3eb1b0_0
  - expat=2.6.4=h286801f_0
  - filelock=3.13.1=py312hca03da5_0
  - font-ttf-dejavu-sans-mono=2.37=hd3eb1b0_0
  - font-ttf-inconsolata=2.001=hcb22688_0
  - font-ttf-source-code-pro=2.030=hd3eb1b0_0
  - font-ttf-ubuntu=0.83=h8b1ccd4_0
  - fontconfig=2.15.0=h1383a14_1
  - fonts-anaconda=1=h8fa9717_0
  - fonts-conda-ecosystem=1=hd3eb1b0_0
  - freetype=2.12.1=hadb7bae_2
  - fribidi=1.0.10=h1a28f6b_0
  - fsspec=2024.6.1=py312hca03da5_0
  - gdk-pixbuf=2.42.12=h7ddc832_0
  - gettext=0.21.0=hbdbcc25_2
  - gflags=2.2.2=h313beb8_1
  - glib=2.82.2=hb1db9eb_0
  - glib-tools=2.82.2=h25d4a46_0
  - glog=0.7.1=heb240a5_0
  - gobject-introspection=1.78.1=py312hb338bcb_1
  - graphite2=1.3.14=hc377ac9_1
  - graphviz=2.50.0=h54e2d63_4
  - gtk2=2.24.33=h29ed485_2
  - gts=0.7.6=hde733a8_3
  - harfbuzz=10.1.0=h9df47df_0
  - humanize=3.10.0=pyhd3eb1b0_0
  - ibis-framework=9.5.0=hd8ed1ab_0
  - ibis-framework-core=9.5.0=pyhd8ed1ab_0
  - icu=75.1=hfee45f7_0
  - idna=3.7=py312hca03da5_0
  - importlib-metadata=8.5.0=py312hca03da5_0
  - importlib-resources=6.4.0=pyhd3eb1b0_0
  - importlib_resources=6.4.0=py312hca03da5_0
  - jinja2=3.1.4=py312hca03da5_1
  - joblib=1.4.2=py312hca03da5_0
  - krb5=1.21.3=hf3e1bf2_0
  - lerc=4.0.0=h313beb8_0
  - libabseil=20240722.0=cxx17_hf9b8971_1
  - libarrow=18.1.0=h4a2f8bd_6_cpu
  - libarrow-acero=18.1.0=hf07054f_6_cpu
  - libarrow-dataset=18.1.0=hf07054f_6_cpu
  - libarrow-substrait=18.1.0=h86344ea_6_cpu
  - libblas=3.9.0=26_osxarm64_openblas
  - libbrotlicommon=1.1.0=hd74edd7_2
  - libbrotlidec=1.1.0=hd74edd7_2
  - libbrotlienc=1.1.0=hd74edd7_2
  - libcblas=3.9.0=26_osxarm64_openblas
  - libcrc32c=1.1.2=hc377ac9_0
  - libcurl=8.11.1=h73640d1_0
  - libcxx=19.1.6=ha82da77_1
  - libdeflate=1.23=hec38601_0
  - libedit=3.1.20230828=h80987f9_0
  - libev=4.33=h1a28f6b_1
  - libevent=2.1.12=h02f6b3c_1
  - libexpat=2.6.4=h286801f_0
  - libffi=3.4.4=hca03da5_1
  - libgd=2.3.3=hac1b3a8_10
  - libgfortran=5.0.0=13_2_0_hd922786_3
  - libgfortran5=13.2.0=hf226fd6_3
  - libglib=2.82.2=h07bd6cf_0
  - libgoogle-cloud=2.32.0=h8d8be31_0
  - libgoogle-cloud-storage=2.32.0=h7081f7f_0
  - libgrpc=1.67.1=hc70892a_0
  - libiconv=1.17=h0d3ecfb_2
  - libintl=0.22.5=h8414b35_3
  - libintl-devel=0.22.5=h8414b35_3
  - libjpeg-turbo=3.0.3=h80987f9_0
  - liblapack=3.9.0=26_osxarm64_openblas
  - libllvm14=14.0.6=hd1a9a77_4
  - liblzma=5.6.3=h39f12f2_1
  - liblzma-devel=5.6.3=h39f12f2_1
  - libnghttp2=1.64.0=h6d7220d_0
  - libopenblas=0.3.28=openmp_hf332438_1
  - libparquet=18.1.0=h636d7b7_6_cpu
  - libpng=1.6.44=hc14010f_0
  - libprotobuf=5.28.2=h8f0b736_0
  - libre2-11=2024.07.02=h2348fd5_1
  - librsvg=2.58.4=h266df6f_2
  - libsqlite=3.47.2=h3f77e49_0
  - libssh2=1.11.1=h9cc3647_0
  - libthrift=0.21.0=h64651cc_0
  - libtiff=4.7.0=h551f018_3
  - libutf8proc=2.9.0=h5505292_1
  - libwebp-base=1.5.0=h2471fea_0
  - libxml2=2.13.5=h178c5d8_1
  - libzlib=1.3.1=h8359307_2
  - llvm-openmp=19.1.6=hdb05f8b_0
  - llvmlite=0.43.0=py312ha9ca408_1
  - lz4-c=1.10.0=h286801f_1
  - markdown-it-py=2.2.0=py312hca03da5_1
  - markupsafe=2.1.3=py312h80987f9_0
  - mdurl=0.1.0=py312hca03da5_0
  - multipledispatch=0.6.0=py312hca03da5_0
  - ncurses=6.5=h7bae524_1
  - ninja=1.12.1=hca03da5_0
  - ninja-base=1.12.1=h48ca7d4_0
  - numba=0.60.0=py312h41cea2d_0
  - numpy=2.0.2=py312h94ee1e1_1
  - openssl=3.4.0=h39f12f2_0
  - orc=2.0.3=hbcee414_1
  - packaging=24.2=py312hca03da5_0
  - pandas=2.2.3=py312hcd31e36_1
  - pango=1.54.0=h73f1e88_4
  - parsy=2.1=pyhd8ed1ab_1
  - pcre2=10.44=h297a79d_2
  - pins=0.8.7=pyhd8ed1ab_1
  - pip=24.3.1=pyh8b19718_2
  - pixman=0.44.2=h2f9eb0b_0
  - pyarrow=18.1.0=py312h1f38498_0
  - pyarrow-core=18.1.0=py312hc40f475_0_cpu
  - pyarrow-hotfix=0.6=pyhd8ed1ab_1
  - pygments=2.15.1=py312hca03da5_1
  - pysocks=1.7.1=py312hca03da5_0
  - python=3.12.8=hc22306f_1_cpython
  - python-dateutil=2.9.0.post0=pyhff2d567_1
  - python-duckdb=1.1.3=py312hd8f9ff3_0
  - python-graphviz=0.20.1=py312hca03da5_0
  - python-tzdata=2024.2=pyhd8ed1ab_1
  - python-xxhash=2.0.2=py312h80987f9_1
  - python_abi=3.12=5_cp312
  - pytz=2024.1=pyhd8ed1ab_0
  - pyyaml=6.0.2=py312h80987f9_0
  - re2=2024.07.02=hcd0e937_1
  - readline=8.2=h92ec313_1
  - regex=2024.9.11=py312h80987f9_0
  - requests=2.32.3=py312hca03da5_1
  - rich=13.9.4=py312hca03da5_0
  - setuptools=75.6.0=pyhff2d567_1
  - six=1.17.0=pyhd8ed1ab_0
  - snappy=1.2.1=h313beb8_0
  - sqlglot=25.10.0=py312hca03da5_0
  - sqlite=3.47.2=hd7222ec_0
  - tk=8.6.13=h5083fa2_1
  - toolz=0.12.0=py312hca03da5_0
  - typing-extensions=4.12.2=py312hca03da5_0
  - typing_extensions=4.12.2=py312hca03da5_0
  - tzdata=2024b=hc8b5060_0
  - urllib3=2.2.3=py312hca03da5_0
  - wheel=0.45.1=pyhd8ed1ab_1
  - xxhash=0.8.0=h1a28f6b_3
  - xz=5.6.3=h9a6d368_1
  - xz-gpl-tools=5.6.3=h9a6d368_1
  - xz-tools=5.6.3=h39f12f2_1
  - yaml=0.2.5=h1a28f6b_0
  - zipp=3.21.0=py312hca03da5_0
  - zlib=1.3.1=h8359307_2
  - zstd=1.5.6=hb46c0d2_0
prefix: /Users/greg/miniconda3/envs/rule_solver

### ./environment.yml END ###


### ./codebase.md END ###

### ./main.py BEGIN ###
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

### ./main.py END ###

### ./rule_solver/scoring.py BEGIN ###
import numpy as np
from typing import Dict, Union

def fast_ranks(x):
    """Simple ranking function using numpy only"""
    temp = x.argsort()
    ranks = np.empty_like(temp)
    ranks[temp] = np.arange(len(x))
    return (ranks + 1) / (len(x) + 1)  # Add 1 to avoid 0s

def calculate_rank_score(df, rule, target_column='species') \
                        -> Dict[str, Union[float, int, str, None]]:
    """Calculate hybrid score using rank-based metrics"""
    def matches_rule(row, rule):
        for feature, value in rule.items():
            if feature == target_column:
                continue
            if isinstance(value, tuple):
                min_val, max_val = value
                if not (min_val <= row[feature] <= max_val):
                    return False
            else:
                if row[feature] != value:
                    return False
        return True

    matching_mask = df.apply(lambda row: matches_rule(row, rule), axis=1)

    if matching_mask.sum() == 0:
        return {
            'score': 0.0,
            'rank_score': 0.0,
            'class_score': 0.0,
            'coverage': 0.0,
            'matching_samples': 0,
            'dominant_class': None
        }

    matching_df = df[matching_mask]
    non_matching_df = df[~matching_mask]

    # Compute rank scores for continuous features
    continuous_features = [f for f, v in rule.items() if isinstance(v, tuple)]
    rank_scores = []

    for feature in continuous_features:
        values = df[feature].values
        normalized_ranks = fast_ranks(values)

        matching_ranks = normalized_ranks[matching_mask]
        nonmatching_ranks = normalized_ranks[~matching_mask]

        # Use numpy percentile instead of median for better performance
        rank_separation = abs(np.percentile(matching_ranks, 50) -
                            np.percentile(nonmatching_ranks, 50))
        rank_scores.append(1 - rank_separation)

    continuous_score = np.mean(rank_scores) if rank_scores else 0

    # Categorical scoring
    class_counts = matching_df[target_column].value_counts()
    dominant_class = class_counts.index[0]
    categorical_score = class_counts.iloc[0] / len(matching_df)

    coverage = matching_mask.sum() / len(df)
    final_score = (continuous_score + categorical_score) * coverage / 2

    return {
        'score': final_score,
        'rank_score': continuous_score,
        'class_score': categorical_score,
        'coverage': coverage,
        'matching_samples': matching_mask.sum(),
        'dominant_class': dominant_class,
        'feature_scores': dict(zip(continuous_features, rank_scores))
    }

def score_improvement(new_score, base_score, new_coverage, base_coverage,
                     coverage_weight=0.1):
    """Calculate improvement in score with coverage penalty/bonus"""
    return (new_score - base_score) + coverage_weight * (new_coverage - base_coverage)

### ./rule_solver/scoring.py END ###

### ./rule_solver/rules.py BEGIN ###
# rules.py
import numpy as np
from .utils import infer_feature_types, matches_rule
from .scoring import calculate_rank_score, score_improvement

def create_rule(point1, point2, continuous_features, categorical_features):
    """Create a rule from two points"""
    rule = {}
    for feature in continuous_features:
        min_val = min(point1[feature], point2[feature])
        max_val = max(point1[feature], point2[feature])
        rule[feature] = (min_val, max_val)
    for feature in categorical_features:
        if point1[feature] == point2[feature]:
            rule[feature] = point1[feature]
    return rule

def generate_rules(df, num_rules=100, target_column='species'):
    """Generate initial rules by sampling points"""
    continuous_features, categorical_features = infer_feature_types(df)
    continuous_features.remove(target_column) if target_column in continuous_features else None

    rules = []
    for _ in range(num_rules):
        points = df.sample(2, replace=False)
        rule = create_rule(points.iloc[0], points.iloc[1],
                         continuous_features, categorical_features)
        rules.append(rule)
    return rules

def prune_rule(df, rule, target_column='species', min_improvement=-0.01):
    """Prune conditions using rank-based scoring"""
    base_metrics = calculate_rank_score(df, rule, target_column)

    # Explicitly check if base_metrics is None and handle the case
    if base_metrics is None:
        raise ValueError("Base metrics cannot be None. Ensure calculate_rank_score always returns a valid dictionary.")

    current_rule = rule.copy()
    pruning_history = []

    while True:
        best_improvement = -float('inf')
        best_feature_to_remove = None
        best_new_metrics = None

        for feature in list(current_rule.keys()):
            if feature == target_column:
                continue

            test_rule = {k: v for k, v in current_rule.items() if k != feature}
            if not test_rule:
                continue

            test_metrics = calculate_rank_score(df, test_rule, target_column)

            # Ensure test_metrics is valid
            if test_metrics is None:
                continue

            improvement = score_improvement(
                test_metrics['score'],
                base_metrics['score'],
                test_metrics['coverage'],
                base_metrics['coverage']
            )

            if improvement > best_improvement:
                best_improvement = improvement
                best_feature_to_remove = feature
                best_new_metrics = test_metrics

        if best_improvement < min_improvement or best_feature_to_remove is None:
            break

        current_rule.pop(best_feature_to_remove)
        base_metrics = best_new_metrics

        pruning_history.append({
            'removed_feature': best_feature_to_remove,
            'improvement': best_improvement,
            'metrics': best_new_metrics,
            'current_rule': current_rule.copy()
        })

    return current_rule, base_metrics, pruning_history


def find_best_rules(df, num_rules=5, target_column='species'):
    """Generate, prune and rank rules"""
    rules = generate_rules(df, num_rules, target_column)
    pruned_rules = []

    for rule in rules:
        pruned_rule, metrics, history = prune_rule(df, rule, target_column)
        pruned_rules.append((pruned_rule, metrics, history))

    # Sort by score
    pruned_rules.sort(key=lambda x: x[1]['score'], reverse=True)
    return pruned_rules

### ./rule_solver/rules.py END ###

### ./rule_solver/utils.py BEGIN ###
# utils.py
# import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype

def infer_feature_types(df):
    """Split features into continuous and categorical"""
    continuous_features = []
    categorical_features = []
    for col in df.columns:
        if is_numeric_dtype(df[col]):
            continuous_features.append(col)
        else:
            categorical_features.append(col)
    return continuous_features, categorical_features

def matches_rule(row, rule, target_column):
    """Check if a row matches rule conditions"""
    for feature, value in rule.items():
        if feature == target_column:
            continue
        if isinstance(value, tuple):
            min_val, max_val = value
            if not (min_val <= row[feature] <= max_val):
                return False
        else:
            if row[feature] != value:
                return False
    return True

# utils.py
def format_rule_for_human(rule, metrics, history):
    """Format a rule and its metrics into a readable string"""
    lines = []
    lines.append("=" * 50)

    # Format conditions
    lines.append("Rule Conditions:")
    for feature, value in rule.items():
        if isinstance(value, tuple):
            lines.append(f"  {feature}: {value[0]:.1f} to {value[1]:.1f}")
        else:
            lines.append(f"  {feature}: {value}")

    # Format key metrics
    lines.append("\nPerformance:")
    lines.append(f"  Score: {metrics['score']:.3f}")
    lines.append(f"  Coverage: {metrics['coverage']:.3f} ({metrics['matching_samples']} samples)")
    lines.append(f"  Dominant Class: {metrics['dominant_class']}")

    # Format pruning history
    if history:
        lines.append("\nPruning Steps:")
        for step in history:
            lines.append(f"  Removed: {step['removed_feature']} "
                        f"(improvement: {step['improvement']:.3f})")

    return "\n".join(lines) + "\n"

def save_rules_to_file(rules, filename='rules_output.txt'):
    """Save rules to a text file"""
    with open(filename, 'w') as f:
        f.write(f"Generated Rules Report\n")
        f.write(f"Date: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

        for i, (rule, metrics, history) in enumerate(rules, 1):
            f.write(f"Rule {i}\n")
            f.write(format_rule_for_human(rule, metrics, history))
            f.write("\n")

### ./rule_solver/utils.py END ###

### ./tests/test_scoring.py BEGIN ###

### ./tests/test_scoring.py END ###

### DIRECTORY ./ FLATTENED CONTENT ###
