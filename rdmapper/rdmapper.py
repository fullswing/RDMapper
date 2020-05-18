import copy
import rdkit
from rdkit import Chem
from rdkit.Chem import rdChemReactions, Draw, AllChem, rdchem, rdFMCS
from rdkit.Chem.Draw import rdMolDraw2D
from rdkit.Chem.Draw.rdMolDraw2D import MolDraw2DSVG
from typing import Any, Dict
import networkx as nx

class Error(Exception):
    pass

class FormatError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

def initialize_smarts(smarts: str, start_count: int = 1) -> str:
    initialized_smarts = ""
    count = start_count
    idx = 0
    while idx < len(smarts):
        from_idx = -1
        to_idx = -1
        if smarts[idx] == '[':
            initialized_smarts += '['
            idx += 1
            if smarts[idx] == '#':
                initialized_smarts += smarts[idx]
                idx += 1
                from_idx = idx
            else:
                raise FormatError(smarts, "Invalid SMARTS")
        elif smarts[idx] == ']':
            to_idx = idx
            digit = smarts[from_idx:to_idx]
            initialized_smarts += "{}:{}".format(digit, count)
            idx += 1
            count += 1
            initialized_smarts += ']'
        else:
            initialized_smarts += smarts[idx]
            idx += 1
    return initialized_smarts, count

def smiles_to_smarts(smiles):
    return Chem.MolToSmarts(Chem.MolFromSmiles(smiles))

def smarts_to_graph(smarts: str) -> Any:
    reactant_graph = nx.Graph()
    product_graph = nx.Graph()
    return reactant_graph, product_graph

def mcs_mapping(reactant_graph, product_graph) -> Dict:
    return {}

def mapped_smarts(smarts: str, idx_mapping: Dict):
    return smarts

def atom_mapper(smarts: str) -> str:
    reactant_graph, product_graph = smarts_to_graph(smarts)
    idx_mapping = mcs_mapping(reactant_graph, product_graph)
    result = mapped_smarts(smarts, idx_mapping)
    return result