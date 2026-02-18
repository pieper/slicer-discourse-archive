# Extract values at voxels within a segment

**Topic ID**: 28077
**Date**: 2023-02-27
**URL**: https://discourse.slicer.org/t/extract-values-at-voxels-within-a-segment/28077

---

## Post #1 by @ZSoltani (2023-02-27 21:24 UTC)

<p>Hello everyone,</p>
<p>I want to extract HU values at each voxel from my CT scan files, which for I use the following command:</p>
<p>HU_Array = slicer.util.array(‘myfile.nrrd’)</p>
<p>However, using “nrrd” file I get the values at all voxels. I was wondering if there is a way that I can extract values in a specific area after segmenting?</p>
<p>Thank you,<br>
Zahra</p>

---

## Post #2 by @muratmaga (2023-02-28 01:22 UTC)

<p>Run either the maskvolume or Split Volume effect with your segmentaiton and then run your one liner.</p>
<p>MaskVolume will set all voxels out of segmentation are to 0 (or your value of your choosing). While SplitVolume will crop out everything outside of the segmentation area.</p>

---

## Post #4 by @ZSoltani (2023-03-15 02:15 UTC)

<p>Thank you <a class="mention" href="/u/muratmaga">@muratmaga</a> for your reply. Do you know how I can get " the coordinates of voxels" inside a specific segmentation, instead of the whole nrrd file?</p>

---

## Post #5 by @muratmaga (2023-03-15 04:35 UTC)

<p>If you mean the physical (RAS) coordinates, I think you can rework this example:</p><aside class="quote quote-modified" data-post="2" data-topic="19408">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ungi/48/78573_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/convert-between-ras-and-numpy-array-indices/19408/2">Convert between RAS and numpy array indices</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    First, download MRHead data from Sample Data module 
import numpy as np
volumeArray = slicer.util.array("MRHead")  # Get the image data in numpy array format
volumeArray[60, 127, 150] = 0  # Make one voxel black, numpy array is in KJI, not IJK.
volumeNode = slicer.mrmlScene.GetFirstNodeByName("MRHead")
volumeNode.Modified()  # I think this is needed to let Slicer know the image was modified.
ijkToRasMatrix = vtk.vtkMatrix4x4()
volumeNode.GetIJKToRASMatrix(ijkToRasMatrix)
ijkPoint = np.array([150…
  </blockquote>
</aside>


---

## Post #6 by @ZSoltani (2023-03-15 16:38 UTC)

<p>Thank you <a class="mention" href="/u/muratmaga">@muratmaga</a> for your help.</p>

---

## Post #7 by @pieper (2023-03-15 16:47 UTC)

<p>If you want to know the coordinates of all voxels with a specific value you can work from this example: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-the-values-of-all-voxels-for-a-label-value">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-the-values-of-all-voxels-for-a-label-value</a></p>

---

## Post #8 by @ZSoltani (2023-03-15 17:32 UTC)

<p>That’s very useful, I appreciate that.</p>

---
