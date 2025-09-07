import pandas as  pd

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats



df = pd.read_csv('sm_addiction.csv')
print('Inspection of the dataset:')
#Display the first 5 rows of the DataFrame
print('first 5 rows of the dataset:')
print(df.head(5))

#overview of the columns
print('overview of the columns:')  
print(df.columns)

#Create a list of column names
print('list of column names:')
colunm_names = df.columns.tolist()
print(colunm_names)

# check the data types of each column
print('data types of each column:')   
check = df.dtypes
print(check)

#check the number of rows and columns
print(f"Number of rows: {df.shape[0]}, Number of columns: {df.shape[1]}")

plt.hist(df['Gender'], bins=5, color='blue', edgecolor='black')
plt.title('Distribution of Gender in Social Media Addiction Dataset')
plt.xlabel('Gender')
plt.ylabel('Frequency')
plt.show()
plt.close()

#check if gender is balanced 
print('amount of Male participants:')
count_m = np.sum(df['Gender']== 'Male') # count
print(count_m)

print('amount of Female participants:')
count_f = np.sum(df['Gender']== 'Female') # count
print(count_f)

#check missing values in the dataset
print('missing values in the dataset:')
missing_values = df.isnull().sum()
print(missing_values)

print('Analysis of Social Media Addiction Dataset')
#check if their is a connection between gender and addiction
print('Is there a connection between the Gender and Addiction Score?')

sns.barplot(x='Gender', y='Addicted_Score', data=df)
plt.title('Average Addiction by Gender')
plt.xlabel('Gender')
plt.ylabel('Average Addiction')
plt.show()
plt.close()

#calculate the average addcition score
average_addiction = df['Addicted_Score'].mean()
print(f'Average Addiction Score: {average_addiction}')

#calculate the average addiction score for women
average_addiction_f = np.mean(df[df['Gender']=='Female']['Addicted_Score'])
print(f'Average Addiction Score for women: {average_addiction_f}')

#calculate the average addiction score for men
average_addiction_m = np.mean(df[df['Gender']=='Male']['Addicted_Score'])
print(f'Average Addiction Score for men : {average_addiction_m}')

#perform a t-test to check if the difference is significant
addiction_score_women = df[df['Gender']=='Female']['Addicted_Score']
addiction_score_men = df[df['Gender']=='Male']['Addicted_Score']

t_stat, p_value = stats.ttest_ind(addiction_score_women, addiction_score_men, equal_var=False)
print(f'T-test results: t-statistic = {t_stat}, p-value = {p_value}')
if p_value < 0.05:
    print('The difference in addiction scores between men are women is statistically significant.')
else:
    print('The difference in addiction scores between men and women is not statistically significant.\n')

print('Conclusion: There is not a significant difference in addiction score between men and women. \n'
'This suggests that social media addiction is not significantly influenced by gender.\n')


#check if there is a connection between mental health and addiction score
print('Is there a correlation between Mental Health Score and Addiction Score?')
sns.scatterplot(x='Mental_Health_Score', y='Addicted_Score', data=df)
plt.title('Correlation Between Mental Health Score and Addiction Score')
plt.xlabel('Mental Health Score')
plt.ylabel('Addiction Score')
plt.show()

correlation = df['Mental_Health_Score'].corr(df['Addicted_Score'])
print(f'Correlation between Mental Health Score and Addiction Score: {correlation}')
print('Conclusion: There is a negative correlation between Mental Health Score and Addiction Score. \n' \
'This suggests that as Mental health increases, Adiccted score decreases. \n' \
'Either, social media addiction has a negative impact on mental health, \n' \
'or people with poor mental health are more likely to be addicted to social media. \n' \
'This suggests that social media addiction can have a negative impact on mental health.\n')

print('According to our analysis there is no correlation between gebder and addiction score, \n'
'but there is a correlation between mental health and addiction score. \n'
'Next we will look at the age of the participants and see if there is a connection between age and addiction score.\n')

