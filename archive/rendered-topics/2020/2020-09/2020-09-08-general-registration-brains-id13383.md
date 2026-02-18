# General Registration (BRAINS)

**Topic ID**: 13383
**Date**: 2020-09-08
**URL**: https://discourse.slicer.org/t/general-registration-brains/13383

---

## Post #1 by @zahiraabdala (2020-09-08 01:21 UTC)

<p>Hi everyone, I need to know how general registration brain module works. I use it and its works very well but I need more information about the functionality. I was looking for more information but I only found this link and it’s not enough <a href="https://www.slicer.org/w/index.php/Documentation/4.1/Modules/BRAINSFit" rel="nofollow noopener">https://www.slicer.org/w/index.php/Documentation/4.1/Modules/BRAINSFit</a></p>
<p>Im working with two different MR images and im using rigid registration, using the center of head align, how does the algorithm know which is the center of the head? Then if I choose the fixed image and moving image, how the algorithm makes the registration using the fixed image like a reference?</p>
<p>Thanks.</p>

---

## Post #2 by @lassoan (2020-09-08 01:47 UTC)

<p>BrainsFit (General registration (BRAINS) module) is just a thin wrapper over ITK library’s registration framework. See some more information in this paper: <a href="https://www.insight-journal.org/browse/publication/180">https://www.insight-journal.org/browse/publication/180</a></p>

---
