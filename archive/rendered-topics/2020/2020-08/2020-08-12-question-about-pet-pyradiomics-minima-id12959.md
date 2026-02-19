---
topic_id: 12959
title: "Question About Pet Pyradiomics Minima"
date: 2020-08-12
url: https://discourse.slicer.org/t/12959
---

# Question about PET Pyradiomics Minima

**Topic ID**: 12959
**Date**: 2020-08-12
**URL**: https://discourse.slicer.org/t/question-about-pet-pyradiomics-minima/12959

---

## Post #1 by @tyusufaly (2020-08-12 04:47 UTC)

<p>Hello,</p>
<p>I am having trouble interpreting the Pyradiomics output when applied to PET dicom images, in particular, the values of the ‘diagnostic-original’ features related to the minima, maxima, and range. I am doing the processing without normalization, and I set the default sampling bin width to 25. When I apply this to a large batch of PET dicoms, I get one of two things:</p>
<ol>
<li>the minimum value equal to 0, with a max on the order of 18000,</li>
<li>the minimum value on the order of -32000, and the max on the order of +32000.</li>
</ol>
<p>This binary dichotomy holds even if I vary my bin width by several orders of magnitude.</p>
<p>Can someone please explain to me what the minima, maxima, range values of my Pyradiomics PET output mean? What are the units of these values and what would cause an image to have one characteristic range or another? I just do not understand what the code is calculating.</p>
<p>Thank you.</p>

---

## Post #2 by @pieper (2020-08-12 12:50 UTC)

<p>PET images can be in many forms so you need to be careful to understand which series you are using.  I’m not a PET/CT expert, but a study typically includes a raw data series and an attenuation corrected series.  Also, sometimes the raw values and encoded on different scales per-slice, so you need to be sure that has been accounted for; SimpleITK/ITK does this automatically.  It looks like PyRadiomics is giving you valid data but how you interpret it depends on the specific kind of PET data you provide and how you process it.</p>

---