# create the distribution plot for age 
print('Which age group is more addicted to social media?')

#distribution
sns.histplot(df['Age'], kde=True, bins=20)
plt.title('Distribution of Age in Social Media Addiction Dataset')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()
plt.close()

# check the average addiction score for each age group
age_groups = pd.cut(df['Age'], bins=[0, 18, 25], labels=['0-18', '19-25'])
df['Age_Group'] = age_groups
average_addiction_by_age = df.groupby('Age_Group', observed=False)['Addicted_Score'].mean().reset_index()
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

print('Conclusion: The average addiction score for the age group 0-18 is higher than the age group 19-25. \n'
'Younger people are more likely to be addicted to social media. \n'
'Meaning that social media addiction is more prevalent among younger people.\n')
print('Next we will look at the different platforms and see which platforms are the most addictive.\n')   

print('Analysis of Social Media Platforms')
#which platform is the most used
most_used_platform = df['Most_Used_Platform'].mode()[0]
print(f'The most used platform is: {most_used_platform}\n')

#which platforms are the two most addictive
print('Which platform is the most addictive?')
most_addictive_platform = df.groupby('Most_Used_Platform')['Addicted_Score'].mean().idxmax()
print(f'The most addictive platform is: {most_addictive_platform}')

second_most_addictive_platform = df.groupby('Most_Used_Platform')['Addicted_Score'].mean().nlargest(2).idxmin()
print(f'The second most addictive platform is: {second_most_addictive_platform}\n')

print('Overview of the addiction score for each platform')

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

#top 3 most addictive platforms
top_4_addictive_platforms = addiction_score_by_platform.nlargest(4, 'Addicted_Score')
print('Top 4 most addictive platforms:')
print(top_4_addictive_platforms)

print('Conclusion: The most addictive platform is Snapchat, followed by TikTok and Instagram. \n'
'These platforms have the highest average addiction scores,\n'
'indicating that users of these platforms are more likely to be addicted to social media.\n'   
'this is not counting whatsapp, as it is a means of communication between parent and child, work in some cases even school assignments.\n') 

print('Next we will look at the relationship between platform usage, sleep hours and mental health.\n')
#ones with lower sleep hours per day which platform do they use the most
print('Eventhough there is no direct data on the relationship between platform usage and sleep hours, \n'
'we can look at the most used platform by people with lower sleep hours.\n')

lower_sleep_hours_platform = df[df['Sleep_Hours_Per_Night'] < 6]['Most_Used_Platform'].value_counts().idxmax()
print(f'The most used platform by people with lower sleep hours is: {lower_sleep_hours_platform}')

print('Next we will look at the mental health scores of users of different platforms.\n'
      'We will first look at the mental health scores of tiktok users and\n'
      'compare them to the average mental health score of all users.\n')

#mental health scores of tiktok users 
tiktok_users = df[df['Most_Used_Platform'] == 'TikTok']
average_mental_health_tiktok = tiktok_users['Mental_Health_Score'].mean()
print(f'Average Mental Health Score for TikTok users: {average_mental_health_tiktok}\n')
#average mental health score of all users
average_mental_health_all = df['Mental_Health_Score'].mean()
print(f'Average Mental Health Score for all users: {average_mental_health_all}\n')

#is it significant lower
tiktok_mental_health_scores = tiktok_users['Mental_Health_Score']
all_mental_health_scores = df['Mental_Health_Score']
t_stat, p_value = stats.ttest_ind(tiktok_mental_health_scores, all_mental_health_scores, equal_var=False)
print(f'T-test results: t-statistic = {t_stat}, p-value = {p_value}')
if p_value < 0.05:
    print('The difference in mental health scores between TikTok users and all users is statistically significant.\n')
else:
    print('The difference in mental health scores between TikTok users and all users is not statistically significant.\n')  

print('Conclusion: The average mental health score for TikTok users is lower than the average mental health score of all users. \n'
'Sugesting that TikTok users may be more likely to have lower mental health scores. \n'
'Thus, TikTok usage may be associated with lower mental health scores.\n')


