# Tracing outline of models onto plane via curve

**Topic ID**: 40433
**Date**: 2024-11-28
**URL**: https://discourse.slicer.org/t/tracing-outline-of-models-onto-plane-via-curve/40433

---

## Post #1 by @esomjai (2024-11-28 22:31 UTC)

<p>Hi,</p>
<p>I have been trying to “translate” some facial approximation studies into slicer.<br>
My most pressing issue is the complexity of facial scans - I am using data from the NMDID, so the resolution is good, but when I try tracing any surface areas on planes, I seem to fail.</p>
<p>I created models based on thresholds -520-500 for “Skin” and 500-1100 for “Bone” and have “Plane_A”, “Plane_B”, “Plane_C” and “Plane_D” where I want to find the curve in which the respective models “meet”.</p>
<p>I have a code but it seems to freeze my Slicer whenever getting to the line it actually drawing the curves themselves. I basically want to trace the outline of the nose and the nasal opening of the cranium onto planes via creating these curves - I hope this makes sense.<br>
I hollowed out both models, but still have an “inside” and “outside” shell for both - is there a way to just create a “Mask”? I am running low on ideas how to simplify a face without losing detail too much.</p>
<p>Thank you in advance.<br>
Eszter</p>
<p>PS: these are the codes I am trying to run:<br>
1.</p>
<pre><code class="lang-auto">import slicer
import vtk
import logging
import time

# Configure logging
logging.basicConfig(level=logging.INFO)

# Assuming 'Skin', 'Bone', 'Plane_A', 'Plane_B', 'Plane_C', 'Plane_D' are already defined in the scene
skinModel = slicer.util.getNode('Skin')
boneModel = slicer.util.getNode('Bone')

def create_intersection_curve(modelNode, planeNode, curveName, color):
    logging.info(f"Starting to draw curve: {curveName}")

    # Create a plane
    plane = vtk.vtkPlane()
    plane.SetOrigin(planeNode.GetOriginWorld())
    plane.SetNormal(planeNode.GetNormalWorld())

    # Create cutter
    cutter = vtk.vtkCutter()
    cutter.SetCutFunction(plane)
    cutter.SetInputData(modelNode.GetPolyData())
    cutter.Update()

    # Create a new curve node
    curveNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsCurveNode', curveName)
    curveNode.CreateDefaultDisplayNodes()
    curveNode.GetDisplayNode().SetColor(color)
    curveNode.GetDisplayNode().SetLineThickness(2.0)

    # Add points to the curve node
    points = cutter.GetOutput().GetPoints()
    numPoints = points.GetNumberOfPoints()
    
    # Create progress bar
    progressBar = slicer.util.createProgressDialog()
    progressBar.setLabelText(f"Drawing curve: {curveName}")
    progressBar.setMaximum(numPoints)

    for i in range(numPoints):
        point = points.GetPoint(i)
        curveNode.AddControlPoint(vtk.vtkVector3d(point))
        progressBar.setValue(i + 1)
        time.sleep(0.01)  # Simulate work for demonstration purposes

    progressBar.close()
    logging.info(f"Finished drawing curve: {curveName}")

    return curveNode

planeNode_A = slicer.util.getNode('Plane_A')
skinColor = (1, 0, 1)  # Pink color in RGB
boneColor = (0, 1, 0)  # Green color in RGB

create_intersection_curve(skinModel, planeNode_A, 'Curve_Skin_A', skinColor)


planeNode_B = slicer.util.getNode('Plane_B')

create_intersection_curve(skinModel, planeNode_B, 'Curve_Skin_B', skinColor)
create_intersection_curve(boneModel, planeNode_B, 'Curve_Bone_B', boneColor)


planeNode_C = slicer.util.getNode('Plane_C')

create_intersection_curve(skinModel, planeNode_C, 'Curve_Skin_C', skinColor)
create_intersection_curve(boneModel, planeNode_C, 'Curve_Bone_C', boneColor)


planeNode_D = slicer.util.getNode('Plane_D')

create_intersection_curve(skinModel, planeNode_D, 'Curve_Skin_D', skinColor)
create_intersection_curve(boneModel, planeNode_D, 'Curve_Bone_D', boneColor)
</code></pre>
<p>AND 2:</p>
<pre><code class="lang-auto">import slicer
import vtk

