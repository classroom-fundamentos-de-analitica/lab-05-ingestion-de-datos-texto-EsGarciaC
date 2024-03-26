import pandas as pd
import glob
import os




def read_file(name: str) -> str:
    with open(name, "r") as file:
        return file.readline()
    
def files_in_dir(dir) -> list[str]:
    return [read_file(archivo) for archivo in glob.glob(os.path.join(dir + '*.txt'))]



def get_df(dir: str) -> pd.DataFrame:
    dictio = {"phrase": [], "sentiment": []}

    for nombre_sentimiento in ["negative", "neutral", "positive"]:
        lista_archivos = files_in_dir(f"{dir}/{nombre_sentimiento}/")
        dictio["phrase"] += lista_archivos
        nueva_lista = [nombre_sentimiento] * len(lista_archivos)
        dictio["sentiment"] += nueva_lista

    return pd.DataFrame(dictio)

if __name__ == "__main__":
    df_test = get_df("test")
    df_train = get_df("train")


    df_test.to_csv("test_dataset.csv", sep = ",", index= False)
    df_train.to_csv("train_dataset.csv", sep = ",", index= False)