"""reducer.py"""
# fill in code

import sys

courseKey = None   # Set key to None
course_list=[]     # Initialise course entry


# Read in lines from mapper output
# Strip of white spaces and split by tab
# Split by space
for line in sys.stdin:
    data = line.strip().split("\t")
    course, name_grade= data
    currentGrade, name = name_grade.split(" ",1)
    
    # Data integrity check
    try:
        currentGrade = int(currentGrade)
    except ValueError:
        # ignore/discard this line if value wasn't a number
        continue
        
    if courseKey == course:
        candidate_score= course, name,currentGrade 
        course_list.append(candidate_score)
        
    else:
        if courseKey:
            # Sort and select bottom 5 students for a last course
            bottomN=sorted(course_list,key=lambda student:student[2],reverse=False)[0:5]
            for bottom_student in bottomN:
                course, name,currentGrade =bottom_student
                print("{}\t{}\t\t{:.2%}".format(course,name,currentGrade/100))
            course_list=[]
        courseKey = course
        

# Sort and select bottom 5 students for last course
bottomN=sorted(course_list,key=lambda student:student[2],reverse=False)[0:5]
for bottom_student in bottomN:
    course, name,currentGrade =bottom_student
    print("{}\t{}\t\t{:.2%}".format(course,name,currentGrade/100))
