# Volume transforms without changing pixel intensity?

**Topic ID**: 3727
**Date**: 2018-08-10
**URL**: https://discourse.slicer.org/t/volume-transforms-without-changing-pixel-intensity/3727

---

## Post #1 by @Chen_Lab (2018-08-10 19:30 UTC)

<p>Hello,</p>
<p>I’m a new user of 3D Slicer.  I have been using the Landmark Registration module to register my 3D image volume and then resample into a new image volume using the BRAINS Resample.   Is there a way to resample my newly registered volume such that I am only change the pixel locations of my moving volume with changing the pixel intensity values of the pixels being moved?</p>
<p>Thanks.</p>

---

## Post #2 by @fedorov (2018-08-10 19:33 UTC)

<p>If you place your volume under a linear transform, and then harden the transform (“Data” module, “Transform hierarchy” tab, select the volume and right mouse click to see the context menu), then the voxel values or raster of the volume will not change.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3d321c6b35dc7c5b9ad317a61a0f0c1a2cc149ae.png" alt="image" data-base62-sha1="8Jmug2kMWQ2Z8v1sZqYGR7klU7A" width="338" height="137"></p>

---

## Post #3 by @pieper (2018-08-10 19:44 UTC)

<p>If you end up resampling, then you can use the nearest neighbor option and this will choose one of the pixel values from the moving image at each location in the resampled image.  This may be what you want, but the result will be much “blockier” which is why the usual mode is to do some kind of averaging.</p>

---
