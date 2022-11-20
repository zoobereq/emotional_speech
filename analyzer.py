#!/usr/bin/env python
"""A script to extract the following acousting features from an audio file:
- Pitch (minimum, maximum, and average
- Intensity (minimum, maximum, and average
- Jitter
- Shimmer
- HNR (harmonics-to-noise ratio)
- Estimated speaking rate
"""

# imports
import glob2
import parselmouth
from parselmouth.praat import call
from tabulate import tabulate


# loads the data
sound_files = glob2.glob("*.wav")


# gets the correct transcript
def get_transcript(path: str, file_name: str) -> str:
    transcription = ""
    with open(path, "r") as source:
        for line in source:
            if line.lower().split(":")[0] == file_name:
                transcription = line.split(":")[1]
    return transcription


def main():
    first_row = [
        "Emotion",
        "Min F0",
        "Max F0",
        "Mean F0",
        "Min Int",
        "Max Int",
        "Mean Int",
        "Jitter",
        "Shimmer",
        "HNR",
        "Speaking Rate",
    ]
    table = []

    for file in sound_files:
        file_name = file.split(".")[0]
        input_sound = parselmouth.Sound(file)
        # extracts the duration
        duration = input_sound.get_total_duration()
        # extracts the pitch metrics
        pitch = call(input_sound, "To Pitch", 0.0, 75.0, 600.0)
        minF0 = call(pitch, "Get minimum", 0.0, duration, "Hertz", "Parabolic")
        maxF0 = call(pitch, "Get maximum", 0.0, duration, "Hertz", "Parabolic")
        avgF0 = call(pitch, "Get mean", 0.0, duration, "Hertz")
        # extracts the intensity metrics
        intensity = call(input_sound, "To Intensity", 75.0, 0.0)
        min_intensity = intensity.get_minimum()
        max_intensity = intensity.get_maximum()
        avg_intensity = intensity.get_average()
        # extracts jitter
        point_process = call(input_sound, "To PointProcess (periodic, cc)", 75.0, 600.0)
        jitter = call(point_process, "Get jitter (local)", 0.0, 0.0, 0.0001, 0.02, 1.3)
        # extracts shimmer
        shimmer = call(
            [input_sound, point_process],
            "Get shimmer (local)",
            0,
            0,
            0.0001,
            0.02,
            1.3,
            1.6,
        )
        # extracts HNR
        harmonicity = call(input_sound, "To Harmonicity (cc)", 0.01, 75.0, 0.1, 1.0)
        hnr = call(harmonicity, "Get mean", 0, 0)
        # extracts speaking rate
        transcript = get_transcript("transcripts.txt", file_name)
        num_words = len(transcript.split())
        speaking_rate = num_words / duration
        # assembles the table
        metrics = [
            file_name,
            round(minF0, 3),
            round(maxF0, 3),
            round(avgF0, 3),
            round(min_intensity, 3),
            round(max_intensity, 3),
            round(avg_intensity, 3),
            round(jitter, 3),
            round(shimmer, 3),
            round(hnr, 3),
            round(speaking_rate, 3),
        ]
        table.append(metrics)

    # prints the results
    print(tabulate(table, headers=first_row))


if __name__ == "__main__":
    main()
