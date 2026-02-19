---
topic_id: 1699
title: "Get Filename Of Loaded Volume"
date: 2017-12-21
url: https://discourse.slicer.org/t/1699
---

# Get filename of loaded volume

**Topic ID**: 1699
**Date**: 2017-12-21
**URL**: https://discourse.slicer.org/t/get-filename-of-loaded-volume/1699

---

## Post #1 by @spring (2017-12-21 09:45 UTC)

<p>Operating system: MS windows 10 64bit<br>
Slicer version: 4.9.0<br>
Expected behavior: not report error of NoneType<br>
Actual behavior: failed at NoneType error</p>
<p>Hi developers,</p>
<p>I just found this error in Slicer 4.9.0, not sure this one is bug in fnmatch.translate, could you help to confirm?</p>
<pre>
    BNode = slicer.util.getNode(BId)
  File "C:\Program Files\Slicer 4.9.0-2017-10-23\bin\Python\slicer\util.py", line 622, in getNode
    nodes = getNodes(pattern, scene)
  File "C:\Program Files\Slicer 4.9.0-2017-10-23\bin\Python\slicer\util.py", line 609, in getNodes
    if (fnmatch.fnmatchcase(name, pattern) or
  File "C:\Program Files\Slicer 4.9.0-2017-10-23\lib\Python\Lib\fnmatch.py", line 78, in fnmatchcase
    res = translate(pat)
  File "C:\Program Files\Slicer 4.9.0-2017-10-23\lib\Python\Lib\fnmatch.py", line 89, in translate
    i, n = 0, len(pat)
TypeError: object of type 'NoneType' has no len()
</pre>
<p>Thanks,<br>
Chunbo</p>

---

## Post #2 by @lassoan (2017-12-21 12:55 UTC)

<p>To specify a string, you need to put it between quotation marks:</p>
<pre><code>BNode = slicer.util.getNode("BId")</code></pre>

---

## Post #3 by @spring (2017-12-21 14:46 UTC)

<p>Thanks for your quick replies,Lassoan.<br>
I tried the line with quotation marks <code>(str(BID))</code>, but reported following error:</p>
<pre>
Traceback (most recent call last):
  File "widgetMammogram.py", line 162, in onSideSelect
    filename1 = self.getFileNameByTag('View1')
  File "widgetMammogram.py", line 173, in getFileNameByTag
    StorageNode = BNode.GetStorageNode()
AttributeError: 'NoneType' object has no attribute 'GetStorageNode'
</pre>
<p>I attached my codes now:</p>
<pre>
    def getFileNameByTag(self, tag):
        widget = slicer.app.layoutManager().sliceWidget(tag)
        CNode = widget.sliceLogic().GetSliceCompositeNode()
        BId = CNode.GetBackgroundVolumeID()
        BNode = slicer.util.getNode(str(BId))
        StorageNode = BNode.GetStorageNode()
        filename=StorageNode.GetFileName()
        print('filename = {}'.format(filename))
        return filename
</pre>
<p>btw, it can print the filename correctly after outputing above error message. Here, I have convert the args(BID) as String, not sure BNode is None?</p>
<p>Thanks,<br>
Chunbo</p>

---

## Post #4 by @lassoan (2017-12-21 15:02 UTC)

<p>This works for me:</p>
<pre><code>def getFileNameByTag(tag):
  sliceWidget = slicer.app.layoutManager().sliceWidget(tag)
  sliceCompositeNode = sliceWidget.sliceLogic().GetSliceCompositeNode()
  backgroundVolumeID = sliceCompositeNode.GetBackgroundVolumeID()
  backgroundVolume = slicer.mrmlScene.GetNodeByID(backgroundVolumeID)
  storageNode = backgroundVolume.GetStorageNode()
  if not storageNode:
    return None
  filename = backgroundVolume.GetStorageNode().GetFileName()
  return filename

print getFileNameByTag("Red")
</code></pre>
<p>However, filename may not be always available and it should not be necessary to access it anyway. What would you like to achieve? Pass the image to an external software? Or get additional metadata from the image?</p>

---

## Post #5 by @spring (2017-12-21 15:18 UTC)

<p>Hi Lassoan,</p>
<blockquote>
<p>“What would you like to achieve? Pass the image to an external software? Or get additional metadata from the image?”</p>
</blockquote>
<p>The background is: I setted Slicer’s layout as two scenes (widgets), each scene will display one dcm file, the user will add some polydata in the scenes and we will save the position of these polydata into a json file for each dcm file (the path is same of each dcm file), so we have to know the source path of each node (dcm).</p>
<p>Any good ideas ?</p>
<p>Thanks,<br>
Chunbo</p>

---

## Post #6 by @lassoan (2017-12-21 15:22 UTC)

<p>This should do what you need:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_get_path_and_filename_of_a_loaded_DICOM_volume.3F">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_get_path_and_filename_of_a_loaded_DICOM_volume.3F</a></p>

---

## Post #7 by @spring (2017-12-21 15:29 UTC)

<p>Thanks,Lassoan.</p>
<p>Yes,these lines work well(to get dcm file’s path from it’s name). If we want to get the file’s path from sliceWidgets,is there anyother good methods?</p>
<p>Thanks,<br>
Chunbo</p>

---

## Post #8 by @lassoan (2017-12-21 15:29 UTC)

<p>It is a trivial combination of the two examples above.</p>

---
