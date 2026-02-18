# STL conversion to OBJ

**Topic ID**: 11972
**Date**: 2020-06-09
**URL**: https://discourse.slicer.org/t/stl-conversion-to-obj/11972

---

## Post #1 by @Queen_Rei (2020-06-09 23:45 UTC)

<p>Hello! I used the following code snippet to import a STL as a segmentation and export that segmentation into a OBJ.</p>
<p>Issue: Right now the exported OBJ seems to be lower quality than if I did this manually. I feel as though there many be a flaw in my approach. I would love some insight on the code snippet below. Thank you &lt;3</p>
<pre><code>        # Load STL, import as segmentation, and export as OBJ
        stlSegmentationNode = slicer.util.loadSegmentation(inputFolder)
        segmentIDs = vtk.vtkStringArray()
        segmentIDs.InsertNextValue(fileName)
        slicer.vtkSlicerSegmentationsModuleLogic.ExportSegmentsClosedSurfaceRepresentationToFiles(outputFolder, stlSegmentationNode, segmentIDs, "OBJ", True, 1.0, False)</code></pre>

---

## Post #2 by @lassoan (2020-06-10 00:29 UTC)

<p>There should be no difference at all. Could you post a screenshot that shows what difference you see between results of different methods?</p>

---

## Post #3 by @Queen_Rei (2020-06-10 16:10 UTC)

<p>The original STL is: 347 MB<br>
In essence I would like to replicate this manual process in a module:</p>
<ol>
<li>Import STL as segmentation<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8e5ae6352058a66375571a4cf830ce414c7f2727.png" alt="image" data-base62-sha1="kjkyc8yi4osM4XGyl5lo06sxCYf" width="320" height="145"></li>
<li>Export the segmentation as a OBJ<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e26f3e44b73ba2d0233c3a95bb8f61d674fc9f0c.png" alt="image" data-base62-sha1="wj8ff4ePj879KMexnwVnaCp25SA" width="520" height="339"><br>
<strong>Output OBJ’s look like this</strong><br>
Manual STL-&gt;Segmentation-&gt;OBJ: 316 MB<br>
Script STL-&gt;Segmentation-&gt;OBJ: 288 MB</li>
</ol>
<p>I am wondering why the sizes may be different between the manual process and the script.</p>

---

## Post #4 by @lassoan (2020-06-10 16:54 UTC)

<p>Probably the difference is that you set size scale of 0.005 on the GUI. Since OBJ is a text-based format, if you change the scale then coordinate values may be longer/shorter (“5” is shorter than “0.005”).</p>
<p>Why did you set scale to 0.005 on the GUI? Normally you should set it to 1.0 (to export in mm), but you can change it if you want to export in meters or inches - but 0.005 does not seem to correspond to any commonly used distance unit.</p>

---

## Post #5 by @Queen_Rei (2020-06-10 17:15 UTC)

<p>Ohh! My apologies, I completely overlooked how that may be effecting it. I set it to 0.005 thinking it would scale it down (it is arbitrary, since I was just testing it out earlier - didn’t think it would effect the file size). Based on what you are saying it makes most sense to just keep it at 1mm, so I will do so.</p>
<p>Always appreciated! Hope you and your family/friends have been safe &lt;3</p>

---
