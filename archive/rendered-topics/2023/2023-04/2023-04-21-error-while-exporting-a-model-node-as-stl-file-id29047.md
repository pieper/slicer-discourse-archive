---
topic_id: 29047
title: "Error While Exporting A Model Node As Stl File"
date: 2023-04-21
url: https://discourse.slicer.org/t/29047
---

# Error while exporting a model node as stl file

**Topic ID**: 29047
**Date**: 2023-04-21
**URL**: https://discourse.slicer.org/t/error-while-exporting-a-model-node-as-stl-file/29047

---

## Post #1 by @Luca (2023-04-21 13:19 UTC)

<p>Hello everyone,</p>
<p>every time I try to export a model node (simple or complex) as stl file by using the GUI, I get the following error:</p>
<blockquote>
<p>Error: ERROR: In D:\D\S\S-0-build\VTK\IO\Geometry\vtkSTLWriter.cxx, line 248<br>
vtkSTLWriter (000001870E471130): Couldn’t open file: C:/Users/user/Desktop/New folder/bone.stl Reason: Permission denied<br>
Error: Saving failed with all writers found for file ‘C:/Users/user/Desktop/New folder/bone.stl’ of type ‘ModelFile’.<br>
Error: Error encountered while exporting liver.<br>
Error: ERROR: In D:\D\S\S-0-build\VTK\IO\Geometry\vtkSTLWriter.cxx, line 248<br>
vtkSTLWriter (000001870E471130): Couldn’t open file: C:/Users/user/Desktop/New folder/bone.stl Reason: Permission denied</p>
</blockquote>
<p>However, if I save the model node by code using slicer.util.saveNode() the Python Interactor, it works.</p>
<p>Can someone explain me what is happening and why? It is strange that it searches in D: because my pc has got just one disk (C:). Did anything go wrong during Slicer installation? Any other hints?</p>
<p>Thanks in advance!</p>

---

## Post #2 by @RafaelPalomar (2023-04-21 14:03 UTC)

<aside class="quote no-group" data-username="Luca" data-post="1" data-topic="29047">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/51bf81/48.png" class="avatar"> Luca:</div>
<blockquote>
<p>D:\D\S\S-0-build\VTK\IO\Geometry\vtkSTLWriter.cxx, line 248</p>
</blockquote>
</aside>
<p>If you are using a pre-compiled binary of Slicer, this is probably the path where the source tree was located when built. I would  think you can safely ignore this.</p>
<p>However, it seems the application does not have permission to write in the following folder:</p>
<aside class="quote no-group" data-username="Luca" data-post="1" data-topic="29047">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/51bf81/48.png" class="avatar"> Luca:</div>
<blockquote>
<p>C:/Users/user/Desktop/New folder</p>
</blockquote>
</aside>
<p>Are you able to create a file in that folder using any other application? Could you try also in a new folder without spaces in the name? (e.g., C:/Users/user/Desktop/newfolder).</p>

---

## Post #3 by @Luca (2023-04-21 14:42 UTC)

<p>Thanks for your quick reply.</p>
<p>Spaces don’t influence the result and yes, I can create files in that folder. For sure It is a permission problem, but I configured my two computers in the same way and installed Slicer in the same way. Why does the problem appear on just one pc?<br>
I will try re-installing it again with administrator permissions, but on the other pc I didn’t do so…</p>

---

## Post #4 by @Luca (2023-04-24 08:20 UTC)

<p>Update:<br>
I have re-installed Slicer as administrator, but I still cannot export models to stl files. The error is still the same as above</p>

---

## Post #5 by @RafaelPalomar (2023-04-25 13:59 UTC)

<p>This sounds strange to me and probably a Windows configuration issue, not Slicer. I have given a quick scan to similar problems online and found this post which offers different strategies to deal with the same (or similar problem):</p>
<p><a href="https://answers.microsoft.com/en-us/windows/forum/all/cusersusernamedesktop-is-not-accessible/69860653-d076-4c62-aa3d-5cce22f838e3" rel="noopener nofollow ugc">https://answers.microsoft.com/en-us/windows/forum/all/cusersusernamedesktop-is-not-accessible/69860653-d076-4c62-aa3d-5cce22f838e3</a></p>
<p>I unfortunately cannot reproduce the issue. I hope this helps.</p>

---
