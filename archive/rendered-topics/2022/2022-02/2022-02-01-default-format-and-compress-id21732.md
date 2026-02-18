# Default format and compress

**Topic ID**: 21732
**Date**: 2022-02-01
**URL**: https://discourse.slicer.org/t/default-format-and-compress/21732

---

## Post #1 by @Benoit (2022-02-01 14:19 UTC)

<p>Hi<br>
I used 3d slicer to segment organs and I’m here because of 2 questions :</p>
<ul>
<li>I want to change the default format of 3d model in ply and not vtk</li>
<li>I want to unset compress option instead of doing it manually.</li>
</ul>
<p>I don’t know anything about code and I wonder if it’s possible to do this.<br>
Thanks a lot for your advice, it could save me a lot of time.</p>

---

## Post #2 by @mikebind (2022-02-01 16:50 UTC)

<p>This is possible without you doing any coding, you just need to follow the instructions here: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#change-default-output-file-type-for-new-nodes" class="inline-onebox">Script repository — 3D Slicer documentation</a> in the section “Change default output file type for new nodes”.</p>
<p>For the compression option, add the line</p>
<pre><code class="lang-auto">defaultModelStorageNode.SetUseCompression(0) # change default to uncompressed
</code></pre>
<p>to your <code>.slicerrc.py</code> file right before the last line you just pasted in.</p>
<p>So, the 4 lines total which you will have added to the file will be</p>
<pre><code class="lang-auto">defaultModelStorageNode = slicer.vtkMRMLModelStorageNode()
defaultModelStorageNode.SetDefaultWriteFileExtension("ply") # change default to .ply
defaultModelStorageNode.SetUseCompression(0) # change default to uncompressed
slicer.mrmlScene.AddDefaultNode(defaultModelStorageNode)
</code></pre>
<p>These settings will take effect next time you open Slicer.   So, if you add these lines to your <code>.slicerrc.py</code> file while you have Slicer open, you will still need to change the settings manually in that Slicer session.</p>

---

## Post #3 by @Benoit (2022-02-11 16:10 UTC)

<p>Thanks a lot. It works well!<br>
Do you know if it’s also possible for nrrd and color table files?<br>
Thanks</p>

---

## Post #4 by @mikebind (2022-02-11 23:17 UTC)

<p>It looks like you could use exactly the analogous approach for color tables.</p>
<pre><code class="lang-auto">defaultColorTableStorageNode = slicer.vtkMRMLColorTableStorageNode()
defaultModelStorageNode.SetDefaultWriteFileExtension("txt") # looks like txt is the other option for color tables
slicer.mrmlScene.AddDefaultNode(defaultColorTableStorageNode)
</code></pre>
<p>For image files, it looks a little different:</p>
<pre><code class="lang-auto">defaultImageStorageNode = slicer.vtkMRMLVolumeArchetypeStorageNode()
defaultImageStorageNode.SetDefaultWriteFileExtension( 'nii.gz' ) # insert extension you want here 
slicer.mrmlScene.AddDefaultNode(defaultImageStorageNode)
</code></pre>
<p>I think this will likely work fine for the color tables.  I’m less sure whether this will work for image volumes.  If it doesn’t work, I would post a new discourse question on that topic to get suggestions from others.  One consideration is that images are very likely to have been loaded from a particular format, and may remember that format rather than have that overridden by a default setting.</p>

---

## Post #5 by @Benoit (2022-02-15 10:10 UTC)

<p>Thank you for your answer.<br>
Maybe I was not clear but it was for changing the compression default for color table and image files.<br>
Once again, thanks a lot</p>

---

## Post #6 by @mikebind (2022-02-15 15:58 UTC)

<p>For the compression settings on each of these storage nodes, you can use the <code>SetUseCompression()</code> function.  You can add the lines</p>
<pre><code class="lang-auto"># Insert this line before: slicer.mrmlScene.AddDefaultNode(defaultColorTableStorageNode)
defaultColortTableStorageNode.SetUseCompression(0) # 0 for no compression, 1 for compression

# Insert this line before: slicer.mrmlScene.AddDefaultNode(defaultImageStorageNode)
defaultImageStorageNode.SetUseCompression(0) # 0 for no compression, 1 for compression
</code></pre>
<p>I’m not sure which setting wins if the format/extension conflicts with the <code>SetUseCompression()</code> setting, but you can test and see. For example, if you specified the extension as ‘nii.gz’, indicating a compressed Nifti file, but set <code>SetUseCompression(0)</code>, indicating not to compress it, I’m not sure whether the output would be compressed or not. Safest would be to make sure the two settings are compatible with each other.</p>

---
