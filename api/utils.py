def convert_price(price : str) -> float:
    return float(price.replace(" zł", "").replace(",", ".").replace("\xa0", "").replace("zł", ""))