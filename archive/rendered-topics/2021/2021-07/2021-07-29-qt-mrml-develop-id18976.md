# QT+MRML develop

**Topic ID**: 18976
**Date**: 2021-07-29
**URL**: https://discourse.slicer.org/t/qt-mrml-develop/18976

---

## Post #1 by @yuguoxin (2021-07-29 16:54 UTC)

<p>main.cpp<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/68d6768e9431bf7fee52564f54f58b53ed5f88de.png" alt="image" data-base62-sha1="eXr8NX5VbuYy2FUMAoTrKqWitaK" width="408" height="146"><br>
mainwindow.cpp<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0edd46ee5620d69d8b9aa1e422c8ba05592a5b0b.png" data-download-href="/uploads/short-url/27uLEexE7tsmM54VUmJpfyRWaCL.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0edd46ee5620d69d8b9aa1e422c8ba05592a5b0b_2_690x132.png" alt="image" data-base62-sha1="27uLEexE7tsmM54VUmJpfyRWaCL" width="690" height="132" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0edd46ee5620d69d8b9aa1e422c8ba05592a5b0b_2_690x132.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0edd46ee5620d69d8b9aa1e422c8ba05592a5b0b.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0edd46ee5620d69d8b9aa1e422c8ba05592a5b0b.png 2x" data-dominant-color="2B2D2C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">872×168 37.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/695c4018c53085bbae2f3d6767f90f0c9b788de1.png" data-download-href="/uploads/short-url/f23Mm0RZVLLyBSaJnPMVsZs2BnH.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/695c4018c53085bbae2f3d6767f90f0c9b788de1_2_690x37.png" alt="image" data-base62-sha1="f23Mm0RZVLLyBSaJnPMVsZs2BnH" width="690" height="37" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/695c4018c53085bbae2f3d6767f90f0c9b788de1_2_690x37.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/695c4018c53085bbae2f3d6767f90f0c9b788de1.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/695c4018c53085bbae2f3d6767f90f0c9b788de1.png 2x" data-dominant-color="282E2E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">816×44 9.12 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/492ee69ea4fe7b852281f2c52bc91d402c0d8cf6.png" alt="image" data-base62-sha1="arpl4PUMtbLgxrC3A9FaCvL7UA6" width="614" height="69"><br>
when running the exe, exception happen<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6a2c4b49e394975e3fbc1d61e83573c09d269b2.png" alt="image" data-base62-sha1="zbQbChx8df9cmHdw95F9tPXH7EK" width="395" height="84"><br>
can you tell me why?</p>

---

## Post #2 by @lassoan (2021-07-31 22:39 UTC)

<p>Most <code>qSlicer*</code> classes assume that the application class is <code>qSlicerApplication</code> and not just a generic <code>QApplication</code>. Currently, the easiest way is to run Slicer-dependent Python code in Slicer’s Python environment (using command-line arguments, or Slicer’s Python console, or Slicer’s Jupyter kernel, or using Slicer web server, etc.).</p>
<p>In the future, maybe in a year or two, we will make essential Slicer libraries (MRML, vtkSegmentationCore, vtkAddon, vtkITK, etc.) easily pip-installable and usable without instantiating a Slicer application. Later we may make module logics and GUI widgets independently available, too. If you wanted to get this earlier and you are willing learn the internals of Slicer and work in C++ then let us know, we can help you getting started.</p>

---
