---
topic_id: 23048
title: "Question About Applying Automatic Maximum Entropy On The Fdg"
date: 2022-04-20
url: https://discourse.slicer.org/t/23048
---

# Question about applying automatic maximum entropy on the FDG PET image

**Topic ID**: 23048
**Date**: 2022-04-20
**URL**: https://discourse.slicer.org/t/question-about-applying-automatic-maximum-entropy-on-the-fdg-pet-image/23048

---

## Post #1 by @Jinny_Lee (2022-04-20 11:29 UTC)

<p>Hi,</p>
<p>I’m currently working on FDG PET images to segment a tumor using automatic maximum entropy. I thought the maximum entropy would be able to automatically segment the tumor, but it selects other organs like the heart or liver from time to time.</p>
<p>I tried cropping the area of interest that only contains the tumor to prevent the selection of other organs, but it changed the minimum threshold values of the tumor depending on the location/size/area of the cropped area.</p>
<p>Does anyone know how to segment the tumor using automatic maximum entropy without selecting other organs? Please let me know if you have experienced the same problem.</p>
<p>Thank you!</p>

---

## Post #2 by @mau_igna_06 (2022-04-20 12:29 UTC)

<p>If your segmentations contains islands that should not be selected. You can use split islands effect. Calculate the centroid of each segment on segmentStatistics and use the Z value of those positions to keep only the tallest one (delete the other segments). It is not a very inteligent algorithm but it may work based on your description of the problem. You can automate all this in a scripted module</p>

---

## Post #3 by @Jinny_Lee (2022-04-21 06:17 UTC)

<p>Thanks so much for the suggestion! I’ll take a look at it. I actually started using 3D slicer just a few weeks ago, so I’m not entirely sure what you meant by a scripted modeule. Could you elaborate a little bit more?</p>

---

## Post #4 by @mau_igna_06 (2022-04-21 10:32 UTC)

<p>Please check this out:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/PerkLab/PerkLabBootcamp/blob/master/Doc/day3_2_SlicerProgramming.pptx">
  <header class="source">

      <a href="https://github.com/PerkLab/PerkLabBootcamp/blob/master/Doc/day3_2_SlicerProgramming.pptx" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/PerkLab/PerkLabBootcamp/blob/master/Doc/day3_2_SlicerProgramming.pptx" target="_blank" rel="noopener">PerkLab/PerkLabBootcamp/blob/master/Doc/day3_2_SlicerProgramming.pptx</a></h4>


  This file is binary. <a href="https://github.com/PerkLab/PerkLabBootcamp/blob/master/Doc/day3_2_SlicerProgramming.pptx" target="_blank" rel="noopener">show original</a>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
