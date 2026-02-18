# Spine segmentation in cervico-thoracic region

**Topic ID**: 11234
**Date**: 2020-04-21
**URL**: https://discourse.slicer.org/t/spine-segmentation-in-cervico-thoracic-region/11234

---

## Post #1 by @Ricardoneuro (2020-04-21 20:43 UTC)

<p>Hi community,</p>
<p>It´s being very difficult to segment a spine in a dual quality aquisition dataset. This happens, for example, in the the cervical-thoracic transition of the spine.</p>
<p>If someone else is in this issue please join.</p>

---

## Post #2 by @pieper (2020-04-21 21:07 UTC)

<p>Can you post a screenshot?</p>

---

## Post #3 by @Ricardoneuro (2020-04-24 15:47 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/df3d2bccf14174023cb7b53dd18c70f7a1904129.jpeg" data-download-href="/uploads/short-url/vQRx89puJixp2q1mc3rWjiRovHP.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/df3d2bccf14174023cb7b53dd18c70f7a1904129_2_690x347.jpeg" alt="image" data-base62-sha1="vQRx89puJixp2q1mc3rWjiRovHP" width="690" height="347" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/df3d2bccf14174023cb7b53dd18c70f7a1904129_2_690x347.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/df3d2bccf14174023cb7b53dd18c70f7a1904129_2_1035x520.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/df3d2bccf14174023cb7b53dd18c70f7a1904129.jpeg 2x" data-dominant-color="5D4D58"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1287×649 339 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>In this study, for example, the quality of segmentation in the upper cervical spine and chest levels is very different due to the extremely different body mass between these regions. My point here is: how to minimize or deal with this situation since uniform bone segmentation is required. The ultimate goal here is to build drilling guides and precision on contact surfaces is highly required.</p>

---

## Post #4 by @pieper (2020-04-28 18:26 UTC)

<p>Unfortunately you are probably limited by the CT, and of course people who need spine surgery may also have weak bones that don’t image as clearly as strong bones.  There is a wide array of filters that you might try, like anisotropic diffusion or others that try to enhance edges but be aware that those might also have an impact on the fine details in the image (always compare before and after closely).</p>
<p>If you want to share a deidentified example perhaps someone will try it out and give more suggestions.</p>

---

## Post #5 by @lassoan (2020-04-28 21:01 UTC)

<p>The quality of this scan is pretty good and some filtering that <a class="mention" href="/u/pieper">@pieper</a> suggested above may improve it a bit further. It is also very fortunate that you don’t need to separate the vertebrae (separating bones from discs are very hard to do on CT) and that you only need cortical bone surfaces (as they usually have quite good contrast).</p>
<p>A single global threshold value may not work well for the entire image, so instead I would create a “bone” and “other” segment, and use them as seeds for “Grow from seeds”. Bone segment would use a high threshold value, which is only bone (everywhere in the image) and the other segment would be created with a low threshold value, which only contains non-bone regions.</p>
<p>Probably after all this you will still have holes inside the bone (as cancellous bone density is similar to soft tissue). You can fill those using “Wrap Solidify” effect (provided by SurfaceWrapSolidify extension).</p>

---
