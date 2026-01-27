def c_to_f(c: float) -> float:
    return c * 9 / 5 + 32

def km_to_mi(km: float) -> float:
    return km * 0.621371

def read_float(prompt: str) -> float:
    while True:
        raw = input(prompt).strip().replace(',', '.')
        try:
            return float(raw)
        except ValueError:
            print('Please enter a valid number.')

def main() -> None:
    print('Unit Converter')
    print('1) Celsius -> Fahrenheit')
    print('2) Kilometers -> Miles')
    choice = input('Choose 1 or 2: ').strip()
    if choice == '1':
        c = read_float('Celsius: ')
        print(f'{c} C = {c_to_f(c):.2f} F')
    elif choice == '2':
        km = read_float('Kilometers: ')
        print(f'{km} km = {km_to_mi(km):.2f} mi')
    else:
        print('Invalid choice.')

if __name__ == '__main__':
    main()
