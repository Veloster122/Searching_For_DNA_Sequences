This file contains a script using Entrez API that allows the user to gather sequences from NCBI database

/// Features

- gets the sequences from NCBI db.
- Allows the user to choose which database to query
- Allows the user to search a term to filter which sequences they want
- outputs the retrieved sequence into a FASTA file.

/// Pre-requisites

- This program was tested using python3 and linux shell
- you should have installed biopython: 'pip install biopython'
- import SeqIO and Entrez API

/// How does each function functions?

- 'sequence_gather(database, term)': as its name says, 'sequence gather' will search sequences according the
arguments: database and term
    - Entrez.esearch: in this line, 

/// How to use :D

- open your terminal in the directory of Entrez.py document
  You should type in the terminal: "python3 Entrez.py database <search_term> <output_file>"
  NOTE: in orther to correctly gather your sequence, you should replace:
    - 'database': Name of the db to query. for exemple: "nucleotide"
    - '<search_term>': A term to filter the sequences.
    - '<output_file>': A file to save the sequences gathered in a FASTA format.
  
  Exemple: "python3 Entrez.py nucleotide neurofibromin NF1.fasta"
    this exemple will gather sequences in the nucleotide database specifically the NF1 genes, associated to
  neurofibromin and they will be saved on a fasta file.

