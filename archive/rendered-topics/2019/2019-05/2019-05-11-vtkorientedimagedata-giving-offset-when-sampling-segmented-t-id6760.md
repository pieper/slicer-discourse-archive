# vtkOrientedImageData giving offset when sampling segmented tumor volume

**Topic ID**: 6760
**Date**: 2019-05-11
**URL**: https://discourse.slicer.org/t/vtkorientedimagedata-giving-offset-when-sampling-segmented-tumor-volume/6760

---

## Post #1 by @joshicola (2019-05-11 15:48 UTC)

<p>I have several segmented tumors with catheters inserted to sample the biological environment.  I know the shape and location of each catheter membrane.  I want to sample this to determine what percentage of the membrane is in the tumor versus out of the tumor.</p>
<p>Using Slicer 4.10.1</p>
<pre><code class="lang-python">N = slicer.util.getNodes('Segmentation').GetSegmentation()
B=Seg.GetSegmentRepresentation('Segment_1','Binary labelmap')
</code></pre>
<p>Gives me a <code>vtkSegmentationCorePython.vtkOrientedImageData</code>  object.</p>
<p>Using,</p>
<pre><code class="lang-python">cell_ID=B.FindCell(point,...)
cell=B.GetCell(cell_ID) 
for i in range(8):
       pointValue+= weights[i]*pointData.GetValue(cell.GetPointId(i))
</code></pre>
<p>I can check for a given “point” on my membrane being within or without the segmented tumor.</p>
<p>However, the above predicts points that are offset from world coordinates by a consistent direction (scale invariant)…that varies between original volumes.</p>
<p>Exporting the above segmentation to a new labelmap (“Segmentation-label”) and sampling:</p>
<pre><code class="lang-python">SegLabel=slicer.util.getNode('Segmentation-label')
B=SegLabel.GetImageData()
</code></pre>
<p>I am able to sample points and tell if they are within or without the segmented tumor.</p>
<p>Is there something I could do better to get the point-by-point segmentation label?</p>

---

## Post #2 by @lassoan (2019-05-11 18:17 UTC)

<p>This <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_centroid_of_a_segment_in_world_.28RAS.29_coordinates" rel="nofollow noopener">example in the script repository</a> contains everything you need.</p>
<p>You can also <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Export_labelmap_node_from_segmentation_node" rel="nofollow noopener">export segments to a labelmap volume node</a> and convert between IJK and RAS coordinatesas shown in these examples: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_volume_voxel_coordinates_from_markup_fiducial_RAS_coordinates" rel="nofollow noopener">RAS-&gt;IJK</a> and <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_markup_fiducial_RAS_coordinates_from_volume_voxel_coordinates" rel="nofollow noopener">IJK-&gt;RAS</a>.</p>
<p>Oriented images have been recently introduced in VTK, which will allow us to simplify image coordinate system transformations in Slicer, but it will take us at least a couple of months to make all the necessary updates.</p>

---

## Post #3 by @joshicola (2019-05-14 15:47 UTC)

<p>Thank You!</p>
<p>The insight is appreciated!</p>

---
