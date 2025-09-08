# Mind Over Media 
## Analyzing Social Media’s Effects on Mental Health

My final project for SHARE Academy  

__Summary__

This project analyzes how social media usage across social media platforms relates to the mental health of students aged 18 to 24. Using a Kaggle dataset, Python for data analysis, and Tableau for visualization, the study highlights potential correlations between platform usage and self-reported well-being.

__Project Description__

In today’s digital age, social media plays a central role in students’ daily lives, shaping both positive and negative aspects of mental well-being. This project explores usage patterns across major platforms and examines their relationship to self-reported mental health scores.

The primary aim is to identify potential correlations between platform usage and mental health among students aged 18 to 24. 
While mental health is a complex and multifaceted issue, this analysis seeks to uncover trends and insights that may highlight platforms with greater negative impacts.

The dataset was sourced from Kaggle, and the analysis was performed using Python for data cleaning, statistical modeling, and exploration. Results are visualized through an interactive Tableau Public dashboard, providing clear and accessible insights into the findings.

__Research Question__

Main question:
How does social media platforms affect the mental health scores of students?

To answer this question we will zoom into 3 factors: Gender, Age and Platform. 
- Question 1 : To what extent is gender associated with differences in mental health scores?
- Question 2 : Which age group demonstrates the highest levels of social media addiction?
- Question 3 : Which platforms are most strongly linked to higher addiction scores and greater average usage?
- Question 4 : How strongly is time spent on social media correlated with mental health scores?

## Data Insight

The dataset consists of student responses and includes the following columns:

- `Student_ID`  
- `Age`  
- `Gender`  
- `Academic_Level`  
- `Country`  
- `Avg_Daily_Usage_Hours`  
- `Most_Used_Platform`  
- `Affects_Academic_Performance`  
- `Sleep_Hours_Per_Night`  
- `Mental_Health_Score`  
- `Relationship_Status`  
- `Conflicts_Over_Social_Media`  
- `Addicted_Score`  

### Columns Used in This Analysis

For this project, the following columns are the focus:

- **`Student_ID`** – Unique identifier for each participant  
- **`Age`** – Age of the student
- **`Gender`** - self-reported gender, recorded as “Male” or “Female” to allow for demographic breakdowns in usage and outcome measures
- **`Avg_Daily_Usage_Hours`** – Average hours spent on social media per day  
- **`Most_Used_Platform`** – Primary social media platform used by the student  
- **`Sleep_Hours_Per_Night`** – Average hours of sleep per night  
- **`Mental_Health_Score`** – Self-reported mental health score  
- **`Addicted_Score`** – A composite score from 1 (low addiction) to 10 (high addiction) based on a standardized survey scale (e.g., Bergen Social Media Addiction Scale), quantifying the degree of problematic usage.
- **`Affects_Academic_Performance`** - A binary indicator (“Yes”/“No”) reflecting whether the student perceives their social media use as having a negative impact on their academic performance.


__Data Contact__


* **Stacy Alves <stacy.alves21@gmail.com>** - Contact for inqueries regarding data.
* **Kagle -  [(https://www.kaggle.com/datasets/adilshamim8/social-media-addiction-vs-relationships)](url)


## Getting Started

__Tools & Technologies__

<li> Python: Core programming language

<li> Pandas / NumPy: Data wrangling

<li> Matplotlib / Seaborn: Data visualization

<li> Tableau Public : Data Visualization </li>


### Set Up Instructions

Clone Repository to Local 

```
git clone https://github.com/stacyA21/social-media-mental-health.git
cd social-media-mental-health
```

Create and Activate Python Virtual Environment 

```
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

Download necessary libraries and packages

```
pip install -r requirements.txt
```
## Tableau Dashboard  
Explore the interactive visualizations here: [View on Tableau Public](https://public.tableau.com/views/socialmediaaddiction_17573283795910/Dashboard1?:language=en-GB&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

## Results

- 1. There is no significant difference in addiction score between genders. 
- 2. There is a negative correlation between mental health score and addiction score. 
- 3. The most addictive platforms are Snapchat, TikTok, and Instagram. 
- 4. TikTok usage may be associated with lower sleep hours, lower mental health scores, and higher social media usage.
- 5. There is a negative correlation between time spent on social media and mental health score.
- 6. There is a positive correlation between the affects on academic performance and addiction scores.
- 7. There is a positive correlation between daily usage and affect on academic performance.


## Reflection

Further analysis would be more insightful over the methods used on these platform to retain users. What is also interested is how WhatsApp and KaKao stand in such analysis and if these also have a negative effect. 

## Authors

* **Stacy Alves** - [StacyA](https://github.com/stacyA21); stacy.alves21@gmail.com