# Assuming 'Skin', 'Bone', 'Plane_A', 'Plane_B', 'Plane_C', 'Plane_D' are already defined in the scene
skinModel = slicer.util.getNode('Skin')
boneModel = slicer.util.getNode('Bone')
planes = ['Plane_A', 'Plane_B', 'Plane_C', 'Plane_D']
def create_intersection_curve(modelNode, planeNode, curveName, color):
    # Create a plane
    plane = vtk.vtkPlane()
    plane.SetOrigin(planeNode.GetOriginWorld())
    plane.SetNormal(planeNode.GetNormalWorld())

    # Create cutter
    cutter = vtk.vtkCutter()
    cutter.SetCutFunction(plane)
    cutter.SetInputData(modelNode.GetPolyData())
    cutter.Update()

    # Create a new curve node
    curveNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsCurveNode', curveName)
    curveNode.CreateDefaultDisplayNodes()
    curveNode.GetDisplayNode().SetColor(color)
    curveNode.GetDisplayNode().SetLineThickness(2.0)

    # Add points to the curve node
    points = cutter.GetOutput().GetPoints()
    for i in range(points.GetNumberOfPoints()):
        point = points.GetPoint(i)
        curveNode.AddControlPoint(vtk.vtkVector3d(point))

    return curveNode
skinColor = (1, 0, 1)  # Pink color in RGB
boneColor = (0, 1, 0)  # Green color in RGB

for i, plane_name in enumerate(planes):
    planeNode = slicer.util.getNode(plane_name)
    create_intersection_curve(skinModel, planeNode, f'Curve_Skin_{chr(65 + i)}', skinColor)
    create_intersection_curve(boneModel, planeNode, f'Curve_Bone_{chr(65 + i)}', boneColor)
</code></pre>

---

## Post #2 by @pieper (2024-11-29 15:40 UTC)

<p>This sound interesting and your issue is probably solvable, but it is hard to tells from what you sent.  Can you provide end-to-end instructions to replicate the issue using public data?  (e.g. something from Slicer’s SampleData).</p>
<aside class="quote no-group" data-username="esomjai" data-post="1" data-topic="40433">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/e/e274bd/48.png" class="avatar"> esomjai:</div>
<blockquote>
<p>seems to freeze my Slicer</p>
</blockquote>
</aside>
<p>It’s likely that some operation you are doing needs to have an event update cycle to propagate through the system.  This is often the case when something works interactively but not via a script.  Strategically adding <code>slicer.app.processEvents(qt.QEventLoop.ExcludeUserInputEvents)</code> can often help.</p>

---

## Post #3 by @esomjai (2024-11-30 18:01 UTC)

<p>Hi, thank you so much for the reply - I am providing some examples from my Scene if that’s OK. I also experimented a bit with not forcing a curve, but use VTK cutter - however I am struggling to find the intersection points between the “shelled” model and my line markups. For context, I am “translating” Rynn et al.'s 2006 thesis interpretation of the original Prokopec and Ubelaker method (see <a href="https://archives.fbi.gov/archives/about-us/lab/forensic-science-communications/fsc/jan2002/prokopec.htm" rel="noopener nofollow ugc">https://archives.fbi.gov/archives/about-us/lab/forensic-science-communications/fsc/jan2002/prokopec.htm</a>) which is also referred to as mirror-plane method. The goal is to implement the originally 2D tracing in 3D.<br>
I used the CTBrain sample data for demo purposes - please note that my reference planes “PTP” (transverse), “NPP” (mirror plane along rhinion, perpendicuar to A, B, C, D) and “INB” (mid-sagittal) in this instance is randomly drawn, but in my original method it is created by other planes, etc. My other outline planes (Plane_A,B,C, D) are programmatically made to be equidistant between the “MAW” measurement and “rhinion” fiducial stored in “hard tissue” node at the 5th position: and to be parallell to the “PTP” plane:</p>
<pre><code class="lang-auto">import slicer
import numpy as np

# Get the PTP plane node
ptpPlaneNode = slicer.util.getNode('PTP')

# Get the MAW measurement position (assuming it's stored in a node)
# Replace 'MAW' with the actual node name or method to get the MAW position
mawNode = slicer.util.getNode('maximum nasal width MAW')
mawPosition = np.array(mawNode.GetNthControlPointPositionWorld(0))  # Adjust index if needed

