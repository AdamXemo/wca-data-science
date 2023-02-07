import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib as mpl

def to_seconds(arr):
    return arr / 100

def get_country(df, country_name):
    return df.drop(df[df['personCountryId'] != country_name].index, inplace = False)

def get_event(df, event_id):
    return df.drop(df[df['eventId'] != event_id].index, inplace = False)

def get_average(df):
    return np.array(df['average'])

def get_singles(df):
    return np.concatenate((np.array(df['value1']),
                           np.array(df['value2']),
                           np.array(df['value3']),
                           np.array(df['value4']),
                           np.array(df['value5'])))

def remove_dnf(arr):
    return arr[arr > 0]

def show_hist(data, bins=200, xlim=[0,100]):
    plt.hist(data, bins=bins, color='mediumorchid', histtype='stepfilled', weights=np.ones(len(data)) / len(data))
    plt.xlabel('time, s')
    plt.ylabel('percentage, %')
    plt.xlim(xlim)
    plt.gca().yaxis.set_major_formatter(mpl.ticker.PercentFormatter(1))
    plt.show()

def show_pie_chart(df, title=None, bbox_to_anchor=None, colors=None):
    font = {'family': 'DejaVu Sans','size': 16}
    plt.rc('font', **font)

    ax = df.plot(kind='pie', y='people', figsize=(11,6), autopct='%1.1f%%', colors=colors)
    plt.title(title)
    plt.tight_layout()
    plt.legend(bbox_to_anchor=bbox_to_anchor)
    ax.set_ylabel('')
    plt.show()

continent_dict = {
    'Afghanistan': 'Asia',
    'Albania': 'Europe',
    'Algeria': 'Africa',
    'Andorra': 'Europe',
    'Angola': 'Africa',
    'Argentina': 'South America',
    'Armenia': 'Asia',
    'Australia': 'Oceania',
    'Austria': 'Europe',
    'Azerbaijan': 'Asia',
    'Bahamas': 'North America',
    'Bahrain': 'Asia',
    'Bangladesh': 'Asia',
    'Belarus': 'Europe',
    'Belgium': 'Europe',
    'Belize': 'North America',
    'Bhutan': 'Asia',
    'Bolivia': 'South America',
    'Bosnia and Herzegovina': 'Europe',
    'Brazil': 'South America',
    'Brunei': 'Asia',
    'Bulgaria': 'Europe',
    'Cambodia': 'Asia',
    'Canada': 'North America',
    'Chile': 'South America',
    'China': 'Asia',
    'Colombia': 'South America',
    'Costa Rica': 'North America',
    'Cote d_Ivoire': 'Africa',
    'Croatia': 'Europe',
    'Cuba': 'North America',
    'Cyprus': 'Asia',
    'Czech Republic': 'Europe',
    'Democratic Republic of the Congo': 'Africa',
    'Denmark': 'Europe',
    'Dominican Republic': 'North America',
    'Ecuador': 'South America',
    'Egypt': 'Africa',
    'El Salvador': 'North America',
    'Eritrea': 'Africa',
    'Estonia': 'Europe',
    'Fiji': 'Oceania',
    'Finland': 'Europe',
    'France': 'Europe',
    'Georgia': 'Asia',
    'Germany': 'Europe',
    'Ghana': 'Africa',
    'Greece': 'Europe',
    'Grenada': 'North America',
    'Guatemala': 'North America',
    'Guyana': 'South America',
    'Haiti': 'North America',
    'Honduras': 'North America',
    'Hong Kong': 'Asia',
    'Hungary': 'Europe',
    'Iceland': 'Europe',
    'India': 'Asia',
    'Indonesia': 'Asia',
    'Iran': 'Asia',
    'Iraq': 'Asia',
    'Ireland': 'Europe',
    'Israel': 'Asia',
    'Italy': 'Europe',
    'Jamaica': 'North America',
    'Japan': 'Asia',
    'Jordan': 'Asia',
    'Kazakhstan': 'Asia',
    'Kenya': 'Africa',
    'Korea': 'Asia',
    'Kosovo': 'Europe',
    'Kuwait': 'Asia',
    'Kyrgyzstan': 'Asia',
    'Latvia': 'Europe',
    'Lebanon': 'Asia',
    'Libya': 'Africa',
    'Liechtenstein': 'Europe',
    'Lithuania': 'Europe', 
    'Luxembourg': 'Europe', 
    'Macau': 'Asia', 
    'Madagascar': 'Africa',
    'Malawi': 'Africa', 
    'Malaysia': 'Asia', 
    'Maldives': 'Asia',
    'Malta': 'Europe',
    'Mauritius': 'Africa',
    'Mexico': 'North America',
    'Moldova': 'Europe',
    'Monaco': 'Europe',
    'Mongolia': 'Asia',
    'Montenegro': 'Europe',
    'Morocco': 'Africa',
    'Mozambique': 'Africa',
    'Namibia': 'Africa',
    'Nepal': 'Asia',
    'Netherlands': 'Europe',
    'New Zealand': 'Oceania',
    'Nicaragua': 'North America',
    'Nigeria': 'Africa',
    'North Macedonia': 'Europe',
    'Norway': 'Europe',
    'Oman': 'Asia',
    'Pakistan': 'Asia',
    'Palestine': 'Asia',
    'Panama': 'North America',
    'Papua New Guinea': 'Oceania',
    'Paraguay': 'South America',
    'Peru': 'South America',
    'Philippines': 'Asia',
    'Poland': 'Europe',
    'Portugal': 'Europe',
    'Qatar': 'Asia',
    'Romania': 'Europe',
    'Russia': 'Europe',
    'Saint Kitts and Nevis': 'North America',
    'Samoa': 'Oceania',
    'Saudi Arabia': 'Asia',
    'Senegal': 'Africa',
    'Serbia': 'Europe',
    'Singapore': 'Asia',
    'Slovakia': 'Europe',
    'Slovenia': 'Europe',
    'Somalia': 'Africa',
    'South Africa': 'Africa',
    'Spain': 'Europe',
    'Sri Lanka': 'Asia',
    'Sudan': 'Africa',
    'Suriname': 'South America',
    'Sweden': 'Europe',
    'Switzerland': 'Europe',
    'Syria': 'Asia',
    'Taiwan': 'Asia',
    'Tajikistan': 'Asia',
    'Tanzania': 'Africa',
    'Thailand': 'Asia',
    'Togo': 'Africa',
    'Tonga': 'Oceania',
    'Trinidad and Tobago': 'North America',
    'Tunisia': 'Africa',
    'Turkey': 'Asia',
    'Turkmenistan': 'Asia',
    'USA': 'North America',
    'Uganda': 'Africa',
    'Ukraine': 'Europe',
    'United Arab Emirates': 'Asia',
    'United Kingdom': 'Europe',
    'Uruguay': 'South America',
    'Uzbekistan': 'Asia',
    'Venezuela': 'South America',
    'Vietnam': 'Asia',
    'Yemen': 'Asia',
    'Zambia': 'Africa',
    'Zimbabwe': 'Africa'}














