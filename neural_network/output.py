import pandas as pd
import numpy as np
import single_hidden_layer as nn
import load_data
from constants import FID, HALF_SIZE_IMAGE
import ipdb


## predict results
features_test = load_data.test()
features_name = load_data.feature_name()
results = nn.predict(features_test)





def prepare_for_output(results):
    """Convert numpy array to dataframe"""

    ##convert to pixels
    results2 = results*float(HALF_SIZE_IMAGE) + float(HALF_SIZE_IMAGE)
    ipdb.set_trace()
    ## refactor data
    header = ["RowId", "ImageId", "FeatureName", "Location"]
    n_images = 1783
    n_features = 30
    rowid = 1
    df = pd.DataFrame(index=range(n_images*n_features),columns=header)

    ##nested loops are not efficient at all, but who cares
    for image in xrange(n_images):
        for feat in xrange(n_features):
            print float(rowid) / (n_images*n_features) * 100., "%"
            df.loc[rowid,:] = [rowid, 
                               image+1,
                               features_name[feat],
                                results[image, feat]]
            rowid += 1

    df.dropna(inplace=True) #remove rowid=0
    return df




def filter_lookuptable(df):
    """Output only the desired features"""

    df = df.set_index(["ImageId","FeatureName"])
    df_lookup = df_lookup = pd.read_csv(FID, names=[u'RowId2', u'ImageId', u'FeatureName', u'Location2'],skiprows=1)
    df_lookup = df_lookup.set_index(["ImageId","FeatureName"])
    joined_df = pd.concat([df,df_lookup],axis=1)
    joined_df.drop("Location2",1,inplace=True)
    joined_df.dropna(inplace=True)
    joined_df = joined_df.set_index("RowId2")
    joined_df["RowId"] = joined_df.index
    joined_df["RowId"] = joined_df["RowId"].astype(int)
    return joined_df.sort()










df = prepare_for_output(results)
df = filter_lookuptable(df)



##write to csv

##filter using idlookuptable
outputfile = "kaggle.csv"
df.to_csv(outputfile, header=["RowId","Location"], index=False)
