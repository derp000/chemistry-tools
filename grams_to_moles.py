import json
import re

symbols = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne',
            'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca',
            'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni',
            'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr',
            'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru',
            'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te',
            'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm',
            'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm',
            'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir',
            'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn',
            'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am',
            'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr',
            'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn',
            'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og']
symbols = [s.lower() for s in symbols]

# NaNO2
def grams_to_moles(compound: str) -> tuple[int, str]:
    grams = 0
    equation = ""
    elements = compound.split(" ")
    with open("PeriodicTable.json", "r", encoding="utf8") as fp:
        table = json.load(fp)["elements"]
        elements = split_alphanumeric(elements)
        for e in elements:
            symbol = e[0]
            scalar = e[1] if len(e) > 1 else 1
            index = symbols.index(symbol.lower())
            element_object = table[index]
            grams += float(scalar) * element_object["atomic_mass"]
            equation += f"{scalar}({element_object['atomic_mass']})+"
    return grams, equation[:-1]

def split_alphanumeric(strings: list[str]) -> list[list[str]]:
    return [re.split(r'(\d+)', s) for s in strings] 

def main():
    # print(grams_to_moles("Na N O2"))
    symbol = input("Symbol: ")
    output = grams_to_moles(symbol)
    print(output[0], output[1], sep="\n")

if __name__ == "__main__":
    main()
