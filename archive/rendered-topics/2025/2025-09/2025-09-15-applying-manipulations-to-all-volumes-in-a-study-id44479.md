---
topic_id: 44479
title: "Applying Manipulations To All Volumes In A Study"
date: 2025-09-15
url: https://discourse.slicer.org/t/44479
---

# Applying manipulations to all volumes in a study

**Topic ID**: 44479
**Date**: 2025-09-15
**URL**: https://discourse.slicer.org/t/applying-manipulations-to-all-volumes-in-a-study/44479

---

## Post #1 by @shai-ikko (2025-09-15 14:27 UTC)

<p>Hi,</p>
<p>We’ve been working on a new modality, and at least for now, we’ve been producing a set of separate volumes in each “study” (a bit like t1 and t2 in MRI). As everything is still experimental and in development, a lot of time we need to do different kinds of editing – the most common are cropping and/or rotations. However, often we want to apply the same manipulation to all volumes in a study.</p>
<p>Other than scripting to support each type of transformation, is there a way to do this that I missed? Assuming not, are there tools that will help this scripting? (I am aware of the Subject Hierarchy, and have been using it to find all the “siblings” of a given volume).</p>
<p>Thanks!</p>

---

## Post #2 by @pieper (2025-09-15 15:10 UTC)

<p>This should already work with the Data module, if I understand your goal correctly.  Just put the related volumes in the same folder and then right click on the transform column for the folder and you can apply the transform to all of them.  I don’t think there’s anything for cropping though.  This would require some scripting ideally as a new subject hierarchy plugin.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/6091505799d58759e2db3e9e72f816550ea438fe.jpeg" data-download-href="/uploads/short-url/dMhazS5auXuIdWBiMAdQ71288yy.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/6091505799d58759e2db3e9e72f816550ea438fe_2_690x244.jpeg" alt="image" data-base62-sha1="dMhazS5auXuIdWBiMAdQ71288yy" width="690" height="244" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/6091505799d58759e2db3e9e72f816550ea438fe_2_690x244.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/6091505799d58759e2db3e9e72f816550ea438fe_2_1035x366.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/6091505799d58759e2db3e9e72f816550ea438fe_2_1380x488.jpeg 2x" data-dominant-color="CED3D8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1580×560 106 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @shai-ikko (2025-09-17 07:02 UTC)

<p>Thanks a bunch! Things are better than I thought they were, and a Subject Hierarchy Plugin is a direction I hadn’t considered.</p>

---

## Post #4 by @shai-ikko (2025-11-27 14:20 UTC)

<p>Just for completeness – when I said “crop”, I really meant “mask”, and I ended up writing the functionality of “use the same mask for all volumes in a folder” as a Segment Editor Effect, rather than a Subject Hierarchy Plugin. Basically a modified MaskVolume.</p>

---
