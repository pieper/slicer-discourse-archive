# How can I find midsagittal slice from dicom file

**Topic ID**: 32954
**Date**: 2023-11-22
**URL**: https://discourse.slicer.org/t/how-can-i-find-midsagittal-slice-from-dicom-file/32954

---

## Post #1 by @Nutchanon_Hemapattam (2023-11-22 12:14 UTC)

<p>I want to annotate the landmark in sagittal plane, but I can’t find the midsagittal slice.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/1830fa9d1d3337c21873a154e29a44eefd3437be.jpeg" data-download-href="/uploads/short-url/3s0oz6j18kx72kBj8dmESgw7Z6e.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/1830fa9d1d3337c21873a154e29a44eefd3437be_2_690x427.jpeg" alt="image" data-base62-sha1="3s0oz6j18kx72kBj8dmESgw7Z6e" width="690" height="427" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/1830fa9d1d3337c21873a154e29a44eefd3437be_2_690x427.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/1830fa9d1d3337c21873a154e29a44eefd3437be_2_1035x640.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/1830fa9d1d3337c21873a154e29a44eefd3437be_2_1380x854.jpeg 2x" data-dominant-color="4E4E5A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1471×912 72.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2023-11-22 12:21 UTC)

<p>All the sagittal slices are displayed in the Yellow slice viewer, including the midsagittal one.</p>
<p>To locate the middle slice, probably the easiest is to enable display of slice intersections in the toolbar and hold down the Shift key while moving the mouse (do not click the mouse button) in the axial (red) slice view:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f12fa26bfa502bbd19172719db5688b388fbabe7.jpeg" data-download-href="/uploads/short-url/ypD7Rbi8lt0MOeqJSZbB6Gv0lg3.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f12fa26bfa502bbd19172719db5688b388fbabe7_2_690x418.jpeg" alt="image" data-base62-sha1="ypD7Rbi8lt0MOeqJSZbB6Gv0lg3" width="690" height="418" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f12fa26bfa502bbd19172719db5688b388fbabe7_2_690x418.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f12fa26bfa502bbd19172719db5688b388fbabe7_2_1035x627.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f12fa26bfa502bbd19172719db5688b388fbabe7_2_1380x836.jpeg 2x" data-dominant-color="424144"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1165 145 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @Nutchanon_Hemapattam (2023-11-22 15:34 UTC)

<p>I’m so grateful for your help. Thank you for your advice.</p>

---

## Post #4 by @Nutchanon_Hemapattam (2023-11-25 16:15 UTC)

<p>Excuse me sir, I have one more question.<br>
How can we be sure that the selected slide is actually the middle slide?</p>

---

## Post #5 by @lassoan (2023-11-25 17:51 UTC)

<p>In the axial (red) view you can see when the yellow slice is in the middle.</p>

---
