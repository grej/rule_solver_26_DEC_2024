### DIRECTORY ./ FOLDER STRUCTURE ###
/
    rules_petal_width_min.txt
    flatten.py
    pyrightconfig.json
    environment.yml
    rules_output.txt
    scratch.py
    README.md
    .gitignore
    rules_sepal_length_max.txt
    rules_species_setosa.txt
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
.git/
    config
    HEAD
    description
    index
    COMMIT_EDITMSG
    objects/
        68/
            f2e0bca5dd97fcdc23d2bc68d6855cc499e3ff
        03/
            baecc77454b2fd911e402afd5d7094a8a22402
        5f/
            aace3f5e990aedd3515f4684baa1b0c42b3eb5
        b5/
            80cc051b971e5f0f72a72b5f77d842fba2df02
        bc/
            4a9b9a5f5ae24b038af4eace5a81a48e61ef06
        ed/
            14e0dbf1a5496cc261dea900c177f56d68b472
        pack/
        11/
            1759cb4456fb8584590f2d213ad7fc91bfcd2d
        info/
        97/
            8a069de0dd419347d51915e064d5990dc822ef
        de/
            d07694bafbb54f6a5cf665fe4c451df7208fba
        e6/
            9de29bb2d1d6434b8b29ae775ad8c2e48c5391
        46/
            f96881377dfb189663a30da2c74f70936be57a
        1b/
            364b85a1ad09662ccd3c84c3b7761fdfad987e
        1e/
            d185a4eb81eb6680331d1ae056b10f6ac362b2
        4a/
            2a7a675d4df24c519ce7f5387b024957209d79
        24/
            eca2093c08afa5ceb327bbd3a482772848c612
        8b/
            016d807b83885ba41eb31604f24d3f36861de2
        13/
            ee03e099613e788af99a6a2241be1a1266ff8e
        7a/
            09c1ac006e17513b735925830315ad73b67391
        22/
            852ecbe03f5f140903efd03bfe1e954bf3b51e
    info/
        exclude
    logs/
        HEAD
        refs/
            heads/
                main
            remotes/
                origin/
                    main
    hooks/
        commit-msg.sample
        pre-rebase.sample
        pre-commit.sample
        applypatch-msg.sample
        fsmonitor-watchman.sample
        pre-receive.sample
        prepare-commit-msg.sample
        post-update.sample
        pre-merge-commit.sample
        pre-applypatch.sample
        pre-push.sample
        update.sample
        push-to-checkout.sample
    refs/
        heads/
            main
        tags/
        remotes/
            origin/
                main
data/
    iris.parquet
### DIRECTORY ./ FOLDER STRUCTURE ###

### DIRECTORY ./ FLATTENED CONTENT ###
### ./rules_petal_width_min.txt BEGIN ###
Generated Rules Report
Target: petal_width (minimize)
Date: 2024-12-27 12:51:53

Rule 1
==================================================
Rule Conditions:
  sepal_length: 3.4 to 5.5
  petal_length: -0.9 to 3.5
  species: setosa

Performance:
  Score: 0.489
  Direction Score: 0.867
  Coverage: 0.300 (45 samples)

Target Variable Statistics:
  Matching Median: 0.200
  Non-matching Median: 1.500

Pruning Steps:
  Removed: sepal_width (improvement: 0.076)

Distribution Analysis:
Rule Impact Analysis
==================================================

Matching Samples: 45 (30.0% of data)

petal_width Distribution:
Matching samples median: 0.20

Matching samples:
  0.10 | █████                          |   5
  0.15 |                                |   0
  0.20 | ██████████████████████████████ |  26
  0.25 | ██████                         |   6
  0.30 |                                |   0
  0.35 |                                |   0
  0.40 | ██████                         |   6
  0.45 |                                |   0
  0.50 | █                              |   1
  0.55 | █                              |   1

Non-matching samples median: 1.50
Non-matching samples:
  0.20 | ███████                        |   5
  0.43 |                                |   0
  0.66 |                                |   0
  0.89 | ███████████████                |  10
  1.12 | ███████████████████████████    |  18
  1.35 | ██████████████████████████████ |  20
  1.58 | ███████████████████████████    |  18
  1.81 | ████████████████               |  11
  2.04 | █████████████                  |   9
  2.27 | █████████████████████          |  14

Improvement: +86.7%

Feature Distributions (Matching Samples):

sepal_length:
  4.30 | ███████████████                |   4
  4.41 | ███                            |   1
  4.52 | ███████████████                |   4
  4.63 | ███████                        |   2
  4.74 | ██████████████████             |   5
  4.85 | ███████████████                |   4
  4.96 | ██████████████████████████████ |   8
  5.07 | ██████████████████████████████ |   8
  5.18 | ███████████                    |   3
  5.29 | ██████████████████████         |   6
Rule range: [3.35, 5.45]

petal_length:
  1.00 | ██                             |   1
  1.09 | ██                             |   1
  1.18 | ██                             |   1
  1.27 | ███████████████                |   6
  1.36 | ██████████████████████████████ |  12
  1.45 | ██████████████████████████████ |  12
  1.54 | █████████████████              |   7
  1.63 | ███████                        |   3
  1.72 |                                |   0
  1.81 | █████                          |   2
Rule range: [-0.90, 3.50]

Rule 2
==================================================
Rule Conditions:
  petal_length: 1.5 to 5.3

Performance:
  Score: 0.235
  Direction Score: 0.278
  Coverage: 0.640 (96 samples)

Target Variable Statistics:
  Matching Median: 1.300
  Non-matching Median: 1.800

Distribution Analysis:
Rule Impact Analysis
==================================================

Matching Samples: 96 (64.0% of data)

petal_width Distribution:
Matching samples median: 1.30

Matching samples:
  0.10 | ███████████████████████████    |  18
  0.33 | ██████████                     |   7
  0.56 | █                              |   1
  0.79 | ██████████                     |   7
  1.02 | ████████████                   |   8
  1.25 | ██████████████████████████████ |  20
  1.48 | █████████████████████████      |  17
  1.71 | ███████████████                |  10
  1.94 | ██████                         |   4
  2.17 | ██████                         |   4

Non-matching samples median: 1.80
Non-matching samples:
  0.10 | ██████████████████████████████ |  23
  0.34 | █                              |   1
  0.58 |                                |   0
  0.82 |                                |   0
  1.06 |                                |   0
  1.30 | █                              |   1
  1.54 | █                              |   1
  1.78 | ███████████                    |   9
  2.02 | ███████████                    |   9
  2.26 | █████████████                  |  10

Improvement: +27.8%

Feature Distributions (Matching Samples):

petal_length:
  1.50 | ██████████████████████████████ |  24
  1.88 | ██                             |   2
  2.26 |                                |   0
  2.64 | █                              |   1
  3.02 | ██                             |   2
  3.40 | █████                          |   4
  3.78 | ███████████████                |  12
  4.16 | ██████████████████████         |  18
  4.54 | █████████████████████          |  17
  4.92 | ████████████████████           |  16
Rule range: [1.50, 5.32]

Rule 3
==================================================
Rule Conditions:
  petal_length: 1.4 to 5.8

Performance:
  Score: 0.177
  Direction Score: 0.278
  Coverage: 0.840 (126 samples)

Target Variable Statistics:
  Matching Median: 1.300
  Non-matching Median: 1.800

Distribution Analysis:
Rule Impact Analysis
==================================================

Matching Samples: 126 (84.0% of data)

petal_width Distribution:
Matching samples median: 1.30

Matching samples:
  0.10 | ████████████████████████████   |  31
  0.34 | ██████                         |   7
  0.58 |                                |   1
  0.82 | ██████                         |   7
  1.06 | ███████                        |   8
  1.30 | ██████████████████████████████ |  33
  1.54 | █████                          |   6
  1.78 | ████████████████               |  18
  2.02 | █████                          |   6
  2.26 | ████████                       |   9

Non-matching samples median: 1.80
Non-matching samples:
  0.10 | ██████████████████████████████ |  10
  0.34 | ███                            |   1
  0.58 |                                |   0
  0.82 |                                |   0
  1.06 |                                |   0
  1.30 |                                |   0
  1.54 |                                |   0
  1.78 | ███████████████                |   5
  2.02 | █████████                      |   3
  2.26 | ███████████████                |   5

Improvement: +27.8%

Feature Distributions (Matching Samples):

petal_length:
  1.40 | ██████████████████████████████ |  37
  1.84 | █                              |   2
  2.28 |                                |   0
  2.72 |                                |   1
  3.16 | ███                            |   4
  3.60 | ████████                       |  11
  4.04 | ██████████                     |  13
  4.48 | ████████████████████           |  25
  4.92 | ████████████                   |  16
  5.36 | █████████████                  |  17
Rule range: [1.40, 5.80]


### ./rules_petal_width_min.txt END ###

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
Date: 2024-12-27 12:33:18

Rule 1
==================================================
Rule Conditions:
  petal_length: 3.4 to 7.8
  petal_width: 0.8 to 2.8
  species: virginica

Performance:
  Score: 0.939
  Coverage: 0.647 (97 samples)
  Dominant Class: virginica
  Separation Score: 0.425
  Recall Score: 1.000
  Purity: 0.515

Pruning Steps:
  Removed: sepal_length (improvement: 0.121)
  Removed: sepal_width (improvement: 0.124)

Distribution Analysis:
Rule Distribution Analysis
==================================================

Matching Samples: 97 (64.7% of data)

Class Distribution:
virginica    | ████████████████████ |  50 (51.5%)
versicolor   | ██████████████████   |  47 (48.5%)

Feature Distributions (Matching Samples):

petal_length:
  3.50 | ████████                       |   5
  3.84 | ██████████████████             |  11
  4.18 | ██████████████████████████████ |  18
  4.52 | ████████████████████           |  12
  4.86 | ████████████████████████████   |  17
  5.20 | ███████████████                |   9
  5.54 | ████████████████████           |  12
  5.88 | ███████████                    |   7
  6.22 | ███                            |   2
  6.56 | ██████                         |   4
Rule range: [3.40, 7.80]

petal_width:
  1.00 | ██████████                     |   7
  1.15 | ███████                        |   5
  1.30 | ██████████████████████████████ |  21
  1.45 | █████████████████              |  12
  1.60 | ████████                       |   6
  1.75 | █████████████████              |  12
  1.90 | ███████████████                |  11
  2.05 | ████████                       |   6
  2.20 | ███████████████                |  11
  2.35 | ████████                       |   6
Rule range: [0.80, 2.80]

Rule 2
==================================================
Rule Conditions:
  petal_length: 1.3 to 1.7

Performance:
  Score: 0.923
  Coverage: 0.293 (44 samples)
  Dominant Class: setosa
  Separation Score: 0.412
  Recall Score: 0.880
  Purity: 1.000

Pruning Steps:
  Removed: petal_width (improvement: 0.067)
  Removed: sepal_length (improvement: 0.057)
  Removed: sepal_width (improvement: 0.092)

Distribution Analysis:
Rule Distribution Analysis
==================================================

Matching Samples: 44 (29.3% of data)

Class Distribution:
setosa       | ████████████████████ |  44 (100.0%)

Feature Distributions (Matching Samples):

petal_length:
  1.30 | ████████████████               |   7
  1.34 |                                |   0
  1.38 | ██████████████████████████████ |  13
  1.42 |                                |   0
  1.46 |                                |   0
  1.50 | ██████████████████████████████ |  13
  1.54 |                                |   0
  1.58 | ████████████████               |   7
  1.62 |                                |   0
  1.66 | █████████                      |   4
Rule range: [1.30, 1.70]

Rule 3
==================================================
Rule Conditions:
  petal_length: 1.3 to 1.6

Performance:
  Score: 0.874
  Coverage: 0.267 (40 samples)
  Dominant Class: setosa
  Separation Score: 0.416
  Recall Score: 0.800
  Purity: 1.000

Pruning Steps:
  Removed: sepal_length (improvement: 0.071)
  Removed: sepal_width (improvement: 0.135)
  Removed: petal_width (improvement: 0.130)

Distribution Analysis:
Rule Distribution Analysis
==================================================

Matching Samples: 40 (26.7% of data)

Class Distribution:
setosa       | ████████████████████ |  40 (100.0%)

Feature Distributions (Matching Samples):

petal_length:
  1.30 | ████████████████               |   7
  1.33 |                                |   0
  1.36 |                                |   0
  1.39 | ██████████████████████████████ |  13
  1.42 |                                |   0
  1.45 |                                |   0
  1.48 | ██████████████████████████████ |  13
  1.51 |                                |   0
  1.54 |                                |   0
  1.57 | ████████████████               |   7
