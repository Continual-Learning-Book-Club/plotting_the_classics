# Imports were not included in the example
from urllib.request import urlopen
from datascience.tables import Table
import numpy as np
import pandas as counts
import matplotlib
import matplotlib.pyplot as plots
import warnings

# By default, matplotlib wouldn't show the graphs, switching matplotlib's configuration to us
# tkagg fixed the issue
matplotlib.use('tkagg')

# Gets rid of the warning about implicit column method lookup being deprecated
warnings.simplefilter(action="ignore", category=FutureWarning)

# This function was not defined in the example, but was called, causing an error
def read_url(url):
    return urlopen(url).read().decode()


huck_finn_url = 'https://www.inferentialthinking.com/data/huck_finn.txt'
huck_finn_text = read_url(huck_finn_url)
huck_finn_chapters = huck_finn_text.split('CHAPTER ')[44:]

little_women_url = 'https://www.inferentialthinking.com/data/little_women.txt'
little_women_text = read_url(little_women_url)
little_women_chapters = little_women_text.split('CHAPTER ')[1:]

# Added print() method to display the results from the example
print(Table().with_column('Chapters', huck_finn_chapters))

counts = Table().with_columns([
        'Jim', np.char.count(huck_finn_chapters, 'Jim'),
        'Tom', np.char.count(huck_finn_chapters, 'Tom'),
        'Huck', np.char.count(huck_finn_chapters, 'Huck')
    ])

cum_counts = counts.cumsum().with_column('Chapter', np.arange(1,44,1))
cum_counts.plot(column_for_xticks=3)
plots.title('Cumulative Number of Times Each Name Appears', y=1.08)

# Added to display the graph of the plots defined above
plots.show()

# Added print() method to display the results from the example
print(Table().with_column('Chapters', little_women_chapters))

counts = Table().with_columns([
        'Amy', np.char.count(little_women_chapters, 'Amy'),
        'Beth', np.char.count(little_women_chapters, 'Beth'),
        'Jo', np.char.count(little_women_chapters, 'Jo'),
        'Meg', np.char.count(little_women_chapters, 'Meg'),
        'Laurie', np.char.count(little_women_chapters, 'Laurie'),

    ])

cum_counts = counts.cumsum().with_column('Chapter', np.arange(1, 48, 1))
cum_counts.plot(column_for_xticks=5)
plots.title('Cumulative Number of Times Each Name Appears', y=1.08);

# Added to display the graph of the plots defined above
plots.show()

chars_periods_huck_finn = Table().with_columns([
        'Huck Finn Chapter Length', [len(s) for s in huck_finn_chapters],
        'Number of Periods', np.char.count(huck_finn_chapters, '.')
    ])
chars_periods_little_women = Table().with_columns([
        'Little Women Chapter Length', [len(s) for s in little_women_chapters],
        'Number of Periods', np.char.count(little_women_chapters, '.')
    ])


plots.figure(figsize=(6, 6))
plots.scatter(chars_periods_huck_finn.column(1),
            chars_periods_huck_finn.column(0),
            color='darkblue')
plots.scatter(chars_periods_little_women.column(1),
                chars_periods_little_women.column(0),
                color='gold')
plots.xlabel('Number of periods in chapter')
plots.ylabel('Number of characters in chapter')

# Added to display the graph of the plots defined above
plots.show()