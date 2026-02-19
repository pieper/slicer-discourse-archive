---
topic_id: 25614
title: "How To Transform Sagittal Images To Axis Images"
date: 2022-10-09
url: https://discourse.slicer.org/t/25614
---

# How to transform sagittal images to Axis images？

**Topic ID**: 25614
**Date**: 2022-10-09
**URL**: https://discourse.slicer.org/t/how-to-transform-sagittal-images-to-axis-images/25614

---

## Post #1 by @slicer365 (2022-10-09 09:07 UTC)

<p>Hello，friends,<br>
I am studying deep learning,I need to change the dicom images into the same position.<br>
how to transform sagittal DICOM to axial DICOM？</p>
<p>as you see,the default position is sagittal,when I load it into slicer ,it can show axial,but when I use Creat a DICOM series module to creat a new dicom series ,it is still Sagittal position.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b51201a95fbd6f1c79b1950514038baec278779.jpeg" alt="1665306062603" data-base62-sha1="m9ZOJxIsWj4SLYz4ExgYgCDdMXD" width="302" height="228"></p>

---

## Post #2 by @pieper (2022-10-09 14:16 UTC)

<p>You can use the Orient Scalar Volume module for that.</p>

---

## Post #3 by @slicer365 (2022-10-09 22:52 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="25614">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>ule for that.</p>
</blockquote>
</aside>
<p>Great! Thank you very much,Mr. Pieper,it works.</p>
<p>Another question is how I can get the python code,I want to write it into my python scripts,as a part of pretreatments for batch.</p>

---

## Post #4 by @pieper (2022-10-10 16:25 UTC)

<p>The script repository is a good place to get ideas.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository</a></p>
<p>Although a lot of the training materials are for slightly older versions, they are still valid for understanding how Slicer works and ways to address tasks via programming:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.10/Training#Tutorials_for_software_developers" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/4.10/Training#Tutorials_for_software_developers</a></p>

---
