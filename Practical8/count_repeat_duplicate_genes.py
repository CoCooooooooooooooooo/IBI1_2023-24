import re

repeat_sequence = input("Please input one of the 2 the sequence 'GTGTGT' or 'GTCTGT': ")
output_file_name = f"{repeat_sequence}_duplicate_genes.fa"
fasta_file_path = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'

def repetitive_counter(seq, pattern):
    return len(re.findall(pattern, seq))

def extract_and_write_fasta(fasta_file_path, output_file_path, repeat_seq):
    with open(fasta_file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
        gene_sequence = ''  
        for line in infile:
            if line.startswith('>'):
                if gene_sequence and repetitive_counter(gene_sequence, repeat_seq) != 0:  
                    outfile.write(f">{current_gene} Repeat:{repetitive_counter(gene_sequence, repeat_seq)}\n{gene_sequence}\n")
                current_gene = line[1:].strip().split()[0]  
                gene_sequence = ''  
                if re.search(r'\bduplication\b', line[1:].strip()):
                    writing = True
                else:
                    writing = False
                    continue
            elif writing:  
                gene_sequence += line.strip()

        if gene_sequence and repetitive_counter(gene_sequence, repeat_seq) != 0:
            outfile.write(f">{current_gene} Repeat:{repetitive_counter(gene_sequence, repeat_seq)}\n{gene_sequence}\n")

extract_and_write_fasta(fasta_file_path, output_file_name, repeat_sequence)