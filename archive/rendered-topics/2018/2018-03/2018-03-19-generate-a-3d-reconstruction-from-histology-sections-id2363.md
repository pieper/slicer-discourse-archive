---
topic_id: 2363
title: "Generate A 3D Reconstruction From Histology Sections"
date: 2018-03-19
url: https://discourse.slicer.org/t/2363
---

# Generate a 3D reconstruction from histology sections

**Topic ID**: 2363
**Date**: 2018-03-19
**URL**: https://discourse.slicer.org/t/generate-a-3d-reconstruction-from-histology-sections/2363

---

## Post #1 by @hematoxylin (2018-03-19 21:17 UTC)

<p>What I ultimately want to do is create a 3D reconstruction of structure from histology sections. I have imaged the H&amp;E slides and aligned them using TrakEM2 on Fiji, and saved the files individually as TIFF files. When I open the images on Slicer, they are loaded separately and not as one volume.</p>
<p>Others on this forum have asked this question and the solution has been the following:</p>
<ol>
<li>Click on “Add Data”</li>
<li>Select one of the image</li>
<li>Click “Option” -&gt; Uncheck “Single File”</li>
</ol>
<p>However, when I try this, it still does not work.</p>
<p>I would appreciate any help in this matter. Many thanks.</p>

---

## Post #2 by @ENTresident (2018-03-19 22:11 UTC)

<p>I have a very similar problem, using Fiji and Slicer.</p>

---

## Post #3 by @lassoan (2018-03-19 22:15 UTC)

<p>The files need to have exactly the same size and named similarly (e.g., image_001, image_002,…). If you still have issues loading files then upload somewhere and copy-paste the link here so that we can try, too.</p>

---

## Post #4 by @hematoxylin (2018-03-19 22:57 UTC)

<p>That worked! Thank you Andras. You’re the man.</p>

---

## Post #5 by @ENTresident (2018-03-19 23:15 UTC)

<p>Andreas for president. Worked for everything as well, thanks.</p>

---

## Post #6 by @hematoxylin (2018-03-20 19:58 UTC)

<p>After I segment all the slides, what is the best way to create a 3-D model?</p>
<p>I tried the “show 3-d” button but the 3-d rendering is not displayed inside the pink box making it difficult to visualize the rendering. Also, it seems like the 3-d rendering is flat so I think I need to input section thickness and distance between slices somewhere, but not sure where.</p>
<p>Thank you!</p>

---

## Post #7 by @lassoan (2018-03-20 20:06 UTC)

<aside class="quote no-group" data-username="hematoxylin" data-post="6" data-topic="2363">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/74df32/48.png" class="avatar"> hematoxylin:</div>
<blockquote>
<p>3-d rendering is not displayed inside the pink box</p>
</blockquote>
</aside>
<p>Click on crosshair icon (“Center the 3D view…”) right above the 3D view to reset the box size and position.</p>
<aside class="quote no-group" data-username="hematoxylin" data-post="6" data-topic="2363">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/74df32/48.png" class="avatar"> hematoxylin:</div>
<blockquote>
<p>it seems like the 3-d rendering is flat</p>
</blockquote>
</aside>
<p>That’s why people who work with 3D imaging don’t use TIFF and similar file formats. TIFF images don’t have a standard way of storing spacing between slices. Anyway, you can specify the correct spacing value in Volumes module “Volume information” section.</p>

---

## Post #8 by @hematoxylin (2018-03-20 20:38 UTC)

<p>I know using TIFF images is not ideal, but I only have H&amp;E slides and don’t know any other way of creating a 3D reconstruction from these slides.</p>
<p>I have tried the “volume information” tab, but it does not seem to be working for the following reasons:</p>
<ol>
<li>In “volume information”, under “active volume” I am only given the option of choosing one of the tiff images. Should I be able to choose the 3-d segmentation I have created?</li>
<li>When I try changing the image spacing distances, it does not change my 3-d rendering. It only manipulates the selected images.</li>
<li>Can I input the thickness of each image?</li>
</ol>
<p>Thank you.</p>

---

## Post #9 by @lassoan (2018-03-20 21:26 UTC)

<p>When you import your image stack you must select only the first file and uncheck the Single File option. That way slices will be read into a single volume.</p>

---

## Post #10 by @hematoxylin (2018-03-20 21:40 UTC)

<p>If I choose the first file, how do I upload the rest of the images?<br>
EDIT: Nevermind, figured this out.</p>

---

## Post #11 by @hematoxylin (2018-03-20 22:45 UTC)

<p>I am still having trouble with the following:</p>
<ol>
<li>When I try changing the image spacing distances, the 3-d rendering does not change. It only causes distortion of the selected images in the red box. The distance between each section is 100 microns so where exactly do I input this value as there are 3 options for “image spacing.”</li>
<li>I want to segment all the images and then interpolate the volume between each section (ie interpolate the 100microns between each segment). How do I accomplish this?</li>
</ol>
<p>Thank you for all the help. Much appreciated it.</p>

---

## Post #12 by @muratmaga (2018-03-21 02:04 UTC)

<p>There are three values for image spacing because there are three dimensions. Your 100 micron is your slicer thickness so it goes to the z value (last field). For xy dimensions you need to measure the width of your slides and divide it by the number of pixels<br>
in in your image (unless you have rectangular pixels for some reason, you can do this only for x dimension and enter she value for the first two boxes).</p>
<p>M</p>
<p>Get <a href="https://aka.ms/ghei36" rel="nofollow noopener">Outlook for Android</a></p>

---
