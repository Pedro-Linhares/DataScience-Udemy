#See if have dubbled unique elements -> Don't need on this dataset
#See if have NaN values -> Umidade, Vento |OK
#See if have Data out of domain -> Temperature(Max:130F, Min:-130F), Umidade(max:100, min:0) |OK
#See if have Missing patter -> Aparencia(v = menos) |OK


from turtle import clear
import pandas as pd
import seaborn as srn
import statistics as sts

#Importing Data
dataset = pd.read_csv('tempo.csv', sep=";")
#View Data
# $ print(dataset.head())

temperatura = dataset["Temperatura"]
umidade = dataset["Umidade"]
vento = dataset["Vento"]

def CategoricalData():
    def view():
        #Aparencia/ Vento/ jogar
        aparencia_cluster = dataset.groupby(["Aparencia"]).size()
        #View Aparencia(appearance) Column
        print(f"{aparencia_cluster} \n")

        vento_cluster = dataset.groupby(["Vento"]).size()
        #View Vento(Wind) column
        print(f"{vento_cluster} \n")

        jogar_cluster = dataset.groupby(["Jogar"]).size()
        #View Jogar(Play) column
        print(jogar_cluster)

    #view()
    # Put In Patter===================
    dataset.loc[dataset["Aparencia"] == "menos", "Aparencia"] = "sol"
    #=================================
    view()

def NumericalData():
    def view():
        #Temperatura/ Umidade
        temperatura_cluster = dataset["Temperatura"].describe()
        #View Temperatura(Temperature) column
        print(f"{temperatura_cluster} \n")

        umidade_cluster = dataset["Umidade"].describe()
        #View Umidade(Moisture) column
        print(umidade_cluster)

    def PutInDomain():
        median_temperatura = sts.median(temperatura)
        median_umidade = sts.median(umidade)

        dataset.loc[(temperatura < -130) | (temperatura > 130), "Temperatura"] = median_temperatura
        dataset.loc[(umidade < 0) | (umidade > 100), "Umidade"] = median_umidade

    #view()
    PutInDomain()
    view()

def NanValues():
    def view():
        isNaN = dataset.isnull().sum()
        #view NaN values
        print(isNaN)

    def PutValues():
        median_umidade = sts.median(umidade)

        umidade.fillna(median_umidade, inplace=True)
        vento.fillna('FALSO', inplace=True)

    #view()
    PutValues()
    view()


CategoricalData()
NumericalData()
NanValues()