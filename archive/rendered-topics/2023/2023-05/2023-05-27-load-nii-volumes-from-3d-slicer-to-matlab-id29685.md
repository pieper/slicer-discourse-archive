---
topic_id: 29685
title: "Load Nii Volumes From 3D Slicer To Matlab"
date: 2023-05-27
url: https://discourse.slicer.org/t/29685
---

# Load nii volumes from 3d Slicer to Matlab

**Topic ID**: 29685
**Date**: 2023-05-27
**URL**: https://discourse.slicer.org/t/load-nii-volumes-from-3d-slicer-to-matlab/29685

---

## Post #1 by @Anatole (2023-05-27 03:44 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 3D Slicer 5.2.2.2<br>
Expected behavior: Get the same volumes with the same absolute position in world coordinates from 3d Slicer in Matlab<br>
Actual behavior: Get a slight position difference in world coordinates from 3d Slicer in Matlab</p>
<p>I loaded 2 nifti volumes on 3d Slicer and on Matlab. I tried to get the same world coordinates in Matlab as 3dSlicer.<br>
When visualising volume 1 and volume 2 in world coordinates with matlab I have a slight diffrence in positions.<br>
How to load in world coordinates nii volumes on Maltab ?</p>
<p>Code used below<br>
Code :<br>
% Referential where data are loaded<br>
Rref = imref3d([800 800 400],[-200 200],[-200 200],[-100 100]);</p>
<p>% Load volume 1 from 3d Slicer in Referential Rref<br>
Vol1=niftiread(fixedpath);<br>
Vol1=permute(Vol1,[2 1 3]);<br>
info=niftiinfo(niipath);<br>
tformload=affine3d(info.Transform.T);<br>
Vol1=imwarp(Vol1,imref3d(size(Vol1)),tformload,‘nearest’,‘FillValues’,min(Vol1(:)),‘OutputView’,Rref);</p>
<p>% Load volume 2 from 3d Slicer in Referential Rref<br>
Vol2=niftiread(movingpath);<br>
Vol2=permute(Vol2,[2 1 3]);<br>
info=niftiinfo(niipath);<br>
tformload=affine3d(info.Transform.T);<br>
Vol2=imwarp(Vol2,imref3d(size(Vol2)),tformload,‘nearest’,‘FillValues’,min(Vol2(:)),‘OutputView’,Rref);</p>
<p>Volumes on Slicer<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/020caeb127e58ae3f03ba53f588641096c7e71a8.jpeg" alt="image" data-base62-sha1="i87RyXkh6Au3pSkUMTwCCXjuuk" width="638" height="406"><br>
Volumes on Matlab<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a74faca744cbac098e7736027900c80c34ac775.png" data-download-href="/uploads/short-url/jKQw9LygwEFmXHqnZQi21XhrFQx.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a74faca744cbac098e7736027900c80c34ac775.png" alt="image" data-base62-sha1="jKQw9LygwEFmXHqnZQi21XhrFQx" width="494" height="500" data-dominant-color="63655E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1123×1135 43.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2023-05-27 03:58 UTC)

<p>Nifti is a highly problematic file format with lots of complexities and ambiguities.</p>
<p>I would recommend to save in NRRD file format instead and read/write in Matlab using nrrdread.m and nrrdwrite.m - see <a href="https://github.com/PerkLab/SlicerMatlabBridge/tree/master/MatlabCommander/commandserver">here</a>.</p>

---
