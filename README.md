# Photo Background Remover

A Python project that removes backgrounds from images using the `rembg` library.

## Overview 

This project uses the powerful `rembg` library to automatically detect and remove backgrounds from image files. It's useful for:
- Creating transparent PNGs from regular photos
- Batch processing images
- Product photography editing
- Profile pictures

## Features

- Automatic background removal using AI
- Supports various image formats (JPG, PNG, etc.)
- Simple command-line interface
- Error handling and status messages

## Requirements

- Python 3.7+
- rembg library
- PIL/Pillow

## Installation

1. Clone this repository:
```bash
git clone https://github.com/YOUR_USERNAME/photo-background-remover.git
cd photo-background-remover
```

2. Install dependencies:
```bash
pip install rembg pillow
```

## Usage

Edit `test_rembg.py` and update the paths:

```python
in_path = r'path/to/your/image.jpg'
out_path = r'path/to/output/image_no_bg.png'
```

Then run:
```bash
python test_rembg.py
```

The script will:
1. Read the input image
2. Remove the background
3. Save the result as a PNG file with transparency

## Output

- Input: `download.jpg`
- Output: `download_no_bg.png` (transparent background)

## Project Files

- `test_rembg.py` - Main script for removing backgrounds
- `hello.py` - Simple test file
- `firstp.py` - Additional utility file

## License

MIT License - feel free to use this project for personal or commercial purposes.

## Notes

- The first run may take longer as the model is downloaded
- The process requires a good amount of memory
- For best results, use clear images with distinct subjects
 
