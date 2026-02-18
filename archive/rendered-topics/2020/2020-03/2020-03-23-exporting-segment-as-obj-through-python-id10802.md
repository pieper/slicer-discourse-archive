# Exporting Segment as OBJ through Python

**Topic ID**: 10802
**Date**: 2020-03-23
**URL**: https://discourse.slicer.org/t/exporting-segment-as-obj-through-python/10802

---

## Post #1 by @Queen_Rei (2020-03-23 19:20 UTC)

<p>Heya there! I would love to get some advice on how to export a segment I created to a file. I found this code from another topic and was wondering how and where I can the info. needed to do this for a .obj.</p>
<h1>Write to STL file</h1>
<pre><code>surfaceMesh = segmentationNode.GetClosedSurfaceRepresentation(addedSegmentID)
writer = vtk.vtkSTLWriter()
writer.SetInputData(surfaceMesh)
writer.SetFileName("Z:/something.stl")
writer.Update()
</code></pre>
<p>Thank you in advance &lt;3</p>

---

## Post #2 by @lassoan (2020-03-23 20:19 UTC)

<p>Use vtkOBJWriter instead of vtkSTLWriter to write OBJ file.</p>

---

## Post #3 by @lassoan (2020-03-23 20:20 UTC)

<p>See also this topic:</p>
<aside class="quote" data-post="1" data-topic="10804">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/6de8d8/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-to-export-model-node-to-vrml-2-and-stl-ascii-and-binary/10804">How to export model node to VRML 2 and STL (ascii and binary)</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Hello, 
I need to be able to export a model node as VRML 2, ascii STL, and binary STL files for a module I am developing. I know essentially nothing about vtk so any help or resources you could provide would be lovely. 
Thank you!
  </blockquote>
</aside>


---

## Post #4 by @Queen_Rei (2020-03-23 20:33 UTC)

<p>Thank you for the quick reply! It’s working now~</p>

---

## Post #5 by @Queen_Rei (2020-03-27 16:38 UTC)

<p>Good day, I have a quick question!</p>
<pre><code>outputFolder = "Z:/Dicom2Text/DicomPrefabs"
ExportSegmentsClosedSurfaceRepresentationToFiles(outputFolder, segmentatioNode, [segmentTypeID], "OBJ", true, 1.0, false)
</code></pre>
<p>Given your advice on the topic you provided me I have been trying to use “ExportSegmentsClosedSurfaceRepresentationToFiles”<br>
What am I missing from the code above to make it call the method?</p>
<p>Thank you &lt;3</p>

---

## Post #6 by @Queen_Rei (2020-03-27 18:19 UTC)

<p>I fixed it, but now I am getting a different issue</p>
<pre><code>outputFolder = "Z:/Dicom2Text/DicomPrefabs"
slicer.vtkSlicerSegmentationsModuleLogic.ExportSegmentsClosedSurfaceRepresentationToFiles(outputFolder, segmentationNode, [segmentTypeID], "OBJ", True, 1.0, False)
</code></pre>
<p>The error I am getting is:<br>
TypeError: ExportSegmentsClosedSurfaceRepresentationToFiles argument 3: method requires a VTK object</p>

---

## Post #7 by @lassoan (2020-03-27 18:39 UTC)

<p>To get help on how to use a method, use <code>help</code> method in the Python interactor:</p>
<pre><code class="lang-nohighlight">&gt;&gt;&gt; help(slicer.vtkSlicerSegmentationsModuleLogic.ExportSegmentsClosedSurfaceRepresentationToFiles)
Help on method_descriptor:

ExportSegmentsClosedSurfaceRepresentationToFiles(...)
    V.ExportSegmentsClosedSurfaceRepresentationToFiles(string,
        vtkMRMLSegmentationNode, vtkStringArray, string, bool, float,
        bool) -&gt; bool
    C++: static bool ExportSegmentsClosedSurfaceRepresentationToFiles(
        std::string destinationFolder,
        vtkMRMLSegmentationNode *segmentationNode,
        vtkStringArray *segmentIds=nullptr,
        std::string fileFormat="STL", bool lps=true,
        double sizeScale=1.0, bool merge=false)
    
    Export closed surface representation of multiple segments to
    files. Typically used for writing 3D printable model files.
</code></pre>
<p>As you can see, a <code>vtkStringArray</code> object is expected, while you provided a Python list of strings. If you want to export all segments, you can use <code>None</code>, if you want to export specific segments, create a <code>vtk.vtkStringArray</code> object and add the segment IDs that you would like to export.</p>

---

## Post #8 by @Queen_Rei (2020-03-27 19:01 UTC)

<p>Thank you so much!!! I got it to work and all the information you have provided me has given a much better understand about the magic going on behind the scenes!!!</p>

---

## Post #9 by @lassoan (2021-10-08 03:40 UTC)

<p>A post was split to a new topic: <a href="/t/save-segmentation-as-ply-file/20063">Save segmentation as PLY file</a></p>

---
