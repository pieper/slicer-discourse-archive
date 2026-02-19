---
topic_id: 28512
title: "Image Registration Nrrd Files Appear To Be Scaled Differentl"
date: 2023-03-22
url: https://discourse.slicer.org/t/28512
---

# Image registration nrrd files appear to be scaled differently despite adjusting scaling

**Topic ID**: 28512
**Date**: 2023-03-22
**URL**: https://discourse.slicer.org/t/image-registration-nrrd-files-appear-to-be-scaled-differently-despite-adjusting-scaling/28512

---

## Post #1 by @elrond11 (2023-03-22 01:35 UTC)

<p>I have been using 3D Slicer for rigid registration of two nrrd volumes. The first is an STL file that I have rasterized into an nrrd file within Slicer, this is the fixed image. The second nrrd file, moving image, has been resampled to match the fixed image file in Python. When I open the two files, the fixed image has image spacing units already encoded in Slicer. The moving image has the default of 1 which I set to match the spacing units of the fixed image. This has generally been fine for my registration workflow but for some files I have noticed the fixed image seems to still have features larger then the moving image even after adjusting the image spacing. Is there a way to fix this automatically in Slicer or Python?</p>
<p>Example included below. The overlay is the fixed image which seems to have image features much larger then what’s in the moving image.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f0070eb70650bebac5f01e434b21b05d2e2fbe2a.png" alt="image" data-base62-sha1="yfnIeEvHEY5b8G9TavKWALKkDhg" width="402" height="318"></p>

---

## Post #2 by @muratmaga (2023-03-22 02:37 UTC)

<p>Rigid image registration will  not change the size of the objects. It will resample our volume to that reference volume (so spacing change change from 1,1,1 to 2,2,2 if that’s the spacing of the reference volume), but this will not result in size change.</p>
<p>If you need scaling you need to to use similarity transform (rigid + uniform scaling).</p>

---

## Post #3 by @elrond11 (2023-03-22 02:52 UTC)

<p>I have tried using the Rigid + Scale 7 DOF option but I find the result to look the same. The moving image did not appear to scale to have similar feature size to the fixed image.</p>
<p>Better to provide more context,</p>
<p>The fixed image is an STL file that I had submitted for 3D printing. The moving image is image that I had scanned in microCT. I have tried using landmark registration and used both the rigid registration and the similarity registration. This results in the plates you see in the top and bottom of the image having an incorrect contour and scaling. I am not sure why the STL file and the microCT images do not align as well as they should.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/49c70c22c648b0c7b329b818ffa0a6d1595ec3f8.png" alt="image" data-base62-sha1="awFjn1NCaDhLhVZT93I3jKvcpv2" width="497" height="387"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d12341a090d8d7f05a152fa0f05b22b047bbb51.png" data-download-href="/uploads/short-url/6qIucavlT9hcD1G53tixYvHNqpj.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d12341a090d8d7f05a152fa0f05b22b047bbb51_2_690x251.png" alt="image" data-base62-sha1="6qIucavlT9hcD1G53tixYvHNqpj" width="690" height="251" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d12341a090d8d7f05a152fa0f05b22b047bbb51_2_690x251.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d12341a090d8d7f05a152fa0f05b22b047bbb51.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d12341a090d8d7f05a152fa0f05b22b047bbb51.png 2x" data-dominant-color="9C9CA3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">819×299 71.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @muratmaga (2023-03-22 02:56 UTC)

<p>For any type of image registration to work well, image contents needs to similar in both moving and reference image. In your screenshot above, there is a circular object in one of the image, which I don’t think exists in the other? (it is a bit hard to tell).</p>
<p>Also, the initial alignment matters. Are both images, more or less similarly oriented initially? Most image registration methods will work fine if the images are rotated only a few degrees, but will have hard time matching extreme differences in rotation of the objects.</p>

---

## Post #5 by @elrond11 (2023-03-22 02:58 UTC)

<p>Yes that is a bore from the microCT that was not removed from the registration so that may be confounding the results a bit.</p>
<p>I have gotten a strong initial alignment with landmark registration, but this seems to change the plates at the top and bottom of the image. This issue is not apparent in all of my images however.</p>

---

## Post #6 by @muratmaga (2023-03-22 02:58 UTC)

<aside class="quote no-group" data-username="elrond11" data-post="1" data-topic="28512">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/elrond11/48/18421_2.png" class="avatar"> elrond11:</div>
<blockquote>
<p>first is an STL file that I have rasterized into an nrrd file within Slicer, this is the fixed image.</p>
</blockquote>
</aside>
<p>Rasterized STL file will have no intensity information to help the registration. You will be better of using masks for registration. And use a metric that’s more relevant to register binary images (such as this <a href="https://itk.org/Doxygen/html/classitk_1_1MatchCardinalityImageToImageMetric.html" class="inline-onebox">ITK: itk::MatchCardinalityImageToImageMetric&lt; TFixedImage, TMovingImage &gt; Class Template Reference</a>)</p>

---

## Post #7 by @elrond11 (2023-03-22 02:59 UTC)

<p>A mask of the microCT image? I had decided against it as to not introduce errors from the segmentation process, such as noise that could alter the contour.</p>

---