Rule range: [1.30, 1.60]

Rule 4
==================================================
Rule Conditions:
  petal_length: 4.9 to 6.3

Performance:
  Score: 0.871
  Coverage: 0.307 (46 samples)
  Dominant Class: virginica
  Separation Score: 0.406
  Recall Score: 0.840
  Purity: 0.913

Pruning Steps:
  Removed: sepal_width (improvement: 0.095)
  Removed: petal_width (improvement: 0.072)
  Removed: sepal_length (improvement: 0.062)

Distribution Analysis:
Rule Distribution Analysis
==================================================

Matching Samples: 46 (30.7% of data)

Class Distribution:
virginica    | ████████████████████ |  42 (91.3%)
versicolor   | █                    |   4 (8.7%)

Feature Distributions (Matching Samples):

petal_length:
  4.90 | ██████████████████████████████ |   9
  5.04 | ██████████████████████████     |   8
  5.18 | █████████████                  |   4
  5.32 | ██████                         |   2
  5.46 | ██████████                     |   3
  5.60 | ██████████████████████████████ |   9
  5.74 | ██████████                     |   3
  5.88 | █████████████                  |   4
  6.02 | ██████████                     |   3
  6.16 | ███                            |   1
Rule range: [4.90, 6.31]

Rule 5
==================================================
Rule Conditions:
  petal_length: 5.1 to 6.0

Performance:
  Score: 0.755
  Coverage: 0.220 (33 samples)
  Dominant Class: virginica
  Separation Score: 0.396
  Recall Score: 0.640
  Purity: 0.970

Pruning Steps:
  Removed: sepal_width (improvement: 0.077)
  Removed: petal_width (improvement: 0.084)
  Removed: sepal_length (improvement: 0.056)

Distribution Analysis:
Rule Distribution Analysis
==================================================

Matching Samples: 33 (22.0% of data)

Class Distribution:
virginica    | ████████████████████ |  32 (97.0%)
versicolor   |                      |   1 (3.0%)

Feature Distributions (Matching Samples):

petal_length:
  5.10 | ██████████████████████████████ |   8
  5.19 | ███████                        |   2
  5.28 | ███████                        |   2
  5.37 | ███████                        |   2
  5.46 | ███████████                    |   3
  5.55 | ██████████████████████         |   6
  5.64 | ███████████                    |   3
  5.73 | ███████████                    |   3
  5.82 | ███████                        |   2
  5.91 | ███████                        |   2
Rule range: [5.10, 6.00]


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

### ./.gitignore BEGIN ###
__pycache__/
*.pyc
.ropeproject/

### ./.gitignore END ###

### ./rules_sepal_length_max.txt BEGIN ###
Generated Rules Report
Target: sepal_length (maximize)
Date: 2024-12-27 12:51:53

Rule 1
==================================================
Rule Conditions:
  sepal_width: 2.2 to 3.4
  petal_length: 2.9 to 7.3
  petal_width: 1.4 to 3.4
  species: virginica

Performance:
  Score: 0.172
  Direction Score: 0.182
  Coverage: 0.293 (44 samples)

Target Variable Statistics:
  Matching Median: 6.500
  Non-matching Median: 5.500

Distribution Analysis:
Rule Impact Analysis
==================================================

Matching Samples: 44 (29.3% of data)

sepal_length Distribution:
Matching samples median: 6.50

Matching samples:
  4.90 | ███                            |   1
  5.18 |                                |   0
  5.46 | ██████                         |   2
  5.74 | ████████████████               |   5
  6.02 | ██████████████████████████     |   8
  6.30 | ██████████████████████████████ |   9
  6.58 | ███████████████████████        |   7
  6.86 | █████████████                  |   4
  7.14 | █████████████                  |   4
  7.42 | █████████████                  |   4

Non-matching samples median: 5.50
Non-matching samples:
  4.30 | ██████████                     |   9
  4.66 | ██████████████████████████     |  22
  5.02 | ████████████████               |  14
  5.38 | ██████████████████████████████ |  25
  5.74 | █████████████                  |  11
  6.10 | ███████████████                |  13
  6.46 | ████████                       |   7
  6.82 | ██                             |   2
  7.18 | █                              |   1
  7.54 | ██                             |   2

Improvement: +18.2%

Feature Distributions (Matching Samples):

sepal_width:
  2.50 | ██████████                     |   4
  2.58 | █████                          |   2
  2.66 | ██████████                     |   4
  2.74 | ████████████████████           |   8
  2.82 |                                |   0
  2.90 | █████                          |   2
  2.98 | ██████████████████████████████ |  12
  3.06 | ██████████                     |   4
  3.14 | ████████████                   |   5
  3.22 | ███████                        |   3
Rule range: [2.25, 3.35]

petal_length:
  4.50 | ██                             |   1
  4.74 | █████████████                  |   5
  4.98 | ██████████████████████████████ |  11
  5.22 | ████████                       |   3
  5.46 | █████████████████████          |   8
  5.70 | █████████████████████          |   8
  5.94 | ██████████                     |   4
  6.18 | ██                             |   1
  6.42 | ██                             |   1
  6.66 | █████                          |   2
Rule range: [2.90, 7.30]

petal_width:
  1.40 | █████                          |   2
  1.51 | ██                             |   1
  1.62 | ██                             |   1
  1.73 | ██████████████████████████████ |  11
  1.84 | █████████████                  |   5
  1.95 | █████████████                  |   5
  2.06 | ████████████████               |   6
  2.17 | █████                          |   2
  2.28 | ███████████████████            |   7
  2.39 | ██████████                     |   4
Rule range: [1.40, 3.40]

Rule 2
==================================================
Rule Conditions:
  petal_length: 1.7 to 5.0

Performance:
  Score: 0.119
  Direction Score: 0.009
  Coverage: 0.427 (64 samples)

Target Variable Statistics:
  Matching Median: 5.800
  Non-matching Median: 5.750

Distribution Analysis:
Rule Impact Analysis
==================================================

Matching Samples: 64 (42.7% of data)

sepal_length Distribution:
Matching samples median: 5.80

Matching samples:
  4.80 | ████████████                   |   5
  5.02 | ██████████                     |   4
  5.24 | ███████                        |   3
  5.46 | ███████████████████████████    |  11
  5.68 | █████████████████████████      |  10
  5.90 | ██████████████████████████████ |  12
  6.12 | ████████████████████           |   8
  6.34 | ███████                        |   3
  6.56 | ████████████                   |   5
  6.78 | ███████                        |   3

Non-matching samples median: 5.75
Non-matching samples:
  4.30 | ███████████████                |   9
  4.66 | ██████████████████████████████ |  18
  5.02 | ████████████████               |  10
  5.38 | ██████████                     |   6
  5.74 | ██████████                     |   6
  6.10 | ██████████████████             |  11
  6.46 | ██████████████████             |  11
  6.82 | ██████                         |   4
  7.18 | ████████                       |   5
  7.54 | ██████████                     |   6

Improvement: +0.9%

Feature Distributions (Matching Samples):

petal_length:
  1.70 | ██████████                     |   6
  2.03 |                                |   0
  2.36 |                                |   0
  2.69 | █                              |   1
  3.02 | ███                            |   2
  3.35 | █████                          |   3
  3.68 | ████████████████               |  10
  4.01 | ███████████████                |   9
  4.34 | █████████████████████████      |  15
  4.67 | ██████████████████████████████ |  18
Rule range: [1.70, 5.00]

Rule 3
==================================================
Rule Conditions:
  petal_length: 1.7 to 5.0

Performance:
  Score: 0.119
  Direction Score: 0.009
  Coverage: 0.427 (64 samples)

Target Variable Statistics:
  Matching Median: 5.800
  Non-matching Median: 5.750

Distribution Analysis:
Rule Impact Analysis
==================================================

Matching Samples: 64 (42.7% of data)

sepal_length Distribution:
Matching samples median: 5.80

Matching samples:
  4.80 | ████████████                   |   5
  5.02 | ██████████                     |   4
  5.24 | ███████                        |   3
  5.46 | ███████████████████████████    |  11
  5.68 | █████████████████████████      |  10
  5.90 | ██████████████████████████████ |  12
  6.12 | ████████████████████           |   8
  6.34 | ███████                        |   3
  6.56 | ████████████                   |   5
  6.78 | ███████                        |   3

Non-matching samples median: 5.75
Non-matching samples:
  4.30 | ███████████████                |   9
  4.66 | ██████████████████████████████ |  18
  5.02 | ████████████████               |  10
  5.38 | ██████████                     |   6
  5.74 | ██████████                     |   6
  6.10 | ██████████████████             |  11
  6.46 | ██████████████████             |  11
  6.82 | ██████                         |   4
  7.18 | ████████                       |   5
  7.54 | ██████████                     |   6

Improvement: +0.9%

Feature Distributions (Matching Samples):

petal_length:
  1.70 | ██████████                     |   6
  2.03 |                                |   0
  2.36 |                                |   0
  2.69 | █                              |   1
  3.02 | ███                            |   2
  3.35 | █████                          |   3
  3.68 | ████████████████               |  10
  4.01 | ███████████████                |   9
  4.34 | █████████████████████████      |  15
  4.67 | ██████████████████████████████ |  18
Rule range: [1.70, 5.00]


### ./rules_sepal_length_max.txt END ###

### ./rules_species_setosa.txt BEGIN ###
Generated Rules Report
Target: species (setosa)
Date: 2024-12-27 12:51:53

Rule 1
==================================================
Rule Conditions:
  sepal_length: 3.9 to 6.1
  sepal_width: 2.9 to 4.1
  petal_length: -0.6 to 3.8
  petal_width: -0.4 to 1.6

Performance:
  Score: 0.532
  Direction Score: 0.952
  Coverage: 0.300 (45 samples)

Target Variable Statistics:
  Matching Rate: 1.000
  Non-matching Rate: 0.048

Distribution Analysis:
Rule Impact Analysis
==================================================

Matching Samples: 45 (30.0% of data)

species Distribution:

Matching samples:
setosa       | ████████████████████ | 100.0%

Non-matching samples:
versicolor   | █████████            | 47.6%
virginica    | █████████            | 47.6%
setosa       |                      | 4.8%

Target class improvement: +95.2%

Feature Distributions (Matching Samples):

sepal_length:
  4.30 | ███████                        |   3
  4.45 |                                |   0
  4.60 | ███████████████                |   6
  4.75 | ████████████                   |   5
  4.90 | ██████████████████████████████ |  12
  5.05 | ████████████████████           |   8
  5.20 | ███████                        |   3
  5.35 | ████████████                   |   5
  5.50 | ██                             |   1
  5.65 | █████                          |   2
Rule range: [3.95, 6.05]

sepal_width:
  3.00 | ████████████████████           |   6
  3.10 | █████████████                  |   4
  3.20 | ████████████████               |   5
  3.30 | ██████                         |   2
  3.40 | ██████████████████████████████ |   9
  3.50 | ████████████████████           |   6
  3.60 | ██████████                     |   3
  3.70 | ██████████                     |   3
  3.80 | █████████████                  |   4
  3.90 | ██████████                     |   3
Rule range: [2.95, 4.05]

petal_length:
  1.00 | ██                             |   1
  1.09 | ██                             |   1
  1.18 | █████                          |   2
  1.27 | ████████████████               |   6
  1.36 | ██████████████████████████████ |  11
  1.45 | ██████████████████████████████ |  11
  1.54 | ███████████████████            |   7
  1.63 | ██████████                     |   4
  1.72 |                                |   0
  1.81 | █████                          |   2
Rule range: [-0.60, 3.80]

petal_width:
  0.10 | ████                           |   4
  0.15 |                                |   0
  0.20 | ██████████████████████████████ |  27
  0.25 | ██████                         |   6
  0.30 |                                |   0
  0.35 |                                |   0
  0.40 | ██████                         |   6
  0.45 |                                |   0
  0.50 | █                              |   1
  0.55 | █                              |   1
Rule range: [-0.40, 1.60]

Rule 2
==================================================
Rule Conditions:
  petal_width: 0.2 to 1.9

Performance:
  Score: 0.264
  Direction Score: 0.241
  Coverage: 0.773 (116 samples)

Target Variable Statistics:
  Matching Rate: 0.388
  Non-matching Rate: 0.147

Distribution Analysis:
Rule Impact Analysis
==================================================

Matching Samples: 116 (77.3% of data)

species Distribution:

Matching samples:
versicolor   | ████████             | 43.1%
setosa       | ███████              | 38.8%
virginica    | ███                  | 18.1%

Non-matching samples:
virginica    | █████████████████    | 85.3%
setosa       | ██                   | 14.7%

Target class improvement: +24.1%

