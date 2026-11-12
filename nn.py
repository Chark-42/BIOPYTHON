from Bio.Seq import Seq
My_Seq=Seq("GATCCT")
for index,letter in enumerate(My_Seq):
   # print("%i %s" % (index, letter))

print(len(My_Seq))

#from Bio.Seq import Seq
#my_seq=Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC")
#print(len(my_seq))

#print(my_seq.count("A"))

#SLICING BIOLOGICAL SEQUENCES
from multiprocessing.resource_sharer import stop

from Bio.Seq import Seq
my_seq=Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC")
#print(my_seq[4:12])
##print(my_seq[0::3]) # this means that this sequence skips 3 strings and prints the 4th that last position translates to stride
#print(my_seq[0:15:2])
#print(my_seq[::-1])

#contigs= [Seq("ATG"), Seq("ATCCCG"), Seq("TTGCA")]
#spacer= Seq("N"*10)
#print(spacer.join (contigs))

#CHANGING CASE FOR DNA SEQUENCES
#from Bio.Seq import Seq
#dna_seq=("ACTAAAATTTCCCTCGGGactccagg")
#print(dna_seq.upper()) # converting all the nucs to upper case
#print(dna_seq.lower())#coverts the nucs to lower case
#dna_seq.complement()

from Bio.Seq import Seq
my_seq = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC")
#complement=my_seq.complement()
#reverse_complement=my_seq.reverse_complement()
##reverse_complement=complement[::-1]
#print(f"complement_sequence:",complement)
#print(f"reverse_complement_sequence:",reverse_complement)
#EITHER OF THE REVERSE COMPLEMENTS CAN WORK
  

##TRANSCRIPTION
from Bio.Seq import Seq
coding_seq=("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")
#print(sequence_1)
#coding_seq=sequence_1.reverse_complement
#print(f"coding_sequence:",coding_seq)
#template_dna = coding_seq.reverse_complement()
#template_dna

#from Bio.Seq import Seq
#messenger_rna = Seq("AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUAG")
#protein=messenger_rna.translate()# translating using the regular genetic table
#protein=messenger_rna.translate(table="Vertebrate Mitochondrial")
#print(protein)


#from Bio.Seq import Seq
#seq=Seq("GTGAAAAAGATGCAATCTATCGTACTCGCACTTTCCCTGGTTCTGGTCGCTCCCATGGCA"
#"GCACAGGCTGCGGAAATTACGTTAGTCCCGTCAGTAAAATTACAGATAGGCGATCGTGAT"
#"AATCGTGGCTATTACTGGGATGGAGGTCACTGGCGCGACCACGGCTGGTGGAAACAACAT"
#"TATGAATGGCGAGGCAATCGCTGGCACCTACACGGACCGCCGCCACCGCCGCGCCACCAT"
#"AAGAAAGCTCCTCATGATCATCACGGCGGTCATGGTCCAGGCAAACATCACCGCTAA")
#print(Seq.translate(table="Bacterial"))
##protein=seq.translate(table="Bacterial",cds=True)
#print(protein)

#from Bio.Seq import CodonTable
#standard_codon_table= CodonTable.unambiguous_dna_by_id[1]
#vertebrate_codon_table=CodonTable.unambiguous_dna_by_id[2]
#print(standard_codon_table)
#print(vertebrate_codon_table)
#stop_codons_1=vertebrate_codon_table.stop_codons
#print(f"stop_codons_1:",stop_codons_1)

#stop_codons_2=standard_codon_table.stop_codons
#print(f"stop_codons_2:",stop_codons_2)

from Bio.Seq import Seq
#Seq_1=Seq("ATC")
#"ATC" == Seq_1
#WHY IS I NOT PRINTING TRUE AT THE TERMINAL


#MUTABLE SEQ OBJECTS involves the conversion of dna seq to a form that can be altered
from Bio.Seq import Seq, MutableSeq
mut_seq=MutableSeq("GCCATTGTAATGGGCCGCTGAAAGGGTGCCCGA")
print(mut_seq)

mut_seq.remove("A")
print(mut_seq)

mut_seq.reverse()
print(mut_seq)

#HOW DO YOU ACTUALLY REPLACE A NUCS
mut_seq[5]
print(mut_seq)

seq_new=Seq(mut_seq)
print(seq_new)



from Bio.Seq import Seq

unk_dna = Seq("N" * 15)
unk_prot = Seq("X" * 22)
print(unk_dna)
print(unk_prot)

from Bio.Seq import Seq