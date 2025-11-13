# %% required libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm

# %% load CDC data in trasport format (.xpt)
diet = pd.read_sas('data/DR1TOT_J.XPT')
body = pd.read_sas('data/BMX_J.XPT')
GLU_lab = pd.read_sas('data/GLU_J.XPT')
demo = pd.read_sas('data/DEMO_J.XPT')

# %%Merger all datasets using SEQN (unique participants)
df = diet.merge(body, on='SEQN', how='inner') 
df = df.merge(GLU_lab, on='SEQN', how='inner')
df = df.merge(demo[['SEQN', 'RIDAGEYR', 'RIAGENDR']], on='SEQN', how='inner')
#print("merged datasets shape:", df.shape)
#df_nan_count = df.isna().sum()
#print("Missing values per column:\n", df_nan_count)


# %% ## Data Cleaning
#selecting relevant columns
cols = ['SEQN', 'DR1TPROT', 'DR1TCARB', 'DR1TTFAT', 'BMXBMI', 'LBXGLU', 'RIDAGEYR', 'RIAGENDR']
data = df[cols].dropna()
# Renaming column for readability
data.columns = ['ID', 'Protein', 'Carbs', 'Fat', 'BMI', 'Glucose', 'Age', 'Gender']
#converting Gender code (1=Male and 2=Female)
data['Gender'] = data['Gender'].map({1: 'Male', 2: 'Female'})
#see Summary of the dataset
#print(data.describe())
#print(data.shape)
# filter extreme outliers then find low (<75) and high (>150) glucose values
low_glucose = data[data['Glucose'] < 60]
high_glucose = data[data['Glucose'] > 170]

print("Low glucose (<75) count:", len(low_glucose))
#print(low_glucose[['ID', 'Glucose', 'Age', 'Gender', 'BMI']].to_string(index=False))

print("\nHigh glucose (>150) count:", len(high_glucose))
#print(high_glucose[['ID', 'Glucose', 'Age', 'Gender', 'BMI']].to_string(index=False))

#filter extreme outliers then find low (<75) and high (>150) glucose values
low_bmi = data[data['BMI'] < 15]
high_bmi = data[data['BMI'] > 50]

print("\nLow BMI (<15) count:", len(low_bmi))
print("\nHigh BMI (>50) count:", len(high_bmi))


# %%#### Exploratory Data Analysis (EDA)

sns.pairplot(data[['Protein', 'Carbs', 'Fat', 'BMI', 'Glucose']], diag_kind='kde')
plt.show()

#correlation heatmap
corr = data[['Protein', 'Carbs', 'Fat', 'BMI', 'Glucose']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Nutrient vs Metabolic Correaltions')
plt.show()


# %% ## first task Explore relationships between nutrient intake and metabolic outcomes (e.g., fasting glucose, BMI).

