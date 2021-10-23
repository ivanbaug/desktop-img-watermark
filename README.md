# desktop-img-watermark
Small desktop app to watermark images in python

It autoscales the text size to 10% of the image width.
Places the text in the bottom-right corner

---
## Usage example
![how to](https://ivanotes.s3.amazonaws.com/img/0032-watermark.gif)

Renders the following image:

![result](https://ivanotes.s3.amazonaws.com/img/0033-catnap.jpg)

---
## Note to myself:
- Used QtDesigner to create the basic structure of the ui
- To convert the qtDesigner file
```bash
pyside6-uic input.ui -o output.py
```
- Used the following video as reference for QtDesigner: https://www.youtube.com/watch?v=XXPNpdaK9WA