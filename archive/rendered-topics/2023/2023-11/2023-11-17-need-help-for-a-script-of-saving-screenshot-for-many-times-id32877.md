---
topic_id: 32877
title: "Need Help For A Script Of Saving Screenshot For Many Times"
date: 2023-11-17
url: https://discourse.slicer.org/t/32877
---

# Need help for a script of saving screenshot for many times

**Topic ID**: 32877
**Date**: 2023-11-17
**URL**: https://discourse.slicer.org/t/need-help-for-a-script-of-saving-screenshot-for-many-times/32877

---

## Post #1 by @jp_jp_jp (2023-11-17 15:57 UTC)

<p>Hi, I am working on this red slice<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f998821d88714c4f6f430911bd9c56ffb0887ab2.png" data-download-href="/uploads/short-url/zC1DwTe1kS5i3rP2ZNTwVmp7KSe.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f998821d88714c4f6f430911bd9c56ffb0887ab2.png" alt="image" data-base62-sha1="zC1DwTe1kS5i3rP2ZNTwVmp7KSe" width="690" height="18" data-dominant-color="984941"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">733×20 1.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
The range is from -500mm to 500mm, and all I know is I can save it by clicking Annotation Screenshot, and choosing Red Slice View<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/25d7e8c59764089530c926be8ef4ce8263e20fe7.png" alt="image" data-base62-sha1="5oMfuvQro3Uc9TD1YPzbdx3rmHJ" width="40" height="61"><br>
It would be great if someone could provide a Python script to save the Red Slice every 10 mm as png in an absolute directory, for example, C:\Users\jp1234\Documents</p>
<p>Thank you!</p>

---

## Post #2 by @rbumm (2023-11-17 21:44 UTC)

<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#save-a-series-of-images-from-a-slice-view">This snippet from the repository should get you started …</a></p>

---

## Post #3 by @jp_jp_jp (2023-11-17 22:21 UTC)

<aside class="quote no-group" data-username="jp_jp_jp" data-post="1" data-topic="32877">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/c77e96/48.png" class="avatar"> jp_jp_jp:</div>
<blockquote>
<p>The range is from -500mm to 500mm, and all I know is I can save it by clicking Annotation Screenshot, and choosing Red Slice View<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/25d7e8c59764089530c926be8ef4ce8263e20fe7.png" alt="image" data-base62-sha1="5oMfuvQro3Uc9TD1YPzbdx3rmHJ" width="40" height="61"><br>
It would be great if someone could provide a Python script to save the Red Slice every 10 mm as png in an absolute directory, for example, C:\Users\jp1234\Documents</p>
</blockquote>
</aside>
<p>Thanks, I created this one, and copied it to the Python Console, but nothing shows up</p>
<pre><code class="lang-auto">layoutName = "Red"
imagePathPattern = "C:/Users/jp1234/Documents/red_slice-%03d.png"
startOffset = -10
endOffset = 50
stepSize = 10

widget = slicer.app.layoutManager().sliceWidget(layoutName)
view = widget.sliceView()
logic = widget.sliceLogic()
bounds = [0,]*6
logic.GetSliceBounds(bounds)

currentOffset = startOffset
stepCount = 0

while currentOffset &lt;= endOffset:
    logic.SetSliceOffset(currentOffset)
    view.forceRender()
    image = view.grab().toImage()
    image.save(imagePathPattern % stepCount)
    
    currentOffset += stepSize
    stepCount += 1
</code></pre>
<p>then I tried the example, but [Qt] QPixmap::grabWidget is deprecated, use QWidget::grab() instead</p>
<p>so I use this</p>
<pre><code class="lang-auto">img = qt.QWidget.grab(slicer.util.mainWindow()).toImage()
img.save("C:/Users/jp1234/Documents/red_slice-%03d.png")
</code></pre>
<p>Still nothing shows up</p>

---

## Post #4 by @rbumm (2023-11-18 09:35 UTC)

<aside class="quote no-group" data-username="jp_jp_jp" data-post="1" data-topic="32877" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/c77e96/48.png" class="avatar"> jp_jp_jp:</div>
<blockquote>
<p>Hi, I am working on this red slice</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f998821d88714c4f6f430911bd9c56ffb0887ab2.png" data-download-href="/uploads/short-url/zC1DwTe1kS5i3rP2ZNTwVmp7KSe.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f998821d88714c4f6f430911bd9c56ffb0887ab2.png" alt="image" data-base62-sha1="zC1DwTe1kS5i3rP2ZNTwVmp7KSe" width="690" height="18" data-dominant-color="984941"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">733×20 1.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The range is from -500mm to 500mm, and all I know is I can save it by clicking Annotation Screenshot, and choosing Red Slice View<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/25d7e8c59764089530c926be8ef4ce8263e20fe7.png" alt="image" data-base62-sha1="5oMfuvQro3Uc9TD1YPzbdx3rmHJ" width="40" height="61"><br>
It would be great if someone could provide a Python script to save the Red Slice every 10 mm as png in an absolute directory, for example, C:\Users\jp1234\Documents</p>
<p>Thank you!</p>
</blockquote>
</aside>
<p>ChatGPT is here to help:-)</p>
<p><a href="https://chat.openai.com/share/b43f0fe7-44c3-49a5-afad-fffa27d1c5aa" class="onebox" target="_blank" rel="noopener nofollow ugc">https://chat.openai.com/share/b43f0fe7-44c3-49a5-afad-fffa27d1c5aa</a></p>
<p>The last code iteration works:</p>
<pre><code class="lang-auto">import os
import slicer

# Define the directory to save images
output_directory = "C:/Users/yourname/Documents/SlicerOutput"
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Define the range and step size
start = -500
end = 500
step = 10

# Get the Red Slice widget
red_logic = slicer.app.layoutManager().sliceWidget("Red").sliceLogic()

# Function to take and save screenshot
def saveScreenshot(sliceLogic, filename):
    layoutManager = slicer.app.layoutManager()
    sliceNode = sliceLogic.GetSliceNode()
    sliceView = layoutManager.sliceWidget(sliceNode.GetLayoutName()).sliceView()
    sliceView.forceRender()
    w2i = vtk.vtkWindowToImageFilter()
    w2i.SetInput(sliceView.renderWindow())
    w2i.Update()
    writer = vtk.vtkPNGWriter()
    writer.SetFileName(filename)
    writer.SetInputConnection(w2i.GetOutputPort())
    writer.Write()

# Iterate over the range and save images
for position in range(start, end + 1, step):
    # Set the slice offset
    red_logic.SetSliceOffset(position)

    # Define the file path
    filename = f"Red_Slice_{position}mm.png"
    filepath = os.path.join(output_directory, filename)

    # Save the screenshot
    saveScreenshot(red_logic, filepath)

    # Optional: Print the file path to confirm saving
    print("Saved:", filepath)

print("All slices saved successfully.")

</code></pre>

---
