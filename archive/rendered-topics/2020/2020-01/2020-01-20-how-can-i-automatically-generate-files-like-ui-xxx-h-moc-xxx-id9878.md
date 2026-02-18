# How can I automatically generate files like ui_xxx.h、moc_xxx.h form *.ui?

**Topic ID**: 9878
**Date**: 2020-01-20
**URL**: https://discourse.slicer.org/t/how-can-i-automatically-generate-files-like-ui-xxx-h-moc-xxx-h-form-ui/9878

---

## Post #1 by @Shicong (2020-01-20 08:34 UTC)

<p>I want to create a panel of my own in slicer, I copy a file such as ui and corresponding ui_xxx.h, moc_xxx.cpp, and change its name, smoother can run properly; I edited the .ui file in Qt, how can I automatically generate files like ui_xxx.h, and how can the moc_xxx.cpp file be generated automatically? Thanks.<br>
Like the following files, I think they are automatically generated???<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad9448deba20aefeb02e4f3ff9f5f3ab7e3e80b1.png" data-download-href="/uploads/short-url/oLyiEcLFN0Dm7uFhWQ2ES9PfWMh.png?dl=1" title="fang1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad9448deba20aefeb02e4f3ff9f5f3ab7e3e80b1.png" alt="fang1" data-base62-sha1="oLyiEcLFN0Dm7uFhWQ2ES9PfWMh" width="592" height="500" data-dominant-color="373436"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">fang1</span><span class="informations">713×602 41.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2020-01-20 14:35 UTC)

<p>If you add the .ui file to CMakeLists.txt (search for UI_SRCS) then the associated files will be generated during the build process.</p>

---

## Post #3 by @Shicong (2020-01-21 02:01 UTC)

<p>Thank you very much. I wish you a happy life ！！！</p>

---
