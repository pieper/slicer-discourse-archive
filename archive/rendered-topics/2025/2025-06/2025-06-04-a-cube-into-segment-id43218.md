---
topic_id: 43218
title: "A Cube Into Segment"
date: 2025-06-04
url: https://discourse.slicer.org/t/43218
---

# A  Cube  into segment

**Topic ID**: 43218
**Date**: 2025-06-04
**URL**: https://discourse.slicer.org/t/a-cube-into-segment/43218

---

## Post #1 by @Farah_BH (2025-06-04 14:50 UTC)

<p>Hello,I created a markup ROI node ( a cube) on a ct volume, and now I want to convert it into a visible segment on that CT volume because I want to modify it. How to do so with the simplest approach?</p>

---

## Post #2 by @chir.set (2025-06-04 15:00 UTC)

<aside class="quote no-group" data-username="Farah_BH" data-post="1" data-topic="43218">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/farah_bh/48/78099_2.png" class="avatar"> Farah_BH:</div>
<blockquote>
<p>the simplest approach</p>
</blockquote>
</aside>
<p>The simplest approach might be to use the <code>Scissors</code> tool of the <code>Segment editor</code>: <code>Fill inside/Rectangle/Symmetric</code>. The depth might be the limiting factor.</p>
<p>Alternatively, you may consider <a href="https://gitlab.com/chir-set/Tools7/-/tree/master/MarkupsToSurface?ref_type=heads" rel="noopener nofollow ugc">this module</a>.</p>

---

## Post #3 by @mikebind (2025-06-04 23:35 UTC)

<p>The SurfaceCut effect in Segment Editor Extra Effects extension also can help provide this functionality with a bit of coding (this is what I did when I needed to something similar). If you want to pursue this approach I can dig up and share some code.</p>

---

## Post #4 by @Farah_BH (2025-06-06 14:10 UTC)

<p>I was able using coding to create the cube but now I want to export it as DICOM, with the ct and RT structure,</p>

---

## Post #5 by @mikebind (2025-06-06 17:14 UTC)

<p>I’m unfortunately not very familiar with radiotherapy and haven’t used the RTStruct module at all. However, I assume exporting your cube to a usable DICOM format probably requires it to be one of the following:</p>
<ul>
<li>A scalar image volume</li>
<li>A labelmap image volume</li>
<li>A surface model</li>
<li>A segment in a segmentation</li>
</ul>
<p>I’m not sure which form your cube is in now, but it’s pretty easy to convert between any of these in Slicer.</p>
<ul>
<li>Segment → Model: Segmentations module &gt; export to model</li>
<li>Model → segment: Segmentations module &gt; import from model</li>
<li>Model → LabelMap: Model To Labelmap module</li>
<li>LabelMap → scalar image: <code>slicer.modules.volumes.logic().CreateScalarVolumeFromVolume(slicer.mrmlScene, outputvolumenode, labelmapVolumeNode)</code></li>
</ul>

---
