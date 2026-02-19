---
topic_id: 6442
title: "Uneven Slice Thickness"
date: 2019-04-09
url: https://discourse.slicer.org/t/6442
---

# Uneven slice thickness

**Topic ID**: 6442
**Date**: 2019-04-09
**URL**: https://discourse.slicer.org/t/uneven-slice-thickness/6442

---

## Post #1 by @prorai (2019-04-09 11:16 UTC)

<p>Any Solution for this??</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8af280ef4d9c09b12a8e8c1a66219f1f388bd89f.png" data-download-href="/uploads/short-url/jPbs3N1R5sQbswRbFGJRlCiIv1B.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8af280ef4d9c09b12a8e8c1a66219f1f388bd89f_2_690x360.png" alt="image" data-base62-sha1="jPbs3N1R5sQbswRbFGJRlCiIv1B" width="690" height="360" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8af280ef4d9c09b12a8e8c1a66219f1f388bd89f_2_690x360.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8af280ef4d9c09b12a8e8c1a66219f1f388bd89f_2_1035x540.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8af280ef4d9c09b12a8e8c1a66219f1f388bd89f.png 2x" data-dominant-color="3F414B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1242×649 144 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2019-04-09 19:04 UTC)

<p>This should help: <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM#Image_is_stretched_or_compressed_along_one_axis" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM#Image_is_stretched_or_compressed_along_one_axis</a></p>

---

## Post #3 by @prorai (2019-04-11 10:11 UTC)

<p>Yes this helped me i have changed <em>regularization transform</em> form the settings now the images are looking normal, But why threshold is only applying for particular region?<br>
is this because ROI is following old data reference? How can i set this to auto like above setting?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2eaf15f6f8b996d84695758390b791509004a8e8.png" data-download-href="/uploads/short-url/6EZ59XBnV8Tnz8azPzTvDoEgVbq.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2eaf15f6f8b996d84695758390b791509004a8e8_2_689x358.png" alt="image" data-base62-sha1="6EZ59XBnV8Tnz8azPzTvDoEgVbq" width="689" height="358" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2eaf15f6f8b996d84695758390b791509004a8e8_2_689x358.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2eaf15f6f8b996d84695758390b791509004a8e8_2_1033x537.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2eaf15f6f8b996d84695758390b791509004a8e8.png 2x" data-dominant-color="3E3F49"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1240×644 146 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @prorai (2019-04-11 10:48 UTC)

<p>i found that harden transform works for this, how can i automate this, is their any setting , Or  can i apply this using python code?</p>

---

## Post #5 by @cpinter (2019-04-11 14:02 UTC)

<p>This is the python call:</p>
<p><code>slicer.vtkSlicerTransformLogic.hardenTransform(volumeNode)</code></p>

---

## Post #6 by @lassoan (2019-04-11 14:16 UTC)

<p>Acquisition regularization seems to work well. Should we change the DICOM importer in Slicer nightly version to enable regularization by default?</p>
<p>A few things still do not support dynamically applied non-linear transforms, such as volume rendering, and extent computation in Segment Editor, but we should be able to fix these (e.g., by hardening the transform in the volume rendering displayable manager and computing segmentation extents from transformed volume’s corners).</p>
<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/fedorov">@fedorov</a> <a class="mention" href="/u/cpinter">@cpinter</a> <a class="mention" href="/u/jcfr">@jcfr</a></p>

---

## Post #7 by @jcfr (2019-04-11 14:33 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="6442">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>by hardening the transform in the volume rendering displayable manager</p>
</blockquote>
</aside>
<p>Are you thinking of automating the hardening (e.g by comparing a LastHardernedTime of a copy of the volume node with the MTime of the selected volume. Ideally, the two volume would share the same image data …)</p>

---

