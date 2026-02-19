---
topic_id: 1792
title: "Unable To Load Tiff Sequence Created By Python3 Tifffile Mod"
date: 2018-01-09
url: https://discourse.slicer.org/t/1792
---

# Unable to load tiff sequence created by python3 tifffile module

**Topic ID**: 1792
**Date**: 2018-01-09
**URL**: https://discourse.slicer.org/t/unable-to-load-tiff-sequence-created-by-python3-tifffile-module/1792

---

## Post #1 by @hclai (2018-01-09 14:51 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.8.1<br>
Expected behavior: Load tiff sequence created by python3 tifffile module and render the volume<br>
Actual behavior: The loading bar shows up but the Active Volume is empty.</p>
<p>I try to create tiff sequence with python 3.4.5 on a CentOS 7 server. The py code is demonstrated as follow:</p>
<p>============================TIFF generation============================</p>
<pre><code class="lang-auto">import numpy as np
import tifffile as tiff

data = np.zeros((x_axis, y_axis, z_axis)) #just a sample
for z in range(z_axis):
  tiff.imsave(str(z)+'.tiff', data[:, :, z])
  image = tiff.imread(str(z)+'.tiff')
  print(np.array_equal(image, data[:, :, z])) #always print True
</code></pre>
<p>============================TIFF generation============================</p>
<p>The last line of the code always print True, which means that I can successfully write and load the tiff image and they are the same.</p>
<p>However, when I try to load it with Slicer, it fails. The steps I take was:</p>
<ol>
<li>Add data</li>
<li>Choose a directory and add</li>
<li>Show options and uncheck singlefile</li>
</ol>
<p>The loading bar shows up and finishes. However, the Active Volume in the Volume module is empty. I cannot select volume loaded from Volume Rendering module, either. I’m wondering where I do it wrong.</p>
<p>Thanks for answering!</p>

---

## Post #2 by @ihnorton (2018-01-09 14:55 UTC)

<aside class="quote no-group" data-username="hclai" data-post="1" data-topic="1792">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/e0b2c6/48.png" class="avatar"> hclai:</div>
<blockquote>
<p>Choose a directory and add</p>
</blockquote>
</aside>
<p>Try <code>Choose files to add</code> rather than adding directory. Also, does the file load in other software?</p>
<p>If that doesn’t work, you could upload a (small) example file for someone to look at.</p>
<p>(by the way, for code you can quote with triple-backtick: “```”`)</p>

---

## Post #3 by @lassoan (2018-01-09 15:12 UTC)

<p>See detailed instructions here: <a href="https://www.slicer.org/wiki/Documentation/4.6/FAQ#How_to_load_data_from_a_sequence_of_jpg.2C_tif.2C_or_png_files.3F">https://www.slicer.org/wiki/Documentation/4.6/FAQ#How_to_load_data_from_a_sequence_of_jpg.2C_tif.2C_or_png_files.3F</a></p>

---

## Post #4 by @hclai (2018-01-09 15:34 UTC)

<p>Thanks for your comment. I also try to open the tiff files with GIMP 2 but it doesn’t work either.<br>
I tried to upload some examples but it says tiff files are not authorized. Only jpg, png, gif is allowed.</p>
<p>I’m wondering if the data type of the numpy array should be uint16 or anything else. The original intensities are designed to be 16 bit unsigned integer. However, although I tried to modify the array to np.uint16, the output tiff files are still unreadable.</p>

---

## Post #5 by @hclai (2018-01-09 15:37 UTC)

<p>Thanks for your comment. I tried your suggestion but it also failed.<br>
There is no options for me in “Active Volume” in Volume module.</p>

---

## Post #6 by @ihnorton (2018-01-09 16:09 UTC)

<p>If the file doesn’t load in GIMP then it certainly won’t load in Slicer, unfortunately. (your code sample doesn’t run as-is so I can’t try it myself)</p>
<aside class="quote no-group" data-username="hclai" data-post="4" data-topic="1792">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/e0b2c6/48.png" class="avatar"> hclai:</div>
<blockquote>
<p>I tried to upload some examples but it says tiff files are not authorized.</p>
</blockquote>
</aside>
<p>Try dropbox, onedrive, etc and post a link.</p>

---

## Post #7 by @hclai (2018-01-10 05:26 UTC)

<p>Thanks for your help! I think I just figure it out and solve it.<br>
The data type of 3D numpy array should be “float32” so that the output image can be correctly loaded and rendered.</p>

---
