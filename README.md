# Social media addiction analysis
My final project for SHARE Academy  

__Project Description__

In this digital age, students are increasingly exposed to social media, which can have both positive and negative impacts on mental well-being. This project analyzes usage patterns across platforms such as Instagram, TikTok, Snapchat, Facebook, and X (formerly Twitter), and investigates how these patterns relate to self-reported mental health scores.

The primary goal of this analysis is to identify which social media platforms may negatively influence the mental health of students aged 18 to 24. The dataset was sourced from Kaggle, and the analysis was conducted using Python for data cleaning and statistical modeling. Visualizations of the results are available on a Tableau Public dashboard, providing clear and interactive representations of key findings.

__Research Question__
How does social media platforms affect the mental health scores of students?

To answer this question we will zoom into 3 factors: Gender, Age and Platform. 
Question 1 : Is there a correlation between gender and mental health score?
Question 2 : Which age group have a higher addicted score?
Question 3 : Which Platforms have the highest addicted score and average usage?
Question 4 : Is there a correlation between time spent on platforms and mental health scores?

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
- **`Avg_Daily_Usage_Hours`** – Average hours spent on social media per day  
- **`Most_Used_Platform`** – Primary social media platform used by the student  
- **`Sleep_Hours_Per_Night`** – Average hours of sleep per night  
- **`Mental_Health_Score`** – Self-reported mental health score  
- **`Addicted_Score`** – A score estimating social media addiction level  

These variables were selected because they are most relevant for exploring correlations between **social media usage** and **student mental health**.


__Data Contact__


* **Stacy Alves <stacy.alves21@gmail.com>** - Contact for inqueries regarding data.
* **Kagle -  [(https://www.kaggle.com/datasets/adilshamim8/social-media-addiction-vs-relationships)](url)


## Getting Started

__Tools & Technologies__

<li> Python: Core programming language

<li> Pandas / NumPy: Data wrangling

<li> Matplotlib / Seaborn: Data visualization

<li> Tableau Public : Data Visualization </li>


### Requirements

Clone Repository to Local 

```
git clone https://github.com/stacyA21/social-media-mental-health.git
cd social-media-mental-health
```

Create and Activate Python Virtual Environment 

```
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

```

Create and Activate Python Virtual Environment 

```
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

```

Download necessary libraries and packages

```
pip install -r requirements.txt
````

## Results

1. There is no significant difference in addiction score between genders. 
2. There is a negative correlation between mental health score and addiction score. 
3. Younger people are more likely to be addicted to social media.
4. The most addictive platforms are Snapchat, TikTok, and Instagram. 
5. TikTok usage may be associated with lower sleep hours, lower mental health scores, and higher social media usage.
6. Different age groups have different platform preferences. 
7. There is a negative correlation between time spent on social media and mental health score.

## Reflection

Further analysis would be more insightful over the methods used on these platform to retain users. What is also interested is how WhatsApp and KaKao stand in such analysis and if these also have a negative effect. 

## Authors

List all authors, their contributions, and how to contact; Preferably an internal and external form of contact.

* **Stacy Alves** - [StacyA](https://github.com/stacyA21); stacy.alves21@gmail.com

