from pathlib import Path
import pandas as pd


def load_clinical_data(data_path="../data/raw", filename="clinical_data.txt"):
    data_path = Path(data_path)
    clinical_path = data_path / filename

    if not clinical_path.exists():
        raise FileNotFoundError(f"Clinical file not found: {clinical_path}")

    # sep=None + engine="python" intenta detectar automáticamente el separador
    clinical = pd.read_csv(clinical_path, sep=None, engine="python")
    return clinical


def load_case(case_id, data_path="../data/raw", cases_folder="cases"):
    data_path = Path(data_path)
    # Usar doble espacio para coincidir con los nombres reales
    filename = f"case  {case_id}.csv"
    if cases_folder is None:
        case_path = data_path / filename
    else:
        case_path = data_path / cases_folder / filename

    if not case_path.exists():
        raise FileNotFoundError(f"Case file not found: {case_path}")

    df = pd.read_csv(case_path)
    return df


def load_all_cases(data_path="../data/raw", cases_folder="cases", n_cases=208):
    patients = {}

    for case_id in range(1, n_cases + 1):
        patients[case_id] = load_case(
            case_id=case_id,
            data_path=data_path,
            cases_folder=cases_folder
        )

    return patients


def load_dataset(data_path="../data/raw", clinical_filename="clinical_data.txt", n_cases=208):
    clinical = load_clinical_data(
        data_path=data_path,
        filename=clinical_filename
    )

    # Detectar automáticamente el folder de casos
    cases_folder = "cases" if (Path(data_path) / "cases").exists() else None
    patients = load_all_cases(
        data_path=data_path,
        cases_folder=cases_folder,
        n_cases=n_cases
    )

    return clinical, patients