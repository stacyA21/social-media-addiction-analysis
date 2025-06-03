import pandas as  pd

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



df = pd.read_csv('sm_addiction.csv')

# Display the first 5 rows of the DataFrame
print('first 5 rows of the dataset:')
print(df.head(5))

# overview of the columns
print('overview of the columns:')  
print(df.columns)

# Create a list of column names
print('list of column names:')
colunm_names = df.columns.tolist()
print(colunm_names)

# check the data types of each column
print('data types of each column:')   
check = df.dtypes
print(check)

# check the number of rows and columns
print(f"Number of rows: {df.shape[0]}, Number of columns: {df.shape[1]}")

plt.hist(df['Gender'], bins=5, color='blue', edgecolor='black')
plt.title('Distribution of Gender in Social Media Addiction Dataset')
plt.xlabel('Gender')
plt.ylabel('Frequency')
plt.show()
plt.close()

# check if gender is balanced 
print('amount of Male participants:')
count_m = np.sum(df['Gender']== 'Male') # count
print(count_m)

print('amount of Female participants:')
count_f = np.sum(df['Gender']== 'Female') # count
print(count_f)

# check missing values in the dataset
print('missing values in the dataset:')
missing_values = df.isnull().sum()
print(missing_values)


#check if their is a connection between gender and addiction

sns.barplot(x='Gender', y='Addicted_Score', data=df)
plt.title('Average Addiction by Gender')
plt.xlabel('Gender')
plt.ylabel('Average Addiction')
plt.show()
plt.close()

print('Is there a connection between the Gender and Addiction Score?')

#calculate the average addcition score
average_addiction = df['Addicted_Score'].mean()
print(f'Average Addiction Score: {average_addiction}')

#calculate the average addiction score for women
average_addiction_f = np.mean(df[df['Gender']=='Female']['Addicted_Score'])
print(f'Average Addiction Score for women: {average_addiction_f}')
#calculate the average addiction score for mean

average_addiction_m = np.mean(df[df['Gender']=='Male']['Addicted_Score'])
print(f'Average Addiction Score for men : {average_addiction_m}')

print('Conclusion: There is not a significant difference in addiction score between men and women. \n' \
'The average addiction score for womwn is slightly higher than men, but the difference is not significant. \n' \
'This suggests that social media addiction is not significantly influenced by gender.')



#check how addiction effects night sleep

#check if there is a connection between mental health and addiction score
print('Is there a connection between Mental Health Score and Addiction Score?')
sns.scatterplot(x='Mental_Health_Score', y='Addicted_Score', data=df)
plt.title('Correlation Between Mental Health Score and Addiction Score')
plt.xlabel('Mental Health Score')
plt.ylabel('Addiction Score')
plt.show()

correlation = df['Mental_Health_Score'].corr(df['Addicted_Score'])
print(f'Correlation between Mental Health Score and Addiction Score: {correlation}')
print('Conclusion: There is a negative correlation between Mental Health Score and Addiction Score. \n' \
'This suggests that as Mental health increases, Adiccted score decreases. \n' \
'This indicates that social media addiction has a negative impact on mental health. \n' \
'or that people with poor mental health are more likely to be addicted to social media. \n' \
'This is a significant finding, as it suggests that social media addiction can have a negative impact on mental health.\n')

# create the distribution plot for age 
sns.histplot(df['Age'], kde=True, bins=20)
plt.title('Distribution of Age in Social Media Addiction Dataset')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()
plt.close()

# check the average addiction score for each age group
age_groups = pd.cut(df['Age'], bins=[0, 18, 25], labels=['0-18', '19-25'])
df['Age_Group'] = age_groups
average_addiction_by_age = df.groupby('Age_Group')['Addicted_Score'].mean().reset_index()
print('Average Addiction Score by Age Group:')
print(average_addiction_by_age)
sns.barplot(x='Age_Group', y='Addicted_Score', data=average_addiction_by_age)
plt.title('Average Addiction Score by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Average Addiction Score')
plt.show()
plt.close()

#calcilate the average addiction score for each age group
average_addiction_0_18 = np.mean(df[df['Age_Group']=='0-18']['Addicted_Score'])
print(f'Average Addiction Score for Age Group 0-18: {average_addiction_0_18}')
average_addiction_19_25 = np.mean(df[df['Age_Group']=='19-25']['Addicted_Score'])
print(f'Average Addiction Score for Age Group 19-25: {average_addiction_19_25}')


#which one is the most used platform 
print('Most used platform:')
most_used_platform = df['Most_Used_Platform'].mode()[0]
print(f'The most used platform is: {most_used_platform}')

#which platfporm is the most addictive
print('Most addictive platform:')
most_addictive_platform = df.groupby('Most_Used_Platform')['Addicted_Score'].mean().idxmax()
print(f'The most addictive platform is: {most_addictive_platform}')

#teh 2nd most addictive platform
second_most_addictive_platform = df.groupby('Most_Used_Platform')['Addicted_Score'].mean().nlargest(2).idxmin()
print(f'The second most addictive platform is: {second_most_addictive_platform}')

#create a overview of the addiction score for each platform
addiction_score_by_platform = df.groupby('Most_Used_Platform')['Addicted_Score'].mean().reset_index()
print('Addiction Score by Platform:')
print(addiction_score_by_platform)
 #order the platforms by addiction score
addiction_score_by_platform = addiction_score_by_platform.sort_values(by='Addicted_Score', ascending=False)
sns.barplot(x='Most_Used_Platform', y='Addicted_Score', data=addiction_score_by_platform)
plt.title('Addiction Score by Platform')
plt.xlabel('Platform')
plt.ylabel('Addiction Score')
plt.xticks(rotation=45)
plt.show()
plt.close()

#print top 3 most addictive platforms
top_3_addictive_platforms = addiction_score_by_platform.nlargest(3, 'Addicted_Score')
print('Top 3 most addictive platforms:')
print(top_3_addictive_platforms)

#ones with lower sleep hours per day which platform do they use the most
lower_sleep_hours_platform = df[df['Sleep_Hours_Per_Night'] < 6]['Most_Used_Platform'].value_counts().idxmax()
print(f'The most used platform by people with lower sleep hours is: {lower_sleep_hours_platform}')

#do tiktok users have a bad mental health score
tiktok_users = df[df['Most_Used_Platform'] == 'TikTok']
average_mental_health_tiktok = tiktok_users['Mental_Health_Score'].mean()
print(f'Average Mental Health Score for TikTok users: {average_mental_health_tiktok}')

#create an overview of the mental health score for each platform
mental_health_score_by_platform = df.groupby('Most_Used_Platform')['Mental_Health_Score'].mean().reset_index()
print('Mental Health Score by Platform:')
print(mental_health_score_by_platform)
#order the platforms by mental health score
mental_health_score_by_platform = mental_health_score_by_platform.sort_values(by='Mental_Health_Score', ascending=False)
sns.barplot(x='Most_Used_Platform', y='Mental_Health_Score', data=mental_health_score_by_platform)
plt.title('Mental Health Score by Platform')
plt.xlabel('Platform')
plt.ylabel('Mental Health Score')
plt.xticks(rotation=45)
plt.show()
plt.close()

#which platform has the highest average daily usage hours
average_daily_usage_by_platform = df.groupby('Most_Used_Platform')['Avg_Daily_Usage_Hours'].mean().reset_index()
print('Average Daily Usage Hours by Platform:')
print(average_daily_usage_by_platform)

