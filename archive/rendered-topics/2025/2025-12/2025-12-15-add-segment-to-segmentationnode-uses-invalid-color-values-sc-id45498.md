# Add Segment to SegmentationNode uses invalid color values (scalar) and adds a new colortable node

**Topic ID**: 45498
**Date**: 2025-12-15
**URL**: https://discourse.slicer.org/t/add-segment-to-segmentationnode-uses-invalid-color-values-scalar-and-adds-a-new-colortable-node/45498

---

## Post #1 by @baderstine (2025-12-15 18:00 UTC)

<p>Summary:</p>
<p>I am attempting to import/edit/export segmentations from numpy to slicer to numpy.  I am using custom color tables but am getting invalid color IDs on export after a segment has been added.</p>
<p>For example, my color table file defines 118 colors from IDs 0 to 117.  I load a segmentation, set the color node to my loaded color file, then when I add a new segment in Segment Editor to that segmentation node, I select the appropriate color for it from the loaded terminology. However, on export the newly added segment has segment ID 118, not the correct value that would be found on lookup in either the terminology JSON file or the color table node.  I noticed that in the All nodes tab of slicer a new color table node now exists with name <code>[segmentation node name]</code>_ColorTable and that new colortablenode contains an extra segment with ID 118 and the name from the terminology file.  So rather than using the color table node that I’ve defined it’s just making one up.  I’m using the code found here - <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#import-export-labelmap-node-using-custom-label-value-mapping" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a> - for importing/exporting but it doesn’t seem to be working as I would expect?  Is there some extra python code that I need to include to ensure that segments added to an existing segmentationnode use that node’s assigned colortablenode for name/id lookups?</p>

---

## Post #2 by @baderstine (2025-12-15 20:16 UTC)

<p>Here is some code:</p>
<p>Within my slicer extension Widget class I load a custom terminology file:</p>
<pre data-code-wrap="python"><code class="lang-python">path = self.resourcePath("Terminologies/[terminology filename].json")
tlogic = slicer.modules.terminologies.logic()
tlogic.LoadTerminologyFromFile(path)
</code></pre>
<p>Within my slicer extension module’s [Module]Lib folder [name].py file:</p>
<p>This is the code that loads a numpy array into a labelmapvolume, assigns the custom color table, and then imports the labelmapvolume node into a segmentationnode using a custom terminology file (which matches the custom color table).</p>
<pre data-code-wrap="python"><code class="lang-python"># load numpy array into slicer node: 
vol, affine = getvol(...) # loads numpy arrays for labels and affine transform

name = 'myNumpyImportNode'
nodetype = "vtkMRMLLabelMapVolumeNode"
arraytype = vtk.VTK_INT

node = slicer.mrmlScene.AddNewNodeByClass(nodetype, name)

vtkArray = vtk.util.numpy_support.numpy_to_vtk(
    num_array=vol.ravel('F'), deep=True, array_type=arraytype
)
image = vtk.vtkImageData()
image.SetDimensions(vol.shape)
image.GetPointData().SetScalars(vtkArray)
# Set the volume node's "image" data
node.SetAndObserveImageData(image)
transformMatrix = vtk.vtkMatrix4x4()
for i in range(4):
    for j in range(4):
        transformMatrix.SetElement(i, j, affine[i, j])
node.SetIJKToRASMatrix(transformMatrix)        

color_table_node = slicer.util.loadColorTable([color_file.txt])
color_table_node.SetNumberOfColors(num_colors)

node.CreateDefaultDisplayNodes()
node.GetDisplayNode().SetAndObserveColorNodeID(color_table_node.GetID())

