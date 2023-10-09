#%%
print("Hello world!")



#%%
# Question 1: Create a Markdown cell with the followings:
# Two paragraphs about yourself. In one of the paragraphs, give a hyperlink of a website 
# that you want us to see. Can be about yourself, or something you like.
#%% [markdown] 
## Introduction 
# Hi, I am Kanishk. I am a Data Science graduate student at GWU. I might like capital regions as I have transitioned from New Delhi to Washington DC. Being a Delhite, I am a big-time foodie. Rajma Chawal while watching cricket is all I want. 
# 
# "Two roads diverged in a wood, and I, I took the one less travelled by, and that has made all the difference.” This line from “The Road Not Taken” by Robert Frost truly depicts my professional life till now, which has been like a mountain journey-curved roads everywhere. Like, I went on to pursue a B.S. in Mathematics instead of engineering and trust me that's not a trend in India. Lately, I developed an interest towards Data Science as it involves both Maths and programming. You can check out some of my work [here.](https://kanishkgoel1999.github.io/)


#%%
# Question 2: Create
# a list of all the class titles that you are planning to take in the data science program. 
# Have at least 6 classes, even if you are not a DS major
# Then print out the last entry in your list.

myCourseTitles = ['Intro to Data Science', 'Data Warehousing', 'Intro to Data Mining', 'Visualization of Complex Data', 'Machine Learning 1', 'Quantitative Investing', 'Deep Learning', 'Capstone Project']
myCourseTitles[-1]



#%%
# Question 3: After you completed question 2, you feel Intro to data mining is too stupid, so you are going 
# to replace it with Intro to Coal mining. Do that in python here.
i=0
for i in range(len(myCourseTitles)):
    if myCourseTitles[i]=='Intro to Data Mining':
        myCourseTitles[i]='Intro to Coal mining'
        break
    i+=1

myCourseTitles
        



#%%
# Question 4: Before you go see your academic advisor, you are 
# asked to create a python dictionary of the classes you plan to take, 
# with the course number as key. Since coal mining class doesn't have a 
# course number, so let's use Intro to Data Mining instead.

i=0
for i in range(len(myCourseTitles)):
    if myCourseTitles[i]=='Intro to Coal mining':
        myCourseTitles[i]='Intro to Data Mining'
        break
    i+=1

myCourseList = {6101:myCourseTitles[0], 
                6102:myCourseTitles[1], 
                6103:myCourseTitles[2], 
                6401:myCourseTitles[3], 
                6202:myCourseTitles[4], 
                4103:myCourseTitles[5], 
                6303:myCourseTitles[6], 
                6501:myCourseTitles[7]}

myCourseList


#%%
# Question 5: print out and show your advisor how many 
# classes (print out the number, not the list/dictionary) you plan 
# to take.
print('I am taking {} courses in total.'.format(len(myCourseTitles)))



#%%
# Question 6: Fast forward to the end of your degree here at GWU. You will no 
# longer take any more classes. Convert the list of Course Titles (list, not dictionary) 
# into a tuple, so no one will change it. 
# Print out the second half of the tuple. 

myTupleCourseTitles = tuple(myCourseTitles)
x=int(len(myTupleCourseTitles)/2)
myTupleCourseTitles[x:]


# %%
# Question 7: Create an object (JSON) described below, which is just multiple layers of 
# python lists and dictionary: 
# A dictionary about yourself, here at GW in data science, with the keys 
# "Firstname", "Lastname", "CompletedClasses", "InProgressClasses", "PlannedClasses", "ExpectedGraduationYear", 
# And for the record of each class, it should contains "CourseNumber", "CourseTitle", "Prerequisites".
# Note that each prerequisite class is a class itself, so it should have all these attributes as well. 
# For the InProgress and Completed classes, you should also include "Year", "Semester", "Instructor".
#
# ATTENTION: if you see a key/word in plural, that most likely means the value should be a list of similar 
# things. Otherwise, the value should be a single object.
#

myself = { "Firstname" : "Kanishk", 
            "Lastname" :  "Goel",
            "CompletedClasses" : [],
            "InProgressClasses" : [{"CourseNumber": 6101, "CourseTitle":"Intro to Data Science", "Prerequisites":"None", "Year":2023, "Semester":"Fall", "Instructor":"Darcy Morris"}, 
                                   {"CourseNumber":6102, "CourseTitle":"Data Warehousing", "Prerequisites":{"CourseNumber":2118, "CourseTitle":"Regression Analysis", "Prerequisites":"None"}, "Year":2023, "Semester":"Fall", "Instructor":"Abdi Awl"}, 
                                   {"CourseNumber":6103, "CourseTitle":"Intro to Data Mining", "Prerequisites":"None", "Year":2023, "Semester":"Fall", "Instructor":"Ning Rui"}],

            "PlannedClasses" : [{"CourseNumber":6401, "CourseTitle":"Visualization of Complex Data", "Prerequisites":[{"CourseNumber":6101, "CourseTitle":"Intro to Data Science", "Prerequisites":"None"},{"CourseNumber":6102, "CourseTitle":"Data Warehousing", "Prerequisites":"None"},{"CourseNumber":6103, "CourseTitle":"Intro to Data Mining", "Prerequisites":"None"}]},
                                {"CourseNumber":6202, "CourseTitle":"Machine Learning 1", "Prerequisites":[{"CourseNumber":6101, "CourseTitle":"Intro to Data Science", "Prerequisites":"None"}, {"CourseNumber":6103, "CourseTitle":"Intro to Data Mining", "Prerequisites":"None"}]},
                                {"CourseNumber":4103, "CourseTitle":"Quantitative Investing", "Prerequisites":{"CourseNumber":3501, "CourseTitle":"Financial Management and Markets", "Prerequisites":"None"}},
                                {"CourseNumber":6303, "CourseTitle":"Deep Learning", "Prerequisites":{"CourseNumber":6101, "CourseTitle":"Intro to Data Science", "Prerequisites":"None"}},
                                {"CourseNumber":6501, "CourseTitle":"Capstone Project", "Prerequisites":[{"CourseNumber":6101, "CourseTitle":"Intro to Data Science", "Prerequisites":"None"},{"CourseNumber":6102, "CourseTitle":"Data Warehousing", "Prerequisites":"None"},{"CourseNumber":6103, "CourseTitle":"Intro to Data Mining", "Prerequisites":"None"}]}],
            "ExpectedGraduationYear" : 2024
        }

myself

# %%
# Question 8: Make a copy of your info for a friend. Make sure that when they change their info, 
# yours will not be affected.
import copy
friend = copy.deepcopy(myself)


# %%
