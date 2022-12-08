all_diseases = {
    "Coronary Artery Disease": {
        'chest pain', 'body pain', 'falling sick', 'feeling faint',
        'shortness of breath'
    },
    "Vulvar Heart Disease":
    {'swollen ankles', 'fanting', 'shortness of breath'},
    "Heart Arrhythmia": {
        'racing heartbeat', 'slow heartbeat', 'chest pain', 'anxiety',
        'sweating'
    },
    "Minor Heart Attack":
    {'cold sweat', 'heartburn', 'sudden dizziness', 'discomfort in joints'},
    "Jaundice": {
        'itching', 'abdominal pain', 'weight loss', 'yellow eyes',
        'yellow nails', 'vomiting'
    },
    "Chickenpox":
    {'rashes on skin', 'fever', 'sore throat', 'brown spots', 'itching'},
    "Measles":
    {'fever', 'runny nose', 'sneezing', 'pink eye', 'skin rash', 'diarrhoea'},
    "Dengue": {
        'Eye pain', ' fever', ' muscle pain', ' nausea', ' joint pain',
        ' rash on thigh'
    },
    "Malaria": {
        'pain in muscle', 'pain in abdomin', 'night sweat', 'shivering',
        'fast heart rate', 'mental confusion'
    },
    "Tuberculosis":
    {'chest pain', 'Night sweats', 'shortness of breath', 'blood cough'},
    "Diabetes": {
        'increase thirst', 'frequent urination', 'hunger', 'blurred vision',
        'slow healing'
    },
    "Pneumonia": {'fever', 'chills', 'sharp pain in chest', 'clammy skin'},
    "Hypertension": {
        'nose bleeds', 'dizziness', 'morning headaches',
        'irregular heart rhythms', 'vision changes', 'buzzing in the ears'
    },
    "Emphysema":
    {'lot of mucus', 'tight chest', 'whistle sound while breathing'},
    "Cyanosis": {'bluish colour in sikn', 'lips', 'nail beds'},
    "Hay Fever": {
        'itchy', 'red and watery eyes', 'rod of mouth being itchy',
        'runny or blocked nose'
    },
    "Anoxia": {
        'unusual headache', 'memory loss', 'slurred speech', 'forgotten words',
        'trouble in walking', 'trouble in moving arms',
        'trouble in moving legs'
    },
    "Hypercapnia": {
        'anxiety', 'shortness of breath', 'headache',
        'daytime sleep even after sleeping a lot at night',
        'daytime sluggishness'
    },
    "Bronchitis": {
        'sleeping difficulty', 'sore throat', 'chest pressure',
        'shortness of breath', 'runny nose'
    },
    "Asthama": {
        'wheezing', 'anxiety', 'early awakening',
        'shortness of breath at night', 'cough', 'throat irritation'
    },
}

# sympa = input("Enter symptom a : ")
# sympb = input("Enter symptom b : ")
# sympc = input("Enter symptom c : ")
# sympd = input("Enter symptom d : ")
# experienced_symptoms = {sympa, sympb, sympc, sympd}

# def get_disease_scores(symptoms: set[str],
#                        diseases: dict[str, set[str]]) -> dict[str, float]:
#     scores = {}

#     # Iterate over all diseases with their symptoms
#     for disease, disease_symptoms in diseases.items():
#         # Get the symptoms common to the disease and experienced ones
#         common_symptoms = symptoms.intersection(disease_symptoms)
#         # Calculate and keep track of score
#         scores[disease] = len(common_symptoms) / len(disease_symptoms)

#     return scores

# print(get_disease_scores(experienced_symptoms, all_diseases))


def get_disease(symptoms, diseases):
    for disease, disease_symptoms in diseases.items():
        if (symptoms == disease_symptoms):
            print("You Might Have ", disease)
            return

    print("Not Registered")


symptoms = set(
    map(str,
        input("Enter symptoms seperated by commas :\n").strip().split(",")))
symptoms = {item.strip() for item in symptoms}
print(symptoms)
get_disease(symptoms, all_diseases)