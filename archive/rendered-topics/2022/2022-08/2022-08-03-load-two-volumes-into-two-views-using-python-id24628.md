---
topic_id: 24628
title: "Load Two Volumes Into Two Views Using Python"
date: 2022-08-03
url: https://discourse.slicer.org/t/24628
---

# Load two volumes into two views using Python

**Topic ID**: 24628
**Date**: 2022-08-03
**URL**: https://discourse.slicer.org/t/load-two-volumes-into-two-views-using-python/24628

---

## Post #1 by @bzhu (2022-08-03 22:47 UTC)

<p>Operating system: Windows<br>
Slicer version:4.11.20210226 r29738</p>
<p>I am developing a Slicer module that performs image enhancement of computed tomography volumes. Once the module is executed, I’d like to allow the user to see both the original volume and the post-processed volume. I found a previous thread of a similar request in which the response was to drag-and-drop the volume into the corresponding view.</p><aside class="quote quote-modified" data-post="1" data-topic="19638">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/dfb087/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/python-viewing-two-volumes-side-by-side-four-over-four/19638">Python viewing two volumes side by side (four over four)</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    I wanted to have two volumes that I load from dicom series to be viewed side by side separately. something like this view: 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e64cadff1111f93682da9e9edcbbb78fb84a0ecb.jpeg" data-download-href="/uploads/short-url/wRk6qpDEJuy1SLKR2gRrLp72R1V.jpeg?dl=1" title="Capture" rel="noopener nofollow ugc">[Capture]</a> 
how is the good approach to that?
  </blockquote>
</aside>

<p>This works manually. However, is there a way to do it programmatically (e.g., have the module reference a specific view in which to load the volume)?</p>
<p>Namely, to do the following 2 steps in Python code,<br>
Step 1. Configure a layout (e.g., Compare with two views)<br>
Step 2. Load two separate DICOM volumes in its own view</p>

---

## Post #2 by @pieper (2022-08-03 23:21 UTC)

<p>Same suggestion as in the post you linked: try the Compare Volumes module and then look at the code - you may be able to use the <a href="https://github.com/pieper/CompareVolumes/blob/master/CompareVolumes.py#L337"><code>viewerPerVolume</code></a> method from the logic.</p>

---
