# Openslide-python not working when trying to use monailabel

**Topic ID**: 33427
**Date**: 2023-12-17
**URL**: https://discourse.slicer.org/t/openslide-python-not-working-when-trying-to-use-monailabel/33427

---

## Post #1 by @Vineet_Saravanan (2023-12-17 23:40 UTC)

<p>When I try to install monailabel with the command ‘pip install -U monailabel’, I get this issue:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a3673608ee0e4e647c51318f7927bd6d42506531.png" data-download-href="/uploads/short-url/njwXimfB1zb2xrE4Ne8SrtoLPWN.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a3673608ee0e4e647c51318f7927bd6d42506531_2_690x276.png" alt="image" data-base62-sha1="njwXimfB1zb2xrE4Ne8SrtoLPWN" width="690" height="276" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a3673608ee0e4e647c51318f7927bd6d42506531_2_690x276.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a3673608ee0e4e647c51318f7927bd6d42506531_2_1035x414.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a3673608ee0e4e647c51318f7927bd6d42506531_2_1380x552.png 2x" data-dominant-color="242323"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1588×637 65 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I pip installed openslide-python before, but I am still having an issue. I also tried installing it with a GitHub clone, but that didn’t work. How should I solve this issue?</p>

---

## Post #2 by @jamesobutler (2023-12-18 01:34 UTC)

<p>Since the <code>monai</code> package of <code>monailabel</code> requires <code>openslide-python</code> 1.1.2 as stated <a href="https://github.com/Project-MONAI/MONAI/blob/865972f7a791bf7b42efbcd87c8402bd865b329e/setup.cfg#L63" rel="noopener nofollow ugc">here</a>, then I would suggest using Python 3.10 or earlier as there are only Whl files available for those versions. See <a href="https://pypi.org/project/openslide-python/1.1.2/#files" class="inline-onebox" rel="noopener nofollow ugc">openslide-python · PyPI</a>. Python 3.11 was not released when this openslide version was released so it is not officially supported.</p>

---

## Post #3 by @Vineet_Saravanan (2023-12-18 17:10 UTC)

<p>Hello, I tried using 3.9.13 but still have the same issue.</p>

---

## Post #4 by @diazandr3s (2023-12-20 18:46 UTC)

<p>This is strange. There shouldn’t be an issue with Python 3.9. Can you please share the error?</p>
<p>Also, I’d suggest trying a fresh Python environment using version 3.9 or 3.10. More comments about this issue are also here: <a href="https://github.com/Project-MONAI/MONAILabel/issues/1569#issuecomment-1864967422" class="inline-onebox" rel="noopener nofollow ugc">monailabel cannot be installed in python 3.11 · Issue #1569 · Project-MONAI/MONAILabel · GitHub</a></p>
<p>Hope this helps,</p>

---

## Post #5 by @Vineet_Saravanan (2023-12-20 23:25 UTC)

<p>Hello. I tried again by uninstalling python and reinstalling an earlier version and it worked. Thank you for the help!</p>

---

## Post #6 by @diazandr3s (2024-01-01 21:18 UTC)

<p>Thanks for the update, <a class="mention" href="/u/vineet_saravanan">@Vineet_Saravanan</a></p>

---

## Post #7 by @howtoostart (2024-08-20 03:42 UTC)

<p>hello.What was the final successful version of Python?</p>

---
