---
topic_id: 22981
title: "How To Increase The Segmentation Resolution"
date: 2022-04-15
url: https://discourse.slicer.org/t/22981
---

# How to increase the segmentation resolution?

**Topic ID**: 22981
**Date**: 2022-04-15
**URL**: https://discourse.slicer.org/t/how-to-increase-the-segmentation-resolution/22981

---

## Post #1 by @Makhlouf (2022-04-15 21:50 UTC)

<p>Hi everybody,</p>
<p>How can I increase the resolution of the segmentation as the default one uses large size of voxels (cubes)?</p>
<p>Is this called oversampling? how to do it without changing the volume as I need to calculate the volume afterwards?</p>
<p>Thanks,</p>

---

## Post #2 by @lassoan (2022-04-16 00:27 UTC)

<p>These instructions should help: <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#segmentation-is-not-accurate-enough" class="inline-onebox">Segment editor — 3D Slicer documentation</a></p>

---

## Post #3 by @Makhlouf (2022-04-16 20:51 UTC)

<p>Thank you so much for your reply, buddy, I really appreciate it!</p>
<p>If I want to segment a pericardial fat layer and then calculate the volume in cm3, will any of the mentioned 2 methods that you have provided me with, change the actual volume even slightly?</p>

---

## Post #4 by @lassoan (2022-04-17 03:32 UTC)

<p>Usually volume changes due to smoothing and resampling are usually below 1%. You can get the segment volume from Segment Statistics module.</p>

---

## Post #5 by @DIV (2022-04-18 06:41 UTC)

<aside class="quote no-group" data-username="Makhlouf" data-post="1" data-topic="22981">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/5fc32e/48.png" class="avatar"> Makhlouf:</div>
<blockquote>
<p>how to do it without changing the volume as I need to calculate the volume afterwards?</p>
</blockquote>
</aside>
<p>I suggest that you <em>would</em> want the volume of the segmented anatomy to change (slightly), because you want it to become more accurate!</p>
<p>On the other hand, you would want to ensure that the scaling wasn’t perturbed:  for instance, if you halved the voxel size in each of the three dimensions, then you would want 8 of the new voxels to have the same volume as 1 original voxel.  (Of course, any functionality in <em>Slicer</em> should respect this.)<br>
And you would want to avoid excessive smoothing if your object of interest contains small features that should be retained, rather than smeared away.  That is more of a judgement for you to make.</p>
<p>If you are concerned about this, then you can perform your own check by comparing the volume you got originally with the volume obtained from a refined/smoothed segmentation (or a series of progressively refined/smoothed segmentations).</p>
<p>—DIV</p>

---

## Post #6 by @Makhlouf (2022-04-18 15:31 UTC)

<p>Thank you so much guys, I really appreciate your help. That worked!</p>
<p>But I have another problem with the software on a different computer, when It comes to the step of data loading, it shows me this message.</p>
<p>“Error occurred while loading the selected files. Click ‘Show details’ button and check the application log for more information.” when I click “show details” button, It gives me this “sample 3/SER00007/IMG00001.dcm -  load failed”</p>

---

## Post #7 by @lassoan (2022-04-18 21:09 UTC)

<p>Please check if you can find any error or warning messages in the application log (menu: Help / Report a bug) and if you see any then copy it here. Make sure you <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#read-dicom-files-into-the-scene">load DICOM data with DICOM module</a> (to load DICOM data, do not use the menu: <code>File</code> → <code>Add data</code>).</p>

---
