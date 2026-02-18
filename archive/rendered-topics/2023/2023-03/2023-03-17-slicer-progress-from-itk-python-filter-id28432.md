# Slicer progress from ITK Python filter

**Topic ID**: 28432
**Date**: 2023-03-17
**URL**: https://discourse.slicer.org/t/slicer-progress-from-itk-python-filter/28432

---

## Post #1 by @dzenanz (2023-03-17 19:30 UTC)

<p>I have similar question to <a href="https://discourse.slicer.org/t/use-progress-bar-from-python/4343">this</a>: What is the best way to update progress bar from a scripted module? I am thinking of the progress bar which sometimes appears when running a CLI module or something similar.</p>
<p><a href="https://github.com/KitwareMedical/SlicerITKUltrasound/commit/d5f3f4a7dc0ac507e47eb46783ff876b6b77bfc1#diff-928228c3d79d7a1efcefd79907d8089c0f8b11753b78b613869ee30e5d6132adR345" rel="noopener nofollow ugc">ITK Ultrasound BMode filter</a> is concrete module I am working on. As ITK filters usually have progress, it would be good if we could route these updates to Slicer’s GUI.</p>

---

## Post #2 by @pieper (2023-03-17 22:43 UTC)

<p>You could look how it’s done in SimpleITK.  <a href="https://www.na-mic.org/wiki/2013_Project_Week:Threaded_SimpleITK_Modules">We set it up to</a> release the GIL during processing.</p>

---
