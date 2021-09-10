#!/usr/bin/env python
# coding: utf-8

# ## Data Analysis with Python: Zero to Pandas - Course Project Guidelines
# #### (remove this cell before submission)
# 
# Important links:
# - Make submissions here: https://jovian.ml/learn/data-analysis-with-python-zero-to-pandas/assignment/course-project
# - Ask questions here: https://jovian.ml/forum/t/course-project-on-exploratory-data-analysis-discuss-and-share-your-work/11684
# - Find interesting datasets here: https://jovian.ml/forum/t/recommended-datasets-for-course-project/11711
# 
# 
# This is the starter notebook for the course project for [Data Analysis with Python: Zero to Pandas](https://jovian.ml/learn/data-analysis-with-python-zero-to-pandas). You will pick a real-world dataset of your choice and apply the concepts learned in this course to perform exploratory data analysis. Use this starter notebook as an outline for your project . Focus on documentation and presentation - this Jupyter notebook will also serve as a project report, so make sure to include detailed explanations wherever possible using Markdown cells.
# 
# ### Evaluation Criteria
# 
# Your submission will be evaluated using the following criteria:
# 
# * Dataset must contain at least 3 columns and 150 rows of data
# * You must ask and answer at least 4 questions about the dataset
# * Your submission must include at least 4 visualizations (graphs)
# * Your submission must include explanations using markdown cells, apart from the code.
# * Your work must not be plagiarized i.e. copy-pasted for somewhere else.
# 
# 
# Follow this step-by-step guide to work on your project.
# 
# 
# ### Step 1: Select a real-world dataset 
# 
# - Find an interesting dataset on this page: https://www.kaggle.com/datasets?fileType=csv
# - The data should be in CSV format, and should contain at least 3 columns and 150 rows
# - Download the dataset using the [`opendatasets` Python library](https://github.com/JovianML/opendatasets#opendatasets)
# 
# Here's some sample code for downloading the [US Elections Dataset](https://www.kaggle.com/tunguz/us-elections-dataset):
# 
# ```
# import opendatasets as od
# dataset_url = 'https://www.kaggle.com/tunguz/us-elections-dataset'
# od.download('https://www.kaggle.com/tunguz/us-elections-dataset')
# ```
# 
# You can find a list of recommended datasets here: https://jovian.ml/forum/t/recommended-datasets-for-course-project/11711
# 
# ### Step 2: Perform data preparation & cleaning
# 
# - Load the dataset into a data frame using Pandas
# - Explore the number of rows & columns, ranges of values etc.
# - Handle missing, incorrect and invalid data
# - Perform any additional steps (parsing dates, creating additional columns, merging multiple dataset etc.)
# 
# 
# ### Step 3: Perform exploratory analysis & visualization
# 
# - Compute the mean, sum, range and other interesting statistics for numeric columns
# - Explore distributions of numeric columns using histograms etc.
# - Explore relationship between columns using scatter plots, bar charts etc.
# - Make a note of interesting insights from the exploratory analysis
# 
# ### Step 4: Ask & answer questions about the data
# 
# - Ask at least 4 interesting questions about your dataset
# - Answer the questions either by computing the results using Numpy/Pandas or by plotting graphs using Matplotlib/Seaborn
# - Create new columns, merge multiple dataset and perform grouping/aggregation wherever necessary
# - Wherever you're using a library function from Pandas/Numpy/Matplotlib etc. explain briefly what it does
# 
# 
# ### Step 5: Summarize your inferences & write a conclusion
# 
# - Write a summary of what you've learned from the analysis
# - Include interesting insights and graphs from previous sections
# - Share ideas for future work on the same topic using other relevant datasets
# - Share links to resources you found useful during your analysis
# 
# 
# ### Step 6: Make a submission & share your work
# 
# - Upload your notebook to your Jovian.ml profile using `jovian.commit`.
# - **Make a submission here**: https://jovian.ml/learn/data-analysis-with-python-zero-to-pandas/assignment/course-project
# - Share your work on the forum: https://jovian.ml/forum/t/course-project-on-exploratory-data-analysis-discuss-and-share-your-work/11684
# - Browse through projects shared by other participants and give feedback
# 
# 
# ### (Optional) Step 7: Write a blog post
# 
# - A blog post is a great way to present and showcase your work.  
# - Sign up on [Medium.com](https://medium.com) to write a blog post for your project.
# - Copy over the explanations from your Jupyter notebook into your blog post, and [embed code cells & outputs](https://medium.com/jovianml/share-and-embed-jupyter-notebooks-online-with-jovian-ml-df709a03064e)
# - Check out the Jovian.ml Medium publication for inspiration: https://medium.com/jovianml
# 
# 
# 
# 
# 
# ### Example Projects
# 
# Refer to these projects for inspiration:
# 
# * [Analyzing StackOverflow Developer Survey Results](https://jovian.ml/aakashns/python-eda-stackoverflow-survey)
# 
# * [Analyzing Covid-19 data using Pandas](https://jovian.ml/aakashns/python-pandas-data-analysis) 
# 
# * [Analyzing your browser history using Pandas & Seaborn](https://medium.com/free-code-camp/understanding-my-browsing-pattern-using-pandas-and-seaborn-162b97e33e51) by Kartik Godawat
# 
# * [WhatsApp Chat Data Analysis](https://jovian.ml/PrajwalPrashanth/whatsapp-chat-data-analysis) by Prajwal Prashanth
# 
# * [Understanding the Gender Divide in Data Science Roles](https://medium.com/datadriveninvestor/exploratory-data-analysis-eda-understanding-the-gender-divide-in-data-science-roles-9faa5da44f5b) by Aakanksha N S
# 
# * [2019 State of Javscript Survey Results](https://2019.stateofjs.com/demographics/)
# 
# * [2020 Stack Overflow Developer Survey Results](https://insights.stackoverflow.com/survey/2020)
# 
# 
# 
# **NOTE**: Remove this cell containing the instructions before making your submission. You can do using the "Edit > Delete Cells" menu option.

