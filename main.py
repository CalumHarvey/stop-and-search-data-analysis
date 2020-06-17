import pandas as pd
import matplotlib as plt




def readFile():
    df = pd.read_csv("stop-and-search.csv")

    return df


def cleanData(data):
    data.columns = [c.replace(' ', '_') for c in data.columns]
    data.columns = [c.replace(',', '') for c in data.columns]

    data.rows = [c.replace(',', '') for c in data.columns]

    data.drop(["Notes"], axis=1, inplace=True)

    indexNames = data[data["Rate_per_1000_population_by_ethnicity"] == " N/A "].index
    data.drop(indexNames, inplace=True)

    indexNames = data[data["Rate_per_1000_population_by_ethnicity"] == " -   "].index
    data.drop(indexNames, inplace=True)


    data["Rate_per_1000_population_by_ethnicity"] = data["Rate_per_1000_population_by_ethnicity"].astype(float)

    data["Time"] = data["Time"].astype(str)



    return data


def main():

    df = readFile()
    cleanDF = cleanData(df)

    totalData = cleanDF[cleanDF['Geography'] == "All - including BTP"]

    #print(totalData)

    index = totalData["Ethnicity"]
    index.drop_duplicates(inplace=True)

    year1 = totalData[totalData['Time'].isin(["2006/07"])]
    year2 = totalData[totalData["Time"] == "2007/08"]
    year3 = totalData[totalData["Time"] == "2008/09"]
    year4 = totalData[totalData["Time"] == "2009/10"]
    year5 = totalData[totalData["Time"] == "2010/11"]
    year6 = totalData[totalData["Time"] == "2011/12"]
    year7 = totalData[totalData["Time"] == "2012/13"]
    year8 = totalData[totalData["Time"] == "2013/14"]
    year9 = totalData[totalData["Time"] == "2014/15"]
    year10 = totalData[totalData["Time"] == "2015/16"]
    year11 = totalData[totalData["Time"] == "2016/17"]
    year12 = totalData[totalData["Time"] == "2017/18"]
    print(year3)


    #df = pd.DataFrame({"2006/7" : year1, "2007/8" : year2, "2008/9" : year3, "2009/10" : year4, "2010/11" : year5, "2011/12" : year6, "2012/13" : year7,
    #"2013/14" : year8, "2014/15" : year9, "2015/16" : year10, "2016/17" : year11, "2017/18" : year12}, index=index)


    #print(totalData.groupby("Ethnicity")["Rate_per_1000_population_by_ethnicity"].mean())


    #cleanDF.plot.bar(x="Ethnicity")











if __name__ == "__main__":
    main()