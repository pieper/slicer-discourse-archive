---
topic_id: 43190
title: "Incorrect Values When Converting Segmentation To Binary Labe"
date: 2025-06-02
url: https://discourse.slicer.org/t/43190
---

# Incorrect values when converting segmentation to binary labelmap

**Topic ID**: 43190
**Date**: 2025-06-02
**URL**: https://discourse.slicer.org/t/incorrect-values-when-converting-segmentation-to-binary-labelmap/43190

---

## Post #1 by @JASON (2025-06-02 18:11 UTC)

<p>I have noticed that converting a segmentation to binary labelmap causes all label values to be remapped from their current value to the segment’s index (1 … n+1).</p>
<p>This is true for UI option “<code>Export visible segments to binary labelmap</code>”, as well as python method <code>slicer.modules.segmentations.logic().ExportAllSegmentsToLabelmapNode</code>.</p>
<p>Is there a way to create a labelmap from segmentation with the correct values?</p>

---

## Post #2 by @muratmaga (2025-06-02 20:44 UTC)

<p>That’s because in labelmaps 0 is reserved for background. So indexing starts at 1.</p>

---

## Post #3 by @JASON (2025-06-02 20:55 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> background label value is 0 in both the source segmentation and in the output labelmap, but the issues I’m facing is the non-zero label values are remapped to segment index.</p>
<p>In my case I’m using the segmentation in an AI workflow where labelmap values have semantic meaning. Opening, modifying, and saving the seg.nrrd will maintain the same segment values, but attempts to operate on the labelmap will alter the segment values.</p>

---

## Post #4 by @muratmaga (2025-06-02 20:59 UTC)

<p>If you want your segment names to map consistently to same values as labelmaps, you should create a color table, and specify that during the segment-&gt;labelmap conversion (use segmentations module, not the right-click one).</p>
<p>Here is an older example. <a href="https://github.com/SlicerMorph/SlicerMEMOS/blob/main/MEMOS/Resources/Support/KOMP2.ctbl" class="inline-onebox" rel="noopener nofollow ugc">SlicerMEMOS/MEMOS/Resources/Support/KOMP2.ctbl at main · SlicerMorph/SlicerMEMOS · GitHub</a></p>
<p>(you should really use the new csv based color table, which doesn’t have the issues associated with this older format).</p>

---

## Post #5 by @JASON (2025-06-02 22:02 UTC)

<p>OK, I can create and apply a color table from the existing values, and then get the correct values from <code>segNode.GenerateMergedLabelmapForAllSegments()</code>.</p>
<p>— Create Color table</p>
<pre><code class="lang-auto">def ColorTableFromSegmentation(segNode, tableName="SegmentationColorTable"):
    segmentation = segNode.GetSegmentation()

    colorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLColorTableNode", tableName)
    colorNode.SetTypeToUser()
    colorNode.HideFromEditorsOff()

    maxLabel = 0
    for segId in segmentation.GetSegmentIDs():
        seg = segmentation.GetSegment(segId)
        lv = int(seg.GetLabelValue())
        if lv &gt; maxLabel:
            maxLabel = lv
    colorNode.SetNumberOfColors(maxLabel + 1)

    for segId in segmentation.GetSegmentIDs():
        seg = segmentation.GetSegment(segId)
        name       = seg.GetName()
        labelValue = int(seg.GetLabelValue())
        (r, g, b)  = seg.GetColor()

        Ri = int(round(r * 255))
        Gi = int(round(g * 255))
        Bi = int(round(b * 255))
        Ai = 255

        colorNode.SetColor(labelValue, Ri, Gi, Bi, Ai)
        colorNode.SetColorName(labelValue, name)

    return colorNode

</code></pre>
<p>— Apply Color table</p>
<pre><code class="lang-auto">ct = ColorTableFromSegmentation(segNode)
segNode.SetLabelmapConversionColorTableNodeID( ct.GetID() )
</code></pre>
<p>— Create labelmap with ConversionColorTable applied</p>
<pre><code class="lang-auto">import slicer
import vtk
import os
import tempfile
import numpy as np
from vtk.util import numpy_support

