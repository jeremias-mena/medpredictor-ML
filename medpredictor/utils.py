class Utils:
    values_age_order = ['18 to 24','25 to 29', '30 to 34', '35 to 39',
                '40 to 44', '45 to 49', '50 to 54', '55 to 59',
                '60 to 64', '65 to 69', '70 to 74', '75 to 79', '80 or older']

    values_income_order = ['Less than $10,000', 
                '$10k to less than $15k', 
                '$15k to less than $20k', 
                '$20k to less than $25k',
                '$25k to less than $35k', 
                '$35k to less than $50k', 
                '$50k to less than $75k', 
                '$75,000 or more']
    
    values_education_order = ['Never attended school or only kindergarten',
                   'Elementary',
                   'Some high school',
                   'High school graduate', 
                   'Some college or technical school',
                   'College graduate']
    
    values_sex_order = ["Female", "Male"]

    values_eh_order = ["Eats fruits and vegetables", 
                   "Only eats fruits", 
                   "Only eats vegetables", 
                   "Does not eat fruits neither vegetables"]

    values_bh_order = ["Uses alcohol and tobacco", 
                   "Only consumes alcohol", 
                   "Only uses tobacco", 
                   "Does not use alcohol neither tobacco"]

    values_status_order = ['Excellent',
                'Very good',
                'Good',
                'Fair',
                'Poor']

    dict_colors_status = {'Excellent':'#1976D2',
               'Very good':'#388E3C',
               'Good':'#FBC02D',
               'Fair': '#F57C00',
               'Poor': '#D32F2F'}

    answer_filter_order = ['Yes', 'No']

    values_diabetes_order = ['No diabetes',
                         'Prediabetes',
                         'Diabetes']

    values_age_range_order = ['Young',
                          'Young adulthood',
                          'Middle adulthood',
                          'Late adulthood',
                          'Old age']
     
    def __init__(self):
        pass

    """
    This methods calculate percentajes
    """
    def calc_percentajes(self, value, total):
        return ( value * 100 ) / total if (total > 0) else 0
    
    
    """
    This method labels person's eating habits having regard his/her survey's answers
    Parameters
    value f = answer to the question Consume Fruit 1 or more times per day
    value v = answer to the question Consume Vegetables 1 or more times per day
    """
    def good_habits_labeling(self, value_f, value_v):
        if (value_f == 'Yes') & (value_v == 'Yes'):
            return 'Eats fruits and vegetables'
        elif (value_f == 'Yes') & (value_v == 'No'):
            return 'Only eats fruits'
        elif (value_f == 'No') & (value_v == 'Yes'):
            return 'Only eats vegetables'
        else:
            return 'Does not eat fruits neither vegetables'

    """
    This method labels person's bad habits such as consume alcohol or tobacco having regard his/her survey's answers
    Parameters
    value a = answer to the question Do you have X drinks per week? (adult men >= 14 drinks per week and adult women >= 7 drinks per week)
    value t = answer to the question Have you smoked at least 100 cigarettes in your entire life? 
    """    
    def bad_habits_labeling(self, value_a, value_t):
        if (value_a == 'Yes') & (value_t == 'Yes'):
            return 'Uses alcohol and tobacco'
        elif (value_a == 'Yes') & (value_t == 'No'):
            return 'Only consumes alcohol'
        elif (value_a == 'No') & (value_t == 'Yes'):
            return 'Only uses tobacco'
        else:
            return 'Does not use alcohol neither tobacco'

    """
    This method assigns a label taking into account the age range of the person.
    Parameters
    answer = person's age is between x and y.
    """    
    def age_range_labeling(self, answer):
        if answer in ['18 to 24']:
            return 'Young'
        elif answer in ['25 to 29', '30 to 34', '35 to 39']:
            return 'Young adulthood'
        elif answer in ['40 to 44', '45 to 49']:
            return 'Middle adulthood'
        elif answer in ['50 to 54', '55 to 59']:
            return 'Late adulthood'
        else:
            return 'Old age'