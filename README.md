## Data sonification of "Napster" vs. "Spotify"

https://on.soundcloud.com/QVwL7M8gyykHFw456


This is a sonification of the usage of words "Napster" and "Spotify" in books between 1990 and 2022, **Napster is represented by the piano** and **Spotify is represented by the violins**. The data comes from ![Google Ngrams](https://books.google.com/ngrams/), which tracks word frequency across Google's entire collection of scanned books and expresses frequency as a percentage of words published in a given year. The sonification is limited to the period from 1990 to 2022. The starting point was set to 1990, shortly before Napster was launched. The endpoint was set at 2022 because that is where Google Ngram data cuts off. Data was scaled and mapped to MIDI pitch notes and instruments using Michael Corey's ![MIDITime package](https://github.com/mikejcorey/miditime).
<br /> 
<br /> 

### Data before sound mapping
<br /> 


![ggram](https://github.com/user-attachments/assets/3aaf18f2-4f68-490d-afd9-33078c3b847d)

### Data after sound mapping
<br /> 

![midiplot](https://github.com/user-attachments/assets/e7a6fc89-90d8-4be7-86e0-91d4fe90d47e)


## References
- https://books.google.com/ngrams/
- https://cran.r-project.org/web/packages/ngramr/
- https://github.com/mikejcorey/miditime
