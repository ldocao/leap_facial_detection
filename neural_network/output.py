import pandas as pd
import numpy as np
import single_hidden_layer as nn
import load_data
import ipdb


## predict results
features_test = load_data.test()
features_name = load_data.feature_name()
results = nn.predict(features_test)





def prepare_for_output(results):
    """Convert numpy array to dataframe"""


    ## refactor data
    header = ["RowId", "ImageId", "FeatureName", "Location"]
    n_images = 1783
    n_features = 30
    rowid = 1
    df = pd.DataFrame(index=range(n_images*n_features),columns=header)

    ##nested loops are not efficient at all, but who cares
    for image in xrange(n_images):
        for feat in xrange(n_features):
            print rowid / (n_images*n_features) * 100., "%"
            df.loc[rowid,:] = [rowid, 
                               image+1,
                               features_name[feat],
                                results[image, feat]]
            rowid += 1

    df.dropna(inplace=True) #remove rowid=0
    return df




def filter_lookuptable(df):
    """Output only the desired features"""





df = prepare_for_output(results)

##write to csv
idlookuptable = ""
##filter using idlookuptable
outputfile = "kaggle.csv"
df.to_csv(outputfile, header=header, index=False)
