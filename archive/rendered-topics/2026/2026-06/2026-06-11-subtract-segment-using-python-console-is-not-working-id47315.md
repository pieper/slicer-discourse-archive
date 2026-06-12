---
topic_id: 47315
title: " Subtract Segment using python console is not working"
date: 2026-06-11
url: https://discourse.slicer.org/t/47315
last_bumped: 2026-06-11T15:10:32.159Z
---

#  Subtract Segment using python console is not working

**Topic ID**: 47315
**Date**: 2026-06-11
**URL**: https://discourse.slicer.org/t/subtract-segment-using-python-console-is-not-working/47315

---

## Post #1 by @Gaia_Eligio (2026-06-11 15:10 UTC)

<p>Hi, all. I am working on a Python script to automate the creation of skull, meninges, and CSF with the use of segmentations imported from FreeSurfer and MRI images. This is for a research project on Traumatic Brain Injuries.</p>
<p>The code has around 1628 lines. In lines 1312 and 1319, I call a function named: “subtract_segment”. What I’m trying to accomplish is to subtract the first segment (in this case called “final_falx”) and the second segment (in this case called “Skull”) from the final segment (in this case the “csf”), because the csf is overlapping with the skull and falx, but the falx and skull are not overlapping with each other.</p>
<p>The function works before and after in the code, but in this specific case, it just doesn’t. It says that it is working and it’s even using the correct IDs, but when I paste the code into Slicer, the CSF is still overlapping.</p>
<p>This is the function defined in line 628:</p>
<pre><code class="lang-auto">def subtract_segment(segmentation_node, segment_to_modify_id, segment_to_subtract_id):
        # Ensure binary labelmap is available
        segmentation_node.GetSegmentation().CreateRepresentation("BinaryLabelmap")

        # Set up the Segment Editor
        editor_node = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
        editor_node.SetOverwriteMode(slicer.vtkMRMLSegmentEditorNode.OverwriteNone)

        editor_widget = slicer.qMRMLSegmentEditorWidget()
        editor_widget.setMRMLScene(slicer.mrmlScene)
        editor_widget.setMRMLSegmentEditorNode(editor_node)
        editor_widget.setSegmentationNode(segmentation_node)

        # Set the segment to be modified (target)
        editor_node.SetSelectedSegmentID(segment_to_modify_id)
        editor_widget.setActiveEffectByName("Logical operators")

        effect = editor_widget.activeEffect()
        effect.setParameter("Operation", "SUBTRACT")
        effect.setParameter("ModifierSegmentID", segment_to_subtract_id)
        #effect.setParameter("OverwriteMode", "OverwriteNone")  # Keep segments separate
        effect.self().onApply()

        print(f"➖ Subtracted segment '{segment_to_subtract_id}' from '{segment_to_modify_id}'.")

        slicer.mrmlScene.RemoveNode(editor_node)
        editor_widget = None  # cleanup

</code></pre>
<p>And these are lines 1312 and 1319:</p>
<pre><code class="lang-auto">    seg_node = slicer.util.getNode(f"Segmentation_{subj_str}")
    csf_id = seg_node.GetSegmentation().GetSegmentIdBySegmentName("csf")
    final_falx_id = seg_node.GetSegmentation().GetSegmentIdBySegmentName("final_falx")
    subtract_segment(seg_node, csf_id, final_falx_id)

    seg_node = slicer.util.getNode(f"Segmentation_{subj_str}")
    csf_id = seg_node.GetSegmentation().GetSegmentIdBySegmentName("csf")
    skull_id = seg_node.GetSegmentation().GetSegmentIdBySegmentName("Skull")
    subtract_segment(seg_node, csf_id, skull_id)

</code></pre>
<p>This is the full code:</p>
<p><a href="https://github.com/user-attachments/files/28803784/AUTOMATED_SLICER_SEGMENTATION_edits.py" rel="noopener nofollow ugc">AUTOMATED_SLICER_SEGMENTATION</a></p>

---
