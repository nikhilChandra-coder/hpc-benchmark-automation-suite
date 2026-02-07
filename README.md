# HPC Benchmark Automation Suite

![Status](https://img.shields.io/badge/build-passing-brightgreen) ![Python](https://img.shields.io/badge/python-3.10%2B-blue) ![ReFrame](https://img.shields.io/badge/reframe-4.x-orange)

## Project Overview
This project is an automated regression testing framework designed to simulate High-Performance Computing (HPC) workflows. It uses **ReFrame** to orchestrate the compilation and execution of C++ scientific kernels (Matrix Multiplication) in a staged environment, ensuring reproducibility and performance verification.

## Architecture
The suite follows a standard HPC "Build-Run-Analyze" lifecycle:
1.  **Stage:** Isolates source code in a temporary sandbox.
2.  **Build:** Compiles C++ kernels using `g++` with optimization flags.
3.  **Run:** Executes the binary and captures standard output.
4.  **Verify:** regex-based sanity checks ensure numerical correctness.
5.  **Analyze:** A Python aggregator parses logs and ingests **GFlops** metrics into a SQL backend.

## Tech Stack
* **Framework:** ReFrame 4.x
* **Languages:** Python, C++, SQL, Bash
* **Database:** SQLite (Prototyping), extensible to InfluxDB
* **System:** Linux (WSL/Ubuntu)

## Quick Start

### 1. Install Dependencies
pip install reframe-hpc

### 2. Run the Benchmark
reframe -c matrix_test.py -r --report-file report.json

### 3. Ingest Data
python3 aggregator.py report.json

### 4. Query Results
sqlite3 hpc_metrics.db "SELECT * FROM benchmark_runs;"

Sample Output

[SUCCESS] Ingesting: MatrixBenchmark -> GFlops = 0.37 GFlops
