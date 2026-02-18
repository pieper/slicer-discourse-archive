# How to export segment by LPS coordinate system?

**Topic ID**: 32391
**Date**: 2023-10-24
**URL**: https://discourse.slicer.org/t/how-to-export-segment-by-lps-coordinate-system/32391

---

## Post #1 by @derekcbr (2023-10-24 03:25 UTC)

<p>Is there api to export segment by LPS?</p>
<pre><code class="lang-python">          # Get segmentation node (replace 'Segmentation' with the name of your segmentation node in the scene)
            segmentation_node = slicer.util.getNode('Segmentation')


            # get the segmentation
            segmentation = segmentation_node.GetSegmentation()

            # get all segment IDs
            segment_ids = vtk.vtkStringArray()
            segmentation.GetSegmentIDs(segment_ids)

            
            segment_id = segment_ids.GetValue(int(mysegmentid) - 1)

            # get the segment
            segment = segmentation.GetSegment(segment_id)

            # now you can work with the individual segment
            print(f"Segment {segment_id} Name: {segment.GetName()}")


            # Export logic
            model_node = slicer.mrmlScene.AddNode(slicer.vtkMRMLModelNode())
            model_node.SetName(segment_id)
            
            # Create a transform to convert from RAS to LPS
            transform_matrix = vtk.vtkMatrix4x4()
            transform_matrix.Identity()
            transform_matrix.SetElement(0, 0, -1)  # Flip the X axis
            transform_matrix.SetElement(1, 1, -1)  # Flip the Y axis
            
            transform_node = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLinearTransformNode')
            transform_node.SetMatrixTransformToParent(transform_matrix)
            
            # Apply the LPS transform to the model node
            model_node.SetAndObserveTransformNodeID(transform_node.GetID())
            
            export_success = slicer.modules.segmentations.logic().ExportSegmentToRepresentationNode(segment, model_node)
</code></pre>
<p>I use this way but not sure whether it works or not?<br>
Thanks!</p>

---

## Post #2 by @lassoan (2023-10-24 18:10 UTC)

<p>RAS to LPS conversion happens when you write the segmentation or model to file. Before that I would recommend to stay in RAS, as the internal representation of all data objects in Slicer is in RAS.</p>

---
