---
topic_id: 3628
title: "Merge T1 Weighted Image With Tracts"
date: 2018-08-01
url: https://discourse.slicer.org/t/3628
---

# Merge T1-weighted image with tracts

**Topic ID**: 3628
**Date**: 2018-08-01
**URL**: https://discourse.slicer.org/t/merge-t1-weighted-image-with-tracts/3628

---

## Post #1 by @Vinny (2018-08-01 16:06 UTC)

<p>Hi,</p>
<p>Slicer version: 4.8.1</p>
<p>I have a T1 anatomical image and tracts both in .nii/.nii.gz formats; the tracts are coregistered and resampled into T1 space.  I’d like to merge these two images together to create a single T1 image with embedded tracts for export in .nii/.nii.gz format.  What module can I use for this?</p>
<p>Thanks,</p>
<p>Vinny</p>

---

## Post #2 by @pieper (2018-08-01 21:13 UTC)

<p>Hi -  what do you mean by merging them?  Do you want to mask the T1 or display the tracts as some kind of overlay?  How would you use the result?</p>
<p>-Steve</p>

---

## Post #3 by @Vinny (2018-08-01 23:47 UTC)

<p>Hi,</p>
<p>Like an overlay but if it’s possible to save the image as a single volume for subsequent segmentation of these tracts on commercial neuronavigation software.</p>
<p>Thanks,</p>
<p>Vinny</p>

---

## Post #4 by @lassoan (2018-08-02 07:53 UTC)

<p>Slicer can connect to Medtronic or BrainLab navigation systems and do real-time tractography in the operating room. See <a href="http://www.slicerigt.org/wp/user-tutorial/">step-by-step instructions in U-37 SlicerIGT tutorial</a>.</p>
<p>Stryker still does not have a research interface, which would allow Slicer or other software to receive real-time navigation data. If you have a Stryker system then let them know that you would like to have this feature (the more of us ask for it, the more likely they will realize that they need to offer this feature).</p>

---

## Post #5 by @Vinny (2018-08-02 10:34 UTC)

<p>Thanks for sending the links.  We use StealthNav so definitely this is doable.  For now, I’ve been importing tracts from other software into 3d Slicer.  I’d like to export a T1 volume with these embedded tracts so that I may reorient and/or segment them out in StealthNav.  Is it possible to do this type of merging?</p>
<p>Thanks,</p>
<p>Vinny</p>

---

## Post #6 by @lassoan (2018-08-02 11:32 UTC)

<p>You can easily merge two volumes in Slicer. For example, load tracts volume as labelmap volume, import it into a new Segmentation node, and use Mask volume effect in Segment Editor module to paint the tracts into the anatomical volume. If you don’t find Mask volume effect, then install SegmentEditorExtraEffects extension.</p>
<p>Of course setting up Slicer to work in the OR will provide much more flexibility, way better visualization, etc. so I would highly recommend this method instead of burning tracts into an anatomical image.</p>

---

## Post #7 by @Vinny (2018-08-02 15:47 UTC)

<p>Thanks for providing the merge methdology.  I’ll be going through the tutorial sets and will consult with my team on the feasibility of linking Slicer with our current workflow.  The features look impressive from what I’ve read.  Thanks again for your help.</p>

---

## Post #8 by @slicer365 (2021-10-21 11:39 UTC)

<p>Problem is how to connect Medtronic S7 to Slicer.<br>
I don’t konw which interface should be selected to connect the computer</p>

---

## Post #9 by @lassoan (2021-10-21 14:44 UTC)

<p>Slicer can connect to Medtronic StealthStation using StealthLink. However, StealthLink is disabled by default on clinical systems. Medtronic typically gives you a license to enable it if you set up a research agreement with them. For this you need to write a one-page proposal describing what you want to do, what support you need from Medtronic, etc. If you don’t need any help from Medtronic and you don’t want to do something extremely risky then the process is fairly simple.</p>

---

## Post #10 by @slicer365 (2021-10-21 14:52 UTC)

<p>I see ,thank you very much!</p>

---
