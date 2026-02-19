---
topic_id: 22376
title: "Build And Update Translation File"
date: 2022-03-08
url: https://discourse.slicer.org/t/22376
---

# Build and update translation file

**Topic ID**: 22376
**Date**: 2022-03-08
**URL**: https://discourse.slicer.org/t/build-and-update-translation-file/22376

---

## Post #1 by @syrjay (2022-03-08 15:05 UTC)

<p>Hello,<br>
I have some errors when I try to build slicer, in the step for run the command make -j4, I got this :<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d10a4f800ec3d4ffcec4ac6a3aa6f3ce49d592bb.png" data-download-href="/uploads/short-url/tPfSEKWtIjVY95cJXlB1xfIxEiD.png?dl=1" title="Capture d’écran 2022-03-05 à 22.06.50" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d10a4f800ec3d4ffcec4ac6a3aa6f3ce49d592bb_2_690x442.png" alt="Capture d’écran 2022-03-05 à 22.06.50" data-base62-sha1="tPfSEKWtIjVY95cJXlB1xfIxEiD" width="690" height="442" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d10a4f800ec3d4ffcec4ac6a3aa6f3ce49d592bb_2_690x442.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d10a4f800ec3d4ffcec4ac6a3aa6f3ce49d592bb_2_1035x663.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d10a4f800ec3d4ffcec4ac6a3aa6f3ce49d592bb.png 2x" data-dominant-color="342C2D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture d’écran 2022-03-05 à 22.06.50</span><span class="informations">1144×734 101 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/48599f41d1d8f96de7dbffdc2f9b2aa409a0a904.png" data-download-href="/uploads/short-url/ak2ok7G3rWQ9q4pXGy2nne61lMU.png?dl=1" title="Capture d’écran 2022-03-05 à 22.07.02" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/48599f41d1d8f96de7dbffdc2f9b2aa409a0a904_2_690x88.png" alt="Capture d’écran 2022-03-05 à 22.07.02" data-base62-sha1="ak2ok7G3rWQ9q4pXGy2nne61lMU" width="690" height="88" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/48599f41d1d8f96de7dbffdc2f9b2aa409a0a904_2_690x88.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/48599f41d1d8f96de7dbffdc2f9b2aa409a0a904_2_1035x132.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/48599f41d1d8f96de7dbffdc2f9b2aa409a0a904.png 2x" data-dominant-color="302C2D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture d’écran 2022-03-05 à 22.07.02</span><span class="informations">1144×146 20 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
So after this, I can’t run slicer with /opt/s/Slicer-build/Slicer, “no such file or directory”.</p>
<p>Also when I try to update translation file, I was working as well with Qt6, but as it is the 5 version of Qt with is recommended, I install it but  I got this error :<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bdbd06ac3890aeee96b053050fe4c62adba9f85e.png" data-download-href="/uploads/short-url/r4ve9WfxXSPt1vKAHMAkjlTdPPg.png?dl=1" title="Capture d’écran 2022-03-05 à 22.05.09" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bdbd06ac3890aeee96b053050fe4c62adba9f85e_2_690x398.png" alt="Capture d’écran 2022-03-05 à 22.05.09" data-base62-sha1="r4ve9WfxXSPt1vKAHMAkjlTdPPg" width="690" height="398" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bdbd06ac3890aeee96b053050fe4c62adba9f85e_2_690x398.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bdbd06ac3890aeee96b053050fe4c62adba9f85e_2_1035x597.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bdbd06ac3890aeee96b053050fe4c62adba9f85e_2_1380x796.png 2x" data-dominant-color="393739"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture d’écran 2022-03-05 à 22.05.09</span><span class="informations">1536×888 134 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>developper guide : <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/macos.html#prerequisites" class="inline-onebox" rel="noopener nofollow ugc">macOS — 3D Slicer documentation</a></p>

---

## Post #2 by @lassoan (2022-03-08 15:21 UTC)

<aside class="quote no-group" data-username="syrjay" data-post="1" data-topic="22376">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/syrjay/48/14577_2.png" class="avatar"> syrjay:</div>
<blockquote>
<p>I have some errors when I try to build slicer, in the step for run the command make -j4, I got this :</p>
</blockquote>
</aside>
<p>It seems that you haven’t installed qtscript Qt component. See in the Slicer build instructions</p>
<blockquote>
<p>make sure to select <code>qtscript</code> and <code>qtwebengine</code> components</p>
</blockquote>
<p>(<a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/macos.html" class="inline-onebox">macOS — 3D Slicer documentation</a>)</p>
<aside class="quote no-group" data-username="syrjay" data-post="1" data-topic="22376">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/syrjay/48/14577_2.png" class="avatar"> syrjay:</div>
<blockquote>
<p>Also when I try to update translation file, I was working as well with Qt6, but as it is the 5 version of Qt with is recommended, I install it but I got this error :</p>
</blockquote>
</aside>
<p>This problem is fixed in recent Slicer Preview Releases (after 2022-02-23).</p>

---