# # Project Title - change this
# 
# TODO - Write some introduction about your project here: describe the dataset, where you got it from, what you're trying to do with it, and which tools & techniques you're using. You can also mention about the course [Data Analysis with Python: Zero to Pandas](zerotopandas.com), and what you've learned from it.

# ### How to run the code
# 
# This is an executable [*Jupyter notebook*](https://jupyter.org) hosted on [Jovian.ml](https://www.jovian.ml), a platform for sharing data science projects. You can run and experiment with the code in a couple of ways: *using free online resources* (recommended) or *on your own computer*.
# 
# #### Option 1: Running using free online resources (1-click, recommended)
# 
# The easiest way to start executing this notebook is to click the "Run" button at the top of this page, and select "Run on Binder". This will run the notebook on [mybinder.org](https://mybinder.org), a free online service for running Jupyter notebooks. You can also select "Run on Colab" or "Run on Kaggle".
# 
# 
# #### Option 2: Running on your computer locally
# 
# 1. Install Conda by [following these instructions](https://conda.io/projects/conda/en/latest/user-guide/install/index.html). Add Conda binaries to your system `PATH`, so you can use the `conda` command on your terminal.
# 
# 2. Create a Conda environment and install the required libraries by running these commands on the terminal:
# 
# ```
# conda create -n zerotopandas -y python=3.8 
# conda activate zerotopandas
# pip install jovian jupyter numpy pandas matplotlib seaborn opendatasets --upgrade
# ```
# 
# 3. Press the "Clone" button above to copy the command for downloading the notebook, and run it on the terminal. This will create a new directory and download the notebook. The command will look something like this:
# 
# ```
# jovian clone notebook-owner/notebook-id
# ```
# 
# 
# 
# 4. Enter the newly created directory using `cd directory-name` and start the Jupyter notebook.
# 
# ```
# jupyter notebook
# ```
# 
# You can now access Jupyter's web interface by clicking the link that shows up on the terminal or by visiting http://localhost:8888 on your browser. Click on the notebook file (it has a `.ipynb` extension) to open it.
# 

# ## Downloading the Dataset
# 
# **TODO** - add some explanation here

# > Instructions for downloading the dataset (delete this cell)
# >
# > - Find an interesting dataset on this page: https://www.kaggle.com/datasets?fileType=csv
# > - The data should be in CSV format, and should contain at least 3 columns and 150 rows
# > - Download the dataset using the [`opendatasets` Python library](https://github.com/JovianML/opendatasets#opendatasets)

# In[1]:


get_ipython().system('pip install jovian opendatasets --upgrade --quiet')


# Let's begin by downloading the data, and listing the files within the dataset.

# In[6]:


# Change this
dataset_url = 'https://www.kaggle.com/lava18/google-play-store-apps' 


# In[7]:


import opendatasets as od
od.download(dataset_url)


# The dataset has been downloaded and extracted.

# In[8]:


# Change this
data_dir = './google-play-store-apps'


# In[9]:


import os
os.listdir(data_dir)


# Let us save and upload our work to Jovian before continuing.

# In[10]:


project_name = "Mohnish-zerotopandas-course-project-starter" # change this (use lowercase letters and hyphens only)


# In[11]:


get_ipython().system('pip install jovian --upgrade -q')


# In[12]:


import jovian


# In[ ]:


jovian.commit(project=project_name)


# ## Data Preparation and Cleaning
# 
# **TODO** - Write some explanation here.
# 
# 

