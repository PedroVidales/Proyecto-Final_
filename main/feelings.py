from transformers import pipeline
import pandas as pd
import warnings

warnings.filterwarnings('ignore')
pd.set_option('display.max_columns', None)

rev = pd.read_csv(r'C:\Users\Pedro Vidales\Desktop\Proyecto-Final_\reviews_detailed.csv')
rev = rev.drop('reviewer_name', axis=1)
rev.dropna(axis=0, inplace=True)
rev.reset_index(drop=True, inplace=True)
rev.date=pd.to_datetime(rev.date, format='%Y-%m-%d')

sentiment_pipeline = pipeline("sentiment-analysis")

def find_sentiment(text):
    sent = sentiment_pipeline([text[:250]])[0]
    score = sent["score"]
    if sent["label"] == "NEGATIVE":
        score *= -1
    return score
rev.shape
from tqdm import tqdm

batch_size = 10000
batches = [rev[i:i+batch_size] for i in range(0, len(rev), batch_size)]

# Inicializar el diccionario para almacenar los resultados
edits = {}

# Procesar cada lote por separado
for batch in tqdm(batches, total=len(batches), leave=True):
    # Iterar sobre cada fila del lote
    for index, row in batch.iterrows():
        date = row["date"]
        comment = row["comments"]
        if pd.isnull(comment):  # Si el comentario es nulo, omitir la fila
            continue
        if not pd.isnull(date):
            date = pd.to_datetime(date).strftime("%Y-%m-%d")
        else:
            date = "No date available"
        comment_id = row["id"]
        if date not in edits:
            edits[date] = dict(sentiments=list(), edit_count=0, comment_ids=list())
        edits[date]["edit_count"] += 1
        edits[date]["comment_ids"].append(comment_id)
        edits[date]["sentiments"].append(find_sentiment(comment))

# Combinar los resultados en un DataFrame
results = pd.concat([pd.DataFrame({"date": k, **v}) for k, v in edits.items()], ignore_index=True)