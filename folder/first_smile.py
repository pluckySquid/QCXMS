import rdkit

from rdkit import Chem
from rdkit.Chem import Draw
#from rdkit.Chem.Draw import IPythonConsole
from rdkit.Chem import Descriptors
from rdkit.Chem import AllChem
from rdkit import DataStructs
import numpy as np



m = Chem.MolFromSmiles('C(CCl)O')
m = Chem.MolFromSmiles('O')
#m = Chem.MolFromMolFile('data/input.mol')
#stringWithMolData=open('data/input.mol','r').read()
#m = Chem.MolFromMolBlock(stringWithMolData)
print("before: ")
print(Chem.MolToMolBlock(m))  
AllChem.Compute2DCoords(m)
print("after: ")
print(Chem.MolToMolBlock(m))  
m3 = Chem.AddHs(m)
AllChem.EmbedMolecule(m3)
print(Chem.MolToMolBlock(m)) 
print(Chem.MolToMolBlock(m3))   

print("m is: ", m)
mw = Descriptors.MolWt(m)
mw

print(mw)

Draw.MolToFile(m,'images/cdk2_mol1.o.png') 

m2 = Chem.MolFromSmiles('COc(c1)cccc1C#N')
#m2 = Chem.MolFromSmiles('C(CCl)O')
Draw.MolToFile(m2,'images/3-cyanoanisole.o.png') 


print(Chem.MolToMolBlock(m)) 
print(Chem.MolToMolBlock(m3),file=open('mol/foo.mol','w+'))










AllChem.Compute2DCoords(m2)
m4 = Chem.AddHs(m2)
print(Chem.MolToMolBlock(m4)) 
AllChem.Compute2DCoords(m4)
AllChem.EmbedMolecule(m4,randomSeed=0xf00d)

print(Chem.MolToMolBlock(m4))   
print("end")



m_Dichlorobenzamide = Chem.MolFromSmiles('C1=CC(=C(C(=C1)Cl)C(=O)N)Cl')
#m_Dichlorobenzamide = Chem.MolFromSmiles('C(CCl)O')

m_Dichlorobenzamide_withHs = Chem.AddHs(m_Dichlorobenzamide)
AllChem.EmbedMolecule(m_Dichlorobenzamide_withHs, randomSeed=0xf00d)
print(Chem.MolToMolBlock(m_Dichlorobenzamide_withHs),file=open('Dichlorobenzamide/m.mol','w+'))


readFile = open('Dichlorobenzamide/m.mol', 'r')
Lines = readFile.readlines()

writeFile = open('Dichlorobenzamide/coord', 'w')
writeFile.write("$coord\n")

for line in Lines:
    if " 0  0  0  0  0  0  0  0  0  0  0  0" in line:
        writeFile.write(line)
writeFile.write("$end")

