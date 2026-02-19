---
topic_id: 3094
title: "Volume Rendering Vessel Segmentation Of Oct"
date: 2018-06-06
url: https://discourse.slicer.org/t/3094
---

# Volume rendering/vessel segmentation of OCT

**Topic ID**: 3094
**Date**: 2018-06-06
**URL**: https://discourse.slicer.org/t/volume-rendering-vessel-segmentation-of-oct/3094

---

## Post #1 by @Philipp.nicol (2018-06-06 17:38 UTC)

<p>Hey,</p>
<p>I’m fairly new with 3D slicer so forgive me for any stupidities. I’ve been trying to produce 3d volume renderings of OCT pullbacks (DICOM) from coronary arteries but somehow my results so far were unsatisfying. I’ve looked a lot so far but haven’t found any good advice on this. The best I got was by segmenting the vessel wall from the lumen by using the threshold but the result was very porous. Does anyone has any experience with this? It would be ideal to have an STL at the end for further usage in other applications.<br>
Thanks so much in advance!</p>

---

## Post #2 by @pieper (2018-06-06 19:20 UTC)

<p>Did you find this thread?</p><aside class="quote quote-modified" data-post="1" data-topic="494">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/65b543/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/using-3dslicer-for-optical-coherence-tomography-st-judes/494">Using 3DSlicer for Optical Coherence Tomography (St Jude's)</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi Everyone, 
I’m very new to 3D slicer, I just downloaded it to try get some 3D images for a case report but having some trouble. 
Not sure if anyone has experience in using the St Jude’s OCT system (used in cardiology for imaging inside the coronary arteries, <a href="https://www.sjm.com/optis/index.html" rel="noopener nofollow ugc">https://www.sjm.com/optis/index.html</a>). This system can export a DICOM file which I’ve then tried loading into 3DSlicer however the ‘DICOM’ importer doesn’t work, when I examine the file it comes up with: 
“Multi-frame image. If slice orie…
  </blockquote>
</aside>


---

## Post #3 by @lassoan (2018-06-06 20:33 UTC)

<p>Probably Segment editor’s “Grow from seeds” and especially “Watershed” (in SegmenEditorExtraEffects extension) will give you smooth, non-porous vessel wall. Small holes you can fill by “Smoothing” effect. Check out <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Image_Segmentation">segmentation tutorials.</a></p>
<p>We can give more specific help if you attach sample screenshots (or even better, a sample volume).</p>

---
