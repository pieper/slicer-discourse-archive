# Determining current file name

**Topic ID**: 1241
**Date**: 2017-10-18
**URL**: https://discourse.slicer.org/t/determining-current-file-name/1241

---

## Post #1 by @stevenagl12 (2017-10-18 16:23 UTC)

<p>I was wondering if someone can create some sort of interface to determine the file name of the image that is currently portrayed within the red scene view. This would help the viewer to determine which file might need to be deleted from a volume easier, or more closely examined by other softwares, etc?</p>

---

## Post #2 by @lassoan (2017-10-18 19:03 UTC)

<p>You can get it through the Python console like this:</p>
<pre><code>slicer.mrmlScene.GetNodeByID(slicer.util.getNode('SliceComposite').GetBackgroundVolumeID()).GetStorageNode().GetFileName()
</code></pre>
<p>Maybe this could be implemented when Slice View Annotations feature is reworked to be more configurable. Filename could be one of the fields that the user could choose to show. You can configure Slice View Annotations in the DataProbe module.</p>

---
