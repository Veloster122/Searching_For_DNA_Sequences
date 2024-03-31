import sys


from Bio import Entrez
from Bio import SeqIO

Entrez.email = "202200065@estudantes.ips.pt"


def sequence_gather(database, term):
    handle = Entrez.esearch(db=database, term=term, usehistory="y")
    record = Entrez.read(handle)
    id_list = record["IdList"]
    handle = Entrez.efetch(db=database, id=id_list, rettype="fasta", retmode="text")
    sequences = list(SeqIO.parse(handle, "fasta"))
    return sequences

def display_sequences(sequences):
    print(sequences)

def main():
    """
    Main function to handle command-line arguments and retrieve sequences.
    """
    if len(sys.argv) != 4:
        print("Usage: python script.py <database> <search_term> <output_file>")
        sys.exit(1)

    database = sys.argv[1]
    search_term = sys.argv[2]
    output_file = sys.argv[3]

    sequences = sequence_gather(database, search_term)
    Display = display_sequences(sequences)
    with open(output_file, "w") as f:
        SeqIO.write(sequences, f, "fasta")

if __name__ == "__main__":
    main()

