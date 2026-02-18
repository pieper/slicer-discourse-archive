# Avoid creating multiple module widget instances from a python script

**Topic ID**: 36717
**Date**: 2024-06-12
**URL**: https://discourse.slicer.org/t/avoid-creating-multiple-module-widget-instances-from-a-python-script/36717

---

## Post #1 by @RomanStriker (2024-06-12 10:45 UTC)

<p>Hi,<br>
I am trying to generate centerlines for a batch of segmentation masks. I use a python script that uses the VMTK Extract Centerline widget. The issue is that for every new segmentation, Slicer opens a new Extract Centerline widget window, while keeping the previous window open as well, leading to a lot of windows, as the script processes more masks. The script has the following structure.</p>
<pre><code class="lang-auto">for volume, segmentation in zip(volume_list, segmentation_list):
# 1. load volume and segmentation
...

# 2. Auto-detect the endpoints and extract centerline
extractCenterlineWidget = ExtractCenterline.ExtractCenterlineWidget()
# Set the parameters
extractCenterlineWidget._parameterNode.SetNodeReferenceID("InputSurface", seg.GetID())
extractCenterlineWidget._parameterNode.SetParameter("InputSegmentID", segmentID)
...
extractCenterlineWidget.onAutoDetectEndPoints()
extractCenterlineWidget.onApplyButton()

# Save centerline
...

# Clean up
slicer.mrmlScene.Clear(0)

# Hoping this would exit slicer completely and start 
# again for the next iteration of the loop but it does not.
slicer.app.exit()
</code></pre>
<p>How to avoid opening multiple widget windows or close the previous one when the processing for the current segmentation is finished?</p>

---

## Post #2 by @cpinter (2024-06-12 10:55 UTC)

<p>The simplest solution is to re-use the same widget and only change the parameter node content before calling apply again.</p>

---
