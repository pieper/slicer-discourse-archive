# Surface area of model "islands" after threshold applied

**Topic ID**: 21057
**Date**: 2021-12-14
**URL**: https://discourse.slicer.org/t/surface-area-of-model-islands-after-threshold-applied/21057

---

## Post #1 by @adamy (2021-12-14 16:30 UTC)

<p>Hello everyone. I have a model which has a scalar value at every cell (first image). I have applied a threshold (from the Models module) and the result is in the second image. The location of the islands does not need to be obtained, however, I would like to calculate (1) the number of islands and (2) the surface area of each island after thresholding. Any help would be greatly appreciated!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/91be7df062421b4388444ba5cf9f81c0e1a020ee.jpeg" data-download-href="/uploads/short-url/kNjml7GVX86A1csfQ8OtAcaRvXM.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/91be7df062421b4388444ba5cf9f81c0e1a020ee_2_396x375.jpeg" alt="image" data-base62-sha1="kNjml7GVX86A1csfQ8OtAcaRvXM" width="396" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/91be7df062421b4388444ba5cf9f81c0e1a020ee_2_396x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/91be7df062421b4388444ba5cf9f81c0e1a020ee_2_594x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/91be7df062421b4388444ba5cf9f81c0e1a020ee.jpeg 2x" data-dominant-color="CBCB61"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">630×596 171 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/508fb714f67cc6f878cd70895eb2f2124e41ef4f.png" data-download-href="/uploads/short-url/buG6zhMG0uWzRlhe5JEM1NNJwoT.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/508fb714f67cc6f878cd70895eb2f2124e41ef4f_2_405x375.png" alt="image" data-base62-sha1="buG6zhMG0uWzRlhe5JEM1NNJwoT" width="405" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/508fb714f67cc6f878cd70895eb2f2124e41ef4f_2_405x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/508fb714f67cc6f878cd70895eb2f2124e41ef4f_2_607x562.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/508fb714f67cc6f878cd70895eb2f2124e41ef4f.png 2x" data-dominant-color="F8F6F9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">623×575 26.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2021-12-14 17:48 UTC)

<p>I don’t think there is a module for this task, but you can get what you need by a bit of Python scripting (probably 20-30 lines in total): assign a unique scalar to each island using vtkPolyDataConnectivityFilter, extract each island using vtkThreshold, and then get its surface area using vtkMassProperties. See examples of how to use VTK filters on models in Slicer in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#models">script repository</a>.</p>

---
