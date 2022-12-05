x = input("Enter Your Symptoms: ".lower())

# Symptoms
cadsym = ['chest pain' , 'body pain' , 'falling sick' , 'feeling faint' , 'shortness of breath']
vhdsym = ['swollen ankles' , 'fanting' , 'shortness of breath']
hasym = ['racing heartbeat', 'slow heartbeat', 'chest pain' , 'anxiety', 'sweating']
mhasym = ['cold sweat', 'heartburn', 'sudden dizziness', 'discomfort in joints']
jsym = ['itching', 'abdominal pain', 'weight loss', 'yellow eyes' , 'yellow nails', 'vomiting']
cpsym = ['rashes on skin' , 'fever' , 'sore throat' , 'brown spots' , 'itching']
msym = ['fever',' runny nose','sneezing','pink eye',' skin rash','diarrhoea']
dsym = ['Eye pain',' fever',' muscle pain',' nausea',' joint pain',' rash on thigh']
masym = ['pain in muscle','pain in abdomin',' Night sweat',' shivering',' fast heart rate',' mental confusion']
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

if x in cadsym:
    print("You Might Have Coronary Artery Disease")
elif x in vhdsym:
    print("You Might Have Vulvar Heart Disease")
elif x in hasym:
    print("You Might Have Heart Arrhythmia ")
elif x in mhasym:
    print("You Might Have Minor Heart Attack")
elif x in jsym:
    print("You Might Have Jaundice")    
elif x in cpsym:
    print("You Might Have Chickenpox")
elif x in msym:
    print("You Might Have Measles")
elif x in dsym:
    print("You Might Have Dengue")
elif x in masym:
    print("You Might Have Malaria")
elif x in tcsym:
    print("You Might Have Tuberculosis")
elif x in disym:
    print("You Might Have Diabetes")
elif x in pnsym:
    print("You Might Have Pneumonia")
elif x in htsym:
    print("You Might Have Hypertension")
elif x in emsym:
    print("You Might Have Emphysema")
elif x in cysym:
    print("You Might Have Cyanosis")
elif x in hysym:
    print("You Might Have Hay Fever")
elif x in ansym:
    print("You Might Have Anoxia")
elif x in hcsym:
    print("You Might Have Hypercapnia")
elif x in bcsym:
    print("You Might Have Bronchitis")
elif x in asym:
    print("You Might Have Asthama")   
else:
    print("Not Registered")