# Surface smoothing and exporting model

**Topic ID**: 1144
**Date**: 2017-09-29
**URL**: https://discourse.slicer.org/t/surface-smoothing-and-exporting-model/1144

---

## Post #1 by @hherhold (2017-09-29 23:57 UTC)

<p>Quick (hopefully quick, anyway) question - When you export a model from a segmentation, does it use the surface smoothing parameter from the “Show 3D” option in the Segment Editor?</p>
<p>I think this might have been discussed in the Development list but a quick look didn’t reveal anything obvious… Apologies in advance if this has been covered elsewhere.</p>
<p>Thanks!</p>
<p>-Hollister</p>

---

## Post #2 by @lassoan (2017-09-30 03:21 UTC)

<aside class="quote no-group" data-username="hherhold" data-post="1" data-topic="1144">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar"> hherhold:</div>
<blockquote>
<p>When you export a model from a segmentation, does it use the surface smoothing parameter from the “Show 3D” option in the Segment Editor?</p>
</blockquote>
</aside>
<p>Yes. What you see is what is exported.</p>

---

## Post #3 by @hherhold (2017-09-30 11:07 UTC)

<p>Sounds good. Thanks!</p>

---

## Post #4 by @Saima (2021-10-07 14:12 UTC)

<p>Hi Andras,<br>
How can the surface smoothing be reduced in segmenteditor (usign script) before exporting the model as a PLY file.</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #5 by @hherhold (2021-10-07 14:17 UTC)

<p>You can reduce the smoothing of segments before exporting as a model:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8ac65dd33ba6c990830b45fbfcec2b287c1ec855.png" data-download-href="/uploads/short-url/jNET84GstE4rEmuYNhmwcu45gEd.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8ac65dd33ba6c990830b45fbfcec2b287c1ec855_2_690x195.png" alt="image" data-base62-sha1="jNET84GstE4rEmuYNhmwcu45gEd" width="690" height="195" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8ac65dd33ba6c990830b45fbfcec2b287c1ec855_2_690x195.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8ac65dd33ba6c990830b45fbfcec2b287c1ec855.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8ac65dd33ba6c990830b45fbfcec2b287c1ec855.png 2x" data-dominant-color="76818A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">890×252 34.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Or do you need to do this in a script?</p>

---

## Post #6 by @Saima (2021-10-07 14:20 UTC)

<p>Hi,<br>
Is there a way to set the smoothing to 20% instead of 0 in segment editor before exporting model.</p>
<p>Thank you</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #7 by @Saima (2021-10-07 14:49 UTC)

<p>I need to do it in a script</p>
<p>can you tell how can i do.</p>
<p>regards,<br>
Saima Safdar</p>

---

## Post #8 by @hherhold (2021-10-07 14:58 UTC)

<p>Check out the example in the script repository:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#re-convert-using-a-modified-conversion-parameter" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#re-convert-using-a-modified-conversion-parameter</a></p>

---
