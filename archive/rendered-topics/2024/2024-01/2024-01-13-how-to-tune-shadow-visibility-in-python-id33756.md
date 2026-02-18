# How to tune Shadow Visibility in python?

**Topic ID**: 33756
**Date**: 2024-01-13
**URL**: https://discourse.slicer.org/t/how-to-tune-shadow-visibility-in-python/33756

---

## Post #1 by @chir.set (2024-01-13 10:45 UTC)

<p>Hi,</p>
<p>The 3D viewers now default to ‘Shadows visibility’ enabled at 25%. The picture below shows the effect on the right. The left image, with this setting off, is brighter and more comfortable to look at. It’s not just comfort, distinction between structures is more obvious.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/2352206b6b34bd322bfcd57198289a56ee0059f0.jpeg" data-download-href="/uploads/short-url/52sFlRDEUtpq5bjV4iK6rl0N19C.jpeg?dl=1" title="bright_dim" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/2352206b6b34bd322bfcd57198289a56ee0059f0.jpeg" alt="bright_dim" data-base62-sha1="52sFlRDEUtpq5bjV4iK6rl0N19C" width="690" height="417" data-dominant-color="52362C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">bright_dim</span><span class="informations">966×584 78.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I didn’t find a tunable in ‘Application settings / Volume rendering’ to either disable ‘Shadows visibility’ or set it at 100%. There is probably a few lines we could drop in slicerrc.py to enable this. Could you hint at the code that can do that?</p>
<p>Thank you.</p>

---

## Post #2 by @chir.set (2024-01-13 15:18 UTC)

<p>Ok, using this in slicerrc.py, in case it might be of interest to anyone. The 3D views get updated, but not the controlling widget.</p>
<pre><code class="lang-auto">def noShadows():
    nb = slicer.app.layoutManager().threeDViewCount
    for x in range(0, nb):
        view = slicer.app.layoutManager().threeDWidget(x).threeDView()
        renderWindow = view.renderWindow()
        view.setShadowsVisibility(False)
        renderWindow.Render()
</code></pre>

---

## Post #3 by @lassoan (2024-01-14 02:45 UTC)

<p>Shadows are applied to both surface and volume rendering, therefore defaults are specified in Views section of application settings.</p>
<p>You can conveniently configure these settings along with additional light controls in Lights module (in Sandbox extension).</p>

---

## Post #4 by @chir.set (2024-01-14 07:51 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="33756">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Views section of application settings</p>
</blockquote>
</aside>
<p>Great, that’s the right way to set global settings, than you very much.</p>

---
