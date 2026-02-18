# Signed vs. PointToPointVector for (model2model) distance output

**Topic ID**: 15647
**Date**: 2021-01-25
**URL**: https://discourse.slicer.org/t/signed-vs-pointtopointvector-for-model2model-distance-output/15647

---

## Post #1 by @sfglio (2021-01-25 08:55 UTC)

<p>I created a VTK output file from two segmented sinus (segmentation of the sinus derived from two ct scans at different time points).<br>
Now I would like to know whether there has been any reduction/expansion of the sinus volume but I focus on the anatomical region, i.e. where exactly has been any change.<br>
Attached is the VTK Output of the sinus.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/04bab79c3d503bafb13da06942a144d6dcdd5679.png" data-download-href="/uploads/short-url/FPWSDt1dGTce9L3YdLyjRQrffj.png?dl=1" title="Screenshot_sinus" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/04bab79c3d503bafb13da06942a144d6dcdd5679_2_688x500.png" alt="Screenshot_sinus" data-base62-sha1="FPWSDt1dGTce9L3YdLyjRQrffj" width="688" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/04bab79c3d503bafb13da06942a144d6dcdd5679_2_688x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/04bab79c3d503bafb13da06942a144d6dcdd5679_2_1032x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/04bab79c3d503bafb13da06942a144d6dcdd5679_2_1376x1000.png 2x" data-dominant-color="9A97CB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_sinus</span><span class="informations">1394×1012 63.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
However when exporting the distances between the meshes I can choose between “signed” and “PointToPointVector” (from the scalar of the vtk) resulting in different values of mm.<br>
I would like to assess where exactly has been the highest distance between the two models.<br>
I could try to visually detect it on a distance map but I prefer to stick to the output of the distances.</p>
<p>If I ignore the direction and just would like to know the max. distance then probably “signed” is fine.<br>
If I would like to assess the max. vertical (sup-inferior) expansion of the sinus would the PointToPointVector (y-Axis) be sufficient to tell???<br>
I am asking because the values are different in regard to max. distance (of mm?).<br>
In this example: y-axis (second column): max 1.65 (mm?)<br>
signed: max. 0.51 (mm?)<br>
In return, if I would like to tell the max. lateral expansion of the sinus is the x-axis (pointtopointvector) appropiate?</p>
<p>Another example would be the comparison of dental models (as seen here: <img src="https://i.stack.imgur.com/f8u3t.png" alt="" role="presentation" width="" height=""><br>
Different software but obviously the “signed” distance is depicted and referred to as cloud-to-mesh (c2m) distance.<br>
Again: if I would like to assess whether there is a difference in the vertical height (e.g. after filling treatment) between two dental models is “signed” or “Pointtopointvector” more suitable?<br>
I am wondering whether this has been paid attention to while measuring distances between meshes…</p>

---

## Post #2 by @nrex45 (2021-01-28 02:24 UTC)

<p>I don’t have a great answer to your question, but you might start by trying to look at the raw data from the output files to understand some of the differences between the two models.</p>
<p>I’d recommend executing the model2model distance and then running something similar to the following code to export the models as CSVs to help answer your questions:</p>
<pre><code>outputNode = findModelToModelDistance(modelNode1,modelNode2)
VTKFieldData = outputNode.GetMesh().GetAttributesAsFieldData(0)
resultTableNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLTableNode","surface_distances")

for j in range(0,VTKFieldData.GetNumberOfArrays()):
    resultTableNode.AddColumn(VTKFieldData.GetArray(j))
</code></pre>
<p>I hope this is somewhat helpful in answering your question.</p>

---

## Post #3 by @lassoan (2021-01-28 03:35 UTC)

<p>You can also get all the computed distances as a numpy array (<code>slicer.util.arrayFromModelPointData</code>) and from that you can compute any statistics, minimum/maximum, projections on any axes, etc. using standard numpy functions.</p>

---
