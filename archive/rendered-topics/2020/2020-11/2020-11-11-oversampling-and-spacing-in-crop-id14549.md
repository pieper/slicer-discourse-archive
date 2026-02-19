---
topic_id: 14549
title: "Oversampling And Spacing In Crop"
date: 2020-11-11
url: https://discourse.slicer.org/t/14549
---

# Oversampling and Spacing in crop

**Topic ID**: 14549
**Date**: 2020-11-11
**URL**: https://discourse.slicer.org/t/oversampling-and-spacing-in-crop/14549

---

## Post #1 by @manjula (2020-11-11 21:29 UTC)

<p>Hi,</p>
<p>Can someone please tell me how the oversampling actually works? As I understand oversampling or reducing the spacing scale &lt;1 in crop module will increase the image resolution and the image dimensions are increased accordingly.</p>
<p>So is it a software algorithm that creates these extra slices?</p>
<p>What are the advantages and disadvantages of oversampling?</p>
<p>For example If the scanner can scan a image at 0.25 resolution and if we scan the image at 0.5 to lower the dose and or time and we oversample the image by 2 to get the 0.25 what is the difference? i assume the former is better but i do not know the logic behind that. I am thinking about this like optical zoom and digital zoom in cameras.</p>
<p>thanks</p>

---

## Post #2 by @lassoan (2020-11-11 21:47 UTC)

<aside class="quote no-group" data-username="manjula" data-post="1" data-topic="14549">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar"> manjula:</div>
<blockquote>
<p>I am thinking about this like optical zoom and digital zoom in cameras.</p>
</blockquote>
</aside>
<p>Exactly. We can call oversampling “digital zoom”.</p>
<p>It does not add new information (the oversampled image should look exactly the same as the original), it just allows representing finer details in the image or segmentation. For example, if you apply a sharpening filter then you can enhance finer details, or if you segment structures, you can represent thinner walls or smaller vessels.</p>

---
