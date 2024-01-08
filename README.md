# Predictive Analytics of Brain Stroke  
We aim to examine how diverse factors such as gender, age, health conditions, lifestyle, and social variables influence brain stroke susceptibility. The study's results are vital for assessing stroke risk, shaping public health strategies, guiding medical interventions, and informing healthcare policies.

# Data
![image](https://github.com/KanishkGoel1999/FA23-DATS6101-Project-Group-6/assets/66896800/3cbbd462-5533-4261-b8ce-2a481ee2e2d4)
## Inferences from the data 
- Age: The mean and median do not have a huge difference, therefore less likely to have outliers.
- Avg_glucose_level: The mean and median have a significant difference and, therefore likely to have outliers.
- BMI: The mean and median do not have a huge difference, therefore less likely to have outliers.

# Checking for missing values and outliers
![image](https://github.com/KanishkGoel1999/FA23-DATS6101-Project-Group-6/assets/66896800/42df0150-1173-4bad-9dbc-366a13b6b89b)
## BMI
![image](https://github.com/KanishkGoel1999/FA23-DATS6101-Project-Group-6/assets/66896800/d5342ad5-8335-4904-bbc4-bb566486541f)
## Average glucose level
![image](https://github.com/KanishkGoel1999/FA23-DATS6101-Project-Group-6/assets/66896800/a69a48da-22a8-4e55-8d5c-5ffb141be351)

# Introducing a new column called Age categories
![image](https://github.com/KanishkGoel1999/FA23-DATS6101-Project-Group-6/assets/66896800/88ccd58d-136c-468b-a13c-4f56e5911134)

## Distribution of BMI and Avg Glucose Level
![image](https://github.com/KanishkGoel1999/FA23-DATS6101-Project-Group-6/assets/66896800/ac4a193f-6b81-4e8c-93fe-5fcb348a02ed)
![image](https://github.com/KanishkGoel1999/FA23-DATS6101-Project-Group-6/assets/66896800/ad35add6-7b24-4f93-85f7-22b42dbd508a)

## Box Plot of BMI by Gender
![image](https://github.com/KanishkGoel1999/FA23-DATS6101-Project-Group-6/assets/66896800/65c2641b-f377-4218-ad7e-29f166eb1632)
![image](https://github.com/KanishkGoel1999/FA23-DATS6101-Project-Group-6/assets/66896800/ae89d0af-9d81-4889-b981-d52e15d68f7d)

# 1. Does brain stroke depend on age group?
- Null Hypothesis(H0): Age groups and stroke variables are independent.
- Alternate Hypothesis(H1): Age group and stroke are not independent
![image](https://github.com/KanishkGoel1999/FA23-DATS6101-Project-Group-6/assets/66896800/374241da-2f65-43c4-a7e7-e5d6076366e7)

## Hypothesis Test Says: Age group and stroke are dependent
![image](https://github.com/KanishkGoel1999/FA23-DATS6101-Project-Group-6/assets/66896800/3f9baaef-bc30-471d-82d5-1f709cd819eb)

# 2. What is the case fatality rate of stroke by gender, location, and work type?
- Null Hypothesis(H0): Work type and stroke variables are independent.
- Alternate Hypothesis(H1): Work type and stroke are not independent.
![image](https://github.com/KanishkGoel1999/FA23-DATS6101-Project-Group-6/assets/66896800/184f3eb2-6702-4f96-9aed-fe15cce192a2)

## Hypothesis Test Says: Work type and stroke are dependent
![image](https://github.com/KanishkGoel1999/FA23-DATS6101-Project-Group-6/assets/66896800/d343cb1e-9241-4606-a4a2-9f5ba0150358)

Null Hypothesis(H0): Gender and stroke variables are independent.
Alternate Hypothesis(H1): Gender and stroke are not independent.

p-value: 0.575, Therefore gender and stroke are independent.

Null Hypothesis(H0): Location and stroke variables are independent.
Alternate Hypothesis(H1): Location and stroke are not independent.

p-value: 0.271, Therefore location and stroke are independent.

![image](https://github.com/KanishkGoel1999/FA23-DATS6101-Project-Group-6/assets/66896800/dfb49aa6-4a03-4434-8538-17d48af1b227)

# 3. Are there any biological or social factors that explain the gender differences in stroke risk?
- Null hypothesis(H0): ever_married and stroke variables are independent
- Alternative hypothesis(H1): ever_married and stroke variables are not independent
![image](https://github.com/KanishkGoel1999/FA23-DATS6101-Project-Group-6/assets/66896800/32b5ba76-73a0-4477-9fb6-2ce490bfde6e)

## Bar Plot of Percentage of Strokes by Ever-married or Not
![image](https://github.com/KanishkGoel1999/FA23-DATS6101-Project-Group-6/assets/66896800/61f4664a-7009-472f-bed3-2c4bdf782e39)

## Chi-squared test between ever-married and age period
- Null hypothesis(H0): ever_married and age are independent
- Alternative hypothesis(H1): ever_married and age are not independent
![image](https://github.com/KanishkGoel1999/FA23-DATS6101-Project-Group-6/assets/66896800/8a5f03f0-abcc-4ec4-a533-cdedd14f26f2)

# 4. What is the strength of the association between hypertension, heart disease, and brain stroke?
![image](https://github.com/KanishkGoel1999/FA23-DATS6101-Project-Group-6/assets/66896800/f983d07a-ce6b-41cc-87f9-ac49587f7b31)
![image](https://github.com/KanishkGoel1999/FA23-DATS6101-Project-Group-6/assets/66896800/40cebb37-94e1-4d22-b640-87b7122690a7)

## Hypothesis Test Says: Hypertension, heart disease and stroke are all related.
![image](https://github.com/KanishkGoel1999/FA23-DATS6101-Project-Group-6/assets/66896800/1c16ee67-ced8-4742-a00a-e9779a01dc67)

# What are modifiable risk factors for stroke in healthy people?
![image](https://github.com/KanishkGoel1999/FA23-DATS6101-Project-Group-6/assets/66896800/2237b0af-601a-44b1-bc54-501d6ac90378)

- Null hypothesis: Smoking status and stroke are independent
- Alternative hypothesis: Smoking status and stroke are not independent
![image](https://github.com/KanishkGoel1999/FA23-DATS6101-Project-Group-6/assets/66896800/cd305229-cf15-44f9-8fc5-bcf6bdca057e)

![image](https://github.com/KanishkGoel1999/FA23-DATS6101-Project-Group-6/assets/66896800/286ec1ea-83db-44f5-8e38-4f396bc86f10)

- Null hypothesis: Stroke and bmi are independent​
- Alternative hypothesis: Stroke and bmi are not independent

![image](https://github.com/KanishkGoel1999/FA23-DATS6101-Project-Group-6/assets/66896800/784d747e-2dec-48ee-a916-c3c1e99d8ef4)

![image](https://github.com/KanishkGoel1999/FA23-DATS6101-Project-Group-6/assets/66896800/bbcdc356-96e5-4692-b86b-344352e14f10)

- Null hypothesis: Stroke and average glucose level are independent​​
- Alternative hypothesis: Stroke and average glucose level are not independent​​
![image](https://github.com/KanishkGoel1999/FA23-DATS6101-Project-Group-6/assets/66896800/5f1cfa73-dfbd-4621-b2c4-904eede79294)

![image](https://github.com/KanishkGoel1999/FA23-DATS6101-Project-Group-6/assets/66896800/312a4252-6cc4-48df-aaa1-ea6e24024bf2)

![image](https://github.com/KanishkGoel1999/FA23-DATS6101-Project-Group-6/assets/66896800/7c24e032-06fc-4267-bfd2-5f03e3d57acc)

- Null Hypothesis: Stroke and marriage status are independent​​​
- Alternate hypothesis: Stroke and marriage status are not independent​​​
![image](https://github.com/KanishkGoel1999/FA23-DATS6101-Project-Group-6/assets/66896800/a9e7db50-17b0-47a5-9bdc-50942f93d702)

![image](https://github.com/KanishkGoel1999/FA23-DATS6101-Project-Group-6/assets/66896800/88d5f1e7-7133-4212-aea9-b4c8ac433aac)
