# Could not load...as a Scalar Volume

**Topic ID**: 13200
**Date**: 2020-08-27
**URL**: https://discourse.slicer.org/t/could-not-load-as-a-scalar-volume/13200

---

## Post #1 by @sanna (2020-08-27 18:38 UTC)

<p>Hi! I’ve just started using Slicer (I have an MRI scan of my spine that I’d like to export for 3D printing) and I’m stuck on the “Could not load…as a Scalar Volume”. I understand there can be several reasons for it, but none of the ones I’ve found in the forum so far seems to match, and since I’m a complete newbie on anything having to do with medical scans or the dicom format I just wanted to ask for any suggestions.</p>
<p>I’m attaching screencaps of the files I want to load and the error messages.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/94a7a0a6d6e9453ff1e0bb03737ee4e05db54742.png" data-download-href="/uploads/short-url/ld3NYdfIgQxjRGfi64HYVsrkzRg.png?dl=1" title="Skärmklipp" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/94a7a0a6d6e9453ff1e0bb03737ee4e05db54742_2_690x236.png" alt="Skärmklipp" data-base62-sha1="ld3NYdfIgQxjRGfi64HYVsrkzRg" width="690" height="236" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/94a7a0a6d6e9453ff1e0bb03737ee4e05db54742_2_690x236.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/94a7a0a6d6e9453ff1e0bb03737ee4e05db54742_2_1035x354.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/94a7a0a6d6e9453ff1e0bb03737ee4e05db54742_2_1380x472.png 2x" data-dominant-color="DEE0EC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Skärmklipp</span><span class="informations">1860×638 373 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/706e11e9feeffb6b7480ee7e4cc85f93b04f9093.png" data-download-href="/uploads/short-url/g2BiDecCbkKG4HoPnbLLPRe97Oz.png?dl=1" title="Skärmklipp2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/706e11e9feeffb6b7480ee7e4cc85f93b04f9093_2_690x212.png" alt="Skärmklipp2" data-base62-sha1="g2BiDecCbkKG4HoPnbLLPRe97Oz" width="690" height="212" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/706e11e9feeffb6b7480ee7e4cc85f93b04f9093_2_690x212.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/706e11e9feeffb6b7480ee7e4cc85f93b04f9093_2_1035x318.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/706e11e9feeffb6b7480ee7e4cc85f93b04f9093_2_1380x424.png 2x" data-dominant-color="FDF7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Skärmklipp2</span><span class="informations">1634×503 157 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2020-08-27 20:40 UTC)

<p>The issue is that your files or directories contain special characters. If you upgrade to latest Slicer-4.11 Preview Release and Windows10 version (Build 18363 or later) then it should work. If you don’t want to upgrade then rename all your DICOM folders and files to only contain ASCII characters.</p>

---
