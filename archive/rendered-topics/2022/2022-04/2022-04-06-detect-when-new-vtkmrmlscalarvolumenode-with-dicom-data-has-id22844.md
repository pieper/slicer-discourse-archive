---
topic_id: 22844
title: "Detect When New Vtkmrmlscalarvolumenode With Dicom Data Has"
date: 2022-04-06
url: https://discourse.slicer.org/t/22844
---

# Detect when new vtkMRMLScalarVolumeNode with DICOM data has been added

**Topic ID**: 22844
**Date**: 2022-04-06
**URL**: https://discourse.slicer.org/t/detect-when-new-vtkmrmlscalarvolumenode-with-dicom-data-has-been-added/22844

---

## Post #1 by @bruce (2022-04-06 05:24 UTC)

<p>Hello,<br>
I am writing a ScriptedLoadableModule that includes a custom table of all nodes loaded directly from DICOM data (along with custom information relating to these nodes). The table is populated based on whether DICOM appears in the node attributes.<br>
I am struggling to trigger a refresh of this table when the user has loaded a new DICOM dataset through the DICOM module and then switches back to my custom module. Is there an event I can observe to detect when the DICOM node is fully loaded or when my module is back in focus (in the module pane)? The slicer.mrmlScene.nodeAddedEvent fires with the additional node but it appears to do so before the node attributes are populated.<br>
Thanks</p>

---

## Post #2 by @lassoan (2022-04-06 05:40 UTC)

<p>Any module can make any follow-up changes to any nodes anytime after they are loaded. So, if you want to keep your table up-to-date then you need to add observer to scene’s <code>NodeAddedEvent</code> and if you find that a volume node is added then observe that node. Whenever any volume node is changed you can refresh your table (maybe indirectly, via a resettable timer, so you would only refresh the table if there is no volume node modification for a few seconds).</p>
<p>If you don’t need a generic solution because you don’t need to make your module compatible with all modules (for example, because you create a custom application and users cannot install extensions) then you can simplify. For example, it may be enough to just wait a bit after a volume is loaded. Or you can monkey-patch the DICOM browser’s <code>onLoadingFinished</code> method to send a notification to your module.</p>

---
