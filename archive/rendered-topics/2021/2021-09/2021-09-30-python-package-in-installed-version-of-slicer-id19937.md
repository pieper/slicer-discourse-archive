# Python package in installed version of slicer

**Topic ID**: 19937
**Date**: 2021-09-30
**URL**: https://discourse.slicer.org/t/python-package-in-installed-version-of-slicer/19937

---

## Post #1 by @riep (2021-09-30 15:44 UTC)

<p>Hi everyone,<br>
We are working on a slicelet on Slicer v4.11.20210226. We are installing a library call weasyprint during compilation time. Everything is working fine in development environment. However, when we generate the installer, the application crashes at</p>
<blockquote>
<p>import weasyprint</p>
</blockquote>
<p>and generate an error when trying to do:</p>
<blockquote>
<p>from PIL import Image</p>
</blockquote>
<p>Same thing on slicer stable version. However, on the preview version, everything is fine.<br>
Could anyone give me a hint to know what could have solved this issue at install?</p>
<p>Cheers,<br>
Pierre</p>

---

## Post #2 by @lassoan (2021-09-30 15:59 UTC)

<p>weasyprint has tons of dependencies - see <a href="https://github.com/Kozea/WeasyPrint/blob/master/docs/first_steps.rst" class="inline-onebox">WeasyPrint/first_steps.rst at master · Kozea/WeasyPrint · GitHub</a>. You need to make sure that all those dependencies are bundled with your application as it was recommended <a href="https://discourse.slicer.org/t/python-package-installation/19496">here</a>.</p>

---

## Post #3 by @jamesobutler (2021-09-30 16:02 UTC)

<p>Is your platform Linux?</p>
<p>You might be experiencing the issue discussed below which was tracked as <a href="https://github.com/Slicer/Slicer/issues/5474" class="inline-onebox" rel="noopener nofollow ugc">Importing the numpy C-extensions failed. [slicer 4.11.20200930, archlinux] · Issue #5474 · Slicer/Slicer · GitHub</a> and fixed in mid-March 2021 (after the Slicer 4.11.20210226 release).</p>
<aside class="quote quote-modified" data-post="1" data-topic="14448">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fernando/48/5640_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/slicer-4-11-20200930-cant-import-pip-installed-pillow-on-linux/14448">Slicer-4.11.20200930: Can't import pip-installed Pillow on Linux</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi all, 
I can’t run the line below in the current Linux stable (and preview) release, after running pip_install('Pillow'): 
&gt;&gt;&gt; from PIL import Image
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
  File "/home/fernando/opt/Slicer-4.11.20200930-linux-amd64/lib/Python/lib/python3.6/site-packages/PIL/Image.py", line 94, in &lt;module&gt;
    from . import _imaging as core
ImportError: /home/fernando/opt/Slicer-4.11.20200930-linux-amd64/lib/Python/lib/python3.6/site-packages/…
  </blockquote>
</aside>


---

## Post #4 by @riep (2021-09-30 16:30 UTC)

<p>Thank you both. Yes, we are on linux, I will check this, it looks interesting!! I let you know.<br>
Pierre</p>

---
