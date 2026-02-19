---
topic_id: 24740
title: "How To Work On A Dicom File With Burned In Segmentation"
date: 2022-08-13
url: https://discourse.slicer.org/t/24740
---

# How to Work on a DICOM file with Burned In Segmentation 

**Topic ID**: 24740
**Date**: 2022-08-13
**URL**: https://discourse.slicer.org/t/how-to-work-on-a-dicom-file-with-burned-in-segmentation/24740

---

## Post #1 by @PrinceAla93 (2022-08-13 16:55 UTC)

<p>Hello All,<br>
I have obtained a dicom image set with the segmented objects of interest burnt in (ie: for red nucleus, the image just shows up as white around that area). I am wondering if 3D slicer can take that Burnt in data of the object, extract it, and recompile the object without the burn in. Further, could i write a python script that could extract that data?</p>
<p>I used brainlab to segment the dicom but brainlab has no way of exporting those object segmentations</p>
<p>I hope this makes sense</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2022-08-13 21:07 UTC)

<aside class="quote no-group" data-username="PrinceAla93" data-post="1" data-topic="24740">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/7ab992/48.png" class="avatar"> PrinceAla93:</div>
<blockquote>
<p>brainlab has no way of exporting those object segmentations</p>
</blockquote>
</aside>
<p>BrainLab can save segmentation as DICOM segmentation object. Slicer can load this segmentation if the <a href="https://qiicr.gitbooks.io/quantitativereporting-guide">Quantitative Reporting extension</a>. This workflow has been tested and works well.</p>
<p>You may also consider using Slicer for segmentation. There are lots of manual, semi-automatic, and fully automatic segmentation tools for all kinds of structures.</p>

---

## Post #3 by @PrinceAla93 (2022-08-13 21:15 UTC)

<p>Thank you for your response!</p>
<p>how strange, then why are the brainlab reps telling me that the only way they will allow for exporting the object segmentations is if they are burnt in.</p>
<p>Do you have a link or a resource to the workflow mentioned?</p>

---

## Post #4 by @lassoan (2022-08-13 21:21 UTC)

<p>These capabilities are described in the DICOM conformance statement of the software application: <a href="https://www.brainlab.com/dicom" class="inline-onebox">DICOM - Brainlab</a></p>
<p>See test results of DICOM segmentation object export from Brainlab and import into 3D Slicer here: <a href="https://dicom4qi.readthedocs.io/en/latest/results/seg/brainlab/" class="inline-onebox">Brainlab - DICOM4QI</a></p>

---

## Post #5 by @PrinceAla93 (2022-08-13 21:23 UTC)

<p>Thank you so much!!<br>
You may have just saved this med students research!!</p>

---