# > Instructions (delete this cell):
# >
# > - Load the dataset into a data frame using Pandas
# > - Explore the number of rows & columns, ranges of values etc.
# > - Handle missing, incorrect and invalid data
# > - Perform any additional steps (parsing dates, creating additional columns, merging multiple dataset etc.)

# In[426]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

get_ipython().system('pip install plotly')

import plotly
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode,iplot
init_notebook_mode(connected=True)


# In[427]:


google_df= pd.read_csv('google-play-store-apps/googleplaystore.csv')


# In[428]:


google_df


# ### Convert installs into float type

# In[429]:


x=google_df['Installs']=='Free'
google_df[x]


# In[430]:


google_df.at[10472,'Installs']=0
google_df.at[10472,'Reviews']=3000000


# In[431]:


google_df['Installs']=google_df['Installs'].str.split('+',n=1,expand=True)
google_df['Installs']=google_df['Installs'].str.join('')
google_df['Installs']=google_df['Installs'].str.split(',')
google_df['Installs']=google_df['Installs'].str.join('')


# In[432]:


google_df['Installs']=pd.to_numeric(google_df['Installs'])


# ### Convert reviews
# 

# In[433]:


google_df.Reviews=pd.to_numeric(google_df.Reviews)


# ### Convert size
# 

# In[434]:


google_df['Size']=google_df['Size'].str.split('M')
google_df['Size']=google_df['Size'].str.join('')


# In[435]:


google_df.Size=pd.to_numeric(google_df.Size,errors='coerce')


# ### Convert Price

# In[436]:


google_df.Price=google_df.Price.str.split('$')
google_df.Price=google_df.Price.str.join('')


# In[437]:


google_df.Price=pd.to_numeric(google_df.Price,errors='coerce')


# In[438]:


google_df=google_df.rename(columns={'Price':'Price($)'})


# ## datetime

# In[439]:


count_genres=google_df['Genres'].value_counts()
count_size=google_df['Size'].value_counts()
count_rating=google_df['Rating'].value_counts()


# In[440]:


google_df['Last Updated']=pd.to_datetime(google_df['Last Updated'],errors='coerce')


# In[441]:



google_df['year_added']=google_df['Last Updated'].dt.year
google_df['month_added']=google_df['Last Updated'].dt.month


# ## Missing data

# In[442]:


google_df.dropna(how='any').shape
#missing data is very less so wwe can drop the missing values


# In[443]:


google_df.dropna(how='any',inplace=True)


# In[444]:


google_df.drop_duplicates(subset='App',keep ='first' , inplace = True)


# In[445]:


google_df.shape


# ### Free and Paid apps

# In[446]:


data_free  = google_df[google_df['Type'] == 'Free']
data_paid =  google_df[google_df['Type'] == 'Paid']


# ### Convert flaot to int

# In[447]:


google_df.Installs=google_df.Installs.apply(np.int64)


# In[448]:


google_df.Size=google_df.Size.apply(np.int64)


# In[449]:


google_df


# In[450]:


google_df.info()


# In[451]:


import jovian


# In[452]:


jovian.commit()


# ## Exploratory Analysis and Visualization
# 
# **TODO** - write some explanation here.
# 
# 

# > Instructions (delete this cell)
# > 
# > - Compute the mean, sum, range and other interesting statistics for numeric columns
# > - Explore distributions of numeric columns using histograms etc.
# > - Explore relationship between columns using scatter plots, bar charts etc.
# > - Make a note of interesting insights from the exploratory analysis

# Let's begin by importing`matplotlib.pyplot` and `seaborn`.

# In[453]:


import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

sns.set_style('darkgrid')
matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['figure.figsize'] = (25, 10)
matplotlib.rcParams['figure.facecolor'] = '#00000000'


# **TODO** - Lets see the data type , count ,means of the data

# In[454]:


google_df.info()


# In[455]:


google_df.describe()


# all values seams to be correct

# **TODO** - Lets see the Total no of riviews

# In[456]:


#as the reviews type is objecct so lets convert it into int
google_df.Reviews=google_df.Reviews.astype(int)


# In[457]:


#Total riviews are
riviews_sum = google_df.Reviews.sum()
print('Total Riviews are:{}'.format(riviews_sum))


# **TODO** - Ratings histogram

# In[458]:


plt.title('Rating')
plt.hist(google_df.Rating);


# We can see that most people rate the apps on playstore in range of 4-4.5

# **TODO** - Category

# In[459]:


top_category=google_df.Category.value_counts().reset_index()
top_category


# In[460]:


plt.xticks(rotation=75)
plt.title('Category')
sns.barplot(x=top_category['index'],y=top_category.Category);


# It can be seen that there is high proportion of "FAMILY","GAME" and "TOOLS" types of application on paly sotre.

# **TODO** - Play store Geners barplot

# In[461]:


top_geners=google_df.Genres.value_counts().reset_index().head(15)
top_geners


