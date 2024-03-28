import numpy as np
fuel_efficiency = np.array([25, 30, 20, 35, 28, 22, 32, 27, 24])
average_fuel_efficiency = np.mean(fuel_efficiency)
print("Average fuel efficiency:", average_fuel_efficiency)
fuel_efficiency_model1 = fuel_efficiency[0]
fuel_efficiency_model2 = fuel_efficiency[3]
percentage_improvement = ((fuel_efficiency_model2 - fuel_efficiency_model1) / fuel_efficiency_model1) * 100
print("Percentage improvement in fuel efficiency between the two car models:", percentage_improvement, "%")
