amount_participants = [input("Введите фамилию кандидата и количество голосов: ").title().split() for _ in
                       range(int(input("Введите количество записей: ")))]

counted_votes = {}
for i in amount_participants:
    counted_votes[i[0]] = counted_votes.get(i[0], 0) + int(i[1])

for participant in counted_votes:
    print(f"\n{participant} | Общее количество голосов: {counted_votes.get(participant)}")
