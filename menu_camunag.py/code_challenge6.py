print("\tGrading System\n")

prelim_grade = eval(input("enter your Prelim Grade ---> : "))
midterm_grade = eval(input("enter your Midterm Grade ---> : "))
semifinal_grade = eval(input("enter your Semi Final Grade ---> : "))
final_grade = eval(input("enter your Final Grade ---> : "))
quiz_grade = eval(input("enter your Quiz Grade ---> : ")) 
project_grade = eval(input("enter your Project Grade ---> : ")) 

prelim_fg = prelim_grade * .15
midterm_fg = midterm_grade * .15
semifinal_fg = semifinal_grade * .15
final_fg = final_grade * .15
quiz_fg = quiz_grade * .25
project_fg = project_grade * .15

fg = prelim_fg + midterm_fg + semifinal_fg + final_fg + quiz_fg + project_fg

print("\nYour Prelim Grade is", prelim_fg)
print("Your Midterm Grade is", midterm_fg)
print("Your Semi Final Grade is", semifinal_fg)
print("Your Final Grade is", final_fg)
print("Your Quiz Grade is", quiz_fg)
print("Your Project Grade is", project_fg)
print("\nYour Overall FG is", fg)

if fg > 74:
	print("\nCongratulations! You passed the course!")
else:
	print("\nSorry, you failed.")
