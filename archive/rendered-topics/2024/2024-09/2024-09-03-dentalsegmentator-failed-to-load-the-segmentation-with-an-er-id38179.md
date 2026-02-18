# DentalSegmentator failed to load the segmentation with an error occurred during install : nnunetv2

**Topic ID**: 38179
**Date**: 2024-09-03
**URL**: https://discourse.slicer.org/t/dentalsegmentator-failed-to-load-the-segmentation-with-an-error-occurred-during-install-nnunetv2/38179

---

## Post #1 by @igy (2024-09-03 12:26 UTC)

<p>Hello，I encountered an error while applying the extension<br>
this was how it went<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/3322f11578a1ba52bf0ebd1878bcd1fb1ed6f10d.png" data-download-href="/uploads/short-url/7inddYkGABofbAGS0uSQ5dTT4aV.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/3322f11578a1ba52bf0ebd1878bcd1fb1ed6f10d.png" alt="image" data-base62-sha1="7inddYkGABofbAGS0uSQ5dTT4aV" width="690" height="155" data-dominant-color="F5F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1077×243 6.89 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
2024/09/03 16:42:23.363 :: Start nnUNet install with requirements : nnunetv2</p>
<p>2024/09/03 16:42:23.368 :: - Installing pandas…</p>
<p>2024/09/03 16:42:32.044 :: Install returned non-zero exit status : Command ‘[‘D:/Slicer 5.7.0-2024-08-28/bin/…/bin\PythonSlicer.EXE’, ‘-m’, ‘pip’, ‘install’, ‘pandas’]’ returned non-zero exit status 1… Attempting to continue…</p>
<p>2024/09/03 16:42:32.049 :: - Installing pillow&lt;10.1…</p>
<p>2024/09/03 16:42:40.689 :: Install returned non-zero exit status : Command ‘[‘D:/Slicer 5.7.0-2024-08-28/bin/…/bin\PythonSlicer.EXE’, ‘-m’, ‘pip’, ‘install’, ‘pillow&lt;10.1’]’ returned non-zero exit status 1… Attempting to continue…</p>
<p>2024/09/03 16:42:40.697 :: - Installing nnunetv2 --no-deps…</p>
<p>2024/09/03 16:42:49.326 :: Install returned non-zero exit status : Command ‘[‘D:/Slicer 5.7.0-2024-08-28/bin/…/bin\PythonSlicer.EXE’, ‘-m’, ‘pip’, ‘install’, ‘nnunetv2’, ‘–no-deps’]’ returned non-zero exit status 1… Attempting to continue…</p>
<p>2024/09/03 16:42:49.334 :: Error occurred during install : nnunetv2</p>
<p>And I switched module to pytorch utils, I tried many times,but it still showed that I fail to install pytorch like this.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/6530683eb31412a7d42950ed1a50a61c9a2c9aa5.png" data-download-href="/uploads/short-url/er9W3ONeCvadlxxEm7whhP2wpA9.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/6530683eb31412a7d42950ed1a50a61c9a2c9aa5.png" alt="image" data-base62-sha1="er9W3ONeCvadlxxEm7whhP2wpA9" width="690" height="268" data-dominant-color="F6F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1105×430 12.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0ed90977efbd18eeaa2111d2f096780e351e6236.png" data-download-href="/uploads/short-url/27lGq0qMGOxXR5AM6CBI8ruoOjk.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0ed90977efbd18eeaa2111d2f096780e351e6236_2_690x112.png" alt="image" data-base62-sha1="27lGq0qMGOxXR5AM6CBI8ruoOjk" width="690" height="112" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0ed90977efbd18eeaa2111d2f096780e351e6236_2_690x112.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0ed90977efbd18eeaa2111d2f096780e351e6236_2_1035x168.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0ed90977efbd18eeaa2111d2f096780e351e6236_2_1380x224.png 2x" data-dominant-color="F6F4F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1594×260 22.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
How can I solve these problems?Thanks.</p>

---
