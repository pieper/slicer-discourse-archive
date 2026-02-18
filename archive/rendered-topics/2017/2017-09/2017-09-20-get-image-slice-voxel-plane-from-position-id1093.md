# Get image slice/voxel plane from position

**Topic ID**: 1093
**Date**: 2017-09-20
**URL**: https://discourse.slicer.org/t/get-image-slice-voxel-plane-from-position/1093

---

## Post #1 by @stevenagl12 (2017-09-20 17:09 UTC)

<p>Also, does anyone know if there is an easy way to figure out slice/voxel planes from the positions you desire in 3d slicer? What I mean is, if I want to know a particular slice number given the transverse (red) position in mm’s out of all the volume slices in a faster method than calculating it, is there one? Same with the sagittal and coronal planes to figure out the dimensions for a potential bounding box for an automated segmentation pipeline?</p>

---

## Post #2 by @lassoan (2017-09-20 19:17 UTC)

<aside class="quote no-group quote-modified" data-username="stevenagl12" data-post="2" data-topic="1092">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/stevenagl12/48/3391_2.png" class="avatar"><a href="https://discourse.slicer.org/t/automated-registration-in-the-nightly-build/1092/2">Automated registration in the Nightly Build</a></div>
<blockquote>
<p>if I want to know a particular slice number given the transverse (red) position in mm’s out of all the volume slices in a faster method than calculating it, is there one?</p>
</blockquote>
</aside>
<p>“Computation” of IJK (voxel coordinates) from RAS or LPS (physical coordinates) is multiplication of the coordinates by a 4x4 matrix, so it cannot really be any simpler than that. The matrix you need is the RAS to IJK matrix, available in the volume node.</p>

---

## Post #3 by @stevenagl12 (2017-09-21 16:59 UTC)

<p>The listed IJK to RAS direction matrix in the volumes module is only a 3x3 matrix (-1, 0, 0; 0, -1, 0;0, 0, 1). How do I get the 4x4 matrix then?</p>

---

## Post #4 by @stevenagl12 (2017-09-21 17:05 UTC)

<p>Also, ultimately what I am trying to do is figure out the file number from the volume of files that starts and ends my boudning box, then the planes for the sides with the voxels. This will work that out for me?</p>

---

## Post #5 by @stevenagl12 (2017-09-21 17:26 UTC)

<p>My bounding box is going to be hard-coded values for the dimensions to automatically generate the bounding box in all of my CT volumes, but I’m not sure how to do that in slicer so I am trying to do it in MATLAB, but I need to know the dimension from the volume of files?</p>

---

## Post #6 by @cpinter (2017-09-21 17:57 UTC)

<p>There’s a bunch of utility functions to convert positions between world, image, and slice positions:<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/EditorEffects/qSlicerSegmentEditorAbstractEffect.h#L342-L368" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/EditorEffects/qSlicerSegmentEditorAbstractEffect.h#L342-L368" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/EditorEffects/qSlicerSegmentEditorAbstractEffect.h#L342-L368</a></h4>
<pre class="onebox"><code class="lang-h"><ol class="start lines" start="342" style="counter-reset: li-counter 341 ;">
<li>/// Convert RAS position to XY in-slice position</li>
<li>static QPoint rasToXy(double ras[3], qMRMLSliceWidget* sliceWidget);</li>
<li>/// Convert RAS position to XY in-slice position, python accessor method</li>
<li>Q_INVOKABLE static QPoint rasToXy(QVector3D ras, qMRMLSliceWidget* sliceWidget);</li>
<li>/// Convert XYZ slice view position to RAS position:</li>
<li>/// x,y uses slice (canvas) coordinate system and actually has a 3rd z component (index into the</li>
<li>/// slice you're looking at), hence xyToRAS is really performing xyzToRAS. RAS is patient world</li>
<li>/// coordinate system. Note the 1 is because the transform uses homogeneous coordinates.</li>
<li>static void xyzToRas(double inputXyz[3], double outputRas[3], qMRMLSliceWidget* sliceWidget);</li>
<li>/// Convert XYZ slice view position to RAS position, python accessor method</li>
<li>Q_INVOKABLE static QVector3D xyzToRas(QVector3D inputXyz, qMRMLSliceWidget* sliceWidget);</li>
<li>/// Convert XY in-slice position to RAS position</li>
<li>static void xyToRas(QPoint xy, double outputRas[3], qMRMLSliceWidget* sliceWidget);</li>
<li>/// Convert XY in-slice position to RAS position</li>
<li>static void xyToRas(double xy[2], double outputRas[3], qMRMLSliceWidget* sliceWidget);</li>
<li>/// Convert XY in-slice position to RAS position, python accessor method</li>
<li>Q_INVOKABLE static QVector3D xyToRas(QPoint xy, qMRMLSliceWidget* sliceWidget);</li>
<li>/// Convert XYZ slice view position to image IJK position, \sa xyzToRas</li>
<li>static void xyzToIjk(double inputXyz[3], int outputIjk[3], qMRMLSliceWidget* sliceWidget, vtkOrientedImageData* image);</li>
<li>/// Convert XYZ slice view position to image IJK position, python accessor method, \sa xyzToRas</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/EditorEffects/qSlicerSegmentEditorAbstractEffect.h#L342-L368" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---

## Post #7 by @stevenagl12 (2017-09-21 17:59 UTC)

<p>Are these codes that I would input? I’ve never done any python coding so I’m not sure?</p>

---

## Post #8 by @lassoan (2017-09-22 04:33 UTC)

<aside class="quote no-group" data-username="stevenagl12" data-post="4" data-topic="1093">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/stevenagl12/48/3391_2.png" class="avatar"> stevenagl12:</div>
<blockquote>
<p>figure out the file number from the volume of files that starts and ends my boudning box</p>
</blockquote>
</aside>
<p>Getting the DICOM file number from physical coordinates is much more complicated than getting IJK coordinates from a volume file. Doing all this in Matlab sounds even worse.</p>
<p>Fortunately, you can easily crop the volume in Slicer by creating a small Python script that creates a region of interest (ROI) node and uses the Crop volume module to crop the input volume using that ROI node. You can get started by completing the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Programming_Tutorial">Slicer4 programming tutorial</a> then create a new module that does the cropping you need. If you are stuck at any point then post your question and a link to the source code of your module on GitHub and we’ll help you.</p>

---
