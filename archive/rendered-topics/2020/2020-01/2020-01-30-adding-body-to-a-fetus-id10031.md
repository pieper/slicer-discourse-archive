---
topic_id: 10031
title: "Adding Body To A Fetus"
date: 2020-01-30
url: https://discourse.slicer.org/t/10031
---

# Adding body to a Fetus

**Topic ID**: 10031
**Date**: 2020-01-30
**URL**: https://discourse.slicer.org/t/adding-body-to-a-fetus/10031

---

## Post #1 by @Pieter (2020-01-30 16:24 UTC)

<p>HI there, I have these fetus rendering but I am trying to close the head of the fetus so it is not just a face mask but a closed scull. IT does not have to be a complete head but at least something that is closed and looks nice for 3D printing. The draw function does not want to work.</p>

---

## Post #2 by @Pieter (2020-01-30 17:54 UTC)

<p>Hi there,</p>
<p>I have done a face of an ultrasound file but my issue is I would like to close the head of the image. I tried the paint function but for some reason it does not want to work.</p>
<p>If I can close the head in a semi good way, export it as STL and then edit that image to look presentable then I’ll be happy but I cannot add anything to the image.</p>
<p>Is there something I am doing wrong?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/292249af643b077e3ff019451099bc6259837d69.png" data-download-href="/uploads/short-url/5RT2kEsSGnCEwsV7a0t1LMlODfH.png?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/292249af643b077e3ff019451099bc6259837d69_2_690x496.png" alt="1" data-base62-sha1="5RT2kEsSGnCEwsV7a0t1LMlODfH" width="690" height="496" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/292249af643b077e3ff019451099bc6259837d69_2_690x496.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/292249af643b077e3ff019451099bc6259837d69_2_1035x744.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/292249af643b077e3ff019451099bc6259837d69.png 2x" data-dominant-color="7E849F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1239×892 191 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @lassoan (2020-01-30 20:00 UTC)

<p>You can use Crop volume module to crop and/or enlarge the original ultrasound volume to make it large enough to contain the entire shape you want to paint.</p>
<p>A proven solution for creating aesthetically pleasing, complete fetus models from ultrasound is to take an existing generic fetus model and replace face/hand/feet surfaces obtained from the ultrasound image. You can create the real models in Slicer but it is better to use a 3D modelling/sculpting software (such as Blender) to combine the models.</p>

---
