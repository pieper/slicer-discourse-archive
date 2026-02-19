---
topic_id: 42864
title: "Beginner Question What Is Same Physical Space"
date: 2025-05-10
url: https://discourse.slicer.org/t/42864
---

# Beginner question: what is ”same physical space”?

**Topic ID**: 42864
**Date**: 2025-05-10
**URL**: https://discourse.slicer.org/t/beginner-question-what-is-same-physical-space/42864

---

## Post #1 by @Mikko_Pyysalo (2025-05-10 11:40 UTC)

<p>Dear community,<br>
I have two aligned sinus STL models. Converted them to binary labelmaps via segmentation nodes. I made sure they have same spacing and origo. Then I tried to compute the euclidian distance with SimiarityIndexFilter. There comes an error, which tells the objects don’t share same physical space. What else than same origo and spacing is needed?</p>
<p>Best regards,<br>
Mikko</p>

---

## Post #2 by @lassoan (2025-05-10 11:43 UTC)

<p>The default image geometry will not be exactly the same for two different surface models. You can use the “Specify geometry” button to change the geometry of the segmentation before exporting to labelmap; or you can choose the first exported labelmap as reference volume when you export the second segmentation to labelmap.</p>

---

## Post #3 by @Mikko_Pyysalo (2025-05-10 18:11 UTC)

<p>Thank you!<br>
Now their geometry is similar.<br>
There comes an error:<br>
Error before execution of SimilarityIndexImageFilter: ’NoneType’ object has no attribute ’GetAddressAsString’</p>
<p>SquaredDifferenceImageFilter works perfectly but SimilarityIndexImageFilter gives an error.</p>
<p>Br<br>
Mikko</p>

---

## Post #4 by @Mikko_Pyysalo (2025-05-11 12:24 UTC)

<p>Now there becomes an error, which tells that input file type is not correct. I have binary labelmap. What is the right input file type for SimilarityIndexImageFilter?</p>
<p>Br<br>
Mikko</p>

---
