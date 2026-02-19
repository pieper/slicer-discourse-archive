---
topic_id: 28744
title: "How To Scale Dimensions Of The Segmentations To Match New Vo"
date: 2023-04-04
url: https://discourse.slicer.org/t/28744
---

# How to scale dimensions of the segmentations to match new volume image spacing

**Topic ID**: 28744
**Date**: 2023-04-04
**URL**: https://discourse.slicer.org/t/how-to-scale-dimensions-of-the-segmentations-to-match-new-volume-image-spacing/28744

---

## Post #1 by @testzj (2023-04-04 10:47 UTC)

<p>So I have run into an issue here.<br>
I started segmenting a z-stack of images and forgot to specify the volume image spacing dimensions beforehand.</p>
<p>After changing the volume to the correct images the segmentations no longer match.<br>
Is there a way to scale the label maps to match the new dimensions properly?</p>
<p>Best,<br>
a humble grad student</p>

---

## Post #2 by @lassoan (2023-04-04 13:10 UTC)

<p>To change the segmentation to match a selected volume’s geometry, you can use <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#segmentation-is-not-accurate-enough">Specify geometry</a>. You may apply some smoothing after this resampling (e.g., joint smoothing).</p>

---

## Post #3 by @jfkamhi (2023-06-19 18:59 UTC)

<p>Thank you for providing this link!  I have a similar situation - I need to change the volumes of the segmentation.  However, the specify geometry button won’t let me change each dimension separately (x, y need to be the same size but z is larger).  Do you know of a way to do this?  Thank you!</p>

---

## Post #4 by @lassoan (2023-06-19 19:16 UTC)

<p>I would recommend to use isotropic spacing - same resolution along all axes because that allows you to use all details of the segmentation for creating a smooth 3D model.</p>
<p>If for some reason you must exactly match the spacing of another volume then you can uncheck the “isotropic spacing” option in the “Segmentation geometry” window.</p>

---

## Post #5 by @capsaicin (2024-02-26 17:49 UTC)

<p>Trying to solve a similar situation… I made a segmentation on a volume with incorrect spacing information, and would like to update the spacing of the volume and segmentation to the correct values. I first changed the spacing on the volume from the “volumes” tab, then went to “specify geometry” to try to change the spacing on the segmentation, but all spacing fields are greyed out.<br>
I tried selecting the volume as source geometry in “specify geometry” then just pressing “ok” - this seems to have changed the segment’s labelmap geometry (the display changed, and the segment labelmap now shows the same spacing info as the volume) but the resulting segment does not correctly align with the volume. What step could I be missing?<br>
The initial (incorrect) spacing was 0.0015 x 0.0015 x 1, and the spacing I’m trying to change to is 0.5 x 0.5 x 1… not sure if the large scaling jump may be causing part of my issues.</p>

---

## Post #6 by @lassoan (2024-02-26 21:26 UTC)

<p>You can export the segmentation to labelmap volume, use Volume information section in Volumes module’s to change spacing, and then convert the labelmap to segmentation.</p>
<p>If you find that this removes some metadata that you want to preserve (segment terminology, layers, etc.) then an easy way is to save the segmentation into seg.nhdr file. In this file format the header and the voxel data are saved in separate files. You can use notepad or any other text editor application to modify the spacing values in the .nhdr file.</p>

---

## Post #7 by @capsaicin (2024-04-15 19:01 UTC)

<p>Thanks so much for the solutions!<br>
I tried saving to nhdr and changing the spacing value in notepad. The segmentation loads normally in Slicer, but when I tried saving it I get an error that the program has run out of memory (error message was “bad allocation”). Any ideas what the issue may be, and whether there’s a quick fix?</p>

---

## Post #8 by @lassoan (2024-04-19 04:23 UTC)

<p>If you can share the file (upload somewhere and post the link here) then we can have a look.</p>

---

## Post #9 by @capsaicin (2024-04-24 18:50 UTC)

