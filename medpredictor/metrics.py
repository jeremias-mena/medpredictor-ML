from IPython.display import Markdown

class MetricsDisplay:
    
    def __init__(self):
        pass
    
    @staticmethod
    def show_metric(name_metric, metric):
        Markdown(f"{name_metric}: {metric}%")
        return

    @staticmethod
    def show_metrics(metrics):
        for name, value in metrics.items():
            Markdown(f"{name}: {value}%")
        return