def drop_n_clean(results):
    new_results = results.drop(['value1',
                'value2', 
                'value3', 
                'value4', 
                'value5', 
                'regionalSingleRecord', 
                'regionalAverageRecord', 
                'personId', 
                'roundTypeId', 
                'pos', 
                'formatId'],
                axis=1, 
                inplace=False)
    new_results = new_results.reset_index(drop=True)
    index_names = []

    index_names.extend(results[results['best']==-1].index)
    index_names.extend(results[results['average']==0].index)
    index_names.extend(results[results['average']==-1].index)


    return new_results.drop(index_names)

def sort(results):
    return results.sort_values(by='best', ascending=True, axis=0)

def df_to_seconds(results):
    new_results = results
    new_results['best'] = pd.DataFrame(map(lambda x: x/100, new_results['best'])).values
    new_results['average'] = pd.DataFrame(map(lambda x: x/100, results['average'])).values

    return new_results

def get_national_records(results):
    nrs = []
    countries = np.unique(results['personCountryId'])
    for country in countries:
        best = results.loc[results['personCountryId'] == country, 'best'].min()
        nrs.append(best)

    data = {'time': nrs, 'country': countries}
    national_records = pd.DataFrame(data).dropna()
    national_records['time'] = pd.to_numeric(national_records['time'])
    return national_records

"""
m = folium.Map(location=[0, 0], zoom_start=2)

folium.Choropleth(
    geo_data=world_geo,
    bins=8,
    name='choropleth',
    data=national_records_3x3,
    columns=['country', 'time'],
    key_on='feature.properties.name',
    fill_color='Greens',
    highlight=True,
    nan_fill_color='darkgreen',
    threshold_scale=[3, 4, 4.8, 6, 9, 15, 20, 101],
    fill_opacity=0.9,
    line_opacity=0.18,
    legend_name='National Record (seconds)'
    
).add_to(m)

folium.LayerControl().add_to(m)
"""