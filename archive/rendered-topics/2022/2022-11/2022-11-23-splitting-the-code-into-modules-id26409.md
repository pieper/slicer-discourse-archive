# Splitting the code into modules

**Topic ID**: 26409
**Date**: 2022-11-23
**URL**: https://discourse.slicer.org/t/splitting-the-code-into-modules/26409

---

## Post #1 by @S_Arbabi (2022-11-23 15:17 UTC)

<p>Hi,</p>
<p>for the sake of improving readability  I wanted to put some useful functions that I write and frequently call into another file.py and only import and use them inside the slicer module code (inside widget or logic).<br>
But for some reason it doesn’t work properly, and whenever I update the function in my file.py, I need to restart slicer so the slicer module can see and use the changes I made.<br>
Any ideas?</p>
<p>Best</p>

---

## Post #2 by @pll_llq (2022-11-23 21:30 UTC)

<p>If you have developer mode enabled and your module UI has the default ״Reload module” button- press it every time you edit your script so that only the module is reloaded and not the whole slicer.<br>
Hope this helps</p>

---

## Post #3 by @lassoan (2022-11-23 22:49 UTC)

<p>The reload button only knows about your module.py file. You need to add reloading of any additional files. See example in <a href="https://github.com/SlicerHeart/SlicerHeart/blob/d5de4cb42c8cdda24eac430d096eddca5f14e8fd/ValveAnnulusAnalysis/ValveAnnulusAnalysis.py#L785-L798">SlicerHeart extension</a>. Note that if you have a complex dependency between multiple files then you need to reload the files in the correct order (or else you may need to click reload a few times).</p>

---
