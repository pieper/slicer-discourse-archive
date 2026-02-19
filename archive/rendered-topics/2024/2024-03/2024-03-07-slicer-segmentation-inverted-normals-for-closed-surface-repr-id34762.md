---
topic_id: 34762
title: "Slicer Segmentation Inverted Normals For Closed Surface Repr"
date: 2024-03-07
url: https://discourse.slicer.org/t/34762
---

# Slicer Segmentation inverted normals for closed surface representation

**Topic ID**: 34762
**Date**: 2024-03-07
**URL**: https://discourse.slicer.org/t/slicer-segmentation-inverted-normals-for-closed-surface-representation/34762

---

## Post #1 by @Thibault_Pelletier (2024-03-07 07:46 UTC)

<p>Hi everyone,</p>
<p>We have recently noticed a problem when exporting STL and OBJ from segmentations in Slicer. Depending on the Volume’s affine, the generated normals can point inside instead of outside.</p>
<p>This doesn’t cause any problems for Slicer’s rendering as backface culling is disabled, but it can cause multiple problems including when trying to perform boolean operations or exporting to other softwares.</p>
<p>The problem is easily reproducible by creating a sphere brush segmentation in the following volumes :</p>
<pre><code class="lang-auto">
import numpy as np
inverted_volume = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode")
inverted_volume.SetName("InvertedVolume")
inverted_volume.CreateDefaultDisplayNodes()

m = np.eye(4)
m[0,0] = -1
m[1,1] = -1
m[2,2] = -1
inverted_volume.SetIJKToRASMatrix(slicer.util.vtkMatrixFromArray(m))
inverted_volume.SetSpacing([1, 1, 1])
slicer.util.updateVolumeFromArray(inverted_volume, np.zeros((256,256,256)))


not_inverted_volume = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode")
not_inverted_volume.SetName("NotInvertedVolume")
not_inverted_volume.CreateDefaultDisplayNodes()

m = np.eye(4)
m[0,0] = -1
m[1,1] = -1
not_inverted_volume.SetIJKToRASMatrix(slicer.util.vtkMatrixFromArray(m))
not_inverted_volume.SetSpacing([1, 1, 1])
slicer.util.updateVolumeFromArray(not_inverted_volume, np.zeros((256,256,256)))

</code></pre>
<p>Exporting to STL and displaying the face orientation in Blender yields the following results :</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/92c7f33261ee9dd8b927c9897e4eaeb52eec7460.png" alt="image" data-base62-sha1="kWu6io8Uaqveglza9biWvmqDj6U" width="283" height="456"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/74fa6782454ba4cf46e2086b4bcf1c4c707ff0c3.jpeg" data-download-href="/uploads/short-url/gGPSgX7crSL3uxScPOqLX1xKcQX.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/74fa6782454ba4cf46e2086b4bcf1c4c707ff0c3_2_312x500.jpeg" alt="image" data-base62-sha1="gGPSgX7crSL3uxScPOqLX1xKcQX" width="312" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/74fa6782454ba4cf46e2086b4bcf1c4c707ff0c3_2_312x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/74fa6782454ba4cf46e2086b4bcf1c4c707ff0c3_2_468x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/74fa6782454ba4cf46e2086b4bcf1c4c707ff0c3.jpeg 2x" data-dominant-color="4E424F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">525×841 43.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> and <a class="mention" href="/u/lassoan">@lassoan</a> what do you think of this issue?</p>
<p>Best,<br>
Thibault</p>

---

## Post #2 by @lassoan (2024-03-07 19:35 UTC)

<p>IJK coordinate system of the image must be right-handed (IJK to Physicial transformation matrix must have positive determinant). Left-handed coordinate system is currently not supported, because it would be hard to ensure that every algorithms are prepared to deal with it.</p>
<p>It would be nice if Slicer reported a warning and offer to fix it (reorder slices and invert the K axis). But until then, we rely on users to generate valid images (or resample them to a valid geometry after they are generated, before doing any further processing).</p>

---

## Post #3 by @Thibault_Pelletier (2024-03-08 06:29 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Thanks for the information!</p>
<p>In all the cases we saw, these images were loaded from NIFTI or other import file formats. So I think that handling the inversion when loading the files would be the best to address 99.9% of our needs.</p>
<p>For developers, a warning mechanism would be sufficient.</p>
<p>Do you know where would be the best places to implement these fixes?</p>

---

## Post #4 by @lassoan (2024-03-08 13:38 UTC)

<p>Inverting the slice order and flipping the K axis direction could be done right after reading the image into a VTK image in vtkMRMLVolumeArchetypeStorageNode:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/024b340baaa191968b6fc954b9f0e548adb40d6d/Libs/MRML/Core/vtkMRMLVolumeArchetypeStorageNode.cxx#L495">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/024b340baaa191968b6fc954b9f0e548adb40d6d/Libs/MRML/Core/vtkMRMLVolumeArchetypeStorageNode.cxx#L495" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/024b340baaa191968b6fc954b9f0e548adb40d6d/Libs/MRML/Core/vtkMRMLVolumeArchetypeStorageNode.cxx#L495" target="_blank" rel="noopener">Slicer/Slicer/blob/024b340baaa191968b6fc954b9f0e548adb40d6d/Libs/MRML/Core/vtkMRMLVolumeArchetypeStorageNode.cxx#L495</a></h4>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="485" style="counter-reset: li-counter 484 ;">
          <li>ici-&gt;SetOutputOrigin( 0, 0, 0 );</li>
          <li>ici-&gt;Update();</li>
          <li></li>
          <li>if (ici-&gt;GetOutput() == nullptr)</li>
          <li>{</li>
          <li>  vtkErrorToMessageCollectionMacro(this-&gt;GetUserMessages(), "vtkMRMLVolumeArchetypeStorageNode::ReadDataInternal",</li>
          <li>    "Cannot read file: " &lt;&lt; fullName);</li>
          <li>  return 0;</li>
          <li>}</li>
          <li></li>
          <li class="selected">vtkNew&lt;vtkImageData&gt; outputImage;</li>
          <li>outputImage-&gt;ShallowCopy(ici-&gt;GetOutput());</li>
          <li>volNode-&gt;SetAndObserveImageData(outputImage.GetPointer());</li>
          <li></li>
          <li>int voxelVectorType = ConvertVoxelVectorTypeVTKITKToMRML(reader-&gt;GetVoxelVectorType());</li>
          <li>volNode-&gt;SetVoxelVectorType(voxelVectorType);</li>
          <li></li>
          <li>// If voxel values store spatial vectors then we need to convert from LPS to RAS</li>
          <li>if (voxelVectorType == vtkMRMLVolumeNode::VoxelVectorTypeSpatial</li>
          <li>  &amp;&amp; outputImage-&gt;GetNumberOfScalarComponents() == 3)</li>
          <li>{</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @Thibault_Pelletier (2024-03-11 07:22 UTC)

<p>Thanks for the link! I’ll have a look!</p>

---
