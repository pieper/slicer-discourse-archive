---
topic_id: 36326
title: "Flip Image Along An Axis"
date: 2024-05-20
url: https://discourse.slicer.org/t/36326
---

# Flip image along an axis

**Topic ID**: 36326
**Date**: 2024-05-20
**URL**: https://discourse.slicer.org/t/flip-image-along-an-axis/36326

---

## Post #1 by @Stuart (2024-05-20 20:24 UTC)

<p>Hi Mark,</p>
<p>Thanks for sending this python snippet but I don’t know how to implement this code. I did read the discussion titled <a href="/t/running-python-file-in-slicer-on-mac/24356">Running python file in Slicer on Mac</a> from July 2022 and that made it clear that this is way beyond my skill level. Hopefully others will be able to benefit from your expertise.</p>
<p>Stuart</p>

---

## Post #2 by @lassoan (2024-05-22 13:56 UTC)

<p>First of all, make sure that your image is really flipped and not rotated. If it is indeed flipped then it may be also incorrect in other ways, such as its spacing, position, or orientation may be corrupted, too. How did you get a flipped image? Can you fix the process of obtaining the image? It would be safer than applying some arbitrary fix later.</p>
<p>If you want to mirror an image along one or more axes then you can do that using the graphical user interface:</p>
<ul>
<li>create a new transform in Transforms module</li>
<li>change diagonal value in the matrix from 1 to -1 for the axes you want to flip around</li>
<li>apply and harden the transform on the image</li>
</ul>

---

## Post #3 by @chir.set (2024-05-22 14:57 UTC)

<p>Would the ‘Filtering / Simple filters / FlipImageFilter’ be an option too? Its main advantage would be using a single tool.</p>

---

## Post #4 by @lassoan (2024-05-22 18:21 UTC)

<p>There are many ways to do it. There may be differences between the options in how flipping is done, for example if image voxels are reordered or only the IJK to RAS matrix is modified.</p>

---

## Post #5 by @Stuart (2024-05-23 16:08 UTC)

<p>Hi Andras,</p>
<p>This solved my problem. Thanks.</p>
<p>We don’t know how the orientation of the microCT images became reversed in the first place as they came from another source. There is no question of the reversal, however, as we produced a segmented version the mandible and compared it with a photograph of the specimen. We will definitely contact the folks who made the original scan regarding this issue. It certainly would be best to fix the problem at its source but in this case we had many segmenting hours invested in this project that we did not want to abandon.</p>
<p>Thanks for your support,</p>
<p>Stuart</p>

---
