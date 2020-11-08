import sys

gradeTotal = 0 
courseKey = None
count = 0
key=None

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
      
    if courseKey== course:
        gradeTotal += float(currentGrade)
        count += 1
        
    else:
        if courseKey:
            print(courseKey, "\t", float(gradeTotal/count))
        gradeTotal = float(currentGrade)
        count = 1
        courseKey = course
    
print(courseKey, "\t", float(gradeTotal/count))
 