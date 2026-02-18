# OCT .fds image in 3D slicer?

**Topic ID**: 18219
**Date**: 2021-06-18
**URL**: https://discourse.slicer.org/t/oct-fds-image-in-3d-slicer/18219

---

## Post #1 by @Daiana_P (2021-06-18 19:11 UTC)

<p>Wondering if I can load OCT .fds files into 3D slicer.</p>
<p>Otherwise I can get .png files but how can i stack them?</p>

---

## Post #2 by @pieper (2021-06-18 19:22 UTC)

<p>I’m not too familiar with OCT, but if you can convert them to something Slicer can read it should work.  People have done it before and had good luck.  It looks like <a href="https://github.com/marksgraham/OCT-Converter">this converter</a> could be helpful and maybe you could use it to bypass the png step by reading directly into slicer.  Or if you have the pngs already you could use <a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/ImageStacks">ImageStacks</a> from SlicerMorph to read them in and set the spacing parameters.</p>

---

## Post #3 by @lassoan (2021-06-18 19:42 UTC)

<p>If you often need to read such images into Slicer then you can use the converter that <a class="mention" href="/u/pieper">@pieper</a> suggested above to create a reader plugin for Slicer (probably you need to write less than 30 lines of code, see a complete example <a href="https://github.com/Slicer/Slicer/blob/master/Applications/SlicerApp/Testing/Python/SlicerScriptedFileReaderWriterTest.py">here</a>). If you can share an example file then I can give it a try to write a plugin.</p>

---

## Post #4 by @Daiana_P (2021-06-20 13:29 UTC)

<p>Thank you very much for your help. Here is an example file <a href="https://uwoca-my.sharepoint.com/:u:/g/personal/dpur_uwo_ca/EbAqtJUjuBpEpAm8QD_uxfYBy359eLrZNye78o2K41Ftag?e=z4FSzk" rel="noopener nofollow ugc">https://uwoca-my.sharepoint.com/:u:/g/personal/dpur_uwo_ca/EbAqtJUjuBpEpAm8QD_uxfYBy359eLrZNye78o2K41Ftag?e=z4FSzk</a></p>
<p><a class="mention" href="/u/pieper">@pieper</a> Thank you for the suggestions I have tried it, it did work to get the PNG files with a different OCT file. The one I plan on using seems to have a slightly different internal organization and it’s giving me some errors when converting to PNG. I reached out to the creator of the converter and hopefully he has some tips!</p>

---

## Post #5 by @dpuruwo (2021-07-07 17:09 UTC)

<p>I am wondering if you have had a chance to write a plugin for it. Thank you</p>

---

## Post #6 by @lassoan (2021-07-09 05:53 UTC)

<p>I’ve added an <a href="https://github.com/PerkLab/SlicerSandbox/blob/master/ImportOCT/ImportOCT.py">OCT importer plugin</a> to Sandbox extension that uses <a href="https://github.com/marksgraham/OCT-Converter">OCT-Converter</a> Python package to read OCT volumes stored in .fda file format. It is available in the latest Slicer Preview Release.</p>

---

## Post #7 by @dpuruwo (2021-07-21 01:14 UTC)

<p>Thank you very much! I’ve been struggling to find the extension in the extension manager. Not sure why! This is what I see</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6b71c1b61e99edd885c0139ee0b617855c9cc40.jpeg" data-download-href="/uploads/short-url/zcxLEHmfcLCjvgLDQ5hJeufgBwY.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f6b71c1b61e99edd885c0139ee0b617855c9cc40_2_690x393.jpeg" alt="image" data-base62-sha1="zcxLEHmfcLCjvgLDQ5hJeufgBwY" width="690" height="393" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f6b71c1b61e99edd885c0139ee0b617855c9cc40_2_690x393.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f6b71c1b61e99edd885c0139ee0b617855c9cc40_2_1035x589.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f6b71c1b61e99edd885c0139ee0b617855c9cc40_2_1380x786.jpeg 2x" data-dominant-color="F6F6F6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1894×1080 141 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @lassoan (2021-07-21 01:28 UTC)

<p>Thanks for reporting this. I’ve made a mistake when I added the new module, which cause packaging to fail. The Sandbox extension should be available again in the Slicer Preview Release from tomorrow.</p>

---

## Post #9 by @dpuruwo (2021-08-01 14:00 UTC)

<p>Hello! Sorry to bug you again. I’ve tried different things but I still cannot access it.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8b2389e0c78a0db4801b778b9a22fe8b43b29530.jpeg" data-download-href="/uploads/short-url/jQSvAn3Ln3QlAi80drxOpQoTqhy.jpeg?dl=1" title="Screen Shot 2021-08-01 at 9.58.19 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8b2389e0c78a0db4801b778b9a22fe8b43b29530_2_690x407.jpeg" alt="Screen Shot 2021-08-01 at 9.58.19 AM" data-base62-sha1="jQSvAn3Ln3QlAi80drxOpQoTqhy" width="690" height="407" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8b2389e0c78a0db4801b778b9a22fe8b43b29530_2_690x407.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8b2389e0c78a0db4801b778b9a22fe8b43b29530_2_1035x610.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8b2389e0c78a0db4801b778b9a22fe8b43b29530_2_1380x814.jpeg 2x" data-dominant-color="F2F3F1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-08-01 at 9.58.19 AM</span><span class="informations">1868×1104 156 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/9552b1d37c066041c1eca85c7f857cdd69dc2a17.jpeg" data-download-href="/uploads/short-url/liYjyTZU8DqwH7YS9FFLU7mnG4L.jpeg?dl=1" title="Screen Shot 2021-08-01 at 9.58.41 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9552b1d37c066041c1eca85c7f857cdd69dc2a17_2_676x500.jpeg" alt="Screen Shot 2021-08-01 at 9.58.41 AM" data-base62-sha1="liYjyTZU8DqwH7YS9FFLU7mnG4L" width="676" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9552b1d37c066041c1eca85c7f857cdd69dc2a17_2_676x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9552b1d37c066041c1eca85c7f857cdd69dc2a17_2_1014x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9552b1d37c066041c1eca85c7f857cdd69dc2a17_2_1352x1000.jpeg 2x" data-dominant-color="DDDDE4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-08-01 at 9.58.41 AM</span><span class="informations">1738×1284 172 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I can see and download the Sandbox but when I try to access it via Slicer it’s not there.</p>

---

## Post #10 by @lassoan (2021-08-01 20:37 UTC)

<p>All you need is to install the extension. It registers the reader plugin automatically. You can then simply drag-and-drop the .fda file to the application window to load it.</p>

---

## Post #11 by @YaseminTurkan (2022-04-24 12:02 UTC)

<p>Hi, I am also trying to run fds files with the 3D Slicer. I have seen that you have developed an extention. However when I try to install the sandbox extention I can not see it. I am new to 3D Slicer, do I miss anything?</p>

---

## Post #12 by @YaseminTurkan (2022-04-24 13:29 UTC)

<p>Hi, I have managed to install the sandbox and the extension. When I choose the fda file I can see the correct Description called “OCT image”<br>
However when I try to open the file I get the following error:</p>
<p>Error occurred while loading the selected files.</p>
<p>Click ‘Show details’ button and check the application log for more information.</p>

---

## Post #13 by @lassoan (2022-04-24 19:29 UTC)

<p>What do you see in “See details” and in the application log?</p>

---
