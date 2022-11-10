amount_participants = {}
for _ in range(int(input("Введите количество записей: "))):
    participant, votes = input("Введите фамилию кандидата и количество голосов: ").split()
    participant = participant.lower()
    amount_participants[participant] = amount_participants.get(participant, 0) + int(votes)

print()

for name, vote in amount_participants.items():
    print(f"{name.capitalize()} | Общее количество голосов: {vote}")