Feature Distributions (Matching Samples):

petal_width:
  0.20 | ██████████████████████████████ |  36
  0.37 | ██████                         |   8
  0.54 |                                |   1
  0.71 |                                |   0
  0.88 | █████                          |   7
  1.05 | ██████                         |   8
  1.22 | ██████████                     |  13
  1.39 | ████████████████               |  20
  1.56 | █████                          |   6
  1.73 | ██████████████                 |  17
Rule range: [0.20, 1.90]

Rule 3
==================================================
Rule Conditions:
  sepal_length: 5.0 to 6.5

Performance:
  Score: 0.061
  Direction Score: -0.078
  Coverage: 0.653 (98 samples)

Target Variable Statistics:
  Matching Rate: 0.306
  Non-matching Rate: 0.385

Distribution Analysis:
Rule Impact Analysis
==================================================

Matching Samples: 98 (65.3% of data)

species Distribution:

Matching samples:
versicolor   | ████████             | 41.8%
setosa       | ██████               | 30.6%
virginica    | █████                | 27.6%

Non-matching samples:
virginica    | ████████             | 44.2%
setosa       | ███████              | 38.5%
versicolor   | ███                  | 17.3%

Target class improvement: -7.8%

Feature Distributions (Matching Samples):

sepal_length:
  5.00 | ██████████████████████████████ |  19
  5.15 | ██████                         |   4
  5.30 | ███████████                    |   7
  5.45 | ███████████                    |   7
  5.60 | ██████████████████████         |  14
  5.75 | ███████████                    |   7
  5.90 | ██████████████                 |   9
  6.05 | █████████                      |   6
  6.20 | ████████████████████           |  13
  6.35 | ██████████████████             |  12
Rule range: [5.00, 6.52]


### ./rules_species_setosa.txt END ###

### ./codebase.md BEGIN ###
### DIRECTORY ./ FOLDER STRUCTURE ###
/
    rules_petal_width_min.txt
    flatten.py
    pyrightconfig.json
    environment.yml
    rules_output.txt
    scratch.py
    README.md
    .gitignore
    rules_sepal_length_max.txt
    rules_species_setosa.txt
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
.git/
    config
    HEAD
    description
    index
    COMMIT_EDITMSG
    objects/
        68/
            f2e0bca5dd97fcdc23d2bc68d6855cc499e3ff
        03/
            baecc77454b2fd911e402afd5d7094a8a22402
        5f/
            aace3f5e990aedd3515f4684baa1b0c42b3eb5
        b5/
            80cc051b971e5f0f72a72b5f77d842fba2df02
        bc/
            4a9b9a5f5ae24b038af4eace5a81a48e61ef06
        ed/
            14e0dbf1a5496cc261dea900c177f56d68b472
        pack/
        11/
            1759cb4456fb8584590f2d213ad7fc91bfcd2d
        info/
        97/
            8a069de0dd419347d51915e064d5990dc822ef
        de/
            d07694bafbb54f6a5cf665fe4c451df7208fba
        e6/
            9de29bb2d1d6434b8b29ae775ad8c2e48c5391
        46/
            f96881377dfb189663a30da2c74f70936be57a
        1b/
            364b85a1ad09662ccd3c84c3b7761fdfad987e
        1e/
            d185a4eb81eb6680331d1ae056b10f6ac362b2
        4a/
            2a7a675d4df24c519ce7f5387b024957209d79
        24/
            eca2093c08afa5ceb327bbd3a482772848c612
        8b/
            016d807b83885ba41eb31604f24d3f36861de2
        13/
            ee03e099613e788af99a6a2241be1a1266ff8e
        7a/
            09c1ac006e17513b735925830315ad73b67391
        22/
            852ecbe03f5f140903efd03bfe1e954bf3b51e
    info/
        exclude
    logs/
        HEAD
        refs/
            heads/
                main
            remotes/
                origin/
                    main
    hooks/
        commit-msg.sample
        pre-rebase.sample
        pre-commit.sample
        applypatch-msg.sample
        fsmonitor-watchman.sample
        pre-receive.sample
        prepare-commit-msg.sample
        post-update.sample
        pre-merge-commit.sample
        pre-applypatch.sample
        pre-push.sample
        update.sample
        push-to-checkout.sample
    refs/
        heads/
            main
        tags/
        remotes/
            origin/
                main
data/
    iris.parquet
### DIRECTORY ./ FOLDER STRUCTURE ###

### DIRECTORY ./ FLATTENED CONTENT ###
### ./rules_petal_width_min.txt BEGIN ###
Generated Rules Report
Target: petal_width (minimize)
Date: 2024-12-27 12:51:53

Rule 1
==================================================
Rule Conditions:
  sepal_length: 3.4 to 5.5
  petal_length: -0.9 to 3.5
  species: setosa

Performance:
  Score: 0.489
  Direction Score: 0.867
  Coverage: 0.300 (45 samples)

Target Variable Statistics:
  Matching Median: 0.200
  Non-matching Median: 1.500

Pruning Steps:
  Removed: sepal_width (improvement: 0.076)

Distribution Analysis:
Rule Impact Analysis
==================================================

Matching Samples: 45 (30.0% of data)

petal_width Distribution:
Matching samples median: 0.20

Matching samples:
  0.10 | █████                          |   5
  0.15 |                                |   0
  0.20 | ██████████████████████████████ |  26
  0.25 | ██████                         |   6
  0.30 |                                |   0
  0.35 |                                |   0
  0.40 | ██████                         |   6
  0.45 |                                |   0
  0.50 | █                              |   1
  0.55 | █                              |   1

Non-matching samples median: 1.50
Non-matching samples:
  0.20 | ███████                        |   5
  0.43 |                                |   0
  0.66 |                                |   0
  0.89 | ███████████████                |  10
  1.12 | ███████████████████████████    |  18
  1.35 | ██████████████████████████████ |  20
  1.58 | ███████████████████████████    |  18
  1.81 | ████████████████               |  11
  2.04 | █████████████                  |   9
  2.27 | █████████████████████          |  14

Improvement: +86.7%

Feature Distributions (Matching Samples):

sepal_length:
  4.30 | ███████████████                |   4
  4.41 | ███                            |   1
  4.52 | ███████████████                |   4
  4.63 | ███████                        |   2
  4.74 | ██████████████████             |   5
  4.85 | ███████████████                |   4
  4.96 | ██████████████████████████████ |   8
  5.07 | ██████████████████████████████ |   8
  5.18 | ███████████                    |   3
  5.29 | ██████████████████████         |   6
Rule range: [3.35, 5.45]

petal_length:
  1.00 | ██                             |   1
  1.09 | ██                             |   1
  1.18 | ██                             |   1
  1.27 | ███████████████                |   6
  1.36 | ██████████████████████████████ |  12
  1.45 | ██████████████████████████████ |  12
  1.54 | █████████████████              |   7
  1.63 | ███████                        |   3
  1.72 |                                |   0
  1.81 | █████                          |   2
Rule range: [-0.90, 3.50]

Rule 2
==================================================
Rule Conditions:
  petal_length: 1.5 to 5.3

Performance:
  Score: 0.235
  Direction Score: 0.278
  Coverage: 0.640 (96 samples)

Target Variable Statistics:
  Matching Median: 1.300
  Non-matching Median: 1.800

Distribution Analysis:
Rule Impact Analysis
==================================================

Matching Samples: 96 (64.0% of data)

petal_width Distribution:
Matching samples median: 1.30

Matching samples:
  0.10 | ███████████████████████████    |  18
  0.33 | ██████████                     |   7
  0.56 | █                              |   1
  0.79 | ██████████                     |   7
  1.02 | ████████████                   |   8
  1.25 | ██████████████████████████████ |  20
  1.48 | █████████████████████████      |  17
  1.71 | ███████████████                |  10
  1.94 | ██████                         |   4
  2.17 | ██████                         |   4

Non-matching samples median: 1.80
Non-matching samples:
  0.10 | ██████████████████████████████ |  23
  0.34 | █                              |   1
  0.58 |                                |   0
  0.82 |                                |   0
  1.06 |                                |   0
  1.30 | █                              |   1
  1.54 | █                              |   1
  1.78 | ███████████                    |   9
  2.02 | ███████████                    |   9
  2.26 | █████████████                  |  10

Improvement: +27.8%

Feature Distributions (Matching Samples):

petal_length:
  1.50 | ██████████████████████████████ |  24
  1.88 | ██                             |   2
  2.26 |                                |   0
  2.64 | █                              |   1
  3.02 | ██                             |   2
  3.40 | █████                          |   4
  3.78 | ███████████████                |  12
  4.16 | ██████████████████████         |  18
  4.54 | █████████████████████          |  17
  4.92 | ████████████████████           |  16
Rule range: [1.50, 5.32]

Rule 3
==================================================
Rule Conditions:
  petal_length: 1.4 to 5.8

Performance:
  Score: 0.177
  Direction Score: 0.278
  Coverage: 0.840 (126 samples)

Target Variable Statistics:
  Matching Median: 1.300
  Non-matching Median: 1.800

Distribution Analysis:
Rule Impact Analysis
==================================================

Matching Samples: 126 (84.0% of data)

petal_width Distribution:
Matching samples median: 1.30

Matching samples:
  0.10 | ████████████████████████████   |  31
  0.34 | ██████                         |   7
  0.58 |                                |   1
  0.82 | ██████                         |   7
  1.06 | ███████                        |   8
  1.30 | ██████████████████████████████ |  33
  1.54 | █████                          |   6
  1.78 | ████████████████               |  18
  2.02 | █████                          |   6
  2.26 | ████████                       |   9

Non-matching samples median: 1.80
Non-matching samples:
  0.10 | ██████████████████████████████ |  10
  0.34 | ███                            |   1
  0.58 |                                |   0
  0.82 |                                |   0
  1.06 |                                |   0
  1.30 |                                |   0
  1.54 |                                |   0
  1.78 | ███████████████                |   5
  2.02 | █████████                      |   3
  2.26 | ███████████████                |   5

Improvement: +27.8%

Feature Distributions (Matching Samples):

petal_length:
  1.40 | ██████████████████████████████ |  37
  1.84 | █                              |   2
  2.28 |                                |   0
  2.72 |                                |   1
  3.16 | ███                            |   4
  3.60 | ████████                       |  11
  4.04 | ██████████                     |  13
  4.48 | ████████████████████           |  25
  4.92 | ████████████                   |  16
  5.36 | █████████████                  |  17
Rule range: [1.40, 5.80]


### ./rules_petal_width_min.txt END ###

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
Date: 2024-12-27 12:33:18

Rule 1
==================================================
Rule Conditions:
  petal_length: 3.4 to 7.8
  petal_width: 0.8 to 2.8
  species: virginica

Performance:
  Score: 0.939
  Coverage: 0.647 (97 samples)
  Dominant Class: virginica
  Separation Score: 0.425
  Recall Score: 1.000
  Purity: 0.515

Pruning Steps:
  Removed: sepal_length (improvement: 0.121)
  Removed: sepal_width (improvement: 0.124)

Distribution Analysis:
Rule Distribution Analysis
==================================================

Matching Samples: 97 (64.7% of data)

Class Distribution:
virginica    | ████████████████████ |  50 (51.5%)
versicolor   | ██████████████████   |  47 (48.5%)

Feature Distributions (Matching Samples):

petal_length:
  3.50 | ████████                       |   5
  3.84 | ██████████████████             |  11
  4.18 | ██████████████████████████████ |  18
  4.52 | ████████████████████           |  12
  4.86 | ████████████████████████████   |  17
  5.20 | ███████████████                |   9
  5.54 | ████████████████████           |  12
  5.88 | ███████████                    |   7
  6.22 | ███                            |   2
  6.56 | ██████                         |   4
Rule range: [3.40, 7.80]

petal_width:
  1.00 | ██████████                     |   7
  1.15 | ███████                        |   5
  1.30 | ██████████████████████████████ |  21
  1.45 | █████████████████              |  12
  1.60 | ████████                       |   6
  1.75 | █████████████████              |  12
  1.90 | ███████████████                |  11
  2.05 | ████████                       |   6
  2.20 | ███████████████                |  11
  2.35 | ████████                       |   6
Rule range: [0.80, 2.80]

Rule 2
==================================================
Rule Conditions:
  petal_length: 1.3 to 1.7

Performance:
  Score: 0.923
  Coverage: 0.293 (44 samples)
  Dominant Class: setosa
  Separation Score: 0.412
  Recall Score: 0.880
  Purity: 1.000

Pruning Steps:
  Removed: petal_width (improvement: 0.067)
  Removed: sepal_length (improvement: 0.057)
  Removed: sepal_width (improvement: 0.092)

