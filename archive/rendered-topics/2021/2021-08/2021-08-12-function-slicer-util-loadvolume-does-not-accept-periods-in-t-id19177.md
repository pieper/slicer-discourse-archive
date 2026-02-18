# Function slicer.util.loadVolume does not accept periods in the filename

**Topic ID**: 19177
**Date**: 2021-08-12
**URL**: https://discourse.slicer.org/t/function-slicer-util-loadvolume-does-not-accept-periods-in-the-filename/19177

---

## Post #1 by @giovform (2021-08-12 22:50 UTC)

<p>If the file has a period in its name, e.g. <strong>word1.word2.tif</strong>, then the loaded volume using <strong>slicer.util.loadVolume</strong> function will have its name as just <strong>word1</strong>.</p>
<p>Is this intended?</p>
<p>Tested on 4.11.20210226 r29738.</p>

---

## Post #2 by @lassoan (2021-08-13 04:33 UTC)

<p>When you load a file using the GUI then there is a mechanism that strips known file extensions for the selected reader and allows the user to edit it before loading.</p>
<p>If you load a node programmatically then a simpler mechanism is used that removes the complete file extension.</p>
<p>If you want to remove only the longest <em>known</em> file extension then you can use the storage node’s <code>GetFileNameWithoutExtension()</code> method:</p>
<pre><code class="lang-python">volumeNode = slicer.util.loadVolume(r'c:\tmp\word1.word2.tif')
volumeNode.SetName(volumeNode.GetStorageNode().GetFileNameWithoutExtension())
</code></pre>

---
