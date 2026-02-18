# Calculating the volume encompassed by a given isodose

**Topic ID**: 42712
**Date**: 2025-04-28
**URL**: https://discourse.slicer.org/t/calculating-the-volume-encompassed-by-a-given-isodose/42712

---

## Post #1 by @azam (2025-04-28 10:23 UTC)

<p>Hi everyone<br>
I exported DICOM RT Dose from the treatment planning system and I want to calculate the volume encompassed by each isodose (for example, isodose 20 Gy). I used the isodose module for this purpose, But I don’t know how to calculate the value of this volume. Can you  guide me?</p>
<p>Thanks a lot</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/48ff606e5b7bdb297a9046ea130138b994afc4bf.png" data-download-href="/uploads/short-url/apLwetlWmLLbkq7iCWXcPCuThuf.png?dl=1" title="isodose" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/48ff606e5b7bdb297a9046ea130138b994afc4bf_2_517x199.png" alt="isodose" data-base62-sha1="apLwetlWmLLbkq7iCWXcPCuThuf" width="517" height="199" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/48ff606e5b7bdb297a9046ea130138b994afc4bf_2_517x199.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/48ff606e5b7bdb297a9046ea130138b994afc4bf_2_775x298.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/48ff606e5b7bdb297a9046ea130138b994afc4bf_2_1034x398.png 2x" data-dominant-color="4EDB15"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">isodose</span><span class="informations">1396×540 99.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @cpinter (2025-04-28 10:58 UTC)

<p>You can see the volume of closed surfaces in the Models module, however, in the latest version of the Isodose module, all the isodose surfaces are stored in the same model node (the isodose levels are identified by scalar values in the point data), so you’ll see the volume of the smallest dose (i.e. the largest region). You’ll need to separate the isodose level surfaces into different model nodes to see the surfaces of each.</p>
<p>It would be very useful if we could do either of these easily in Slicer</p>
<ol>
<li>Split such a model node by scalar value</li>
<li>Import such a model node into a segmentation node, each scalar value into a different segment</li>
</ol>
<p>Unfortunately, as far as I know, neither of these exist at the moment. What you can do is separate them with a little Python scripting.</p>
<p>I created a little sample snippet for you to start from.</p>
<pre><code class="lang-auto">import vtk

# Get your vtkPolyData
m = slicer.util.getNode('5: RTDOSE_IsodoseLevels')
polyData = m.GetPolyData()

# Create a vtkThreshold filter
threshold = vtk.vtkThreshold()
threshold.SetInputData(polyData)

# Define the scalar range for the first surface
threshold.ThresholdBetween(lower_value, upper_value)
threshold.Update()

# Extract the thresholded data
m0 = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLModelNode')
m0.SetAndObservePolyData(threshold.GetOutput())
m0.SetName('IsodoseLevel_X')

# Repeat for other scalar ranges
# ...
</code></pre>

---
