# Adding "missing" images to extend volume

**Topic ID**: 5860
**Date**: 2019-02-20
**URL**: https://discourse.slicer.org/t/adding-missing-images-to-extend-volume/5860

---

## Post #1 by @rshalev (2019-02-20 22:41 UTC)

<p>I have 200 2D images (slices) which represent a volume of a blood vessel (basically, a tube). The pixel size in each of the 2D images is 5 microns and the distance between the slices is 200 microns. How can I add slices such that, when viewing the volume, the voxels are approximately square (i.e. how to I add 40 new slices between each pair of the original slices?).</p>
<p>Thank you</p>

---

## Post #2 by @cpinter (2019-02-20 23:08 UTC)

<p>If the data you have is a scalar volume or labelmap volume then you can resample it in the Crop Volumes module.<br>
What format is the file(s) you load into Slicer?</p>

---

## Post #3 by @rshalev (2019-02-20 23:24 UTC)

<p>I have it in a single file as stacked tiff. I separated the stacked tiff and saved the separate images in order to load into 3D Slicer.</p>

---
