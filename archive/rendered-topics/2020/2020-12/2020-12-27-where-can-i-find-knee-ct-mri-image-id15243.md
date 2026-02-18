# Where can I find knee CT/MRI image?

**Topic ID**: 15243
**Date**: 2020-12-27
**URL**: https://discourse.slicer.org/t/where-can-i-find-knee-ct-mri-image/15243

---

## Post #1 by @arankenny (2020-12-27 19:57 UTC)

<p>Hi, I’m a final year biomedical engineering student and have just started using 3D-Slicer for my final year project. Could anyone tell me how I import DICOM files or is there somewhere online that I can find them. I need a CT/MRI scan of a knee joint.<br>
Thanks!</p>

---

## Post #2 by @arankenny (2020-12-27 18:19 UTC)

<p>Hi, I’m just wondering how you uploaded this file to 3d slicer. I’m trying to find images of a knee joint but I’ve had no luck</p>

---

## Post #3 by @pieper (2020-12-27 19:05 UTC)

<p>I think this is a particularly nice leg scan:</p>
<aside class="quote quote-modified" data-post="1" data-topic="15157">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/nice-leg-dataset-could-be-used-for-atlas/15157">Nice leg dataset - could be used for atlas</a> <a class="badge-category__wrapper " href="/c/community/openanatomy/25"><span data-category-id="25" style="--category-badge-color: #0088CC; --category-badge-text-color: #FFFFFF; --parent-category-badge-color: #F7941D;" data-parent-category-id="12" data-drop-close="true" class="badge-category --has-parent"><span class="badge-category__name">OpenAnatomy</span></span></a>
  </div>
  <blockquote>
    Here’s <a href="https://www.dropbox.com/s/nw7xk91v7293bw8/tcga-cv-a6ju_left-leg.nrrd?dl=0">a nrrd file of a CT leg</a> at nice resolution (.7 x .7 x .3 mm) voxels. 
The link above is just the left leg, but both legs and more pelvic anatomy is available in the original DICOM data.  It is shared under a CC-by attribution license and the original is on TCIA.  Be sure to cite the data source if you use it. 
The data is for subject TCGA-CV-A6JU in the <a href="https://wiki.cancerimagingarchive.net/display/Public/TCGA-HNSC#118295898f30f3d924e54ae8bfee4fb5ac9fcb5e">TCGA-HNSC</a> collection. 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b0d714cc4c499b17d1555b125c8fb7629e0811b.jpeg" data-download-href="/uploads/short-url/fh1TaSIC80oTMGelH7FxSc5pymT.jpeg?dl=1" title="image">[image]</a>
  </blockquote>
</aside>


---

## Post #4 by @lassoan (2020-12-27 20:33 UTC)

<p>You can also use the knee atlas (available in Data Store module). The image quality is not great but the imagxomea with segmentation.</p>

---

## Post #5 by @Lagari (2021-02-23 23:05 UTC)

<p>Hi Arankenny,</p>
<p>i am looking for CT images of the knee aswell. Have you found some hidden gems that you can share?</p>
<p>Unfortunately the Knee Atlas just contains stl files made of MRI scans, which are no help to me.</p>
<p>Would appreciate it, if you have found some CT dataset of the knee/leg that you can share.<br>
(p.s. CT images outside of the CancerImagingArchive)</p>

---

## Post #6 by @pieper (2021-02-23 23:07 UTC)

<p>I like this one:</p>
<aside class="quote quote-modified" data-post="1" data-topic="15157">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/nice-leg-dataset-could-be-used-for-atlas/15157">Nice leg dataset - could be used for atlas</a> <a class="badge-category__wrapper " href="/c/community/openanatomy/25"><span data-category-id="25" style="--category-badge-color: #0088CC; --category-badge-text-color: #FFFFFF; --parent-category-badge-color: #F7941D;" data-parent-category-id="12" data-drop-close="true" class="badge-category --has-parent"><span class="badge-category__name">OpenAnatomy</span></span></a>
  </div>
  <blockquote>
    Here’s <a href="https://www.dropbox.com/s/nw7xk91v7293bw8/tcga-cv-a6ju_left-leg.nrrd?dl=0">a nrrd file of a CT leg</a> at nice resolution (.7 x .7 x .3 mm) voxels. 
The link above is just the left leg, but both legs and more pelvic anatomy is available in the original DICOM data.  It is shared under a CC-by attribution license and the original is on TCIA.  Be sure to cite the data source if you use it. 
The data is for subject TCGA-CV-A6JU in the <a href="https://wiki.cancerimagingarchive.net/display/Public/TCGA-HNSC#118295898f30f3d924e54ae8bfee4fb5ac9fcb5e">TCGA-HNSC</a> collection. 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b0d714cc4c499b17d1555b125c8fb7629e0811b.jpeg" data-download-href="/uploads/short-url/fh1TaSIC80oTMGelH7FxSc5pymT.jpeg?dl=1" title="image">[image]</a>
  </blockquote>
</aside>


---

## Post #7 by @Lagari (2021-02-23 23:27 UTC)

<p>Hi Pieper,</p>
<p>thank you for the reply.</p>
<p>But i already have that one :). Am already searching trough the Cancer Imaging Archive to find more like that. Since I want to use them to train a neural network I need some more.</p>
<p>I thought maybe arankenny had found some additional sources, since this entry is a few months old.<br>
If you know some other sources for CT images of the knee/leg, I welcome you to share them, I would appreciate it <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #8 by @rkikinis (2021-02-23 23:34 UTC)

<p><a href="https://nda.nih.gov/oai/" rel="noopener nofollow ugc">https://nda.nih.gov/oai/</a></p>

---
