---
topic_id: 37780
title: "Download Of Extension Failed"
date: 2024-08-08
url: https://discourse.slicer.org/t/37780
---

# Download of extension failed

**Topic ID**: 37780
**Date**: 2024-08-08
**URL**: https://discourse.slicer.org/t/download-of-extension-failed/37780

---

## Post #1 by @muratmaga (2024-08-08 16:11 UTC)

<p>I am trying to test our new extension SlicerEditor, which was integrated into the extension catalog a few days ago. According to Cdash everything is ok. Extension is also appears in the catalog, but when I try to install it, I get this error:<br>
<code>Download of extension failed, could not find an extension with id = 66b4c1c3edd3d1d681d958ff</code></p>
<p>This is with the stable on Mac. Everything works fine with the latest preview.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a>  <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a></p>

---

## Post #2 by @pieper (2024-08-08 18:22 UTC)

<p>I was able to install the SlicerEditor extension on the most recent Preview build for linux and it worked.</p>

---

## Post #3 by @muratmaga (2024-08-08 19:24 UTC)

<p>yes, my inquiry is specific to the Stable build.</p>

---

## Post #4 by @jcfr (2024-08-09 03:45 UTC)

<p><code>SlicerEditor</code> is expected to be available with the latest stable.</p>
<p>See <a href="https://extensions.slicer.org/view/SlicerEditor/32448/macosx">https://extensions.slicer.org/view/SlicerEditor/32448/macosx</a></p>
<p>Are you now able to install the extension ?</p>

---

## Post #5 by @muratmaga (2024-08-09 03:52 UTC)

<p>It is there but failing. See:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc72ee9da51589fccfd8fcc9fcc18b302542064a.png" data-download-href="/uploads/short-url/qT60krpWAejbxNyiTh4tPgVuJfk.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bc72ee9da51589fccfd8fcc9fcc18b302542064a_2_690x444.png" alt="image" data-base62-sha1="qT60krpWAejbxNyiTh4tPgVuJfk" width="690" height="444" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bc72ee9da51589fccfd8fcc9fcc18b302542064a_2_690x444.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bc72ee9da51589fccfd8fcc9fcc18b302542064a_2_1035x666.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bc72ee9da51589fccfd8fcc9fcc18b302542064a_2_1380x888.png 2x" data-dominant-color="EFEBEB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1824×1174 169 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>In any event, <a class="mention" href="/u/pieper">@pieper</a> clarified that SlicerEditor relies on features incorporated after 5.6.2 is cut, so it won’t work with the stable anyways… So we can actually delete this thread.</p>

---

## Post #6 by @rkikinis (2024-08-09 08:25 UTC)

<p>I would consider calling the module SlicerPythonEditor. This would help prevent confusion with the SegmentEditor.</p>

---
