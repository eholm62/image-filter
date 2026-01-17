### What Does It Do?
This program repeatedly sharpens and blurs an input image such that the resulting image of each repetition becomes one frame of a video displaying the gradual degredation of the image, creating a very interesting snake-like effect.

### Dependencies
 - python-pipx

### Supported Operating Systems
 - Linux
 - Other operating systems are untested but should be possible to use with minimal effort

### Usage and Defaults
 - Navigate to the project directory
 - Execute with `pipx run main.py`
 - Follow with arguments
 - Currently only supports MP4 output
 - Output file defaults to `output.mp4`
 - ***TODO:*** Document render settings defaults and usage

### Usage Examples
 - `pipx run main.py -i input.jpg`
 - `pipx run main.py -i input.jpg -o alternative-output.mp4`

### Known Issues
 - Output files have spotty player compatibility (I recommend using mpv for playback)