# Get the PTP plane position and normal
ptpPlanePosition = np.array(ptpPlaneNode.GetOrigin())
ptpPlaneNormal = np.array(ptpPlaneNode.GetNormal())

# Create the new plane "A" at the MAW level
planeA = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsPlaneNode', 'Plane_A')
planeA.SetOrigin(mawPosition)
planeA.SetNormal(ptpPlaneNormal)

# Get the hard tissue node position
hardTissueNode = slicer.util.getNode('hard tissue')
rhinionPosition = np.array(hardTissueNode.GetNthControlPointPositionWorld(5))

# Calculate the distance between Plane_A and the rhinion
distance = np.dot(mawPosition - rhinionPosition, ptpPlaneNormal)

# Calculate the positions for the new planes B, C, D
numPlanes = 3
planePositions = [rhinionPosition + (i + 1) * distance / (numPlanes + 1) * ptpPlaneNormal for i in range(numPlanes)]

# Create new planes with names B, C, D
planeNames = ['B', 'C', 'D']
for i, pos in enumerate(planePositions):
    planeNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsPlaneNode', f'Plane_{planeNames[i]}')
    planeNode.SetOrigin(pos)
    planeNode.SetNormal(ptpPlaneNormal)
</code></pre>
<p>I also changed the new plane’s sizes to absolute - -50 and 50 in all directions so that the profile outlines extend only to that area, hoping to make it less complicated for Slicer - the script is 50-50 works, but I am desperate.</p>
<p>Then I made 2 models via Segmentations representing the “Skin” and “Bone” outlines that I want to “draw” onto planes A, B, C, D and INB, then find the intersection points between the outlines and lines (stay tuned - sorry, it is a convoluted one!) on planes.<br>
So I make a bone segmentation preserving the outline of the skull (314.30 and 1996 ) and a skin segmentation preserving the nasal profile outline (-659.58 to 1996) via the SegmentEditor threshold toggles, then hollowed them out as “inside surface” for bone and “outside surface” for skin 3mm shell thickness applied to visible segments. Then exported these as models, and loaded those back in renamed “Skin” and “Bone”.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b89f167aaa78bd6dc411a6e17143a1c374e13720.png" data-download-href="/uploads/short-url/qleHjvaHfwXq05qxR7e4MQNyBNK.png?dl=1" title="all planes and models established - getting to the issue" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b89f167aaa78bd6dc411a6e17143a1c374e13720_2_690x341.png" alt="all planes and models established - getting to the issue" data-base62-sha1="qleHjvaHfwXq05qxR7e4MQNyBNK" width="690" height="341" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b89f167aaa78bd6dc411a6e17143a1c374e13720_2_690x341.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b89f167aaa78bd6dc411a6e17143a1c374e13720_2_1035x511.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b89f167aaa78bd6dc411a6e17143a1c374e13720_2_1380x682.png 2x" data-dominant-color="6E6E86"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">all planes and models established - getting to the issue</span><span class="informations">1395×690 167 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I then employ a shell-making vtkCutter script:</p>
<pre><code class="lang-auto">import vtk
import slicer

def create_shell_from_bone_contours(boneModelNode, planeNodes, shellName, color):
    appendFilter = vtk.vtkAppendPolyData()
    
    for planeNode in planeNodes:
        # Create a plane
        plane = vtk.vtkPlane()
        plane.SetOrigin(planeNode.GetOriginWorld())
        plane.SetNormal(planeNode.GetNormalWorld())

        # Create cutter
        cutter = vtk.vtkCutter()
        cutter.SetCutFunction(plane)
        cutter.SetInputData(boneModelNode.GetPolyData())
        cutter.Update()

        # Get the bounds of the plane node
        bounds = [0]*6
        planeNode.GetRASBounds(bounds)

        # Create a box to clip the polydata within the bounds
        box = vtk.vtkBox()
        box.SetBounds(bounds)

        # Clip the cut polydata to only include points within the box bounds
        clipper = vtk.vtkClipPolyData()
        clipper.SetInputData(cutter.GetOutput())
        clipper.SetClipFunction(box)
        clipper.InsideOutOn()  # Keep the inside of the box
        clipper.Update()

        # Append the clipped polydata to the append filter
        appendFilter.AddInputData(clipper.GetOutput())

    # Clean the appended polydata
    cleanFilter = vtk.vtkCleanPolyData()
    cleanFilter.SetInputConnection(appendFilter.GetOutputPort())
    cleanFilter.Update()

    # Create a new model node for the shell
    shellModelNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLModelNode', shellName)
    shellModelNode.SetAndObservePolyData(cleanFilter.GetOutput())
    shellModelNode.CreateDefaultDisplayNodes()
    shellModelNode.GetDisplayNode().SetColor(color)
    shellModelNode.GetDisplayNode().SetOpacity(0.5)  # Adjust opacity as needed

    return shellModelNode

