import seaborn as sns
import matplotlib.pyplot as plt

class Graph:
    width = 15
    height = 10
    title_font_size = 20
    xlabel_font_size = 15
    ylabel_font_size = 15

    def __init__(self, colors, graph_title, xlabel_name, ylabel_name):
        self.colors = colors
        self.graph_title = graph_title
        self.xlabel_name = xlabel_name
        self.ylabel_name = ylabel_name
        return
    
"""
This method set up the config for a graph
"""
@staticmethod
def graph_decorator(func):
        def wrapper(*args, **kwargs):
            plt.figure(figsize=(Graph.width, Graph.height))
            result = func(*args, **kwargs)
            plt.title(kwargs.get('graph_title', ''), fontsize=Graph.title_font_size)
            plt.xlabel(kwargs.get('xlabel_name', ''), fontsize=Graph.xlabel_font_size)
            plt.ylabel(kwargs.get('ylabel_name', ''), fontsize=Graph.ylabel_font_size)
            plt.tight_layout()
            plt.show()
            return result
        return wrapper

"""
This method creates a bar plot with its features
"""
@graph_decorator
def bar_plot_sns(x, y, data,**kwargs):
    sns.barplot(
    x=x,
    y=y,
    hue=kwargs.get('hue', 'x'),
    hue_order=kwargs.get('order', None),
    legend= False,
    data=data,
    palette=kwargs.get('palette', 'muted'),
    edgecolor=kwargs.get('edgecolor', 'black'))
    return

"""
This method creates an histogram with its features
"""
@graph_decorator
def hist_plot_sns(x, data, **kwargs):
     sns.histplot(
          data=data, 
          x=x, 
          kde=kwargs.get('kde', False),
          bins=kwargs.get('bins', 50)
          )
     return
