def answer_one():
    import pandas as pd
    import numpy as np
    import re
    url = 'Energy Indicators.xls'
    energy = (pd.read_excel(url, header = 0, skiprows = 17, skip_footer=38)
            .drop(['Unnamed: 0', 'Unnamed: 1'], axis=1)
            .rename(columns={'Unnamed: 2': 'Country'})
            .rename(columns={'Petajoules': 'Energy Supply'})
            .rename(columns={'Gigajoules': 'Energy Supply per Capita'})
            .rename(columns={'%': '% Renewable'}))
    energy['Energy Supply'] = pd.to_numeric(energy['Energy Supply'], errors = 'coerce')
    energy['Energy Supply per Capita'] = pd.to_numeric(energy['Energy Supply per Capita'], errors = 'coerce')
    energy['% Renewable'] = pd.to_numeric(energy['% Renewable'], errors = 'coerce')
    energy['Energy Supply'] = energy['Energy Supply'] * 1000000
    country_map = {"Republic of Korea": "South Korea",
    "United States of America": "United States",
    "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
    "China, Hong Kong Special Administrative Region": "Hong Kong"}
    energy['Country'] = energy['Country'].apply(lambda x: re.compile("[\\(|\d]").split(x)[0].strip())
    for key, value in country_map.items():
        energy.loc[(energy['Country'] == key), 'Country'] = value
    GDP = (pd.read_csv('world_bank.csv', skiprows = 4, header = 0)
                .rename(columns={'Country Name': 'Country'}))
    country_map = {"Korea, Rep.": "South Korea", 
    "Iran, Islamic Rep.": "Iran",
    "Hong Kong SAR, China": "Hong Kong"}
    for key, value in country_map.items():
        GDP.loc[(GDP['Country'] == key), 'Country'] = value
    gdp_drop_columns = ['Country Code', 'Indicator Name', 'Indicator Code',
           '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968',
           '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977',
           '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986',
           '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995',
           '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004',
           '2005']
    GDP = GDP.drop(gdp_drop_columns, axis=1)
    url = 'scimagojr-3.xlsx'
    ScimEn = (pd.read_excel(url, header = 0))
    #join_type = 'inner'
    join_type = 'left'
    tdf = pd.merge(ScimEn, energy, how = join_type, on='Country')
    tdf = pd.merge(tdf, GDP, how = join_type, on='Country')
    tdf = tdf.sort_values(by='Rank', ascending=True).head(15)
    tdf.set_index('Country',inplace=True)
    return tdf

answer_one()

def answer_two():
    import pandas as pd
    import numpy as np
    import re
    url = 'Energy Indicators.xls'
    energy = (pd.read_excel(url, header = 0, skiprows = 17, skip_footer=38)
            .drop(['Unnamed: 0', 'Unnamed: 1'], axis=1)
            .rename(columns={'Unnamed: 2': 'Country'})
            .rename(columns={'Petajoules': 'Energy Supply'})
            .rename(columns={'Gigajoules': 'Energy Supply per Capita'})
            .rename(columns={'%': '% Renewable'}))
    energy['Energy Supply'] = pd.to_numeric(energy['Energy Supply'], errors = 'coerce')
    energy['Energy Supply per Capita'] = pd.to_numeric(energy['Energy Supply per Capita'], errors = 'coerce')
    energy['% Renewable'] = pd.to_numeric(energy['% Renewable'], errors = 'coerce')
    energy['Energy Supply'] = energy['Energy Supply'] * 1000000
    country_map = {"Republic of Korea": "South Korea",
    "United States of America": "United States",
    "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
    "China, Hong Kong Special Administrative Region": "Hong Kong"}
    energy['Country'] = energy['Country'].apply(lambda x: re.compile("[\\(|\d]").split(x)[0].strip())
    for key, value in country_map.items():
        energy.loc[(energy['Country'] == key), 'Country'] = value
    GDP = (pd.read_csv('world_bank.csv', skiprows = 4, header = 0)
                .rename(columns={'Country Name': 'Country'}))
    country_map = {"Korea, Rep.": "South Korea", 
    "Iran, Islamic Rep.": "Iran",
    "Hong Kong SAR, China": "Hong Kong"}
    for key, value in country_map.items():
        GDP.loc[(GDP['Country'] == key), 'Country'] = value
    gdp_drop_columns = ['Country Code', 'Indicator Name', 'Indicator Code',
           '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968',
           '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977',
           '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986',
           '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995',
           '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004',
           '2005']
    GDP = GDP.drop(gdp_drop_columns, axis=1)
    url = 'scimagojr-3.xlsx'
    ScimEn = (pd.read_excel(url, header = 0))
    join_type = 'inner'
    tdf = pd.merge(ScimEn, energy, how = join_type, on='Country')
    tdf = pd.merge(tdf, GDP, how = join_type, on='Country')
    tdf.set_index('Country',inplace=True)
    len1 = len(tdf)    
    join_type = 'outer'
    tdf = pd.merge(ScimEn, energy, how = join_type, on='Country')
    tdf = pd.merge(tdf, GDP, how = join_type, on='Country')
    tdf.set_index('Country',inplace=True)
    len2 = len(tdf) 
    return len2 - len1

answer_two()

def answer_three():
    Top15 = answer_one()
    Top15["avgGDP"]=Top15[['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']].mean(axis=1)
    Top15 = Top15.sort_values(by='avgGDP', ascending=False)
    avgGDP_series= Top15.loc[:,'avgGDP']
    return avgGDP_series

