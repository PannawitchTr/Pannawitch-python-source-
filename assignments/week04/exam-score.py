scores = []

for i in range(1,6):
    score = float(input(f"Enter score of student {i}: "))
    scores.append(score)
print()
for score in scores:
    result = "ไม่ผ่าน"

    if score >= 50:
        result = "ผ่าน"

    print(f"Student {i} {score:.0f} -> {result}")
