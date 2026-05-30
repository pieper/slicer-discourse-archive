---
topic_id: 47172
title: "Why won't my mrml file open in 3D slicer, or my stl file become visible?"
date: 2026-05-29
url: https://discourse.slicer.org/t/47172
last_bumped: 2026-05-29T14:34:17.304Z
---

# Why won't my mrml file open in 3D slicer, or my stl file become visible?

**Topic ID**: 47172
**Date**: 2026-05-29
**URL**: https://discourse.slicer.org/t/why-wont-my-mrml-file-open-in-3d-slicer-or-my-stl-file-become-visible/47172

---

## Post #1 by @Emerson (2026-05-29 13:56 UTC)

<p>I was trying to open an mrml file I have saved, and while it opened the app it did not open the file or show up anywhere. I tried again with the stl file and while it showed up under ‘data’ (which is farther than I got with mrml) it didn’t show up as a model no matter what I tried. I need to fix a landmark I made on this skull and I can’t figure out how to access it, and now I’m worried the way I’m saving it isn’t working. But the mrml file says its 14 kb, so it shouldn’t be empty. How do I fix this?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ea0f471bc127eaa3652b9ba3c6013a434c8cb17f.png" data-download-href="/uploads/short-url/xoAsym4dw6hd6yg0JR9aHpT8BBB.png?dl=1" title="Screenshot 2026-05-28 at 6.03.43 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ea0f471bc127eaa3652b9ba3c6013a434c8cb17f_2_654x500.png" alt="Screenshot 2026-05-28 at 6.03.43 PM" data-base62-sha1="xoAsym4dw6hd6yg0JR9aHpT8BBB" width="654" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ea0f471bc127eaa3652b9ba3c6013a434c8cb17f_2_654x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ea0f471bc127eaa3652b9ba3c6013a434c8cb17f_2_981x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ea0f471bc127eaa3652b9ba3c6013a434c8cb17f.png 2x" data-dominant-color="3C3B3B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2026-05-28 at 6.03.43 PM</span><span class="informations">1144×874 50.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7d8758f799b3b6ba70e58f6f1d5ec6fe6174c90b.png" data-download-href="/uploads/short-url/hUtFcwjFPRYfafeS2IzO3tMchx9.png?dl=1" title="Screenshot 2026-05-28 at 5.59.51 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d8758f799b3b6ba70e58f6f1d5ec6fe6174c90b_2_235x500.png" alt="Screenshot 2026-05-28 at 5.59.51 PM" data-base62-sha1="hUtFcwjFPRYfafeS2IzO3tMchx9" width="235" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d8758f799b3b6ba70e58f6f1d5ec6fe6174c90b_2_235x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d8758f799b3b6ba70e58f6f1d5ec6fe6174c90b_2_352x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d8758f799b3b6ba70e58f6f1d5ec6fe6174c90b_2_470x1000.png 2x" data-dominant-color="403E39"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2026-05-28 at 5.59.51 PM</span><span class="informations">518×1102 65 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2026-05-29 14:34 UTC)

<p>The .mrml file is just a kind of manifest that keeps track of your scene info (like camera views and colors) while bulk data like STL files are stored separately.  If the path to the STL file changes then Slicer won’t be able to load it from your mrml file (you can check the error log).  You may be better off saving in MRB, which is a single file (a zip file) with both the MRML manifest and the bulk data files.</p>

---
