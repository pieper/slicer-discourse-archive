---
topic_id: 36245
title: "How To Computer Normals From A Model"
date: 2024-05-18
url: https://discourse.slicer.org/t/36245
---

# How to computer normals from a Model

**Topic ID**: 36245
**Date**: 2024-05-18
**URL**: https://discourse.slicer.org/t/how-to-computer-normals-from-a-model/36245

---

## Post #1 by @LukaBloomRox (2024-05-18 03:15 UTC)

<p>Hi, everybody.</p>
<p>I am a software engineer who also designs tracheostomy tubes for my medical advocacy clients (Paraclete Advocacy, Ontario, Canada) and have found Slicer extremely helpful, both to create new tube designs (with the help of SolidWorks and Blender) and also to do virtual insertions of trach tube models into DICOM data from CAT scans and to measure scanned tubes.</p>
<p>I’ve been trying to “up my game” by going less by “look and feel” and becoming more precise and repeatable by automating portions of my workflow.  One such example is producing normal vectors at the proximal and distal centerlines of candidate trach tube designs.</p>
<p>Surprise surprise, ChatGPT got it right this time.  This snippet of code allowed me to take a point set csv from a trach tube manufacturer representing the centerline of a manufactured tube, and via the CurveMaker extension, allow me to wrap the centerline with a curvy cylinder and then save it as a model.</p>
<p>The following script allowed me to create a complete set of normals for every point in the model (I only really needed normals form the top/bottom faces but this worked as well).  The normals came in as a separate object that I could display/hide at will from my data view.  I was able to quickly measure the proposed tube shape and compare it against the design that I had created that ultimately caused the manufacturer to generate the shape.</p>
<p>For the first time ever using the Python Interactor, I have to say it was a wonderful experience with a little help from ChatGPT.    I have industry experience with Python development but since this work is not billable, I hadn’t delved too far into slicer Python handshaking.   This was a really nice working introduction that I wanted to share, since it helped me serve a client with more accuracy than in the past.</p>
<p>Medical GPT<br>
To visualize surface normals as lines on a model in 3D Slicer, you can use Python scripting within Slicer to programmatically create line representations of the normals and then add these to the 3D display. Here is a step-by-step guide on how to accomplish this:</p>
<p>Step 1: Prepare Your Model<br>
Ensure your model is loaded in 3D Slicer. You’ll need to work with this model’s mesh data.</p>
<p>Step 2: Open Python Interactor<br>
Open the Python Interactor in 3D Slicer, which can be accessed from the menu or by pressing Ctrl+3.</p>
<p>Step 3: Script to Create Lines for Normals<br>
The following Python script will:</p>
<p>Compute the normals for the mesh.<br>
Create lines for each normal.<br>
Display these lines in the 3D view.<br>
python<br>
Copy code</p>
<pre><code class="lang-auto"># Replace 'ModelName' with the name of your model in the scene
modelNode = slicer.util.getNode('ModelName')
polyData = modelNode.GetPolyData()

# Ensure normals are computed
polyData.BuildNormals()

# Access the normals
normals = polyData.GetPointData().GetNormals()

# Create a new model for the normals display
linesNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLModelNode", "NormalsVisualization")
linePolyData = vtk.vtkPolyData()
linesNode.SetAndObservePolyData(linePolyData)

# Prepare to create lines
points = vtk.vtkPoints()
lines = vtk.vtkCellArray()
linePolyData.SetPoints(points)
linePolyData.SetLines(lines)

# Scaling factor for normal vectors visualization
scaleFactor = 10.0

# Create lines representing normals
for i in range(normals.GetNumberOfTuples()):
    x, y, z = polyData.GetPoint(i)
    nx, ny, nz = normals.GetTuple(i)
    
    # Start point of the line
    start = [x, y, z]
    # End point of the line (extending the normal by scaleFactor)
    end = [x + nx * scaleFactor, y + ny * scaleFactor, z + nz * scaleFactor]
    
    idxStart = points.InsertNextPoint(start)
    idxEnd = points.InsertNextPoint(end)
    
    line = vtk.vtkLine()
    line.GetPointIds().SetId(0, idxStart)
    line.GetPointIds().SetId(1, idxEnd)
    lines.InsertNextCell(line)

# Update model display properties
modelDisplay = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLModelDisplayNode")
modelDisplay.SetColor(1, 0, 0)  # Red color
modelDisplay.SetLineWidth(2)    # Line width
linesNode.SetAndObserveDisplayNodeID(modelDisplay.GetID())

