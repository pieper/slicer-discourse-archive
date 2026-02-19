---
topic_id: 8125
title: "Data Augmentation Library For 3D Us Medical Images"
date: 2019-08-21
url: https://discourse.slicer.org/t/8125
---

# Data augmentation library for 3D (US) medical images

**Topic ID**: 8125
**Date**: 2019-08-21
**URL**: https://discourse.slicer.org/t/data-augmentation-library-for-3d-us-medical-images/8125

---

## Post #1 by @che85 (2019-08-21 17:29 UTC)

<p>Hi everyone,</p>
<p>we are working on some DeepLearning networks and we would like to do some data augmentation when exporting data from Slicer.</p>
<p>Do you guys have any plans for creating a library for supporting this kind of matter or does anyone know a good library or code chunks to start?</p>
<p>We are mainly interested in doing <code>affine</code> and <code>elastic</code> deformations as well as <code>intensity shift</code>.</p>
<p>P.S. We are using pytorch for training</p>
<p>I am thankful for any help.</p>
<p>Best<br>
Christian</p>

---

## Post #2 by @Prashant_Pandey (2019-08-21 20:27 UTC)

<p>I would check out Albumentations: <a href="https://github.com/albu/albumentations" rel="nofollow noopener">https://github.com/albu/albumentations</a><br>
Haven’t used it myself but it does elastic and affine transformations.</p>
<p>Intensity shifts should be easily implementable in Pytorch using the basic Dataset classes: <a href="https://pytorch.org/tutorials/beginner/data_loading_tutorial.html" rel="nofollow noopener">https://pytorch.org/tutorials/beginner/data_loading_tutorial.html</a></p>

---

## Post #3 by @JanWitowski (2019-08-22 01:26 UTC)

<p>As <a class="mention" href="/u/prashant_pandey">@Prashant_Pandey</a> suggested, albumentations are a good choice. I have used them with success. Alternatively, if you want to implement elastic transformations yourself, this is a good starting point: <a href="https://www.kaggle.com/bguberfain/elastic-transform-for-data-augmentation" rel="nofollow noopener">https://www.kaggle.com/bguberfain/elastic-transform-for-data-augmentation</a></p>
<p>Affine transformations (along with other standard are also part of default torchvision transforms: <a href="https://pytorch.org/docs/stable/torchvision/transforms.html" rel="nofollow noopener">https://pytorch.org/docs/stable/torchvision/transforms.html</a></p>
<p>Also, as above, I wouldn’t augment data via exporting new datasets through Slicer, but rather dynamically and randomly augmenting them through pytorch DataLoader transforms. This way you can even implement e.g. adaptive histogram equalization with randomly assigned parameters from skimage, or other interesting solutions.</p>

---

## Post #4 by @che85 (2019-08-22 14:06 UTC)

<p><a class="mention" href="/u/prashant_pandey">@Prashant_Pandey</a>, <a class="mention" href="/u/janwitowski">@JanWitowski</a> Thanks for your quick response. If I am not wrong, Albumentations doesn’t seem to do data augmentation on 3D volumetric data.</p>

---

## Post #5 by @pieper (2019-08-22 14:28 UTC)

<aside class="quote no-group" data-username="che85" data-post="4" data-topic="8125">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/che85/48/636_2.png" class="avatar"> che85:</div>
<blockquote>
<p>Albumentations doesn’t seem to do data augmentation on 3D volumetric data.</p>
</blockquote>
</aside>
<p>Yes, that’s what it looks like to me as well.  Perhaps the architecture is such that we could plug in a 3D augmentation path?  If not, perhaps follow the general style but with a 3D approach in mind (or maybe ND for that matter).</p>
<aside class="quote no-group" data-username="JanWitowski" data-post="3" data-topic="8125">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/janwitowski/48/4512_2.png" class="avatar"> JanWitowski:</div>
<blockquote>
<p>Also, as above, I wouldn’t augment data via exporting new datasets through Slicer, but rather dynamically and randomly augmenting them through pytorch DataLoader transforms.</p>
</blockquote>
</aside>
<p>Yes, for sure it would be good to follow this approach.</p>

---

## Post #6 by @Fernando (2021-03-19 10:44 UTC)

<p>This probably comes in very late, but in case someone needs this, you can use <a href="https://torchio.readthedocs.io/" rel="noopener nofollow ugc">TorchIO</a>.</p>

---
