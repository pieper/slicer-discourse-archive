---
topic_id: 8448
title: "Programmatically Create A Segmentationnode And Labelmapnode"
date: 2019-09-16
url: https://discourse.slicer.org/t/8448
---

# Programmatically Create a SegmentationNode and LabelMapNode from Polygon Coordinates

**Topic ID**: 8448
**Date**: 2019-09-16
**URL**: https://discourse.slicer.org/t/programmatically-create-a-segmentationnode-and-labelmapnode-from-polygon-coordinates/8448

---

## Post #1 by @rmd (2019-09-16 18:00 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.10.2</p>
<p>Hello,</p>
<p>I have some manually drawn ROIs represented as points in the row, column, slice coordinate frame. I am trying to programmatically generate a vtkMRMLSegmentationNode from those points. I also want to be able to export a image that is 1 everywhere inside the polygon and 0 outside. Right now, the approach I am taking is as follows, with actual code below</p>
<ol>
<li>Turn the polygon coordinates (row, column, slice) into a binary numpy array that equals to 1 inside the polygon and zero everywhere else.</li>
<li>Take the binary numpy array and put it into a vtkMRMLLabelMapVolumeNode</li>
<li>Import that LabelMapNode into a vtkMRMLSegmentationNode</li>
<li>Save the segmentation node as an RTStruct (not shown in the code because I’m doing it manually)</li>
</ol>
<p>The problem I am having is with step 1 above. Although scikit-image and PIL have great functions to help convert polygon points into a binary map (e.g. skimage.draw.polygon) I cannot successfully install scikit-image or PIL into the Python interpreter. The rest of the steps 2-4 work fine, as verified by manually creating a box mask using numpy array slicing.</p>
<p>Does slicer already have a function that can convert a polygon to a binary mask? Or, alternatively, can I just somehow directly load the polygon coordinates into a segmentation node? The polygons are 3D (i.e. they span multiple rows, columns, slices).</p>
<p>Here is the relevant portions of my code:</p>
<p><span class="hashtag">#function</span> createSegNode creates a segmentation node from a mask and name<br>
<span class="hashtag">#inputs</span><br>
<span class="hashtag">#mask:</span> a 3D numpy array with 1s everywhere inside the polygons and 0s elsewhere<br>
<span class="hashtag">#name:</span> name to assign new segmentation node<br>
def createSegNode(mask,name):</p>
<pre><code>#create volume node representing a labelmap
volumeNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLabelMapVolumeNode')
volumeNode.CreateDefaultDisplayNodes()

#place np array in volume node
updateVolumeFromArray(volumeNode, mask.astype(int))

#orient the labelmap in the right direction
volumeNode.SetOrigin(im_node.GetOrigin())
volumeNode.SetSpacing(im_node.GetSpacing())
imageDirections = [[1,0,0], [0,-1,0], [0,0,-1]]
volumeNode.SetIJKToRASDirections(imageDirections)

#convert labelmap into a segmentation object
segNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLSegmentationNode')
slicer.modules.segmentations.logic().ImportLabelmapToSegmentationNode(volumeNode, segNode)
segNode.SetName(name)
</code></pre>
<p><span class="hashtag">#create</span> a toy 2d polygon mask<br>
r = [100, 150, 150, 100] <span class="hashtag">#polygon</span> rows<br>
c= [100, 100, 150, 150] <span class="hashtag">#polygon</span> columns<br>
m2=np.zeros((2,len(r)))<br>
polygon_array = create_polygon([512,512], m2.T).T <span class="hashtag">#I</span> don’t have a good function to do this reliably. Right now I’m using a function I found on stackoverflow that doesn’t accurately reproduce the polygons</p>
<p><span class="hashtag">#put</span> the polygon into a 3d array<br>
im_node=getNode(“&lt;&lt; node name&gt;&gt;”)<br>
node_np=slicer.util.arrayFromVolume(im_node)<br>
polygon_array_3d=np.zeros(node_np.shape)<br>
polygon_array_3d[20,200:250,200:250]=1<br>
createSegNode(seg_d,seg) <span class="hashtag">#calls</span> above function</p>

---

## Post #2 by @lassoan (2019-09-16 18:26 UTC)