#mental health score for each platform

mental_health_score_by_platform = df.groupby('Most_Used_Platform')['Mental_Health_Score'].mean().reset_index()
print('Ordered Mental Health Score by Platform:')
ordered_platforms = mental_health_score_by_platform.sort_values(by='Mental_Health_Score', ascending=True)
print(ordered_platforms.head(5))

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
#order the platforms by average daily usage hours
ordered_platforms = average_daily_usage_by_platform.sort_values(by='Avg_Daily_Usage_Hours', ascending=False)
print(ordered_platforms.head(5))

#order the platforms by average daily usage hours
average_daily_usage_by_platform = average_daily_usage_by_platform.sort_values(by='Avg_Daily_Usage_Hours', ascending=False)
sns.barplot(x='Most_Used_Platform', y='Avg_Daily_Usage_Hours', data=average_daily_usage_by_platform)
plt.title('Average Daily Usage Hours by Platform')
plt.xlabel('Platform')
plt.ylabel('Average Daily Usage Hours')
plt.xticks(rotation=45)
plt.show()
plt.close()
 
print(average_daily_usage_by_platform.head(5))

#which platform do age group 0-18 use the most
most_used_platform_0_18 = df[df['Age_Group']=='0-18']['Most_Used_Platform'].mode()[0]
print(f'The most used platform by age group 0-18 is: {most_used_platform_0_18}')    
#which platform do age group 19-25 use the most
most_used_platform_19_25 = df[df['Age_Group']=='19-25']['Most_Used_Platform'].mode()[0]
print(f'The most used platform by age group 19-25 is: {most_used_platform_19_25}\n')

print('Conclusion: The most used platform by people with lower sleep hours is TikTok. \n'
'Thus, TikTok users may be more likely to have lower sleep hours. \n'
'TikTok usage may be associated with lower sleep hours.\n')

print('The average mental health score for TikTok users is lower than the average mental health score of all users. \n'
'This suggests that TikTok users may be more likely to have lower mental health scores. \n'
'Thus, TikTok usage may be associated with lower mental health scores.\n')

print('The platform with the highest average daily usage hours is TikTok. \n'
'This suggests that TikTok users may be more likely to spend more time on social media. \n'
'as it suggests that TikTok usage may be associated with higher social media usage, which is concerning with the previous conclusions.\n')

print('Overall, our analysis suggests that TikTok usage may be associated with lower sleep hours, lower mental health scores, and higher social media usage. \n'
'This is a significant finding, as it suggests that TikTok usage may have negative effects on users\' well-being.\n')

print('Next we will look at KakaoTalk and Snapchat\n')
print('KakaoTalk.\n')
#which age group uses kakao talk the most
most_used_platform_kakao = df[df['Most_Used_Platform']=='KakaoTalk']
most_used_platform_kakao_age_group = most_used_platform_kakao['Age_Group'].mode()[0]
print(f'The age group that uses KakaoTalk the most is: {most_used_platform_kakao_age_group}') 

print('Ive visited KakaoTalks website and it is a messaging app that is popular in South Korea,\n'
'which is similar to WhatsApp. \n'
'As Whatsapp is not categorized as a social media platform in this analysis, so is KakoaTalk excluded.\n') 

print('The reason why I included KakaoTalk in the analysis is because of its low mental health score and high addiction score.\n'
'This suggests that KakaoTalk users may be more likely to have lower mental health scores and higher addiction scores. \n'
'this wouldve contradict the findings of the analysis, as the daily usage hours is low and the addiction score is high.\n' 
'and the mental health score is low. \n'
'However, as KakaoTalk is a messaging app, it is not fair to compare it to other social media platforms. \n')

