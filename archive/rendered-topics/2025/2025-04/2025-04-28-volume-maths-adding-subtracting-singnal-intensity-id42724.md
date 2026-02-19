---
topic_id: 42724
title: "Volume Maths Adding Subtracting Singnal Intensity"
date: 2025-04-28
url: https://discourse.slicer.org/t/42724
---

# Volume maths (adding, subtracting ,,, singnal intensity)

**Topic ID**: 42724
**Date**: 2025-04-28
**URL**: https://discourse.slicer.org/t/volume-maths-adding-subtracting-singnal-intensity/42724

---

## Post #1 by @Kenneth (2025-04-28 17:22 UTC)

<p>Hy. I need to ADD 2 nifti MR registered volumes (of the same size and body part) in order to have a new volume whith the higher signal intensity of each of the two volume. Each pixel must have a signal value (intensity) resulting from the sum of the signal of the corresponding voxels from the two volumes or the signal value of the image with higher signal).<br>
Same thing, but at the opposite, should happen when subtracting.<br>
I would like to avoid segmentation.</p>
<p>Thanks!</p>

---

## Post #2 by @pieper (2025-04-28 23:42 UTC)

<p>There are Add Scalar Scalar Volume and Subtract Scalar Volume modules.</p>

---

## Post #3 by @muratmaga (2025-04-29 00:17 UTC)

<aside class="quote no-group" data-username="Kenneth" data-post="1" data-topic="42724">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/94ad74/48.png" class="avatar"> Kenneth:</div>
<blockquote>
<p>I need to ADD 2 nifti MR registered volumes</p>
</blockquote>
</aside>
<p>If the volumes are registered to a common coordinate system and have exact dimensions and spacing (which should be after registration), you will probably want to do this as a numpy operation on image arrays. It will give you far more flexibility than the add/subtract scalar volumes.<br>
You can get started with simple examples in the script repository like this:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#modify-voxels-in-a-volume">
  <header class="source">

      <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#modify-voxels-in-a-volume" target="_blank" rel="noopener nofollow ugc">slicer.readthedocs.io</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#modify-voxels-in-a-volume" target="_blank" rel="noopener nofollow ugc">Script repository — 3D Slicer  documentation</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
