---
topic_id: 10948
title: "Screencapture Png Stack Looks Flattened"
date: 2020-03-31
url: https://discourse.slicer.org/t/10948
---

# ScreenCapture - PNG stack looks flattened

**Topic ID**: 10948
**Date**: 2020-03-31
**URL**: https://discourse.slicer.org/t/screencapture-png-stack-looks-flattened/10948

---

## Post #1 by @KTing (2020-03-31 21:24 UTC)

<p>Hello,</p>
<p>When I re-load images from the Screen Capture module back into Slicer, my volume appears flattened. Attached is an example using the MRHead sample data and generating 50 PNGs. All of the slices are generated but the volume rendering does not look correct</p>
<p>This is fixed by using a larger number of PNG’s, but I’m wondering if it’s possible to scale this automatically such that I can generate 50 PNG’s and just get a smaller but correctly-scaled model?</p>
<p>Thank you.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3bd12523c46e080910d27e130388da8f0973836b.png" data-download-href="/uploads/short-url/8xagfc5wbkCPLExzqqEy6BQK3rB.png?dl=1" title="MRHead - ScreenCapture50slices" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3bd12523c46e080910d27e130388da8f0973836b_2_457x500.png" alt="MRHead - ScreenCapture50slices" data-base62-sha1="8xagfc5wbkCPLExzqqEy6BQK3rB" width="457" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3bd12523c46e080910d27e130388da8f0973836b_2_457x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3bd12523c46e080910d27e130388da8f0973836b_2_685x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3bd12523c46e080910d27e130388da8f0973836b.png 2x" data-dominant-color="3B3C45"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">MRHead - ScreenCapture50slices</span><span class="informations">802×877 147 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2020-03-31 21:27 UTC)

<p>You lost the correct z spacing, when you saved the volume as PNG stack. PNG doesn’t retain this information. You can manually enter the correct spacing (I think it is 1.3mm for the original MRHead.NRRD) using the <code>Volumes</code> module</p>

---

## Post #3 by @lassoan (2020-03-31 21:59 UTC)

<p>Note that screen capture is a lossy operation (you lose dynamic range, window/level settings are burnt in, etc), so do not use it for data export. It is for presentations, testing, etc.</p>

---

## Post #4 by @KTing (2020-04-01 18:25 UTC)

<p>Thanks! 1.3mm looks about right for MRHead.</p>

---

## Post #5 by @KTing (2020-04-01 18:28 UTC)

<p>Is there another method you would recommend for data export?<br>
I’m working with segmentations which I’ve exported to labelmaps, then volumeNodes.</p>
<p>I also tried using SlicerFab bitmap generator but kept getting copies of one layer rather than slices throughout the whole volume.</p>

---

## Post #6 by @muratmaga (2020-04-01 18:40 UTC)

<p>Why aren’t you saving them NRRD? It is not clear to me what you are trying to accomplish. The cross-sections above seems like regular slices from the sample data, not an output SlicerFab. So, the best would be use the default volume format, NRRD which will retain slice spacing.</p>

---

## Post #7 by @KTing (2020-04-01 18:45 UTC)

<p>The application I’m working on creates voxel objects by loading in stacks of PNG’s. I have some segmentation files (NRRD) in Slicer and the goal is to export them to PNGs so I can load them into my application</p>

---

## Post #8 by @muratmaga (2020-04-01 19:07 UTC)

<p>I think all you need to do is to convert your segmentation to label map and then save it NRRD. I don’t think slicer output a volume as sequence of PNG files through the save dialog box, and using the screen capture has the potential issues <a class="mention" href="/u/lassoan">@lassoan</a> pointed out (although I am not sure how relevant they are for label maps). You can use Fiji to convert your NRRD to PNG sequence…</p>

---

## Post #9 by @lassoan (2020-04-04 21:16 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="8" data-topic="10948">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>You can use Fiji to convert your NRRD to PNG sequence…</p>
</blockquote>
</aside>
<p>You can write out a 3D numpy array as a png sequence using a few lines of Python code (you can find examples by web search; you can use <code>pip_install</code> command in Slicer to install any additional packages for png writing).</p>

---
