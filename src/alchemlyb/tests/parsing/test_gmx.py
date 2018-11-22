"""Gromacs parser tests.

"""

from alchemlyb.parsing.gmx import extract_dHdl, extract_u_nk
from alchemtest.gmx import load_benzene
from alchemtest.gmx import load_expanded_ensemble_case_1, load_expanded_ensemble_case_2, load_expanded_ensemble_case_3


def test_dHdl():
    """Test that dHdl has the correct form when extracted from files.

    """
    dataset = load_benzene()

    for leg in dataset['data']:
        for filename in dataset['data'][leg]:
            dHdl = extract_dHdl(filename, T=300)

            assert dHdl.index.names == ['time', 'fep-lambda']
            assert dHdl.shape == (4001, 1)

def test_u_nk():
    """Test that u_nk has the correct form when extracted from files.

    """
    dataset = load_benzene()

    for leg in dataset['data']:
        for filename in dataset['data'][leg]:
            u_nk = extract_u_nk(filename, T=300)

            assert u_nk.index.names == ['time', 'fep-lambda']
            if leg == 'Coulomb':
                assert u_nk.shape == (4001, 5)
            elif leg == 'VDW':
                assert u_nk.shape == (4001, 16)

def test_u_nk_case1():
    """Test that u_nk has the correct form when extracted from expanded ensemble files (case 1).

    """
    dataset = load_expanded_ensemble_case_1()

    for leg in dataset['data']:
        for filename in dataset['data'][leg]:
            u_nk = extract_u_nk(filename, T=300)

            assert u_nk.index.names == ['time', 'fep-lambda', 'coul-lambda', 'vdw-lambda', 'restraint-lambda']

            assert u_nk.shape == (50001, 28)

def test_dHdl_case1():
    """Test that dHdl has the correct form when extracted from expanded ensemble files (case 1).

    """
    dataset = load_expanded_ensemble_case_1()

    for leg in dataset['data']:
        for filename in dataset['data'][leg]:
            dHdl = extract_dHdl(filename, T=300)

            assert dHdl.index.names == ['time', 'fep-lambda', 'coul-lambda', 'vdw-lambda', 'restraint-lambda']
            assert dHdl.shape == (50001, 4)

def test_u_nk_case2():
    """Test that u_nk has the correct form when extracted from expanded ensemble files (case 2).

    """
    dataset = load_expanded_ensemble_case_2()

    for leg in dataset['data']:
        for filename in dataset['data'][leg]:
            u_nk = extract_u_nk(filename, T=300)

            assert u_nk.index.names == ['time', 'fep-lambda', 'coul-lambda', 'vdw-lambda', 'restraint-lambda']

            assert u_nk.shape == (25001, 28)

def test_u_nk_case3():
    """Test that u_nk has the correct form when extracted from REX files (case 3).

    """
    dataset = load_expanded_ensemble_case_3()

    for leg in dataset['data']:
        for filename in dataset['data'][leg]:
            u_nk = extract_u_nk(filename, T=300)

            assert u_nk.index.names == ['time', 'fep-lambda', 'coul-lambda', 'vdw-lambda', 'restraint-lambda']

            assert u_nk.shape == (2500, 28)

def test_dHdl_case3():
    """Test that dHdl has the correct form when extracted from REX files (case 3).

    """
    dataset = load_expanded_ensemble_case_3()

    for leg in dataset['data']:
        for filename in dataset['data'][leg]:
            dHdl = extract_dHdl(filename, T=300)

            assert dHdl.index.names == ['time', 'fep-lambda', 'coul-lambda', 'vdw-lambda', 'restraint-lambda']
            assert dHdl.shape == (2500, 4)
