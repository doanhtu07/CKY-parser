# CKY-parser

A simple Cocke-Kasami-Younger (CKY) parser to create parse trees for sentences

## Usage

1. Go to main() function, then adjust the sentences array to your preference.

2. Adjust the CNF library to your preference. The library is a Chomsky Normal Form library containing all forms in your grammar. You should declare base cases for your atomic word too like in `CNF-lib.txt` right now.

3. Then run simply the main.py with the path to CNF library: `python3 main.py [path] [mode]`
- `path` is required: Should take a simple path like `./CNF-lib.txt`
- `mode` is optional: Should take values `compact` or `expand` (Default: `expand`)