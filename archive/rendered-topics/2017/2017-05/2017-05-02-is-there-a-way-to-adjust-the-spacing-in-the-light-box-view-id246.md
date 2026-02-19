---
topic_id: 246
title: "Is There A Way To Adjust The Spacing In The Light Box View"
date: 2017-05-02
url: https://discourse.slicer.org/t/246
---

# Is there a way to adjust the spacing in the light box view

**Topic ID**: 246
**Date**: 2017-05-02
**URL**: https://discourse.slicer.org/t/is-there-a-way-to-adjust-the-spacing-in-the-light-box-view/246

---

## Post #1 by @muratmaga (2017-05-02 17:03 UTC)

<p>Hi,</p>
<p>I am using the lightbox view and liking it. But currently it is picking up slices that are too close to each other. It is great for local coverage but not so for the entire volume. Is there away to adjust the spacing between slices (every other, every third etc)?</p>

---

## Post #2 by @lassoan (2017-05-02 17:21 UTC)

<p>Lightbox uses the slice spacing. You can edit it in the slice view controller: click spacing icon, Manual spacing, and enter a new value.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/61777e9b8fe77867d2bdb872e8ea28852d30899d.png" alt="image" data-base62-sha1="dUekuDmrfjYpJSnsfGNniIgKGRf" width="531" height="190"></p>
<p>The value change does not affect an already active lightbox view, so you need to change layout to update to the new spacing.</p>

---

## Post #3 by @muratmaga (2017-05-02 18:54 UTC)

<p>Thanks Andras. I did try to update the spacing, now I know why it didn’t work.<br>
M</p>

---