def SegNode_to_Labelmap(segNode, volNode):
    segmentation = segNode.GetSegmentation()
    mergedImageData = slicer.vtkOrientedImageData()
    extent = slicer.vtkSegmentation.EXTENT_REFERENCE_GEOMETRY
    segIDs = vtk.vtkStringArray()
    segVals = vtk.vtkIntArray()
    for segTemp in AtlasTemplate.brainTemplate_99:
        segIDs.InsertNextValue(segTemp['name'])
        segVals.InsertNextValue(int(segTemp['value']))

    success = segNode.GenerateMergedLabelmapForAllSegments(mergedImageData, extent, None, segIDs, segVals)

    print("GenerateMergedLabelmap success:", success)

    if success:
        labelmapNode = slicer.mrmlScene.AddNewNodeByClass( "vtkMRMLLabelMapVolumeNode", "Merged_Labelmap" )
        labelmapNode.SetAndObserveImageData(mergedImageData)

        #print unique values in mergedImageData
        scalars = mergedImageData.GetPointData().GetScalars()
        npArray = numpy_support.vtk_to_numpy(scalars)
        uniqueValues = np.unique(npArray)
        print("values:", uniqueValues)
        return labelmapNode
     else:
         return None
</code></pre>
<p>This prints a list of the correct values, however when I hover over the labelmap, I stream of errors:<br>
<code>[VTK] GetScalarIndex: Pixel (26, 0, 22) not in memory. [VTK]  Current extent= (12, 190, 15, 223, 17, 187)</code></p>
<p>Also, the labelmap doesn’t use the colors from the color table, yet the correct colors are applied if I do NOT apply the color table.</p>

---

## Post #6 by @JASON (2025-06-02 22:05 UTC)

<p>In my opinion, maintaining the correct label values should be the default behavior when converting the labelmap.</p>
<p>I do find that simply importing the seg.nrrd files as volume (instead of segmentation) will result in the correct label values being respected.</p>
<p>This feels very hacky, but this is the best solution I have so far…</p>
<pre><code class="lang-auto">def SegNode_to_LabelmapArray(segNode):
    fd, tempPath = tempfile.mkstemp(suffix=".seg.nrrd")
    os.close(fd)

    try:
        slicer.util.saveNode(segNode, tempPath)
        volumeNode = slicer.util.loadVolume(tempPath)
        os.remove(tempPath)
        labelArray = slicer.util.arrayFromVolume(volumeNode)

        uniqueLabels = np.unique(labelArray)
        print("Unique label values in merged labelmap:", uniqueLabels)

        #remove volumeNode from scene
        slicer.mrmlScene.RemoveNode(volumeNode)

        return labelArray

    except Exception as e:
        if os.path.exists(tempPath):
            os.remove(tempPath)
        raise
</code></pre>

---

## Post #7 by @muratmaga (2025-06-03 03:53 UTC)

<aside class="quote no-group" data-username="JASON" data-post="6" data-topic="43190">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jason/48/13419_2.png" class="avatar"> JASON:</div>
<blockquote>
<p>maintaining the correct label values should be t</p>
</blockquote>
</aside>
<p>Try this:</p>
<ol>
<li>Create a segmentation, with three segments, Segment_1, Segment_2, Segment_3 save it as a segmentation</li>
<li>Create a new segmentation from scratch with two segments: Segment_1, Segment_3</li>
</ol>
<p>Read the values in seg.nrrd with your script. What is the ordinal you get for Segment_3 in both cases? Which one is correct?</p>

---

## Post #8 by @JASON (2025-06-03 16:35 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="7" data-topic="43190">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Try this:</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> I set up a test that illustrates the issue and found an alternate method that maintains the correct values.  Feel free to try this code to replicate results:</p>
<pre><code class="lang-auto">
import slicer
import numpy as np
import vtk
from vtk.util import numpy_support


