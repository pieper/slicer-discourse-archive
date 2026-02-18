# Issue when pip_install("matplotlib wxPython")

**Topic ID**: 16604
**Date**: 2021-03-17
**URL**: https://discourse.slicer.org/t/issue-when-pip-install-matplotlib-wxpython/16604

---

## Post #1 by @siaeleni (2021-03-17 20:20 UTC)

<p>Hello,</p>
<p>I try to install <code>pip_install("matplotlib wxPython")</code> on Slicer Stable version 4.11.20210226 and it freezes and does not respond. This is what I get in Python Interactor:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/4655b4e0fcba88b1083671583d53832d432f4431.jpeg" data-download-href="/uploads/short-url/a2d2ZZxbGNQGtZHJ5SjnbSNJ5Rv.jpeg?dl=1" title="issue" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4655b4e0fcba88b1083671583d53832d432f4431_2_690x88.jpeg" alt="issue" data-base62-sha1="a2d2ZZxbGNQGtZHJ5SjnbSNJ5Rv" width="690" height="88" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4655b4e0fcba88b1083671583d53832d432f4431_2_690x88.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4655b4e0fcba88b1083671583d53832d432f4431_2_1035x132.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4655b4e0fcba88b1083671583d53832d432f4431_2_1380x176.jpeg 2x" data-dominant-color="F7F7F7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">issue</span><span class="informations">1779×228 78.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Do you have any idea why?</p>
<p>Thanks,<br>
Eleni</p>

---

## Post #2 by @jcfr (2021-03-17 21:36 UTC)

<p>I suggest you try again using the following command:</p>
<pre><code class="lang-auto">pip_install("matplotlib wxPython --verbose")
</code></pre>
<p>This should help understand which command is blocking …</p>

---
