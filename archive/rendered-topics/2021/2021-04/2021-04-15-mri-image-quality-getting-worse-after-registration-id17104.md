---
topic_id: 17104
title: "Mri Image Quality Getting Worse After Registration"
date: 2021-04-15
url: https://discourse.slicer.org/t/17104
---

# MRI image quality getting worse after registration

**Topic ID**: 17104
**Date**: 2021-04-15
**URL**: https://discourse.slicer.org/t/mri-image-quality-getting-worse-after-registration/17104

---

## Post #1 by @peter_adidharma (2021-04-15 13:43 UTC)

<p>Hello everyone,</p>
<p>I was having as issue where everytime a registration was performed, the image quality of the MRI seems to get worse. Is there any way to avoid such condition?</p>
<p>Many thanks,<br>
Peter</p>

---

## Post #2 by @cpinter (2021-04-15 14:01 UTC)

<p>It’s very hard to give proper answer with so little information, but let’s assume that you mean the output volume for Elastix registration gets more and more “blurry”. The solution is that instead of specifying output volume, specify an output transform. That way the transformation will not be “burnt” into the volume, only applied on it.</p>

---
