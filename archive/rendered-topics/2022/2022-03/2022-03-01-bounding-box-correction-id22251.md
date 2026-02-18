# Bounding box correction

**Topic ID**: 22251
**Date**: 2022-03-01
**URL**: https://discourse.slicer.org/t/bounding-box-correction/22251

---

## Post #1 by @Kalman (2022-03-01 21:24 UTC)

<p>Hi, I would like to ask you regarding the size of the transformation result.</p>
<p>The brief summary: I use the Elastix modul for non-linear normalization to get the transformation matrix (on a mean volume), which is then applied to a series of individual runs (having their position similar to the transformed volume) in the Transforms modul with the above created bspline matrix.</p>
<p>However, the end result dimensions are sometimes different (e.g. the bounding box sizes is altered, once it is [102 100 34], the next time is [100 101 32]). For the subsequent MATLAB analysis the software requires similar sizes. This is the error message which is currently presented in SPM:</p>
<ul>
<li>"** The images do not all have the same dimensions. **</li>
<li>The function assumes that a voxel in one image corresponds with the same  voxel in another.   This  is not a safe assumption if the  image dimensions differ.   Please  ensure  that  you  have processed all the image data in the same way (eg. check spatial normalisation bounding-boxes, voxel-sizes etc)."</li>
</ul>
<p>Is there a way how I can ensure that the outcome of a transformation always have the same dimensions? (either with the Elastix, or with another module which adds a certain number of blank (black) voxels to the volumes’ margin to create the same-dimensioned bounding-box?)</p>
<p>Thank your for your suggestions!</p>

---

## Post #2 by @Kalman (2022-03-05 19:33 UTC)

<p>I was thinking about another method: by cropping all the volumes with the same ROI box.<br>
In this way the bounding box would be identical throughout the image series.</p>
<p>One question regarding to that: is there a way to apply the cropping to multiple volumes at the same time?</p>

---
