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

#distribution
sns.histplot(df['Age'], kde=True, bins=25, color='blue', edgecolor='black')
plt.title('Distribution of Age in Social Media Addiction Dataset')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()
plt.close()

print('Distribution of Age in Social Media Addiction Dataset')
#average age of the participants
average_age = df['Age'].mean()
print(f'Average Age of participants: {average_age}')

#which age group have a higher addicted score
print('Which age group have a higher addicted score?')
average_addiction_by_age = df.groupby('Age')['Addicted_Score'].mean().reset_index()
print('Average Addiction Score by Age:')
order_addicytion_by_age = average_addiction_by_age.sort_values(by='Addicted_Score', ascending=False)
print(order_addicytion_by_age.head(5))

#add amount of participants in each age group
age_group_counts = df['Age'].value_counts().reset_index()
age_group_counts.columns = ['Age', 'Count']
average_addiction_by_age = average_addiction_by_age.merge(age_group_counts, on='Age')
print('Average Addiction Score by Age with Participant Counts:')
print(average_addiction_by_age.sort_values(by='Addicted_Score', ascending=False).head(5))   

#plot the average addiction score by age
sns.lineplot(x='Age', y='Addicted_Score', data=average_addiction_by_age)
plt.title('Average Addiction Score by Age') 
plt.xlabel('Age')
plt.ylabel('Average Addiction Score')
plt.show()
plt.close()

print('Eventhough the age group 16-19 have the highest average addiction score, \n'
      'it is important to note that not all age groups have the same amount of participants. \n'
        'Thus, the results might be skewed by the amount of participants in each age group.\n')

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
  

print('The average addiction score for Snapchat users is higher than the average addiction score for TikTok users. \n'
'Suggesting that Snapchat users may be more likely to be addicted to social media. \n')
print('However, there are only 8 Snapchat users in the dataset, \n'
'which is a very small sample size compared to the 70 TikTok users. \n'
'Thus, the results may be skewed by the small sample size of Snapchat users. \n')

print('Overall, our analysis suggests that Snapchat usage may be associated with higher addiction scores. \n'
'This is concerning because of the effects that it might have on the users mental health.\n')

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
'something to analyse and ethically question, especially for social media applications that are more prevalent in younger age groups.\n') 

#effects of social media and academic performance

#change string yes/no to 1/0
df['Affects_Academic_Performance'] = df['Affects_Academic_Performance'].map({'Yes': 1, 'No': 0})

print('Effects of Social Media and Affects Academic Performance')
correlation_academic_performance = df['Affects_Academic_Performance'].corr(df['Addicted_Score'])
print(f'Correlation between Affects_Academic_Performance and Addicted_Score: {correlation_academic_performance}')
t_stat, p_value = stats.pearsonr(df['Affects_Academic_Performance'], df['Addicted_Score'])
print(f'T-test results: t-statistic = {t_stat}, p-value = {p_value}')
if p_value < 0.05:
    print('The correlation between Affects_Academic_Performance and Addicted_Score is statistically significant.\n')
else:
    print('The correlation between Affects_Academic_Performance and Addicted_Score is not statistically significant.\n')   
print('Conclusion: There is a positive correlation between Affects_Academic_Performance and Addicted_Score. \n'
'Suggesting that as addiction score increases, the negative effects on academic performance also increase. \n'
'Thus, social media addiction can have a negative impact on academic performance.\n') 

#how many tiktok users are there in the dataset
tiktok_users_count = df[df['Most_Used_Platform'] == 'TikTok'].shape[0]
print(f'Number of TikTok users in the dataset: {tiktok_users_count}')

#how many snapchat users are there in the dataset
snapchat_users_count = df[df['Most_Used_Platform'] == 'Snapchat'].shape[0]
print(f'Number of Snapchat users in the dataset: {snapchat_users_count}')   


#final conclusion
print('Final Conclusion: \n'
'1. There is no significant difference in addiction score between genders. \n'
'2. There is a negative correlation between mental health score and addiction score. \n'
'3. The most addictive platforms are Snapchat, TikTok, and Instagram. \n'
'4. TikTok usage may be associated with lower sleep hours, lower mental health scores, and higher social media usage. \n'
'5. There is a negative correlation between time spent on social media and mental health score. \n')
'6. There is a positive correlation between the affects on academic performance and addiction scores.\n'

print('Overall, our analysis suggests that social media addiction is a complex issue that is influenced by a variety of factors,\n'
'including age, platform usage, and mental health. \n'
'It is important to continue to study this issue in order to better understand the effects of social media on individuals and society as a whole.\n')

