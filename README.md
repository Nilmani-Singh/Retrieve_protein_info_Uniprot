# Retrieve_protein_info_Uniprot

Read protein information from Uniprot website (https://www.uniprot.org/) and retrieve a few parameters using regular expressions (regex). 



The input file contains list of unique Uniprot ID of proteins in a text file. The uniprot IDs are separated by newline in the text file. If the IDs are separated by tab or space, this script won't work. 



The output will be an excel file with following infromation.

ID	:- The uniprot ID 

Name	:- The short recommended name 

Uniprot_Domains	:- The domains as listed on Uniprot. 
all domains found in protein will be written in one cell in excel.

Length	    :- Length of canonical isoform in amino acids

Isoforms	 :- NUmber of isoforms of the protein

PDB_ID	    :- The PDB ID, if there are any known crystal structures

Full name   :- Full name of the proteins
