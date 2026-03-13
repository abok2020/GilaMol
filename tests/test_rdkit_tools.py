from gilamol.tools.rdkit_tools import compute_basic_descriptors, parse_smiles


def test_parse_smiles_valid():
    mol = parse_smiles("CCO")
    assert mol is not None


def test_parse_smiles_invalid():
    mol = parse_smiles("not_a_smiles")
    assert mol is None


def test_compute_basic_descriptors_valid():
    descriptors = compute_basic_descriptors("CCO")

    assert "molecular_weight" in descriptors
    assert "logp" in descriptors
    assert "num_h_donors" in descriptors
    assert "num_h_acceptors" in descriptors
    assert "num_rotatable_bonds" in descriptors

    assert descriptors["num_h_donors"] == 1
    assert descriptors["num_h_acceptors"] == 1


def test_compute_basic_descriptors_invalid():
    try:
        compute_basic_descriptors("not_a_smiles")
        assert False, "Expected ValueError for invalid SMILES"
    except ValueError:
        assert True
