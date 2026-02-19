---
topic_id: 1604
title: "What Is The Underlying Function Of Interpolate Option Of Vol"
date: 2017-12-06
url: https://discourse.slicer.org/t/1604
---

# What is the underlying function of 'interpolate' option of Volumes module

**Topic ID**: 1604
**Date**: 2017-12-06
**URL**: https://discourse.slicer.org/t/what-is-the-underlying-function-of-interpolate-option-of-volumes-module/1604

---

## Post #1 by @muratmaga (2017-12-06 17:36 UTC)

<p>I have a resampled volume which looks smoother when the interpolate option is checked. I would like to save the volume like that. What is the actual function it uses to do that?</p>

---

## Post #2 by @lassoan (2017-12-06 21:58 UTC)

<p>That option controls how the image is sampled when scaled for display: nearest neighbor / linear (see <a href="https://en.wikipedia.org/wiki/Image_scaling">https://en.wikipedia.org/wiki/Image_scaling</a> for details). There is nothing to save - what you see is still the original volume.</p>

---
