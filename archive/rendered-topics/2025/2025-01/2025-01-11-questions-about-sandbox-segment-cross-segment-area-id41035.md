# Questions about Sandbox/Segment Cross-segment Area

**Topic ID**: 41035
**Date**: 2025-01-11
**URL**: https://discourse.slicer.org/t/questions-about-sandbox-segment-cross-segment-area/41035

---

## Post #1 by @Magnus_Wiman (2025-01-11 00:08 UTC)

<p>Hello. I´m an absolute newbie to Slicer so forgive me if my questions are a bit daft.<br>
I found 3D Slicer by chance searching for a solution to a problem I have.<br>
We have a lot of different  cylindrical “connectors” that we need to spot weld in place. In an effort to pre select welding parameters, and to find possible troublesome connectors, I´m trying to estimate the total resistivity of all our connectors (hundreds of different) and one way I found to do that is to calculate the average cross section area through the components z-axis and then divide the total height of the components with this average area.<br>
Enter 3D Slicer…<br>
I found that the module Segment Cross-section Area gives me a table with the area of a bunch of slices if used on our STL-files. This table I copy to excel for further calculations.<br>
Now, a few questions.</p>
<p>If I do this on components with the same height but different diameters I seem to get different amount of rows in the table. I guess based of it being sliced in different slice thickness? What sets this “thickness”? Can I set it somehow?<br>
I open the STL-file by drag and drop and then state “Segmentation” in the pop-up.</p>
<p>I have a lot of these models to analyze. Is it possible to do it in batch?<br>
Preferably with the average slice area of each file as the only output.</p>
<p>Thank you in advance!</p>

---

## Post #2 by @Magnus_Wiman (2025-01-14 10:06 UTC)

<p>Hello again.<br>
I started to do some learning by trail and error in Python Console.<br>
Managed to select module by:<br>
<em>slicer.util.selectModule(“SegmentCrossSectionArea”)</em><br>
and then load my stl-file by:<br>
<em>segmentNode = slicer.util.loadSegmentation(r"C:\Swep\00070105.ipt.stl")</em><br>
Now, trying to actually execute the module, I got stuck:<br>
<em>slicer.util.getModuleLogic(‘SegmentCrossSectionArea’).run(segmentNode, “None”, “slice”, “Create”, “Create”)</em><br>
Following the error I found that it probably misses a table and a chart to put the result in but I´m very new to python and do not have a clue on how to create those.<br>
If someone could point me in the right direction, maybe have some example to refer to, I would be very thankful!</p>

---

## Post #3 by @Magnus_Wiman (2025-01-15 12:32 UTC)

<p>Oh, well.<br>
After quite a bit of trial and error I got where I wanted.</p>
<blockquote>
<p>slicer.util.selectModule(“SegmentCrossSectionArea”)<br>
segmentNode = slicer.util.loadSegmentation(r"C:\Anslutningar STL\00070105.ipt.stl")<br>
tableNode =  slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLTableNode”)<br>
chartNode = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLPlotChartNode”)<br>
slicer.util.getModuleLogic(‘SegmentCrossSectionArea’).run(segmentNode, None, “slice”, tableNode, chartNode)<br>
slicer.util.getModuleLogic(‘SegmentCrossSectionArea’).showTable(tableNode)<br>
numCols = tableNode.GetNumberOfColumns()<br>
numRows = tableNode.GetNumberOfRows()<br>
print("Number of Columns: ", numCols)<br>
print("Number of Rows: ", numRows)<br>
print("First Row: ", tableNode.GetCellText(0,2))<br>
print("Last Row: ", tableNode.GetCellText(numRows-1,2))</p>
<p>sumAv = 0.0<br>
for x in range(numRows):<br>
sumAv = sumAv + float(tableNode.GetCellText(x,2))</p>
<p>AverageArea = sumAv/(numRows)<br>
print("Sum Area: ", sumAv)<br>
print("Average Area: ", AverageArea)</p>
</blockquote>
<p>But I still wonder if I could state the thickness of the segments/slices and thus set how many rows my table will get, somehow?<br>
Also I wonder if I can preview my posts before posting them…?</p>

---

## Post #4 by @cpinter (2025-01-22 12:13 UTC)

