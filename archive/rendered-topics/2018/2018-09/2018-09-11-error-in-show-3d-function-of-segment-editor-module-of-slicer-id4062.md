---
topic_id: 4062
title: "Error In Show 3D Function Of Segment Editor Module Of Slicer"
date: 2018-09-11
url: https://discourse.slicer.org/t/4062
---

# error in show 3D function of segment editor module of slicer 4.8.1  

**Topic ID**: 4062
**Date**: 2018-09-11
**URL**: https://discourse.slicer.org/t/error-in-show-3d-function-of-segment-editor-module-of-slicer-4-8-1/4062

---

## Post #1 by @Anis (2018-09-11 13:09 UTC)

<p>I have Ct data of human tooth. I am trying to create stl file for gmesh.I have constructed nrrd using a stack of 300 tomography slices using Fiji. The nrrd file is 9.2MB. I could segment the data but show 3D doesn’t work with Slicer 4.8.1 although it shows 3D for sample data downloaded for slicer.<br>
Pls help.<br>
Anis Fatima</p>

---

## Post #2 by @lassoan (2018-09-11 13:13 UTC)

<aside class="quote no-group" data-username="Anis" data-post="1" data-topic="4062">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/anis/48/3547_2.png" class="avatar"> Anis:</div>
<blockquote>
<p>show 3D doesn’t work</p>
</blockquote>
</aside>
<p>What do you do? What do you expect to happen? What happens instead?</p>
<p>Have you clicked the small box button in the top-left corner of 3D view to make sure it is in the field of view?<br>
Does it work with latest nightly Slicer version?</p>

---

## Post #3 by @Anis (2018-09-12 05:45 UTC)

<p>I am trying to create a 3D after  segmenting  the data but there is no image seen when I click show 3D. Yes I tried to center the 3D view on the screen but it didn’t work.<br>
I could get 3D when I work with sample data files like CT-chest. nrrd , MR-head.nrrd. But the image is not observed with my CT data.</p>
<p>I have not tried nightly Slicer version.</p>
<p>Anis Fatima</p>

---

## Post #4 by @Anis (2018-09-12 09:20 UTC)

<p>I have now tried nightly Slicer 4.9 with the data I had problems. 3D surface is not seen again.Also I have tried the other CT data set but could not get 3D in the window.<br>
Anis</p>

---

## Post #5 by @lassoan (2018-09-12 13:24 UTC)

<p>Could you please load your data, draw some segments on it, click Show 3D, upload the application log (menu: Help / Report a bug) to dropbox/onedrive/gdrive, and post the link here?</p>
<p>Could you take a screen capture of what you are doing, upload to dropbox/onedrive/gdrie and post the link here? (you can record screen capture using free <a href="https://screencast-o-matic.com/screen-recorder">sceencast-o-matic</a> tool)</p>

---

## Post #6 by @Anis (2018-09-14 06:27 UTC)

<p>I cannot install dropbox here.<br>
I tried gray scale modelling of my 9.2 MB stack and could see 3D. I changed the background colour to black and after zooming I got the 3D.</p>
<p>Now the problem is with full data set uploading. I have nrrd file of 624 MB. After segmentation 3D surface processing takes too long and software shows Not Responding.</p>
<p>Is there any setting for increasing the memory for processing large data?</p>
<p>Is it must to use nrrd file format. When I load tiff from the folder only the selected tiff is displayed in the axial view window. When I scroll to see other files of folder I could not see all files of the folder.</p>
<p>Regards</p>

---

## Post #7 by @lassoan (2018-09-14 15:22 UTC)

<aside class="quote no-group" data-username="Anis" data-post="6" data-topic="4062">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/anis/48/3547_2.png" class="avatar"> Anis:</div>
<blockquote>
<p>After segmentation 3D surface processing takes too long</p>
</blockquote>
</aside>
<p>Set smoothing factor to 0.0 (click the small down-arrow of the “Show 3D” button to edit smoothing factor) or temporarily turn off 3D display while editing the segmentation. This requires recent nightly version of Slicer, which has several more optimizations, which drastically improves segmentation 3D update speed compared to 4.8.1.</p>
<aside class="quote no-group" data-username="Anis" data-post="6" data-topic="4062">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/anis/48/3547_2.png" class="avatar"> Anis:</div>
<blockquote>
<p>Is it must to use nrrd file format.</p>
</blockquote>
</aside>
<p>NRRD format is not required but it is a good file format for storing 3D image data. Consumer file formats, such as jpg, png, and tiff are not well suited for medical image storage, due to low bit depth (typically up to 8 bits), lack of metadata (slice spacing, image orientation, etc.), and fragile frame management (difficult to detect missing or incorrectly ordered frames).</p>
<aside class="quote no-group" data-username="Anis" data-post="6" data-topic="4062">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/anis/48/3547_2.png" class="avatar"> Anis:</div>
<blockquote>
<p>When I load tiff from the folder only the selected tiff is displayed in the axial view window.</p>
</blockquote>
</aside>
<p>You need to disable “single” option. See this page for details: <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ#How_to_load_data_from_a_sequence_of_jpg.2C_tif.2C_or_png_files.3F" class="inline-onebox">Documentation/Nightly/FAQ - Slicer Wiki</a></p>

---
