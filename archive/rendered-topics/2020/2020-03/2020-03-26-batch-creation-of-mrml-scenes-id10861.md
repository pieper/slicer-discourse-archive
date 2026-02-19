---
topic_id: 10861
title: "Batch Creation Of Mrml Scenes"
date: 2020-03-26
url: https://discourse.slicer.org/t/10861
---

# Batch creation of mrml scenes

**Topic ID**: 10861
**Date**: 2020-03-26
**URL**: https://discourse.slicer.org/t/batch-creation-of-mrml-scenes/10861

---

## Post #1 by @Masteling (2020-03-26 19:00 UTC)

<p>I have a series of 3D ultrasounds that I converted to mhd+raw files.</p>
<p>I want to automate the creation of mrml scenes for all my files (&gt; 500 files), to make it easier to visualize by others.</p>
<p>Goal: import mhd+raw -&gt; save as .mrml</p>
<p>Is there any script I can use/adapt?</p>
<p>Thank you,<br>
Mariana</p>

---

## Post #2 by @lassoan (2020-03-26 19:02 UTC)

<p>These examples in the script repository should help:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Load_volume_from_file" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Load_volume_from_file</a></p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Save_the_scene_into_a_single_MRB_file" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Save_the_scene_into_a_single_MRB_file</a></p>

---

## Post #3 by @sobiny (2020-03-26 19:43 UTC)

<pre><code>source_dir='C:\\mhddir\\'
for parent, dirnames, filenames in os.walk(source_dir):
    for filename in filenames:
        mhdfile = os.path.join(parent, filename)
        if mhdfile.endswith(".mhd"):
            [success, mhdNode] = slicer.util.loadVolume(mhdfile, returnNode=True)

sceneSaveFilename ="c:\\test.mrb"
slicer.util.saveScene(sceneSaveFilename)
</code></pre>
<p>I haven’t tested this code<br>
I don’t know if I understand what you mean</p>

---
