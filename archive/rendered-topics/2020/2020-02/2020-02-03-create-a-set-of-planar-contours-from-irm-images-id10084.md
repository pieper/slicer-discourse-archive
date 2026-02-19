---
topic_id: 10084
title: "Create A Set Of Planar Contours From Irm Images"
date: 2020-02-03
url: https://discourse.slicer.org/t/10084
---

# Create a set of planar contours from IRM images

**Topic ID**: 10084
**Date**: 2020-02-03
**URL**: https://discourse.slicer.org/t/create-a-set-of-planar-contours-from-irm-images/10084

---

## Post #1 by @loubna (2020-02-03 14:01 UTC)

<p>Hi every one;</p>
<p>I have some ambiguities about segmentation of IRM images in Slicer 3D. I want to get a set of planar 2D contours. If i segment the ROI using segemnt editor (manually segmentation or semi-automatically). I get as master representation labelMap. But I need the planar contours.</p>
<p>I may be need to install the slicerRt extension but what are the different steps please to segment the set of IRM images and get the set of 2D contours. (i need the planar contours as representation master and not a labelMap).</p>
<p>I found many tutorial about planar contours but with CT images, but i Have IRM images of brain. Bref I am confused between the different steps.</p>
<p>Thanks in advance for you helps</p>

---

## Post #3 by @cpinter (2020-02-04 16:15 UTC)

<aside class="quote no-group" data-username="loubna" data-post="1" data-topic="10084">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/cab0a1/48.png" class="avatar"> loubna:</div>
<blockquote>
<p>I may be need to install the slicerRt extension</p>
</blockquote>
</aside>
<p>Your hunch is right, SlicerRT has this function. It’s not that trivial, so it’s good you asked. Currently there is no built-in conversion to planar contours in Segmentations, but it is possible to do via DICOM RTSS export. Make sure you have a valid patient and study in the Data module, and have the master volume and your segmentation under the study. Right-click study, choose Export to DICOM, then make sure RT is selected as export type. The image will be re-exported (see details <a href="https://discourse.slicer.org/t/export-rtstruct-referencing-original-volume/9771">here</a>), but you will have an RTSS series. Load it in Slicer, and then you’ll have the planar contours. Let me know how it goes.</p>

---

## Post #4 by @loubna (2020-02-06 14:50 UTC)

<p>It works like charm thank you so much</p>

---

## Post #5 by @loubna (2020-04-30 09:42 UTC)

<p>How can I visualize the 3D reconstructed surface from the planar contours in 3D slicer (for exemple in 3d Slicer, we can visualize the 3D surface reconstructed from the labelMap, by clicking on view 3D which execute the marching cubes (i.e flying edges) . what about planar contours?</p>
<p>thank’s in advance</p>

---

## Post #6 by @cpinter (2020-04-30 10:49 UTC)

<p>Please create a new topic so that separate questions can be discovered more easily. Thanks</p>

---
