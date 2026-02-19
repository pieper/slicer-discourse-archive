---
topic_id: 32956
title: "Calculating Centroid Based On Signal Intensity"
date: 2023-11-22
url: https://discourse.slicer.org/t/32956
---

# Calculating centroid based on signal intensity

**Topic ID**: 32956
**Date**: 2023-11-22
**URL**: https://discourse.slicer.org/t/calculating-centroid-based-on-signal-intensity/32956

---

## Post #1 by @ingunnev (2023-11-22 12:31 UTC)

<p>Hello!</p>
<p>I am working on a project where calculating the centroid of a segmentation based on the intensity in each voxel in the MRI-picture could be interesting. Slicer had a centroid calculation option easily available, but it only told me the geometrical centroid of a segmentation, not a centroid based on intensity.</p>
<p>I have tried (with some assistance from friends) to use the python console to extract the data (both the intensity voxels from the MRI-image, and the position of the segmentation). It didn’t seem very straightforward, so if anybody could give some guidance it would be very helpful!</p>
<p>I also looked for solutions online, but I couldn’t find anything that helps, or anybody with the same issue.</p>
<p>Best regards,<br>
Ingunn</p>

---

## Post #2 by @pieper (2023-11-22 17:36 UTC)

<p>This is a good question and thanks for asking it.  I don’t think we have an example just like that in our script repository, so rather than writing out a long description myself I tried an experiment by pasting into google’s bard tool.  The answer below is probably not exactly correct, but from a quick read it looks close.  Other tools like ChatGPT or microsoft bing would also probably do a good job and maybe if you try and then ask follow up questions you will be able to debug it.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://bard.google.com/share/fa6b4851c529">
  <header class="source">
      <img src="https://www.gstatic.com/lamda/images/favicon_v1_150160cddff7f294ce30.svg" class="site-icon" width="500" height="500">

      <a href="https://bard.google.com/share/fa6b4851c529" target="_blank" rel="noopener">bard.google.com</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/361;"><img src="https://lh3.googleusercontent.com/bard/AL4VpuNGk6rtnk6e48ndpV8XjjmDPObt1ToZfsVhmuRtpp_jZSagNxANxnSSg6JjuNjDKEpayA5it_tMNm_sMefg3LxVaMQQzKsVSPUe3tkFnoSk0RcgThlZAoNUsQK9LUfEtEXW4qzLgoEQ9ymiAnPpb2naZhVcmC8J0KY_Nt99CzkZZCCoMNSH5KFqh3fBkJ_I3ib-C3-ak6ViOaNvUNZJ4sRiZGTS_NBXmm4D_XS5cvJBpwhDy64tN6pnQ5FVDIVZbug134TsrDpOa9Q2QGE-qVJ_bMlR6Q6-GlTUL5wvMYFQZwzoWeXoLRux0owBikNYjtF5byimjheEUU4=s1200" class="thumbnail" width="690" height="361"></div>

<h3><a href="https://bard.google.com/share/fa6b4851c529" target="_blank" rel="noopener">‎In 3D Slicer: Hello!

I am working on a project where calculating the...</a></h3>

  <p>Created with Bard.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @ingunnev (2023-11-23 10:43 UTC)

<p>Thank you for your answer!<br>
I actually asked ChatGTP 3.5, but the answer seemed to lack some necessary parts for the script to work. The answer from Bard seems more extensive.<br>
I will give it a try!</p>

---
