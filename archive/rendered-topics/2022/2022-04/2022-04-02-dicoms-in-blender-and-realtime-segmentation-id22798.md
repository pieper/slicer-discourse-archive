---
topic_id: 22798
title: "Dicoms In Blender And Realtime Segmentation"
date: 2022-04-02
url: https://discourse.slicer.org/t/22798
---

# .dicoms in Blender and realtime segmentation

**Topic ID**: 22798
**Date**: 2022-04-02
**URL**: https://discourse.slicer.org/t/dicoms-in-blender-and-realtime-segmentation/22798

---

## Post #1 by @Melodicpinpon (2022-04-02 10:37 UTC)

<p>I was wondering if the dicom-viewers were able to move the visible domain in real time as in this video:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://www.linkedin.com/feed/update/urn:li:activity:6915967013798518784">
  <header class="source">
      <img src="https://static-exp1.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" class="site-icon" width="64" height="64">

      <a href="https://www.linkedin.com/feed/update/urn:li:activity:6915967013798518784" target="_blank" rel="noopener nofollow ugc">linkedin.com</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/388;"><img src="https://media-exp1.licdn.com/dms/image/C5605AQG1G0V5lH6Jkw/videocover-high/0/1648895009565?e=2147483647&amp;v=beta&amp;t=kX3i260Wf6pOr03dU7dBe1ya6EVyCzHQpyCzXgY9bZE" class="thumbnail" width="690" height="388"></div>

<h3><a href="https://www.linkedin.com/feed/update/urn:li:activity:6915967013798518784" target="_blank" rel="noopener nofollow ugc">Z-Anatomy on LinkedIn: Dicom Blender</a></h3>

  <p>.DICOM

Although the .dicom (https://lnkd.in/gPvEJygt) used by 'BodyParts3D' to create the open source human models could not be found, it may be good ...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #2 by @lassoan (2022-04-02 13:07 UTC)

<p>By “move the visible domain” do you mean you want to show the slice view in 3D or you want to crop the volume?</p>
<p>Clinical DICOM viewers are mostly 2D - showing only the acquired image slices. More advanced viewers (which are typically not just viewers but analysis, quantification, planning applications) can slice through the volume and show the slices in 3D.</p>
<p>Are you thinking about implementing your anatomy viewer based on a “DICOM viewer”? That would make sense if you want it to be useful for training of medical students, who will mostly interact with DICOM viewers in their career. Which platform(s) you want it to run it on - desktop, web, or virtual reality?</p>

---

## Post #3 by @Melodicpinpon (2022-04-02 13:30 UTC)

<p>Not really, this is just a trick that I found after trying to use the ‘Orthogonblender’ without much success.</p>
<p>If I had the .dicom used as reference for the 3D model of the open source atlas, I would add it in the file, and if I ever work on an animal model, I would probably try to add at least the cranium with this kind of technique.</p>
<p>But I do not code and trying to make a decent open 3D atlas based on the new edition of the Terminologia Anatomica is already much work for one person.</p>

---
