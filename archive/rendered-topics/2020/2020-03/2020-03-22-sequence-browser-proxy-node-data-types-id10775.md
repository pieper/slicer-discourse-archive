---
topic_id: 10775
title: "Sequence Browser Proxy Node Data Types"
date: 2020-03-22
url: https://discourse.slicer.org/t/10775
---

# Sequence browser - proxy node data types?

**Topic ID**: 10775
**Date**: 2020-03-22
**URL**: https://discourse.slicer.org/t/sequence-browser-proxy-node-data-types/10775

---

## Post #1 by @hnisar3 (2020-03-22 02:41 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.11.0-2019-07-23<br>
Expected behavior:<br>
I am streaming data through PLUS and using OpenIGTLinkIF. Data includes a transform, an image and a string (text read from the image by PLUS). The string streams in as ‘vtkMRMLTextNode’. In the sequence browser, I am able to set the transform (vtkMRMLLinearTransformNode) and the image(vtkMRMLScalarVolumeNode) as a proxy node for new sequences. Similarly, I want to set the string(vtkMRMLTextNode) as a proxy node and be able to record the incoming string/text information.<br>
P.S. it is actually a number that I want but PLUS streams as a string so I record it as a string and convert to float later on.</p>
<p>Actual behavior:<br>
In the sequence browser, in the drop-down menu, I can’t see the name of the text node.<br>
Is it not allowed to have vtkMRMLTextNode set as a proxy node for sequences?</p>
<p>Thank you for helping me. Wishing everyone wellness and health in these times.</p>

---

## Post #2 by @lassoan (2020-03-22 03:14 UTC)

<p>I’ve added support for sequencing vtkMRMLTextNodes now, it should be available for download on Monday.</p>

---

## Post #3 by @hnisar3 (2020-03-23 14:11 UTC)

<p>Thank you Andras! I will let you know as soon as I try it again</p>

---

## Post #4 by @hnisar3 (2020-03-24 20:25 UTC)

<p>It works perfectly fine! Thank you</p>

---
