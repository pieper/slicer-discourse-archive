---
topic_id: 3037
title: "Loading File Into Existing Node"
date: 2018-06-01
url: https://discourse.slicer.org/t/3037
---

# Loading file into existing node

**Topic ID**: 3037
**Date**: 2018-06-01
**URL**: https://discourse.slicer.org/t/loading-file-into-existing-node/3037

---

## Post #1 by @adelmo (2018-06-01 10:30 UTC)

<p>Greetings slicer experts,</p>
<p>I was wondering is someone could help me solving my little problem.<br>
What I would like to do is loading a file directly into an existing node.</p>
<p>In this moment to load a file (.nii for example) the instruction I use is:<br>
_, self.upNode = slicer.util.loadVolume(filepath, returnNode=True)</p>
<p>This creates a new node (upNode), with the same name as the filename, where I can explore my image.</p>
<p>Would it be possible to load filepath directly into an already existing node (a vtkMRMLScalarVolumeNode) ?<br>
Completely overriding what was already in it but leaving untouched the node name and ID.</p>
<p>Thank You,<br>
Alex</p>

---

## Post #2 by @ihnorton (2018-06-01 13:53 UTC)

<p>As long as the file is still compatible with the node type, you can try:</p>
<pre><code class="lang-auto">node = slicer.util.getNode("NODENAME")

storage = slicer.vtkMRMLNRRDStorageNode()
storage.SetFileName(filepath)
storage.ReadData(node)
</code></pre>

---