# Assuming 'Bone', 'Plane_A', 'Plane_B', 'Plane_C', 'Plane_D' are already defined in the scene
boneModel = slicer.util.getNode('Bone')
planeNodes = [slicer.util.getNode('Plane_A'), slicer.util.getNode('Plane_B'), slicer.util.getNode('Plane_C'), slicer.util.getNode('Plane_D')]
shellColor = (0, 1, 0)  # Green color in RGB

create_shell_from_bone_contours(boneModel, planeNodes, 'Shell_Bone', shellColor)

import vtk
import slicer

def create_shell_from_contours_skin(modelNode, planeNodes, shellName, color):
    appendFilter = vtk.vtkAppendPolyData()
    
    for planeNode in planeNodes:
        # Create a plane
        plane = vtk.vtkPlane()
        plane.SetOrigin(planeNode.GetOriginWorld())
        plane.SetNormal(planeNode.GetNormalWorld())

        # Create cutter
        cutter = vtk.vtkCutter()
        cutter.SetCutFunction(plane)
        cutter.SetInputData(modelNode.GetPolyData())
        cutter.Update()

        # Get the bounds of the plane node
        bounds = [0]*6
        planeNode.GetRASBounds(bounds)

        # Create a box to clip the polydata within the bounds
        box = vtk.vtkBox()
        box.SetBounds(bounds)

        # Clip the cut polydata to only include points within the box bounds
        clipper = vtk.vtkClipPolyData()
        clipper.SetInputData(cutter.GetOutput())
        clipper.SetClipFunction(box)
        clipper.InsideOutOn()  # Keep the inside of the box
        clipper.Update()

        # Append the clipped polydata to the append filter
        appendFilter.AddInputData(clipper.GetOutput())

    # Clean the appended polydata
    cleanFilter = vtk.vtkCleanPolyData()
    cleanFilter.SetInputConnection(appendFilter.GetOutputPort())
    cleanFilter.Update()

    # Create a new model node for the shell
    shellModelNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLModelNode', shellName)
    shellModelNode.SetAndObservePolyData(cleanFilter.GetOutput())
    shellModelNode.CreateDefaultDisplayNodes()
    shellModelNode.GetDisplayNode().SetColor(color)
    shellModelNode.GetDisplayNode().SetOpacity(0.5)  # Adjust opacity as needed

    return shellModelNode

# Assuming 'Skin', 'Plane_A', 'Plane_B', 'Plane_C', 'Plane_D' are already defined in the scene
skinModel = slicer.util.getNode('Skin')
planeNodes = [slicer.util.getNode('Plane_A'), slicer.util.getNode('Plane_B'), slicer.util.getNode('Plane_C'), slicer.util.getNode('Plane_D')]
skinColor = (1, 0, 1)  # Pink color in RGB

create_shell_from_contours_skin(skinModel, planeNodes, 'Shell_Skin', skinColor)



import vtk
import slicer

def create_shell_from_contours_INB(modelNode, planeNode, shellName, color):
    appendFilter = vtk.vtkAppendPolyData()
    
    # Create a plane
    plane = vtk.vtkPlane()
    plane.SetOrigin(planeNode.GetOriginWorld())
    plane.SetNormal(planeNode.GetNormalWorld())

    # Create cutter
    cutter = vtk.vtkCutter()
    cutter.SetCutFunction(plane)
    cutter.SetInputData(modelNode.GetPolyData())
    cutter.Update()

    # Get the bounds of the plane node in RAS coordinates
    bounds = [0]*6
    planeNode.GetRASBounds(bounds)

    # Create a box to clip the polydata within the bounds
    box = vtk.vtkBox()
    box.SetBounds(bounds)

    # Clip the cut polydata to only include points within the box bounds
    clipper = vtk.vtkClipPolyData()
    clipper.SetInputData(cutter.GetOutput())
    clipper.SetClipFunction(box)
    clipper.InsideOutOn()  # Keep the inside of the box
    clipper.Update()

    # Append the clipped polydata to the append filter
    appendFilter.AddInputData(clipper.GetOutput())

    # Clean the appended polydata
    cleanFilter = vtk.vtkCleanPolyData()
    cleanFilter.SetInputConnection(appendFilter.GetOutputPort())
    cleanFilter.Update()

    # Create a new model node for the shell
    shellModelNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLModelNode', shellName)
    shellModelNode.SetAndObservePolyData(cleanFilter.GetOutput())
    shellModelNode.CreateDefaultDisplayNodes()
    shellModelNode.GetDisplayNode().SetColor(color)
    shellModelNode.GetDisplayNode().SetOpacity(0.5)  # Adjust opacity as needed

    return shellModelNode

