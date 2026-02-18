# How to Create of Surface Meshes from Parallel Polygons using VTK and Python

**Topic ID**: 35557
**Date**: 2024-04-17
**URL**: https://discourse.slicer.org/t/how-to-create-of-surface-meshes-from-parallel-polygons-using-vtk-and-python/35557

---

## Post #1 by @shahrokh (2024-04-17 10:44 UTC)

<p>Hello<br>
Dear Developers and Users</p>
<p>I have several polygons that are parallel to each other and spaced at certain intervals. These are of type “<strong>model</strong>” and their mesh type is <strong>Surface Mesh (vtkPolyData)</strong>. <a href="https://drive.google.com/file/d/1NukFEyFwvqIAhYW433xNRLWtbMVAxANK/view?usp=sharing" rel="noopener nofollow ugc">This data has been placed along with CT in [Google Drive]</a>. An image of these models is shown below.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/782f909192efb2101eb35bbba945106bb9a51850.png" data-download-href="/uploads/short-url/h9dcBRJzIznpt6uBgQRhKZqE1PO.png?dl=1" title="Screenshot from 2024-04-17 14-09-30" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/782f909192efb2101eb35bbba945106bb9a51850_2_690x424.png" alt="Screenshot from 2024-04-17 14-09-30" data-base62-sha1="h9dcBRJzIznpt6uBgQRhKZqE1PO" width="690" height="424" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/782f909192efb2101eb35bbba945106bb9a51850_2_690x424.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/782f909192efb2101eb35bbba945106bb9a51850_2_1035x636.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/782f909192efb2101eb35bbba945106bb9a51850.png 2x" data-dominant-color="A5ABC6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2024-04-17 14-09-30</span><span class="informations">1373×845 194 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>It is obvious that the Number of Points, Number of Cells, and Volume may vary between them. Now I want to create a new Surface Mesh from these Surface Meshes in a way that its boundaries consist of the initial and final polygons of this set, and its body is composed of these polygons.</p>
<p>Can this be implemented using the available functions in VTK and in Python?</p>
<p>Please guide me,<br>
Best regards.<br>
Shahrokh</p>

---

## Post #2 by @cpinter (2024-04-17 11:37 UTC)

<p>My first try would be to write a Python script that does the following:</p>
<ul>
<li>Copy the contents of the model nodes in one <code>vtkPolyData</code> using <code>vtkAppendPolyDataFilter</code></li>
<li>Create a new segmentation node, and set the source representation to ‘Planar contour’ (<a href="https://github.com/Slicer/Slicer/blob/main/Libs/vtkSegmentationCore/vtkSegmentationConverter.h#L56" class="inline-onebox">Slicer/Libs/vtkSegmentationCore/vtkSegmentationConverter.h at main · Slicer/Slicer · GitHub</a>)</li>
<li>Set the appended polydata as the <code>Planar contour</code> representation of the segmentation node</li>
<li>Call <code>GetClosedSurfaceRepresentation</code> on the segmentation node. Then the underlying conversion rule will do this interpolation for you</li>
</ul>
<p>Note that you will need the SlicerRT extension to be installed first, because the mentioned conversion rule is provided there.</p>
<p>It is probably useful to check out the third figure in the page <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html" class="inline-onebox">Image Segmentation — 3D Slicer documentation</a>. You will see that this type of representation is often the original input when you work with radiation therapy data. This interpolator has been stable for quite a while now, so you should be able to use it safely.</p>

---

## Post #3 by @shahrokh (2024-04-17 14:33 UTC)

<p>Dear Csaba Pinter</p>
<p>Thanks a lot for your guidance completely…</p>
<p>I’ve completed up to the second step of thinking, and I wasn’t successful in implementing the third step… Hopefully, I’ll be able to continue the work next week…</p>
<p>The following lines are my code at this point.</p>
<pre><code class="lang-auto">import vtk
import slicer
import vtkSegmentationCorePython

nodeNames = ["Model_-407.5", "Model_-405.0", "Model_-400.0", "Model_-395.0", "Model_-390.0", "Model_-385.0", "Model_-380.0", "Model_-375.0", "Model_-372.5"]

appendFilter = vtk.vtkAppendPolyData()

for nodeName in nodeNames:
    node = slicer.util.getNode(nodeName)
    if node:
        # Get the vtkPolyData from the node
        polyData = node.GetPolyData()
        if polyData:
            # Add the polyData to the appendFilter
            appendFilter.AddInputData(polyData)

appendFilter.Update()

