import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df=csv.DictReader(csv_file)
        fig=px.scatter(df,x="Days Present", y="Marks In Percentage")
        fig.show()

def getDataSource(data_path):
    Marks = []
    Presents = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Marks.append(float(row["Marks In Percentage"]))
            Presents.append(float(row["Days Present"]))

    return {"x" : Marks, "y": Presents}

def findCorrelation(datasource):
    correlation=np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Marks in percentage and Days present:",correlation[0,1])

def setup():
    data_path="/Users/raama/Documents/White hat jr./python/p106/data.csv"

    datasource=getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)

setup()