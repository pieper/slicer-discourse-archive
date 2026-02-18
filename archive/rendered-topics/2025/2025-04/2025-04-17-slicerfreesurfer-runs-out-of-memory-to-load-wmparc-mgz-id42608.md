# SlicerFreeSurfer runs out of memory to load wmparc.mgz

**Topic ID**: 42608
**Date**: 2025-04-17
**URL**: https://discourse.slicer.org/t/slicerfreesurfer-runs-out-of-memory-to-load-wmparc-mgz/42608

---

## Post #1 by @tbillah (2025-04-17 18:47 UTC)

<p>Slicer-5.6.1</p>
<p><a class="mention" href="/u/pieper">@pieper</a> asked us to use SlicerFreeSurfer extension. We installed it. But when trying to load a <code>wmparc.mgz</code> file, we get the following:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/ed7c1f4371a659c1096d9e8bed6576f9358cbfb3.png" data-download-href="/uploads/short-url/xST5DulTkiOFTiO9J8IyFmumAD1.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/ed7c1f4371a659c1096d9e8bed6576f9358cbfb3_2_690x320.png" alt="image" data-base62-sha1="xST5DulTkiOFTiO9J8IyFmumAD1" width="690" height="320" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/ed7c1f4371a659c1096d9e8bed6576f9358cbfb3_2_690x320.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/ed7c1f4371a659c1096d9e8bed6576f9358cbfb3.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/ed7c1f4371a659c1096d9e8bed6576f9358cbfb3.png 2x" data-dominant-color="A1A0A1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">760×353 33.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Console error is:</p>
<blockquote>
<p>Slicer has caught an application error, please save your work and restart.\n\nThe application has run out of memory. Increasing swap size in system settings or adding more RAM may fix this issue.\n\nIf you have a repeatable sequence of steps that causes this message, please report the issue following instructions available at <a href="https://slicer.org" rel="noopener nofollow ugc">https://slicer.org</a>\n\n\nThe message detail is:\n\nException thrown in event: std::bad_alloc</p>
</blockquote>
<p>But the <code>wmparc.mgz</code> loads fine in a fresh Slicer-5.6.1 where there is no SlicerFreeSurfer extension.</p>
<p>Please advise.</p>

---

## Post #2 by @pieper (2025-04-17 20:05 UTC)

<p><a class="mention" href="/u/tbillah">@tbillah</a> please report this on the extension’s github issues.  Include a link to this tread too.</p>

---
