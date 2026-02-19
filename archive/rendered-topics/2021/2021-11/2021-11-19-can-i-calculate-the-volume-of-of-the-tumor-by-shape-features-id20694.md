---
topic_id: 20694
title: "Can I Calculate The Volume Of Of The Tumor By Shape Features"
date: 2021-11-19
url: https://discourse.slicer.org/t/20694
---

# can I calculate the volume of  of the tumor by shape features ?

**Topic ID**: 20694
**Date**: 2021-11-19
**URL**: https://discourse.slicer.org/t/can-i-calculate-the-volume-of-of-the-tumor-by-shape-features/20694

---

## Post #1 by @mina (2021-11-19 07:00 UTC)

<p>Hello,<br>
I am  doing a radiomics project in 3D Slicer and I am new to all the things.<br>
I have a problem.<br>
I need to have the volume of the tumor, but in the extracted features (Shape features), there is no Volume and no compactness.<br>
I read some articles and according  to them, I can calculate volume by counting the number of pixels in the tumor region and multiplying this value by the voxel size.<br>
For shape features I have these features:</p>
<p>Elongation	<br>
Flatness	<br>
LeastAxisLength	<br>
MajorAxisLength	<br>
Maximum2DDiameterColumn	<br>
Maximum2DDiameterRow	<br>
Maximum2DDiameterSlice	<br>
Maximum3DDiameter	<br>
MeshVolume	<br>
MinorAxisLength	<br>
Sphericity	<br>
SurfaceArea	<br>
SurfaceVolumeRatio	<br>
VoxelVolume</p>
<p>how can I calculate the volume of the tumor ?<br>
I’m sorry if my question seems very basic.It’s my 1st project and I am somehow confused.<br>
would you please help me .</p>

---

## Post #2 by @mikebind (2021-11-19 17:20 UTC)

<p>I’m not sure what module you are using, so I can’t be 100% confident, but I expect the value you are looking for is in the VoxelVolume feature.  This is almost certainly the volume of the region as calculated by counting the number of voxels included multiplie by the volume of a voxel. I suspect MeshVolume is also the region volume, calculated as the volume inside a surface mesh.  These may differ slightly due to smoothing during the generation of the mesh or due to pixelization of the surface, but should be very similar for any large or compact shape.</p>

---

## Post #3 by @mina (2021-11-19 18:06 UTC)

<p>Thank you very much.<br>
You helped me a lot.<br>
Thank you.</p>

---

## Post #4 by @rbumm (2021-11-19 20:51 UTC)

<p>A different, maybe easier approach would be to segment the tumor in the segment editor and run “Segment Statistics” on the segmentation results. “Segment Statistics” can be found in “Quantification” submenu.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba25a58c07a6da39b1c0cbd8ba72daa8327b8059.jpeg" data-download-href="/uploads/short-url/qyJsXBcrEFQl5cFnSEJpUKxOVC1.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/ba25a58c07a6da39b1c0cbd8ba72daa8327b8059_2_690x370.jpeg" alt="image" data-base62-sha1="qyJsXBcrEFQl5cFnSEJpUKxOVC1" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/ba25a58c07a6da39b1c0cbd8ba72daa8327b8059_2_690x370.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba25a58c07a6da39b1c0cbd8ba72daa8327b8059.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba25a58c07a6da39b1c0cbd8ba72daa8327b8059.jpeg 2x" data-dominant-color="B2B2BC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1012×543 142 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
