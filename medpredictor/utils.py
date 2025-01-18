class Utils:
    
    def __init__(self):
        pass

    def calc_percentajes(self, value, total):
        return (value*100)/total if (total > 0) else 0
    
    
    """
    This method labels person's eating habits having regard his/her survey's answers
    Parameters
    value f = answer to the question Consume Fruit 1 or more times per day
    value v = answer to the question Consume Vegetables 1 or more times per day
    """
    def good_habits_labeling(value_f, value_v):
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
    def bad_habits_labeling(value_a, value_t):
        if (value_a == 'Yes') & (value_t == 'Yes'):
            return 'Consume alcohol and tobacco'
        elif (value_a == 'Yes') & (value_t == 'No'):
            return 'Only consume alcohol'
        elif (value_a == 'No') & (value_t == 'Yes'):
            return 'Only consume tobacco'
        else:
            return 'Does not consume alcohol neither tobacco'

    """
    This method assigns a label taking into account the age range of the person.
    Parameters
    answer = person's age is between x and y.
    """    
    def age_range_labeling(answer):
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