Distribution Analysis:
Rule Distribution Analysis
==================================================

Matching Samples: 44 (29.3% of data)

Class Distribution:
setosa       | ████████████████████ |  44 (100.0%)

Feature Distributions (Matching Samples):

petal_length:
  1.30 | ████████████████               |   7
  1.34 |                                |   0
  1.38 | ██████████████████████████████ |  13
  1.42 |                                |   0
  1.46 |                                |   0
  1.50 | ██████████████████████████████ |  13
  1.54 |                                |   0
  1.58 | ████████████████               |   7
  1.62 |                                |   0
  1.66 | █████████                      |   4
Rule range: [1.30, 1.70]

Rule 3
==================================================
Rule Conditions:
  petal_length: 1.3 to 1.6

Performance:
  Score: 0.874
  Coverage: 0.267 (40 samples)
  Dominant Class: setosa
  Separation Score: 0.416
  Recall Score: 0.800
  Purity: 1.000

Pruning Steps:
  Removed: sepal_length (improvement: 0.071)
  Removed: sepal_width (improvement: 0.135)
  Removed: petal_width (improvement: 0.130)

Distribution Analysis:
Rule Distribution Analysis
==================================================

Matching Samples: 40 (26.7% of data)

Class Distribution:
setosa       | ████████████████████ |  40 (100.0%)

Feature Distributions (Matching Samples):

petal_length:
  1.30 | ████████████████               |   7
  1.33 |                                |   0
  1.36 |                                |   0
  1.39 | ██████████████████████████████ |  13
  1.42 |                                |   0
  1.45 |                                |   0
  1.48 | ██████████████████████████████ |  13
  1.51 |                                |   0
  1.54 |                                |   0
  1.57 | ████████████████               |   7
Rule range: [1.30, 1.60]

Rule 4
==================================================
Rule Conditions:
  petal_length: 4.9 to 6.3

Performance:
  Score: 0.871
  Coverage: 0.307 (46 samples)
  Dominant Class: virginica
  Separation Score: 0.406
  Recall Score: 0.840
  Purity: 0.913

Pruning Steps:
  Removed: sepal_width (improvement: 0.095)
  Removed: petal_width (improvement: 0.072)
  Removed: sepal_length (improvement: 0.062)

Distribution Analysis:
Rule Distribution Analysis
==================================================

Matching Samples: 46 (30.7% of data)

Class Distribution:
virginica    | ████████████████████ |  42 (91.3%)
versicolor   | █                    |   4 (8.7%)

Feature Distributions (Matching Samples):

petal_length:
  4.90 | ██████████████████████████████ |   9
  5.04 | ██████████████████████████     |   8
  5.18 | █████████████                  |   4
  5.32 | ██████                         |   2
  5.46 | ██████████                     |   3
  5.60 | ██████████████████████████████ |   9
  5.74 | ██████████                     |   3
  5.88 | █████████████                  |   4
  6.02 | ██████████                     |   3
  6.16 | ███                            |   1
Rule range: [4.90, 6.31]

Rule 5
==================================================
Rule Conditions:
  petal_length: 5.1 to 6.0

Performance:
  Score: 0.755
  Coverage: 0.220 (33 samples)
  Dominant Class: virginica
  Separation Score: 0.396
  Recall Score: 0.640
  Purity: 0.970

Pruning Steps:
  Removed: sepal_width (improvement: 0.077)
  Removed: petal_width (improvement: 0.084)
  Removed: sepal_length (improvement: 0.056)

Distribution Analysis:
Rule Distribution Analysis
==================================================

Matching Samples: 33 (22.0% of data)

Class Distribution:
virginica    | ████████████████████ |  32 (97.0%)
versicolor   |                      |   1 (3.0%)

Feature Distributions (Matching Samples):

petal_length:
  5.10 | ██████████████████████████████ |   8
  5.19 | ███████                        |   2
  5.28 | ███████                        |   2
  5.37 | ███████                        |   2
  5.46 | ███████████                    |   3
  5.55 | ██████████████████████         |   6
  5.64 | ███████████                    |   3
  5.73 | ███████████                    |   3
  5.82 | ███████                        |   2
  5.91 | ███████                        |   2
Rule range: [5.10, 6.00]


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

### ./.gitignore BEGIN ###
__pycache__/
*.pyc
.ropeproject/

### ./.gitignore END ###

### ./rules_sepal_length_max.txt BEGIN ###
Generated Rules Report
Target: sepal_length (maximize)
Date: 2024-12-27 12:51:53

Rule 1
==================================================
Rule Conditions:
  sepal_width: 2.2 to 3.4
  petal_length: 2.9 to 7.3
  petal_width: 1.4 to 3.4
  species: virginica

Performance:
  Score: 0.172
  Direction Score: 0.182
  Coverage: 0.293 (44 samples)

Target Variable Statistics:
  Matching Median: 6.500
  Non-matching Median: 5.500

Distribution Analysis:
Rule Impact Analysis
==================================================

Matching Samples: 44 (29.3% of data)

sepal_length Distribution:
Matching samples median: 6.50

Matching samples:
  4.90 | ███                            |   1
  5.18 |                                |   0
  5.46 | ██████                         |   2
  5.74 | ████████████████               |   5
  6.02 | ██████████████████████████     |   8
  6.30 | ██████████████████████████████ |   9
  6.58 | ███████████████████████        |   7
  6.86 | █████████████                  |   4
  7.14 | █████████████                  |   4
  7.42 | █████████████                  |   4

Non-matching samples median: 5.50
Non-matching samples:
  4.30 | ██████████                     |   9
  4.66 | ██████████████████████████     |  22
  5.02 | ████████████████               |  14
  5.38 | ██████████████████████████████ |  25
  5.74 | █████████████                  |  11
  6.10 | ███████████████                |  13
  6.46 | ████████                       |   7
  6.82 | ██                             |   2
  7.18 | █                              |   1
  7.54 | ██                             |   2

Improvement: +18.2%

Feature Distributions (Matching Samples):

sepal_width:
  2.50 | ██████████                     |   4
  2.58 | █████                          |   2
  2.66 | ██████████                     |   4
  2.74 | ████████████████████           |   8
  2.82 |                                |   0
  2.90 | █████                          |   2
  2.98 | ██████████████████████████████ |  12
  3.06 | ██████████                     |   4
  3.14 | ████████████                   |   5
  3.22 | ███████                        |   3
Rule range: [2.25, 3.35]

petal_length:
  4.50 | ██                             |   1
  4.74 | █████████████                  |   5
  4.98 | ██████████████████████████████ |  11
  5.22 | ████████                       |   3
  5.46 | █████████████████████          |   8
  5.70 | █████████████████████          |   8
  5.94 | ██████████                     |   4
  6.18 | ██                             |   1
  6.42 | ██                             |   1
  6.66 | █████                          |   2
Rule range: [2.90, 7.30]

petal_width:
  1.40 | █████                          |   2
  1.51 | ██                             |   1
  1.62 | ██                             |   1
  1.73 | ██████████████████████████████ |  11
  1.84 | █████████████                  |   5
  1.95 | █████████████                  |   5
  2.06 | ████████████████               |   6
  2.17 | █████                          |   2
  2.28 | ███████████████████            |   7
  2.39 | ██████████                     |   4
Rule range: [1.40, 3.40]

Rule 2
==================================================
Rule Conditions:
  petal_length: 1.7 to 5.0

Performance:
  Score: 0.119
  Direction Score: 0.009
  Coverage: 0.427 (64 samples)

Target Variable Statistics:
  Matching Median: 5.800
  Non-matching Median: 5.750

Distribution Analysis:
Rule Impact Analysis
==================================================

Matching Samples: 64 (42.7% of data)

sepal_length Distribution:
Matching samples median: 5.80

Matching samples:
  4.80 | ████████████                   |   5
  5.02 | ██████████                     |   4
  5.24 | ███████                        |   3
  5.46 | ███████████████████████████    |  11
  5.68 | █████████████████████████      |  10
  5.90 | ██████████████████████████████ |  12
  6.12 | ████████████████████           |   8
  6.34 | ███████                        |   3
  6.56 | ████████████                   |   5
  6.78 | ███████                        |   3

Non-matching samples median: 5.75
Non-matching samples:
  4.30 | ███████████████                |   9
  4.66 | ██████████████████████████████ |  18
  5.02 | ████████████████               |  10
  5.38 | ██████████                     |   6
  5.74 | ██████████                     |   6
  6.10 | ██████████████████             |  11
  6.46 | ██████████████████             |  11
  6.82 | ██████                         |   4
  7.18 | ████████                       |   5
  7.54 | ██████████                     |   6

Improvement: +0.9%

Feature Distributions (Matching Samples):

petal_length:
  1.70 | ██████████                     |   6
  2.03 |                                |   0
  2.36 |                                |   0
  2.69 | █                              |   1
  3.02 | ███                            |   2
  3.35 | █████                          |   3
  3.68 | ████████████████               |  10
  4.01 | ███████████████                |   9
  4.34 | █████████████████████████      |  15
  4.67 | ██████████████████████████████ |  18
Rule range: [1.70, 5.00]

Rule 3
==================================================
Rule Conditions:
  petal_length: 1.7 to 5.0

Performance:
  Score: 0.119
  Direction Score: 0.009
  Coverage: 0.427 (64 samples)

Target Variable Statistics:
  Matching Median: 5.800
  Non-matching Median: 5.750

Distribution Analysis:
Rule Impact Analysis
==================================================

Matching Samples: 64 (42.7% of data)

sepal_length Distribution:
Matching samples median: 5.80

Matching samples:
  4.80 | ████████████                   |   5
  5.02 | ██████████                     |   4
  5.24 | ███████                        |   3
  5.46 | ███████████████████████████    |  11
  5.68 | █████████████████████████      |  10
  5.90 | ██████████████████████████████ |  12
  6.12 | ████████████████████           |   8
  6.34 | ███████                        |   3
  6.56 | ████████████                   |   5
  6.78 | ███████                        |   3

Non-matching samples median: 5.75
Non-matching samples:
  4.30 | ███████████████                |   9
  4.66 | ██████████████████████████████ |  18
  5.02 | ████████████████               |  10
  5.38 | ██████████                     |   6
  5.74 | ██████████                     |   6
  6.10 | ██████████████████             |  11
  6.46 | ██████████████████             |  11
  6.82 | ██████                         |   4
  7.18 | ████████                       |   5
  7.54 | ██████████                     |   6

Improvement: +0.9%

Feature Distributions (Matching Samples):

petal_length:
  1.70 | ██████████                     |   6
  2.03 |                                |   0
  2.36 |                                |   0
  2.69 | █                              |   1
  3.02 | ███                            |   2
  3.35 | █████                          |   3
  3.68 | ████████████████               |  10
  4.01 | ███████████████                |   9
  4.34 | █████████████████████████      |  15
  4.67 | ██████████████████████████████ |  18
Rule range: [1.70, 5.00]


### ./rules_sepal_length_max.txt END ###


### ./codebase.md END ###

### ./main.py BEGIN ###
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

### ./main.py END ###

### ./rule_solver/scoring.py BEGIN ###
import numpy as np
from typing import Dict, Union, Tuple, Literal

def fast_ranks(x):
    """Simple ranking function using numpy only"""
    temp = x.argsort()
    ranks = np.empty_like(temp)
    ranks[temp] = np.arange(len(x))
    return (ranks + 1) / (len(x) + 1)  # Add 1 to avoid 0s