#--- Create a random labelmap with specified values
sourceValues = [2, 4, 8, 16]
shape = (64, 64, 64)
np_arr = np.random.choice(sourceValues, size=shape).astype(np.int16)
unique_vals = np.unique(np_arr)
print("1.] Source values:", unique_vals)


#--- Convert the numpy array to volume labelmap
flat_arr = np_arr.flatten(order='F')
vtk_arr = numpy_support.numpy_to_vtk(
    num_array=flat_arr,
    deep=True,
    array_type=vtk.VTK_SHORT
)
imageData = vtk.vtkImageData()
imageData.SetDimensions(shape[0], shape[1], shape[2])
imageData.SetSpacing(1.0, 1.0, 1.0)
imageData.GetPointData().SetScalars(vtk_arr)
labelmapNode = slicer.mrmlScene.AddNewNodeByClass( "vtkMRMLLabelMapVolumeNode", "RandomLabelmap")
labelmapNode.SetAndObserveImageData(imageData)
labelmapNode.CreateDefaultDisplayNodes()

#--- Check the values in the labelmap node
volImageData = labelmapNode.GetImageData()
volScalars = volImageData.GetPointData().GetScalars()
vol_np = numpy_support.vtk_to_numpy(volScalars)
unique_vals_vol = np.unique(vol_np)
print("2.] labelmap values:", unique_vals_vol)

#--- Create a segmentation node from the labelmap
segmentationNode = slicer.mrmlScene.AddNewNodeByClass( "vtkMRMLSegmentationNode", "RandomSegmentation" )
segmentationNode.CreateDefaultDisplayNodes()
segmentationLogic = slicer.vtkSlicerSegmentationsModuleLogic()
segmentationLogic.ImportLabelmapToSegmentationNode(labelmapNode, segmentationNode)
segmentation = segmentationNode.GetSegmentation()
print("--- Segmentation Node:")
for segID in segmentation.GetSegmentIDs():
    segment = segmentation.GetSegment(segID)
    labelValue = segment.GetLabelValue()
    segment.SetName(f"value_{labelValue}")
    print(f"seg: {segment.GetName()}  |  value: {labelValue}")


#--- Create a labelmap from the segmentation node : slicer.modules.segmentations.logic().ExportAllSegmentsToLabelmapNode
labelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLabelMapVolumeNode", "labelMap_ExportAllSegments")
slicer.modules.segmentations.logic().ExportAllSegmentsToLabelmapNode(segmentationNode, labelmapVolumeNode, slicer.vtkSegmentation.EXTENT_REFERENCE_GEOMETRY)
#--- extract array from labelmapVolumeNode, print unique values
vol2ImageData = labelmapVolumeNode.GetImageData()
vol2Scalars = vol2ImageData.GetPointData().GetScalars()
vol2_np = numpy_support.vtk_to_numpy(vol2Scalars)
unique_vals_export = np.unique(vol2_np)
print("3.] ExportAllSegmentsToLabelmapNode values:", unique_vals_export)



#--- Create a labelmap from the segmentation node : GenerateMergedLabelmapForAllSegments
mergedImageData = slicer.vtkOrientedImageData()
extent = slicer.vtkSegmentation.EXTENT_REFERENCE_GEOMETRY
segIDsArray = vtk.vtkStringArray()
segValsArray = vtk.vtkIntArray()
for segID in segmentation.GetSegmentIDs():
    segIDsArray.InsertNextValue(segID)
    segValsArray.InsertNextValue(segmentation.GetSegment(segID).GetLabelValue())
success = segmentationNode.GenerateMergedLabelmapForAllSegments(
    mergedImageData,
    extent,
    None,
    segIDsArray,
    segValsArray
)
if success:
    vtk_arr2 = mergedImageData.GetPointData().GetScalars()
    np_arr2 = numpy_support.vtk_to_numpy(vtk_arr2)
    unique_vals2 = np.unique(np_arr2)
    print("4.] GenerateMergedLabelmapForAllSegments values:", unique_vals2)
