---
topic_id: 31566
title: "Load Scene Into Slicer"
date: 2023-09-05
url: https://discourse.slicer.org/t/31566
---

# Load scene into Slicer

**Topic ID**: 31566
**Date**: 2023-09-05
**URL**: https://discourse.slicer.org/t/load-scene-into-slicer/31566

---

## Post #1 by @Kening_Zhang (2023-09-05 12:34 UTC)

<p>Dear developers,<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/896c0fb8deccc66625e9ea25fa5778f8f424f849.png" data-download-href="/uploads/short-url/jBGVU9Vl5rJfVnPhikojIoImb2h.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/896c0fb8deccc66625e9ea25fa5778f8f424f849.png" alt="image" data-base62-sha1="jBGVU9Vl5rJfVnPhikojIoImb2h" width="690" height="96" data-dominant-color="525C67"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">984×138 20.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
As can be seen in the code, I try to load a scene in Slicer, but errors happened,<br>
it says:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6ff1716ab709e5da4ec6c065c966c229b51f1a94.png" data-download-href="/uploads/short-url/fYihT896RQw96SVa3C9ofiO5ITq.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6ff1716ab709e5da4ec6c065c966c229b51f1a94_2_690x318.png" alt="image" data-base62-sha1="fYihT896RQw96SVa3C9ofiO5ITq" width="690" height="318" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6ff1716ab709e5da4ec6c065c966c229b51f1a94_2_690x318.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6ff1716ab709e5da4ec6c065c966c229b51f1a94_2_1035x477.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6ff1716ab709e5da4ec6c065c966c229b51f1a94_2_1380x636.png 2x" data-dominant-color="FDE0E0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1406×648 161 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
and I tried to load it just dragging the file into Slicer, error shows:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/facdeb27d16162078b1e136eb2487d479ff44391.png" data-download-href="/uploads/short-url/zMIxRjr5T3V5shsP7fa2MaKPkKl.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/facdeb27d16162078b1e136eb2487d479ff44391_2_690x432.png" alt="image" data-base62-sha1="zMIxRjr5T3V5shsP7fa2MaKPkKl" width="690" height="432" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/facdeb27d16162078b1e136eb2487d479ff44391_2_690x432.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/facdeb27d16162078b1e136eb2487d479ff44391.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/facdeb27d16162078b1e136eb2487d479ff44391.png 2x" data-dominant-color="D6D4D4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">842×528 52.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
It seems a vtp file has errors, from my point of view, T_PLIC_left seems to be a empty file. I dont know how to settle this problem,<br>
by the way, other errors show but I dont know which line of code bring this, such as this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f0542e75290fb95013a64259757bc190651003f.png" data-download-href="/uploads/short-url/fQ8gQ0lat1parHjbqajjeGt1cez.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6f0542e75290fb95013a64259757bc190651003f_2_690x78.png" alt="image" data-base62-sha1="fQ8gQ0lat1parHjbqajjeGt1cez" width="690" height="78" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6f0542e75290fb95013a64259757bc190651003f_2_690x78.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6f0542e75290fb95013a64259757bc190651003f_2_1035x117.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6f0542e75290fb95013a64259757bc190651003f_2_1380x156.png 2x" data-dominant-color="FDE1E1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1408×160 25.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Best wishes,<br>
Joshua</p>

---

## Post #2 by @pieper (2023-09-05 13:05 UTC)

<aside class="quote no-group" data-username="Kening_Zhang" data-post="1" data-topic="31566">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kening_zhang/48/65641_2.png" class="avatar"> Kening_Zhang:</div>
<blockquote>
<p>T_PLIC_left seems to be a empty file</p>
</blockquote>
</aside>
<p>Please check with other versions of slicer to see if this is a regression and if so provide a dataset that can be used for debugging.</p>

---

## Post #3 by @cpinter (2023-09-05 14:33 UTC)

<p>Do you have the SlicerDMRI extension installed? Based on the error it seems that it would be necessary.</p>

---

## Post #4 by @Kening_Zhang (2023-09-05 14:34 UTC)

<p>Yes I have installed it in my Slicer.</p>

---

## Post #5 by @lassoan (2023-09-05 16:38 UTC)

<aside class="quote no-group" data-username="Kening_Zhang" data-post="1" data-topic="31566">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kening_zhang/48/65641_2.png" class="avatar"> Kening_Zhang:</div>
<blockquote>
<p>It seems a vtp file has errors, from my point of view, T_PLIC_left seems to be a empty file. I dont know how to settle this problem,</p>
</blockquote>
</aside>
<p>If you don’t expect that file to contain some valid content then you can ignore this error. VTK may report it as an error when you attempt to read or write an empty file, while it may be normal that a fiber is empty.</p>
<p>I would suggest you to report this error to the SlicerDMRI extension repository. You can add a note that a possible fix would be to apply the same technique as it is done in the model storage node: use the <a href="https://github.com/Slicer/Slicer/blob/4540594f5ff293cb387fd252e24e32be13e377c8/Libs/MRML/Core/vtkMRMLModelStorageNode.cxx#L160C32-L160C45"><code>SkippedNoData</code> write state</a> to indicate that the file is expected to be empty.</p>

---

## Post #6 by @Kening_Zhang (2023-09-05 17:02 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="31566">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If you don’t expect that file to contain some valid content then you can ignore this error. VTK may report it as an error when you attempt to read or write an empty file, while it may be normal that a fiber is empty.</p>
<p>I would suggest you to report this error to the SlicerDMRI extension repository. You can add a note that a possible fix would be to apply the same technique as it is done in the model storage node: use the <a href="https://github.com/Slicer/Slicer/blob/4540594f5ff293cb387fd252e24e32be13e377c8/Libs/MRML/Core/vtkMRMLModelStorageNode.cxx#L160C32-L160C45" rel="noopener nofollow ugc"><code>SkippedNoData</code> write state</a> to indicate that the file is expected to be empty.</p>
</blockquote>
</aside>
<p>Yes this is what I want, it should still load the scene even there are some empty fibers.</p>

---

## Post #7 by @lassoan (2023-09-07 18:31 UTC)

<p>The scene is still loaded. The error just lets you know that there were fiber nodes that were empty, so you can ignore them. It would be still nice to fix to avoid having these false alarms.</p>
<p>Have you submitted a bug report to SlicerDMRI? Could you post the link here for reference? Thank you.</p>

---

## Post #8 by @Kening_Zhang (2023-09-08 07:21 UTC)

<p>Yes, I have reported. Here is the link: <a href="https://discourse.slicer.org/t/load-scene-into-slicer-with-empty-vtk-errors/31615">Load scene into Slicer with empty vtk errors - Community / SlicerDMRI - 3D Slicer Community</a>.<br>
Thanks so much.</p>

---

## Post #9 by @lassoan (2023-09-08 11:30 UTC)

<p>Thanks for the link. However, I meant to file a bug report in the <a href="https://github.com/SlicerDMRI/SlicerDMRI/issues">SlicerDMRI repository’s bugtracker</a>. There is a higher chance that maintainers will notice and eventually fix it.</p>

---

## Post #10 by @Kening_Zhang (2023-09-08 14:51 UTC)

<p>I am sorry for misunderstanding that. I reported the same one in bugtracker now, here is the link: <a href="https://github.com/SlicerDMRI/SlicerDMRI/issues/181" rel="noopener nofollow ugc">Load scene into Slicer with empty vtk errors · Issue #181 · SlicerDMRI/SlicerDMRI (github.com)</a></p>

---
