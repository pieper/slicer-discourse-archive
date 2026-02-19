---
topic_id: 44649
title: "Sudden Crash During Save"
date: 2025-10-02
url: https://discourse.slicer.org/t/44649
---

# Sudden crash during save

**Topic ID**: 44649
**Date**: 2025-10-02
**URL**: https://discourse.slicer.org/t/sudden-crash-during-save/44649

---

## Post #1 by @dfajtai (2025-10-02 13:15 UTC)

<p>Dear Slicer Developers,</p>
<p>Please accept my greatest gratitude for developing such a <em>marvelous</em> software, one that excels at crashing right when saving, while also making sure to destroy everything I had saved before. That level of brilliance is simply unmatched.</p>
<p>Truly, only the most <em>genius</em> minds could come up with a system where hours of work vanish into thin air with a single click. It’s not just buggy — it’s an act of sabotage disguised as software. Seriously, hats off, this isn’t a bug, it’s a masterpiece of frustration.</p>
<p>Thank you for reminding us all that progress can always be erased in an instant. Your contribution to wasted time, broken nerves, and pure rage is invaluable.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/220b7a9e9b60d1727adf34e8bf3b4b571b4f657c.png" data-download-href="/uploads/short-url/4RaPjiLKujo6NJ7OQJHVbuyKJLS.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/220b7a9e9b60d1727adf34e8bf3b4b571b4f657c_2_690x355.png" alt="image" data-base62-sha1="4RaPjiLKujo6NJ7OQJHVbuyKJLS" width="690" height="355" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/220b7a9e9b60d1727adf34e8bf3b4b571b4f657c_2_690x355.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/220b7a9e9b60d1727adf34e8bf3b4b571b4f657c_2_1035x532.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/220b7a9e9b60d1727adf34e8bf3b4b571b4f657c_2_1380x710.png 2x" data-dominant-color="8B8A91"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1917×987 139 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @jamesobutler (2025-10-02 14:09 UTC)

<p>Hi <a class="mention" href="/u/dfajtai">@dfajtai</a> and welcome back to the forum! It appears there is some possible corruption when loading your nrrd file. Are you able to replicate the crash consistently? If you pull the volume locally instead of on your NAS does it have the same issue? Have you modified the NRRD header in any way while it had been saved in a compressed format thereby corrupting the expected size of the file?</p>

---

## Post #3 by @dfajtai (2025-10-02 14:29 UTC)

<p>Yes, I tried to open it about 10 times, using various scenarios. First, I tried to reopen the scene from Recent Files. Then I tried opening the scene manually. After that, I opened the scene from an already running Slicer instance. I also tried with an older version of Slicer (the scene was initially created with version 5.6.2). Then I attempted to load only the segmentation. Finally, I moved the files to a local SSD drive and repeated the last three attempts. None of them worked.</p>
<p>What I truly do not understand is that until today, I thought Slicer had a quite robust and sophisticated saving procedure: initialize a temporary writer, write the actual stage to temporary files, and once completed, overwrite the old version with the new one before removing the temp files. However, in this case I ended up with neither temporary files nor the original, just the corrupted one. What exactly happened here? (Aside from the fact that I just lost 4–5 hours of work.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7a9a395d4867f6740ad9c58ca004d0c3f6471b2c.png" data-download-href="/uploads/short-url/huAFQydVEN5JUpodG4vBTHssKIc.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7a9a395d4867f6740ad9c58ca004d0c3f6471b2c_2_690x365.png" alt="image" data-base62-sha1="huAFQydVEN5JUpodG4vBTHssKIc" width="690" height="365" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7a9a395d4867f6740ad9c58ca004d0c3f6471b2c_2_690x365.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7a9a395d4867f6740ad9c58ca004d0c3f6471b2c_2_1035x547.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7a9a395d4867f6740ad9c58ca004d0c3f6471b2c_2_1380x730.png 2x" data-dominant-color="E3E3E3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1914×1015 121 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
