disease_data = {
    'DISEASE_NAME': ['Common Cold', 'Diabetes', 'Bronchitis', 'Influenza', 'Kidney Stones'],
    'DIAGNOSED_PATIENTS': [320, 120, 100, 150, 60]
}
disease_distribution = {}
for disease, patients in zip(disease_data['DISEASE_NAME'], disease_data['DIAGNOSED_PATIENTS']):
    disease_distribution[patients] = disease
most_common_patients = max(disease_distribution.keys())
most_common_disease = disease_distribution[most_common_patients]
print("The most common disease is:", most_common_disease, "with", most_common_patients, "diagnosed patients.")
