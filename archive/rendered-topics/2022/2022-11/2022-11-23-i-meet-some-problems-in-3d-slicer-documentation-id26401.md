# I meet some problems in 3D slicer documentation

**Topic ID**: 26401
**Date**: 2022-11-23
**URL**: https://discourse.slicer.org/t/i-meet-some-problems-in-3d-slicer-documentation/26401

---

## Post #1 by @f1oNae (2022-11-23 09:15 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/43e2bcece5396750e345408304cd92227ab71723.png" data-download-href="/uploads/short-url/9GxM0SBPgJRtBJLLHzPN2CN4K55.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/43e2bcece5396750e345408304cd92227ab71723_2_690x43.png" alt="image" data-base62-sha1="9GxM0SBPgJRtBJLLHzPN2CN4K55" width="690" height="43" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/43e2bcece5396750e345408304cd92227ab71723_2_690x43.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/43e2bcece5396750e345408304cd92227ab71723_2_1035x64.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/43e2bcece5396750e345408304cd92227ab71723_2_1380x86.png 2x" data-dominant-color="EBEBEB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1864×118 30.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/cameras.html" rel="noopener nofollow ugc">Cameras — 3D Slicer documentation</a><br>
I can’t find the selection “Create New View”.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/2061440431e4ce43c2d23fd520a87bd15c98143a.png" data-download-href="/uploads/short-url/4CrFwPIs8EzHZioRGkBpGBN1Ysq.png?dl=1" title="20221123171216" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/2061440431e4ce43c2d23fd520a87bd15c98143a.png" alt="20221123171216" data-base62-sha1="4CrFwPIs8EzHZioRGkBpGBN1Ysq" width="690" height="223" data-dominant-color="E5ECF0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">20221123171216</span><span class="informations">879×285 10.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This question has been torturing me.I’d apperaciate it if anyone can give me some help.</p>

---

## Post #2 by @chir.set (2022-11-23 11:16 UTC)

<p>There seem to be a documentation bug, probably.</p>
<p>You can still create up to 3 3D views using the layout button :</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e4fdf2d4ce219a61b50a00bfa4cc71516c0f6f2d.png" alt="layout_button" data-base62-sha1="wFKWCFayjKdiNCkwqZHyoGP5J2R" width="58" height="43"></p>

---

## Post #3 by @f1oNae (2022-11-23 11:25 UTC)

<p>Thanks for your help.But if I need more 3d views,what should I do?</p>

---

## Post #4 by @chir.set (2022-11-23 12:24 UTC)

<aside class="quote no-group" data-username="f1oNae" data-post="3" data-topic="26401">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/f1onae/48/17418_2.png" class="avatar"> f1oNae:</div>
<blockquote>
<p>if I need more 3d views</p>
</blockquote>
</aside>
<ol>
<li>
<p>Do you need more than three 3D views ?</p>
</li>
<li>
<p>You may start another instance of Slicer and load the same data.</p>
</li>
<li>
<p>You may consider using Python scripting, I only guess it should be possible.</p>
</li>
<li>
<p>If that is beyond your skills, you may hire an expert to write specific code for that expectation.</p>
</li>
<li>
<p>You may ask Slicer devs if they can consider adding this feature.</p>
</li>
</ol>

---

## Post #5 by @mikebind (2022-11-23 18:28 UTC)

<p>Using custom layouts, you can have as many 3D views as you want.  Here is some example code for creating a custom layout:  <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#customize-view-layout" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a></p>

---

## Post #6 by @f1oNae (2022-11-24 02:53 UTC)

<p>thanks,that really works</p>

---
