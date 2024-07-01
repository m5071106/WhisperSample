## Whisper sample program with m3, macOS 14.5, Python 3.10.14

### Directions

#### CLI (sound_trans.py on terminal)

1. Set sound source in `source` directory.
2. Run `python3 sound_trans.py [model1] [model2] ...`
   Conversion will start with models that you indicated. (models are tiny, base, small, medium, or large)
3. Conversion result is in the `result` directory.)


#### GUI (Web) (`http://[hostname]:5001/`)

1. Run `python3 front_web.py`
1. Run browser and input `http://[hostname]:5001/` to address bar.
1. Upload sound source to web, and start conversion.
1. Conversion result is on the Web.

### Installation instructions:
#### for macOS:
  1. Install homebrew (https://brew.sh/ja/)
  1. brew install python@3.10
  1. pip3 install -U openai-whisper
  1. brew install ffmpeg
  1. pip3 install ffmpeg-python
  1. pip3 install torch
  1. pip3 install torchvision
  1. pip3 install torchaudio

#### for Ubuntu:
  1. pip3 install whisper
  1. pip3 install git+https://github.com/openai/whisper.git
  1. pip3 install ffmpeg-python
  1. pip3 install -U openai-whisper
  1. sudo apt install ffmpeg (https://github.com/openai/whisper#)
  1. pip3 --no-cache-dir install torch (for avoiding process `killed` )
  1. pip3 install torchvision

#### for Windows:
  1. pip3 install -U openai-whisper
  1. Install ffmpeg (https://github.com/BtbN/FFmpeg-Builds/releases)
  1. pip3 install ffmpeg-python
  1. pip3 install torch
  1. pip3 install torchvision
  1. pip3 install torchaudio
  1. pip3 uninstall numpy # 2.0.0 is not acceptable
  1. pip3 install numpy<2
  
  
