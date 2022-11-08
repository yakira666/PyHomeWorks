amount_participants = [input("Введите фамилию кандидата и количество голосов: ").title().split() for _ in
                       range(int(input("Введите количество записей: ")))]

counted_votes = {}
for item in amount_participants:
    counted_votes[item[0]] = counted_votes.get(item[0], 0) + int(item[1])

for participant in counted_votes:
    print(f"\n{participant} | Общее количество голосов: {counted_votes.get(participant)}")
