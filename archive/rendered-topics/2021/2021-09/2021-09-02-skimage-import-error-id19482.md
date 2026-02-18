# Skimage import error

**Topic ID**: 19482
**Date**: 2021-09-02
**URL**: https://discourse.slicer.org/t/skimage-import-error/19482

---

## Post #1 by @shatz (2021-09-02 10:00 UTC)

<p>When importing the <code>io</code> module from skimage, I get this error: <code>ImportError: /projects/msieve_dev3/usr/shats/apps/Slicer-4.11.20210226-linux-amd64/lib/Python/lib/python3.6/site-packages/PIL/_imaging.cpython-36m-x86_64-linux-gnu.so: ELF load command address/offset not properly aligned</code>. The other modules ive used work fine.</p>
<p>Ive tried to pip_uninstall and then reinstall scikit-image, to no avail. Seems like some people on the internet get this error in different situations when the “<a href="https://en.wikipedia.org/wiki/Strip_(Unix)" rel="noopener nofollow ugc">strip</a>” program, so I wonder if slicer is using that internally.</p>
<p>In any case, does anyone have a fix for this?</p>
<p>OS: Linux<br>
Slicer Version: 4.11.20210226</p>

---

## Post #2 by @lassoan (2021-09-02 23:57 UTC)

<p>Information in this issue may help: <a href="https://github.com/Slicer/Slicer/issues/5474">https://github.com/Slicer/Slicer/issues/5474</a></p>

---

## Post #3 by @shatz (2021-09-04 19:40 UTC)

<p>Thanks! apparently this was fixed on Mar 13 but the build I downloaded was only a few weeks before the fix was released!</p>

---