outputPolyData = appendFilter.GetOutput()

newModelNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLModelNode", "outputPolyData")

newModelNode.SetAndObservePolyData(outputPolyData)

segmentationConverter = vtkSegmentationCorePython.vtkSegmentationConverter()
planarContourName = segmentationConverter.GetSegmentationPlanarContourRepresentationName()
print("Planar contour representation name:", planarContourName)

segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")

</code></pre>
<p>Best regaeds.<br>
Shahrokh</p>

---

## Post #4 by @shahrokh (2024-04-21 13:18 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="2" data-topic="35557">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>Set the appended polydata as the <code>Planar contour</code> representation of the segmentation node</p>
</blockquote>
</aside>
<p>First, I must thank Dear Csaba Pinter for the guidance provided in solving the issue I raised. In implementing this guidance, I encounter two issues:</p>
<p><em>First Issue:</em></p>
<p>Executing the above commands in the Python Console in 3DSlicer (repeated below) creates a node named “Segmentation”.</p>
<pre><code class="lang-auto">import vtk
import slicer
import vtkSegmentationCorePython

nodeNames = ["Model_-407.5", "Model_-405.0", "Model_-400.0", "Model_-395.0", "Model_-390.0", "Model_-385.0", "Model_-380.0", "Model_-375.0", "Model_-372.5"]

appendFilter = vtk.vtkAppendPolyData()

for nodeName in nodeNames:
    node = slicer.util.getNode(nodeName)
    if node:
        # Get the vtkPolyData from the node
        polyData = node.GetPolyData()
        if polyData:
            # Add the polyData to the appendFilter
            appendFilter.AddInputData(polyData)

appendFilter.Update()

outputPolyData = appendFilter.GetOutput()

newModelNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLModelNode", "outputPolyData")

newModelNode.SetAndObservePolyData(outputPolyData)

segmentationConverter = vtkSegmentationCorePython.vtkSegmentationConverter()
planarContourName = segmentationConverter.GetSegmentationPlanarContourRepresentationName()
print("Planar contour representation name:", planarContourName)

segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
</code></pre>
<p>As seen in the following figure, its <strong>Representation</strong> type is <strong>Binary labelmap</strong>, not <strong>Planar contour</strong>. I expected that by executing the above commands, the <strong>Representation</strong> type would be <strong>Planar contour</strong>.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/826c54dc64542efdcb2cccdf38c6f791ce223f9f.png" data-download-href="/uploads/short-url/iBMayDrS92kxXEXmy9c2p5pHqmb.png?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/826c54dc64542efdcb2cccdf38c6f791ce223f9f_2_690x431.png" alt="1" data-base62-sha1="iBMayDrS92kxXEXmy9c2p5pHqmb" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/826c54dc64542efdcb2cccdf38c6f791ce223f9f_2_690x431.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/826c54dc64542efdcb2cccdf38c6f791ce223f9f_2_1035x646.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/826c54dc64542efdcb2cccdf38c6f791ce223f9f_2_1380x862.png 2x" data-dominant-color="D3D2D4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1440×900 278 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>How can I set the <strong>Representation</strong> type to <strong>Planar contour</strong> according to the provided guidance by Csaba Pinter?</p>
<p><em>Second Issue</em>:<br>
In implementing the third step, Csaba Pinter told that:<br>
Set the appended polydata as the <code>Planar contour</code> representation of the  segmentation node…</p>
<p>I have a problem. I can do this by setting <strong>Planar contour</strong> and importing outputPolyData in <strong>Segmentations</strong> module (not in Python Console of 3DSlicer), but I encounter the following error. How can I perform this third step?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a868c1abef2434885dc6418aa40b9050a1f680bf.png" data-download-href="/uploads/short-url/o1OEBiKi8iFWasN3hGHJXQoSsnJ.png?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a868c1abef2434885dc6418aa40b9050a1f680bf_2_690x431.png" alt="2" data-base62-sha1="o1OEBiKi8iFWasN3hGHJXQoSsnJ" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a868c1abef2434885dc6418aa40b9050a1f680bf_2_690x431.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a868c1abef2434885dc6418aa40b9050a1f680bf_2_1035x646.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a868c1abef2434885dc6418aa40b9050a1f680bf_2_1380x862.png 2x" data-dominant-color="CFCED0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">1440×900 296 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Please guide me to do step <span class="hashtag-raw">#2</span> and <span class="hashtag-raw">#3</span>.<br>
Best regards.<br>
Shahrokh</p>

---