#Snapchat vs Tiktok
print('Comparison between Snapchat and TikTok')
snapchat_users = df[df['Most_Used_Platform'] == 'Snapchat']
tiktok_users = df[df['Most_Used_Platform'] == 'TikTok'] 
average_addiction_snapchat = snapchat_users['Addicted_Score'].mean()
average_addiction_tiktok = tiktok_users['Addicted_Score'].mean()
print(f'Average Addiction Score for Snapchat users: {average_addiction_snapchat}')
print(f'Average Addiction Score for TikTok users: {average_addiction_tiktok}\n')

#Snapchat users
most_used_platform_snapchat = df[df['Most_Used_Platform']=='Snapchat']
most_used_platform_snapchat_age_group = most_used_platform_snapchat['Age_Group'].mode()[0]
print(f'The age group that uses Snapchat the most is: {most_used_platform_snapchat_age_group}\n')

print('The average addiction score for Snapchat users is higher than the average addiction score for TikTok users. \n'
'Suggesting that Snapchat users may be more likely to be addicted to social media. \n'
'The age group that uses Snapchat the most is 0-18, while the age group that uses TikTok the most is 19-25. \n'
'Thus, younger people are more likely to use Snapchat, while older people are more likely to use TikTok. \n')
print('Overall, our analysis suggests that Snapchat usage may be associated with higher addiction scores. \n'
'This is concerning because of the effects that it might have on the users mental health.\n')

#Tiktok users 
most_used_platform_tiktok = df[df['Most_Used_Platform']=='TikTok']
most_used_platform_tiktok_age_group = most_used_platform_tiktok['Age_Group'].mode()[0]
print(f'The age group that uses TikTok the most is: {most_used_platform_tiktok_age_group}\n')
print('The age group that uses TikTok the most is 19-25, while the age group that uses Snapchat the most is 0-18. \n'
'Thus younger people are more likely to use Snapchat, while older people are more likely to use TikTok. \n'
'Different age groups use different platforms, however does the effects differ?.\n')

#correlation between time spent on social media and mental_health_score_by_platform
print('Is there a significant correlation between time spent on social media and mental health score?')
correlation_time_mental_health = df['Avg_Daily_Usage_Hours'].corr(df['Mental_Health_Score'])
print(f'Correlation between Average Daily Usage Hours and Mental Health Score: {correlation_time_mental_health}')

t_stat, p_value = stats.pearsonr(df['Avg_Daily_Usage_Hours'], df['Mental_Health_Score'])
print(f'T-test results: t-statistic = {t_stat}, p-value = {p_value}')
if p_value < 0.05:
    print('The correlation between time spent on social media and mental health score is statistically significant.\n')   
else:
    print('The correlation between time spent on social media and mental health score is not statistically significant.\n')

print('Conclusion: There is a negative correlation between time spent on social media and mental health score. \n'
'Sugessting that as time spent on social media increases, mental health score decreases. \n'
'Either, social media usage has a negative impact on mental health, \n'
'or people with poor mental health are more likely to spend more time on social media. \n'
'Social media usage can have a negative impact on mental health, even though this is widely known, it is important to keep in mind \n'
'that the landscape is big and it might be the time we spent on social media platforms tied to the methods that are utilized to keep people longer on them that might be\n'
'something to analyse and ethically question, especially for social media applications that are more prevalent in age groups under 18.\n') 

#final conclusion
print('Final Conclusion: \n'
'1. There is no significant difference in addiction score between genders. \n'
'2. There is a negative correlation between mental health score and addiction score. \n'
'3. Younger people are more likely to be addicted to social media. \n'
'4. The most addictive platforms are Snapchat, TikTok, and Instagram. \n'
'5. TikTok usage may be associated with lower sleep hours, lower mental health scores, and higher social media usage. \n'
'6. Different age groups have different platform preferences. \n'
'7. There is a negative correlation between time spent on social media and mental health score. \n')

print('Overall, our analysis suggests that social media addiction is a complex issue that is influenced by a variety of factors,\n'
'including age, platform usage, and mental health. \n'
'It is important to continue to study this issue in order to better understand the effects of social media on individuals and society as a whole.\n')



