# Rendering of a RGB and a scalar volume in the same scene

**Topic ID**: 37699
**Date**: 2024-08-05
**URL**: https://discourse.slicer.org/t/rendering-of-a-rgb-and-a-scalar-volume-in-the-same-scene/37699

---

## Post #1 by @micgriffa (2024-08-05 09:31 UTC)

<p>Dear 3D Slicer users and developers,</p>
<p>I’m wondering whether it is already possible to render, within the same 3D scene, a scalar volume along with an RGB volume, with the possibility of setting one of the two, e.g., the scalar volume, as the foreground and the other volume as a background.</p>
<p>I’ve tried using the Multi-Volume option in the Volume Rendering module, without success. The error message I’ve got is the following:</p>
<p>“If IndependentComponents is Off in the volume property, then the data must have either 2 or 4 component scalars. The input data has 1 component(s).”</p>
<p>The RGB volume is loaded as a stack of RGB TIFF files.</p>
<p>I’m working in a 64-bit Windows environment and with Ver. 5.7.0.</p>
<p>Thanks a lot for any feedback.</p>
<p>Best regards,</p>
<p>Michele</p>

---

## Post #2 by @pieper (2024-08-05 12:33 UTC)

<p>The MultiVolume renderer may not support color rendering - I haven’t tried - but you could try making an RGBA volume.  There’s no specific GUI tool in Slicer for this but it could be done in python or maybe with some tool like imagej.</p>

---

## Post #3 by @muratmaga (2024-08-05 23:32 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="37699">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>There’s no specific GUI tool in Slicer</p>
</blockquote>
</aside>
<p>ColorizeVolume in Sandbox?</p>

---

## Post #4 by @pieper (2024-08-06 12:49 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="3" data-topic="37699">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>ColorizeVolume in Sandbox?</p>
</blockquote>
</aside>
<p>If the RGB volume was originally a labelmap or segmentation, yes, you could create a new version using ColorizeVolume.  But I’ve never tried that with the MultiVolume volume renderer so it may not work.  It would be interesting to try.</p>
<p>Maybe <a class="mention" href="/u/micgriffa">@micgriffa</a> could describe more specifically what the data is and what is desired.</p>

---
