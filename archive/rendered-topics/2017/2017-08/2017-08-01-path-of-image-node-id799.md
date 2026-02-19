---
topic_id: 799
title: "Path Of Image Node"
date: 2017-08-01
url: https://discourse.slicer.org/t/799
---

# Path of image node

**Topic ID**: 799
**Date**: 2017-08-01
**URL**: https://discourse.slicer.org/t/path-of-image-node/799

---

## Post #1 by @dzenanz (2017-08-01 13:28 UTC)

<p>I needed to pass a path to DICOM file to a certain CLI module because that module needed metadata from the header. But to get the path depends on how the node was loaded, via drag-drop or via DICOM browser. Here is a function which works for both cases:</p>
<pre><code>def PathFromNode(self, node):
  storageNode=node.GetStorageNode()
  if storageNode is not None:
      filepath=storageNode.GetFullNameFromFileName()
  else:
      instanceUIDs=node.GetAttribute('DICOM.instanceUIDs').split()
      filepath=slicer.dicomDatabase.fileForInstance(instUids[0])
  return filepath

# example invocation
node=slicer.util.getFirstNodeByName('volume1')
path=self.PathFromNode(node)
print "DICOM path="+path</code></pre>

---

## Post #2 by @lassoan (2017-08-02 03:03 UTC)

<p>Thank you, it’s useful example. Could you please add it to the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository">script repository</a>?</p>

---

## Post #3 by @dzenanz (2017-08-02 15:17 UTC)

<p>Added:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_get_path_and_filename_of_a_loaded_DICOM_volume.3F" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_get_path_and_filename_of_a_loaded_DICOM_volume.3F</a></p>

---
