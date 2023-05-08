# Shared_Scripts

vectortotal.py --> Will read all input cif files in a directory and it will calculate the lattice vectors from the given a,b,c,alpha,beta,gamma. No need to specify anything. Will also write a "Lattice_Vector.txt" file with all the information.

qe_extra.py --> Contains some extra functions that are called in the other scripts present.

qe_in.py --> Will read all cif files in a directory and will write input files for each of the cifs present. #need to add the submission portion

QE_to_cif.py --> Converts a final output file from Quantum Espresso to a cif file to be used in mercury. This requires the output to have coordinates in crystal units. If they are in XYZ, change the resulting cif and use open babel to fix from xyz to crystal.

QE_proto_to_cif.py --> Same as QE_to_cif, just for Fixed cell relaxations that do not print lattice vectors at the end of the file.

