---
topic_id: 6169
title: "How To Load Mrb File And Save All Nodes In Nii Format Using"
date: 2019-03-17
url: https://discourse.slicer.org/t/6169
---

# how to load mrb file and save all nodes in nii format using script

**Topic ID**: 6169
**Date**: 2019-03-17
**URL**: https://discourse.slicer.org/t/how-to-load-mrb-file-and-save-all-nodes-in-nii-format-using-script/6169

---

## Post #1 by @FrankEP (2019-03-17 04:01 UTC)

<p>Operating system: windows 10<br>
Slicer version:4.8.1<br>
Expected behavior: save nodes in nii format using script<br>
Actual behavior: only can save in nrrd format</p>
<p>Hi,<br>
I want to export image and labelmap node in nii format to a directory using python script.<br>
My script is:</p>
<p>mrbfile=r’D:\sample.mrb’<br>
outdir = r’D:\output_dir’<br>
loadScene(infilename)<br>
saveScene(outfilename[:-4])<br>
slicer.mrmlScene.Clear(0);</p>
<p>However, this could only save node in nrrd format, the 3D Slicer default format. How could I save my image node and labelmap node in nii format?</p>
<p>Thanks a lot.</p>

---

## Post #2 by @lassoan (2019-03-17 04:20 UTC)

<p>You can iterate through all the image nodes and save them to any folder using any of the supported file extensions. Something like this:</p>
<pre><code>for volumeNode in slicer.util.getNodesByClass("vtkMRMLScalarVolumeNode"):
  volumeNode.AddDefaultStorageNode()
  slicer.util.saveNode(volumeNode, "c:/tmp/" + volumeNode.GetName() + ".nii")</code></pre>

---

## Post #3 by @FrankEP (2019-03-18 03:28 UTC)

<p>Thank you very much, Andras. It works well.</p>

---
