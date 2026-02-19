---
topic_id: 12234
title: "Automate Model To Ct Registration"
date: 2020-06-17
url: https://discourse.slicer.org/t/12234
---

# Automate model to CT registration

**Topic ID**: 12234
**Date**: 2020-06-17
**URL**: https://discourse.slicer.org/t/automate-model-to-ct-registration/12234

---

## Post #1 by @Tekk_ya (2020-06-17 18:20 UTC)

<p>Hi everyone,</p>
<p>I was wondering if there is a way to use Fiducial registration automatically. I have tried to set the landmarks manually and register an STL file on a CT image in order to align the STL file to the scan. However, the result of the registration is not perfect and there are some errors due to the poor rigid transformation. I am concerned if the resulting error is due to the manually selected landmarks. Is there any way to automatically register as STL model on the CT scan? Is the Fiducial registration the best way of doing this?</p>
<p>Thanks in advance for your help</p>

---

## Post #2 by @lassoan (2020-06-26 15:24 UTC)

<p>There are many options for registering models (surface meshes) to CT images, by matching point set to point set, point set to surface, surface to surface, image to image, etc.</p>
<p>I would recommend to first experiment with various registration modules using their GUI and once you have found a robust solution then automate it using Python scripting.</p>
<p>If you provide more information about what you would like to achieve then we can give recommendations for approaches and Slicer modules that may work well.</p>

---
