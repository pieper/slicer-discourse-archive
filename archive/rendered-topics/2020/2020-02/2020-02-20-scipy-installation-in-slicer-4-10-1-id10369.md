# Scipy installation in slicer 4.10.1

**Topic ID**: 10369
**Date**: 2020-02-20
**URL**: https://discourse.slicer.org/t/scipy-installation-in-slicer-4-10-1/10369

---

## Post #1 by @aseman (2020-02-20 19:12 UTC)

<p>Operating system: Linux<br>
Slicer version: 4.10.1</p>
<p>Hi 3D Slicer experts and all<br>
I want to install Scipy using pip.main([‘install’, ‘scipy’]) , but I get an error, as shown in the following figure. Can you help me with this problem?<br>
1- How can I install Scipy?<br>
2- what is the cause of this problem?<br>
Thanks a lot<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/580adec9fae65d6ec08ce3529dede59d83f057f2.jpeg" data-download-href="/uploads/short-url/cyRj1vCGn4NahKdKA1pg6JRiftg.jpeg?dl=1" title="scipy installation" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/580adec9fae65d6ec08ce3529dede59d83f057f2_2_690x145.jpeg" alt="scipy installation" data-base62-sha1="cyRj1vCGn4NahKdKA1pg6JRiftg" width="690" height="145" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/580adec9fae65d6ec08ce3529dede59d83f057f2_2_690x145.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/580adec9fae65d6ec08ce3529dede59d83f057f2_2_1035x217.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/580adec9fae65d6ec08ce3529dede59d83f057f2_2_1380x290.jpeg 2x" data-dominant-color="808283"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">scipy installation</span><span class="informations">3920×828 2.07 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2020-02-20 19:19 UTC)

<p>You need to use Slicer-4.11.x and install scipy by typing</p>
<pre><code>pip_install('scipy')
</code></pre>
<p>in Slicer’s python console (it is just a shortcut for launching pip install).</p>

---