# Assuming 'Bone', 'Skin', and 'INB' are already defined in the scene
boneModel = slicer.util.getNode('Bone')
skinModel = slicer.util.getNode('Skin')
planeNode_INB = slicer.util.getNode('INB')

# Define colors
boneColor = (0, 1, 0)  # Green color in RGB
skinColor = (1, 0, 1)  # Pink color in RGB

# Create shells for Bone and Skin models using the INB plane
create_shell_from_contours_INB(boneModel, planeNode_INB, 'Shell_Bone_INB', boneColor)
create_shell_from_contours_INB(skinModel, planeNode_INB, 'Shell_Skin_INB', skinColor)
</code></pre>
<p>So I get to the point where I have the outlines from the original DICOM data:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c10a6748abcf8087e94b313a95b6b80f3c2d62eb.png" data-download-href="/uploads/short-url/rxIrlymxf6ibHW6cRr7NJhNE4L9.png?dl=1" title="Capture2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c10a6748abcf8087e94b313a95b6b80f3c2d62eb_2_616x500.png" alt="Capture2" data-base62-sha1="rxIrlymxf6ibHW6cRr7NJhNE4L9" width="616" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c10a6748abcf8087e94b313a95b6b80f3c2d62eb_2_616x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c10a6748abcf8087e94b313a95b6b80f3c2d62eb.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c10a6748abcf8087e94b313a95b6b80f3c2d62eb.png 2x" data-dominant-color="8F81AC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture2</span><span class="informations">874×709 71.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I wanted to transform the tracings into individual curves (Curve_A for the  outline present on Plane A, etc) so that I can find intersection points with lines that I established via:</p>
<pre><code class="lang-auto">################### makes lines between INB and NPP, then creates them along the mirror planes######
import numpy as np
# Get the plane nodes
planeNode1 = getNode('INB')
planeNode2 = getNode('NPP')

# Create a new line node for the intersection line
intersectionLineNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsLineNode', 'NPP_INB_line')

# Get the normal vectors and points on the planes
normal1 = np.array(planeNode1.GetNormalWorld())
point1 = np.array(planeNode1.GetOriginWorld())
normal2 = np.array(planeNode2.GetNormalWorld())
point2 = np.array(planeNode2.GetOriginWorld())

# Calculate the direction vector of the intersection line
direction = np.cross(normal1, normal2)

# Check if the planes are parallel
if np.linalg.norm(direction) == 0:
    print("The planes are parallel and do not intersect.")
else:
    # Calculate a point on the intersection line
    A = np.array([normal1, normal2, direction])
    b = np.array([np.dot(normal1, point1), np.dot(normal2, point2), 0])
    intersection_point = np.linalg.solve(A, b)

    # Define the start and end points of the line, extending further
    extension_factor = 1000  # Adjust this factor as needed
    start_point = intersection_point - extension_factor * direction
    end_point = intersection_point + extension_factor * direction

    # Set the points in the line node
    intersectionLineNode.AddControlPointWorld(start_point)
    intersectionLineNode.AddControlPointWorld(end_point)

    print("Extended intersection line created successfully.")
	
	
#########making intersection lines along INB and each mirror plane########
	# Function to create intersection line between two planes
