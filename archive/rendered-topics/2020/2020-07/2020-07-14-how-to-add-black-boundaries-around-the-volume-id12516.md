---
topic_id: 12516
title: "How To Add Black Boundaries Around The Volume"
date: 2020-07-14
url: https://discourse.slicer.org/t/12516
---

# How to add black boundaries around the Volume?

**Topic ID**: 12516
**Date**: 2020-07-14
**URL**: https://discourse.slicer.org/t/how-to-add-black-boundaries-around-the-volume/12516

---

## Post #1 by @siaeleni (2020-07-14 00:40 UTC)

<p>Hello,</p>
<p>I have a model and I convert it into a Scalar Volume, but I want to add some extra black space around. Please check the picture. Is this possible?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d941a927760870e8e83fc15d4dd00aac3535995.jpeg" alt="Capture" data-base62-sha1="dlPIn3dqig6vJrL3mRBgTIPopiB" width="280" height="210"></p>
<p>Thanks</p>

---

## Post #2 by @muratmaga (2020-07-14 01:22 UTC)

<p>You can:</p>
<ol>
<li>use crop volume and set the rOI bigger than the volume itself, and unclick ‘interpolated cropping’, or</li>
<li>Go to Simple Filters and search for Pad and choose time ImagePadFilter and specify how much you want to expand in each directions.</li>
</ol>

---

## Post #3 by @siaeleni (2020-07-14 04:11 UTC)

<p>Thanks Murat! I used Crop Volume.</p>

---
