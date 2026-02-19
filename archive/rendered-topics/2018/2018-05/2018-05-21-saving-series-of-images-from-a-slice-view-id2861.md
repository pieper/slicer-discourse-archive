---
topic_id: 2861
title: "Saving Series Of Images From A Slice View"
date: 2018-05-21
url: https://discourse.slicer.org/t/2861
---

# Saving series of images from a Slice View

**Topic ID**: 2861
**Date**: 2018-05-21
**URL**: https://discourse.slicer.org/t/saving-series-of-images-from-a-slice-view/2861

---

## Post #1 by @Dedy_Ariansyah (2018-05-21 14:48 UTC)

<p>Hello,</p>
<p>I am trying to save a series of images from red, green, yellow slice to PNG format using the ‘execfile’ command. I am following the example from here<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Capture" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Capture</a></p>
<p>I copy and paste the code into a file and save it into the location e.g., Desktop\record.py (full path). But when I run the code in Python interactor → execfile(‘Desktop\record.py’) it throws errors</p>
<blockquote>
<p>File “”, line 1, in <br>
IOError: [Errno 2] No such file or directory: ‘C:\Users\Desktop\record.py’</p>
</blockquote>
<p>Here is the line that displayed from my Python interactor.<br>
Python 2.7.13 (default, Dec 20 2017, 00:45:45) [MSC v.1800 64 bit (AMD64)] on win32</p>
<p>I wonder if anybody can give me any hint on this issue?</p>
<p>Thanks</p>
<p>Dedy</p>

---

## Post #2 by @pieper (2018-05-21 15:20 UTC)

<p>In python you need to use forward slashes (‘c:/Users’ not ‘c:\Users’)</p>

---

## Post #3 by @lassoan (2018-05-21 15:35 UTC)

<p>Yes, <code>\</code> is an escape character, so you either have to use <code>\\</code> or <code>/</code> or indicate that it is a raw string by prefixing it with <code>r</code>. Any of these will work:</p>
<p><code>r'C:\Users\Desktop\record.py'</code><br>
<code>'C:\\Users\\Desktop\\record.py'</code><br>
<code>'C:/Users/Desktop/record.py'</code></p>
<p>Note that you can record slice sweeps into a series of png files, animated gif, or video by using ScreenCapture module. You can also use ScreenCapture module from script, for example:</p>
<pre><code>import ScreenCapture
ScreenCapture.ScreenCaptureLogic().captureSliceSweep(getNode('vtkMRMLSliceNodeRed'), -125.0, 75.0, 30, r"c:\tmp", "image_%05d.png")</code></pre>

---

## Post #4 by @Dedy_Ariansyah (2018-05-21 15:39 UTC)

<p>oh yes. I am new to python. it works . many thanks.</p>

---

## Post #5 by @Dedy_Ariansyah (2018-05-21 15:52 UTC)

<p>Hi Andras,</p>
<p>Thank you for providing this information. I’ve managed to save images from slice view in PNG format.</p>
<p>However, is it possible to save the images without background color (black)?</p>
<p>I managed to do it in Matlab by adding alpha value to zero for background color of PNG images. But, I am curious if this could be also done in Slicer?</p>
<p>Thanks</p>
<p>Dedy</p>

---

## Post #6 by @lassoan (2018-05-21 16:17 UTC)

<p>The easiest is to set the image size and zoom to include as much of the image and borders as you need.</p>
<p>Also note that this kind of exported data must not be used for further processing, only for visualization in presentations, etc. (for many reasons, including reduced bit depth, resampling, lack of image spacing information and other metadata).</p>
<p>If you use Matlab then you can run MatlabBridge extension to run Matlab functions directly from Slicer. Or, you can also use nrrdread.m function to read volumes saved in Slicer into Matlab (<a href="https://github.com/PerkLab/SlicerMatlabBridge/tree/master/MatlabCommander/commandserver">https://github.com/PerkLab/SlicerMatlabBridge/tree/master/MatlabCommander/commandserver</a>). In the long term, you may consider switching from Matlab to Python, as Python can do almost everything as Matlab can, but Python has many advantages.</p>

---
