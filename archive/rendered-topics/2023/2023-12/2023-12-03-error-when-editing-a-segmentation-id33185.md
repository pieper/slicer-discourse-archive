---
topic_id: 33185
title: "Error When Editing A Segmentation"
date: 2023-12-03
url: https://discourse.slicer.org/t/33185
---

# Error when editing a segmentation

**Topic ID**: 33185
**Date**: 2023-12-03
**URL**: https://discourse.slicer.org/t/error-when-editing-a-segmentation/33185

---

## Post #1 by @dhaughto (2023-12-03 05:40 UTC)

<p>Operating system: MAC OS M2 running Sonoma<br>
Slicer version: 5.6<br>
Expected behavior: painting and drawing will not add on to a segmentation<br>
Actual behavior: Get the following error</p>
<p>Traceback (most recent call last):<br>
File “/Applications/Slicer.app/Contents/lib/Slicer-5.4/qt-scripted-modules/SegmentEditorEffects/SegmentEditorDrawEffect.py”, line 110, in processInteractionEvents<br>
pipeline.apply()<br>
File “/Applications/Slicer.app/Contents/lib/Slicer-5.4/qt-scripted-modules/SegmentEditorEffects/SegmentEditorDrawEffect.py”, line 305, in apply<br>
self.scriptedEffect.modifySelectedSegmentByLabelmap(modifierLabelmap, slicer.qSlicerSegmentEditorAbstractEffect.ModificationModeAdd)<br>
RuntimeError: std::logic_error: vector</p>

---

## Post #2 by @muratmaga (2023-12-03 07:08 UTC)

<p>without knowing the steps leading to the error, we can’t really help you much apart from guessing.</p>
<p>Also I don’t think your slicer version is 5.6, the path shown is for Slicer 5.4</p>
<aside class="quote no-group" data-username="dhaughto" data-post="1" data-topic="33185">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/dbc845/48.png" class="avatar"> dhaughto:</div>
<blockquote>
<p>Applications/Slicer.app/Contents/lib/Slicer-5.4/q</p>
</blockquote>
</aside>
<p>Did you by any change tried to install Slicer 5.6 in the same place as 5.4?</p>

---

## Post #3 by @dhaughto (2023-12-03 15:21 UTC)

<p>Sorry I have been trying past versions to see if the error is replicable across versions but I get the same error no matter what version. I load a segmentation, and when trying to edit it in the segmentation editor I get this error with paint and draw functions. The erase function works fine on the segmentation.</p>
<p>I would rather not post the segmentations that I’m working with. Ive recently been working with the development functions but can’t see how that can be causing this error especially after trying to download it again.</p>

---

## Post #4 by @pieper (2023-12-03 15:30 UTC)

<p>The best way to get help sorting this out is to post some data and the exact steps that lead to the issue.  It doesn’t have to be any particular data, just something you can share publicly that reproduces the issue.  Sometimes the process of trying to replicate the issue on other data helps lead to the solution.</p>

---

## Post #5 by @dhaughto (2023-12-03 16:18 UTC)

<p><a href="https://drive.google.com/drive/folders/1oNu7CLEUSof-u1sBDuibiobz1K7OSaoF?usp=share_link" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/drive/folders/1oNu7CLEUSof-u1sBDuibiobz1K7OSaoF?usp=share_link</a></p>
<p>Here is some data that replicated the error. I load the segmentation and volume. Try adjust the segmentation with the draw or paint and get the following errors.</p>
<p>[FD] 2023-12-03 08:35:52.482 Slicer[3977:146752] ApplePersistenceIgnoreState: Existing state will not be touched. New state will be written to /var/folders/ky/44gy8dbj30v74d3bh0zgp35c0000gn/T/org.slicer.slicer.savedState<br>
[Qt] Populating font family aliases took 151 ms. Replace uses of missing font family “.AppleSystemUIFont” with one that exists to avoid this cost.<br>
Traceback (most recent call last):<br>
File “/Applications/Slicer.app/Contents/lib/Slicer-5.6/qt-scripted-modules/SegmentEditorEffects/SegmentEditorDrawEffect.py”, line 113, in processInteractionEvents<br>
pipeline.apply()<br>
File “/Applications/Slicer.app/Contents/lib/Slicer-5.6/qt-scripted-modules/SegmentEditorEffects/SegmentEditorDrawEffect.py”, line 307, in apply<br>
self.scriptedEffect.modifySelectedSegmentByLabelmap(modifierLabelmap, slicer.qSlicerSegmentEditorAbstractEffect.ModificationModeAdd)<br>
RuntimeError: std::logic_error: vector</p>

