
# Uses miditime program by Michael Corey:
# https://github.com/mikejcorey/miditime


import pandas as pd
import matplotlib.pyplot as plt
from miditime.MIDITime import MIDITime

# read R output into pandas dataframe
data = pd.read_csv('output.csv')

# preview
print(data.head())
print(data.tail())

# convert years 1990-2022 to 0-32 in order to use them as beats
# e.g. 0 will be the first beat
scaled = data.copy()
scaled['Year'] = data['Year'] - 1990
print(scaled)

# set midi pitch range
minmidi = 40
maxmidi = 110

# use exponential scaling given small differences between datapoints
# see:
# https://www.geeksforgeeks.org/python-intensity-transformation-operations-on-images/
# https://rikunert.com/exponential_scaler

exponent = 0.5  # can adjust
scaled['PowerFreq'] = scaled['Frequency'] ** exponent

minval = scaled['PowerFreq'].min()
maxval = scaled['PowerFreq'].max()

scaled['MappedPitch'] = minmidi + ((scaled['PowerFreq'] - minval) * (maxmidi - minmidi)) / (maxval - minval)

# print full dataframe to see how it scaled
pd.set_option('display.max_rows', None)
print(scaled)

# now round to integers so they can be used it with midi pitches
scaled['MIDIPitch'] = scaled['MappedPitch'].round().astype(int)
print(scaled)

# separate napster and spotify data
spotify = scaled[scaled['Phrase'] == 'Spotify'][['Year', 'MIDIPitch']]
napster = scaled[scaled['Phrase'] == 'Napster'][['Year', 'MIDIPitch']]

# preview
print(napster.head())
print(spotify.head())
print(napster.tail())
print(spotify.tail())

# instantiate midi with tempo of 60 (slower makes it easier to hear the data)
mymidi = MIDITime(60, 'sonification.mid')

# now create the notes using year as beat and frequency as pitch
# NOTE:
# after some earlier testing, I found that the violin dominated the piano
# so I created different functions for each instrument
# the first one is for the violin and uses a lower velocity (loudness) and shorter beats
# this way the piano can still be heard well enough

# SPOTIFY (violin)
def createQuiet(data):
    notelist = []
    for idx, row in data.iterrows():
        # beat, pitch, velocity (loudness), duration
        notelist.append([row['Year'], row['MIDIPitch'], 70, 2])
    return notelist

# NAPSTER (piano)
def createLoud(data):
    notelist = []
    for idx, row in data.iterrows():
        notelist.append([row['Year'], row['MIDIPitch'], 125, 5])
    return notelist

SpotifyNotes = createQuiet(spotify)
NapsterNotes = createLoud(napster)

sinstrument = 40  # 40 = violin
ninstrument = 0  # 0 = piano

# add tracks with instruments and notes
mymidi.add_track(SpotifyNotes, sinstrument)  # spotify
mymidi.add_track(NapsterNotes, ninstrument)  # napster

# Save the MIDI file
mymidi.save_midi()

# plot to look at how the notes have been scaled:
# get time and midi pitch from note lists
stimes = [note[0] for note in SpotifyNotes]
spitches = [note[1] for note in SpotifyNotes]

ntimes = [note[0] for note in NapsterNotes]
npitches = [note[1] for note in NapsterNotes]

plt.figure(figsize=(10, 6))
plt.scatter(ntimes, npitches, color='red', label='Napster', alpha=0.6)
plt.scatter(stimes, spitches, color='blue', label='Spotify', alpha=0.6)


plt.xlabel("Beat (Year)")
plt.ylabel("MIDI Pitch (Frequency)")
plt.legend()
plt.grid(True)
plt.savefig('midiplot.png')
plt.close()

