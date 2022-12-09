# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 00:24:05 2022

@author: Akshit
"""

x = input("Enter Your Symptoms1: ".lower())
y = input("Enter Your Symptoms2: ".lower())
z = input("Enter Your Symptoms3: ".lower())
# Symptoms
cadsym = ['chest pain' , 'body pain' , 'falling sick' , 'feeling faint' , 'shortness of breath']
vhdsym = ['swollen ankles' , 'fanting' , 'shortness of breath']
hasym = ['racing heartbeat', 'slow heartbeat', 'chest pain' , 'anxiety', 'sweating']
mhasym = ['cold sweat', 'heartburn', 'sudden dizziness', 'discomfort in joints']
jsym = ['itching', 'abdominal pain', 'weight loss', 'yellow eyes' , 'yellow nails', 'vomiting']
cpsym = ['rashes on skin' , 'fever' , 'sore throat' , 'brown spots' , 'itching']
msym = ['fever', 'runny nose','sneezing','pink eye', 'skin rash','diarrhoea']
dsym = ['Eye pain',' fever',' muscle pain',' nausea',' joint pain',' rash on thigh']
masym = ['pain in muscle','pain in abdomin',' Night sweat',' shivering', 'fast heart rate','mental confusion']
tcsym = ['chest pain','Night sweats','shortness of breath','blood cough']
disym = ['increase thirst','frequent urination','hunger','blurred vision','slow healing']
pnsym = ['fever','chills','sharp pain in chest','clammy skin']
htsym = ['nose bleeds','dizziness','morning headaches','irregular heart rhythms','vision changes','buzzing in the ears']
emsym = ['lot of mucus','tight chest','whistle sound while breathing']
cysym = ['bluish colour in sikn',' lips','nail beds']
hysym = ['itchy','red and watery eyes','rod of mouth being itchy','runny or blocked nose']
ansym = ['unusual headache','memory loss','slurred speech','forgotten words','trouble in walking','trouble in moving arms','trouble in moving legs']
hcsym = ['anxiety','shortness of breath','headache','daytime sleep even after sleeping a lot at night','daytime sluggishness']
bcsym = ['sleeping difficulty','sore throat','chest pressure','shortness of breath','runny nose']
asym = ['wheezing','anxiety','early awakening','shortness of breath at night','cough','throat irritation']

if x and y and z in cadsym:
    print("You Might Have Coronary Artery Disease")
    
    
if x and y and z in vhdsym:
    print("You Might Have Vulvar Heart Disease")
   
if x and y and z in hasym:
    print("You Might Have Heart Arrhythmia ")
   
if x and y and z in mhasym:
    print("You Might Have Minor Heart Attack")
    
if x and y and z in jsym:
    print("You Might Have Jaundice")
     
if x and y and z in cpsym:
    print("You Might Have Chickenpox")
   
if x and y and z in msym:
    print("You Might Have Measles")
    
if x and y and z in dsym:
    print("You Might Have Dengue")
    
if x and y and z in masym:
    print("You Might Have Malaria")
    
if x and y and z in tcsym:
    print("You Might Have Tuberculosis")
    
if x and y and z in disym:
    print("You Might Have Diabetes")
    
if x and y and z in pnsym:
    print("You Might Have Pneumonia")
    
if x and y and z in htsym:
    print("You Might Have Hypertension")
    
if x and y and z in emsym:
    print("You Might Have Emphysema")
    
if x and y and z in cysym:
    print("You Might Have Cyanosis")
    
if x and y and z in hysym:
    print("You Might Have Hay Fever")
    
if x and y and z in ansym:
    print("You Might Have Anoxia")
    
if x and y and z in hcsym:
    print("You Might Have Hypercapnia")
    
if x and y and z in bcsym:
    print("You Might Have Bronchitis")
    
if x and y and z in asym:
    print("You Might Have Asthama")   

if x and y and z not in cadsym or vhdsym or hasym or mhasym or jsym or cpsym or msym or dsym or masym or tcsym or disym or pnsym or htsym or emsym or cysym or hysym or ansym or hcsym or bcsym or asym:
    print("Retry!")