else:
    print("GenerateMergedLabelmapForAllSegments failed")
</code></pre>
<p>This generates a labelmap from specified non-consecutive values that do not match index.  Then we create a segmentation from the labelmap.  After this I convert the segNode to labelmap using <code>ExportAllSegmentsToLabelmapNode</code> and demonstrate the values are altered.<br>
I also tried the method <code>segmentationNode.GenerateMergedLabelmapForAllSegments</code>, which includes a parameter for the label values.  Using this method, the correct values are preserved.</p>
<p>Output :</p>
<pre><code class="lang-auto">1.] Source values: [ 2  4  8 16]
2.] labelmap values: [ 2  4  8 16]
--- Segmentation Node:
seg: value_2  |  value: 2
seg: value_4  |  value: 4
seg: value_8  |  value: 8
seg: value_16  |  value: 16
3.] ExportAllSegmentsToLabelmapNode values: [1 2 3 4]
4.] GenerateMergedLabelmapForAllSegments values: [ 2  4  8 16]
</code></pre>

---

## Post #9 by @muratmaga (2025-06-03 18:56 UTC)

<aside class="quote no-group" data-username="JASON" data-post="8" data-topic="43190">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jason/48/13419_2.png" class="avatar"> JASON:</div>
<blockquote>
<p>I set up a test that illustrates the issue and found an alternate method that maintains the correct values.</p>
</blockquote>
</aside>
<p>You can of course do what you want to do, but Slicer does manage correct and consistent label indices with the use of color tables. That’s the suggested method.  So it is your call. You can maintain this code, or debug while your other coded didn’t get the labels correctly from the color table.</p>

---

## Post #10 by @JASON (2025-06-03 19:17 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="9" data-topic="43190">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>consistent label indices</p>
</blockquote>
</aside>
<p>I have confirmed that creating &amp; applying color table using <code>segNode.SetLabelmapConversionColorTableNodeID</code> does <strong>NOT</strong> result in the correct label values being maintained when using UI option <code>Export visible segments to binary labelmap</code> or API method <code>slicer.modules.segmentations.logic().ExportAllSegmentsToLabelmapNode</code>.  In both of these cases, setting the color table has no affect on the output labelmap and the values are remapped to index, just as they are when no color table is applied.</p>
<p>In my testing, I found only 2 ways to maintain the correct values :<br>
1.] Save &amp; Load the seg.nrrd as a volume<br>
2.] Use <code>segmentationNode.GenerateMergedLabelmapForAllSegments</code> with the values array supplied.</p>

---

## Post #11 by @pieper (2025-06-03 19:26 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> can you comment on this?  It’s clearly very important for general interfacing purposes to have everything working cleanly and meeting expectations.</p>

---

## Post #12 by @muratmaga (2025-06-03 20:08 UTC)

<aside class="quote no-group" data-username="JASON" data-post="10" data-topic="43190">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jason/48/13419_2.png" class="avatar"> JASON:</div>
<blockquote>
<p>I have confirmed that creating &amp; applying color table using <code>segNode.SetLabelmapConversionColorTableNodeID</code> does <strong>NOT</strong> result in the correct label values being maintained when using UI option <code>Export visible segments to binary labelmap</code> or API method</p>
</blockquote>
</aside>
<p>I cannot command for programmatic conversion, but this is what I do through the <code>Segmentations</code> module and works all the time.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/57462ef98b5ee324226449e452b377f3614a54a5.png" data-download-href="/uploads/short-url/cs3UfWFekwoGrVzUMzUj7NmtlE9.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/57462ef98b5ee324226449e452b377f3614a54a5_2_690x393.png" alt="image" data-base62-sha1="cs3UfWFekwoGrVzUMzUj7NmtlE9" width="690" height="393" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/57462ef98b5ee324226449e452b377f3614a54a5_2_690x393.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/57462ef98b5ee324226449e452b377f3614a54a5_2_1035x589.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/57462ef98b5ee324226449e452b377f3614a54a5.png 2x" data-dominant-color="EFEFEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1118×638 47.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #13 by @lassoan (2025-06-03 20:27 UTC)

