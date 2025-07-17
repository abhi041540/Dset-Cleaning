import pandas as pd
import numpy as np

def isnullPresent(dataset):
    return dataset.isnull().sum().sum() != 0

def findNullColumns(dataset):
    return dataset.columns[dataset.isnull().any()].tolist()

def nullDataSize(dataset):
    v1=dataset.shape
    v1 = v1[0] * v1[1]
    v2=dataset.dropna().shape
    v2 = v2[0] * v2[1]
    return ((v2 / v1) * 100)

def outputColumnTest(lst, dataset):
    lst_copy = lst.copy()
    for cl in lst_copy:
        if cl == dataset.columns[-1]:
            lst.remove(cl)
            if ((dataset[cl].dtype != np.int64) and (len(dataset[cl].unique()) <= 10)) or \
               ((dataset[cl].dtype == np.int64) and (len(dataset[cl].unique()) <= 2)):
                return [True, 1, cl]
            else:
                return [True, 0, cl]
    target = dataset.columns[-1]
    if ((dataset[target].dtype != np.int64) and (len(dataset[target].unique()) <= 10)) or \
       ((dataset[target].dtype == np.int64) and (len(dataset[target].unique()) <= 2)):
        return [False, 1, target]
    else:
        return [False, 0, target]

def outputColumnTreating(lst, dataset):
    if lst[0]:
        v2 = dataset[lst[2]].shape[0]
        v1 = dataset[lst[2]].isnull().sum()
        if (v1 / v2) * 100 <= 8:
            dataset.dropna(subset=[lst[2]], inplace=True)
        else:
            if dataset[lst[2]].dtype == np.int64:
                dataset[lst[2]].fillna(dataset[lst[2]].mean(), inplace=True)
            else:
                mode_vals = dataset[lst[2]].mode(dropna=True)
                if not mode_vals.empty:
                    dataset[lst[2]].fillna(mode_vals[0], inplace=True)

def treatColumns(dataset, size, lst):
    for l in lst:
        v1 = dataset[l].isnull().sum()
        v2 = dataset[l].shape[0]
        if ((v1 / v2) * 100 >= 70):
            dataset.drop(columns=[l], inplace=True)
        else:
            retained = dataset.dropna(subset=[l]).copy()
            per = ((retained.shape[0] * retained.shape[1]) / size) * 100
            if per <= 8:
                dataset.dropna(subset=[l], inplace=True)
            else:
                if np.issubdtype(dataset[l].dtype, np.number):
                    dataset[l].fillna(round(dataset[l].mean()), inplace=True)
                    dataset[l] = dataset[l].astype(dataset[l].dtype)
                else:
                    mode_vals = dataset[l].mode()
                    if not mode_vals.empty:
                        dataset[l].fillna(mode_vals[0], inplace=True)

def treatOutlairs(dataset):
    lst = dataset.columns
    for l in lst:
        if np.issubdtype(dataset[l].dtype, np.number):
            skewness = dataset[l].skew()
            if -1 <= skewness <= 1:
                continue
            q1 = dataset[l].quantile(.25)
            q3 = dataset[l].quantile(.75)
            iqr = q3 - q1
            if skewness < 0:
                data1 = dataset[dataset[l] >= (q3 - (1.5 * iqr))].copy()
                min = dataset[l].mean() - (3 * dataset[l].std())
                data2 = dataset[dataset[l] >= min].copy()
            else:
                data1 = dataset[dataset[l] <= (q3 + (1.5 * iqr))].copy()
                min = dataset[l].mean() + (3 * dataset[l].std())
                data2 = dataset[dataset[l] <= min].copy()
            dataset.drop(index=dataset.index.difference((data1 if data1.shape[0] >= data2.shape[0] else data2).index), inplace=True)

def dataClaning(dataset):
    s1=dataset.shape[0]*dataset.shape[1]
    if isnullPresent(dataset):
        per_null = nullDataSize(dataset)
        if per_null >= 90:
            data = dataset.dropna().copy()
            treatOutlairs(data)
            data.drop_duplicates(inplace=True)
            return data
        else:
            size = dataset.shape[0] * dataset.shape[1]
            null_column_lst = findNullColumns(dataset)
            ocl_type = outputColumnTest(lst=null_column_lst, dataset=dataset)
            outputColumnTreating(ocl_type, dataset)
            treatColumns(dataset=dataset, size=size, lst=null_column_lst)
            treatOutlairs(dataset)
    else:
        treatOutlairs(dataset)
    dataset.drop_duplicates(inplace=True)
    return dataset

if __name__ == "__main__":
    print("main file")