# import to segmentation node and apply terminology (which matches color table node in terms of Segment ID:Name lookups) 
seg_node = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
slicer.modules.segmentations.logic().ImportLabelmapToSegmentationNodeWithTerminology(node, seg_node, [terminology name])
</code></pre>
<p>Is it bad practice to import the labelmap with terminology here since a colortable has already been defined?  The colortable and terminology files match in terms of id:segment name lookups.</p>
<p>&lt;Edit the segmentation node using SegmentEditor, add a segment, assign segment name by double-clicking on the new segment color box to bring up the Terminology selector, select the correct terminology for the new segment, close. assign some pixels to that segment.&gt;</p>
<p>This is the code that saves the edited segmentation node back to numpy:</p>
<pre data-code-wrap="python"><code class="lang-python">seg_node = slicer.util.getNode([name of edited segmentation node])
# lbl_node.GetClassName() == 'vtkMRMLSegmentationNode'
vol_name = lbl_node.GetName()
tmp_node = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLabelMapVolumeNode")
&lt;re-load the original, unedited numpy array into a reference node&gt; 
ref_node = slicer.util.getNode([name of unedited labelmapvolume node])

ctb_node = seg_node.GetDisplayNode().GetColorNode()
segmentIds = seg_node.GetSegmentation().GetSegmentIDs()
slicer.modules.segmentations.logic().ExportSegmentsToLabelmapNode(seg_node, segmentIds, tmp_node, ref_node, slicer.vtkSegmentation.EXTENT_REFERENCE_GEOMETRY, ctb_node)
# ExportSegmentsToLabelmapNode() adds a new (unnecessary) color table node to the list of nodes with name [name of edited segmentation node]_ColorTable. This colortablenode contains an incorrect lookup value for the new class. 

tmp_node.GetDisplayNode().GetColorNode().GetName() # the color table node assigned to the exported labelmapvolume node is this new color table node not the one passed to the export function. 

# convert to num_py arrays
tmp_array = slicer.util.arrayFromVolume(tmp_node)
ref_array = slicer.util.arrayFromVolume(ref_node)

# check the contents: 
tmp_vals, tmp_cnts = np.unique(tmp_array,return_counts=True)
ref_vals, ref_cnts = np.unique(ref_array,return_counts=True)
</code></pre>
<p>It is unclear why an additional ColorTableNode is created by <code>ExportSegmentsToLabelmapNode()</code>.  This new (seemingly unnecessary) color table node is added to the list of nodes in the “All nodes” tab of the Data module with name [name of edited segmentation node]_ColorTable.</p>
<p><code>tmp_vals</code> contains one additional segment ID value for the added segment.  Ideally this value should match the ID that is found for that segment name/color record in the terminology/color table file. i.e., if i added ‘blah’ segment name corresponding to ID = 8 in the color file then the new ID added should be 8.  Sometimes the new ID is 8 and sometimes it is assigned the value n+1 where where n is the max ID found in the color table file.  Based on this function: <a href="https://github.com/Slicer/Slicer/blob/294f0baf9ad23ed1e7ebf96f2ff3bb15fda12f3c/Modules/Loadable/Segmentations/Logic/vtkSlicerSegmentationsModuleLogic.cxx#L2494" rel="noopener nofollow ugc">https://github.com/Slicer/Slicer/blob/294f0baf9ad23ed1e7ebf96f2ff3bb15fda12f3c/Modules/Loadable/Segmentations/Logic/vtkSlicerSegmentationsModuleLogic.cxx#L2494</a> This seems to be the expected behavior when a segment name is not found on lookup. … and now that I’ve tested this theory it is what is causing the problem.  In the Terminology JSON file and the Color Table files, all of my segment names that contain underscores are not found on lookup whereas the ones without underscores are found.  So it seems that the functions <code>vtkSlicerTerminologiesModuleLogic::GetColorIndexByTerminology()</code> and <code>GetColorIndexByName(segmentName)</code> will not successfully find segment IDs if the segment names contain underscores in the color table or terminology file.  If so, then this seems like a bug.</p>
<p>I’m using the original colortable file formatting (.txt file) where underscores in the segment names are required due to the use of spaces as separators.  I believe that these underscores are getting incorrectly stripped out during the segment name:ID lookup because (a) the segmentation node segment names DO NOT contain underscores, (b) the Terminology modal for selecting a segment name for the new segment DOES contain underscores, (c) the segmentation node segment name for the newly added segment DOES contain underscores if they were there in the first place, (d) the color table file and terminology files both contain underscores for some segment names, (e) only the segment names containing underscores fail the lookup.</p>
<p>I can think of a few work-arounds for this:</p>
<ol>
<li>switch to the new CSV format of color table file which allows spaces in the segment names</li>
<li>update my terminology JSON file to replace underscores with spaces as this file has no restriction on the use of spaces in segment names.</li>
</ol>
<p>but I suspect you want the segment name to ID lookup to work even if the segment names contain underscores in the source terminology and/or color table files?</p>

