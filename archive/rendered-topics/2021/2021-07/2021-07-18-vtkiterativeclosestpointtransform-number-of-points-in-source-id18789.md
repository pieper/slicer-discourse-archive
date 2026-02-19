---
topic_id: 18789
title: "Vtkiterativeclosestpointtransform Number Of Points In Source"
date: 2021-07-18
url: https://discourse.slicer.org/t/18789
---

# vtkIterativeClosestPointTransform - number of points in source and target

**Topic ID**: 18789
**Date**: 2021-07-18
**URL**: https://discourse.slicer.org/t/vtkiterativeclosestpointtransform-number-of-points-in-source-and-target/18789

---

## Post #1 by @Greydon_Gilmore (2021-07-18 18:57 UTC)

<p>Hi,</p>
<p>I am using <code>vtkIterativeClosestPointTransform</code> in a pipeline that detects radiopaque stereotactic frame fiducials in a CT/MRI. The geometry of the stereotactic frame is know. For a single CT volume there could be ~700-800 markups points, which forms the stereotactic frame localizers. The image below shows all the points that ae found within a CT volume.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fab0c84acad70725d758e2b7901a637ba014335c.jpeg" data-download-href="/uploads/short-url/zLI7zv4sgpuGdgNffnKR29qWvtG.jpeg?dl=1" title="leksell_mean_clusters" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fab0c84acad70725d758e2b7901a637ba014335c_2_594x500.jpeg" alt="leksell_mean_clusters" data-base62-sha1="zLI7zv4sgpuGdgNffnKR29qWvtG" width="594" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fab0c84acad70725d758e2b7901a637ba014335c_2_594x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fab0c84acad70725d758e2b7901a637ba014335c_2_891x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fab0c84acad70725d758e2b7901a637ba014335c_2_1188x1000.jpeg 2x" data-dominant-color="F7F7F7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">leksell_mean_clusters</span><span class="informations">1536×1291 147 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>When running the ICP registration I convert all the CT markups points to polydata and generate an equal number of points for the frame. The top and bottom of each localizer bar have known coordinates and the bars have a known length (points on the same line in the image above).</p>
<p>My question: Do the source and target point clouds need have the same number of points? Realistically, I could have many more points in the target point cloud as it is generate in real-time based on the frame geometry. I have tried setting both point clouds to the same size as well as setting the target to have 4x as many points. I notice a substantial reduction in RMS error when the target cloud had 4x more points.</p>
<p>Is super-sampling the target point cloud frowned upon? I know it can be an issue if the target cloud has fewer points than the source but I couldn’t find anything about the target having many more points.</p>
<p>Thank you!</p>

---

## Post #2 by @lassoan (2021-07-18 23:04 UTC)

<p>ICP do not require matching number of fixed and moving points. In fact, it registers a point cloud with a surface (I think line cells work, too). So, it should not be necessary to represent the template with many points, you just need to make sure that you have lines in the template’s polygonal mesh, not just points.</p>
<p>However, you probably don’t need to implement Z-frame registration from scratch. Slicer has an extension for automated Z-frame detection, subpixel-accuracy intersection point position estimattion, and optimal fitting: <a href="https://github.com/SlicerProstate/SlicerZFrameRegistration" class="inline-onebox">GitHub - SlicerProstate/SlicerZFrameRegistration: This extension can be used for the registration between intra-procedural image frame of reference with the transperineal biopsy or cryoablation templates</a> You may need to tune it a bit for your images and the geometry of your frame.</p>
<p>If this extension is not flexible enough to specify different Z-frame geometries then it could be updated to use the general linear registration method developed by <a class="mention" href="/u/mholden8">@mholden8</a>. It can register any pattern made up of points, lines, and planes and guarantees to find the optimal match with a non-iterative method. As far as I remember, it is already available in one of the IGT extensions in Slicer.</p>

---

## Post #3 by @Greydon_Gilmore (2021-07-18 23:50 UTC)

<p>This was the exact solution. I modified the code to use <code>vtkLine</code> instead and it performs much better now. I just passed the <code>vtkPolyData</code> object to the ICP transform instead.</p>
<pre><code class="lang-auto">tubePolyData = vtk.vtkPolyData()
tubePolyData.SetPoints(framePoints)
tubePolyData.SetLines(frameLines)

