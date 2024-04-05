# CKY-parser

A simple Cocke-Kasami-Younger (CKY) parser to create parse trees for sentences

## Usage

1. Go to main() function, then adjust the sentences array to your preference.

2. Adjust the CNF library to your preference. The library is a Chomsky Normal Form library containing all forms in your grammar. You should declare base cases for your atomic word too like in `CNF-lib.txt` right now.

3. Then run simply the main.py with the path to CNF library: `python3 main.py [path] [mode]`
- `path` is required: Should take a simple path like `./CNF-lib.txt`
- `mode` is optional: Should take values `compact` or `expand` (Default: `expand`)

## Example run

```
% python3 main.py ./CNF-lib.txt compact

Sentence: Figure skater lands historic quadruple jump in senior international competition at the 2019 World Figure Skating Championships on Day 3 but could only clinch a silver medal .

Parses: [['S', [(0, 20, 0), (21, 27, 0)]], ['S', [(0, 20, 2), (21, 27, 0)]], ['X14', [(0, 26, 0), (27, 27, 0)]], ['X14', [(0, 26, 1), (27, 27, 0)]], ['X14', [(0, 26, 2), (27, 27, 0)]], ['X14', [(0, 26, 3), (27, 27, 0)]]]

Number of parses: 6

Walks:

[S [X13 [VP [VP [VP [VP [X10 [NP [NOUN Figure] [NOUN skater]] [VERB lands]] [NP [ADJ historic] [X5 [ADJ quadruple] [NOUN jump]]]] [PP [PREP in] [NP [ADJ senior] [X5 [ADJ international] [NOUN competition]]]]] [PP [PREP at] [X11 [DET the] [NP [NUM 2019] [NP [X4 [NOUN World] [NOUN Figure]] [X4 [NOUN Skating] [NOUN Championships]]]]]]] [PP [PREP on] [NP [NOUN Day] [NUM 3]]]] [CONJ but]] [X14 [VP [VP [X9 [VERB could] [ADV only]] [VERB clinch]] [NP [X2 [DET a] [NOUN silver]] [NOUN medal]]] [PD .]]]

[S [X13 [VP [VP [VP [VP [VP [X10 [NP [NOUN Figure] [NOUN skater]] [VERB lands]] [NP [ADJ historic] [X5 [ADJ quadruple] [NOUN jump]]]] [PP [PREP in] [NP [ADJ senior] [X5 [ADJ international] [NOUN competition]]]]] [PP [PREP at] [X11 [DET the] [NP [NUM 2019] [NP [NOUN World] [NOUN Figure]]]]]] [NP [NOUN Skating] [NOUN Championships]]] [PP [PREP on] [NP [NOUN Day] [NUM 3]]]] [CONJ but]] [X14 [VP [VP [X9 [VERB could] [ADV only]] [VERB clinch]] [NP [X2 [DET a] [NOUN silver]] [NOUN medal]]] [PD .]]]

[X14 [VP [X7 [VP [VP [VP [VP [X10 [NP [NOUN Figure] [NOUN skater]] [VERB lands]] [NP [ADJ historic] [X5 [ADJ quadruple] [NOUN jump]]]] [PP [PREP in] [NP [ADJ senior] [X5 [ADJ international] [NOUN competition]]]]] [PP [PREP at] [X11 [DET the] [NP [NUM 2019] [NP [X4 [NOUN World] [NOUN Figure]] [X4 [NOUN Skating] [NOUN Championships]]]]]]] [PP [PREP on] [NP [NOUN Day] [NUM 3]]]] [CONJ but]] [VP [VP [X9 [VERB could] [ADV only]] [VERB clinch]] [NP [X2 [DET a] [NOUN silver]] [NOUN medal]]]] [PD .]]

[X14 [VP [X7 [VP [VP [VP [VP [VP [X10 [NP [NOUN Figure] [NOUN skater]] [VERB lands]] [NP [ADJ historic] [X5 [ADJ quadruple] [NOUN jump]]]] [PP [PREP in] [NP [ADJ senior] [X5 [ADJ international] [NOUN competition]]]]] [PP [PREP at] [X11 [DET the] [NP [NUM 2019] [NP [NOUN World] [NOUN Figure]]]]]] [NP [NOUN Skating] [NOUN Championships]]] [PP [PREP on] [NP [NOUN Day] [NUM 3]]]] [CONJ but]] [VP [VP [X9 [VERB could] [ADV only]] [VERB clinch]] [NP [X2 [DET a] [NOUN silver]] [NOUN medal]]]] [PD .]]

[X14 [VP [VP [X7 [VP [VP [VP [VP [X10 [NP [NOUN Figure] [NOUN skater]] [VERB lands]] [NP [ADJ historic] [X5 [ADJ quadruple] [NOUN jump]]]] [PP [PREP in] [NP [ADJ senior] [X5 [ADJ international] [NOUN competition]]]]] [PP [PREP at] [X11 [DET the] [NP [NUM 2019] [NP [X4 [NOUN World] [NOUN Figure]] [X4 [NOUN Skating] [NOUN Championships]]]]]]] [PP [PREP on] [NP [NOUN Day] [NUM 3]]]] [CONJ but]] [VP [X9 [VERB could] [ADV only]] [VERB clinch]]] [NP [X2 [DET a] [NOUN silver]] [NOUN medal]]] [PD .]]

[X14 [VP [VP [X7 [VP [VP [VP [VP [VP [X10 [NP [NOUN Figure] [NOUN skater]] [VERB lands]] [NP [ADJ historic] [X5 [ADJ quadruple] [NOUN jump]]]] [PP [PREP in] [NP [ADJ senior] [X5 [ADJ international] [NOUN competition]]]]] [PP [PREP at] [X11 [DET the] [NP [NUM 2019] [NP [NOUN World] [NOUN Figure]]]]]] [NP [NOUN Skating] [NOUN Championships]]] [PP [PREP on] [NP [NOUN Day] [NUM 3]]]] [CONJ but]] [VP [X9 [VERB could] [ADV only]] [VERB clinch]]] [NP [X2 [DET a] [NOUN silver]] [NOUN medal]]] [PD .]]
```