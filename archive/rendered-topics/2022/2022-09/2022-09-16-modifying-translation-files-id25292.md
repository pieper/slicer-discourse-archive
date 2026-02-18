# Modifying translation files

**Topic ID**: 25292
**Date**: 2022-09-16
**URL**: https://discourse.slicer.org/t/modifying-translation-files/25292

---

## Post #1 by @miniminic (2022-09-16 05:05 UTC)

<p>I downloaded the Chinese translation file from the official website, but how can I add the translation file to the Slicer project and then modify it</p>

---

## Post #2 by @lassoan (2022-09-16 05:21 UTC)

<p>While you can modify translation files locally, I would recommend to update translation on Weblate and download the translation file from there. See more information in the <a href="https://github.com/Slicer/SlicerLanguagePacks/blob/main/HowToUse.md">LanguagePacks extension documentation</a>.</p>

---

## Post #3 by @miniminic (2022-09-16 05:23 UTC)

<p>But I modified part of the function to add some things, they also need to be translated, in the local I now have to manually modify it</p>

---

## Post #4 by @lassoan (2022-09-16 05:29 UTC)

<p>If you modify Slicer core source code then you need to regenerate the translation source file using Qt’s <code>lupdate</code> tool, then add the translated strings (you can use Qt linguist), and use that in the <code>Language Tools</code> module.</p>

---

## Post #5 by @miniminic (2022-09-16 05:35 UTC)

<p>Yes, I thought so at first, but I couldn’t find how to create a new translation file in the Slicer project</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b6c0f303afb9913676b0f3bd5780578228d61a3.jpeg" data-download-href="/uploads/short-url/hBQfbrengE6E7ZqKocoHxspXbiz.jpeg?dl=1" title="屏幕截图 2022-09-16 133417" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b6c0f303afb9913676b0f3bd5780578228d61a3_2_690x381.jpeg" alt="屏幕截图 2022-09-16 133417" data-base62-sha1="hBQfbrengE6E7ZqKocoHxspXbiz" width="690" height="381" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b6c0f303afb9913676b0f3bd5780578228d61a3_2_690x381.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b6c0f303afb9913676b0f3bd5780578228d61a3.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b6c0f303afb9913676b0f3bd5780578228d61a3.jpeg 2x" data-dominant-color="2D2D2E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">屏幕截图 2022-09-16 133417</span><span class="informations">742×410 61.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
There is no option to create a new translation file</p>

---

## Post #6 by @lassoan (2022-09-16 05:39 UTC)

<p><code>lupdate</code> is a command-line tool, you can run it in the terminal. See more information in the <a href="https://github.com/Slicer/Slicer/wiki/I18N">Slicer i18n labs page</a>.</p>

---

## Post #7 by @miniminic (2022-09-16 05:42 UTC)

<p>Ok Thank you very much</p>

---
