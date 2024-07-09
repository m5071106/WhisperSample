cd /d %~dp0
python3 conv_mp4_to_mp3\conv_mp4_to_mp3.py
python3 audio_splitter\audio_splitter.py
python3 sound_trans\sound_trans.py
python3 text_coordinater\text_coordinater.py
pause
