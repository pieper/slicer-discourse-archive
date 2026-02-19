---
topic_id: 19861
title: "Issue With Margin Effect Margin Value Sign"
date: 2021-09-26
url: https://discourse.slicer.org/t/19861
---

# Issue with Margin Effect margin value sign

**Topic ID**: 19861
**Date**: 2021-09-26
**URL**: https://discourse.slicer.org/t/issue-with-margin-effect-margin-value-sign/19861

---

## Post #1 by @Sharada (2021-09-26 07:16 UTC)

<p>Hello,</p>
<p>I have a weird issue with the margin effect in the Segmentation module. The mask seems to grow when I try to shrink it. I apologize in advance if there might be a simple oversight.</p>
<p>Code:</p>
<p>slicer.app.processEvents()<br>
segmentEditorWidget.setActiveEffectByName(“Margin”)<br>
effect = segmentEditorWidget.activeEffect()<br>
effect.setParameter(“Operation”, “Shrink”)<br>
effect.setParameter(“MarginSize”, “1”)<br>
effect.self().onApply()</p>
<p>Before:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/49ff150068094b158ce09109d50b382a6b8ead93.jpeg" data-download-href="/uploads/short-url/ayBmHeUu47qy4s8ajqvsgbSqDMD.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/49ff150068094b158ce09109d50b382a6b8ead93_2_370x500.jpeg" alt="image" data-base62-sha1="ayBmHeUu47qy4s8ajqvsgbSqDMD" width="370" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/49ff150068094b158ce09109d50b382a6b8ead93_2_370x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/49ff150068094b158ce09109d50b382a6b8ead93_2_555x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/49ff150068094b158ce09109d50b382a6b8ead93.jpeg 2x" data-dominant-color="636E63"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">562×758 36.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>After:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/72ae9e6e0f3ce9dd7ad9b85703fe560e07f24e62.jpeg" data-download-href="/uploads/short-url/gmwy9nKnLVRvse75amhfRKbMuvU.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/72ae9e6e0f3ce9dd7ad9b85703fe560e07f24e62_2_361x500.jpeg" alt="image" data-base62-sha1="gmwy9nKnLVRvse75amhfRKbMuvU" width="361" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/72ae9e6e0f3ce9dd7ad9b85703fe560e07f24e62_2_361x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/72ae9e6e0f3ce9dd7ad9b85703fe560e07f24e62_2_541x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/72ae9e6e0f3ce9dd7ad9b85703fe560e07f24e62.jpeg 2x" data-dominant-color="647364"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">551×762 39.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>What am I doing wrong?</p>
<p>Thanks,<br>
Sharada</p>

---

## Post #2 by @Sharada (2021-09-26 23:08 UTC)

<p>Never mind, I had to pass in -1 instead of 1 for margin size. It seems a little strange to do when the operation is already specified as shrink.</p>

---

## Post #3 by @lassoan (2021-09-27 03:09 UTC)

<p>There is no such parameter of the Margin Effect as <code>Operation</code> or <code>MarginSize</code>. The list of parameter names are described in the [Developer documentation]) <a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/segmenteditor.html#margin" class="inline-onebox">Segment editor — 3D Slicer documentation</a>).</p>

---

## Post #4 by @Sharada (2021-09-27 03:16 UTC)

<p>Okay, makes perfect sense what I was doing wrong now. Thank you!</p>

---
