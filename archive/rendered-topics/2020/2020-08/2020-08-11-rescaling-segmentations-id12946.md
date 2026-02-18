# Rescaling Segmentations

**Topic ID**: 12946
**Date**: 2020-08-11
**URL**: https://discourse.slicer.org/t/rescaling-segmentations/12946

---

## Post #1 by @SLDT (2020-08-11 18:46 UTC)

<p>Hello Slicer Community,</p>
<p>I recently began using 3D Slicer as an alternative to Mimics, so I am still learning the nuances of the program, but I’ve run into a bit of a problem while conducting segmentations. During my first segmentation, I inadvertently scaled up the image spacing to 0.732558 mm * 0.732558 mm * 1 mm (the original image spacing for the TIFF stack that I was working with was 0.063 mm * 0.063 mm * 0.086 mm, but I scaled up the spacing because, at the time, I didn’t know how to refocus on a smaller field of view in each panel). I thought that I could rescale the model when I went to export the segmentations as STL files, but the scale factors I have tried have been producing models that are much too small and/or much to larger relative to other models that I have produced for different structures using the appropriate image spacing.</p>
<p>Is there a way to rescale the segmentations to fit the original image spacing, or, alternatively, is there a better way to calculate the scale factor during model export to get the appropriate model size? If anyone has any suggestions, I would very much like to hear them!</p>

---

## Post #2 by @lassoan (2020-08-11 18:49 UTC)

<p>You can click <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#panels-and-their-use">Specify geometry</a> button in Segment Editor module to adjust the spacing of the segmentation. After that you probably want to smooth the segmentation to take advantage of the increased resolution.</p>

---

## Post #3 by @SLDT (2020-08-11 19:12 UTC)

<p>When I open the Specify geometry panel for the master volume, all of the numeric entry fields are grayed out (i.e., I can’t edit them). Is there any reason why that might be the case, and is there any way to fix it?</p>

---

## Post #4 by @lassoan (2020-08-11 19:13 UTC)

<p>Yes, you need to select a source node as described <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#panels-and-their-use">here</a>.</p>

---

## Post #5 by @SLDT (2020-08-11 20:24 UTC)

<p>When I select either the master volume or the segmentation as the source geometry in the Specify geometry panel, the numeric entry fields remained grayed out. I reviewed the page that you linked, but it doesn’t seem to specify any additional information about why this might be happening. Is there something that I am missing?</p>

---

## Post #6 by @lassoan (2020-08-11 20:40 UTC)

<p>Can you post a screenshot?</p>
<p>It should be possible to enter spacing, everything else is computed from that.</p>

---

## Post #8 by @SLDT (2020-08-11 20:52 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b8f933e7f512df3feb5cb4089f9ff1b6779b936f.png" data-download-href="/uploads/short-url/qolLG4vtVTmaeLpJ0zSDU1PiR2v.png?dl=1" title="Source Geometry" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b8f933e7f512df3feb5cb4089f9ff1b6779b936f_2_690x374.png" alt="Source Geometry" data-base62-sha1="qolLG4vtVTmaeLpJ0zSDU1PiR2v" width="690" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b8f933e7f512df3feb5cb4089f9ff1b6779b936f_2_690x374.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b8f933e7f512df3feb5cb4089f9ff1b6779b936f_2_1035x561.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b8f933e7f512df3feb5cb4089f9ff1b6779b936f_2_1380x748.png 2x" data-dominant-color="88878D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Source Geometry</span><span class="informations">1920×1041 366 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Alright, here is a screenshot of the panel.</p>

---

## Post #9 by @lassoan (2020-08-11 21:12 UTC)

<p>This looks good! You can specify spacing by specifying oversampling factor and isotropic spacing checkbox and see the resulting geometry in the “Segmentation labelmap geometry” section.</p>

---

## Post #10 by @SLDT (2020-08-11 21:51 UTC)

<p>Thank you! When I tried applying the oversampling factor, though, I received the following error:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e4e7fa4d042b4223cc286cad2e77da7bf553079.png" data-download-href="/uploads/short-url/fJOHF6KuJ54PBAmdmEHFnEReDIl.png?dl=1" title="Error" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e4e7fa4d042b4223cc286cad2e77da7bf553079_2_690x374.png" alt="Error" data-base62-sha1="fJOHF6KuJ54PBAmdmEHFnEReDIl" width="690" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e4e7fa4d042b4223cc286cad2e77da7bf553079_2_690x374.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e4e7fa4d042b4223cc286cad2e77da7bf553079_2_1035x561.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e4e7fa4d042b4223cc286cad2e77da7bf553079_2_1380x748.png 2x" data-dominant-color="7F7D83"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Error</span><span class="informations">1920×1041 391 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #11 by @lassoan (2020-08-11 22:22 UTC)

<p>“Bad allocation” means that you have run out of memory. Since oversampling by a factor of 2 increases memory need by almost a magnitude, it is easy to go overboard. I would recommend to upgrade to latest Slicer Preview Release, as we have made memory management of non-overlapping segments more efficient. You can also increase virtual memory size in your system settings to make sure that there is always enough memory space (I would recommend having 10x more memory than your raw data size to allow enough memory for data processing and visualization).</p>

---

## Post #12 by @ahmad_alminnawi (2023-07-10 14:09 UTC)

<p>Can you please let me know how to do so using python instead of GUI?</p>

---

## Post #13 by @lassoan (2023-07-10 14:13 UTC)

<p>See <a href="https://discourse.slicer.org/t/change-spacing-of-segment-using-python/30499" class="inline-onebox">Change spacing of segment using Python</a></p>

---