<aside class="quote no-group" data-username="rmd" data-post="1" data-topic="8448">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/c57346/48.png" class="avatar"> rmd:</div>
<blockquote>
<p>Turn the polygon coordinates (row, column, slice) into a binary numpy array that equals to 1 inside the polygon and zero everywhere else.</p>
</blockquote>
</aside>
<p>It is very difficult to do this robustly. Naive implementation in scikit-image and PIL work for simple cases and maybe yours is like that, so that’s one approach you can try. You can only install non-native Python binary packages in recent Slicer Preview versions, not in Slicer-4.10.x.</p>
<aside class="quote no-group" data-username="rmd" data-post="1" data-topic="8448">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/c57346/48.png" class="avatar"> rmd:</div>
<blockquote>
<p>can I just somehow directly load the polygon coordinates into a segmentation node? The polygons are 3D (i.e. they span multiple rows, columns, slices).</p>
</blockquote>
</aside>
<p>Yes, you can. Segmentations module can accept various representations, including “planar contours”, which is how your data is represented now. Then, segmentations module can automatically convert this to various other representations, such as binary labelmap or closed surface. The converter to binary labelmap is much more sophisticated than the simple one in scikit-image - it can can handle handle keyholes, branching, contours at non-equal distances, etc.</p>
<p>What you need to do is to save your contours a VTK polydata and add some <a href="https://apidocs.slicer.org/master/classvtkMRMLSegmentationStorageNode.html#details">custom fields</a> that indicate that the polydata should be interpreted as a segmentation node. See complete example <a href="https://1drv.ms/u/s!Arm_AFxB9yqHt-tneCcdRys0WuQGfQ?e=4elYpL">here</a>.</p>
<p>Closed surface representation is provided by SlicerRT extension (as planar contours are commonly used representation in radiation therapy), so you need to install this extension for this representation to show up in Slicer.</p>

---

## Post #3 by @rmd (2019-09-16 23:35 UTC)

<p>Hello,<br>
Thanks for the help. This points me in the right direction but I’m relatively new to VTK so I hope I can ask a few follow-ups.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="8448">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>What you need to do is to save your contours a VTK polydata and add some <a href="https://apidocs.slicer.org/master/classvtkMRMLSegmentationStorageNode.html#details" rel="noopener nofollow ugc">custom fields</a> that indicate that the polydata should be interpreted as a segmentation node. See complete example <a href="https://1drv.ms/u/s!Arm_AFxB9yqHt-tneCcdRys0WuQGfQ?e=4elYpL" rel="noopener nofollow ugc">here </a>.</p>
</blockquote>
</aside>
<ol>
<li>If I understand correctly, I need to save the contour points (e.g. rows, columns, slices) to a .vtk polyData file on my hard drive using a function like vtkToPoly <a href="https://vtk.org/Wiki/VTK/Writing_VTK_files_using_python" rel="noopener nofollow ugc">here</a>.</li>
<li>While saving the .vtk file, I need to set a custom field as so: Segmentation_ContainedRepresentationNames = “Planar contours”</li>
<li>Use the function vtkMRMLSegmentationStorageNode.ReadPolyDataRepresentation() to open the .vtk file as a segmentation node.</li>
</ol>
<p>If that is correct, then my main question is how to save a .vtk file from the slicer python interpreter? I think I can’t install the evtk.hl module linked above from the windows slicer python interpreter.</p>
<p>Thanks a lot for your help.</p>
<p>Ryan</p>

---

## Post #4 by @lassoan (2019-09-17 03:55 UTC)

<aside class="quote no-group" data-username="rmd" data-post="3" data-topic="8448">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/c57346/48.png" class="avatar"> rmd:</div>
<blockquote>
<p>my main question is how to save a .vtk file from the slicer python interpreter?</p>
</blockquote>
</aside>
<p>Probably the simplest is to create a segmentation node directly instead of creating a vtk file that can be loaded as segmentation. Here is a complete example of creating a segment (including closed surface and binary labelmap representation) from a list of contour points:</p>
<pre data-code-wrap="python"><code class="lang-python"># Create segmentation node where we will store segments
segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
segmentationNode.CreateDefaultDisplayNodes()

# Create a segment from planar contours - can be repeated for multiple segments

segmentName = "test"
segmentColor = [1, 0, 0]
contours = [
    [[10,10,0], [30,10,0], [30,40,0], [10,25,0]],
    [[12,13,10], [31,9,10], [34,41,10], [12,23,10]],
    [[14,8,20], [22,11,20], [28,16,20], [16,28,20], [2,21,20]],
]

contoursPolyData = vtk.vtkPolyData()
contourPoints = vtk.vtkPoints()
contourLines = vtk.vtkCellArray()
contoursPolyData.SetLines(contourLines)
contoursPolyData.SetPoints(contourPoints)
for contour in contours:
    startPointIndex = contourPoints.GetNumberOfPoints()
    contourLine = vtk.vtkPolyLine()
    linePointIds = contourLine.GetPointIds()
    for point in contour:
        linePointIds.InsertNextId(contourPoints.InsertNextPoint(point))
    linePointIds.InsertNextId(startPointIndex) # make the contour line closed
    contourLines.InsertNextCell(contourLine)

segment = slicer.vtkSegment()
segment.SetName(segmentName)
segment.SetColor(segmentColor)
segment.AddRepresentation('Planar contour', contoursPolyData)
segmentationNode.GetSegmentation().AddSegment(segment)
</code></pre>

---

## Post #5 by @rmd (2019-09-18 23:35 UTC)

