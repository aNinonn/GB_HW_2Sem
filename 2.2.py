# 2.2[12]: Петя и Катя – брат и сестра. Петя – студент, 
# а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать.

# Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.
S = 6
P = 5

discriminant = int((S**2 - 4*P)**0.5)

SN_var1 = int((S - discriminant)//2)
SN_var2 = int((S + discriminant)//2)

if SN_var1 >= 0:
     SecondNumber = SN_var1 
else:
     SecondNumber = SN_var2

FirstNumber = S - SecondNumber


print(f"{FirstNumber} {SecondNumber}")