<p><a class="mention" href="/u/jason">@JASON</a> We designed the color table based terminology selection in the Segment Editor exactly for the use case you describe - to be able to explicitly assign a label value (and label name, color, and terminology) for segmentation stored in a simple labelmap volume. Please test with the GUI first, it should all work well. Once you can complete your full workflow using the GUI, we can help you automate it by Python scripting.</p>

---

## Post #14 by @JASON (2025-06-03 20:32 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="12" data-topic="43190">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p><code>Segmentations</code> module</p>
</blockquote>
</aside>
<p>Thanks, <a class="mention" href="/u/muratmaga">@muratmaga</a> and <a class="mention" href="/u/lassoan">@lassoan</a> I appreciate your feedback. I can successfully get correct values using this method by creating the color table using the code above and manually exporting from Segmentations module as you suggest.</p>
<p>I am looking for a scripted solution here and color table has some drawbacks :</p>
<ul>
<li>my max labelmap value is 10,000, the color table ends up including every possible integer between 0 and 10,000, so the *.ctbl file ends up being larger file size than the segmentation seg.nrdd</li>
<li>manual export creates a *.nii file than needs to be re-imported as volume.  I could more easily just import the source *.seg.nrrd as volume and get the same correct labelmap values without the color table.</li>
</ul>
<p>Working through this, I have found an acceptable API solution, but my humble recommendation to <a class="mention" href="/u/lassoan">@lassoan</a> is consider maintaining label values as the default behavior of <code>Export visible segments to binary labelmap</code> and <code>slicer.modules.segmentations.logic().ExportAllSegmentsToLabelmapNode</code>.</p>

---

## Post #15 by @muratmaga (2025-06-03 20:43 UTC)

<aside class="quote no-group" data-username="JASON" data-post="14" data-topic="43190">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jason/48/13419_2.png" class="avatar"> JASON:</div>
<blockquote>
<p>my max labelmap value is 10,000, the color table ends up including every possible integer between 0 and 10,000, so the *.ctbl file ends up being larger file size than the segmentation seg.nrdd</p>
</blockquote>
</aside>
<p>If you don’t need 10,000 distinct values your color table does not have to contain 10000 values. I can be just 1, 5, 10000 if you want it to be.</p>
<p>However, most deep-learning frameworks I used (e.g., MONAI) is not happy about non-continuous discrete values in the labelmap. We once had a segmentation with gaps in labelmaps and had to reorder the label indices to make them contiguous starting from 0.</p>

---

## Post #16 by @JASON (2025-06-03 20:59 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="15" data-topic="43190">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>you don’t need 10,000 distinct values</p>
</blockquote>
</aside>
<p>The first value in the color table is the index, not the value, so the table has to be a length of maxValue +1.  Try this :</p>
<pre><code class="lang-auto">colorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLColorTableNode")
colorNode.SetTypeToUser()
colorNode.HideFromEditorsOff()

colorNode.SetNumberOfColors(2)
colorNode.SetColor(1, 1, 0, 0, 1)
colorNode.SetColor(10000, 1, 0, 0, 1)
</code></pre>
<p>ERROR:<br>
<code>[VTK] vtkMRMLColorTableNode::SetColor: requested entry 10000 is out of table range: 0 - 2, call SetNumberOfColors</code></p>

---

## Post #17 by @lassoan (2025-06-03 21:09 UTC)