<p>Sorry for the long wait! Interesting project.</p>
<aside class="quote no-group" data-username="Magnus_Wiman" data-post="2" data-topic="41035">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/magnus_wiman/48/79071_2.png" class="avatar"> Magnus_Wiman:</div>
<blockquote>
<p>segmentNode = slicer.util.loadSegmentation(r"C:\Swep\00070105.ipt.stl")</p>
</blockquote>
</aside>
<p>It would really help if you could share one of these STL files so that I can try your script and see where we are at.</p>
<p>Great progress from an “absolute newbie”! I am happy to help with this, but let’s have a concrete case I can try and you can approve the results for.</p>
<p>Thanks for your patience. The whole community is preparing for the project week (next week) and the new 5.8 release so support is a bit slower I guess.</p>

---

## Post #5 by @Magnus_Wiman (2025-01-23 12:14 UTC)

<p>Thank you <a class="mention" href="/u/cpinter">@cpinter</a>!<br>
I understand there can be periods of low activity in these kind of forums. No problem!<br>
But I have come a long way. Now my script can scan a whole folder and iterate through all STL-files in there, building a new table with the information I need. Next step will be to export that table to a file (in a format I have yet not decided…).</p>
<p>I still wonder about the difference in number of rows between STL-files even though the height (z-axis) is the same.<br>
But it is not a big issue, I have concluded, as there is normally enough rows to get a average with descent accuracy.</p>
<p>I am not allowed to share our models (STL). What I could do is to make rough dummies of models that will behave the same.<br>
But I do not know what is the best way to share them as the upload function in this system does not allow STL-files.</p>

---

## Post #6 by @Magnus_Wiman (2025-01-23 12:17 UTC)

<p>I have also noticed that if I copy the code I posted from here into the Python Console it will not work as several characters will be misinterpreted…<br>
But I guess you guys already now that.</p>

---

## Post #7 by @cpinter (2025-01-23 13:38 UTC)

<aside class="quote no-group" data-username="Magnus_Wiman" data-post="5" data-topic="41035">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/magnus_wiman/48/79071_2.png" class="avatar"> Magnus_Wiman:</div>
<blockquote>
<p>I am not allowed to share our models (STL). What I could do is to make rough dummies of models that will behave the same.</p>
</blockquote>
</aside>
<p>That would be great too, the point is to have a case to try it on!</p>
<p>Normally we share using our own drives, everyone these days has some online storage…</p>
<aside class="quote no-group" data-username="Magnus_Wiman" data-post="6" data-topic="41035" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/magnus_wiman/48/79071_2.png" class="avatar"> Magnus_Wiman:</div>
<blockquote>
<p>I have also noticed that if I copy the code I posted from here into the Python Console it will not work as several characters will be misinterpreted…<br>
But I guess you guys already now that.</p>
</blockquote>
</aside>
<p>I don’t yet understand this, but once being able to try, maybe I’ll see.</p>

---

## Post #8 by @Magnus_Wiman (2025-01-23 14:00 UTC)

<p>Ok. Lets try!<br>
<a href="https://drive.google.com/file/d/1WBedN6w0_GJJjo6oNmtFma2i4H2o81iG/view?usp=drive_link" rel="noopener nofollow ugc">Dummy File 1</a><br>
<a href="https://drive.google.com/file/d/1_mlZZA_fL-keTwCyvQ2DYdILkigralkm/view?usp=drive_link" rel="noopener nofollow ugc">Dummy File 2</a></p>
<p>Don´t bother with script at this point.<br>
If File 1 is dragged and dropped into Slicer, Loaded as Segmentation, and Module Segment Cross-section Area is run, it  will get a table with 258 rows.<br>
If File 2 is used, the table will get 158 rows.<br>
Segmentation is done in Z-axis, as I can understand, and both models has the same height of 22 mm.</p>
<p>See if you get access to the files, and come back if not.<br>
Thank you!</p>

---

## Post #9 by @cpinter (2025-01-23 14:07 UTC)

