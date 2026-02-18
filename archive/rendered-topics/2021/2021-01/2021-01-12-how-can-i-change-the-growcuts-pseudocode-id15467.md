# How can I change the GrowCut's pseudocode?

**Topic ID**: 15467
**Date**: 2021-01-12
**URL**: https://discourse.slicer.org/t/how-can-i-change-the-growcuts-pseudocode/15467

---

## Post #1 by @Anonymous1 (2021-01-12 08:17 UTC)

<p>Hi!</p>
<p>I want to change the GrowCut’s pseudocode in Slicer 3D so that it has another function or an ‘extra’.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/479ae2ce36f397d3c435506b759d060f1c73db0e.png" data-download-href="/uploads/short-url/adrK0oCruLj1Ndd9YkwYjmGO7Zs.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/479ae2ce36f397d3c435506b759d060f1c73db0e_2_677x499.png" alt="image" data-base62-sha1="adrK0oCruLj1Ndd9YkwYjmGO7Zs" width="677" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/479ae2ce36f397d3c435506b759d060f1c73db0e_2_677x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/479ae2ce36f397d3c435506b759d060f1c73db0e_2_1015x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/479ae2ce36f397d3c435506b759d060f1c73db0e.png 2x" data-dominant-color="F9F9F9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1208×892 56 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
This is the pseudocode that I need to change in Python. Does anyone know how I can do it?</p>
<p>Thank you</p>

---

## Post #2 by @lassoan (2021-01-12 20:55 UTC)

<p>The code is implemented in C++ (running such pixel-level manipulation in Python would be incredibly slow). Once you build Slicer, you can easily modify the algorithm. The source code is <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/Logic/vtkImageGrowCutSegment.cxx">here</a>.</p>
<p>We already improved upon the originally described cost, for example we added a m_DistancePenalty term to add locality constraint. How do you plan to modify the cost term, for what purpose?</p>

---

## Post #3 by @Anonymous1 (2021-01-12 22:34 UTC)

<p>What I intend to do is to experiment with a specific function or routine that I have been able to implement from the GrowCut algorithm with the Python interpreter of Slicer4 and draw conclusions.</p>

---
