'''
Python program to find the average of best of 2 internal Assement
Marks from 3 internal Assesments Tests

'''
import math 
print("Enter the positive marks for Assignment 1,Assignment 2,Assignment 3")
print("Each ssignment is for max 25 marks")
assignment_marks=[]
print("enter the assignment marks")
for i in range(0,3):
    assignment_marks.append(float(input()))
    
    if assignment_marks > 25:
        exit()
print(assignment_marks);
highest = assignment_marks[0]
second_highest = assignment_marks[1]

for marks in assignment_marks:
    if marks > highest:
        second_highest=highest
        marks=second_highest
    else highest > marks > second_highest:
        second_highest=marks
print("highest:",highest,"second_highest:",second_highest)
final_avg= (highest+second_highest)/2
final_avg=math.ceil((final_avg*100)/100)
print("Final_average marks =",final_avg)