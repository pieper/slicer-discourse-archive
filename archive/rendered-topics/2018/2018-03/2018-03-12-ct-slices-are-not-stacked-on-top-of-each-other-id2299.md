# CT slices are not stacked on top of each other

**Topic ID**: 2299
**Date**: 2018-03-12
**URL**: https://discourse.slicer.org/t/ct-slices-are-not-stacked-on-top-of-each-other/2299

---

## Post #1 by @ReNeu (2018-03-12 15:49 UTC)

<p>Hi Andras,</p>
<p>Another problem that I have encountered while loading a file of CT images is that they don’t stack on top of each other.  This does not occur when viewing the images outside Slicer. I’ve tried attaching screen shots.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/dd279b603d7a182bb913392be273a21639a0ca51.jpeg" data-download-href="/uploads/short-url/vyqnsJ4KfiUo2LgZhy0C3Jd2Kjv.jpeg?dl=1" title="Unstacked%20CT%20slices" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd279b603d7a182bb913392be273a21639a0ca51_2_690x387.jpeg" alt="Unstacked%20CT%20slices" data-base62-sha1="vyqnsJ4KfiUo2LgZhy0C3Jd2Kjv" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd279b603d7a182bb913392be273a21639a0ca51_2_690x387.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd279b603d7a182bb913392be273a21639a0ca51_2_1035x580.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/dd279b603d7a182bb913392be273a21639a0ca51.jpeg 2x" data-dominant-color="898888"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Unstacked%20CT%20slices</span><span class="informations">1366×768 111 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b7f273479e19d899c0ee08f0b3bb3d4845306604.png" data-download-href="/uploads/short-url/qfgP7kOw3bV758BKyVfrtQcLFEE.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b7f273479e19d899c0ee08f0b3bb3d4845306604_2_690x387.png" alt="image" data-base62-sha1="qfgP7kOw3bV758BKyVfrtQcLFEE" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b7f273479e19d899c0ee08f0b3bb3d4845306604_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b7f273479e19d899c0ee08f0b3bb3d4845306604_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b7f273479e19d899c0ee08f0b3bb3d4845306604.png 2x" data-dominant-color="848383"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1366×768 115 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Cheers,</p>
<p>Ettie</p>

---

## Post #2 by @lassoan (2018-03-12 15:56 UTC)

<p>By default Slicer shows standard axial, sagittal, coronal oriented slices. If your volume is not axis-aligned and the spacing between slices is very large then you may get staircase appearance.</p>
<p>For non-axis-aligned acquisitions, you may want to show the slices in their native orientation, by <a href="https://discourse.slicer.org/t/mri-dwi-images-load-with-wrong-orientation/482/2?u=lassoan">using “Rotate to volume plane” function</a>.</p>
<p>If you want to process a volume that has highly anisotropic spacing (e.g., 10x larger spacing between slices than spacing between pixels within a slice) and you want to process it (segment, register, etc.) then it is strongly recommended to crop&amp;resample the volume to have isotropic spacing, using Crop volume module.</p>

---
