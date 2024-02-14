from sklearn.manifold import TSNE
import pandas as pd
import numpy as np
import os

def tsne_to_csv(file_name):
    input_csv = os.path.join('.', 'data', file_name)
    df = pd.read_csv(input_csv)

    df

    labels = df['label']
    df = df.drop(['label'], axis = 1)

    tsne = TSNE(init='random', n_components=3, random_state=42, perplexity=45)

    tsne_result = tsne.fit_transform(df)

    tsne_df = pd.DataFrame(data=tsne_result, columns=['x', 'y', 'z'])

    tsne_df['label'] = labels
        
    output_csv = os.path.join('.', 'data', file_name + '_TSNE')
    tsne_df.to_csv(output_csv, index=False)