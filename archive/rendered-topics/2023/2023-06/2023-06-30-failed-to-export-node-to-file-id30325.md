---
topic_id: 30325
title: "Failed To Export Node To File"
date: 2023-06-30
url: https://discourse.slicer.org/t/30325
---

# Failed to export node to file

**Topic ID**: 30325
**Date**: 2023-06-30
**URL**: https://discourse.slicer.org/t/failed-to-export-node-to-file/30325

---

## Post #1 by @Patrick_Li (2023-06-30 15:20 UTC)

<p>I’m attempting to export multiple vtkMRMLTableNodes from an array to a directory</p>
<pre><code class="lang-auto">        for preset in self.presets:
            if preset and preset.IsA('vtkMRMLStorableNode') and preset.GetStorageNode():
                filename = presetsDir + '\\' + preset.GetName()
                if '.csv' not in filename:
                    filename += '.csv'
                slicer.util.exportNode(preset, filename)
</code></pre>
<p>But preset.GetStorageNode() continually returns None despite preset.IsA(‘vtkMRMLStorableNode’) being True. When I remove preset.GetStorageNode(), this shows up.</p>
<pre><code class="lang-auto">[Python] Failed to export node to file: C:\directory\...
[Python] Error: Unable to find a storable node with ID vtkMRMLTableNode1
</code></pre>
<p>However, the program successfully exports other table nodes that are in the subject hierarchy. I tried adding the tables I wanted to save to the hierarchy, but the issue persists.</p>

---