# Refresh to show lines
linesNode.CreateDefaultDisplayNodes()
linePolyData.Modified()
</code></pre>
<p>Step 4: Adjust Parameters<br>
Scaling Factor: Adjust scaleFactor to make the normal lines longer or shorter as needed to better visualize them against the model.<br>
Color and Line Width: Set the color and line width to make the normal lines clearly visible.<br>
Step 5: Run the Script<br>
Paste and run this script in the Python Interactor. The normals will be visualized as red lines extending from the surface of your model in the 3D view.</p>
<p>Conclusion<br>
This script creates a separate model node to hold the visualization of the normals, allowing you to easily toggle their visibility or remove them without affecting the original model. You can customize this further as needed for specific visualization requirements or to include in a custom Slicer module for more interactive use.</p>
<p>ChatGPT can make mistakes. Check important info.<br>
?<br>
ChatGPT</p>

---

## Post #2 by @lassoan (2024-05-18 03:18 UTC)

<p>This all sounds great, thanks for sharing. It would awesome if you could also post some screenshots or photos of your results.</p>

---

## Post #3 by @LukaBloomRox (2024-05-18 06:13 UTC)

<p>By request, I’m uploading some visuals.</p>
<p>Here are two visuals with normals (in red color) visible (end and side views)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a4f38b5400f9fd1cc19e69ed21d0a9d83a5c4d27.png" data-download-href="/uploads/short-url/nxe5YbVKHh71xl6CAA7LxNov9IP.png?dl=1" title="NormalsSeenFromEndOfTube" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/4/a4f38b5400f9fd1cc19e69ed21d0a9d83a5c4d27_2_690x322.png" alt="NormalsSeenFromEndOfTube" data-base62-sha1="nxe5YbVKHh71xl6CAA7LxNov9IP" width="690" height="322" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/4/a4f38b5400f9fd1cc19e69ed21d0a9d83a5c4d27_2_690x322.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/4/a4f38b5400f9fd1cc19e69ed21d0a9d83a5c4d27_2_1035x483.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/4/a4f38b5400f9fd1cc19e69ed21d0a9d83a5c4d27_2_1380x644.png 2x" data-dominant-color="B4729B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">NormalsSeenFromEndOfTube</span><span class="informations">1920×898 102 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e5d0125ec8aaf5c45e6c0e7a1d3faf1d7b10568.jpeg" data-download-href="/uploads/short-url/fKjMxCn61EhPlxt5zDw0MxPB9dS.jpeg?dl=1" title="NormalsSeenFromSideOfTube" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e5d0125ec8aaf5c45e6c0e7a1d3faf1d7b10568_2_690x322.jpeg" alt="NormalsSeenFromSideOfTube" data-base62-sha1="fKjMxCn61EhPlxt5zDw0MxPB9dS" width="690" height="322" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e5d0125ec8aaf5c45e6c0e7a1d3faf1d7b10568_2_690x322.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e5d0125ec8aaf5c45e6c0e7a1d3faf1d7b10568_2_1035x483.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e5d0125ec8aaf5c45e6c0e7a1d3faf1d7b10568_2_1380x644.jpeg 2x" data-dominant-color="AC79A5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">NormalsSeenFromSideOfTube</span><span class="informations">1920×898 162 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @LukaBloomRox (2024-05-18 06:14 UTC)

<p>Here are another two visuals with my measurements (with alignment of markups confirmed not only by eye but also by normals, top and side views).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89f0e8ffdb475bacabb510497d76f181a0612aad.png" data-download-href="/uploads/short-url/jGhyMM9HuAZPy3i0MLcKe3xsTTL.png?dl=1" title="TopDownView_ShowsJogToPatientRightAsPerDesign" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/89f0e8ffdb475bacabb510497d76f181a0612aad_2_690x462.png" alt="TopDownView_ShowsJogToPatientRightAsPerDesign" data-base62-sha1="jGhyMM9HuAZPy3i0MLcKe3xsTTL" width="690" height="462" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/89f0e8ffdb475bacabb510497d76f181a0612aad_2_690x462.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/89f0e8ffdb475bacabb510497d76f181a0612aad_2_1035x693.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89f0e8ffdb475bacabb510497d76f181a0612aad.png 2x" data-dominant-color="9497D0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">TopDownView_ShowsJogToPatientRightAsPerDesign</span><span class="informations">1341×898 106 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7a7e69eaa49f78e0b35ae924f9c265b413331f93.jpeg" data-download-href="/uploads/short-url/htD5G1duB4Tkf6Id9PCROtz8IHF.jpeg?dl=1" title="SideViewFacingToPatientRight_AngleWrong_LengthsWrong" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7a7e69eaa49f78e0b35ae924f9c265b413331f93_2_690x322.jpeg" alt="SideViewFacingToPatientRight_AngleWrong_LengthsWrong" data-base62-sha1="htD5G1duB4Tkf6Id9PCROtz8IHF" width="690" height="322" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7a7e69eaa49f78e0b35ae924f9c265b413331f93_2_690x322.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7a7e69eaa49f78e0b35ae924f9c265b413331f93_2_1035x483.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7a7e69eaa49f78e0b35ae924f9c265b413331f93_2_1380x644.jpeg 2x" data-dominant-color="8E92D0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SideViewFacingToPatientRight_AngleWrong_LengthsWrong</span><span class="informations">1920×898 146 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
