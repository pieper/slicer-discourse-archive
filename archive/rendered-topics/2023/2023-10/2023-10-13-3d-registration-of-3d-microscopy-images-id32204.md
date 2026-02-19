---
topic_id: 32204
title: "3D Registration Of 3D Microscopy Images"
date: 2023-10-13
url: https://discourse.slicer.org/t/32204
---

# 3D registration of 3D microscopy images

**Topic ID**: 32204
**Date**: 2023-10-13
**URL**: https://discourse.slicer.org/t/3d-registration-of-3d-microscopy-images/32204

---

## Post #1 by @ylcnkzy (2023-10-13 10:08 UTC)

<p>Greetings Everyone,<br>
In our lab, we have developed a methodology that allows us to stain the same sample for different biological targets at different time points, and enable us to visualize the same sample again and again after each staining session.</p>
<p>I plan to register the 3D images obtained at different time points to visualize all the markers in the same images ( in principle it’s like image registration of patients whose CT images were obtained at different time points).</p>
<p>The image file is originally .tiff (but .nii and .nrrd may also work). The size of the data now is about 100Mb -200Mb, (but in the future, it’s planned to have 50 Gb, later on).</p>
<p>I am just wondering if you have any idea how to perform it via 3D Slicer.</p>
<p>PS: I have attached <strong><a href="https://drive.google.com/drive/folders/1zTvTXgc4I0wyR_ro9riiw9ahBrfoMd-S?usp=sharing" rel="noopener nofollow ugc">two example files</a></strong>, obtained at different time points but the same markers, in case anyone wants to try registering them.<br>
I believe this may be interesting for <a class="mention" href="/u/pieper">@pieper</a>, <a class="mention" href="/u/muratmaga">@muratmaga</a> and <a class="mention" href="/u/egorzindy">@EgorZindy</a>.</p>
<p>Kind regards,</p>

---

## Post #2 by @EgorZindy (2023-10-16 15:36 UTC)

<p>Hi <a class="mention" href="/u/ylcnkzy">@ylcnkzy</a> ,</p>
<p>Thanks for tagging me, 3-D registration is something I would be super interested in as well, for example for the (fixed) cells I was showing in my <a href="https://discourse.slicer.org/t/working-on-a-czi-zeiss-microscopy-image-stack-reader-for-3d-slicer-any-help-or-advice-welcome/30769/3">CZI importer thread</a>. The idea here (if I understood correctly) is to reimage the beads with different tagged markers and then somehow apply 3-D registration to show marker colocalization.</p>
<p>I don’t have stacks to register yet, so thank you for sharing yours!</p>
<p>Just to be sure, are your two timepoints called “original” and “crop”? Are these the two stacks you want to register together?</p>
<p>In my project, I was thinking of determining the centroids of each cells / nuclei and register my stacks based on a deformation field from point cloud 1 to point cloud 2.</p>
<p>PS: 3-D volumetric visualisation is quite hard for microscopy images, possibly due to the presence of background noise which creates some kind of “haze” between the observer and the object being observed… Working out some default values in the “Volume rendering” tab is on my TODO list <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/87580bb5901531e5026e402860c69a4920fdbbda.jpeg" data-download-href="/uploads/short-url/jjj5VCVTMyqoHDYpBPe0cHB5lEe.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/87580bb5901531e5026e402860c69a4920fdbbda_2_690x466.jpeg" alt="image" data-base62-sha1="jjj5VCVTMyqoHDYpBPe0cHB5lEe" width="690" height="466" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/87580bb5901531e5026e402860c69a4920fdbbda_2_690x466.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/87580bb5901531e5026e402860c69a4920fdbbda_2_1035x699.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/87580bb5901531e5026e402860c69a4920fdbbda_2_1380x932.jpeg 2x" data-dominant-color="4F4F4F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1298 157 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Cheers,<br>
Egor</p>

---

## Post #3 by @ylcnkzy (2023-10-17 08:16 UTC)

<p>Hi Egor,</p>
<p>Thanks for your input. These two time points are the stack images of the same sample. The original one has more stack than the crop one. Stack size and resolution are the same, but the number of stacks in the original is higher. Some areas share the same morphological area that I thought could be registered. Those two stacks are the ones that need to be registered via deformable image registration.</p>
<p>it would be so cool to establish image registration for 3D Microscopy images. It is really the need of the field.</p>
<p>PS: I will improve the quality of the image obtained.</p>
<p>Thanks,</p>

---

## Post #4 by @pieper (2023-11-05 18:13 UTC)

<aside class="quote no-group" data-username="ylcnkzy" data-post="1" data-topic="32204">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ylcnkzy/48/12189_2.png" class="avatar"> ylcnkzy:</div>
<blockquote>
<p>I am just wondering if you have any idea how to perform it via 3D Slicer.</p>
</blockquote>
</aside>
<p>If the same structures appear in the images just with different relative intensities then I would think a mutual information based approach like in the General Registration (BRAINS) module would work.</p>
<p>But if you have some control over the imaging process, then including some markers that can be used for alignment would be really helpful.</p>
<p>From a quick look at the data you provided they don’t appear to have much in common.  Maybe they are flipped with respect to each other?</p>
<p>Also does the tissue deform as part of the staining process?</p>

---