<aside class="quote no-group" data-username="JASON" data-post="14" data-topic="43190">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jason/48/13419_2.png" class="avatar"> JASON:</div>
<blockquote>
<p>my max labelmap value is 10,000, the color table ends up including every possible integer between 0 and 10,000, so the *.ctbl file ends up being larger file size than the segmentation seg.nrdd</p>
</blockquote>
</aside>
<p>Use the latest Slicer Preview Release and the new .csv format. It will not save the undefined colors. That said, it is good to keep the label value range small, as a large color table with lots of gaps may lead to inefficiencies (not just in Slicer but in general).</p>
<aside class="quote no-group" data-username="JASON" data-post="14" data-topic="43190">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jason/48/13419_2.png" class="avatar"> JASON:</div>
<blockquote>
<p>manual export creates a *.nii file than needs to be re-imported as volume. I could more easily just import the source *.seg.nrrd as volume and get the same correct labelmap values without the color table.</p>
</blockquote>
</aside>
<p>NIFTI and raw NRRD export feature is only intended for exporting. That is, when you need to translate your general-purpose segmentation (that identifies segments by standard terminology, segment name, or segment UID) to a project-specific label volume (that identifies segments by label value).</p>
<aside class="quote no-group" data-username="JASON" data-post="14" data-topic="43190">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jason/48/13419_2.png" class="avatar"> JASON:</div>
<blockquote>
<p>Working through this, I have found an acceptable API solution, but my humble recommendation to <a class="mention" href="/u/lassoan">@lassoan</a> is consider maintaining label values as the default behavior of <code>Export visible segments to binary labelmap</code></p>
</blockquote>
</aside>
<p>This is already implemented: when you import a segment from labelmap with a color table mapping then by default the same color table is used when you export. If you don’t want to create an existing color table then a new one is generated during export.</p>
<aside class="quote no-group" data-username="JASON" data-post="16" data-topic="43190">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jason/48/13419_2.png" class="avatar"> JASON:</div>
<blockquote>
<pre><code class="lang-auto">colorNode.SetNumberOfColors(2)
colorNode.SetColor(1, 1, 0, 0, 1)
colorNode.SetColor(10000, 1, 0, 0, 1)
</code></pre>
<p>ERROR:<br>
<code>[VTK] vtkMRMLColorTableNode::SetColor: requested entry 10000 is out of table range: 0 - 2, call SetNumberOfColors</code></p>
</blockquote>
</aside>
<p>Number of colors is 10001. <code>SetColor</code> will define labels <code>1</code> and <code>10000</code>, while all the other table entries will be left undefined. Undefined colors are not written to file and they are only shown in the GUI if <code>Hide empty colors</code> option is unchecked.</p>
<hr>
<p>Everything should work as the user expects and it is clearly not the case now. I’m just wondering how we can change the software (GUI, maybe some logic) or user expectations (by training, documentation) to make the experience better.</p>

---

## Post #18 by @muratmaga (2025-06-03 21:13 UTC)

<p>I can confirm that with this csv color table, things are working as expected for labelmap export (i.e., I get non-continuous labelmap values of 0, 1, 4, 6, 8)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/efd98be9afbc440f66d3776891a0b792bfdcfe92.png" data-download-href="/uploads/short-url/ydOcOHrnQVenRwWRqLkvrcZKj4K.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/efd98be9afbc440f66d3776891a0b792bfdcfe92_2_690x154.png" alt="image" data-base62-sha1="ydOcOHrnQVenRwWRqLkvrcZKj4K" width="690" height="154" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/efd98be9afbc440f66d3776891a0b792bfdcfe92_2_690x154.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/efd98be9afbc440f66d3776891a0b792bfdcfe92_2_1035x231.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/efd98be9afbc440f66d3776891a0b792bfdcfe92.png 2x" data-dominant-color="F0F0F0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1066×238 22.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #19 by @JASON (2025-06-03 21:17 UTC)

<p>Thanks, I’ll check out color tables in the latest Preview Release.</p>
<p>If I had a time machine, I’d go back and use values 1…n, but I’m now maintaining a database of 57,000 segmentations that use <a href="https://surfer.nmr.mgh.harvard.edu/fswiki/FsTutorial/AnatomicalROI/FreeSurferColorLUT" rel="noopener nofollow ugc">the FreeSurfer convention</a>.</p>

