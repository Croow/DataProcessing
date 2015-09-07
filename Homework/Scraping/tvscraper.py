#!/usr/bin/env python
# Name: Caroline Azeau
# Student number: 10334858
'''
This script scrapes IMDB and outputs a CSV file with highest ranking tv series.
'''
import csv

from pattern.web import URL, DOM, plaintext

TARGET_URL = "http://www.imdb.com/search/title?num_votes=5000,&sort=user_rating,desc&start=1&title_type=tv_series"
BACKUP_HTML = 'tvseries.html'
OUTPUT_CSV = 'tvseries.csv'


def extract_tvseries(dom):
    '''
    Extract a list of highest ranking TV series from DOM (of IMDB page).

    Each TV series entry should contain the following fields:
    - TV Title
    - Ranking
    - Genres (comma separated if more than one)
    - Actors/actresses (comma separated if more than one)
    - Runtime (only a number!)
    '''
    series = []                             # Create list for series
    for e in dom.by_tag(".title"):
        serie = []                          # Create list for one serie
        serie.append(plaintext(e.by_tag('a')[0].content).encode('utf-8'))           # Append title of serie
        serie.append(plaintext(e.by_tag(".value")[0].content).encode('utf-8'))      # Append ranking of serie
        genres = []                                                                 # Create list for genres
        for a in e.by_tag(".genre")[:1]:                                            # Find genres of serie
            for b in a.by_tag("a"):
                genres.append(plaintext(b.content).encode('utf-8'))
        serie.append(', '.join(genres))                                             # Append genres of serie
        actors = []                                                                 # Create list for actors
        for a in e.by_tag("span.credit")[:1]:                                       # Find actors of serie
            for b in a.by_tag("a"):
                actors.append(plaintext(b.content).encode('utf-8'))
        serie.append(', '.join(actors))                                             # Append genres of serie
        if e.by_tag('.runtime'):
            serie.append(plaintext(e.by_tag('.runtime')[0].content).replace(' mins.',"").encode('utf-8'))       # If runtime is known: append runtime of serie
        else:
            serie.append('0')                                                                                   # If runtime is not known: set runtime to zero
        series.append(serie)
    return series


def save_csv(f, tvseries):
    '''
    Output a CSV file containing highest ranking TV-series.
    '''
    writer = csv.writer(f)
    writer.writerow(['Title', 'Ranking', 'Genre', 'Actors', 'Runtime'])
    for i in tvseries:
        writer.writerow(i)

    # ADD SOME CODE OF YOURSELF HERE TO WRITE THE TV-SERIES TO DISK

if __name__ == '__main__':
    # Download the HTML file
    url = URL(TARGET_URL)
    html = url.download()

    # Save a copy to disk in the current directory, this serves as an backup
    # of the original HTML, will be used in testing / grading.
    with open(BACKUP_HTML, 'wb') as f:
        f.write(html)

    # Parse the HTML file into a DOM representation
    dom = DOM(html)

    # Extract the tv series (using the function you implemented)
    tvseries = extract_tvseries(dom)

    # Write the CSV file to disk (including a header)
    with open(OUTPUT_CSV, 'wb') as output_file:
        save_csv(output_file, tvseries)