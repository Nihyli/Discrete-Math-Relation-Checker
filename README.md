# Relation Checker

## Files

* **main.py**  
  The core script that:
  1. Parses the input file.
  2. Checks relation properties.
  3. Prints each property (Yes/No).
  4. If not an equivalence relation, prints closures in order.

* **testcases/**  
  Sample inputs covering empty, degenerate, valid, and malformed relations:

  * `test1.txt` – Empty relation (n=0)  
  * `test2.txt` – Single element, non-reflexive  
  * `test3.txt` – Single element, reflexive  
  * `test4.txt` – Identity on 2 elements (equivalence)  
  * `test5.txt` – Symmetric but not reflexive (2×2)  
  * `test6.txt` – 3×3: reflexive only  
  * `test7.txt` – 3×3 identity (equivalence)  
  * `test8.txt` – Asymmetric example (3×3)  
  * `test9.txt` – Reflexive only, needs symmetric & transitive closures  
  * `test10.txt` – Missing entries

## Usage

Run the script with one argument pointing to a test file:

```bash
python3 main.py testcases/testX.txt
