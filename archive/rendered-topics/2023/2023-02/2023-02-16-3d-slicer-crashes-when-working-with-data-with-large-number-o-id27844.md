---
topic_id: 27844
title: "3D Slicer Crashes When Working With Data With Large Number O"
date: 2023-02-16
url: https://discourse.slicer.org/t/27844
---

# 3D Slicer Crashes When Working With Data With Large Number of Slices

**Topic ID**: 27844
**Date**: 2023-02-16
**URL**: https://discourse.slicer.org/t/3d-slicer-crashes-when-working-with-data-with-large-number-of-slices/27844

---

## Post #1 by @Russell_Engelman (2023-02-16 04:32 UTC)

<p>I recently tried to download a dataset from MorphoSource (<a href="https://www.morphosource.org/concern/media/000084459?locale=en" rel="noopener nofollow ugc">https://www.morphosource.org/concern/media/000084459?locale=en</a>) to segment in 3D Slicer. The dataset is very large and I am trying to export a surface mesh of the data. However, when I try to threshold the image stack in Slicer the program invariably crashes. Specifically, I can threshold the model, but when I try to view the 3D volume or save it the program becomes unresponsive and crashes. My workflow is simply “load model → open segmentation module → threshhold → try to do something with threshholded image → crash”.</p>
<p>Notably, this dataset (~5 gB) is much smaller than others I have successfully loaded on this computer, and when I try to load the same data into Avizo/Amira the latter program will not load the image stack at all. It doesn’t even crash, the dataset or its loading screen just fails to appear.</p>
<p>The only thing I can think of is this image stack has more than 2000 slices. I remember reading that there is an issue in Avizo/Amira where if an image stack is more than 2000 images the program will fail to load it as it can only consider &lt; 2000 slices at once (and I have had similar issues with scans over 2000 slices there). I was wondering if 3D Slicer has a similar issue?</p>
<p>Has anyone had this issue or know how to resolve it?</p>

---

## Post #2 by @hherhold (2023-02-16 11:18 UTC)

<p>I’m going to have to double check some datasets, but I’m pretty sure I’ve loaded more than a few stacks (micro-CT volumes) with more than 2000 slices. I’m not aware of any such limitation in Slicer.</p>
<p>What are your system’s specs (RAM, GPU, etc)?</p>

---

## Post #3 by @muratmaga (2023-02-16 17:37 UTC)

<p><a class="mention" href="/u/russell_engelman">@Russell_Engelman</a></p>
<p>I have successfully loaded the dataset with ImageStacks at full resolution, see the screen capture below.</p>
<p>Apart from a weirdly reconstructed dataset (like circular cropping of the dentition), there is nothing wrong with the data. However, it is big. It is not 5.2GB (that’s the size of the compressed stack), but 8GB (see the outputsize in the screenshot). So you will need a GPU with at least 8GB of GPU RAM to visualize this in slicer. Otherwise it might not render (although it shouldn’t crash). Likewise, if you are going to segment this dataset you will need 64-80GB of RAM. Again, Slicer is only constrained by the available resources of the computer, there is no limit to slice number.</p>
<p>If you do not have such resources available to you, try importing the dataset as “half resolution”, or try setting a ROI to only import the region you are interested (eg., individual molars).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9bfbb346c0ae3f62ea951f4b66c13562c428b8a4.jpeg" data-download-href="/uploads/short-url/mfTgWEe3alYCjwg2KuNUNqIWPEU.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9bfbb346c0ae3f62ea951f4b66c13562c428b8a4_2_690x362.jpeg" alt="image" data-base62-sha1="mfTgWEe3alYCjwg2KuNUNqIWPEU" width="690" height="362" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9bfbb346c0ae3f62ea951f4b66c13562c428b8a4_2_690x362.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9bfbb346c0ae3f62ea951f4b66c13562c428b8a4_2_1035x543.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9bfbb346c0ae3f62ea951f4b66c13562c428b8a4_2_1380x724.jpeg 2x" data-dominant-color="9D9DA7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1637×861 148 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2023-02-16 19:19 UTC)

<p><a class="mention" href="/u/russell_engelman">@Russell_Engelman</a> How much physical RAM do you have in your computer and how much virtual memory have you configured in your system?</p>

---

## Post #5 by @Russell_Engelman (2023-02-20 02:07 UTC)

<p>Okay, I was able to check my system specs.</p>
<p>Windows 10<br>
Processor = Intel(R) Xeon(R) CPU E3-1505M v5 @ 2.80GHz   2.81 GHz<br>
Installed RAM = 64.0 GB (63.9 GB usable)<br>
System type = 64-bit operating system, x64-based processor</p>
<p>Based on this, it’s kind of surprising the dataset wouldn’t load, even though it would be bigger than expected. I still think the suggestions of it being a likely memory issue are correct.</p>

---

## Post #6 by @muratmaga (2023-02-20 04:28 UTC)

<p>I tried segmenting this dataset with our lab computer, which has heaps of RAM, and it worked fine. Most of the slowness of the operation comes from visualizing the 3D model. So if you disable it (until you are ready to export, or need to use a segmentation effect like scissors that require 3D model), you will get better performance.</p>
<p>However, the transient memory usage went as high as 68GB during segmentaiton, which can be the reason for your crash. Please set up sufficient virtual memory (probably at least 32GB) and on it shouldn’t crash anymore (e.g., during scissors operations memory usage went as high as 80GB).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d244b0f71236ea3d417f22a57c11fbbdc375a75d.png" data-download-href="/uploads/short-url/u07re8uAq5uw0HjQ8pNqgUVYpdz.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d244b0f71236ea3d417f22a57c11fbbdc375a75d_2_690x432.png" alt="image" data-base62-sha1="u07re8uAq5uw0HjQ8pNqgUVYpdz" width="690" height="432" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d244b0f71236ea3d417f22a57c11fbbdc375a75d_2_690x432.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d244b0f71236ea3d417f22a57c11fbbdc375a75d_2_1035x648.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d244b0f71236ea3d417f22a57c11fbbdc375a75d.png 2x" data-dominant-color="B2B6BF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1111×697 243 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
