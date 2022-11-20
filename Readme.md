## Emotional Speech Analyzer

A script extracting audio features from emotionally charged speech.

The following features are extracted:
- Pitch (f0 min, f0 max, and f0 mean) measured in Hz
- Intensity (min, max, and mean) measured in dB
- Jitter
- Shimmer
- Speaking rate (`number of words \ duration`)

The script uses [Parselmouth](https://parselmouth.readthedocs.io/en/latest/index.html), a python wrapper for [Praat](http://www.fon.hum.uva.nl/praat/).

### Notes
- For pitch extraction, set pitch floor is set to 75Hz, and pitch ceiling to 600Hz.
- Only local jitter is extracted. Period floor is set to 0.0001s, period ceiling to 0.02s, and maximum period factor to 1.3.
- Only local shimmer is extracted. Period floor is set to 0.0001s, period ceiling to 0.02s, maximum period factor to 1.3, and maximum amplitude factor to 1.6.
- HNR (harmonics-to-noise ratio) is calculated based on harmonicity. For harmonicity time step is set to 0.01, minimum pitch to 75Hz, silence threshold to 0.1, and number of periods per window to 1.0.

### Data
A good source of audio data for emotional speech analysis is the [MSP-Podcast corpus](https://ecs.utdallas.edu/research/researchlabs/msp-lab/MSP-Podcast.html). A handful of adapted examples can be downloaded witht he included Bash script. The examples consists of seven files, each of which illustrates a different emotional state. The transcripts of the sample files are attached.

