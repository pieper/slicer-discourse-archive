---
topic_id: 35353
title: "How To Extract Both X Y Z Coordinates And Normalvector At Ea"
date: 2024-04-08
url: https://discourse.slicer.org/t/35353
---

# How to extract both x-, y-, z-coordinates and normalvector at each point of centerline of airwaysegmentation

**Topic ID**: 35353
**Date**: 2024-04-08
**URL**: https://discourse.slicer.org/t/how-to-extract-both-x-y-z-coordinates-and-normalvector-at-each-point-of-centerline-of-airwaysegmentation/35353

---

## Post #1 by @Johan_Rubak (2024-04-08 13:34 UTC)

<p>Hi. I want to extract a centerline of an airwaysegmentation. I have tried out different tools for this, among other SlicerVMTK extension, but always ending up in a situation with only the possibility of exporting x-, y-, z-coordinates but without corresponding normalvectors that indicate the actual curvature at each point.</p>
<p>It is possible to export the centerline with both the points and the corresponding normalvector at each point?</p>

---

## Post #2 by @lassoan (2024-04-08 13:53 UTC)

<p>Tangent, normal, and binormal vectors can be easily computed from curve points anywhere, anytime, using a coordinate system generator class, such as <code>vtkParallelTransportFrame</code>, so we don’t need to save these vectors.</p>
<p>You can conveniently access these vectors in the world coordinate system in Slicer’s Python console as numpy arrays:</p>
<pre data-code-wrap="python"><code class="lang-python">curveNode = getNode("OC")
curveNode.GetMeasurement("curvature mean").SetEnabled(True)
positions = slicer.util.arrayFromMarkupsCurvePoints(curveNode, True)
normals = slicer.util.arrayFromMarkupsCurveData(curveNode, "Normals", True)
curvatures = slicer.util.arrayFromMarkupsCurveData(curveNode, "Curvature", True)
</code></pre>
<p>If you prefer, you can access all these arrays as VTK polydata (to easily use in VTK filters or write to file):</p>
<pre data-code-wrap="python"><code class="lang-python">curveNode.GetCurveCoordinateSystemGeneratorWorld().Update()
curvePolyData = curveNode.GetCurveCoordinateSystemGeneratorWorld().GetOutput()
</code></pre>

---

## Post #3 by @Johan_Rubak (2024-04-08 19:05 UTC)

<p>Ahh thanks, that helped a lot, seems like the whole medical imaging industry can always rely on you lassoan <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #4 by @Johan_Rubak (2024-04-11 17:42 UTC)

<p>I got the normals exported and was just about using it for a program im developing, when i noticed that the normals is not exactly what i expected them to be. I want them to indicate the normal to the plane to each point facing towards the next point, instead they seem to indicate the normal from the side if that makes any sense. I have tried to extract the centerline in Simpleware SCANIP, where they indicate what i want them to, but i would rather use 3D slicer, since it is open-source! <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=12" title=":smile:" class="emoji" alt=":smile:" loading="lazy" width="20" height="20"> Here are some pictures (first 3d slicer, second scanip):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/72f7233b0874080652d0f3203e44bff3f67c3ed3.jpeg" data-download-href="/uploads/short-url/gp1V8oysfTmZFqi3BYTFS0ZLzov.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/72f7233b0874080652d0f3203e44bff3f67c3ed3_2_690x375.jpeg" alt="image" data-base62-sha1="gp1V8oysfTmZFqi3BYTFS0ZLzov" width="690" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/72f7233b0874080652d0f3203e44bff3f67c3ed3_2_690x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/72f7233b0874080652d0f3203e44bff3f67c3ed3_2_1035x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/72f7233b0874080652d0f3203e44bff3f67c3ed3_2_1380x750.jpeg 2x" data-dominant-color="EDEDED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1786×973 267 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Do you think there is any way i can calculate and export them in way so they indicate what i want them to?</p>

---

## Post #5 by @Johan_Rubak (2024-04-11 19:38 UTC)

