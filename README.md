HDB Resale Data ETL Pipeline
Objective

Develop an end-to-end ETL pipeline that:

Combines all HDB resale datasets
Performs data profiling
Applies validation and cleaning rules
Generates transformed data
Creates hashed identifiers
Produces separate output datasets
Technologies Used
Python 3.x
Pandas
Jupyter Notebook
hashlib (SHA-256)
Git
Project Structure
HDB_ETL/
│
├── input/
│
├── output/
│   ├── raw/
│   ├── cleaned/
│   ├── transformed/
│   ├── hashed/
│   └── failed/
│
├── src/
│   ├── ingestion.py
│   ├── profiling.py
│   ├── validation.py
│   ├── cleaning.py
│   ├── transformation.py
│   ├── hashing.py
│   └── output.py
│
├── notebooks/
│   └── HDB_ETL.ipynb
│
└── README.md
Validation Rules
Month format (YYYY-MM)
Valid town
Valid flat type
Valid storey range
Floor area > 0
Resale price > 0
Cleaning Rules
Standardize flat model
Remove duplicate records (keep highest resale price)
Recompute remaining lease
Detect resale price anomalies using the IQR method
Transformation
Average resale price by Month + Town + Flat Type
Resale Identifier generation

Format:

S + Block + AvgPrice + Month + TownInitial

Example:

S0192301A
Hashing

Algorithm:

SHA-256

Reason:

Irreversible
Deterministic
Low collision probability
Produces fixed 64-character hexadecimal hash
Outputs
Raw
Cleaned
Transformed
Failed
Hashed
How to Run
Install dependencies
Open Jupyter Notebook
Run all cells in order