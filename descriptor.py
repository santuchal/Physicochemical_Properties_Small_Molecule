#!/usr/bin/env python
# coding: utf-8

import os
import sys
import streamlit as st

from rdkit import Chem
from rdkit.Chem import MolFromSmiles
from rdkit.Chem.rdMolDescriptors import CalcMolFormula
from rdkit.Chem.Descriptors import CalcMolDescriptors


class Molecule:
	def __init__(self, smiles: str):

		if not smiles :
			print("Empty smiles are given")
			sys.exit()
		self.smiles = smiles
		self.mol = MolFromSmiles(smiles)

	def descriptor_generator(self):
		return CalcMolDescriptors(self.mol)

def convert_to_molecule(smiles: str):
    try:
        return Molecule(smiles)
    except ValueError:
        return None

SMI = st.text_input('Input SMILE', 'O=Cc1ccc(Cl)cc1')
st.write(f'Physicochemical Properties of :  **{SMI}**')
mol = convert_to_molecule(SMI)
descriptors = mol.descriptor_generator()

st.write("Formula : ", CalcMolFormula(Chem.MolFromSmiles(SMI)))
st.write("Molecular weight : ",str(float("{:.4f}".format(descriptors['MolWt'])))," g/mol ")
st.write(f"Number of H-bond Acceptors : **{str(descriptors['NumHAcceptors'])}**")
st.write(f"Number of H-bond donors :  **{str(descriptors['NumHDonors'])}**")
st.write(f"Number of Heavy Atoms: **{str(descriptors['HeavyAtomCount'])}**")
st.write(f"Number of Rotatable Bonds: **{str(descriptors['NumRotatableBonds'])}**")
st.write(f"FractionCSP3:",str(float("{:.4f}".format(descriptors['FractionCSP3']))))
st.write(f"Molar Refractivity:", str(float("{:.4f}".format(descriptors['MolMR']))))
st.write(f"TPSA:", str(float("{:.4f}".format(descriptors['TPSA']))))
st.write(f"Number of Rings: **{str(descriptors['RingCount'])}**")
st.write(f"Number of Heteroatoms: **{str(descriptors['NumHeteroatoms'])}**")
# st.write(f"Num. heavy atoms: **{str(descriptors['HeavyAtomCount'])}**")
# st.write(f"Num. heavy atoms: **{str(descriptors['HeavyAtomCount'])}**")
# st.write(f"Num. heavy atoms: **{str(descriptors['HeavyAtomCount'])}**")
# st.dataframe(descriptors_1)


