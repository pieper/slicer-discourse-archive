---
topic_id: 13891
title: "Using Png File With Radiomics"
date: 2020-10-06
url: https://discourse.slicer.org/t/13891
---

# Using png file with radiomics

**Topic ID**: 13891
**Date**: 2020-10-06
**URL**: https://discourse.slicer.org/t/using-png-file-with-radiomics/13891

---

## Post #1 by @cucphuong (2020-10-06 13:24 UTC)

<p>Hello everyone, I am working with radiomics and want to use RadiomicsGLCM to extract feature. I want to extract glcm from brain tumor which will be segmented by mask.<br>
Here is my code:<br>
img = sitk.ReadImage(path)<br>
mask = sitk.ReadImage(path) <span class="hashtag-raw">#images</span> are png format<br>
glcm = radiomics.RadiomicsGLCM(img,mask,force2D=2)</p>
<p>But I got an error: min() arg is an empty sequence<br>
Please help me with this problem! Thank u so much in advance!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f725ce3bccf4ac703f21ba62fb6c9b7053793d1d.jpeg" data-download-href="/uploads/short-url/zgmVRHyAwHfayXH4GkwxFOSBFA9.jpeg?dl=1" title="20201006_115046" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f725ce3bccf4ac703f21ba62fb6c9b7053793d1d_2_482x500.jpeg" alt="20201006_115046" data-base62-sha1="zgmVRHyAwHfayXH4GkwxFOSBFA9" width="482" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f725ce3bccf4ac703f21ba62fb6c9b7053793d1d_2_482x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f725ce3bccf4ac703f21ba62fb6c9b7053793d1d_2_723x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f725ce3bccf4ac703f21ba62fb6c9b7053793d1d_2_964x1000.jpeg 2x" data-dominant-color="323546"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">20201006_115046</span><span class="informations">1649×1709 305 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @fedorov (2020-10-06 13:33 UTC)

<p>pyradiomics works with single-channel images, see this section of documentation: <a href="https://pyradiomics.readthedocs.io/en/latest/faq.html?what-modalities-does-pyradiomics-support-2d-3d-color#what-modalities-does-pyradiomics-support-2d-3d-color">https://pyradiomics.readthedocs.io/en/latest/faq.html?what-modalities-does-pyradiomics-support-2d-3d-color#what-modalities-does-pyradiomics-support-2d-3d-color</a></p>

---

## Post #3 by @JoostJM (2020-10-10 13:40 UTC)

<p>In addition, please use the featureextractor module when computing features, as this also contains multiple steps and checks of image preprocessing and provides much better traceback information.</p>
<p>Using feature classes directly is only intended for developers, as there are many caveats and additional steps to be aware of. This type of use is listed <a href="https://pyradiomics.readthedocs.io/en/latest/developers.html#using-feature-classes-directly">here</a>. For regular use (even when interactively from python scripts, spyder, jupyter notebooks etc), see <a href="https://pyradiomics.readthedocs.io/en/latest/usage.html">the usage section in the documentation</a>.</p>

---
