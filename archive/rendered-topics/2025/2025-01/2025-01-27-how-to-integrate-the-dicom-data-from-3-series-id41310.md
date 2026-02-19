---
topic_id: 41310
title: "How To Integrate The Dicom Data From 3 Series"
date: 2025-01-27
url: https://discourse.slicer.org/t/41310
---

# How to integrate the dicom data from 3 series

**Topic ID**: 41310
**Date**: 2025-01-27
**URL**: https://discourse.slicer.org/t/how-to-integrate-the-dicom-data-from-3-series/41310

---

## Post #1 by @cycycy (2025-01-27 12:15 UTC)

<p>Hello, I am trying to evaluate bone quality using the bone texture module of 3d slicer software (ver.5.6.2) from pre- and post-operative CT scans of a certain surgery.</p>
<p>However, not just with 3d slicer, but I am having trouble with axial, coronal, and sagital CT images not being displayed in series.<br>
To be more specific, dicom data a displays axial images clearly, but the resolution of coronal and sagital images becomes very low, and with dicom data b, coronal images are displayed clearly, but the resolution of axial and sagital images becomes low.<br>
I tried to integrate these using Python code, but it didn’t work.</p>
<p>I cannot post the images because they are personal information, so I think the explanation is not insufficient to understand. I am very sorry, but is there any way to integrate all of this data into a clear series?<br>
This may not be a question about 3D Slicer, but if anyone knows, I would be grateful if you could tell me.</p>

---

## Post #2 by @pieper (2025-01-28 08:00 UTC)

<p>It sounds like you have a situation that has been discussed here a lot, and the links posted here should help:</p>
<aside class="quote" data-post="1" data-topic="27089">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/audrina_fernandez/48/17933_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/merge-3-mri-volumes-with-different-orientations-into-one/27089">Merge 3 MRI volumes with different orientations into one</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi, 
I’m working on MRI to segment cheek fat volume and often I have one serie of few images for axial axe, one serie for coronal axe, one serie for sagittal axe (for one patient, one IRM). To get a better volume segmentation I would like to stitch these series. Stitch volume module can help me to match differents axes or it is for differents series of the same axe? 
Sorry for my English <img width="20" height="20" src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title="slight_smile" alt="slight_smile" class="emoji">
  </blockquote>
</aside>

<p>Usually a CT has one high-res series (axial) and sometimes low resolution reconstructions for convenience.  Perhaps you just need to look for the axial with the smallest slice spacing and ignore the others (if you don’t have it for some reason maybe you can request it).</p>

---

## Post #3 by @cycycy (2025-01-29 00:21 UTC)

<p>Thank you for your reply, Mr. Steve. I didn’t realize there was a similar topic. I read it, and I understanded that there is no appropriate method.<br>
Then, assuming that the highest resolution data is selected on one axis, is there a problem with the analysis using bone texture or the accuracy of the generated 3D model?<br>
In other words, is it only a visual problem that is difficult to see when working?<br>
I am concerned because the other two axes become very rough when creating segments.</p>

---

## Post #4 by @pieper (2025-01-29 09:12 UTC)

<p>Yes, the data is what it is in terms of resolution, so you can expect that texture measures and 3D models will be less accurate than they would be on higher resolution data.  But they may be good enough depending on your intended use.</p>

---

## Post #5 by @cycycy (2025-01-29 10:06 UTC)

<p>Thank you. I would like to verify the accuracy of my data carefully.<br>
Thank you very much for your kindness!</p>

---
