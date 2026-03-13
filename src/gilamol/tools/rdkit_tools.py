"""
RDKit utility functions for molecular processing.

This module will contain core cheminformatics operations used by GilaMol.
"""

from rdkit import Chem
from rdkit.Chem import Descriptors


def parse_smiles(smiles: str):
    """
    Convert a SMILES string into an RDKit molecule object.

    Returns None if the SMILES string is invalid.
    """
    mol = Chem.MolFromSmiles(smiles)
    return mol


def compute_basic_descriptors(smiles: str):
    """
    Compute a small set of molecular descriptors.

    Returns a dictionary of descriptor values.
    """

    mol = parse_smiles(smiles)

    if mol is None:
        raise ValueError(f"Invalid SMILES: {smiles}")

    descriptors = {
        "molecular_weight": Descriptors.MolWt(mol),
        "logp": Descriptors.MolLogP(mol),
        "num_h_donors": Descriptors.NumHDonors(mol),
        "num_h_acceptors": Descriptors.NumHAcceptors(mol),
        "num_rotatable_bonds": Descriptors.NumRotatableBonds(mol),
    }

    return descriptors