# In[462]:


plt.xticks(rotation=75)
plt.title('GENERS')
sns.barplot(x=top_geners['index'],y=top_geners.Genres);


# We can see that tools, entertainment and education type of apps are higly popular on playstore

# **TODO** - Lets see earnings of some paid apps

# In[463]:


data_paid['earning']= data_paid['Price($)']*data_paid['Installs']


# In[464]:


df1=data_paid.nlargest(15,['earning'])


# In[466]:


plt.xticks(rotation=75)
plots=sns.barplot(x=(df1['App']),y=df1.earning)
for bar in plots.patches:
    plots.annotate(format(bar.get_height(), '.2f'), 
                   (bar.get_x() + bar.get_width() / 2, 
                    bar.get_height()), ha='center', va='center',
                   size=15, xytext=(0, 8),
                   textcoords='offset points')


# In[467]:


data_paid_2=data_paid.Installs>=0.8e7
data_paid[data_paid_2]


# ### Hitman Sniper is a paid apps with higest installs But the earning of "I am rich	" and "I Am Rich Premium" is more.

# Let us save and upload our work to Jovian before continuing

# In[301]:


import jovian


# In[468]:


jovian.commit()


# ## Asking and Answering Questions
# 
# TODO - write some explanation here.
# 
# 

# > Instructions (delete this cell)
# >
# > - Ask at least 5 interesting questions about your dataset
# > - Answer the questions either by computing the results using Numpy/Pandas or by plotting graphs using Matplotlib/Seaborn
# > - Create new columns, merge multiple dataset and perform grouping/aggregation wherever necessary
# > - Wherever you're using a library function from Pandas/Numpy/Matplotlib etc. explain briefly what it does
# 
# 

# #### Q1: TODO - Lets see how many are free and paid users

# In[469]:


count_free=google_df['Type'].value_counts()


# In[470]:


plt.pie(count_free,labels=['Free','Paid'],autopct='%.2f');


# ## We can see that paid users are very less

# #### Q2: TODO - Does use of application increassing
# 

# In[471]:


v1=data_free['year_added'].value_counts().reset_index()
plt.plot(v1['index'],v1.year_added,'o-');

v2=data_paid['year_added'].value_counts().reset_index()
plt.plot(v2['index'],v2.year_added,'o-');

plt.title('New or updated application over a years:',size=30)
plt.legend(['Free','Paid'])


# Resently of free applications has more updations then paid applications

# #### Q3: TODO - What type of content is preffered

# In[472]:


v1=data_free['Content Rating'].value_counts().reset_index()
v1
v2=data_paid['Content Rating'].value_counts().reset_index()
#v2=v2.rename(columns={'index':'index1','Content Rating':'Content Rating1'})
v2
combined=pd.concat([v1,v2],axis=0)
combined

#sns.scatterplot(combined['index'],combined['Content Rating'])
plt.plot(v1['index'],v1['Content Rating'],'o-')
plt.plot(v2['index'],v2['Content Rating'],'o-');

plt.legend(['Free','Paid'])


# #### Q4: TODO - What type of data do users prefer in free applications
# 

# In[473]:


v1=data_free['Content Rating'].value_counts().reset_index()


# In[474]:


sns.barplot(v1['index'],v1['Content Rating']);


# #### Q5: TODO - Rating of Free and Paid apps

# In[475]:


v1=data_free['Rating'].value_counts().reset_index()
v1=v1.sort_values('index')
v2=data_paid['Rating'].value_counts().reset_index()
v2=v2.sort_values('index')

plt.title('Rating of free and paid apps')


plt.plot(v1['index'],v1['Rating'])
plt.plot(v2['index'],v2['Rating'])

plt.legend(['Free','Paid']);


# #### Q6: TODO - App Category

# In[476]:


v1=data_free['Category'].value_counts().reset_index()
v1=v1.sort_values('index')

v2=data_paid['Category'].value_counts().reset_index()
v2=v2.sort_values('index')

t1=go.Scatter(x=v1['index'],y=v1['Category'],name='free')
t2=go.Scatter(x=v2['index'],y=v2['Category'],name='paid')
y=[t1,t2]
fig=go.Figure(data=y,layout={'title':'App Category','xaxis':{'title':'All Category'}})
iplot(fig)


("")


# 

# Let us save and upload our work to Jovian before continuing.

# In[477]:


import jovian


# In[478]:


jovian.commit()


# ## Inferences and Conclusion
# 
# **TODO** - family Content which is available for everyone and is free for users has seen to be get high ratings and more reviews

# In[479]:


import jovian


# In[480]:


jovian.commit()


# ## References and Future Work
# 
# **TODO** - we can check if ratings depends months or updatation per year or months

# In[ ]:


import jovian


# In[ ]:


jovian.commit()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




