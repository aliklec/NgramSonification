## Data sonification of the words "Napster" and "Spotify" over the years

<iframe width="100%" height="300" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/2041640312&color=%23ff5500&auto_play=true&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"></iframe><div style="font-size: 10px; color: #cccccc;line-break: anywhere;word-break: normal;overflow: hidden;white-space: nowrap;text-overflow: ellipsis; font-family: Interstate,Lucida Grande,Lucida Sans Unicode,Lucida Sans,Garuda,Verdana,Tahoma,sans-serif;font-weight: 100;"><a href="https://soundcloud.com/ali-kleczewski" title="Ali Kleczewski" target="_blank" style="color: #cccccc; text-decoration: none;">Ali Kleczewski</a> · <a href="https://soundcloud.com/ali-kleczewski/sonification" title="Ngram Sonification" target="_blank" style="color: #cccccc; text-decoration: none;">Ngram Sonification</a></div>

This is a sonification of the usage of words "Napster" and "Spotify" in books between 1990 and 2022, **Napster is represented by the piano** and **Spotify is represented by the violins**. The data comes from Google Ngrams (https://books.google.com/ngrams/), which tracks word frequency across Google's entire collection of scanned books and expresses frequency as a percentage of words published in a given year. The sonification is limited to the period from 1990 to 2022. The starting point was set to 1990, shortly before Napster was launched. The endpoint was set at 2022 because that is where Google Ngram data cuts off. Data was scaled and mapped to MIDI pitch notes and instruments using Michael Corey's MIDITime package (https://github.com/mikejcorey/miditime).


![ggram](https://github.com/user-attachments/assets/3aaf18f2-4f68-490d-afd9-33078c3b847d)

![midiplot](https://github.com/user-attachments/assets/406d28d0-6507-4509-9d06-ceb5428dd6ab)

## References
- https://books.google.com/ngrams/
- https://cran.r-project.org/web/packages/ngramr/
- https://github.com/mikejcorey/miditime
