from tkinter import *
win = Tk()
win.title("Disease Diagnosis")
win.geometry("600x500")
#win.resizable(0,0)
win.config(bg="Light Blue")

all_diseases = {
    "Coronary Artery Disease": {'chest pain', 'body pain', 'falling sick', 'feeling faint', 'shortness of breath'}  ,
    "Vulvar Heart Disease": {'swollen ankles', 'fanting', 'shortness of breath'},
    "Heart Arrhythmia": {'racing heartbeat', 'slow heartbeat', 'chest pain', 'anxiety', 'sweating'},
    "Minor Heart Attack": {'cold sweat', 'heartburn', 'sudden dizziness', 'discomfort in joints'},
    "Jaundice": {'itching', 'abdominal pain', 'weight loss', 'yellow eyes' , 'yellow nails', 'vomiting'},
    "Chickenpox": {'rashes on skin', 'fever', 'sore throat', 'brown spots', 'itching'},
    "Measles": {'fever', 'runny nose', 'sneezing', 'pink eye', 'skin rash', 'diarrhoea'},
    "Dengue" : {'eye pain', 'fever', 'muscle pain', 'nausea', 'joint pain', 'rash on thigh'},
    "Malaria": {'pain in muscle', 'pain in abdomin', 'night sweat', 'shivering', 'fast heart rate', 'mental confusion'},
    "Tuberculosis": {'chest pain', 'night sweats', 'shortness of breath', 'blood cough'},
    "Diabetes": {'increase thirst', 'frequent urination', 'hunger', 'blurred vision', 'slow healing'},
    "Pneumonia": {'fever', 'chills', 'sharp pain in chest', 'clammy skin'},
    "Hypertension": {'nose bleeds', 'dizziness', 'morning headaches', 'irregular heart rhythms', 'vision changes', 'buzzing in the ears'},
    "Emphysema": {'lot of mucus', 'tight chest', 'whistle sound while breathing'},
    "Cyanosis": {'bluish colour in sikn', 'lips', 'nail beds'},
    "Hay Fever": {'itchy','red and watery eyes','rod of mouth being itchy','runny or blocked nose'},
    "Anoxia": {'unusual headache', 'memory loss', 'slurred speech', 'forgotten words', 'trouble in walking', 'trouble in moving arms', 'trouble in moving legs'},
    "Hypercapnia": {'anxiety', 'shortness of breath', 'headache', 'daytime sleep even after sleeping a lot at night', 'daytime sluggishness'},
    "Bronchitis": {'sleeping difficulty', 'sore throat', 'chest pressure', 'shortness of breath', 'runny nose'},
    "Asthama": {'wheezing', 'anxiety', 'early awakening', 'shortness of breath at night', 'cough', 'throat irritation'},    
}

def submit():
    sym1 = ent1.get().lower()
    Label(win, text = sym1).pack()
    sym2 = ent2.get().lower()
    Label(win, text = sym2).pack()
    sym3 = ent3.get().lower()
    Label(win, text = sym3).pack()
    sym4 = ent4.get().lower()
    
    #
    Score = (get_disease_scores(experienced_symptoms, all_diseases))
    Label(win, text= Score).pack()
    
    Label(win, text = sym4).pack()
Label(win,bg="Light Blue").pack()
Label(win,text = "DISEASE DIAGNOSIS", font=('Consolas bold', 30),bg="Light Blue").pack()
Label(win,bg="Light Blue").pack()

symp1 = Label(win,text = "Enter Symptom 1", font=('Consolas', 10),bg="Light Blue").pack()
ent1 = Entry(win)
ent1.pack()
symp2 = Label(win,text = "Enter Symptom 2", font=('Consolas', 10),bg="Light Blue").pack()
ent2 = Entry(win)
ent2.pack()
symp3 = Label(win,text = "Enter Symptom 3", font=('Consolas', 10),bg="Light Blue").pack()
ent3 = Entry(win)
ent3.pack()
symp4 = Label(win,text = "Enter Symptom 4", font=('Consolas', 10),bg="Light Blue").pack()   
ent4 = Entry(win)
ent4.pack() 

Label(win,bg="Light Blue").pack()
Button(win,text = "     Submit     ",command = submit,bg="Light Blue",bd=3,font=('Consolas bold', 10)).pack()
Label(win,bg="Light Blue").pack()

experienced_symptoms = {ent1.get(), ent2.get(), ent3.get(), ent4.get()}

def get_disease_scores(
    symptoms: set[str], diseases: dict[str, set[str]]) -> dict[str, float]:
    scores = {}

    # Iterate over all diseases with their symptoms
    for disease, disease_symptoms in diseases.items():
        # Get the symptoms common to the disease and experienced ones
        common_symptoms = symptoms.intersection(disease_symptoms)
        # Calculate and keep track of score
        scores[disease] =  len(common_symptoms) / len(disease_symptoms)

    return scores

win.mainloop()
