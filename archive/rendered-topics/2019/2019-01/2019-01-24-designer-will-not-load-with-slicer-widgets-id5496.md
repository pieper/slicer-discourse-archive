# Designer will not load with slicer widgets

**Topic ID**: 5496
**Date**: 2019-01-24
**URL**: https://discourse.slicer.org/t/designer-will-not-load-with-slicer-widgets/5496

---

## Post #1 by @holmesrb (2019-01-24 17:24 UTC)

<p>Operating system: ubuntu 18.04<br>
Slicer version: 4.11.0<br>
Expected behavior: designer loads slicer widgets after build<br>
Actual behavior: exits with error message - this function is deprecated. Use currentNodeID() instead. qMRMLNodeComboBox::basename failed</p>
<p>I built slicer today, but needed to alter a line in libarchive/archive_pack_dev.c as per the post from phcerdan.</p>
<p>When running ./Slicer --designer I get the error above. I have tried copying the various plugins to the designer directory and that enables me to run designer with most of the widgets - if I copy libqMRMLWidgetsPlugins.so it crashes with the same error.</p>
<p>Many thanks - Robin</p>

---

## Post #2 by @lassoan (2019-01-24 21:18 UTC)

<p>Do you get an error if you just launch <code>./Slicer --designer</code> without loading any .ui file?<br>
Can you post a screenshot so that we can see what displays the error message and where?</p>

---

## Post #3 by @holmesrb (2019-01-24 21:39 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/46840beb89921ad2118773c1187288d4bc612ac8.png" data-download-href="/uploads/short-url/a3OkxQTxTJljz6u4iFzqLY77IzC.png?dl=1" title="screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/46840beb89921ad2118773c1187288d4bc612ac8_2_690x388.png" alt="screenshot" data-base62-sha1="a3OkxQTxTJljz6u4iFzqLY77IzC" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/46840beb89921ad2118773c1187288d4bc612ac8_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/46840beb89921ad2118773c1187288d4bc612ac8_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/46840beb89921ad2118773c1187288d4bc612ac8_2_1380x776.png 2x" data-dominant-color="7B4C5B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">screenshot</span><span class="informations">3200×1800 916 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thanks for the reply. I have attached a screenshot showing the error message after launching ./Slicer --designer.</p>

---

## Post #4 by @lassoan (2019-01-25 14:15 UTC)

<p>It seems that you’ve built Qt designer in debug mode. Debug-mode builds are often forced to crash by <code>assert</code> calls when some consistency checks fail. This problem will not occur with a designer built in Release mode and I believe this is what most people are using. To fix the debug-mode designer, we should probably change the <code>assert</code> in ctkMatrixWidget.cpp, line 241. We’ll change this in CTK, too (I’ve already submitted a <a href="https://github.com/commontk/CTK/pull/847" rel="nofollow noopener">pull request</a>).</p>

---

## Post #5 by @holmesrb (2019-01-26 14:04 UTC)

<p>Brilliant - I have had success in Release mode. Many thanks for your help.</p>

---