---

## Post #6 by @muratmaga (2023-12-03 19:01 UTC)

<aside class="quote no-group" data-username="dhaughto" data-post="5" data-topic="33185">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/dbc845/48.png" class="avatar"> dhaughto:</div>
<blockquote>
<p>Here is some data that replicated the error. I load the segmentation and volume. Try adjust the segmentation with the draw or paint and get the following errors.</p>
</blockquote>
</aside>
<p>I can replicate your issue with the same error on Mac. It appears to me for some reason conversion from the original labelmap to Slicer’s segmentation is not entirely correct. While the segments are shown, it also has some weird display issues (like it shows only in one of the viewers). I do not have this problem if I create a blank segmentation within Slicer and proceed with segmentation. Where did you create this segmentation?  Is there anohter format you can export to?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aaf5f50571da23dd8114bb52d7fa2271dec1ca29.jpeg" data-download-href="/uploads/short-url/ooo86gLoXDSudsVsiLzIAS3jnZL.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aaf5f50571da23dd8114bb52d7fa2271dec1ca29_2_506x500.jpeg" alt="image" data-base62-sha1="ooo86gLoXDSudsVsiLzIAS3jnZL" width="506" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aaf5f50571da23dd8114bb52d7fa2271dec1ca29_2_506x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aaf5f50571da23dd8114bb52d7fa2271dec1ca29_2_759x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aaf5f50571da23dd8114bb52d7fa2271dec1ca29_2_1012x1000.jpeg 2x" data-dominant-color="7A7A82"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2588×2554 818 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @dhaughto (2023-12-03 19:48 UTC)

<p>This data comes from the verse20 dataset in a nifti format. The other data I am working with, that has the same issue, is generated from a machine learning algorithm derived from the verse20 dataset also producing nifti formats segmentations.</p>

---

## Post #8 by @muratmaga (2023-12-03 19:51 UTC)

<p>I can load them labelmap as fine, and the conversion to segmentation doesn’t report an error. So, I am not sure why the resultant segmentation is not editable and generating the error. Perhaps <a class="mention" href="/u/pieper">@pieper</a> or <a class="mention" href="/u/lassoan">@lassoan</a> can chime.</p>

---

## Post #9 by @dhaughto (2023-12-03 21:03 UTC)

<p>This feature worked on this data before. Maybe with the update or because I have been working in developer mode, but I have tried turning off the developer mode and reinstalling the program but still keep getting the error.</p>

---

## Post #10 by @lassoan (2023-12-03 22:15 UTC)

<p>I see two highly unusual properties of these images:</p>
<ul>
<li>The image is turned inside out (i.e., its axes form a left-handed coordinate system). This is an error, <a href="https://discourse.slicer.org/t/how-to-handle-images-defined-in-left-handed-coordinate-system/4133/2">it is not valid NIFTI</a>. This can be fixed by resampling the volume into a right-handed coordinate system by using <code>Crop volume</code> module (using default settings, using the entire volume’s region).</li>
<li>Voxel type is float. This is not technically an error, but there should be no reason for a clinical CT to use this type, and using this voxel type for segmentation is even worse (as you need to store discrete label values). You can fix this by converting to <code>Short</code> type using <code>Cast scalar volume</code> module.</li>
</ul>
<p>Slicer should be able to cope with such images (at least it should display a warning or error when loading them), but we come across with such images so rarely that it is hard to justify investing much time into dealing with them.</p>
<p>I don’t see any errors on Windows (the segmentation is editable without any issue), so it is hard for me to investigate. <a class="mention" href="/u/muratmaga">@muratmaga</a> To narrow down the issue, could you please check if the problem is caused by the first or the second issue? Do you see the issue on linux as well?</p>

---

## Post #11 by @muratmaga (2023-12-03 23:39 UTC)

<p>Converting the labelmap first to unsigned char and then exporting as segmentation fixed the issue. I didn’t have to make any changes to the original intensity image.</p>

---

## Post #12 by @dhaughto (2023-12-04 14:14 UTC)

<p>This solution worked. I will modify the algorithm to produce these images correctly.</p>

---