---

## Post #3 by @baderstine (2025-12-15 21:16 UTC)

<aside class="quote no-group" data-username="baderstine" data-post="2" data-topic="45498">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/baderstine/48/79333_2.png" class="avatar"> baderstine:</div>
<blockquote>
<p><code>ExportSegmentsToLabelmapNode(seg_node, segmentIds, tmp_node, ref_node, slicer.vtkSegmentation.EXTENT_REFERENCE_GEOMETRY, ctb_node)</code></p>
</blockquote>
</aside>
<p>I can confirm that updating the terminology JSON file to replace underscores with spaces does seem to fix the failed lookup.</p>

---

## Post #4 by @lassoan (2025-12-16 01:48 UTC)

<p>Please use the new standard .csv file based format. The old custom txt format used space as separator between columns, so space in color name was replaced by underscores, so underscores were converted to spaces. You don’t have this limitation if you use the new format.</p>
<p>I would also recommend to use standard terminology in the color table file. If terminology is set then matching will be done based on standard codes. It is much more reliable than a simple string comparison, where spelling, capitalization, typos, etc. differences (which are particularly common when you aggregate data from multiple sites or from multiple operators) may prevent matching of segments.</p>
<p><code>ExportSegmentsToLabelmapNode</code> always creates a new color table because you need a way to verify if there were any segments that were not present in the <code>exportColorTable</code> that you provided. After you completed all your checks that you wanted to do, you can remove the color table by a single <code>slicer.mrmlScene.RemoveNode</code> call. If this API is inconvenient then we could add a flag or a new variant of <code>ExportSegmentsToLabelmapNode</code>, which would require the <code>exportColorTable</code> and would return with failure if a segment was not found in the <code>exportColorTable</code>. This varian would not need to create a new color table node, it would just assign <code>exportColorTable</code> to the exported labelmap node.</p>

---

## Post #5 by @baderstine (2026-01-03 16:45 UTC)

<p>Thanks it makes sense that the old format would replace underscores but it wasn’t clear and obvious to me that this was happening behind the scenes. Switching to the new csv format and ensuring that the segment names in the csv and the names in the terminology json file matched worked out perfectly.</p>
<p>Some of the segments that I’m using from totalsegmentator “total” model have underscores in the names so that’s unavoidable for now. For what it’s worth, I think it would be useful to throw a warning into the python console if the color table lookup fails to find a segment name/color and the n+1 value is assigned as that was unexpected, non-obvious behavior. Thanks for everything that you all do.</p>

---

## Post #6 by @lassoan (2026-01-03 23:28 UTC)

<aside class="quote no-group" data-username="baderstine" data-post="5" data-topic="45498">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/baderstine/48/79333_2.png" class="avatar"> baderstine:</div>
<blockquote>
<p>Some of the segments that I’m using from totalsegmentator “total” model have underscores in the names</p>
</blockquote>
</aside>
<p>Is this still causing any problem, even if you don’t use the old color table file format?</p>
<p>Do you use TotalSegmentator module in Slicer? That should import the segmentation results correctly (with reasonable names and colors and standard terminology codes).</p>

---
