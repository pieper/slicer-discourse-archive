# 3D view not working on Linux

**Topic ID**: 34741
**Date**: 2024-03-06
**URL**: https://discourse.slicer.org/t/3d-view-not-working-on-linux/34741

---

## Post #1 by @casper_belier (2024-03-06 13:23 UTC)

<p>Hi, I’m on Linux mint 21, and I am using Slicer 5.6.1.</p>
<p>I cannot see a 3D view, even after pressing the center view button.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a9728aeb90a6d7ce6d1fbd18901cd19eaee40037.png" data-download-href="/uploads/short-url/ob068CqbJSsfMPGz9afnFGZ558b.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a9728aeb90a6d7ce6d1fbd18901cd19eaee40037_2_690x432.png" alt="image" data-base62-sha1="ob068CqbJSsfMPGz9afnFGZ558b" width="690" height="432" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a9728aeb90a6d7ce6d1fbd18901cd19eaee40037_2_690x432.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a9728aeb90a6d7ce6d1fbd18901cd19eaee40037.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a9728aeb90a6d7ce6d1fbd18901cd19eaee40037.png 2x" data-dominant-color="88868C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">957×600 115 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @cpinter (2024-03-06 13:49 UTC)

<p>The 3D view is in the top right corner. It seems to be working. Do you have some kind of data in the scene that is supposed to show up there but doesn’t? The question is not very clear, and the screenshot does not show the scene content.</p>

---

## Post #3 by @jcfr (2024-03-06 17:04 UTC)

<aside class="quote no-group" data-username="casper_belier" data-post="1" data-topic="34741">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/casper_belier/48/66543_2.png" class="avatar"> casper_belier:</div>
<blockquote>
<p>I cannot see a 3D view, even after pressing the center view button.</p>
</blockquote>
</aside>
<p>To display data in the 3D view, you could for example enable volume rendering of the corresponding dataset.</p>
<p>See <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/volumerendering.html" class="inline-onebox">Volume rendering — 3D Slicer documentation</a></p>

---
