
## The Final Countdown: Final Project MD

#### The skinny

- Here's the question in hand: Can a python program predict trends of a bullish or bearish market? 

- The Short Answer: Yeah, it'll get a general layout of whether or not a stock will decrease or increase but the numbers aren't precise. 

----------


## Meat n' Potatoes

Ok ok let's go. How'd I start? First thing's first was to get a compilation of companies and their prices over a series of time. I thought about using the NYSE over the past ten years but my Mac just about pooped itself trying to handle all the data. (There's 2800 companies on the NYSE). Let's go smaller. A lot smaller.

### One small step 

Before I tried tackling a whole stock exchange I wanted to create a graph that'd pull data for a single stock. Here's the link to what I used for [reference](https://towardsdatascience.com/python-how-to-get-live-market-data-less-than-0-1-second-lag-c85ee280ed93). I didn't use it verbatim; I looked at what modules they had and imported it into my own file python file. 

After downloading everything I noticed that PyCharm didn't realize my modules actually existed. Confused, I looked into the project preferences and saw that I was on the stock interpreter for my project. After adding all the modules I needed I could start.

It wasn't anything complex: All I did was pull stock data from Yahoo finance for a decade and convert that dataframe or ```df``` into a .csv file. For formatting I used ``` style.use('ggplot') ``` and for the data I used ```import pandas_datareader.data as web```. ``` matplotlib.pyplot``` and ```datetime``` were also used.
 Here's what that looks like:
```
import datetime as dt
from matplotlib.pyplot import style
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2011, 1, 1)
end = dt.datetime(2021, 5, 1)

df = web.DataReader('TSLA', 'yahoo', start, end)
df.to_csv('TSLA.csv')
```
### Learning to Walk 
So we got data for a single graph. Cool. Let's get the SP500 next! So from here I knew I needed to get a list of all the companies in it. But where? I'm ashamed to say it took me awhile to just google 'S&P 500 companies' and compile a list I found on Wikipedia.  

While searching for that I came across this nifty little youtube tutorial on [Programming for Finance](https://www.youtube.com/watch?v=baCAFPHb1o4&list=PLQVvvaa0QuDcOdF96TBtRtuQksErCEBYZ&index=6). I pulled a majority of my modules and code from this channel. However, the code he used is a little dated so I mostly used his stuff as a frame of reference. More on that later.

Ok back to our normally scheduled program. To get the tickers I had to convert the table - which was in HTML - into python and save that table. Now, I knew how to do this in R and was wondering if it'd be the same exact process (it was but with different syntax). In R, I could used a package called ```rvest``` and ```serialize``` that'd do this exact thing. I tried importing that in Python and saw that it was only compatible with R (much to my sadness 😞) .After another [quick googling](https://stackoverflow.com/questions/11709079/parsing-html-using-python) I saw that I could use  used ```beautiful soup as bs``` and ```pickle``` to compile the data. ```bs``` lets me parse the HTML data into an object (which in my case I just called ```soup```) . ```Pickle``` then serializes that said data into a variable I can call back to later. That way I have the tickers locally and don't have to pull from wikipedia everytime I run this. 

To compile the list I used a ```resp``` to directly look at the wiki page for the S&P 500. At first I searched for them as a class but switched it to an id because I thought it'd be more reliable. I didn't want to accidentally pull extra data if there were multiple elements in the class.
While looking at the table I realized that the HTML had ```-``` replaced with ```.``` and would have ```\n```  which isn't really an issue but it just looks ugly to me. I used: 
```
        if "." in ticker:
            ticker = ticker.replace('.', '-')
            print('ticker replaced to', ticker)
        tickers.append(ticker.strip())
```
        
to get rid all those issues. Once I had all that sorted out I saved it as a pickle ```with open("sp500tickers.pickle", "wb") as f:``` and dumped my tickers into file ```f```. Here's what the code looks like so far:
```
# All the imports
import bs4 as bs
import pickle
import requests
import datetime as dt
import pandas as pd
import pandas_datareader.data as web
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import style

style.use('ggplot')

print(os.getcwd())


# list for the S&P 500
def sp500_tickers():
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, "lxml")
    table = soup.find('table', {'id': 'constituents'})
    # Empty list
    tickers = []
    # tr = table row in case I forget/td = table data/0 is all the company names
    for row in table.findAll('tr')[1:]:
        ticker = row.find('td').text
        if "." in ticker:
            ticker = ticker.replace('.', '-')
            print('ticker replaced to', ticker)
        tickers.append(ticker.strip())
        # strip()gets rid of \n

    with open("sp500tickers.pickle", "wb") as f:
        pickle.dump(tickers, f)

    print(tickers)

    return tickers


sp500_tickers()
```

### Starting to Run

So now we have the list of companies. Now we need to actually get the data for everything we made. For this we'll be pulling from yahoo finance for an entire decade, making individual .csv files per company, and putting all those files into a folder. While running my tickers I ran into some issues. I kept getting key errors for some companies that were either no longer in the S&P 500 past 2016 or were only recently added. My code didn't like having empty spaces in the graphs it seems. I didn't know what the syntax was to override a keyerror so I had to look on [Stack Overflow](https://stackoverflow.com/questions/15653966/ignore-keyerror-and-continue-program/15653995) to figure it out. Problem solved! I put a ```try/except``` into my loop. This part of the code wasn't to difficult - I just had this tiny hiccup. Here's what it looks like:
```
def yahoo_data(reload_sp500=False):
    if reload_sp500:
        tickers = sp500_tickers()
    else:
        with open("sp500tickers.pickle", "rb") as f:
            tickers = pickle.load(f)

    if not os.path.exists('stock_dfs'):
        os.makedirs('stock_dfs')

    start = dt.datetime(2011, 1, 1)
    end = dt.datetime(2021, 5, 1)

    for ticker in tickers:
        try:
            print(ticker)
            if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):
                df = web.DataReader(ticker, 'yahoo', start, end)
                df.reset_index(inplace=True)
                df.set_index('Date', inplace=True)
                df.to_csv('stock_dfs/{}.csv'.format(ticker))
            else:
                print('Already have {}'.format(ticker))
        except KeyError:
            pass


# This took quite awhile to download
yahoo_data()
```
One little aside, when I first did this I didn't download the entire thing. i downloaded the first 10 companies just to see if it'd work. To do that I put ```[:10]``` after ```for ticker in tickers:```
```
for ticker in tickers[:10]:
```
### Compiling the Data into one big .csv file

After that last step we're left with 500 individual .csv files of all the data in the S&P 500 for the last decade. Let's compile it all into one for easy access! Like with the last step I'll be using the pickle to load the S&P 500 into my ```def compile data():``` using ```with open("sp500tickers.pickle"", "rb") as f:```. Since we're doing one big .csv file we'll be using the ```enumerate(tickers)``` function to reference each indidividual stock .csv file. Cool let's make this thing.
Ok ok hold up we have an issue. Per graph there's 6 different columns that represent the open,high,low, close, Volume, and Adj Close on any given day. Those were my y values for each graph but during the merge the y value's have been replaced with the stock name for all 500 companies (long story short, it just printed the names of all the tickers but no data). I had to readjust the columns and my final graph would show the adjusted close for each ticker (so now my y - axis was ```'Adj Close': ticker```. Getting the syntax for this was a little confusing because I thought using ```{}'Adj Close'``` would give me what I wanted but alas that wasn't the case- I was met with a syntax error. Another issue I saw was when making my columns I'd start an axis 0 which would give me an error./ I thought it was aguiven that when you dropped a column you'd start on 1,0 but apparently you have to directly type it in to get it to work. I found this out after finding someone on [YouTrack](https://youtrack.jetbrains.com/issue/PY-38773) having this issue. That's all the issues I had with this portion of the code.
Some other things I did while making this was I used a modulo function 
```
if count % 10 == 0: 
print (count)
``` 
to keep track of all the data I was uploading. It doesn't really do anything important but it does help me keep track of where the program is at in terms of downloading the data. Here's what this part looked like:
```
def compile_data():
    with open("sp500tickers.pickle", "rb") as f:
        tickers = pickle.load(f)

    main_df = pd.DataFrame()

    for count, ticker in enumerate(tickers):
        df = pd.read_csv('stock_dfs/{}.csv'.format(ticker.replace('.', '-')))
        df.set_index('Date', inplace=True)

        df.rename(columns={'Adj Close': ticker}, inplace=True)
        df.drop(['Open', 'High', 'Low', 'Close', 'Volume'], 1, inplace=True)

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df, how='outer')

        if count % 10 == 0:
            print(count)
    print(main_df.tail())
    main_df.to_csv('sp500_joined_closes.csv')
```
### Let's make it do stuff now 

So far we've gotten all the Adj Closed for the S&P 500 for the past decade. Let's go ahead and make it do something with that data. I'll be honest for this video, I borrowed EXTENSIVELY from this guy's [code](https://www.youtube.com/watch?v=Z-5wNWgRJpk). I essentially wanted the program to finally take a stock ticker and predict whether it'd be bullish or bearish within the next few days/weeks/months or however long I put it as. So for this one I actually didn't use the pickle. Since I had all the data on one .csv file I actually made my function ```process_labels``` reference the ```sp500_joined_closes.csv``` instead. Within that I also wanted to determine how many days it'd be analyzing into the future so I also made a variable called ```hm_day = 7``` that'd analyze a week into the future. This number is arbitrary and can be replaced with anything except for negative numbers. I wanted an equation that'd take an integer (in my instance ```i``` ) and go up towards that number but not hit it. 
``` for i in rang( 1, hm_days + 1 ):```
Here's the full equation: 
```
 for i in range(1, hm_days + 1):
        df['{}_{}d'.format(ticker, i)] = (df[ticker].shift(-i) - df[ticker]) / df[ticker]
    df.fillna(0, inplace=True)
```
What it means in lay men terms is we'd get the % growth/decay in the Adj Close for a (ticker) in the next i days. So if the ticker was ```'AAPL'```  and ```hm_days = 7``` it'd be ```df. ['AAPL_7D'] = % changes in Adj Close over the next 7 days```. This'll be important in the next step because I knew I'd want to use the % changes from ```process_labels``` to determine whether the trend of a certain ticker. I just didn't know how yet.

### Args 
For this part we're going to be identifying what's considered a buy sell or hold or ```bsh``` for short. Unlike the previous functions we'll set the parameters on this as ```def bsh(*args)``` so it can take any number of parameters we give it. Now I didn't actually really undertand how to use args until after reading up on it in this [website](https://www.geeksforgeeks.org/args-kwargs-python/#:~:text=The%20special%20syntax%20*args%20in,%2C%20variable%2Dlength%20argument%20list.&text=For%20example%20%3A%20we%20want%20to,to%20multiply%20them%20all%20together.) Before I had absolutely no real clue on how to use it. But now I do! We'll be using the % changes we got from ```process_labels``` and using that as the requirement for our args function. Here I used nested if statements to determine whether or not something was a buy or sell. 
```
def bsh(*args):
    cols = [c for c in args]
    requirement = 0.05
    for col in cols:
        if col > requirement:
            return 1
        if col < -requirement:
            return -1
    return 0
```

Extracting all this data and putting into a tangible portion of the terminal just took a lot of time to write. I had the function ```extract_featuresets(ticker)``` which would take data from the ```bsh``` function and mcompile the list into a something I could look at. For this example I used a span of 7 days so:
```
def extract_featuresets(ticker):
    tickers, df = process_labels(ticker)

    df['{}_target'.format(ticker)] = list(map(bsh,
                                              df['{}_1d'.format(ticker)],
                                              df['{}_2d'.format(ticker)],
                                              df['{}_3d'.format(ticker)],
                                              df['{}_4d'.format(ticker)],
                                              df['{}_5d'.format(ticker)],
                                              df['{}_6d'.format(ticker)],
                                              df['{}_7d'.format(ticker)]))

    vals = df['{}_target'.format(ticker)].values.tolist()
    str_vals = [str(i) for i in vals]
    print('Data spread:', Counter(str_vals))
    df.fillna(0, inplace=True)
    df = df.replace([np.inf, -np.inf], np.nan)
    df.dropna(inplace=True)

    df_vals = df[[ticker for ticker in tickers]].pct_change()
    df_vals = df_vals.replace([np.inf, -np.inf], 0)
    df_vals.fillna(0, inplace=True)

    X = df_vals.values
    y = df['{}_target'.format(ticker)].values
     return X, y, df
```
Here's what it returns:
``` 
Data spread: Counter({'0': 1681, '1': 513, '-1': 405})
```

The last part of the code was the shortest part so I won't talk in too much detail. I found three different Semi supervised, Model - based machine learning modules (LinearSVC, KNeighborsClassifier,and RandomForestClassifier) and ran those all at the same time. I had them run the previous functions and spit out the predicted output for the buys, sells, and holds. I also had accuracy measured as well.
Here's what it looks like:
```
def do_ml(ticker):
    X, y, df = extract_featuresets(ticker)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

    clf = VotingClassifier([('lsvc', svm.LinearSVC()),
                            ('knn', neighbors.KNeighborsClassifier()),
                            ('rfor', RandomForestClassifier())])

    clf.fit(X_train, y_train)
    confidence = clf.score(X_test, y_test)
    print('accuracy:', confidence)
    predictions = clf.predict(X_test)
    print('predicted class counts:', Counter(predictions))
    print()
    print()
    return confidence


do_ml('AAPL')
```
### Future implementations

In the future I'd obviously want to run the program to be more accurate. Right now a new ticker (ie one it hasn't ran before) is met with around 30% accuracy. It's only after running it time and time again that I've seen the accuracy get closer to 65%. Another thing I'd want to do is be able to run companies outside the S&P 500 - Unfortunately right now it can't do that (You can see in the Spoon.py file I'm working on it). When all that's done making it into an interactive program or website would be next. Right now, it's more so just accessible to me and made specifically to cater to me. I haven't put any fancy text or graphs, it's all just hard numbers. Although there's some past lines of codes you can see where I tried putting in a graph - I could probably have it running as an *arg parameter but I didn't get to it.  