def create_intersection_line(planeNode1, planeNode2, lineNodeName):
    # Create a new line node for the intersection line
    intersectionLineNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsLineNode', lineNodeName)

    # Get the normal vectors and points on the planes
    normal1 = np.array(planeNode1.GetNormalWorld())
    point1 = np.array(planeNode1.GetOriginWorld())
    normal2 = np.array(planeNode2.GetNormalWorld())
    point2 = np.array(planeNode2.GetOriginWorld())

    # Calculate the direction vector of the intersection line
    direction = np.cross(normal1, normal2)

    # Check if the planes are parallel
    if np.linalg.norm(direction) == 0:
        print(f"The planes {planeNode1.GetName()} and {planeNode2.GetName()} are parallel and do not intersect.")
    else:
        # Calculate a point on the intersection line
        A = np.array([normal1, normal2, direction])
        b = np.array([np.dot(normal1, point1), np.dot(normal2, point2), 0])
        intersection_point = np.linalg.solve(A, b)

        # Define the start and end points of the line, extending further
        extension_factor = 1000  # Adjust this factor as needed
        start_point = intersection_point - extension_factor * direction
        end_point = intersection_point + extension_factor * direction

        # Set the points in the line node
        intersectionLineNode.AddControlPointWorld(start_point)
        intersectionLineNode.AddControlPointWorld(end_point)

        print(f"Extended intersection line {lineNodeName} created successfully.")

# List of plane pairs and corresponding line node names
plane_pairs = [
    ('INB', 'Plane_A', 'INB_Plane_A'),
    ('INB', 'Plane_B', 'INB_Plane_B'),
    ('INB', 'Plane_C', 'INB_Plane_C'),
    ('INB', 'Plane_D', 'INB_Plane_D')
]

# Iterate over each pair and create the intersection lines
for plane1, plane2, lineName in plane_pairs:
    planeNode1 = getNode(plane1)
    planeNode2 = getNode(plane2)
    create_intersection_line(planeNode1, planeNode2, lineName)


#finding the mirror point for measuring the skin-plane and bone-plane distances###########
import numpy as np
import slicer

# Assuming 'NPP_INB_line' and 'INB_Plane_A', 'INB_Plane_B', 'INB_Plane_C', 'INB_Plane_D' are already defined in the scene
lineNode = slicer.util.getNode('NPP_INB_line')
lines = ['INB_Plane_A', 'INB_Plane_B', 'INB_Plane_C', 'INB_Plane_D']
def find_line_intersection(line1Node, line2Node):
    # Get points and directions of the lines
    p1 = np.array(line1Node.GetLineStartPositionWorld())
    d1 = np.array(line1Node.GetLineEndPositionWorld()) - p1
    p2 = np.array(line2Node.GetLineStartPositionWorld())
    d2 = np.array(line2Node.GetLineEndPositionWorld()) - p2

    # Normalize directions
    d1 /= np.linalg.norm(d1)
    d2 /= np.linalg.norm(d2)

    # Calculate intersection
    cross_d1_d2 = np.cross(d1, d2)
    if np.linalg.norm(cross_d1_d2) == 0:
        return None  # Lines are parallel

    t = np.dot(np.cross((p2 - p1), d2), cross_d1_d2) / np.linalg.norm(cross_d1_d2)**2
    intersection_point = p1 + t * d1
    return intersection_point
for i, line_name in enumerate(lines):
    line2Node = slicer.util.getNode(line_name)
    intersection_point = find_line_intersection(lineNode, line2Node)
    if intersection_point is not None:
        fiducialNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', f'mirror_{chr(65 + i)}')
        fiducialNode.AddControlPointWorld(intersection_point)

</code></pre>
<p>At this point , I just want to make Slicer create a list of fiducials for my “Bone” model and “Skin” model separately where they meet these lines - I am happy to delete the useless ones as the model thicknesses are duplicating the outlines as well as the nasal cavity.</p>
<p>I employed two scripts to try, but they create empty point lists.</p>
<pre><code class="lang-auto">import vtk
import slicer

def create_fiducials_at_intersections(modelNode, planeNode, fiducialNamePrefix):
    # Create a plane
    plane = vtk.vtkPlane()
    plane.SetOrigin(planeNode.GetOriginWorld())
    plane.SetNormal(planeNode.GetNormalWorld())

    # Create cutter
    cutter = vtk.vtkCutter()
    cutter.SetCutFunction(plane)
    cutter.SetInputData(modelNode.GetPolyData())
    cutter.Update()

    # Get the intersection points
    intersectionPolyData = cutter.GetOutput()
    points = intersectionPolyData.GetPoints()

    # Create fiducial node
    fiducialNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', fiducialNamePrefix)

    # Add fiducials at intersection points
    for i in range(points.GetNumberOfPoints()):
        point = points.GetPoint(i)
        fiducialNode.AddFiducialFromArray(point)

    return fiducialNode