icpTransform = vtk.vtkIterativeClosestPointTransform()
icpTransform.SetSource(sourceModel.GetPolyData())
icpTransform.SetTarget(tubePolyData)
...
icpTransform.Modified()
icpTransform.Update()

transform_matrix = vtk.vtkMatrix4x4()
transform_matrix.DeepCopy(icpTransform.GetMatrix())
</code></pre>
<p>Thank you for the quick response. I tried playing around with the ZFrameRegistration module but the stereotactic frames I am using are quite different. I have my own module I will be contributing for human stereotactic frame detection very soon.</p>

---

## Post #4 by @Greydon_Gilmore (2021-07-30 23:48 UTC)

<p>I have a follow-up question after performing the registration for multiple patients. Following the registration, I am computing the registration error and storing the euclidean distance in a list object:</p>
<pre><code class="lang-auto">cellId = vtk.mutable(0)
subId = vtk.mutable(0)
dist2 = vtk.mutable(0.0)
cellLocator = vtk.vtkCellLocator()
cellLocator.SetDataSet(inputTargetModel.GetPolyData())
cellLocator.SetNumberOfCellsPerBucket(1)
cellLocator.BuildLocator()
        
totalDistance = 0.0
accumPoints = []

sourcePoints = inputSourceModel.GetPoints()
for sourcePointIndex in range(sourcePoints.GetNumberOfPoints()):
    sourcePointPos = [0]*3
    sourcePoints.GetPoint(sourcePointIndex, sourcePointPos)
    tSourcePointPos = [0]*4
    sourcePointPos = sourcePointPos+[1]
    icpTransform.MultiplyPoint(sourcePointPos, tSourcePointPos)
    surfacePoint = [0]*3
    transformedSourcePointPos = tSourcePointPos[:3]
    cellLocator.FindClosestPoint(tSourcePointPos, surfacePoint, cellId, subId, dist2)
    totalDistance = totalDistance + math.sqrt(dist2)
    accumPoints.append(np.array(transformedSourcePointPos)-np.array(surfacePoint))
</code></pre>
<p>When I then examine the euclidean distance error for all the fiducials I found that only the fiducials that produce an oblique artifact in the CT volume have error in the z-axis (fiducial 2,5,8). If you look at the previous picture I posted, the diagonal bars in the N would be the bars producing the oblique artifact. The vertical bars that run dorsal to ventral have an error of 0 in the z-axis:</p>
<div class="md-table">
<table>
<thead>
<tr>
<th style="text-align:center">Fiducial</th>
<th style="text-align:center">X coordinate</th>
<th style="text-align:center">Y coordinate</th>
<th style="text-align:center">Z coordinate</th>
<th style="text-align:center">Root mean square error</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center">1</td>
<td style="text-align:center">-0.094 (0.209)</td>
<td style="text-align:center">0.144 (0.067)</td>
<td style="text-align:center">0.000 (0.000)</td>
<td style="text-align:center">0.253</td>
</tr>
<tr>
<td style="text-align:center">2</td>
<td style="text-align:center">0.034 (0.133)</td>
<td style="text-align:center">-0.027 (0.069)</td>
<td style="text-align:center">-0.027 (0.069)</td>
<td style="text-align:center">0.203</td>
</tr>
<tr>
<td style="text-align:center">3</td>
<td style="text-align:center">-0.041 (0.083)</td>
<td style="text-align:center">0.108 (0.065)</td>
<td style="text-align:center">0.000 (0.000)</td>
<td style="text-align:center">0.184</td>
</tr>
<tr>
<td style="text-align:center">4</td>
<td style="text-align:center">-0.006 (0.069)</td>
<td style="text-align:center">-0.085 (0.090)</td>
<td style="text-align:center">0.000 (0.000)</td>
<td style="text-align:center">0.181</td>
</tr>
<tr>
<td style="text-align:center">5</td>
<td style="text-align:center">-0.074 (0.070)</td>
<td style="text-align:center">-0.224 (0.066)</td>
<td style="text-align:center">0.074 (0.070)</td>
<td style="text-align:center">0.296</td>
</tr>
<tr>
<td style="text-align:center">6</td>
<td style="text-align:center">-0.023 (0.063)</td>
<td style="text-align:center">-0.133 (0.075)</td>
<td style="text-align:center">0.000 (0.000)</td>
<td style="text-align:center">0.192</td>
</tr>
<tr>
<td style="text-align:center">7</td>
<td style="text-align:center">0.139 (0.076)</td>
<td style="text-align:center">0.096 (0.059)</td>
<td style="text-align:center">0.000 (0.000)</td>
<td style="text-align:center">0.215</td>
</tr>
<tr>
<td style="text-align:center">8</td>
<td style="text-align:center">0.029 (0.134)</td>
<td style="text-align:center">-0.044 (0.068)</td>
<td style="text-align:center">-0.044 (0.068)</td>
<td style="text-align:center">0.193</td>
</tr>
<tr>
<td style="text-align:center">9</td>
<td style="text-align:center">0.030 (0.202)</td>
<td style="text-align:center">0.167 (0.077)</td>
<td style="text-align:center">0.000 (0.000)</td>
<td style="text-align:center">0.267</td>
</tr>
</tbody>
</table>
</div><p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8e41900e14f27fb6a55a1bd09e3466f2d159cef6.jpeg" data-download-href="/uploads/short-url/kisgDeRjY5Zgs9hmJvkxq8Ml4ay.jpeg?dl=1" title="axial_frame" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8e41900e14f27fb6a55a1bd09e3466f2d159cef6_2_485x500.jpeg" alt="axial_frame" data-base62-sha1="kisgDeRjY5Zgs9hmJvkxq8Ml4ay" width="485" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8e41900e14f27fb6a55a1bd09e3466f2d159cef6_2_485x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8e41900e14f27fb6a55a1bd09e3466f2d159cef6_2_727x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8e41900e14f27fb6a55a1bd09e3466f2d159cef6_2_970x1000.jpeg 2x" data-dominant-color="373434"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">axial_frame</span><span class="informations">1920×1976 80.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Could this have something to do with the partial volume effect of CT? or have I done something incorrect during ICP registration error calculation?</p>
<p>Thank you in advance,<br>
Greydon</p>

