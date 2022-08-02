import numpy as np
from matplotlib import pyplot as plt

survey_responses = ['Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos','Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos']

total_ceballos=sum([1 for n in survey_responses if n=="Ceballos"])
print total_ceballos
# number of responses
ln=float(len(survey_responses))
# % for Ceballos
percentage_ceballos=total_ceballos/ln
print percentage_ceballos

# predicted value (predicated on the prior poll)
possible_surveys=np.random.binomial(ln, 0.54,size=10000)/ln # probability of getting 54% voted

possible_surveys_length=float(len(possible_surveys))
incorrect_predictions=len(possible_surveys[possible_surveys<0.5])

# The percentage the potential votes
ceballos_loss_surveys=incorrect_predictions/possible_surveys_length
print ceballos_loss_surveys

large_survey=np.random.binomial(float(7000),0.54,size=10000)/float(7000)

plt.close()
plt.hist(possible_surveys,range=(0,1),bins=20)
plt.hist(large_survey, alpha=0.5,range=(0,1),bins=20)
plt.show()

incorrect_predictions_large=len(large_survey[large_survey<0.5])
large_survey_length=float(len(large_survey))
ceballos_loss_new=incorrect_predictions_large/large_survey_length

print ceballos_loss_new
