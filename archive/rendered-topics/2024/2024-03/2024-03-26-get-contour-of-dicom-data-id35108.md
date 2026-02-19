---
topic_id: 35108
title: "Get Contour Of Dicom Data"
date: 2024-03-26
url: https://discourse.slicer.org/t/35108
---

# Get contour of dicom data

**Topic ID**: 35108
**Date**: 2024-03-26
**URL**: https://discourse.slicer.org/t/get-contour-of-dicom-data/35108

---

## Post #1 by @koenterheegde (2024-03-26 18:21 UTC)

<p>Hello everyone,</p>
<p>I’m currently struggling to get the contour of dicom data. Lets say you have a CT scan of a human and only want to get the surface of the body, so not the internal stuff. I’ve tried by just standard thresholding but the HU values are too closely related to make a difference. I’ve also tried to just segment the whole body from the CT scan and then use ‘hollow’ and then apply ‘islands’, sometimes this works but in most cases still a lot of the inside has to be removed manually. I’m pretty sure there is a different way to do this as the outside of the body is black and almost everything inside the body has a higher HU value. Would be nice if somebody could help!</p>

---
