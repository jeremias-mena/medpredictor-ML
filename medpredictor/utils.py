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
