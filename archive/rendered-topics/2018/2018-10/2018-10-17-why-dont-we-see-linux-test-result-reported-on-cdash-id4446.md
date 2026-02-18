# Why don't we see Linux test result reported on CDash?

**Topic ID**: 4446
**Date**: 2018-10-17
**URL**: https://discourse.slicer.org/t/why-dont-we-see-linux-test-result-reported-on-cdash/4446

---

## Post #1 by @lassoan (2018-10-17 17:47 UTC)

<p>Why don’t we see Linux test results?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f45921b829948ec46d19fbd99b05504ed63d30e.png" data-download-href="/uploads/short-url/bjgM2dQqBxzMksCDroVDw8XH0tM.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f45921b829948ec46d19fbd99b05504ed63d30e_2_690x97.png" alt="image" data-base62-sha1="bjgM2dQqBxzMksCDroVDw8XH0tM" width="690" height="97" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f45921b829948ec46d19fbd99b05504ed63d30e_2_690x97.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f45921b829948ec46d19fbd99b05504ed63d30e_2_1035x145.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f45921b829948ec46d19fbd99b05504ed63d30e_2_1380x194.png 2x" data-dominant-color="B2C4C1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1517×215 34.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @jcfr (2018-10-17 17:49 UTC)

<aside class="quote no-group quote-modified" data-username="lassoan" data-post="3" data-topic="4422" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"><a href="https://discourse.slicer.org/t/update-slicer-4-10-release-will-be-initiated-tomorrow-morning/4422/3">Update: Slicer 4.10 release will be initiated tomorrow morning</a></div>
<blockquote>
<p>Why don’t we see Linux test results?</p>
</blockquote>
</aside>
<p>Because, we haven’t updated the <a href="https://github.com/thewtex/docker-opengl">docker-opengl</a> image to work with the new VTK OpenGL backend</p>

---

## Post #3 by @ihnorton (2018-10-17 18:06 UTC)

<p>Debian sid and testing have mesa 18. Seems to work fine with volume rendering on recent nightly (10-14).</p>

---
