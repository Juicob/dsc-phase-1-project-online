# Project
This project was created in order to provide insights on what direction a new movie studio should take as they enter the market. My approach to this problem was the same approach I take in my personal life. If I'm looking to do something, or buy something new, first I define my requirements, then I look at the best options in the market that meet those requirements and go from there. Recently I've been in the market for a mechanical keyboard so? Off to google, "Best Mechanical Keyboard 2020". I've recently moved to a new city and looking for looking breweries so? Off to google, "Best breweries Columbus Ohio". With the data provided and a portion that I acquired on my own, I took the same approach of identifying the best (i.e. most profitable) and using those variables as the basis of what to suggest when it comes to making a movie. 

The data provided included several .csv's and .tsv's detailing movie titles, actors, directors, gross revenue, genres, studios, ratings and reviews, as well as several platform specific ID's from platforms such as IMDB, Rotten Tomatoes, and The Movie Database. Included within the unzipped_data folder are two files I've gathered. I pulled genre names from The Movie Database API in order to maintain the integrity of genre order (to discern primary genre versus secondary, tertiary, etc.) as well as franchise statistics to investage the relationship between the number of franchise releases to gross revenue. There was a file containing the actual genre names but this file had the genre names listed in alphabetical order, whereas the file listed with the genre ID's, had the ID's listed in the order to which I believe to be primary first, then the next relevant and so on. This is why I decided to gather the genre ID to name list from the API and map them on my own versus joining the two tables. The franchise information was gathered from IMDB and because it was already in a structured format, I was able to gather it directly from Excels native tools without building a scraper. I've also scraped a list of ranked directors from IMDB with Scrapy; however, after looking further into it, I realized that this list was actually created by a user based off of their personal opinions so I didn't include it in my project and instead created my own ranking of directors based on the data I had. I'm leaving the file and Scrapy script within the repo in case someone would like a template to work off of for a similar but different problem.

# Built With

- Python
- Plotly
- Pandas
- SQLite
- Numpy
- Scrapy
- Caffeine

# Questions

- What are the most profitable movies?
- What are the most profitable genre groups?
- What are the most profitable franchises?
- Who are the most profitable directors?

# Findings

- The most profitable movies are Avatar, Titanic, and Avengers: Infinity War.
- The most profitable genre groups are "Action, Adventure, Sci-Fi", "Comedy", and "Action, Adventure, Fantasy, Sci-Fi".
- The most profitable franchises are the Marvel Cinematic Universe, Star Wars, and the Disney Live Action Reimaginings.
- The most profitable director is James Cameron, Chris Buck, and Anthony Russo.


# Final Recommendation

- Create a franchise centered around the Halo universe directed by James Cameron






