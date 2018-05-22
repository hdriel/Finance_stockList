import csv
import matplotlib.pyplot as plt
import pprint
##
## Hadriel Benjo
##
## ---------------------------------------------------------------------   
## read data from file
def getSymbolLists(companyListFile = 'secwiki_tickers'):
    labels = ['Ticker', 'Name', 'Sector', 'Industry']
    df = {}
    for l in labels:  df[l] = []
    with open(companyListFile+'.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            strintLine = ''
            for l in labels:
                try:
                    df[l].append(row[l])
                except:
                    print('Cannot file the title {0} in the first line of the file {1}.csv'.format(l, companyListFile))
                    print('break down the reader from file...')
                    break
    return df

## ---------------------------------------------------------------------   
## getting data into lists
df = getSymbolLists()
Symbol = df['Ticker']
Name = df['Name']
Sector = df['Sector']
Industry = df['Industry']

sector_frequencies = {}
for s in Sector:
    sector_frequencies[s] = sector_frequencies.get(s,0) + 1

pprint.pprint(sector_frequencies)

sector_val = []
sector_str = []
for k,v in sector_frequencies.items():
    sector_val.append(v)
    sector_str.append(k)
    
## ---------------------------------------------------------------------
## plot bar graph
def bar(Sector, sector_str):
    ax = plt.subplot2grid((1,1),(0,0))
    
    bins = []
    for i in range(len(sector_str)):
        bins.append(i)
        ax.plot([],[], label='{0}-{1} : {2}'.format(i,i+1,sector_str[i]))
        
    for s in range(len(Sector)):
        for l in range(len(sector_str)):
            if(sector_str[l] == Sector[s]):
                Sector[s] = l

    
    
    ax.set_xticks(bins)
    plt.hist(Sector, bins, histtype='bar', rwidth = 0.8)

    plt.title('BAR GRAPH\nDistribution of sectors from the list of shares in the file')
    ax.legend()
    plt.show()
bar(Sector, sector_str)

## ---------------------------------------------------------------------
## plot pie graph
def pie(sector_val, sector_str):
    plt.pie(sector_val,
            labels = sector_str ,
            startangle = 40,
            #explode = explodes,
            autopct = '%1.1f%%')
    
    plt.title('PIE GRAPH\nDistribution of sectors from the list of shares in the file')
    plt.show()
pie(sector_val, sector_str)
