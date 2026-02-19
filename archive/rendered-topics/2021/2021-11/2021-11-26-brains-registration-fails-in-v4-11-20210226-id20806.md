---
topic_id: 20806
title: "Brains Registration Fails In V4 11 20210226"
date: 2021-11-26
url: https://discourse.slicer.org/t/20806
---

# BRAINS Registration fails in V4.11.20210226

**Topic ID**: 20806
**Date**: 2021-11-26
**URL**: https://discourse.slicer.org/t/brains-registration-fails-in-v4-11-20210226/20806

---

## Post #1 by @Lutz (2021-11-26 19:57 UTC)

<p>Hi to all,<br>
I am using Slicer at the University of Nueremberg to train Master students in addition to some theroretical lessons. One experiment is based on CT Registration Tutorial by Michael Fassbind from youtube. Herein, a pre-op and a post-op CT hip data set are manually and automatically registered using transform and Registration (Brains) module, respectively. This worked well in V4.10.2. In version V4.11.2, however, the automatic registration failed with the following error message:<br>
General Registration (BRAINS) standard error:</p>
<p>ExceptionObject caught !<br>
itk::ExceptionObject (000000D53B7E8480)<br>
Location: “unknown”<br>
File: D:\D\S\Slicer-1-build\ITK\Modules\Registration\Metricsv4\include\itkMattesMutualInformationImageToImageMetricv4.hxx<br>
Line: 316<br>
Description: itk::ERROR: itk::ERROR: MattesMutualInformationImageToImageMetricv4(000002BB7544E710): All samples map outside moving image buffer. The images do not sufficiently overlap. They need to be initialized to have more overlap before this metric will work. For instance, you can align the image centers by translation.</p>
<p>Are there any changes necessary I am not aware of?<br>
With best regards,<br>
Lutz<br>
P.S. the 2 data sets are not aligned, I centered them in advance using the volume module</p>

---

## Post #2 by @lassoan (2021-11-26 23:27 UTC)

<p>Registration modules ignore the transforms that are just applied but not hardened to a volume. You need to <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html#harden-transform-on-a-node">harden the transform</a> before the registration.</p>
<p>I would also recommend to try <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html#automatic-image-registration">Elastix and ANTs extensions</a>, as those tend to be work with default parameters, without the need for any parameter tuning.</p>

---

## Post #3 by @Lutz (2021-12-09 10:57 UTC)

<p>Andras,<br>
many thanks, the hardening worked. Now, my students can perfom the course completely. I just wondered that the hardening was not necessary in versions &lt;V4.11<br>
Best wishes<br>
Lutz</p>

---

## Post #4 by @lassoan (2021-12-09 13:44 UTC)

<p>Centering in &lt;4.11 was performed by hardening the transform on it, but in current Slicer versions the transform is just applied, to allow the user to access the original position of the image. Hardening is an irreversible operation, after that the original image position is lost.</p>

---
