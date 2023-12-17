# SubScan

SubScan is a Python tool for scanning subdomains and checking their HTTP status codes.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Options](#options)

## Features

- Scan subdomains and check their HTTP status codes
- Display results with color-coded status codes
- Save results to an output file

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/SubScan.git
    ```

2. Change into the project directory:

    ```bash
    cd SubScan
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the script with the following command:

```sh
./subscan.py -h
```
This will display help for the tool. Here are all the switches it supports.

```console
Options:
    domain_file: Specify the domain file containing subdomains to scan.
    -o, --output: Specify the output file to save the scan results.
```
