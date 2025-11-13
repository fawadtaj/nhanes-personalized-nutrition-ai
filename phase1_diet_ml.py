# required libraries
import pandas as pd

#load CDC data in trasport format (.xpt)
diet = pd.read_sas('data/DR1TOT_J.XPT')
body = pd.read_sas('data/BMX_J.XPT')
GLU_lab = pd.read_sas('data/GLU_J.XPT')
demo = pd.read_sas('data/DEMO_J.XPT')

#Merger all datasets using SEQN (unique participants)
df = diet.merge(body, on='SEQN', how='inner') 
df = df.merge(GLU_lab, on='SEQN', how='inner')
df = df.merge(demo[['SEQN', 'RIDAGEYR', 'RIAGENDR']], on='SEQN', how='inner')
print("merged datasets shape:", df.shape)


print(df.columns.tolist()[:15]) 