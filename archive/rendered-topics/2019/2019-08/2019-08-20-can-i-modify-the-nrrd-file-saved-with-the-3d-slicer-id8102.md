# Can I modify the nrrd file saved with the 3D Slicer?

**Topic ID**: 8102
**Date**: 2019-08-20
**URL**: https://discourse.slicer.org/t/can-i-modify-the-nrrd-file-saved-with-the-3d-slicer/8102

---

## Post #1 by @kscript (2019-08-20 01:53 UTC)

<p>Now I’m working on annotating with the 3D Slicer.</p>
<p>During Annotation, I saved the Volume and looked inside to see that it was saved as index, not color.</p>
<p>My goal is to change this index.</p>
<p>For example, if you annotate using 10 colors, numbers from 1 to 10 will be generated, and I want to change the number 5 to 7.</p>
<p>Is this possible in the 3D Slicer?</p>

---

## Post #2 by @lassoan (2019-08-21 16:27 UTC)

<p>If you save segmentation as 4D .seg.nrrd file (to allow overlapping segments) then color indices are not used, but each segment is stored with 0/1 values along the 4th dimension. You can look up the index of each segment in the <a href="https://apidocs.slicer.org/master/classvtkMRMLSegmentationStorageNode.html#details" rel="nofollow noopener">custom metadata fields in the file header</a>.</p>
<p>If you export the segmentation to a merged labelmap before writing to a 3D nrrd file, you can change voxel values using numpy before writing to file:</p>
<pre><code class="lang-python">volumeNode = getNode('Segmentation-label')

volumeArray=slicer.util.arrayFromVolume(volumeNode)
volumeArray[volumeArray==5] = 7 # change all voxel values of 5 to 7
slicer.util.arrayFromVolumeModified(volumeNode)
</code></pre>

---