<p>Hi Andras,<br>
Thanks so much for the help, I am so close but there is a remaining issue. I expected that when I view the segmentationNode overlaid on my image, the coordinates of the segment should match the numerical values that I loaded into the segmentationNode object. But they don’t.</p>
<p>I searched a lot of documentation and found the SetReferenceImageGeometryParameterFromVolumeNode() function for vtkMRMLSegmentationNode but this didn’t seem to help. I also tried converting the segmentationNode to a binary labelmap, then applying the origin, pixel spacing, and image direction of my image to the labelmap, but still the location of the labelmap didn’t match the value of the contour points that I loaded in.</p>
<p>Here is the relevant code:</p>
<pre><code>#createSegNode2 function from Andras Lasso
def createSegNode2(segmentationNode,contours,name):
    # set up contour objects
    contoursPolyData = vtk.vtkPolyData()
    contourPoints = vtk.vtkPoints()
    contourLines = vtk.vtkCellArray()
    contoursPolyData.SetLines(contourLines)
    contoursPolyData.SetPoints(contourPoints)

    for contour in contours:
	    startPointIndex = contourPoints.GetNumberOfPoints()
        contourLine = vtk.vtkPolyLine()
    	linePointIds = contourLine.GetPointIds()
       	for point in contour:
	    	linePointIds.InsertNextId(contourPoints.InsertNextPoint(point))
	    linePointIds.InsertNextId(startPointIndex) # make the contour line closed
    	contourLines.InsertNextCell(contourLine)

    segment = slicer.vtkSegment()
    segment.SetName(name)
    #segment.SetColor(segmentColor)
    segment.AddRepresentation('Planar contour', contoursPolyData)
    segmentationNode.GetSegmentation().AddSegment(segment)

#load the volume node corresponding to CT image
im_node=getNode("1006: UNKNOWN")

#Create segmentation node where we will store segments
segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
segmentationNode.CreateDefaultDisplayNodes()
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(im_node) #I tried with and without this line

contours = [
[[10,10,0], [30,10,0], [30,40,0], [10,25,0]],
[[12,13,10], [31,9,10], [34,41,10], [12,23,10]],
[[14,8,20], [22,11,20], [28,16,20], [16,28,20], [2,21,20]],
]

createSegNode2(segmentationNode,contours,'test')
</code></pre>
<p>Here is the segment (green) on top of my image<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d59d2863a06014ac97bf17029bdece87b476dbc3.png" data-download-href="/uploads/short-url/utIpqIh7jlfxWB3AiEdEFvcqyNd.png?dl=1" title="Annotation%202019-09-18%20162444" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d59d2863a06014ac97bf17029bdece87b476dbc3_2_690x312.png" alt="Annotation%202019-09-18%20162444" data-base62-sha1="utIpqIh7jlfxWB3AiEdEFvcqyNd" width="690" height="312" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d59d2863a06014ac97bf17029bdece87b476dbc3_2_690x312.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d59d2863a06014ac97bf17029bdece87b476dbc3_2_1035x468.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d59d2863a06014ac97bf17029bdece87b476dbc3_2_1380x624.png 2x" data-dominant-color="9B9B9B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Annotation%202019-09-18%20162444</span><span class="informations">1417×641 171 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The pixel location of the bottom left corner of the green segment according to the data probe is (299,241,30) not even close to the values stored in the contour variable above. How can I match the coordinate system of the segmentation node to the coordinate system of the image?</p>
<p>Thanks again for your help<br>
Ryan</p>

---

## Post #6 by @lassoan (2019-09-19 00:20 UTC)

<p>What software did you use to draw the contours?</p>
<p>What coordinate system the numbers are stored in? Most common are LPS, IJK, and RAS (Slicer uses this).</p>
<p>Do you have an example data set that you can share?</p>

---

## Post #7 by @Gaurav_Gupta (2020-02-07 01:12 UTC)

<p>Ryan, were you able to solve this issue? I am having same issue – my segmentation-polygon are not appearing in expected location in the 2D view, although I am using (y,x,slicecount) format, and coordinates seem to look okay (in text logs)</p>

---

## Post #8 by @lassoan (2020-02-07 01:58 UTC)

<p>If you have any mismatch in coordinates then probably you just did not get the IJK to RAS transformatin right. If you provide an example data set then we can tell you how to do compute and apply the transform correctly.</p>

---

## Post #9 by @Gaurav_Gupta (2020-02-07 02:31 UTC)

<p>Andras, is there an example code-snippet for IJK to RAS transformation?</p>

---

## Post #10 by @lassoan (2020-02-07 03:08 UTC)

<p>There are several examples for that in the script repository, e.g., <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_markup_fiducial_RAS_coordinates_from_volume_voxel_coordinates">this</a>.</p>

---

## Post #11 by @Gaurav_Gupta (2020-02-09 20:36 UTC)

<p>perfect! Thank you, you saved my day.</p>

---

## Post #12 by @rmd (2020-02-10 20:58 UTC)

<p>Hi Gaurav,<br>
Yes, Andras was correct in that I was working in IJK, not physical coordinates. Once I switched to physical, then the contours imported correctly.</p>
<p>Ryan</p>

---