## Post #5 by @cpinter (2024-04-22 13:11 UTC)

<p>The code seems so far so good, but not complete. As you said you’ll need to set the proper source representation, and then the representation itself. By the way I suggest using the latest Slicer, 5.2.2 is now years old, and the API has changed a bit since then too (e.g. “master” vs “source” representation).</p>
<pre><code class="lang-auto">segmentationNode.GetSegmentation().SetSourceRepresentationName(planarContourName)
seg = slicer.vtkSegment()
seg.SetName('NameYouWant')
seg.AddRepresentation(planarContourName, newModelNode.GetPolyData())
segmentationNode.GetSegmentation().AddSegment(seg)
</code></pre>
<p>A few comments:</p>
<ul>
<li>You don’t need <code>import vtkSegmentationCorePython</code>, you can simply do <code>slicer.vtkSegmentationConverter</code>. Also, you don’t need to instantiate it, so just <code>slicer.vtkSegmentationConverter.GetSegmentationPlanarContourRepresentationName()</code></li>
<li>You don’t need to create a new model node. Just have the poly data. So in the above snippet, you can replace <code>newModelNode.GetPolyData()</code> with <code>appendFilter.GetOutput()</code></li>
</ul>

---

## Post #6 by @shahrokh (2024-04-23 11:44 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="2" data-topic="35557">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p><code>GetClosedSurfaceRepresentation</code></p>
</blockquote>
</aside>
<p>Thank you very much to Csaba Pinter for the guidance in implementing the code. As you mentioned, I made the changes in the code as follows:</p>
<pre><code class="lang-auto">import vtk
import slicer

# Step #1
nodeNames = ["Model_-407.5", "Model_-405.0", "Model_-400.0", "Model_-395.0", "Model_-390.0", "Model_-385.0", "Model_-380.0", "Model_-375.0", "Model_-372.5"]

appendFilter = vtk.vtkAppendPolyData()

for nodeName in nodeNames:
    node = slicer.util.getNode(nodeName)
    if node:
        # Get the vtkPolyData from the node
        polyData = node.GetPolyData()
        if polyData:
            # Add the polyData to the appendFilter
            appendFilter.AddInputData(polyData)

appendFilter.Update()

outputPolyData = appendFilter.GetOutput()

newModelNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLModelNode", "outputPolyData")

newModelNode.SetAndObservePolyData(outputPolyData)

# Step #2
segmentationConverter = slicer.vtkSegmentationConverter()
planarContourName = slicer.vtkSegmentationConverter.GetSegmentationPlanarContourRepresentationName()
segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")

# Step #3 (the guidance of Csaba Pinter)
segmentationNode.GetSegmentation().SetSourceRepresentationName(planarContourName)
seg = slicer.vtkSegment()
seg.SetName('bolusSegment')
seg.AddRepresentation(planarContourName, appendFilter.GetOutput())
segmentationNode.GetSegmentation().AddSegment(seg)
</code></pre>
<p>Now, in the implementation of the fourth step, I encountered the following error:</p>
<pre><code class="lang-auto"># Step #4
id = segmentationNode.GetID()
segmentationNode.GetClosedSurfaceRepresentation(id, outputPolyData)
</code></pre>
<p>The output I obtained by executing the last command is as follows:</p>
<pre><code class="lang-auto">False
[VTK] GetClosedSurfaceRepresentation: Invalid segment
</code></pre>
<p>Unfortunately, I don’t understand why I encountered this error. I even used the <strong><a href="https://apidocs.slicer.org/main/classvtkMRMLSegmentationNode.html#a981a64425627037c55d418c36981e371" rel="noopener nofollow ugc">CreateClosedSurfaceRepresentation()</a></strong> method because it was explained in relation to <code>GetClosedSurfaceRepresentation</code> that:</p>
<p>“Get a segment as a surface mesh. If representation does not exist yet then CreateClosedSurfaceRepresentation() must be called before this method. This function returns a copy of the segment closed surface in outputClosedSurface. Returns true on success.”</p>
<p>Please guide me.<br>
Best regards.<br>
Shahrokh</p>

---

