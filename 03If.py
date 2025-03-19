#2025. 3. 19.
#파이썬 수업 조건문

grad = " "
score = int(input("점수를 입력하세요: "))
if score > 60:
    grad = "합격"
else:
    if score > 50:
        grad = "임시합격"
    else:
        grad = "불합격"
print(grad)

if score >= 90:
    grad = 'A'
else:
    if score >= 80:
        grad = 'B'
    else:
        if score >= 70:
            grad = 'C'
        else:
            if score >= 60:
                grad ='D'
            else:
                grad = 'F'
print(grad)