<p><a href="https://drive.google.com/drive/folders/1kJTeN7XiqXdUiqA_FULmfAefJv7OoTR9?usp=drive_link" rel="noopener nofollow ugc">&gt;&gt;Files here&lt;&lt;</a></p>
<p>“Amaterasu-1-seg-adjust.seg.nhdr” is the file in which I changed spacing values with a text editor. The other seg.nhdr file is the original. The voxel measurements I’m trying to change to are 0.48x0.48x2μm, and the original measurements are (roughly) 0.0015x0.0015x1μm.</p>
<p>I loaded the base volume (“C1-Amaterasu-1-stack0.6x.tif”), changed the spacing values for the volume in Volume Information, then loaded the nhdr file with changed spacing. The nhdr file loaded successfully and the loaded segmentation matched up with my base volume, but when I try to save the segmentation I run into the memory error.</p>
<p>I also found that after I changed the spacing for the base volume through Volume Information, save the tiff file and load it again, the x and y values are what I changed them to (0.48μm) but the z value was somehow still 1μm… not sure if I also did something wrong here?</p>
<p>Thanks for taking the time to look through this!</p>

---

## Post #10 by @lassoan (2024-04-24 19:40 UTC)

<aside class="quote no-group" data-username="capsaicin" data-post="9" data-topic="28744">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/capsaicin/48/69489_2.png" class="avatar"> capsaicin:</div>
<blockquote>
<p>I also found that after I changed the spacing for the base volume through Volume Information, save the tiff file and load it again, the x and y values are what I changed them to (0.48μm) but the z value was somehow still 1μm… not sure if I also did something wrong here?</p>
</blockquote>
</aside>
<p>Do not use TIFF file format for 3D image storage. This file format does not have a standard way of storing 3D image geometry (origin, spacing, axis directions) or specify the anatomical coordinate system axis directions. It is expected that if you save into this format then some image geometry information will be lost. Recent Slicer Preview Releases display a warning whenever the user attempts to save 3D image in TIFF to ensure the user is aware of this information loss.</p>
<aside class="quote no-group" data-username="capsaicin" data-post="9" data-topic="28744">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/capsaicin/48/69489_2.png" class="avatar"> capsaicin:</div>
<blockquote>
<p>but when I try to save the segmentation I run into the memory error.</p>
</blockquote>
</aside>
<p>Most likely you try to cover a relatively large area with very fine spacing and so you run out of memory. If you provide a sample image data set and detailed step-by-step instructions then we can have a look.</p>

---

## Post #11 by @lassoan (2024-04-24 20:38 UTC)

<p>Also make sure your segmentation is not float or double type (<code>type</code> in the nrrd file header). If for some reason you have such a segmentation file then you can open it in a recent Slicer Preview Release and save it to automatically convert to an appropriate integer type.</p>

---

## Post #12 by @capsaicin (2024-04-24 22:53 UTC)

<p>Thanks for the tips!<br>
I ended up redoing my segmentations after changing volume info on the base image and things are working so far, so I’ll stick with this instead of trying to fix the old files for now <img src="https://emoji.discourse-cdn.com/twitter/stuck_out_tongue_closed_eyes.png?v=12" title=":stuck_out_tongue_closed_eyes:" class="emoji" alt=":stuck_out_tongue_closed_eyes:" loading="lazy" width="20" height="20"><br>
What format do you recommend for storing the 3D image? My raw images are TIFF, would the best practice in my case be to load them in Slicer, add the relevant 3D geometry data, then save them to a more suitable format?<br>
Also I checked the “type” shown in my nrrd file headers are unsigned char, is that good?<br>
Thanks!</p>

---

## Post #13 by @muratmaga (2024-04-24 23:02 UTC)

<aside class="quote no-group" data-username="capsaicin" data-post="12" data-topic="28744">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/capsaicin/48/69489_2.png" class="avatar"> capsaicin:</div>
<blockquote>
<p>My raw images are TIFF, would the best practice in my case be to load them in Slicer, add the relevant 3D geometry data, then save them to a more suitable format?</p>
</blockquote>
</aside>
<p>Yes! You should save them as NRRD, which will preserve your image header information. Also, if you do want to manipulate your TIFFs prior to saving (e.g., import only a section of the volume), you can use ImageStacks in SlicerMorph extension.</p>

---
