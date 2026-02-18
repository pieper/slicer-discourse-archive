# Change the background color black to white? in red, yellow and green slices?

**Topic ID**: 17715
**Date**: 2021-05-20
**URL**: https://discourse.slicer.org/t/change-the-background-color-black-to-white-in-red-yellow-and-green-slices/17715

---

## Post #1 by @NoobForSlicer (2021-05-20 19:17 UTC)

<p>Would it be possible to somehow change the background color to white rather than having it black?</p>
<p>Thanks…</p>

---

## Post #2 by @lassoan (2021-05-21 17:50 UTC)

<p>There is no GUI for changing the slice view background color, but you can do it by copy-pasting <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#capture-slice-view-into-png-file-with-white-background">these few lines</a> into the Python console.</p>

---

## Post #3 by @hmaguilera (2021-11-18 09:28 UTC)

<p>Hi Andras,<br>
I want to change the background of 3D view to white, so I can get figures with white backgrounds.</p>
<p>I tried copy-pasting the lines, but did not manage to do this for the 3D view. And the " Capture 3D view into PNG file with transparent background" did not do anything other than taking a screenshot.</p>
<p>Thanks</p>

---

## Post #4 by @lassoan (2021-11-18 15:00 UTC)

<p>You can use the GUI to change the 3D view background:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fb05f9a4f4248f2e4d6b76f5cf7f961f3b12522d.png" data-download-href="/uploads/short-url/zOEE6qg4lWWbdnGc6BYsbbgbnUV.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fb05f9a4f4248f2e4d6b76f5cf7f961f3b12522d.png" alt="image" data-base62-sha1="zOEE6qg4lWWbdnGc6BYsbbgbnUV" width="690" height="440" data-dominant-color="BABFDC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">729×465 21.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If you set the background to black then the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#capture-3d-view-into-png-file-with-transparent-background">code snippet for capturing of 3D view with transparent background</a> will work correctly.</p>

---

## Post #5 by @hmaguilera (2021-11-18 15:47 UTC)

<p>Thank you very much!</p>

---
