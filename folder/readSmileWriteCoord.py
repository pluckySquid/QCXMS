import rdkit
import os

from rdkit import Chem
from rdkit.Chem import Draw
#from rdkit.Chem.Draw import IPythonConsole
from rdkit.Chem import Descriptors
from rdkit.Chem import AllChem
from rdkit import DataStructs
import numpy as np


directory = ""
  
# Parent Directory path
parent_dir = "/home/user/QCEIMS/rdk_Exp"
  
# Path
path = os.path.join(parent_dir, directory)
  
# Create the directory
# 'GeeksForGeeks' in
# '/home / User / Documents'




readFile = open('mols.txt', 'r')
Lines = readFile.readlines()




counter = 0
for line in Lines:
    counter = str(counter)
    m = Chem.MolFromSmiles(line)
    directory = counter
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)
    m_withHs = Chem.AddHs(m)
    AllChem.EmbedMolecule(m_withHs, randomSeed=0xf00d)
    print(Chem.MolToMolBlock(m_withHs),file=open(path+'/m.mol','w+'))
    Draw.MolToFile(m,'../images/ ' + counter + '.png') 
    counter = int(counter) + 1


