# Cropping image during loading

**Topic ID**: 9719
**Date**: 2020-01-06
**URL**: https://discourse.slicer.org/t/cropping-image-during-loading/9719

---

## Post #1 by @carterrt (2020-01-06 18:56 UTC)

<p>It is possible to crop an image stack during the loading process to thereby reducing the data foot print that the the computer has to deal with? I have a very large scan but only need a small portion of it and loading the whole thing really gums up my computer.</p>

---

## Post #2 by @pieper (2020-01-06 19:11 UTC)

<p>Hi -</p>
<p>We talked about adding this to the <a href="https://github.com/pieper/SlicerImageStacks">ImageStacks</a> module in SlicerMorph but it wasn’t clear how the user should select the ROI.  Would it be enough just to type in x,y values?</p>
<p>For cropping in Z of course you can just select the range of image slices you need.</p>

---