# Assuming 'Shell_Bone', 'Shell_Skin', and 'INB_Plane_A' are already defined in the scene
shellBoneModel = slicer.util.getNode('Shell_Bone')
shellSkinModel = slicer.util.getNode('Shell_Skin')
lineNode_INB_Plane_A = slicer.util.getNode('INB_Plane_A')

# Create fiducials for intersections with Shell_Bone
create_fiducials_at_intersections(shellBoneModel, lineNode_INB_Plane_A, 'Intersection_Shell_Bone')

# Create fiducials for intersections with Shell_Skin
create_fiducials_at_intersections(shellSkinModel, lineNode_INB_Plane_A, 'Intersection_Shell_Skin')


</code></pre>
<p>AND 2</p>
<pre><code class="lang-auto">
import vtk
import slicer

def find_intersection_points(modelNode, lineNode, markupName, color):
    # Get the start and end points of the line
    startPoint = [0.0, 0.0, 0.0]
    endPoint = [0.0, 0.0, 0.0]
    lineNode.GetNthControlPointPositionWorld(0, startPoint)
    lineNode.GetNthControlPointPositionWorld(1, endPoint)

    # Perform ray-casting to find intersection points
    obbTree = vtk.vtkOBBTree()
    obbTree.SetDataSet(modelNode.GetPolyData())
    obbTree.BuildLocator()

    intersectionPoints = vtk.vtkPoints()
    code = obbTree.IntersectWithLine(startPoint, endPoint, intersectionPoints, None)

    # Check if intersections were found
    if intersectionPoints.GetNumberOfPoints() == 0:
        raise ValueError("No intersection points found between the model and the line.")

    # Create a new markup node
    markupNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', markupName)
    markupNode.CreateDefaultDisplayNodes()
    markupNode.GetDisplayNode().SetColor(color)
    markupNode.GetDisplayNode().SetGlyphScale(2.0)

    # Add intersection points to the markup node
    numPoints = intersectionPoints.GetNumberOfPoints()
    for i in range(numPoints):
        point = intersectionPoints.GetPoint(i)
        markupNode.AddFiducialFromArray(point)

    return markupNode

# Assuming 'Shell_Bone' and 'INB_Plane_A' are already defined in the scene
shellBoneModel = slicer.util.getNode('Shell_Bone')
lineNode_A = slicer.util.getNode('INB_Plane_A')
lineNode_B = slicer.util.getNode('INB_Plane_B')
lineNode_C = slicer.util.getNode('INB_Plane_C')
lineNode_D = slicer.util.getNode('INB_Plane_D')

# Define color for the markup node
greenColor = (0, 1, 0)  # Green color in RGB

# Find intersection points and create the markup node
find_intersection_points(shellBoneModel, lineNode_A, 'nasal bone_A', greenColor)
find_intersection_points(shellBoneModel, lineNode_B, 'nasal bone_B', greenColor)
find_intersection_points(shellBoneModel, lineNode_C, 'nasal bone_C', greenColor)
find_intersection_points(shellBoneModel, lineNode_D, 'nasal bone_D', greenColor)



import vtk
import slicer

def create_intersection_node(modelNode, planeNode, markupName, color):
    # Create a plane
    plane = vtk.vtkPlane()
    plane.SetOrigin(planeNode.GetOriginWorld())
    plane.SetNormal(planeNode.GetNormalWorld())

    # Create cutter
    cutter = vtk.vtkCutter()
    cutter.SetCutFunction(plane)
    cutter.SetInputData(modelNode.GetPolyData())
    cutter.Update()

    # Create a new markup node
    markupNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', markupName)
    markupNode.CreateDefaultDisplayNodes()
    markupNode.GetDisplayNode().SetColor(color)
    markupNode.GetDisplayNode().SetGlyphScale(2.0)

    # Add points to the markup node
    points = cutter.GetOutput().GetPoints()
    numPoints = points.GetNumberOfPoints()

    for i in range(numPoints):
        point = points.GetPoint(i)
        markupNode.AddFiducialFromArray(point)

    return markupNode

