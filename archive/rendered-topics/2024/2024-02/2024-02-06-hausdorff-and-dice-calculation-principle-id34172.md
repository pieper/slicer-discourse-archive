---
topic_id: 34172
title: "Hausdorff And Dice Calculation Principle"
date: 2024-02-06
url: https://discourse.slicer.org/t/34172
---

# Hausdorff and Dice calculation principle

**Topic ID**: 34172
**Date**: 2024-02-06
**URL**: https://discourse.slicer.org/t/hausdorff-and-dice-calculation-principle/34172

---

## Post #1 by @LukasKnybel (2024-02-06 15:23 UTC)

<p>Dear Slicer Users,<br>
sorry if this question is stupid but I realize I am not sure about the principle of DICE coef or Hausdorff distance calculation (even I know the equations).</p>
<p>The question: I am comparing 2 objects, 1 is 3D segmentation, the 2nd is also 3D object but generated from 2D structures (in CT slices). Is Dice coeff. and Hausdorff distance calculated in 2D (slice by slice) or 3D as a comparison of two 3D objects?<br>
Thank you for any explanation how are these measures calculated in the background.</p>
<p>Best</p>
<p>Lukas</p>

---

## Post #2 by @cpinter (2024-02-08 10:14 UTC)

<p>Both metrics are used to compare two labelmaps. Although Hausdorff can be interpreted for any set of points, in Slicer it uses the boundary voxels of labelmaps. Dice gives you an overall score, but it is very sensitive to the shape and relative size of the object in the image, while Hausdorff provides a more balanced and human-readable result (i.e. “95% of the boundary is within 2mm”).</p>
<p>If you’re interested how Segment Comparison in SlicerRT works exactly I suggest reading the class documentations in these two classes:</p>
<aside class="onebox gitlabblob" data-onebox-src="https://gitlab.com/plastimatch/plastimatch/-/blob/master/src/util/dice_statistics.h">
  <header class="source">

      <a href="https://gitlab.com/plastimatch/plastimatch/-/blob/master/src/util/dice_statistics.h" target="_blank" rel="noopener">gitlab.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://gitlab.com/plastimatch/plastimatch/-/blob/master/src/util/dice_statistics.h" target="_blank" rel="noopener">plastimatch/plastimatch/-/blob/master/src/util/dice_statistics.h</a></h4>

  <pre><code class="lang-"></code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox gitlabblob" data-onebox-src="https://gitlab.com/plastimatch/plastimatch/-/blob/master/src/util/hausdorff_distance.h">
  <header class="source">

      <a href="https://gitlab.com/plastimatch/plastimatch/-/blob/master/src/util/hausdorff_distance.h" target="_blank" rel="noopener">gitlab.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://gitlab.com/plastimatch/plastimatch/-/blob/master/src/util/hausdorff_distance.h" target="_blank" rel="noopener">plastimatch/plastimatch/-/blob/master/src/util/hausdorff_distance.h</a></h4>

  <pre><code class="lang-"></code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @LukasKnybel (2024-02-08 12:24 UTC)

<p>Thank you!</p>
<p>Have a ncie day</p>
<p>Lukas</p>

---