def calculate_rank_score(df, rule, target_column='species'):
    """
    Enhanced scoring function that balances separation quality with class recall
    while considering within-class spread.
    """
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

    # Get matching samples
    matching_mask = df.apply(lambda row: matches_rule(row, rule), axis=1)

    if matching_mask.sum() == 0:
        return {
            'score': 0.0,
            'separation_score': 0.0,
            'recall_score': 0.0,
            'coverage': 0.0,
            'matching_samples': 0,
            'dominant_class': None
        }

    matching_df = df[matching_mask]
    non_matching_df = df[~matching_mask]

    # Get class distribution and dominant class
    class_counts = matching_df[target_column].value_counts()
    dominant_class = class_counts.index[0]

    # Calculate class recall for dominant class
    total_in_class = len(df[df[target_column] == dominant_class])
    matching_in_class = len(matching_df[matching_df[target_column] == dominant_class])
    class_recall = matching_in_class / total_in_class if total_in_class > 0 else 0

    # Calculate feature scores for continuous features
    continuous_features = [f for f, v in rule.items()
                         if isinstance(v, tuple) and f != target_column]
    feature_scores = {}

    for feature in continuous_features:
        values = df[feature].values
        normalized_ranks = fast_ranks(values)

        matching_ranks = normalized_ranks[matching_mask]
        nonmatching_ranks = normalized_ranks[~matching_mask]

        # Median separation between classes
        rank_separation = abs(np.percentile(matching_ranks, 50) -
                            np.percentile(nonmatching_ranks, 50))

        # Within-class spread for target class
        target_mask = matching_df[target_column] == dominant_class
        if target_mask.any():
            target_ranks = matching_ranks[target_mask]
            rank_spread = np.percentile(target_ranks, 75) - np.percentile(target_ranks, 25)
            # Penalize high spread within target class
            spread_penalty = 1 / (1 + rank_spread)
        else:
            spread_penalty = 0

        feature_scores[feature] = rank_separation * spread_penalty

    # Calculate separation score
    separation_score = np.mean(list(feature_scores.values())) if feature_scores else 0

    # Calculate purity (proportion of dominant class in matches)
    purity = class_counts.iloc[0] / len(matching_df)

    # Calculate coverage (relative to total dataset)
    coverage = len(matching_df) / len(df)

    # For categorical features, boost score if they help with classification
    categorical_features = [f for f, v in rule.items()
                          if not isinstance(v, tuple) and f != target_column]
    if categorical_features:
        categorical_boost = sum(1 for f in categorical_features
                              if rule[f] == dominant_class) / len(categorical_features)
    else:
        categorical_boost = 0

    # Combine scores with emphasis on meaningful coverage
    # Calculate minimum required coverage based on dataset size
    min_coverage = max(0.1, 10 / len(df))  # At least 10 samples or 10% of data

    # Apply coverage penalty if below minimum
    coverage_score = coverage if coverage >= min_coverage else coverage * (coverage / min_coverage)

    # Combine scores favoring rules with good separation AND good coverage
    base_score = (
        separation_score * 0.4 +  # Continuous feature separation
        class_recall * 0.3 +      # Recall of dominant class
        purity * 0.3             # Class purity in matches
    )

    # Use sigmoid-like function to favor higher coverage when base_score is good
    coverage_weight = 1 / (1 + np.exp(-10 * (base_score - 0.5)))  # Sigmoid centered at 0.5
    final_score = base_score * (1 + coverage_weight * coverage)

    return {
        'score': final_score,
        'separation_score': separation_score,
        'recall_score': class_recall,
        'purity': purity,
        'coverage': coverage,
        'matching_samples': len(matching_df),
        'dominant_class': dominant_class,
        'feature_scores': feature_scores
    }

def calculate_directional_score(df, rule, target_var, direction: Union[Literal['maximize'],
                                                                     Literal['minimize'], str]) \
                                                                     -> Dict[str, Union[float, int, str, None]]:
    """
    Calculate score based on how well the rule drives a target variable in desired direction.

    Args:
        df: DataFrame with all data
        rule: Dictionary of feature conditions
        target_var: Variable to optimize
        direction: Either 'maximize'/'minimize' for continuous variables,
                  or specific category for categorical variables
    """
    def matches_rule(row, rule):
        if target_var in rule:  # Remove target from rule conditions
            return False
        for feature, value in rule.items():
            if isinstance(value, tuple):
                min_val, max_val = value
                if not (min_val <= row[feature] <= max_val):
                    return False
            else:
                if row[feature] != value:
                    return False
        return True

    # Get matching samples
    matching_mask = df.apply(lambda row: matches_rule(row, rule), axis=1)

    if matching_mask.sum() == 0:
        return {
            'score': 0.0,
            'direction_score': 0.0,
            'coverage': 0.0,
            'matching_samples': 0,
        }

    matching_df = df[matching_mask]
    non_matching_df = df[~matching_mask]

    # Calculate directional score based on variable type
    if direction in ['maximize', 'minimize']:
        # For continuous variables
        matching_vals = matching_df[target_var].values
        non_matching_vals = non_matching_df[target_var].values

        # Get medians for comparison
        matching_median = np.median(matching_vals)
        non_matching_median = np.median(non_matching_vals)

        # Calculate how well the rule separates values in desired direction
        if direction == 'maximize':
            direction_score = (matching_median - non_matching_median) / non_matching_median
        else:  # minimize
            direction_score = (non_matching_median - matching_median) / non_matching_median

        # Calculate spread within matching samples
        matching_iqr = np.percentile(matching_vals, 75) - np.percentile(matching_vals, 25)
        total_iqr = np.percentile(df[target_var], 75) - np.percentile(df[target_var], 25)
        spread_score = 1 - (matching_iqr / total_iqr if total_iqr > 0 else 1)

    else:
        # For categorical variables (direction is desired category)
        matching_counts = matching_df[target_var].value_counts(normalize=True)
        non_matching_counts = non_matching_df[target_var].value_counts(normalize=True)

        # Calculate how much more prevalent the desired category is in matching samples
        matching_rate = matching_counts.get(direction, 0)
        non_matching_rate = non_matching_counts.get(direction, 0)

        direction_score = matching_rate - non_matching_rate
        spread_score = matching_rate  # For categorical, spread is just purity

    # Calculate coverage with penalty for very small rules
    min_samples = max(10, len(df) * 0.05)  # At least 10 samples or 5% of data
    coverage = matching_mask.sum() / len(df)
    coverage_score = coverage if matching_mask.sum() >= min_samples else coverage * 0.5

    # Combine scores
    final_score = (direction_score * 0.6 + spread_score * 0.4) * np.sqrt(coverage_score)

    return {
        'score': final_score,
        'direction_score': direction_score,
        'spread_score': spread_score,
        'coverage': coverage,
        'matching_samples': matching_mask.sum(),
        'target_stats': {
            'matching_median': np.median(matching_df[target_var]) if direction in ['maximize', 'minimize'] else None,
            'non_matching_median': np.median(non_matching_df[target_var]) if direction in ['maximize', 'minimize'] else None,
            'matching_rate': matching_rate if direction not in ['maximize', 'minimize'] else None,
            'non_matching_rate': non_matching_rate if direction not in ['maximize', 'minimize'] else None
        }
    }

def score_improvement(new_score, base_score, new_coverage, base_coverage,
                     coverage_weight=0.1):
    """Calculate improvement in score with coverage penalty/bonus"""
    return (new_score - base_score) + coverage_weight * (new_coverage - base_coverage)

### ./rule_solver/scoring.py END ###

### ./rule_solver/rules.py BEGIN ###
# rules.py
import numpy as np
from typing import Dict, Union, List, Tuple
from .utils import infer_feature_types

def fast_ranks(x):
    """Simple ranking function using numpy only"""
    temp = x.argsort()
    ranks = np.empty_like(temp)
    ranks[temp] = np.arange(len(x))
    return (ranks + 1) / (len(x) + 1)  # Add 1 to avoid 0s

def calculate_directional_score(df, rule, target_var, direction) -> Dict[str, Union[float, int, str, None]]:
    """
    Calculate score based on how well the rule drives a target variable in desired direction.
    """
    def matches_rule(row, rule):
        if target_var in rule:  # Remove target from rule conditions
            return False
        for feature, value in rule.items():
            if isinstance(value, tuple):
                min_val, max_val = value
                if not (min_val <= row[feature] <= max_val):
                    return False
            else:
                if row[feature] != value:
                    return False
        return True

    # Get matching samples
    matching_mask = df.apply(lambda row: matches_rule(row, rule), axis=1)

    if matching_mask.sum() == 0:
        return {
            'score': 0.0,
            'direction_score': 0.0,
            'coverage': 0.0,
            'matching_samples': 0,
        }

    matching_df = df[matching_mask]
    non_matching_df = df[~matching_mask]

    # Calculate directional score based on variable type
    if direction in ['maximize', 'minimize']:
        # For continuous variables
        matching_vals = matching_df[target_var].values
        non_matching_vals = non_matching_df[target_var].values

        # Get medians for comparison
        matching_median = np.median(matching_vals)
        non_matching_median = np.median(non_matching_vals)

        # Calculate how well the rule separates values in desired direction
        if direction == 'maximize':
            direction_score = (matching_median - non_matching_median) / non_matching_median
        else:  # minimize
            direction_score = (non_matching_median - matching_median) / non_matching_median

        # Calculate spread within matching samples
        matching_iqr = np.percentile(matching_vals, 75) - np.percentile(matching_vals, 25)
        total_iqr = np.percentile(df[target_var], 75) - np.percentile(df[target_var], 25)
        spread_score = 1 - (matching_iqr / total_iqr if total_iqr > 0 else 1)

    else:
        # For categorical variables (direction is desired category)
        matching_counts = matching_df[target_var].value_counts(normalize=True)
        non_matching_counts = non_matching_df[target_var].value_counts(normalize=True)

        # Calculate how much more prevalent the desired category is in matching samples
        matching_rate = matching_counts.get(direction, 0)
        non_matching_rate = non_matching_counts.get(direction, 0)

        direction_score = matching_rate - non_matching_rate
        spread_score = matching_rate  # For categorical, spread is just purity

    # Calculate coverage with penalty for very small rules
    min_samples = max(10, len(df) * 0.05)  # At least 10 samples or 5% of data
    coverage = matching_mask.sum() / len(df)
    coverage_score = coverage if matching_mask.sum() >= min_samples else coverage * 0.5

    # Combine scores
    final_score = (direction_score * 0.6 + spread_score * 0.4) * np.sqrt(coverage_score)

    return {
        'score': final_score,
        'direction_score': direction_score,
        'spread_score': spread_score,
        'coverage': coverage,
        'matching_samples': matching_mask.sum(),
        'target_stats': {
            'matching_median': np.median(matching_df[target_var]) if direction in ['maximize', 'minimize'] else None,
            'non_matching_median': np.median(non_matching_df[target_var]) if direction in ['maximize', 'minimize'] else None,
            'matching_rate': matching_rate if direction not in ['maximize', 'minimize'] else None,
            'non_matching_rate': non_matching_rate if direction not in ['maximize', 'minimize'] else None
        }
    }

def score_improvement(new_score, base_score, new_coverage, base_coverage,
                     coverage_weight=0.1):
    """Calculate improvement in score with coverage penalty/bonus"""
    return (new_score - base_score) + coverage_weight * (new_coverage - base_coverage)

def create_rule(point1, point2, continuous_features, categorical_features, df):
    """Create rule with adaptive boundary expansion"""
    rule = {}

    # Handle continuous features with margin
    for feature in continuous_features:
        min_val = min(point1[feature], point2[feature])
        max_val = max(point1[feature], point2[feature])

        # Add substantial margin to create meaningful ranges
        feature_range = max_val - min_val
        if feature_range == 0:  # If points are identical, use dataset range
            all_vals = df[feature].values
            feature_range = np.percentile(all_vals, 90) - np.percentile(all_vals, 10)
        margin = feature_range * 0.5  # 50% margin

        rule[feature] = (min_val - margin, max_val + margin)

    # Handle categorical features
    for feature in categorical_features:
        if point1[feature] == point2[feature]:
            rule[feature] = point1[feature]

    return rule

