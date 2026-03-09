# music_app.py
import streamlit as st
import numpy as np
import random
from midiutil import MIDIFile
import base64
import os

st.set_page_config(page_title="Music Generator", page_icon="🎵")

st.title("🎵 AI Music Generator")
st.markdown("---")

# Music theory
notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
scales = {
    'C Major': [0, 2, 4, 5, 7, 9, 11],
    'A Minor': [9, 11, 0, 2, 3, 5, 7],
    'G Major': [7, 9, 11, 0, 2, 4, 5],
}

# Sidebar controls
with st.sidebar:
    st.header("Settings")
    scale = st.selectbox("Scale", list(scales.keys()))
    length = st.slider("Melody Length", 4, 32, 8)
    tempo = st.slider("Tempo (BPM)", 60, 180, 120)

    generate = st.button("Generate Melody", type="primary", use_container_width=True)

# Main area
col1, col2 = st.columns(2)

if generate:
    # Generate melody
    scale_notes = scales[scale]
    melody = []

    for i in range(length):
        note_idx = random.choice(scale_notes)
        octave = 4 if random.random() < 0.8 else 5
        note = f"{notes[note_idx % 12]}{octave}"
        melody.append(note)

    # Display in columns
    with col1:
        st.subheader("Generated Melody")
        st.code(" → ".join(melody))

        # Note sequence
        st.subheader("Note Sequence")
        for i, note in enumerate(melody):
            st.text(f"Note {i + 1}: {note}")

    with col2:
        st.subheader("Visualization")

        # Simple visualization
        chart_data = []
        for note in melody:
            # Convert note to number for visualization
            note_name = note[:-1]
            octave = int(note[-1])
            note_num = notes.index(note_name) + (octave * 12)
            chart_data.append(note_num)

        st.line_chart(chart_data)

        # Create MIDI
        midi = MIDIFile(1)
        track = 0
        time = 0
        midi.addTempo(track, time, tempo)

        for i, note_str in enumerate(melody):
            note_name = note_str[:-1]
            octave = int(note_str[-1])
            pitch = 60 + (notes.index(note_name) - 3) + (octave - 4) * 12
            midi.addNote(track, 0, pitch, time + i, 1, 100)

        # Save and provide download
        midi_file = "melody.mid"
        with open(midi_file, "wb") as f:
            midi.writeFile(f)

        with open(midi_file, "rb") as f:
            midi_bytes = f.read()
            b64 = base64.b64encode(midi_bytes).decode()
            href = f'<a href="data:audio/midi;base64,{b64}" download="melody.mid">⬇️ Download MIDI</a>'
            st.markdown(href, unsafe_allow_html=True)

        os.remove(midi_file)