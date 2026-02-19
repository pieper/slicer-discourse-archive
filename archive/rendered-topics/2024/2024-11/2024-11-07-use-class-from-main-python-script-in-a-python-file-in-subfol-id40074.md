---
topic_id: 40074
title: "Use Class From Main Python Script In A Python File In Subfol"
date: 2024-11-07
url: https://discourse.slicer.org/t/40074
---

# Use Class from Main Python Script in a python file in subfolder

**Topic ID**: 40074
**Date**: 2024-11-07
**URL**: https://discourse.slicer.org/t/use-class-from-main-python-script-in-a-python-file-in-subfolder/40074

---

## Post #1 by @maximeb (2024-11-07 20:40 UTC)

<p>Hi,<br>
Our team is developing a Slicer module.<br>
We want to split our code into different python files (are in subfolders). It works to import variables and functions (for example) from modules to main, but when we try to import a class (or function) of the main module to an extension, it does not work. Any suggestion? See image for hierarchy. Thank you in advance!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/84dbcdeab0768581a09d2909b0224ba410d8b98e.jpeg" data-download-href="/uploads/short-url/iXjXc9ildoynkqEcdKlQura01s2.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84dbcdeab0768581a09d2909b0224ba410d8b98e_2_690x286.jpeg" alt="image" data-base62-sha1="iXjXc9ildoynkqEcdKlQura01s2" width="690" height="286" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84dbcdeab0768581a09d2909b0224ba410d8b98e_2_690x286.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84dbcdeab0768581a09d2909b0224ba410d8b98e_2_1035x429.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84dbcdeab0768581a09d2909b0224ba410d8b98e_2_1380x572.jpeg 2x" data-dominant-color="B5B5B6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1792×744 125 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @rfenioux (2024-11-18 14:38 UTC)

<p>If that function or class is used by subcomponents, it would be better to extract it from the main module and put it into its own file in your subfolder. That way, every component (including the main module) can import it from the same location.</p>

---

## Post #3 by @maximeb (2024-11-18 15:34 UTC)

<p>Ok thanks for the follow-up! We effectively had some circular imports. Has been managed by re-organization of the classes and code. Thanks!</p>

---
