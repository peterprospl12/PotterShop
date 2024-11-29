import os


def convert_price(price : str) -> float:
    return float(price.replace(" zł", "").replace(",", ".").replace("\xa0", "").replace("zł", ""))

def correct_file_path(absolute_path : str, file_path : list) -> list:
    corrected_paths = []
    for path in file_path:
        corrected_paths.append(os.path.join(absolute_path, path))
    return corrected_paths