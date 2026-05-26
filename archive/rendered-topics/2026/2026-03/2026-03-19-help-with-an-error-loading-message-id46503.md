---
topic_id: 46503
title: "Help with an Error: Loading message"
date: 2026-03-19
url: https://discourse.slicer.org/t/46503
last_bumped: 2026-03-23T10:01:40.151Z
---

# Help with an Error: Loading message

**Topic ID**: 46503
**Date**: 2026-03-19
**URL**: https://discourse.slicer.org/t/help-with-an-error-loading-message/46503

---

## Post #1 by @BrittneyL (2026-03-19 18:48 UTC)

<p>Good Afternoon! I have been having the same error consistently and on more than one computer: The text of the error reads:</p>
<p>Error: Loading C:/Users/blacy2/Desktop/A27.mrb - ERROR: In vtkMRMLStorableNode.cxx, line 316</p>
<p>vtkMRMLScalarVolumeNode (0000018599931590): vtkMRMLStorableNode::UpdateScene failed: Failed to read node A-27_Merged_Scans_1-2 (vtkMRMLScalarVolumeNode1) using storage node vtkMRMLVolumeArchetypeStorageNode4.</p>
<p>Could someone help advise on how to fix this error? It does not matter if I load in new data, as soon as I save it I can never open it again</p>

---

## Post #2 by @pieper (2026-03-19 21:27 UTC)

<p>That’s odd.  Is it possible you could share the mrb file for testing?</p>
<p>If not, can you describe the data and the exact steps you go through?</p>

---

## Post #3 by @Nancy_Casper (2026-03-23 10:01 UTC)

<p>That loading error is usually down to a mismatch between the header and the actual data in your file. If Slicer can’t find the specific volume dimensions or spacing it expects, it’ll just hang or throw a generic error. A quick thing to try is using the “Add Data” dialog but checking the “Show Options” box. Sometimes manually setting the file type to “Volume” instead of letting it auto-detect fixes the hang. If it’s a DICOM issue, you might want to try importing it through the DICOM Browser module first rather than just dragging and dropping the file.</p>
<p>If you’re still stuck, check if there are any special characters or spaces in the file path - Slicer can be a bit picky about those depending on the OS.</p>

---