## Post #7 by @shahrokh (2024-04-24 12:55 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="2" data-topic="35557">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>on the segmentation node</p>
</blockquote>
</aside>
<p>As mentioned in the help on built-in function <code>GetClosedSurfaceRepresentation</code>:</p>
<pre><code class="lang-auto">GetClosedSurfaceRepresentation(...) method of MRMLCorePython.vtkMRMLSegmentationNode instance
GetClosedSurfaceRepresentation(self, segmentId:str,
outputClosedSurface:vtkPolyData) -&gt; bool
C++: virtual bool GetClosedSurfaceRepresentation(
const std::string segmentId, vtkPolyData *outputClosedSurface)
Get a segment as a surface mesh. If representation does not exist
yet then CreateClosedSurfaceRepresentation() must be called
before this method. This function returns a copy of the segment
closed surface in outputClosedSurface. Returns true on success.
</code></pre>
<p>As mentioned above, If the representation does not exist, the function <code>CreateClosedSurfaceRepresentation</code> must be called before using this method. Excuse me, but I didn’t understand why Csaba Pinter mentioned that the representation type should be <code>Planar contour</code> in guidance. Anyway, I continued my efforts according to this help (although I believe this is not correct):</p>
<pre><code class="lang-auto">&gt;&gt;&gt; segmentationNode.CreateClosedSurfaceRepresentation()
True
</code></pre>
<p>Then , I call  <code>GetClosedSurfaceRepresentation</code> on the segmentation node.</p>
<pre><code class="lang-auto">&gt;&gt;&gt; segmentationNode.GetClosedSurfaceRepresentation(segmentationNode.GetID(), outputPolyData)
False
[VTK] GetClosedSurfaceRepresentation: Invalid segment
&gt;&gt;&gt; 
</code></pre>
<p>As mentioned above, the problem is related to the first argument of the <code>CreateClosedSurfaceRepresentation</code> method.<br>
Excuse me… How can I set the two arguments of <code>GetClosedSurfaceRepresentation</code> so that it creates and covers all contours of my models <code>(Model_-407.5, Model_-405.0, ..., Model_-372.5)</code> with a solid model?</p>
<p>Please guide me.<br>
Best regards.<br>
Shahrokh</p>

---

## Post #8 by @shahrokh (2024-04-24 14:03 UTC)

<p>During my attempt to call <code>GetClosedSurfaceRepresentation</code>, I encountered an interesting coincidence. Upon executing the following codes, when I run the commands the section of <code>Step #4</code>, 3DSlicer suddenly <strong>crashes and closes</strong>.</p>
<pre><code class="lang-auto">import vtk
import slicer

# Step #1
nodeNames = ["Model_-407.5", "Model_-405.0", "Model_-400.0", "Model_-395.0", "Model_-390.0", "Model_-385.0", "Model_-380.0", "Model_-375.0", "Model_-372.5"]

appendFilter = vtk.vtkAppendPolyData()

for nodeName in nodeNames:
    node = slicer.util.getNode(nodeName)
    if node:
        # Get the vtkPolyData from the node
        polyData = node.GetPolyData()
        if polyData:
            # Add the polyData to the appendFilter
            appendFilter.AddInputData(polyData)

appendFilter.Update()

outputPolyData = appendFilter.GetOutput()

newModelNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLModelNode", "outputPolyData")

newModelNode.SetAndObservePolyData(outputPolyData)

# Step #2
segmentationConverter = slicer.vtkSegmentationConverter()
planarContourName = slicer.vtkSegmentationConverter.GetSegmentationPlanarContourRepresentationName()
segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")

# Step #3 (the guidance of Csaba Pinter)
segmentationNode.GetSegmentation().SetSourceRepresentationName(planarContourName)
seg = slicer.vtkSegment()
seg.SetName('bolusSegment')
seg.AddRepresentation(planarContourName, appendFilter.GetOutput())
segmentationNode.GetSegmentation().AddSegment(seg)


# Step #4
segmentation_node = slicer.util.getNode('Segmentation')
segment_id = segmentation_node.GetSegmentation().GetSegmentIdBySegmentName('bolusSegment')
segmentation_node.CreateClosedSurfaceRepresentation()
segmentation_node.GetClosedSurfaceRepresentation(segment_id, outputPolyData)

</code></pre>
<p>I think that  I am near to implementing of the fourth step (with the minor error)<br>
Please guide me to solve it.<br>
Thanks a lot.<br>
Best regards.<br>
Shahrokh</p>

---

## Post #9 by @lassoan (2024-04-25 04:41 UTC)

<p>I’ve implemented something like this for OsiriX ROI importer module. You might find the code useful: <a href="https://github.com/PerkLab/SlicerSandbox/blob/master/ImportOsirixROI/ImportOsirixROI.py" class="inline-onebox">SlicerSandbox/ImportOsirixROI/ImportOsirixROI.py at master · PerkLab/SlicerSandbox · GitHub</a></p>

---