<p>Thanks a lot! It might take me a good while until I can actually try, but I have an idea based on this description.</p>
<aside class="quote no-group" data-username="Magnus_Wiman" data-post="8" data-topic="41035">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/magnus_wiman/48/79071_2.png" class="avatar"> Magnus_Wiman:</div>
<blockquote>
<p>Loaded as Segmentation</p>
</blockquote>
</aside>
<p>If you do this without specifying geometry, the default image geometry will be used (1mm x 1mm x 1mm).<br>
After loading it as segmentation, first make sure that the default representation is Closed surface. This means that the Representations section in the Segmentations module (not Segment Editor) looks like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/67565000f15093f8ff78b56ab6eff0d30583f3ee.png" data-download-href="/uploads/short-url/eKa6ozdv5nFna9phqSS8Z8MIQSG.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/67565000f15093f8ff78b56ab6eff0d30583f3ee.png" alt="image" data-base62-sha1="eKa6ozdv5nFna9phqSS8Z8MIQSG" width="294" height="134"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">294×134 2.72 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If so, click on the advanced conversion (arrow next to create) in the row of Binary labelmap, you can specify the geometry. Here you can exactly give the slice thickness, i.e. the distance of the per-slice evaluation.</p>

---

## Post #10 by @Magnus_Wiman (2025-01-24 08:42 UTC)

<p>You seem to be absolutely right <a class="mention" href="/u/cpinter">@cpinter</a> (of course…)!<br>
Changing the last spacing (z-axis I guess) to 0,1 mm gives me the result I want.<br>
Exact 220 rows when height is 22 mm.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c2aae98fa9fca886f9e9354f685ad550bced26ec.jpeg" data-download-href="/uploads/short-url/rM6O3cyDb6cmBAktX0ycfT2oiyE.jpeg?dl=1" title="Segment Geometry" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c2aae98fa9fca886f9e9354f685ad550bced26ec.jpeg" alt="Segment Geometry" data-base62-sha1="rM6O3cyDb6cmBAktX0ycfT2oiyE" width="487" height="364"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Segment Geometry</span><span class="informations">487×364 24.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Now, how can I implement this by script?<br>
Can I set this some how before Load as Segmentation?<br>
Or do I have to do a conversion after each loaded model, some how?<br>
Is it even possible?</p>
<p>Thank you again!</p>

---

## Post #11 by @cpinter (2025-01-24 11:13 UTC)

<p>Yes it is possible. Unfortunately I cannot help with an actual script right now (all day meetings, next week the Slicer project week that we are organizing).</p>
<p>But here’s some sample code that may help you get started:</p>
<pre><code class="lang-auto">slicer.vtkSlicerSegmentationsModuleLogic.ImportModelToSegmentationNode(modelNode, segmentationNode)
# Set computed reference image geometry to the segmentation
extent = [0, 1, 0, 1, 0, 1]  # Arbitrary extent
geometryString = slicer.vtkSegmentationConverter.SerializeImageGeometry(referenceGeometryMatrix, extent)
segmentationNode.GetSegmentation().SetConversionParameter(
  slicer.vtkSegmentationConverter.GetReferenceImageGeometryParameterName(), geometryString)
# Use geometry to convert to binary labelmap
segmentationNode.CreateBinaryLabelmapRepresentation()
# Set binary labelmap representation as source
segmentationNode.SetSourceRepresentationToBinaryLabelmap()
</code></pre>

---

## Post #12 by @Magnus_Wiman (2025-02-03 08:21 UTC)

<p>Thank you!<br>
This one was a bit harder to get into my head… And I still don´t understand all of it.</p>
<blockquote>
<p>extent = [0, 1, 0, 1, 0, 1]  # Arbitrary extent</p>
</blockquote>
<p>Arbitrary is in my world, as an engineer, regarded as a curse… <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=12" title=":wink:" class="emoji" alt=":wink:" loading="lazy" width="20" height="20"><br>
What does those six numbers do or represent?<br>
Anyway, I got it to work the way I wanted. By taking a shortcut, going directly to:</p>
<blockquote>
<p>geometryString = “0.1;0;0;0;0;0.1;0;0;0;0;0.1;0;0;0;0;0.1;0;1;0;1;0;1;”</p>
</blockquote>
<p><img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji only-emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>

---

## Post #13 by @cpinter (2025-02-03 10:19 UTC)

<aside class="quote no-group" data-username="Magnus_Wiman" data-post="12" data-topic="41035">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/magnus_wiman/48/79071_2.png" class="avatar"> Magnus_Wiman:</div>
<blockquote>
<p>What does those six numbers do or represent?</p>
</blockquote>
</aside>
<p>It is the extent in format [xMin, xMax, yMin, yMax, zMin, zMax]. Arbitrary initialization is fine because it will be automatically calculated based on the origin and the labelmap content (only the region of the image data is allocated that contains non-background).</p>

---