# Assuming 'Shell_Bone', 'INB_Plane_A', 'INB_Plane_B', 'INB_Plane_C', 'INB_Plane_D' are already defined in the scene
shellBoneModel = slicer.util.getNode('Shell_Bone')
planeNode_A = slicer.util.getNode('INB_Plane_A')
planeNode_B = slicer.util.getNode('INB_Plane_B')
planeNode_C = slicer.util.getNode('INB_Plane_C')
planeNode_D = slicer.util.getNode('INB_Plane_D')

# Define color for the markup nodes
greenColor = (0, 1, 0)  # Green color in RGB

# Create markup nodes for each intersection
create_intersection_node(shellBoneModel, planeNode_A, 'nasalbone_A', greenColor)
create_intersection_node(shellBoneModel, planeNode_B, 'nasalbone_B', greenColor)
create_intersection_node(shellBoneModel, planeNode_C, 'nasalbone_C', greenColor)
create_intersection_node(shellBoneModel, planeNode_D, 'nasalbone_D', greenColor)
</code></pre>
<p>I can also send my MRBL file if helps with the HeadCT and all planes/lines/models/outlines established.</p>
<p>Thank you again and am so sorry about how complicated this is!</p>

---

## Post #4 by @pieper (2024-12-02 21:58 UTC)

<p>Wow, that’s an interesting project, and the reference you cited certainly has a unique history.  It looks like you are a long ways down the path to implementing what you have in mind.  It is indeed a sophisticated use case, and of course there are many modern, natively 3D data-driven approaches that might be applied to the underlying problem.</p>
<p>In your first post you mentioned slicer hanging, but I’m not seeing where in your second post that comes up.  The extra images and scripts do help provide context, but it’s not clear to me what the core slicer programming issue is.</p>
<p>What I was thinking in my earlier response was that you might structure your work like a <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/selftests.html">Slicer SelfTest</a> in the sense that it would be stand-alone and reproducible on any machine where Slicer is installed.  The idea is that the input data is downloaded from a public source (e.g. Slicer SampleData) and then the script sets up the exact configuration and goes through the steps of your analysis.  Then if there’s a spot that’s not working (i.e. the freeze you mentioned) then other people could have a chance to help you debug.</p>
<p>Otherwise with just script snippets and images it’s hard to guess.</p>

---

## Post #5 by @esomjai (2024-12-03 09:44 UTC)

<p>Thank you so much for the prompt reply. I am going to try implementing the SelfTest Module to see where it all goes south. In my second reply, I tried a different approach via vtkCutter to visualise the outline(s) I am trying to programmatically find which works, however, when implementing an code to make a new markup point list of the intersection of the “outline” model and a line, it returns an empty point list. I will also look at resources at the SlicerMorph GitHub, thank you for your time and assistance!</p>

---

## Post #6 by @esomjai (2024-12-10 22:16 UTC)

<p>Hi,</p>
<p>I just wanted to ask about alternatives - I gave up on the first solution as it generates way too much metadata and I suspect that is the reason I freeze the programme. It would also generate more curves than I would need (internal and external surfaces, when I need only the external and no sinus outlines etc), so I tried “tracing” the outlines by generating a curve manually by constraining the point placement to a plane and resampled them to uniform numbers of points. My new upcoming issue is when I try finding the intersection points between the curve and my reference line, it comes back with an empty list of points (it generates my new fiducial, but no actual lists). <strong>I was wondering if the reason the programme cannot find these points is due to the initial outline for visuals being created via vtkCutter and essentially removing the slice there?</strong><br>
I am not familiar with SelfTests - is there a github resource that would walk me through it?</p>
<p>Thank you again,<br>
Eszter</p>

---

## Post #7 by @pieper (2024-12-10 22:25 UTC)

<p>Here are some example tests:</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/Slicer/Slicer/tree/main/Applications/SlicerApp/Testing/Python">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/Slicer/Slicer/tree/main/Applications/SlicerApp/Testing/Python" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/Slicer/Slicer/tree/main/Applications/SlicerApp/Testing/Python" target="_blank" rel="noopener">Slicer/Applications/SlicerApp/Testing/Python at main · Slicer/Slicer</a></h3>


  <p><span class="label1">Multi-platform, free open source software for visualization and image computing. - Slicer/Slicer</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>If you create self-contained examples like this other people might be able to help you debug.</p>

---
