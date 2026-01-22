# Market Basket Analysis using FP-Growth Algorithm

This project performs **Market Basket Analysis** using the
**FP-Growth (Frequent Pattern Growth)** algorithm to identify frequently
purchased itemsets from transactional data. FP-Growth is an efficient
alternative to Apriori that avoids candidate generation and scales well
for large datasets.

---

## Overview

Market Basket Analysis helps uncover relationships between items that
are frequently purchased together. The FP-Growth algorithm builds a
compact data structure called an **FP-Tree** to mine frequent itemsets
efficiently.

This project demonstrates:
- Transaction encoding
- Frequent itemset mining using FP-Growth
- Support-based pattern discovery

---

## Dataset
- File: `Market_Basket_Optimisation.csv`
- Each row represents a transaction
- Each column represents an item in the transaction
- Missing or unused values indicate items not purchased in that
  transaction

---

## Workflow

### 1. Data Loading and Inspection
- Loaded the dataset using pandas
- Inspected dataset structure and data types
- Previewed sample transactions

---

### 2. Transaction Encoding
- Converted transactional data into a one-hot encoded format using
  `TransactionEncoder` from `mlxtend`
- Each column represents an item
- Each row represents a transaction with boolean values

---

### 3. FP-Growth Algorithm
- Applied the FP-Growth algorithm using `mlxtend.frequent_patterns`
- Extracted frequent itemsets based on a minimum support threshold:
  - `min_support = 0.001`
- Generated a list of frequent itemsets without explicit candidate
  generation

---

## Libraries Used
- pandas
- numpy
- mlxtend

---

## How to Run

### 1. Install dependencies
```bash
pip install pandas numpy mlxtend