def generate_rules(df, num_rules=100, target_var=None):
    """Generate initial rules using percentile ranges and density-based sampling"""
    continuous_features, categorical_features = infer_feature_types(df)
    if target_var in continuous_features:
        continuous_features.remove(target_var)
    if target_var in categorical_features:
        categorical_features.remove(target_var)

    rules = []

    # Strategy 1: Generate rules using percentile ranges for features
    percentile_pairs = [(20, 80), (10, 90), (30, 70)]

    for lower_pct, upper_pct in percentile_pairs:
        # Create multiple rules with different feature combinations
        feature_combinations = [(1,), (2,)]  # Try rules with 1 or 2 features

        for n_features in feature_combinations:
            # Randomly select n features
            selected_features = np.random.choice(
                continuous_features,
                size=min(len(n_features), len(continuous_features)),
                replace=False
            )

            rule = {}
            for feature in selected_features:
                values = df[feature].values
                lower = np.percentile(values, lower_pct)
                upper = np.percentile(values, upper_pct)
                if lower != upper:
                    rule[feature] = (lower, upper)

            if rule:  # Only add if we found some defining features
                rules.append(rule)

    # Strategy 2: Density-based point selection
    for _ in range(num_rules // 3):  # Reduced number to make room for percentile rules
        # Sample initial point
        seed_point = df.sample(1).iloc[0]

        # Find nearby points using rank-based distance
        distances = []
        for _, candidate in df.iterrows():
            dist = 0
            for feature in continuous_features:
                # Use rank difference as distance metric
                ranks = fast_ranks(df[feature].values)
                seed_idx = (df[feature] == seed_point[feature]).idxmax()
                candidate_idx = df.index.get_loc(_)
                p1_rank = ranks[seed_idx]
                p2_rank = ranks[candidate_idx]
                dist += (p1_rank - p2_rank) ** 2
            distances.append(np.sqrt(dist))

        # Select point from dense region
        nearest_idx = np.argmin(distances)
        dense_point = df.iloc[nearest_idx]

        rule = create_rule(seed_point, dense_point,
                         continuous_features, categorical_features, df)
        rules.append(rule)

    return rules

def prune_rule(df, rule, target_var, direction, min_improvement=0.05, min_features=2):
    """Prune conditions using directional scoring"""
    base_metrics = calculate_directional_score(df, rule, target_var, direction)

    if base_metrics is None:
        raise ValueError("Base metrics cannot be None. Ensure scoring always returns a valid dictionary.")

    current_rule = rule.copy()
    pruning_history = []

    while True:
        best_improvement = -float('inf')
        best_feature_to_remove = None
        best_new_metrics = None

        for feature in list(current_rule.keys()):
            if feature == target_var:
                continue

            # Ensure we keep minimum number of features
            remaining_features = len([f for f in current_rule if f != target_var])
            if remaining_features < min_features:
                continue

            test_rule = {k: v for k, v in current_rule.items() if k != feature}
            test_metrics = calculate_directional_score(df, test_rule, target_var, direction)

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

def find_best_rules(df, num_rules=5, target_var=None, direction=None):
    """
    Generate, prune and rank rules optimized for driving target_var in specified direction.

    Args:
        df: DataFrame with data
        num_rules: Number of rules to return
        target_var: Variable to optimize
        direction: 'maximize'/'minimize' for continuous, or category name for categorical
    """
    if target_var is None:
        raise ValueError("Must specify target_var")
    if direction is None:
        raise ValueError("Must specify direction (maximize/minimize or category)")

    # Remove target variable from rule generation
    features_to_use = [col for col in df.columns if col != target_var]
    rules = generate_rules(df[features_to_use], num_rules, target_var)

    pruned_rules = []
    for rule in rules:
        pruned_rule, metrics, history = prune_rule(df, rule, target_var, direction)
        pruned_rules.append((pruned_rule, metrics, history))

    # Sort by score
    pruned_rules.sort(key=lambda x: x[1]['score'], reverse=True)
    return pruned_rules[:num_rules]  # Return only requested number of rules

### ./rule_solver/rules.py END ###

### ./rule_solver/utils.py BEGIN ###
# utils.py
import numpy as np
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

def matches_rule(row, rule, target_var):
    """Check if a row matches rule conditions"""
    for feature, value in rule.items():
        if feature == target_var:
            continue
        if isinstance(value, tuple):
            min_val, max_val = value
            if not (min_val <= row[feature] <= max_val):
                return False
        else:
            if row[feature] != value:
                return False
    return True

def create_unicode_histogram(values, bins=10, width=30):
    """Create a simple unicode histogram."""
    hist, bin_edges = np.histogram(values, bins=bins)
    max_count = max(hist)

    # Unicode block characters from least to most filled
    blocks = ' ▁▂▃▄▅▆▇█'

    lines = []
    for count, edge in zip(hist, bin_edges[:-1]):
        bar_len = int((count / max_count) * width)
        bar = blocks[-1] * bar_len
        lines.append(f"{edge:6.2f} | {bar:<{width}} | {count:3d}")

    return '\n'.join(lines)

def visualize_rule_impact(df, rule, target_var, direction):
    """Create text visualization of rule's impact on target variable distribution."""
    matching_mask = df.apply(lambda row: matches_rule(row, rule, target_var), axis=1)
    matching_df = df[matching_mask]
    non_matching_df = df[~matching_mask]
    total_matching = len(matching_df)

    lines = [
        "Rule Impact Analysis",
        "=" * 50,
        f"\nMatching Samples: {total_matching} ({total_matching/len(df):.1%} of data)"
    ]

    # Show target variable distribution
    if direction in ['maximize', 'minimize']:
        matching_median = np.median(matching_df[target_var])
        non_matching_median = np.median(non_matching_df[target_var])

        lines.append(f"\n{target_var} Distribution:")
        lines.append(f"Matching samples median: {matching_median:.2f}")
        lines.append("\nMatching samples:")
        hist = create_unicode_histogram(matching_df[target_var].values)
        lines.append(hist)

        lines.append(f"\nNon-matching samples median: {non_matching_median:.2f}")
        lines.append("Non-matching samples:")
        hist = create_unicode_histogram(non_matching_df[target_var].values)
        lines.append(hist)

        improvement = ((matching_median - non_matching_median) / non_matching_median * 100
                      if direction == 'maximize' else
                      (non_matching_median - matching_median) / non_matching_median * 100)
        lines.append(f"\nImprovement: {improvement:+.1f}%")

    else:
        # For categorical target
        matching_counts = matching_df[target_var].value_counts(normalize=True)
        non_matching_counts = non_matching_df[target_var].value_counts(normalize=True)

        lines.append(f"\n{target_var} Distribution:")
        lines.append("\nMatching samples:")
        for cat, pct in matching_counts.items():
            lines.append(f"{cat:12} | {'█' * int(pct * 20):<20} | {pct:.1%}")

        lines.append("\nNon-matching samples:")
        for cat, pct in non_matching_counts.items():
            lines.append(f"{cat:12} | {'█' * int(pct * 20):<20} | {pct:.1%}")

        target_improvement = (matching_counts.get(direction, 0) -
                            non_matching_counts.get(direction, 0)) * 100
        lines.append(f"\nTarget class improvement: {target_improvement:+.1f}%")

    # Show distribution for all continuous features
    continuous_features = [f for f, v in rule.items() if isinstance(v, tuple)]
    if continuous_features:
        lines.append("\nFeature Distributions (Matching Samples):")
        for feature in continuous_features:
            lines.append(f"\n{feature}:")
            hist = create_unicode_histogram(matching_df[feature].values)
            lines.append(hist)
            if feature in rule:
                min_val, max_val = rule[feature]
                lines.append(f"Rule range: [{min_val:.2f}, {max_val:.2f}]")

    return '\n'.join(lines)

def format_rule_for_human(rule, metrics, history):
    """Format a rule and its metrics into a readable string."""
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
    lines.append(f"  Direction Score: {metrics['direction_score']:.3f}")
    lines.append(f"  Coverage: {metrics['coverage']:.3f} ({metrics['matching_samples']} samples)")

    # Add target variable statistics if available
    if 'target_stats' in metrics:
        lines.append("\nTarget Variable Statistics:")
        stats = metrics['target_stats']
        if stats['matching_median'] is not None:
            lines.append(f"  Matching Median: {stats['matching_median']:.3f}")
            lines.append(f"  Non-matching Median: {stats['non_matching_median']:.3f}")
        if stats['matching_rate'] is not None:
            lines.append(f"  Matching Rate: {stats['matching_rate']:.3f}")
            lines.append(f"  Non-matching Rate: {stats['non_matching_rate']:.3f}")

    # Format pruning history
    if history:
        lines.append("\nPruning Steps:")
        for step in history:
            lines.append(f"  Removed: {step['removed_feature']} "
                        f"(improvement: {step['improvement']:.3f})")

    return '\n'.join(lines) + '\n'

def save_rules_to_file(rules, df, filename='rules_output.txt', target_var=None, direction=None):
    """Save rules to a text file with visualizations."""
    with open(filename, 'w') as f:
        f.write(f"Generated Rules Report\n")
        f.write(f"Target: {target_var} ({direction})\n")
        f.write(f"Date: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

        for i, (rule, metrics, history) in enumerate(rules, 1):
            f.write(f"Rule {i}\n")
            f.write(format_rule_for_human(rule, metrics, history))
            f.write("\nDistribution Analysis:\n")
            f.write(visualize_rule_impact(df, rule, target_var, direction))
            f.write("\n\n")

### ./rule_solver/utils.py END ###

### ./tests/test_scoring.py BEGIN ###

### ./tests/test_scoring.py END ###

### ./.git/config BEGIN ###
[core]
	repositoryformatversion = 0
	filemode = true
	bare = false
	logallrefupdates = true
	ignorecase = true
	precomposeunicode = true
[remote "origin"]
	url = grej/rule_solver_experiment
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "main"]
	remote = origin
	merge = refs/heads/main

### ./.git/config END ###

### ./.git/HEAD BEGIN ###
ref: refs/heads/main

### ./.git/HEAD END ###

### ./.git/description BEGIN ###
Unnamed repository; edit this file 'description' to name the repository.

### ./.git/description END ###

### ./.git/COMMIT_EDITMSG BEGIN ###
Initial commit: Rule discovery system implementation

### ./.git/COMMIT_EDITMSG END ###

### ./.git/info/exclude BEGIN ###
# git ls-files --others --exclude-from=.git/info/exclude
# Lines that start with '#' are comments.
# For a project mostly in C, the following would be a good set of
# exclude patterns (uncomment them if you want to use them):
# *.[oa]
# *~

### ./.git/info/exclude END ###

### ./.git/logs/HEAD BEGIN ###
0000000000000000000000000000000000000000 22852ecbe03f5f140903efd03bfe1e954bf3b51e Greg Jennings <greg@Gregorys-MacBook-Air.local> 1735280353 -0600	commit (initial): Initial commit: Rule discovery system implementation
22852ecbe03f5f140903efd03bfe1e954bf3b51e 0000000000000000000000000000000000000000 Greg Jennings <greg@Gregorys-MacBook-Air.local> 1735280400 -0600	Branch: renamed refs/heads/main to refs/heads/main
22852ecbe03f5f140903efd03bfe1e954bf3b51e 22852ecbe03f5f140903efd03bfe1e954bf3b51e Greg Jennings <greg@Gregorys-MacBook-Air.local> 1735280400 -0600	Branch: renamed refs/heads/main to refs/heads/main
22852ecbe03f5f140903efd03bfe1e954bf3b51e 0000000000000000000000000000000000000000 Greg Jennings <greg@Gregorys-MacBook-Air.local> 1735280466 -0600	Branch: renamed refs/heads/main to refs/heads/main
22852ecbe03f5f140903efd03bfe1e954bf3b51e 22852ecbe03f5f140903efd03bfe1e954bf3b51e Greg Jennings <greg@Gregorys-MacBook-Air.local> 1735280466 -0600	Branch: renamed refs/heads/main to refs/heads/main

### ./.git/logs/HEAD END ###

### ./.git/logs/refs/heads/main BEGIN ###
0000000000000000000000000000000000000000 22852ecbe03f5f140903efd03bfe1e954bf3b51e Greg Jennings <greg@Gregorys-MacBook-Air.local> 1735280353 -0600	commit (initial): Initial commit: Rule discovery system implementation
22852ecbe03f5f140903efd03bfe1e954bf3b51e 22852ecbe03f5f140903efd03bfe1e954bf3b51e Greg Jennings <greg@Gregorys-MacBook-Air.local> 1735280400 -0600	Branch: renamed refs/heads/main to refs/heads/main
22852ecbe03f5f140903efd03bfe1e954bf3b51e 22852ecbe03f5f140903efd03bfe1e954bf3b51e Greg Jennings <greg@Gregorys-MacBook-Air.local> 1735280466 -0600	Branch: renamed refs/heads/main to refs/heads/main

### ./.git/logs/refs/heads/main END ###

### ./.git/logs/refs/remotes/origin/main BEGIN ###
0000000000000000000000000000000000000000 22852ecbe03f5f140903efd03bfe1e954bf3b51e Greg Jennings <greg@Gregorys-MacBook-Air.local> 1735280469 -0600	update by push

### ./.git/logs/refs/remotes/origin/main END ###

### ./.git/hooks/commit-msg.sample BEGIN ###
#!/bin/sh
#
# An example hook script to check the commit log message.
# Called by "git commit" with one argument, the name of the file
# that has the commit message.  The hook should exit with non-zero
# status after issuing an appropriate message if it wants to stop the
# commit.  The hook is allowed to edit the commit message file.
#
# To enable this hook, rename this file to "commit-msg".

# Uncomment the below to add a Signed-off-by line to the message.
# Doing this in a hook is a bad idea in general, but the prepare-commit-msg
# hook is more suited to it.
#
# SOB=$(git var GIT_AUTHOR_IDENT | sed -n 's/^\(.*>\).*$/Signed-off-by: \1/p')
# grep -qs "^$SOB" "$1" || echo "$SOB" >> "$1"

# This example catches duplicate Signed-off-by lines.

test "" = "$(grep '^Signed-off-by: ' "$1" |
	 sort | uniq -c | sed -e '/^[ 	]*1[ 	]/d')" || {
	echo >&2 Duplicate Signed-off-by lines.
	exit 1
}

