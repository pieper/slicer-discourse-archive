---
topic_id: 29686
title: "Drawing A Qrectangle In The Red Green Or Yellow Slice View W"
date: 2023-05-27
url: https://discourse.slicer.org/t/29686
---

# Drawing a QRectangle in the Red, Green, or Yellow Slice View Windows

**Topic ID**: 29686
**Date**: 2023-05-27
**URL**: https://discourse.slicer.org/t/drawing-a-qrectangle-in-the-red-green-or-yellow-slice-view-windows/29686

---

## Post #1 by @mikeT (2023-05-27 03:45 UTC)

<p>In my custom module, the user can adjust the size and position of the image capture of the RGY slice view windows. I would like to implement a button that will show the area to be captured by accessing the QPainter of the slice view window and then drawing a red rectangle in that window.</p>
<p>Here is an example of the script I have been trying to use:<br>
layoutManager = slicer.app.layoutManager()<br>
greenView = layoutManager.sliceWidget(‘Green’).sliceView()<br>
michelangelo = qt.QPainter(greenView)<br>
mPen=qt.QPen(qt.Qt.red)<br>
mPen.setWidth(5)<br>
michelangelo.setPen(mPen)<br>
michelangelo.drawRect(100,100,498,169)<br>
greenView.render()</p>
<p>Nothing shows up after running the code.</p>

---

## Post #2 by @lassoan (2023-05-28 12:09 UTC)

<p>I would recommend to draw a rectangle in a slice view using a markup ROI or plane instead.</p>

---