<p>Okay figured out myself that extracting the tangents would achieve what i wanted. Now I have a new problem… <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>When using the “Extract Centerline” module, i set the curve sampling distance to 0.1269mm (Image 1), this gives 517 controlpoints spread along the centerline (Image 2).  But when I want to save the positions and corresponding tangents (using the commands you showed me) to a csv file, I end up with way more points, 5375 points (Image 3).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/adad12ef04978777734aa1f46cea05b70fed2422.jpeg" data-download-href="/uploads/short-url/oMppwkofq6lXagxeHgeUSXIjCWS.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/adad12ef04978777734aa1f46cea05b70fed2422_2_690x332.jpeg" alt="image" data-base62-sha1="oMppwkofq6lXagxeHgeUSXIjCWS" width="690" height="332" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/adad12ef04978777734aa1f46cea05b70fed2422_2_690x332.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/adad12ef04978777734aa1f46cea05b70fed2422_2_1035x498.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/adad12ef04978777734aa1f46cea05b70fed2422_2_1380x664.jpeg 2x" data-dominant-color="F1F1F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1781×859 151 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I want to extract points with the specific distance 0.1269mm and then the corresponding tangents. Is there a way to access the tangents at each controlpoint instead?</p>

---

## Post #6 by @Johan_Rubak (2024-04-11 21:02 UTC)

<p>So far I have made a way to calculate the tangents between each controlpoint, but do think there is a way this should be done more precise or is it as good as it gets?</p>

---

## Post #7 by @mssm (2024-08-16 01:37 UTC)

<p>Hi, Johan.</p>
<p>Your thread is also very interesting.</p>
<p>I might have the answer for the “many points (5375 points)”.</p>
<p>The Slicer program seems to interpolate the curve when calculating measurements such as tangents, normals, binormals, curvatures, etc. It seems to create nine points between each control point.</p>
<p>So, if the number of control points is N, the total number of measurement points is 10(N-1)+1 = 10N-9.</p>
<p>By the way, I am very interested in the visualization of normal vectors posted on April 12th. Actually, you needed the figure on the right, but I would like the one on the left.</p>
<p>Could you tell me how to draw normal vectors at each control point in 3D slicer with a Python script?</p>
<p>I appreciate any help you can provide.</p>
<p>Masa Shojima, Japan.</p>

---

## Post #8 by @lassoan (2024-08-19 13:21 UTC)