### ./.git/hooks/commit-msg.sample END ###

### ./.git/hooks/pre-rebase.sample BEGIN ###
#!/bin/sh
#
# Copyright (c) 2006, 2008 Junio C Hamano
#
# The "pre-rebase" hook is run just before "git rebase" starts doing
# its job, and can prevent the command from running by exiting with
# non-zero status.
#
# The hook is called with the following parameters:
#
# $1 -- the upstream the series was forked from.
# $2 -- the branch being rebased (or empty when rebasing the current branch).
#
# This sample shows how to prevent topic branches that are already
# merged to 'next' branch from getting rebased, because allowing it
# would result in rebasing already published history.

publish=next
basebranch="$1"
if test "$#" = 2
then
	topic="refs/heads/$2"
else
	topic=`git symbolic-ref HEAD` ||
	exit 0 ;# we do not interrupt rebasing detached HEAD
fi

case "$topic" in
refs/heads/??/*)
	;;
*)
	exit 0 ;# we do not interrupt others.
	;;
esac

# Now we are dealing with a topic branch being rebased
# on top of master.  Is it OK to rebase it?

# Does the topic really exist?
git show-ref -q "$topic" || {
	echo >&2 "No such branch $topic"
	exit 1
}

# Is topic fully merged to master?
not_in_master=`git rev-list --pretty=oneline ^master "$topic"`
if test -z "$not_in_master"
then
	echo >&2 "$topic is fully merged to master; better remove it."
	exit 1 ;# we could allow it, but there is no point.
fi

# Is topic ever merged to next?  If so you should not be rebasing it.
only_next_1=`git rev-list ^master "^$topic" ${publish} | sort`
only_next_2=`git rev-list ^master           ${publish} | sort`
if test "$only_next_1" = "$only_next_2"
then
	not_in_topic=`git rev-list "^$topic" master`
	if test -z "$not_in_topic"
	then
		echo >&2 "$topic is already up to date with master"
		exit 1 ;# we could allow it, but there is no point.
	else
		exit 0
	fi
else
	not_in_next=`git rev-list --pretty=oneline ^${publish} "$topic"`
	/usr/bin/perl -e '
		my $topic = $ARGV[0];
		my $msg = "* $topic has commits already merged to public branch:\n";
		my (%not_in_next) = map {
			/^([0-9a-f]+) /;
			($1 => 1);
		} split(/\n/, $ARGV[1]);
		for my $elem (map {
				/^([0-9a-f]+) (.*)$/;
				[$1 => $2];
			} split(/\n/, $ARGV[2])) {
			if (!exists $not_in_next{$elem->[0]}) {
				if ($msg) {
					print STDERR $msg;
					undef $msg;
				}
				print STDERR " $elem->[1]\n";
			}
		}
	' "$topic" "$not_in_next" "$not_in_master"
	exit 1
fi

<<\DOC_END

This sample hook safeguards topic branches that have been
published from being rewound.

The workflow assumed here is:

 * Once a topic branch forks from "master", "master" is never
   merged into it again (either directly or indirectly).

 * Once a topic branch is fully cooked and merged into "master",
   it is deleted.  If you need to build on top of it to correct
   earlier mistakes, a new topic branch is created by forking at
   the tip of the "master".  This is not strictly necessary, but
   it makes it easier to keep your history simple.

 * Whenever you need to test or publish your changes to topic
   branches, merge them into "next" branch.

The script, being an example, hardcodes the publish branch name
to be "next", but it is trivial to make it configurable via
$GIT_DIR/config mechanism.

With this workflow, you would want to know:

(1) ... if a topic branch has ever been merged to "next".  Young
    topic branches can have stupid mistakes you would rather
    clean up before publishing, and things that have not been
    merged into other branches can be easily rebased without
    affecting other people.  But once it is published, you would
    not want to rewind it.

(2) ... if a topic branch has been fully merged to "master".
    Then you can delete it.  More importantly, you should not
    build on top of it -- other people may already want to
    change things related to the topic as patches against your
    "master", so if you need further changes, it is better to
    fork the topic (perhaps with the same name) afresh from the
    tip of "master".

Let's look at this example:

		   o---o---o---o---o---o---o---o---o---o "next"
		  /       /           /           /
		 /   a---a---b A     /           /
		/   /               /           /
	       /   /   c---c---c---c B         /
	      /   /   /             \         /
	     /   /   /   b---b C     \       /
	    /   /   /   /             \     /
    ---o---o---o---o---o---o---o---o---o---o---o "master"


A, B and C are topic branches.

 * A has one fix since it was merged up to "next".

 * B has finished.  It has been fully merged up to "master" and "next",
   and is ready to be deleted.

 * C has not merged to "next" at all.

We would want to allow C to be rebased, refuse A, and encourage
B to be deleted.

To compute (1):

	git rev-list ^master ^topic next
	git rev-list ^master        next

	if these match, topic has not merged in next at all.

To compute (2):

	git rev-list master..topic

	if this is empty, it is fully merged to "master".

DOC_END

### ./.git/hooks/pre-rebase.sample END ###

### ./.git/hooks/pre-commit.sample BEGIN ###
#!/bin/sh
#
# An example hook script to verify what is about to be committed.
# Called by "git commit" with no arguments.  The hook should
# exit with non-zero status after issuing an appropriate message if
# it wants to stop the commit.
#
# To enable this hook, rename this file to "pre-commit".

if git rev-parse --verify HEAD >/dev/null 2>&1
then
	against=HEAD
else
	# Initial commit: diff against an empty tree object
	against=$(git hash-object -t tree /dev/null)
fi

# If you want to allow non-ASCII filenames set this variable to true.
allownonascii=$(git config --type=bool hooks.allownonascii)

# Redirect output to stderr.
exec 1>&2

# Cross platform projects tend to avoid non-ASCII filenames; prevent
# them from being added to the repository. We exploit the fact that the
# printable range starts at the space character and ends with tilde.
if [ "$allownonascii" != "true" ] &&
	# Note that the use of brackets around a tr range is ok here, (it's
	# even required, for portability to Solaris 10's /usr/bin/tr), since
	# the square bracket bytes happen to fall in the designated range.
	test $(git diff --cached --name-only --diff-filter=A -z $against |
	  LC_ALL=C tr -d '[ -~]\0' | wc -c) != 0
then
	cat <<\EOF
Error: Attempt to add a non-ASCII file name.

This can cause problems if you want to work with people on other platforms.

To be portable it is advisable to rename the file.

If you know what you are doing you can disable this check using:

  git config hooks.allownonascii true
EOF
	exit 1
fi

# If there are whitespace errors, print the offending file names and fail.
exec git diff-index --check --cached $against --

### ./.git/hooks/pre-commit.sample END ###

### ./.git/hooks/applypatch-msg.sample BEGIN ###
#!/bin/sh
#
# An example hook script to check the commit log message taken by
# applypatch from an e-mail message.
#
# The hook should exit with non-zero status after issuing an
# appropriate message if it wants to stop the commit.  The hook is
# allowed to edit the commit message file.
#
# To enable this hook, rename this file to "applypatch-msg".

. git-sh-setup
commitmsg="$(git rev-parse --git-path hooks/commit-msg)"
test -x "$commitmsg" && exec "$commitmsg" ${1+"$@"}
:

### ./.git/hooks/applypatch-msg.sample END ###

### ./.git/hooks/fsmonitor-watchman.sample BEGIN ###
#!/usr/bin/perl

use strict;
use warnings;
use IPC::Open2;

# An example hook script to integrate Watchman
# (https://facebook.github.io/watchman/) with git to speed up detecting
# new and modified files.
#
# The hook is passed a version (currently 2) and last update token
# formatted as a string and outputs to stdout a new update token and
# all files that have been modified since the update token. Paths must
# be relative to the root of the working tree and separated by a single NUL.
#
# To enable this hook, rename this file to "query-watchman" and set
# 'git config core.fsmonitor .git/hooks/query-watchman'
#
my ($version, $last_update_token) = @ARGV;

# Uncomment for debugging
# print STDERR "$0 $version $last_update_token\n";

# Check the hook interface version
if ($version ne 2) {
	die "Unsupported query-fsmonitor hook version '$version'.\n" .
	    "Falling back to scanning...\n";
}

my $git_work_tree = get_working_dir();

my $retry = 1;

my $json_pkg;
eval {
	require JSON::XS;
	$json_pkg = "JSON::XS";
	1;
} or do {
	require JSON::PP;
	$json_pkg = "JSON::PP";
};

launch_watchman();

sub launch_watchman {
	my $o = watchman_query();
	if (is_work_tree_watched($o)) {
		output_result($o->{clock}, @{$o->{files}});
	}
}

sub output_result {
	my ($clockid, @files) = @_;

	# Uncomment for debugging watchman output
	# open (my $fh, ">", ".git/watchman-output.out");
	# binmode $fh, ":utf8";
	# print $fh "$clockid\n@files\n";
	# close $fh;

	binmode STDOUT, ":utf8";
	print $clockid;
	print "\0";
	local $, = "\0";
	print @files;
}

sub watchman_clock {
	my $response = qx/watchman clock "$git_work_tree"/;
	die "Failed to get clock id on '$git_work_tree'.\n" .
		"Falling back to scanning...\n" if $? != 0;

	return $json_pkg->new->utf8->decode($response);
}

sub watchman_query {
	my $pid = open2(\*CHLD_OUT, \*CHLD_IN, 'watchman -j --no-pretty')
	or die "open2() failed: $!\n" .
	"Falling back to scanning...\n";

	# In the query expression below we're asking for names of files that
	# changed since $last_update_token but not from the .git folder.
	#
	# To accomplish this, we're using the "since" generator to use the
	# recency index to select candidate nodes and "fields" to limit the
	# output to file names only. Then we're using the "expression" term to
	# further constrain the results.
	my $last_update_line = "";
	if (substr($last_update_token, 0, 1) eq "c") {
		$last_update_token = "\"$last_update_token\"";
		$last_update_line = qq[\n"since": $last_update_token,];
	}
	my $query = <<"	END";
		["query", "$git_work_tree", {$last_update_line
			"fields": ["name"],
			"expression": ["not", ["dirname", ".git"]]
		}]
	END

	# Uncomment for debugging the watchman query
	# open (my $fh, ">", ".git/watchman-query.json");
	# print $fh $query;
	# close $fh;

	print CHLD_IN $query;
	close CHLD_IN;
	my $response = do {local $/; <CHLD_OUT>};

	# Uncomment for debugging the watch response
	# open ($fh, ">", ".git/watchman-response.json");
	# print $fh $response;
	# close $fh;

	die "Watchman: command returned no output.\n" .
	"Falling back to scanning...\n" if $response eq "";
	die "Watchman: command returned invalid output: $response\n" .
	"Falling back to scanning...\n" unless $response =~ /^\{/;

	return $json_pkg->new->utf8->decode($response);
}

sub is_work_tree_watched {
	my ($output) = @_;
	my $error = $output->{error};
	if ($retry > 0 and $error and $error =~ m/unable to resolve root .* directory (.*) is not watched/) {
		$retry--;
		my $response = qx/watchman watch "$git_work_tree"/;
		die "Failed to make watchman watch '$git_work_tree'.\n" .
		    "Falling back to scanning...\n" if $? != 0;
		$output = $json_pkg->new->utf8->decode($response);
		$error = $output->{error};
		die "Watchman: $error.\n" .
		"Falling back to scanning...\n" if $error;

		# Uncomment for debugging watchman output
		# open (my $fh, ">", ".git/watchman-output.out");
		# close $fh;

		# Watchman will always return all files on the first query so
		# return the fast "everything is dirty" flag to git and do the
		# Watchman query just to get it over with now so we won't pay
		# the cost in git to look up each individual file.
		my $o = watchman_clock();
		$error = $output->{error};

		die "Watchman: $error.\n" .
		"Falling back to scanning...\n" if $error;

		output_result($o->{clock}, ("/"));
		$last_update_token = $o->{clock};

		eval { launch_watchman() };
		return 0;
	}

	die "Watchman: $error.\n" .
	"Falling back to scanning...\n" if $error;

	return 1;
}

sub get_working_dir {
	my $working_dir;
	if ($^O =~ 'msys' || $^O =~ 'cygwin') {
		$working_dir = Win32::GetCwd();
		$working_dir =~ tr/\\/\//;
	} else {
		require Cwd;
		$working_dir = Cwd::cwd();
	}

	return $working_dir;
}

### ./.git/hooks/fsmonitor-watchman.sample END ###

### ./.git/hooks/pre-receive.sample BEGIN ###
#!/bin/sh
#
# An example hook script to make use of push options.
# The example simply echoes all push options that start with 'echoback='
# and rejects all pushes when the "reject" push option is used.
#
# To enable this hook, rename this file to "pre-receive".

if test -n "$GIT_PUSH_OPTION_COUNT"
then
	i=0
	while test "$i" -lt "$GIT_PUSH_OPTION_COUNT"
	do
		eval "value=\$GIT_PUSH_OPTION_$i"
		case "$value" in
		echoback=*)
			echo "echo from the pre-receive-hook: ${value#*=}" >&2
			;;
		reject)
			exit 1
		esac
		i=$((i + 1))
	done
fi

### ./.git/hooks/pre-receive.sample END ###

### ./.git/hooks/prepare-commit-msg.sample BEGIN ###
#!/bin/sh
#
# An example hook script to prepare the commit log message.
# Called by "git commit" with the name of the file that has the
# commit message, followed by the description of the commit
# message's source.  The hook's purpose is to edit the commit
# message file.  If the hook fails with a non-zero status,
# the commit is aborted.
#
# To enable this hook, rename this file to "prepare-commit-msg".

# This hook includes three examples. The first one removes the
# "# Please enter the commit message..." help message.
#
# The second includes the output of "git diff --name-status -r"
# into the message, just before the "git status" output.  It is
# commented because it doesn't cope with --amend or with squashed
# commits.
#
# The third example adds a Signed-off-by line to the message, that can
# still be edited.  This is rarely a good idea.

COMMIT_MSG_FILE=$1
COMMIT_SOURCE=$2
SHA1=$3

/usr/bin/perl -i.bak -ne 'print unless(m/^. Please enter the commit message/..m/^#$/)' "$COMMIT_MSG_FILE"

# case "$COMMIT_SOURCE,$SHA1" in
#  ,|template,)
#    /usr/bin/perl -i.bak -pe '
#       print "\n" . `git diff --cached --name-status -r`
# 	 if /^#/ && $first++ == 0' "$COMMIT_MSG_FILE" ;;
#  *) ;;
# esac

# SOB=$(git var GIT_COMMITTER_IDENT | sed -n 's/^\(.*>\).*$/Signed-off-by: \1/p')
# git interpret-trailers --in-place --trailer "$SOB" "$COMMIT_MSG_FILE"
# if test -z "$COMMIT_SOURCE"
# then
#   /usr/bin/perl -i.bak -pe 'print "\n" if !$first_line++' "$COMMIT_MSG_FILE"
# fi

### ./.git/hooks/prepare-commit-msg.sample END ###

### ./.git/hooks/post-update.sample BEGIN ###
#!/bin/sh
#
# An example hook script to prepare a packed repository for use over
# dumb transports.
#
# To enable this hook, rename this file to "post-update".

exec git update-server-info

### ./.git/hooks/post-update.sample END ###

### ./.git/hooks/pre-merge-commit.sample BEGIN ###
#!/bin/sh
#
# An example hook script to verify what is about to be committed.
# Called by "git merge" with no arguments.  The hook should
# exit with non-zero status after issuing an appropriate message to
# stderr if it wants to stop the merge commit.
#
# To enable this hook, rename this file to "pre-merge-commit".

. git-sh-setup
test -x "$GIT_DIR/hooks/pre-commit" &&
        exec "$GIT_DIR/hooks/pre-commit"
:

### ./.git/hooks/pre-merge-commit.sample END ###

### ./.git/hooks/pre-applypatch.sample BEGIN ###
#!/bin/sh
#
# An example hook script to verify what is about to be committed
# by applypatch from an e-mail message.
#
# The hook should exit with non-zero status after issuing an
# appropriate message if it wants to stop the commit.
#
# To enable this hook, rename this file to "pre-applypatch".

. git-sh-setup
precommit="$(git rev-parse --git-path hooks/pre-commit)"
test -x "$precommit" && exec "$precommit" ${1+"$@"}
:

### ./.git/hooks/pre-applypatch.sample END ###

### ./.git/hooks/pre-push.sample BEGIN ###
#!/bin/sh

# An example hook script to verify what is about to be pushed.  Called by "git
# push" after it has checked the remote status, but before anything has been
# pushed.  If this script exits with a non-zero status nothing will be pushed.
#
# This hook is called with the following parameters:
#
# $1 -- Name of the remote to which the push is being done
# $2 -- URL to which the push is being done
#
# If pushing without using a named remote those arguments will be equal.
#
# Information about the commits which are being pushed is supplied as lines to
# the standard input in the form:
#
#   <local ref> <local oid> <remote ref> <remote oid>
#
# This sample shows how to prevent push of commits where the log message starts
# with "WIP" (work in progress).

remote="$1"
url="$2"

zero=$(git hash-object --stdin </dev/null | tr '[0-9a-f]' '0')

while read local_ref local_oid remote_ref remote_oid
do
	if test "$local_oid" = "$zero"
	then
		# Handle delete
		:
	else
		if test "$remote_oid" = "$zero"
		then
			# New branch, examine all commits
			range="$local_oid"
		else
			# Update to existing branch, examine new commits
			range="$remote_oid..$local_oid"
		fi

		# Check for WIP commit
		commit=$(git rev-list -n 1 --grep '^WIP' "$range")
		if test -n "$commit"
		then
			echo >&2 "Found WIP commit in $local_ref, not pushing"
			exit 1
		fi
	fi
done

exit 0

### ./.git/hooks/pre-push.sample END ###

### ./.git/hooks/update.sample BEGIN ###
#!/bin/sh
#
# An example hook script to block unannotated tags from entering.
# Called by "git receive-pack" with arguments: refname sha1-old sha1-new
#
# To enable this hook, rename this file to "update".
#
# Config
# ------
# hooks.allowunannotated
#   This boolean sets whether unannotated tags will be allowed into the
#   repository.  By default they won't be.
# hooks.allowdeletetag
#   This boolean sets whether deleting tags will be allowed in the
#   repository.  By default they won't be.
# hooks.allowmodifytag
#   This boolean sets whether a tag may be modified after creation. By default
#   it won't be.
# hooks.allowdeletebranch
#   This boolean sets whether deleting branches will be allowed in the
#   repository.  By default they won't be.
# hooks.denycreatebranch
#   This boolean sets whether remotely creating branches will be denied
#   in the repository.  By default this is allowed.
#

# --- Command line
refname="$1"
oldrev="$2"
newrev="$3"

# --- Safety check
if [ -z "$GIT_DIR" ]; then
	echo "Don't run this script from the command line." >&2
	echo " (if you want, you could supply GIT_DIR then run" >&2
	echo "  $0 <ref> <oldrev> <newrev>)" >&2
	exit 1
fi

if [ -z "$refname" -o -z "$oldrev" -o -z "$newrev" ]; then
	echo "usage: $0 <ref> <oldrev> <newrev>" >&2
	exit 1
fi

# --- Config
allowunannotated=$(git config --type=bool hooks.allowunannotated)
allowdeletebranch=$(git config --type=bool hooks.allowdeletebranch)
denycreatebranch=$(git config --type=bool hooks.denycreatebranch)
allowdeletetag=$(git config --type=bool hooks.allowdeletetag)
allowmodifytag=$(git config --type=bool hooks.allowmodifytag)

# check for no description
projectdesc=$(sed -e '1q' "$GIT_DIR/description")
case "$projectdesc" in
"Unnamed repository"* | "")
	echo "*** Project description file hasn't been set" >&2
	exit 1
	;;
esac

# --- Check types
# if $newrev is 0000...0000, it's a commit to delete a ref.
zero=$(git hash-object --stdin </dev/null | tr '[0-9a-f]' '0')
if [ "$newrev" = "$zero" ]; then
	newrev_type=delete
else
	newrev_type=$(git cat-file -t $newrev)
fi

case "$refname","$newrev_type" in
	refs/tags/*,commit)
		# un-annotated tag
		short_refname=${refname##refs/tags/}
		if [ "$allowunannotated" != "true" ]; then
			echo "*** The un-annotated tag, $short_refname, is not allowed in this repository" >&2
			echo "*** Use 'git tag [ -a | -s ]' for tags you want to propagate." >&2
			exit 1
		fi
		;;
	refs/tags/*,delete)
		# delete tag
		if [ "$allowdeletetag" != "true" ]; then
			echo "*** Deleting a tag is not allowed in this repository" >&2
			exit 1
		fi
		;;
	refs/tags/*,tag)
		# annotated tag
		if [ "$allowmodifytag" != "true" ] && git rev-parse $refname > /dev/null 2>&1
		then
			echo "*** Tag '$refname' already exists." >&2
			echo "*** Modifying a tag is not allowed in this repository." >&2
			exit 1
		fi
		;;
	refs/heads/*,commit)
		# branch
		if [ "$oldrev" = "$zero" -a "$denycreatebranch" = "true" ]; then
			echo "*** Creating a branch is not allowed in this repository" >&2
			exit 1
		fi
		;;
	refs/heads/*,delete)
		# delete branch
		if [ "$allowdeletebranch" != "true" ]; then
			echo "*** Deleting a branch is not allowed in this repository" >&2
			exit 1
		fi
		;;
	refs/remotes/*,commit)
		# tracking branch
		;;
	refs/remotes/*,delete)
		# delete tracking branch
		if [ "$allowdeletebranch" != "true" ]; then
			echo "*** Deleting a tracking branch is not allowed in this repository" >&2
			exit 1
		fi
		;;
	*)
		# Anything else (is there anything else?)
		echo "*** Update hook: unknown type of update to ref $refname of type $newrev_type" >&2
		exit 1
		;;
esac

# --- Finished
exit 0

### ./.git/hooks/update.sample END ###

### ./.git/hooks/push-to-checkout.sample BEGIN ###
#!/bin/sh

# An example hook script to update a checked-out tree on a git push.
#
# This hook is invoked by git-receive-pack(1) when it reacts to git
# push and updates reference(s) in its repository, and when the push
# tries to update the branch that is currently checked out and the
# receive.denyCurrentBranch configuration variable is set to
# updateInstead.
#
# By default, such a push is refused if the working tree and the index
# of the remote repository has any difference from the currently
# checked out commit; when both the working tree and the index match
# the current commit, they are updated to match the newly pushed tip
# of the branch. This hook is to be used to override the default
# behaviour; however the code below reimplements the default behaviour
# as a starting point for convenient modification.
#
# The hook receives the commit with which the tip of the current
# branch is going to be updated:
commit=$1

# It can exit with a non-zero status to refuse the push (when it does
# so, it must not modify the index or the working tree).
die () {
	echo >&2 "$*"
	exit 1
}

# Or it can make any necessary changes to the working tree and to the
# index to bring them to the desired state when the tip of the current
# branch is updated to the new commit, and exit with a zero status.
#
# For example, the hook can simply run git read-tree -u -m HEAD "$1"
# in order to emulate git fetch that is run in the reverse direction
# with git push, as the two-tree form of git read-tree -u -m is
# essentially the same as git switch or git checkout that switches
# branches while keeping the local changes in the working tree that do
# not interfere with the difference between the branches.

# The below is a more-or-less exact translation to shell of the C code
# for the default behaviour for git's push-to-checkout hook defined in
# the push_to_deploy() function in builtin/receive-pack.c.
#
# Note that the hook will be executed from the repository directory,
# not from the working tree, so if you want to perform operations on
# the working tree, you will have to adapt your code accordingly, e.g.
# by adding "cd .." or using relative paths.

if ! git update-index -q --ignore-submodules --refresh
then
	die "Up-to-date check failed"
fi

if ! git diff-files --quiet --ignore-submodules --
then
	die "Working directory has unstaged changes"
fi

# This is a rough translation of:
#
#   head_has_history() ? "HEAD" : EMPTY_TREE_SHA1_HEX
if git cat-file -e HEAD 2>/dev/null
then
	head=HEAD
else
	head=$(git hash-object -t tree --stdin </dev/null)
fi

if ! git diff-index --quiet --cached --ignore-submodules $head --
then
	die "Working directory has staged changes"
fi

if ! git read-tree -u -m "$commit"
then
	die "Could not update working tree to new HEAD"
fi

### ./.git/hooks/push-to-checkout.sample END ###

### ./.git/refs/heads/main BEGIN ###
22852ecbe03f5f140903efd03bfe1e954bf3b51e

### ./.git/refs/heads/main END ###

### ./.git/refs/remotes/origin/main BEGIN ###
22852ecbe03f5f140903efd03bfe1e954bf3b51e

### ./.git/refs/remotes/origin/main END ###

### DIRECTORY ./ FLATTENED CONTENT ###
