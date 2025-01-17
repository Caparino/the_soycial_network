# the soycial network

A command-line tool that creates memes from LinkedIn posts by adding soyjak reactions while censoring personal information.

## Features
- Screenshots LinkedIn embed posts
- Anonymizes profile pictures and names
- Overlays with the infamous soyjaks pointing meme

## Prerequisites
- Python 3.x
- Playwright
- Pillow (PIL)

## Installation
1. Clone this repository
```bash
git clone https://github.com/Caparino/the_soycial_network.git
cd the_soycial_network
```

2. Install dependencies:
```bash
pip install -r requirements.txt
playwright install chromium
```


## Usage
1. Get a LinkedIn post embed URL (right-click on post timestamp → "Embed this post")

2. Run the script:
```bash
python soycial_network.py "<embed-url>"
```

3. The processed image will be saved as `output.png`

## Required Files
- `soyjaks-pointing_overlay.png` - The overlay image
- `soycial_network.py` - Main script

## How It Works
1. Uses Playwright to capture a screenshot of the LinkedIn embed
2. Applies black rectangles to censor personal information
3. Crops out unnecessary UI elements
4. Overlays soyjak reactions scaled to the post
5. Saves the final meme as `output.png`

## Notes
- The script is designed for LinkedIn embed URLs, not regular LinkedIn post URLs
- Image dimensions and positioning are optimized for standard LinkedIn post layouts
