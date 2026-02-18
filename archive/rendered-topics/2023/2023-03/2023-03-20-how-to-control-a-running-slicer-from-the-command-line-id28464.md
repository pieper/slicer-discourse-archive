# How to control a running slicer from the command line

**Topic ID**: 28464
**Date**: 2023-03-20
**URL**: https://discourse.slicer.org/t/how-to-control-a-running-slicer-from-the-command-line/28464

---

## Post #1 by @slicer365 (2023-03-20 05:22 UTC)

<p>I know how to use the python console to control slicer.</p>
<p>But now I want to control the python console through an external program,<br>
My idea is to control the python console by entering commands through cmd, and then control the slicer scene.</p>
<p>How to achieve it?</p>
<p>For example, I want to print “HelloWorld” in the current python console through the cmd command.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/442dbd9052ea44b6d321303ff4cee902c15322a0.png" data-download-href="/uploads/short-url/9J8sVjOYVK2skqQ4AnFjGeeDhPq.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/442dbd9052ea44b6d321303ff4cee902c15322a0_2_690x448.png" alt="image" data-base62-sha1="9J8sVjOYVK2skqQ4AnFjGeeDhPq" width="690" height="448" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/442dbd9052ea44b6d321303ff4cee902c15322a0_2_690x448.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/442dbd9052ea44b6d321303ff4cee902c15322a0_2_1035x672.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/442dbd9052ea44b6d321303ff4cee902c15322a0.png 2x" data-dominant-color="6F6E78"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1339×871 52.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2023-03-20 16:17 UTC)

<p>You can use the WebServer module for this:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/webserver.html#remote-control" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/webserver.html#remote-control</a></p>

---
