---
topic_id: 33900
title: "Cannot Import Simpleitk In Build In Python"
date: 2024-01-22
url: https://discourse.slicer.org/t/33900
---

# Cannot import SimpleITK in build-in python

**Topic ID**: 33900
**Date**: 2024-01-22
**URL**: https://discourse.slicer.org/t/cannot-import-simpleitk-in-build-in-python/33900

---

## Post #1 by @schcat (2024-01-22 07:51 UTC)

<p>I have a problem. I compiled SlicerCustomAppTemplate, installed SimpleITK in it’s build-in python, and it crashed when I run “import SimpleITK” in python script.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5a310de269105abbed94e76934ede6c320699bc8.png" data-download-href="/uploads/short-url/cRS4ndy67kuWNy1BTApZEDmwSAU.png?dl=1" title="Screenshot from 2024-01-22 15-37-13" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5a310de269105abbed94e76934ede6c320699bc8.png" alt="Screenshot from 2024-01-22 15-37-13" data-base62-sha1="cRS4ndy67kuWNy1BTApZEDmwSAU" width="690" height="139" data-dominant-color="3D1D35"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2024-01-22 15-37-13</span><span class="informations">729×147 26.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
My environment is Ubuntu22.04. I didn’t open the Slicer_USE_SimpleITK option when compile Slicer, but install SimpleITK by pip, because I find that there are many things to install when open the Slicer_USE_SimpleITK, is it matter?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/274ab6e893b2f6daee8471100baff145178b191a.png" data-download-href="/uploads/short-url/5BAHaWIT7RB6NsW6YgMC0iyxyfo.png?dl=1" title="Screenshot from 2024-01-22 15-46-57" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/274ab6e893b2f6daee8471100baff145178b191a.png" alt="Screenshot from 2024-01-22 15-46-57" data-base62-sha1="5BAHaWIT7RB6NsW6YgMC0iyxyfo" width="690" height="260" data-dominant-color="421F36"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2024-01-22 15-46-57</span><span class="informations">729×275 55.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I test other version of SimpleITK and it also doesn’t work. SimpleITK can works well in my systems python 3.10.</p>

---

## Post #2 by @lassoan (2024-01-23 23:29 UTC)

<p>If you want to use SimpleITK in Slicer then you need to enable Slicer_USE_SimpleITK. If you install some ABI incompatible SimpleITK binaries from PyPI then Slicer will crash.</p>
<p>A special mechanism was implemented for ITK-Python that allows standalone installation from wheels (Slicer’s ITK does not clash with ITK-Python’s ITK), but as far as I know, this mechanism has not been implemented in SimpleITK. If you don’t want to build SimpleITK but you want to use ITK from Python then you can use ITK-Python.</p>

---

## Post #3 by @schcat (2024-01-24 01:29 UTC)

<p>Thank you! I’m trying to compile with Slicer_USE_SimpleITK is ON, and still encountering some difficulties. Perhaps rewrite this part of code with ITK-Python is a good idear.</p>

---

## Post #4 by @lassoan (2024-01-24 04:49 UTC)

<p>If you already installed SimpleITK using pip then you may need to uninstall it, as it may interfere with the one that Slicer builds. But switching to ITK-Python could be a good solution, too.</p>

---

## Post #5 by @schcat (2024-01-24 07:43 UTC)

<p>OK! It was uninstalled. I have turned to ITK-Python, and it works well with Slicer python environment now. Thank you for your help!</p>

---
