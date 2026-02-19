---
topic_id: 36582
title: "Count Volume And Mean"
date: 2024-06-04
url: https://discourse.slicer.org/t/36582
---

# Count volume and mean

**Topic ID**: 36582
**Date**: 2024-06-04
**URL**: https://discourse.slicer.org/t/count-volume-and-mean/36582

---

## Post #1 by @Vikram (2024-06-04 01:53 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86f5d358968d88645d844b41fb725312ef432f83.png" alt="tumor heterogenios" data-base62-sha1="jfUEUDGe5vnh8duChuiQv0vNogr" width="579" height="499"><br>
Hi I have a i  printed heterogeneous tumor and sent for CT scan and pet , after received data now i want to calculate volume of air  and lattice in this CT dicom file, in this tumor there is 3 different types of lattice , that is why i want to calculate separate , lattice and volume in 3 different region , any one can please help me .</p>

---

## Post #2 by @muratmaga (2024-06-04 01:57 UTC)

<p>What you are asking is really simple.</p>
<p>We tried to explain to you a few times that you need to segment each individual structure separately (lattice, air, tumor) and then use the Segment Statistics to calculate mean/sd values within each region.</p>
<p>I think you really have to go through the segmentation tutorial to understand how you can accomplish this.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html</a></p><aside class="onebox githubfolder" data-onebox-src="https://github.com/SlicerMorph/Tutorials/tree/main/Segmentation">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerMorph/Tutorials/tree/main/Segmentation" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/SlicerMorph/Tutorials/tree/main/Segmentation" target="_blank" rel="noopener">Tutorials/Segmentation at main · SlicerMorph/Tutorials</a></h3>


  <p><span class="label1">SlicerMorph module tutorials. Contribute to SlicerMorph/Tutorials development by creating an account on GitHub.</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Vikram (2024-06-04 02:02 UTC)

<p>Yes , but this is heterogeneous tumor in this there is 3 different types area , ( three different thickness of lattice ) , I want to segment three different lattice segment area separately<br>
Thank you</p>

---

## Post #4 by @muratmaga (2024-06-04 02:11 UTC)

<p>From your screenshot I am not seeing any intensity difference in the lattice. That suggest me you will not be able to use intensity based segmentation tools (like threshold) to separate out the differences in different tumor regions.</p>
<p>If you know where your tumors are in the lattice, then you can use the manual segmentation tools (draw, paint, etc.) to outline them and then segment them into separate structures.</p>
<p>Alternatively you can try to place a few seeds in regions where you know the tumors are and then see if grow from the seeds helps to distinguish them.</p>
<p>But honestly, to my non-expert eye, that lattice seems fairly uniform to me.</p>

---

## Post #5 by @lassoan (2024-06-04 16:08 UTC)

<p>You can use the Scissors tool to divide a segment into subregions. See the <a href="https://lassoan.github.io/SlicerSegmentationRecipes/Craniotomy/">“Craniotomy” segmentation recipe</a> for step-by-step instructions.</p>

---
