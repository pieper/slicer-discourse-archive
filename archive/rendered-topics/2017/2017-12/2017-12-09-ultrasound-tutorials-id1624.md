---
topic_id: 1624
title: "Ultrasound Tutorials"
date: 2017-12-09
url: https://discourse.slicer.org/t/1624
---

# Ultrasound tutorials

**Topic ID**: 1624
**Date**: 2017-12-09
**URL**: https://discourse.slicer.org/t/ultrasound-tutorials/1624

---

## Post #1 by @iplneuro (2017-12-09 11:11 UTC)

<p>Hi,</p>
<p>Can anyone give some basic tutorial and links for using the ultrasound extension module.</p>
<p>Thanks and regards,</p>
<p>Suba</p>

---

## Post #2 by @ihnorton (2017-12-09 11:13 UTC)

<p>There are a number of tutorials here:</p>
<p><a href="http://www.slicerigt.org/wp/user-tutorial/" class="onebox" target="_blank">http://www.slicerigt.org/wp/user-tutorial/</a></p>
<p>(some include recorded data so you can demo/test without needing access to real systems)</p>

---

## Post #3 by @iplneuro (2017-12-11 08:55 UTC)

<p>Hi,</p>
<p>Thank you sir for your valuable reply mail. I want to create model from the slicer ultrasound sample data set and I want to know that is possible. I just want to know how the ultrasound extension module is used. If I use the slicer ultrasound data set in the ultrasound extension module that is where I got stuck I don’t know how to use the option in it. Can anyone help me with some tutorials.</p>
<p>Thanks and regards,</p>
<p>Suba</p>

---

## Post #4 by @lassoan (2017-12-11 16:41 UTC)

<aside class="quote no-group" data-username="iplneuro" data-post="3" data-topic="1624">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/i/7ba0ec/48.png" class="avatar"> iplneuro:</div>
<blockquote>
<p>I want to create model from the slicer ultrasound sample data set and I want to know that is possible</p>
</blockquote>
</aside>
<p>Yes, it is. We get best results by segmenting on individual tracked ultrasound slices and reconstruct a model from that using Markups To Models module. This works very fast and robustly for simple shapes, such as tumors. Another option is to reconstruct a volume and segment that (and export segmentation to models). We used this approach with acceptable results for reconstructing more complex shapes, such as bone surfaces.</p>

---

## Post #5 by @iplneuro (2017-12-15 10:29 UTC)

<p>Hi,</p>
<p>Thank you for your valuable reply. Let me try with your valuable instructions and get back to you.</p>
<p>Thanks and regards,</p>
<p>Suba</p>

---
