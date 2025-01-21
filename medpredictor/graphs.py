import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

class Graph:
    width = 15
    height = 10
    title_font_size = 20
    xlabel_font_size = 15
    ylabel_font_size = 15

    def __init__(self, colors, graph_title, xlabel_name, ylabel_name):
        self.colors = colors if colors != None else None 
        self.graph_title = graph_title
        self.xlabel_name = xlabel_name
        self.ylabel_name = ylabel_name
    
    def set_graph_colors(self, x, palette):
        if type(x) != 'list':
            raise TypeError('x must be list type')
        cmap = plt.get_cmap(palette if palette != None else 'viridis', len(x))
        hex_colors = [mcolors.to_hex(cmap(i)) for i in range(len(x))]
        dict_colors = dict(zip(x, hex_colors))
        self.colors = list(dict_colors.values())
        return self.colors
         

    """
    This method set up the config for a graph
    """
    def graph_decorator(func):
            def wrapper(self, *args, **kwargs):
                plt.figure(figsize=(Graph.width, Graph.height))
                result = func(self, *args, **kwargs)
                plt.title(self.graph_title, fontsize=Graph.title_font_size)
                plt.xlabel(self.xlabel_name, fontsize=Graph.xlabel_font_size)
                plt.ylabel(self.ylabel_name, fontsize=Graph.ylabel_font_size)
                plt.tight_layout()
                plt.show()
                return result
            return wrapper

    """
    This method creates a bar plot with its features
    """
    @graph_decorator
    def bar_plot_sns(self, x, y, data,**kwargs):
        sns.barplot(
        x=x,
        y=y,
        hue=kwargs.get('hue', None),
        hue_order=kwargs.get('order', None),
        legend= False,
        data=data,
        palette=self.colors if self.colors != None else 'muted',
        edgecolor=kwargs.get('edgecolor', 'black'))
        return

    """
    This method creates an histogram with its features
    """
    @graph_decorator
    def hist_plot_sns(self, x, data, **kwargs):
        if (type(self.colors) != 'str') and (type(self.colors) != 'NoneType'):
            raise TypeError(f'Type: {type(self.colors)} not supported') 
        else:  
            sns.histplot(
                data=data, 
                x=x, 
                kde=kwargs.get('kde', False),
                bins=kwargs.get('bins', 50),
                color=self.colors
                )
        return
