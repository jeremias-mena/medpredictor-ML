from IPython.display import Markdown

class Metric:
    
    def __init__(self):
        pass

    """
    This method calculates percentajes for datasets features
    """    
    def calc_percentajes(self, value, total):
        return (value*100)/total if (total > 0) else 0