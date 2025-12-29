def score_password(pw: str) -> int:
    score = 0
    if len(pw) >= 8:
        score += 1
    if any(c.islower() for c in pw):
        score += 1
    if any(c.isupper() for c in pw):
        score += 1
    if any(c.isdigit() for c in pw):
        score += 1
    if any(not c.isalnum() for c in pw):
        score += 1
    return score

def label(score: int) -> str:
    labels = ['Very weak', 'Weak', 'Ok', 'Good', 'Strong', 'Very strong']
    return labels[score]

def main() -> None:
    pw = input('Enter a password: ').strip()
    if not pw:
        print('Password cannot be empty.')
        return
    s = score_password(pw)
    print(f'Score: {s}/5 - {label(s)}')

if __name__ == '__main__':
    main()
