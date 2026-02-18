# Translation files

**Topic ID**: 22242
**Date**: 2022-03-01
**URL**: https://discourse.slicer.org/t/translation-files/22242

---

## Post #1 by @Maite_Guix (2022-03-01 18:04 UTC)

<p>the file that I downloaded *.po has the source in the translation and so I cannot pre-translate with poedit and it is much more work, can someone leave the Catalan field blank?</p>

---

## Post #2 by @lassoan (2022-03-01 18:21 UTC)

<p>I’ve downloaded the Catalan .po file from <a href="https://hosted.weblate.org/download/3d-slicer/3d-slicer/ca/?format=po">https://hosted.weblate.org/download/3d-slicer/3d-slicer/ca/?format=po</a> and I was able to edit it in <a href="https://poedit.net/">poedit</a> without any issues.</p>
<p>That said, we maintain translations in .ts file format, which have slightly different capabilities and limitations compared to .po files, so it might lead to complications that the translations are converted to/from .po file. Instead, you can use Qt linguist to edit .ts files directly if you want to use a desktop application for translation. However, in the long term it would be probably better to use Weblate’s web UI to avoid/manage conflicting changes and make sure all metadata is preserved.</p>

---

## Post #3 by @Maite_Guix (2022-03-01 18:26 UTC)

<p>I have no problem opening it with poedit; but I can’t pre-translate it because it’s already pre-translated (the Catalan strings are in English). I usually pre-translate it, and immediately upload it and continue with weblate.</p>

---

## Post #4 by @lassoan (2022-03-01 19:24 UTC)

<p>poedit seems to be able to recognize untranslated strings (untranslated string is orange, translated is black):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/4933cb4cf093624da00d822b0cde9d148d78433e.png" data-download-href="/uploads/short-url/arzP4ChwbDdliqzHt5LfAoCTmfs.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/4933cb4cf093624da00d822b0cde9d148d78433e_2_690x288.png" alt="image" data-base62-sha1="arzP4ChwbDdliqzHt5LfAoCTmfs" width="690" height="288" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/4933cb4cf093624da00d822b0cde9d148d78433e_2_690x288.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/4933cb4cf093624da00d822b0cde9d148d78433e_2_1035x432.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/4933cb4cf093624da00d822b0cde9d148d78433e_2_1380x576.png 2x" data-dominant-color="F3F3F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1707×714 56.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Are you sure you need to clear out the <code>msgstr</code> values? If yes, then you can do it with search and replace in a text editor that supports regex replacement, such as Visual Studio Code:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/30ac5426886f360107e478a586cabd0094106df4.png" data-download-href="/uploads/short-url/6WA887PI3a6HpNZLcfaSJi3f24Y.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/30ac5426886f360107e478a586cabd0094106df4_2_690x312.png" alt="image" data-base62-sha1="6WA887PI3a6HpNZLcfaSJi3f24Y" width="690" height="312" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/30ac5426886f360107e478a586cabd0094106df4_2_690x312.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/30ac5426886f360107e478a586cabd0094106df4_2_1035x468.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/30ac5426886f360107e478a586cabd0094106df4_2_1380x624.png 2x" data-dominant-color="272625"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2109×955 213 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Have you tried Weblate’s automatic suggestions? I’ve found that the suggestions are generally good quality. For example:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d8307b6ef4c40e999f6b4961dbafcb6ba559693.png" data-download-href="/uploads/short-url/4d4zNzDkmJ4Utbqp2pVT9D5s1tV.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1d8307b6ef4c40e999f6b4961dbafcb6ba559693_2_607x500.png" alt="image" data-base62-sha1="4d4zNzDkmJ4Utbqp2pVT9D5s1tV" width="607" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1d8307b6ef4c40e999f6b4961dbafcb6ba559693_2_607x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1d8307b6ef4c40e999f6b4961dbafcb6ba559693_2_910x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1d8307b6ef4c40e999f6b4961dbafcb6ba559693_2_1214x1000.png 2x" data-dominant-color="E7EFEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1674×1378 206 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>For me the main challenge is not to translate English to another language, but finding the correct word in English that accurately captures the meaning of it in Slicer. Kind of translating “Slicer English” to “common English”, then that common English term can be translated to any language much more easily. For example, we first “translate” <code>scene</code> to <code>workspace</code>, because better reflects the actual meaning in Slicer, and then <code>workspace</code> can be easily translated to other languages. We have been also struggling with basic words, such as <code>volume</code> or <code>labelmap</code> because in Slicer they have a special meaning.</p>
<p>Do you find that poedit can translate translating trivial terms (such as “toggle visibility”) so much better than Weblate automatic translations, or poedit can provide significant help with the difficult translations so that it is worth purchasing the software for it?</p>

---

## Post #5 by @Maite_Guix (2022-03-01 21:15 UTC)

<p>I’d rather have msgstr="" and be able to pre-translate it, but I’ll settle for auto-suggestions.  Thanks,</p>

---

## Post #6 by @Maite_Guix (2022-03-02 16:02 UTC)

<p>I have been able to use Visual Studio Code and I am very happy!!</p>
<p>Thank you</p>

---
