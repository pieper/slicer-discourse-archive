# How to set the line width of a model in slice display?

**Topic ID**: 19300
**Date**: 2021-08-22
**URL**: https://discourse.slicer.org/t/how-to-set-the-line-width-of-a-model-in-slice-display/19300

---

## Post #1 by @jumbojing (2021-08-22 23:58 UTC)

<p>How to set the line width of a modle in slice display by python?</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a>@Juicy@jamesobutler <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a><br>
Like this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac47869c5a2e6df8d316007548d44cefaa636ee8.jpeg" data-download-href="/uploads/short-url/oA3mPH3nhJTGH2SquZGnZKIXHCw.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ac47869c5a2e6df8d316007548d44cefaa636ee8_2_690x371.jpeg" alt="image" data-base62-sha1="oA3mPH3nhJTGH2SquZGnZKIXHCw" width="690" height="371" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ac47869c5a2e6df8d316007548d44cefaa636ee8_2_690x371.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ac47869c5a2e6df8d316007548d44cefaa636ee8_2_1035x556.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ac47869c5a2e6df8d316007548d44cefaa636ee8_2_1380x742.jpeg 2x" data-dominant-color="727372"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1035 138 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @jumbojing (2021-08-23 10:54 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>@Juicy@jamesobutler <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a></p>
<p>I try:</p>
<pre><code class="lang-auto">mp.SetLineWith(13)
</code></pre>
<p>the line width fo the modle is changed in 3d slice with line frame only…</p>

---

## Post #3 by @lassoan (2021-08-23 11:46 UTC)

<p>Yes, that is how it is supposed to work. If you need the model of a larger diameter needle, screw, etc. then you can create or load a model of a larger object or apply a scaling transform to your the model (linear transform of a 4x4 diagonal matrix, with values &gt;1.0 in one or more of the first 3 values, and 1.0 as the last value).</p>

---
