# Vmtkflowextensions

**Topic ID**: 19656
**Date**: 2021-09-14
**URL**: https://discourse.slicer.org/t/vmtkflowextensions/19656

---

## Post #1 by @ames (2021-09-14 06:20 UTC)

<p>I am using vmtkflowextensions to add short flow extensions to the inlet and outlets of my 3D model. In the attached screencapture it can be seen that the flow extension does not fit nicely to the domain.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b96cdf0124e320391ec912d3aa7fa7a2e8d5864e.png" data-download-href="/uploads/short-url/qslApD9kAnKgncaSdswkHka8SAu.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b96cdf0124e320391ec912d3aa7fa7a2e8d5864e_2_519x499.png" alt="image" data-base62-sha1="qslApD9kAnKgncaSdswkHka8SAu" width="519" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b96cdf0124e320391ec912d3aa7fa7a2e8d5864e_2_519x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b96cdf0124e320391ec912d3aa7fa7a2e8d5864e.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b96cdf0124e320391ec912d3aa7fa7a2e8d5864e.png 2x" data-dominant-color="D4747B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">737×710 62.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>vmtksurfacereader -ifile inputfile --pipe vmtkcenterlines -seedselector openprofiles --pipe vmtkflowextensions -extensionratio 2 -normalestimationratio 1 -ofile ouptutfile</p>
<p>I am using the above line of code. Where does the problem with the flow extension come from?</p>

---

## Post #2 by @kayarre (2021-11-04 21:10 UTC)

<p>What does the outlet look like before you add the flow extensions?</p>
<p>check the surface normal direction, and the radius value its calculating.</p>
<p>I believe there is also a flag that tapers the extension.</p>

---