<aside class="quote no-group" data-username="mssm" data-post="7" data-topic="35353">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mssm/48/76622_2.png" class="avatar"> mssm:</div>
<blockquote>
<p>So, if the number of control points is N, the total number of measurement points is 10(N-1)+1 = 10N-9.</p>
</blockquote>
</aside>
<p>If your curve already have many points very close to each other then you can <a href="https://apidocs.slicer.org/master/classvtkMRMLMarkupsCurveNode.html#ab7e78f2538dae5ea876ae7d0963e376c">set the number of points per interpolating segment</a> to 0.</p>
<aside class="quote no-group" data-username="mssm" data-post="7" data-topic="35353">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mssm/48/76622_2.png" class="avatar"> mssm:</div>
<blockquote>
<p>By the way, I am very interested in the visualization of normal vectors</p>
</blockquote>
</aside>
<p>This question was also posted and was answered here:</p>
<aside class="quote quote-modified" data-post="5" data-topic="37933">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mssm/48/76622_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-can-i-draw-normal-vectors-of-a-centerline-in-the-3d-slicer/37933/5">How can I draw normal vectors of a centerline in the 3D slicer?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Dear Andras Lasso sensei, 
Thanks a lot. 
I tried the magic code right away. However, I got the error message as shown in the attached image. 
Could you please help me again? 
I also looked into “addCoordinateSystemUpdator”. For some reason, I couldn’t use it in my environment. 
MacStudio, M2, MacOS Sonoma 14.6.1 
Slicer 5.6.2 r32448 / f10cd8c 
Regards, 
Masaaki 
By the way, when application is starting, such messages appears in the python console: 
Python 3.9.10 (main, Apr  5 2024, 00:33:09) 
[…
  </blockquote>
</aside>


---

## Post #9 by @Johan_Rubak (2024-08-19 18:56 UTC)

<p>Thankyou for the respons!</p>
<p>For the normalvectors I ended up using this script to just calculate the normals i needed from point to point manually. Ignore the variable referencepoints that is for something specific in my case. This creates a csv. file with the points and normals.</p>
<pre><code class="lang-auto">import slicer
import csv
import qt
import numpy as np

refpoints_name = qt.QInputDialog.getText(None, "String Input", "Enter name of referencepoints:")
centerline_name = qt.QInputDialog.getText(None, "String Input", "Enter name of centerline:")

curveNode = slicer.util.getNode(centerline_name)
curveNode.GetMeasurement("curvature mean").SetEnabled(True)
#normals = slicer.util.arrayFromMarkupsCurveData(curveNode, "Tangents", True)
#positions = slicer.util.arrayFromMarkupsCurvePoints(curveNode, True)

positions = slicer.util.arrayFromMarkupsControlPoints(curveNode)
normals = []
for i in range(len(positions)-1):
    normal = positions[i+1] - positions[i]
    normal = normal / np.linalg.norm(normal)
    normals.append(normal)

ref_points = slicer.util.getNode(refpoints_name)
ref_points_only = slicer.util.arrayFromMarkupsControlPoints(ref_points)

directory_dialog = qt.QFileDialog()
directory_dialog.setFileMode(qt.QFileDialog.Directory)
directory_dialog.setWindowTitle("Select folder to save the csv file")

directory_dialog.exec_()
selected_directory = directory_dialog.selectedFiles()[0]
print("Selected directory:", selected_directory)

file_name = qt.QInputDialog.getText(None, "File Name Input", "Enter a file name:")
file_path = selected_directory + "/" + file_name + ".csv"
print("Selected file path:", file_path)

with open(file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['X', 'Y', 'Z'])

    for pos in ref_points_only:
        writer.writerow([pos[0], pos[1], pos[2]])
    
    writer.writerow(['X', 'Y', 'Z', 'Normal_X', 'Normal_Y', 'Normal_Z'])
    for i in range(len(positions)-1):
        writer.writerow([positions[i][0], positions[i][1], positions[i][2], normals[i][0], normals[i][1], normals[i][2]])

print("Data saved to:", file_path)
</code></pre>
<p>For the plotting i was using matplotlib, but have also good succes with open3d, but it is not applicable with newer versions of python.</p>
<pre><code class="lang-auto"> import matplotlib.pyplot as plt

        # Create a 3D figure
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Plot the centerline points
        ax.scatter(centerline_points[:, 0], centerline_points[:, 1], centerline_points[:, 2])
        # Plot the normal vectors
        ax.quiver(centerline_points[:, 0], centerline_points[:, 1], centerline_points[:, 2],
                  centerline_points[:, 3], centerline_points[:, 4], centerline_points[:, 5],
                  length=0.1, normalize=True, color='r')

        ax.set_box_aspect([np.ptp(centerline_points[:, 0]), np.ptp(centerline_points[:, 1]), np.ptp(centerline_points[:, 2])])

        # Set labels for the axes
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        # Show the plot
        plt.show()
</code></pre>

---

## Post #10 by @mssm (2024-08-19 22:57 UTC)

<p>How kind you are!<br>
Thanks a lot.</p>

---

## Post #11 by @lassoan (2024-08-24 07:44 UTC)

<aside class="quote no-group" data-username="Johan_Rubak" data-post="9" data-topic="35353">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/johan_rubak/48/69951_2.png" class="avatar"> Johan_Rubak:</div>
<blockquote>
<p>For the plotting i was using matplotlib, but have also good succes with open3d, but it is not applicable with newer versions of python.</p>
</blockquote>
</aside>
<p>You can get really good, interactive plots right in Slicer’s 3D viewer, by simple Python scripting. For example, you can plot the tangent, normal, and binormal for each curve control point with a <a href="https://discourse.slicer.org/t/how-can-i-draw-normal-vectors-of-a-centerline-in-the-3d-slicer/37933/4">short Python script</a>:</p>
<p><a href="https://discourse.slicer.org/t/how-can-i-draw-normal-vectors-of-a-centerline-in-the-3d-slicer/37933/4"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/3794275dd32e10a919d845740a17950db4e1ce8c.jpeg" alt="image" data-base62-sha1="7VFG5AOZmu8Cr5XQty7smHSpT88" width="690" height="388"></a></p>

---
