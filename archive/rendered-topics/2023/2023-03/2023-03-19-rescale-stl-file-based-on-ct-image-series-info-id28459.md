---
topic_id: 28459
title: "Rescale Stl File Based On Ct Image Series Info"
date: 2023-03-19
url: https://discourse.slicer.org/t/28459
---

# Rescale .stl file based on CT image series info

**Topic ID**: 28459
**Date**: 2023-03-19
**URL**: https://discourse.slicer.org/t/rescale-stl-file-based-on-ct-image-series-info/28459

---

## Post #1 by @jusopar (2023-03-19 19:43 UTC)

<p>Hello everyone,<br>
I would like to ask how to rescale a .stl file, when I only have information on the pixel spacing of the CT image series. I acquired .stl file from MorphoSource, where they also have the CT image series (with pixel spacing info).<br>
Thanks!<br>
Julia</p>

---

## Post #2 by @lassoan (2023-03-19 20:12 UTC)

<p>The simplest method for rescaling a model is to use the <code>Scale</code> option in <code>Surface Toolbox</code> module.</p>

---

## Post #3 by @jusopar (2023-03-19 20:52 UTC)

<p>Thank you Andras!<br>
But when I use the X, Y and Z “pixel spacing” number that I acquired from the CT Image Series in MorphoSource, the model gets even smaller. So I’m thinking the “pixel spacing” is probably not the number I should use in "Scale: on 3D Slicer. Would you have any idea about how to get the “Scale” from the “pixel spacing”.<br>
Thanks!</p>

---

## Post #4 by @muratmaga (2023-03-19 21:32 UTC)

<aside class="quote no-group" data-username="jusopar" data-post="1" data-topic="28459">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jusopar/48/10144_2.png" class="avatar"> jusopar:</div>
<blockquote>
<p>when I only have information on the pixel spacing of the CT image series. I acquired .stl file from MorphoSource</p>
</blockquote>
</aside>
<p>If I understand you have the original CT series of a stl you downloaded from MorphoSource, and you want to correctly size this STL?</p>
<p>if that’s the case, probably the easiest thing would be to measure a distance on the STL, and then measure the same distance on the volume rendering of the CT data. Then divide the CT measurement by stl measurement, and use that number to scale the STL model. This is going to be approximate but should be pretty close. Just pickup a distance that you can measure very consistently.</p>

---

## Post #5 by @jusopar (2023-03-19 21:41 UTC)

<p>Okay, I see. Thank you Murat!</p>

---