---

## Post #5 by @lassoan (2021-08-01 23:04 UTC)

<p>Initializing mutable arrays using <code>*</code> operator is a bad practice because it does not create independent copies (it does not cause a problem for simple values, but causes very hard to detect errors when applied to arrays). Also, <code>[0]*3</code> creates an integer array, so computation results will have quantization errors (rounded to integer values). Where did you see such initialization of point position vectors?</p>
<p>A safer and simpler syntax is <code>np.zeros(3)</code>. You could use <code>[0.0, 0.0, 0.0]</code>, too, but it is more verbose and does not allow you to perform numpy operations on the array directly (you need to convert to numpy array first).</p>

---

## Post #6 by @Greydon_Gilmore (2021-08-10 03:37 UTC)

<p>I apologize, I wrote <code>[0]*3</code> in my previous post but meant <code>[0.]*3</code>. However, I replaced this method of initialization with np.zeros(3). Thank you for this suggestion.</p>
<pre><code class="lang-auto">for sourcePointIndex in range(sourcePoints.GetNumberOfPoints()):
    sourcePointPos = np.zeros(3)
    sourcePoints.GetPoint(sourcePointIndex, sourcePointPos)
    tSourcePointPos = np.append(np.zeros(3),1)
    icpTransform.MultiplyPoint(np.append(sourcePointPos,1), tSourcePointPos)
    surfacePoint = np.zeros(3)
    cellLocator.FindClosestPoint(tSourcePointPos[:3], surfacePoint, cellId, subId, dist2)
    totalDistance = totalDistance + math.sqrt(dist2)
    accumPoints.append(tSourcePointPos[:3]-surfacePoint)
</code></pre>
<p>After re-running, the error did not change. I obtained the same registrations errors as reported in the table above. I am trying to rationalize the registration error.</p>
<p>The stereotactic frame is placed into a holder that is attached to the CT table. Assuming the gantry tilt is zero, the vertical fiducial bars would run parallel to the acquisition plane and the position of the artifact they produce would remain relatively consistent across CT slices. However, the position of the artifact produced by the diagonal fiducial bars would change between adjacent CT slices. Am I correct in concluding that the z-axis registration error is the result of the change in position of the diagonal bar artifact?</p>

---
