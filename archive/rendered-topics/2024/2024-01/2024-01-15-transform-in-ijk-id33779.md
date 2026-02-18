# Transform in ijk

**Topic ID**: 33779
**Date**: 2024-01-15
**URL**: https://discourse.slicer.org/t/transform-in-ijk/33779

---

## Post #1 by @brandus1 (2024-01-15 11:53 UTC)

<p>Hi,</p>
<p>I am trying to replicate the behavior of the Resample module directly on numpy arrays, because I have a separate service that cannot integrate or call slicer directly unfortunately.</p>
<p>This is the basic operation I would like to replicate:</p>
<pre><code class="lang-auto">     vol2 = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode", vol.GetName() + "_resampled")
      params = {
        "inputVolume": vol.GetID(),
        "outputVolume": vol2.GetID(),
        "interpolationType": "nn", #nearest neighbor
        "transformationFile": tr.GetID(),
        "inverseITKTransformation": False,
        "referenceVolume": ct.GetID(),
      }
      resample = slicer.cli.run(slicer.modules.resamplescalarvectordwivolume, parameters=params, wait_for_completion=True)
      if resample.GetStatusString() != "Completed":
        raise Exception("Resample failed")
</code></pre>
<p>I am trying to basically get the equivalent of the tranform 4x4 matrix but to be applied on the underlying array (ijk or jki). I am definetely doing something wrong.</p>
<p>This is how i thought it would work:</p>
<pre><code class="lang-auto">      tr_np = slicer.util.arrayFromVTKMatrix(tr.GetMatrixTransformToParent())
      # apply rasToIjk transform to the transform
      ras_to_ijk = vtk.vtkMatrix4x4()
      vol.GetRASToIJKMatrix(ras_to_ijk)
      ras_to_ijk_np = slicer.util.arrayFromVTKMatrix(ras_to_ijk)
      tr_np = np.matmul(tr_np, ras_to_ijk_np)
</code></pre>
<p>The results are totally off though, so I think I am missing something critical.</p>
<p>the general question is: how do you transform a transformMatrix to the ijk or kji coordinate system?</p>

---

## Post #3 by @mikebind (2024-01-15 19:56 UTC)

<p>You might find this example from the script repository informative: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-volume-voxel-coordinates-from-markup-control-point-ras-coordinates" rel="noopener nofollow ugc">Script repository: get-volume-voxel-coordinates-from-markup-control-point-ras-coordinates</a></p>
<p>Note that, as long as you are dealing only with linear transformations, it is generally not going to be necessary to actually resample the array of voxel values.  The location and scale of the voxel array is specified by header metadata, so updating that is likely going to be enough for you. In Slicer, “hardening” a linear transform does not change the voxel array, only the metadata expressing where that array should be displayed in space.</p>

---
