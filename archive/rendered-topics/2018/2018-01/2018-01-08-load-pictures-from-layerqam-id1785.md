---
topic_id: 1785
title: "Load Pictures From Layerqam"
date: 2018-01-08
url: https://discourse.slicer.org/t/1785
---

# Load pictures from LayerQam 

**Topic ID**: 1785
**Date**: 2018-01-08
**URL**: https://discourse.slicer.org/t/load-pictures-from-layerqam/1785

---

## Post #1 by @marcro (2018-01-08 14:07 UTC)

<p>Hello,</p>
<p>Im working with 3D Printing using Arcam EBM technology. In the EBM machine there is something called LayerQam, a camera that takes pictures on every layer that is melted during the build, with the main purpose to monitor porosity created in the melt pocess, I would like to load these Pictures into 3D slicer to try and make a 3D model to better visualize the porosity found. I have tried to load the Pictures but when loaded I can only make one Picture visible at the time and all the Pictures are on the same z-level. Is there a way to move the Pictures consequenlty one layer thickness for each Picture or is it some other way I can import this type of data? The Pictures are in .png format.</p>
<p>BR Marie Cronskär</p>

---

## Post #2 by @lassoan (2018-01-08 14:09 UTC)

<p>See instructions how to load a stack of png images here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ#How_to_load_data_from_a_sequence_of_jpg.2C_tif.2C_or_png_files.3F">https://www.slicer.org/wiki/Documentation/Nightly/FAQ#How_to_load_data_from_a_sequence_of_jpg.2C_tif.2C_or_png_files.3F</a></p>

---

## Post #3 by @marcro (2018-01-10 07:34 UTC)

<p>Thank you! First time it worked well but when I did the same thing again I can only have one Picture visible at the time (even though I unchecked the “single file” option). Is it some setting I have happened to change or what can the reason be? When I go to “data”, I see all the Pictures in the list but can only have one visible at the time.</p>
<p>Also, it takes a lot of time to change all the “image origin values” of all the Pictures, one at the time, but I guess that is the only way to get the spacing between the Pictures?</p>
<p>BR Marie</p>

---

## Post #4 by @lassoan (2018-01-11 04:56 UTC)

<p>It seems that you selected multiple files or a folder. Make sure you only select a single file of your image sequence. If you numbered your files consistently, Slicer will find all the corresponding files.</p>

---

## Post #5 by @marcro (2018-01-12 09:48 UTC)

<p>Ok. Now I have tried to import one picture at the time. I have also tried to give them the names 1, 2, 3… (is that what you mean by numbering the files consistently?) and only selecting the number 1 when importing but then it only imports that picture.</p>
<p>I can still only make one picture visible at the time when imported into slicer.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3e302f6fa76a52767df4aae22559cbb8f70ed4e4.jpeg" data-download-href="/uploads/short-url/8S8Q3LZY1m7Thq7He1qf7WiC5k8.JPG?dl=1" title="Skärmklipp" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3e302f6fa76a52767df4aae22559cbb8f70ed4e4_2_690x395.JPG" alt="Skärmklipp" data-base62-sha1="8S8Q3LZY1m7Thq7He1qf7WiC5k8" width="690" height="395" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3e302f6fa76a52767df4aae22559cbb8f70ed4e4_2_690x395.JPG, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3e302f6fa76a52767df4aae22559cbb8f70ed4e4_2_1035x592.JPG 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3e302f6fa76a52767df4aae22559cbb8f70ed4e4.jpeg 2x" data-dominant-color="7C7C7C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Skärmklipp</span><span class="informations">1167×669 55.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @lassoan (2018-01-12 13:01 UTC)

<p>In the “Add data…” dialog, click on “Show Options” and uncheck the “Single File” option.</p>

---

## Post #7 by @marcro (2018-01-12 13:47 UTC)

<p>I did that but it doesnt seem to work.</p>

---

## Post #8 by @lassoan (2018-01-12 15:19 UTC)

<p>To make the instructions more clear, I’ve uploaded a video:</p>
<div class="lazyYT" data-youtube-id="BcnpzYE8VO8" data-youtube-title="Load sequence of PNG files as a 3D volume into 3D Slicer" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<p>Do all the images have exactly the same size?</p>
<p>Could you go to the Volumes module and check what are the values in Volume Information section, Image Dimensions? The third value should be &gt; 1.</p>

---
