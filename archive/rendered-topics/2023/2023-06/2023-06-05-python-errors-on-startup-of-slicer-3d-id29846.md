---
topic_id: 29846
title: "Python Errors On Startup Of Slicer 3D"
date: 2023-06-05
url: https://discourse.slicer.org/t/29846
---

# Python Errors on startup of Slicer 3D

**Topic ID**: 29846
**Date**: 2023-06-05
**URL**: https://discourse.slicer.org/t/python-errors-on-startup-of-slicer-3d/29846

---

## Post #1 by @prathamtikki (2023-06-05 13:28 UTC)

<p>Operating system: MacOS 13.2.1<br>
Slicer version: 5.2.2</p>
<p>On startup of a freshly downloaded stable release of Slicer 5.2.2, I face all these python errors. I do not know where the problem is and how to over come. Could someone please share some insight into the same?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ff1c67e8903d10eb9892dada709e29cf2850c1c6.jpeg" data-download-href="/uploads/short-url/AoOC5oRlpfQlQDzFS8VOaIiaivI.jpeg?dl=1" title="Screenshot 2023-06-05 at 11.05.34 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff1c67e8903d10eb9892dada709e29cf2850c1c6_2_517x336.jpeg" alt="Screenshot 2023-06-05 at 11.05.34 AM" data-base62-sha1="AoOC5oRlpfQlQDzFS8VOaIiaivI" width="517" height="336" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff1c67e8903d10eb9892dada709e29cf2850c1c6_2_517x336.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff1c67e8903d10eb9892dada709e29cf2850c1c6_2_775x504.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff1c67e8903d10eb9892dada709e29cf2850c1c6_2_1034x672.jpeg 2x" data-dominant-color="352727"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-06-05 at 11.05.34 AM</span><span class="informations">1920×1249 218 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2023-06-05 13:32 UTC)

<p>It seems that your settings file is not writeable. The file is created in your user folder by default, so it is normally writeable. You can print the file location by typing this command into the Python console:</p>
<pre><code>print(slicer.app.settings().fileName())
</code></pre>

---