## Post #8 by @fedorov (2019-04-11 14:53 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="6442">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Should we change the DICOM importer in Slicer nightly version to enable regularization by default?</p>
</blockquote>
</aside>
<p>My concern about this is that it can hide potentially serious issues with the data. I think irregular image geometry should always be a red flag. I would feel fine if the user by default was warned about this issue, and asked to confirm the default choice of regularization. But I think right now the only way to learn about it is in the “Advanced” mode, or via the logs, which I don’t think will draw attention from most users.</p>
<p>About <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM#Image_is_stretched_or_compressed_along_one_axis">this note in the FAQ</a> referenced earlier:</p>
<blockquote>
<p>Scanners may create image volumes with varying image slice spacing.</p>
</blockquote>
<p>I think it is still more likely to have a volume where some slices are simply missing, than varying slice spacing. For what it’s worth, I have never encountered a volume with varying slice spacing, but have seen many with missing slices.</p>

---

## Post #9 by @lassoan (2019-04-11 16:24 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="7" data-topic="6442">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>Are you thinking of automating the hardening (e.g by comparing a LastHardernedTime of a copy of the volume node with the MTime of the selected volume. Ideally, the two volume would share the same image data …)</p>
</blockquote>
</aside>
<p>I’m thinking about just resampling the volume in the volume rendering displayable manager (we can use filter pipeline, so probably we would not need to manually manage MTime).</p>
<aside class="quote no-group" data-username="fedorov" data-post="8" data-topic="6442">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>My concern about this is that it can hide potentially serious issues with the data.</p>
</blockquote>
</aside>
<p>We still display the same warning popup when we load an image with varying slice spacing, regardless of acquisition transform is enabled or not. Acquisition transform cannot solve all problems, but I don’t see how it could make things worse.</p>
<p>I agree that it would be nice to improve warning display, as the advanced section of the DICOM is quite complex. The upcoming <a href="https://github.com/commontk/CTK/pull/858">DICOM browser update</a> allows us to store additional information in Slicer’s DICOM database that can be shown in the series table (not just in the advanced tab). We could also store user’s responses to warning popups (approve loading, apply acquisition transform or not, which loadable to use) so that we would need to only ask once and not every time the user loads the data.</p>

---

## Post #10 by @pieper (2019-04-11 18:33 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="8" data-topic="6442">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>I have never encountered a volume with varying slice spacing,</p>
</blockquote>
</aside>
<p>It’s actually pretty common in some CT acquisitions to vary the slice spacing - e.g. fine cuts near the renal arteries, thicker down the aorta, then fine again in the pelvis.  The goal is to maximize the clinical value while minimizing radiation (and to minimize extra non-valuable images for review).</p>
<p>But yes, users should definitely be made aware when their data doesn’t match the default assumptions of the majority of our processing tools.  I like the idea of automating the hardening operation, but I also think it should be configurable in the Volumes module (e.g. to pick the reference geometry and sampling resolution, as in CropVolume).</p>
<p>It could make sense to add methods to vtkMRMLVolumeNode like <code>GetHardenedImageData</code>, <code>GetHardenedImageDataConnection</code>, <code>SetHardeningReferenceGeometry</code>.</p>

---

## Post #11 by @fedorov (2019-04-11 19:01 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> definitely, if the new DICOM browser would allow to prominently label volumes that have irregular slicing, I would not have any concern enabling regularization by default.</p>
<aside class="quote no-group" data-username="pieper" data-post="10" data-topic="6442">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>It’s actually pretty common in some CT acquisitions to vary the slice spacing</p>
</blockquote>
</aside>
<p>Makes sense, I just shared my personal anecdotal evidence. I am not saying how generalizable it is. I don’t think I ever encountered those myself.</p>

---

## Post #12 by @Davide_Punzo (2023-11-13 08:48 UTC)

<p>NOTE: Support for regularization transform hardening in DICOM Scalar plugin has been added. See <a href="https://discourse.slicer.org/t/enh-support-regularization-transform-hardening-in-dicom-scalar-plugin/32772">link</a>.</p>

---
