---
topic_id: 35952
title: "Error Loading Models In Freesurfer Extension"
date: 2024-05-06
url: https://discourse.slicer.org/t/35952
---

# Error loading models in FreeSurfer extension

**Topic ID**: 35952
**Date**: 2024-05-06
**URL**: https://discourse.slicer.org/t/error-loading-models-in-freesurfer-extension/35952

---

## Post #1 by @tbone (2024-05-06 18:26 UTC)

<p>Hello,</p>
<p>I am trying to use the FreeSurfer Importer to import surface data into slicer. I’ve checked using Freeview that the data can be loaded and visualized, however when using the slicer’s extension an error occurs when loading the files. The log shows this:</p>
<p>Error: Loading /Applications/freesurfer/7.4.1/subjects/sub-CON006/lh.surf.white - Could not load file: /Applications/freesurfer/7.4.1/subjects/sub-CON006/lh.surf.white</p>
<p>Would be grateful for any help! Thanks in advance.</p>

---

## Post #2 by @Sunderlandkyl (2024-05-06 20:13 UTC)

<p>Can you send a link to the full log?<br>
I can also take a look at the model if you can send me a link.</p>

---

## Post #3 by @tbone (2024-05-06 20:22 UTC)

<p>Hi I wasn’t sure how to send you the link so I’ve just copied it here sorry about that.</p>
<p>Critical | Stream<br>
Traceback (most recent call last):<br>
File “/Applications/Slicer.app/Contents/Extensions-32438/SlicerFreeSurfer/lib/Slicer-5.6/qt-scripted-modules/NiBabelModelIO.py”, line 169, in readModelNode<br>
geom = VolGeom.from_surf_footer(metadata)<br>
File “/Applications/Slicer.app/Contents/Extensions-32438/SlicerFreeSurfer/lib/Slicer-5.6/qt-scripted-modules/NiBabelModelIO.py”, line 70, in from_surf_footer<br>
shape=footer[‘volume’],<br>
KeyError: ‘volume’</p>
<p>Warning | Qt<br>
“/Applications/Slicer.app/Contents/Extensions-32438/SlicerFreeSurfer/lib/Slicer-5.6/qt-scripted-modules/NiBabelModelIO.py”  - In “NiBabelModelIOFileReader” class, function ‘write’  is expected to return a string boolean !<br>
static void qSlicerIOManager::showLoadNodesResultDialog(bool, vtkMRMLMessageCollection *) Errors occurred while loading nodes: “Error: Loading /Users/tony/Downloads/lh.surf.white - Could not load file: /Users/tony/Downloads/lh.surf.white\n”</p>
<p>and here is the link to the model: <a href="https://drive.google.com/file/d/1ir9ujO30gsyYEmWNXCO52ZNK82FmZqnb/view?usp=drive_link" rel="noopener nofollow ugc">https://drive.google.com/file/d/1ir9ujO30gsyYEmWNXCO52ZNK82FmZqnb/view?usp=drive_link</a></p>

---
