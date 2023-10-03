import json
import re

# Load periodic table data once
with open("PeriodicTable.json", "r", encoding="utf8") as fp:
    PERIODIC_TABLE = json.load(fp)["elements"]

SYMBOLS = [e['symbol'].lower() for e in PERIODIC_TABLE]

def grams_to_moles(compound: str) -> tuple[int, str]:
    grams = 0
    equation = ""
    elements = compound.split(" ")
    elements = split_alphanumeric(elements)
    for e in elements:
        if len(e) == 1:
            symbol, scalar = e[0], 1
        else:
            symbol, scalar = e[0], int(e[1])
        
        try:
            index = SYMBOLS.index(symbol.lower())
            element_object = PERIODIC_TABLE[index]
            grams += scalar * element_object["atomic_mass"]
            equation += f"{scalar}({element_object['atomic_mass']})+"
        except ValueError:
            print(f"Element {symbol} not found!")
            return 0, ""
    return grams, equation[:-1]

def split_alphanumeric(strings: list[str]) -> list[list[str]]:
    return [re.split(r'(?<=\D)(?=\d)|(?<=\d)(?=\D)', s) for s in strings] 

def main():
    symbol = input("Symbol: ")
    output = grams_to_moles(symbol)
    print(output[0], output[1], sep="\n")

if __name__ == "__main__":
    main()
