# Remake Save function

**Topic ID**: 29786
**Date**: 2023-06-02
**URL**: https://discourse.slicer.org/t/remake-save-function/29786

---

## Post #1 by @dsa934 (2023-06-02 02:08 UTC)

<p>Operating system: 10<br>
Slicer version: 5.2.1</p>
<p>Hi, slicer users,</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/eebe92c1fe4ecc521c5972c8e55d2029ebd4829c.png" data-download-href="/uploads/short-url/y41WeKliKr22tPybqqppnwPFxgg.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/eebe92c1fe4ecc521c5972c8e55d2029ebd4829c.png" alt="image" data-base62-sha1="y41WeKliKr22tPybqqppnwPFxgg" width="690" height="384" data-dominant-color="F6F3F3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">727×405 29.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I want to recreate the currently implemented save function with python.<br>
Is it correct that the current implementation of the save function is made in C++ and qt?</p>
<p>I’m trying to override this with a function that requires some additional conditions to be met when the save button is pressed in order to save. Is it possible to access the save widget with Python?</p>
<p>My first attempt was to overriding the hotkey (“Ctrl+s”), but I can’t seem to override the existing hotkey.</p>

---

## Post #2 by @lassoan (2023-06-02 23:29 UTC)

<p>Yes, sure, you can override the custom save dialog, donwhat vér you need to do, and then if you want you can also call the default dialog. I think the details were asked and described on this forum but if you cannot find it then let us know.</p>

---