---

## Post #20 by @lassoan (2025-06-03 21:35 UTC)

<aside class="quote no-group" data-username="JASON" data-post="14" data-topic="43190">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jason/48/13419_2.png" class="avatar"> JASON:</div>
<blockquote>
<p>Working through this, I have found an acceptable API solution, but my humble recommendation to <a class="mention" href="/u/lassoan">@lassoan</a> is consider maintaining label values as the default behavior of <code>Export visible segments to binary labelmap</code> and <code>slicer.modules.segmentations.logic().ExportAllSegmentsToLabelmapNode</code>.</p>
</blockquote>
</aside>
<p><code>ExportAllSegmentsToLabelmapNode(segmentationNode, labelmapNode, extentComputationMode)</code> is a convenience function, which only accepts a limited set of options. It just calls <code>slicer.modules.segmentations.logic().ExportSegmentsToLabelmapNode(segmentationNode, segmentIDs, labelmapNode, referenceVolumeNode, extentComputationMode, exportColorTable)</code> without specifying a color mapping (<code>exportColorTable</code>).</p>
<p>If we add <code>exportColorTable</code> parameter then we may just as well add the <code>referenceVolumeNode</code> as well and then the <code>ExportAllSegmentsToLabelmapNode</code> becomes about the same as <code>ExportSegmentsToLabelmapNode</code>. Maybe we should deprecate <code>ExportAllSegmentsToLabelmapNode</code> and remove it from the script repository examples?</p>
<p>We have <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#import-export-labelmap-node-using-custom-label-value-mapping">full examples of converting between segmentations to labelmap with custom color mapping</a>, but maybe it is hard to find it among all the other examples or AI chatbots suggest the oversimplified convenience functions.</p>
<p><a class="mention" href="/u/jason">@JASON</a> How did you find the methods that you can use? Reading examples in the script repository, searching the forum, reading the API documentation, asking AI chatbots, …?</p>

---

## Post #21 by @JASON (2025-06-03 22:13 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="20" data-topic="43190">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>How did you find the methods that you can use? Reading examples in the script repository, searching the forum, reading the API documentation, asking AI chatbots, …?</p>
</blockquote>
</aside>
<p>All of the above. I believe I started with the script repo (excellent source of information).<br>
I started with the example of <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#export-labelmap-node-from-segmentation-node" rel="noopener nofollow ugc">ExportAllSegmentsToLabelmapNode</a>, but discovered the values were remapped.</p>
<p>I then check API docs for <a href="https://apidocs.slicer.org/v5.8/classvtkSlicerSegmentationsModuleLogic.html#a1e4cd964c6b4c616a3c79968440b0f0d" rel="noopener nofollow ugc">ExportAllSegmentsToLabelmapNode</a>, but didn’t see anything about values.</p>
<p>While posting to this thread, I found the <a href="https://apidocs.slicer.org/v5.8/classvtkMRMLSegmentationNode.html#ade3e8a38e7c43c5ac511ccae6b3d8153" rel="noopener nofollow ugc">SegmentationNode.GenerateMergedLabelmapForAllSegments</a> method, which includes the ability to supply the label values.  This is currently my preferred method, as it is less steps than creating the color table.</p>
<p>On segmentation import, my module applies a custom color theme to the segments using a python dict that includes segment ID, value, and color.  So I have not used color tables / terminologies and hadn’t considered their use until I saw <a class="mention" href="/u/muratmaga">@muratmaga</a> suggestion.</p>
<p>After that I noticed that the script repository does include <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#export-labelmap-node-from-segmentation-node-using-custom-label-value-mapping" rel="noopener nofollow ugc">ExportSegmentsToLabelmapNode</a>, which uses the color table to provide the values.  This would have also been a fine solution if I had seen it from the beginning.</p>
<p>I didn’t see anything on the forum that had the solution, but I hope this thread is useful to others that run into the issue.</p>

---
