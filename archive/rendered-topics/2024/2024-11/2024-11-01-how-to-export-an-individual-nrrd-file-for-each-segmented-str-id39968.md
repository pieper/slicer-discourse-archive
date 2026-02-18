# How to export an individual .nrrd file for each segmented structure?

**Topic ID**: 39968
**Date**: 2024-11-01
**URL**: https://discourse.slicer.org/t/how-to-export-an-individual-nrrd-file-for-each-segmented-structure/39968

---

## Post #1 by @mitchellwiebe (2024-11-01 00:57 UTC)

<p>Hi there,</p>
<p>I’m working on a project where I will extract features from &gt;200 individuals across several structures (and for CT/dose). As part of the workflow, I feel that it would be most convenient to export a .nrrd file (or .seg.nrrd) for each segmented structure, resulting in as many binary masks as I have structure segmentations. However, when I try to do so, I end up with less masks than total structures (non-overlapping structure are ‘forced’ into the same mask it seems).</p>
<p>I’m sure there’s a nice way to do so but this is giving me trouble! Any advice would be greatly appreciated.</p>

---

## Post #2 by @muratmaga (2024-11-01 02:51 UTC)

<p>If you look into the script repository, there is an example of exporting a labelmap from a named segment:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#export-labelmap-node-from-segmentation-node" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#export-labelmap-node-from-segmentation-node</a></p>
<p>You can loop over segments, and expand this example.</p>

---

## Post #3 by @mitchellwiebe (2024-11-01 21:07 UTC)

<p>Thank you for the response! This was right where I needed to be pointed to.</p>
<p>I put together the lines of code that were of use to me. The final working code is as follows. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<pre><code class="lang-auto"># Loops through all of the existing segmentations and saves them to a file one-by-one (as .nrrd)

# Set output directory
outputPath = r"path\to\savefolder"

def exportEachSegmentAsLabelmap():
    # Get segmentation and reference volume nodes
    segmentationNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLSegmentationNode")
    referenceVolumeNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLScalarVolumeNode")
    segmentationNode.GetSegmentation().CreateRepresentation("BinaryLabelmap")
    
    if not segmentationNode or not referenceVolumeNode:
        print("Segmentation or reference volume node not found.")
        return
    
    # List of segment names you want to export
    segmentNames = list(segmentationNode.GetSegmentation().GetSegmentIDs())
    
    # Iterate over each segment name
    for segmentName in segmentNames:
        print(f"Exporting segment: {segmentName}")
        
        # Get segment ID by name
        segmentId = segmentationNode.GetSegmentation().GetSegmentIdBySegmentName(segmentName)
        
        if not segmentId:
            print(f"Segment {segmentName} not found.")
            continue
        
        # Create a vtkStringArray and add the current segment ID
        segmentIds = vtk.vtkStringArray()
        segmentIds.InsertNextValue(segmentId)
        
        # Create a new labelmap volume node for the export
        labelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLabelMapVolumeNode")
        
        # Export the segment to the labelmap
        slicer.vtkSlicerSegmentationsModuleLogic.ExportSegmentsToLabelmapNode(
            segmentationNode, segmentIds, labelmapVolumeNode, referenceVolumeNode
        )
        
        # Define file path and save each labelmap with the segment name
        filepath = os.path.join(outputPath, f"{segmentName}-label.nrrd")
        slicer.util.saveNode(labelmapVolumeNode, filepath)
        
        # Clean up labelmap node from the scene
        slicer.mrmlScene.RemoveNode(labelmapVolumeNode)
        
        print(f"Segment {segmentName} saved to {filepath}")

# Run the export function directly
exportEachSegmentAsLabelmap()
</code></pre>

---