answer_three()

def answer_four():
    Top15 = answer_one()
    Top15["avgGDP"]=Top15[['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']].mean(axis=1)
    Top15 = Top15.sort_values(by='avgGDP', ascending=False).head(6)
    Top15.drop(Top15.columns[0:10],axis=1, inplace=True)
    avgGDP_series6 = Top15.iloc[5]
    diff = avgGDP_series6[9] - avgGDP_series6[0]
    return diff

answer_four()

def answer_five():
    import pandas as pd
    import numpy as np
    Top15 = answer_one()
    res = np.nanmean(Top15['Energy Supply per Capita'])
    return res.item()

answer_five()

def answer_six():
    Top15 = answer_one()
    Top15 = Top15.sort_values(by='% Renewable', ascending=False).head(1)['% Renewable']
    return (Top15.index.values[0], Top15.values[0])

answer_six()

def answer_seven():
    Top15 = answer_one()
    Top15['ratio'] = Top15['Self-citations']/Top15['Citations']
    Top15 = Top15.sort_values(by='ratio', ascending=False).head(1)['ratio']
    return (Top15.index.values[0], Top15.values[0])

answer_seven()

def answer_eight():
    Top15 = answer_one()
    Top15['Population'] = Top15['Energy Supply']/Top15['Energy Supply per Capita']
    return Top15.sort_values(by='Population', ascending=False).iloc[2].name

answer_eight()

def answer_nine():
    Top15 = answer_one()
    Top15['Estimate Population'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['avgCiteDocPerPerson'] = Top15['Citable documents'] / Top15['Estimate Population']
    x = Top15[['Energy Supply per Capita', 'avgCiteDocPerPerson']]
    return x.corr().loc['avgCiteDocPerPerson', 'Energy Supply per Capita']

answer_nine()

def answer_ten():
    Top15 = answer_one()
    mid = Top15['% Renewable'].median()
    Top15['HighRenew'] = Top15['% Renewable']>=mid
    Top15['HighRenew'] = Top15['HighRenew'].apply(lambda x:1 if x else 0)
    Top15.sort_values(by='Rank', inplace=True)
    return Top15['HighRenew']

answer_ten()

def answer_eleven():
    import pandas as pd
    import numpy as np
    Top15 = answer_one()
    ContinentDict  = {'China':'Asia', 
                  'United States':'North America', 
                  'Japan':'Asia', 
                  'United Kingdom':'Europe', 
                  'Russian Federation':'Europe', 
                  'Canada':'North America', 
                  'Germany':'Europe', 
                  'India':'Asia',
                  'France':'Europe', 
                  'South Korea':'Asia', 
                  'Italy':'Europe', 
                  'Spain':'Europe', 
                  'Iran':'Asia',
                  'Australia':'Australia', 
                  'Brazil':'South America'}
    groups = pd.DataFrame(columns = ['size', 'sum', 'mean', 'std'])
    Top15['Estimate Population'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    for group, frame in Top15.groupby(ContinentDict):
        groups.loc[group] = [len(frame), frame['Estimate Population'].sum(),frame['Estimate Population'].mean(),frame['Estimate Population'].std()]
    return groups

answer_eleven()

def answer_twelve():
    Top15 = answer_one()
    ContinentDict  = {'China':'Asia', 
                  'United States':'North America', 
                  'Japan':'Asia', 
                  'United Kingdom':'Europe', 
                  'Russian Federation':'Europe', 
                  'Canada':'North America', 
                  'Germany':'Europe', 
                  'India':'Asia',
                  'France':'Europe', 
                  'South Korea':'Asia', 
                  'Italy':'Europe', 
                  'Spain':'Europe', 
                  'Iran':'Asia',
                  'Australia':'Australia', 
                  'Brazil':'South America'}
    Top15 = Top15.reset_index()
    Top15['Continent'] = [ContinentDict[country] for country in Top15['Country']]
    Top15['bins'] = pd.cut(Top15['% Renewable'],5)
    return Top15.groupby(['Continent','bins']).size()

answer_twelve()

def answer_thirteen():
    Top15 = answer_one()
    Top15['PopEst'] = (Top15['Energy Supply'] / Top15['Energy Supply per Capita'])
    Top15['PopEst'] = Top15['PopEst'].astype(float)
    return Top15['PopEst'].apply(lambda x: '{0:,}'.format(x))

answer_thirteen()

def plot_optional():
    import matplotlib as plt
    %matplotlib inline
    Top15 = answer_one()
    ax = Top15.plot(x='Rank', y='% Renewable', kind='scatter', 
                    c=['#e41a1c','#377eb8','#e41a1c','#4daf4a','#4daf4a','#377eb8','#4daf4a','#e41a1c',
                       '#4daf4a','#e41a1c','#4daf4a','#4daf4a','#e41a1c','#dede00','#ff7f00'], 
                    xticks=range(1,16), s=6*Top15['2014']/10**10, alpha=.75, figsize=[16,6]);

    for i, txt in enumerate(Top15.index):
        ax.annotate(txt, [Top15['Rank'][i], Top15['% Renewable'][i]], ha='center')

    print("This is an example of a visualization that can be created to help understand the data. \
This is a bubble chart showing % Renewable vs. Rank. The size of the bubble corresponds to the countries' \
2014 GDP, and the color corresponds to the continent.")