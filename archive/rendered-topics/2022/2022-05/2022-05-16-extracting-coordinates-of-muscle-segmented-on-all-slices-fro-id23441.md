---
topic_id: 23441
title: "Extracting Coordinates Of Muscle Segmented On All Slices Fro"
date: 2022-05-16
url: https://discourse.slicer.org/t/23441
---

# Extracting coordinates of muscle segmented on all slices from MRI scans

**Topic ID**: 23441
**Date**: 2022-05-16
**URL**: https://discourse.slicer.org/t/extracting-coordinates-of-muscle-segmented-on-all-slices-from-mri-scans/23441

---

## Post #1 by @Eva (2022-05-16 13:45 UTC)

<p>Hello,</p>
<p>I have segmented muscles on MRI scans every 10 slices and I would like to find the line of action of a muscle. I have to get the centroid of each area segmented to then draw a line between these points.</p>
<p>I can’t find a module to do that in Slicer.<br>
Is there a module which calculate the centroid of each area segmented ? Or can we extract every outlines coordinates of each area segmented ?</p>
<p>Thank you for your response,</p>
<p>Eva</p>

---

## Post #2 by @ebrahim (2022-05-16 15:38 UTC)

<p>Check out <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentstatistics.html" rel="noopener nofollow ugc">segment statistics</a></p>

---

## Post #3 by @lassoan (2022-05-16 21:46 UTC)

<p>If you want to get the centerline of the area segmented then you can use <code>Extract Centerline</code> module in <a href="https://github.com/vmtk/SlicerExtension-VMTK/">VMTK extension</a>. Once you have the centerline you can use <code>Cross-section analysis</code> module to get further information (cross-section areas, resliced images, etc.).</p>
<p>You may also find <a href="https://github.com/jmhuie/Slicer-SegmentGeometry">SegmentGeometry extension</a> useful.</p>

---

## Post #4 by @Eva (2022-05-17 08:42 UTC)

<p>Thank you for your respond.</p>
<p>Unfortunatly, the Extract Centerline module don’t work on the muscle I’m intersting in. The centerline doesn’t follow the muscle line of action at all. I think it’s because this module is adapted to get the centerline of a vessel (which is thin and long) and not on a fat muscle.</p>
<p>Do you have an another solution ?</p>

---

## Post #5 by @lassoan (2022-05-28 00:14 UTC)

<p>Centerline extraction with the “Tree” method should work even if the shape is not very elongated:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/eefe6a874a5f1644ce16b66d9a761e84df31d86e.png" data-download-href="/uploads/short-url/y6eILnXowaA7bt49LpZp98x8v5I.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/eefe6a874a5f1644ce16b66d9a761e84df31d86e_2_508x500.png" alt="image" data-base62-sha1="y6eILnXowaA7bt49LpZp98x8v5I" width="508" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/eefe6a874a5f1644ce16b66d9a761e84df31d86e_2_508x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/eefe6a874a5f1644ce16b66d9a761e84df31d86e_2_762x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/eefe6a874a5f1644ce16b66d9a761e84df31d86e_2_1016x1000.png 2x" data-dominant-color="424241"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1054×1036 53.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If you share an example segmentation (upload the .seg.nrrd file somewhere and post the link here) then I can confirm.</p>
<hr>
<p>Have you tried to use the <a href="https://github.com/jmhuie/Slicer-SegmentGeometry">SegmentGeometry extension</a>? It can give you the coordinates of the centroid points along a reslice axis, which is exactly what you are looking for. The only possible inconvenience is that these centroid positions are reported in voxel coordinate system of the resampled volume, so if you need the centroid positions in RAS coordinate system then you’ll need to multiply voxel coordinates by IJKtoRAS matrix of the resampled volume.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f7bd0cb50538a197fa8cf3387746d5b04a0a79cd.png" data-download-href="/uploads/short-url/zlAYh3PM8DAULaaJGTFPPtyHV6d.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f7bd0cb50538a197fa8cf3387746d5b04a0a79cd_2_690x409.png" alt="image" data-base62-sha1="zlAYh3PM8DAULaaJGTFPPtyHV6d" width="690" height="409" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f7bd0cb50538a197fa8cf3387746d5b04a0a79cd_2_690x409.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f7bd0cb50538a197fa8cf3387746d5b04a0a79cd_2_1035x613.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f7bd0cb50538a197fa8cf3387746d5b04a0a79cd_2_1380x818.png 2x" data-dominant-color="44494C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2329×1381 254 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><a class="mention" href="/u/jmhuie">@jmhuie</a></p>

---

## Post #6 by @Eva (2022-06-08 07:44 UTC)

<p>Thank you very much. SegmentGeometry extension contains exactly what I was searching. Can you precise how I can transform voxel coordinates to RAS coodinates ?</p>

---

## Post #7 by @mau_igna_06 (2022-06-08 09:57 UTC)

<p>Yuo need to use the ijkToRasTransformMatrix from the cirrent volume</p>

---

## Post #8 by @Eva (2022-06-08 12:03 UTC)

<p>Thank you but the IJKtoRAS matrix is a 3x3 matrix and I have only 2 coordinates in voxel (Cx, Cy). The multiplication between these 2 matrices is not possible. Can you help me with that ?</p>

---

## Post #9 by @mau_igna_06 (2022-06-08 12:09 UTC)

<p>If you have only two coordinates you should use something like appears on this post</p><aside class="quote quote-modified" data-post="8" data-topic="23133">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/center-coordinates-of-volume-slices/23133/8">Center coordinates of volume slices?</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Think I got it working (C++) by 
//----------------------------------------------------------------------
void GetBackgroundVolumeXYCenter(double slicePos[2])
{
    vtkMRMLSliceCompositeNode* compositeNode = nullptr;
    compositeNode = vtkMRMLSliceCompositeNode::SafeDownCast(this-&gt;GetSliceNode()-&gt;GetScene()-&gt;GetFirstNodeByClass("vtkMRMLSliceCompositeNode"));
    const char* backgroundVolumeID = compositeNode-&gt;GetBackgroundVolumeID();

    double volumeBounds[6] = { 0.0 };
    double volumeCente…
  </blockquote>
</aside>

<p>If you have 1 slice only you dhould add a 0 to the third coordinate</p>

---

## Post #10 by @lassoan (2022-06-13 14:19 UTC)

<p>IJKtoRAS is a 4x4 homogenous matrix. As <a class="mention" href="/u/mau_igna_06">@mau_igna_06</a> said, if you have a single slice then K coordinate (third value) is 0. The last value is 1 if the coordinates specify a position (and 0 if the coordinates specify a direction vector). Note that this is not some Slicer specific thing but standard “homogeneous coordinates” representation and “homogeneous linear transformations”.</p>

---

## Post #11 by @Eva (2022-06-27 12:12 UTC)

<p>Thank you for your help.<br>
I understand that I have to use the IJKtoRAS matrix to find the centroid coordinates in RAS coordinates system from IJK coordinates system.<br>
I found a IJKtoRAS matrix in the “Segment” section. Can I use this matrix ?<br>
I also found how to calculate the IJKtoRAS matrix with the origin and the spacing, but I don’t found the same result as the IJKtoRAS matrix in Slicer.<br>
One last thing, the Slicer documentation says “Cx correspond to the resampled and cropped volume exported by SegmentGeometry”. Is that mean that the origin of IJK coordinates system is at then beginning of the segmented muscle and not at the beginning of the MRI image ?</p>

---
