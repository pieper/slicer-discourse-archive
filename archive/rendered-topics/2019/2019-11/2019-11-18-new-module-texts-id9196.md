# New module: Texts

**Topic ID**: 9196
**Date**: 2019-11-18
**URL**: https://discourse.slicer.org/t/new-module-texts/9196

---

## Post #1 by @Sunderlandkyl (2019-11-18 18:16 UTC)

<p>We have added a new module (Texts) to recent Slicer Preview Releases (4.11) that allows storage and simple viewing of editing any text files in the scene (custom metadata files, configuration files, etc.)</p>
<div class="lazyYT" data-youtube-id="EdFkE5ztly4" data-youtube-title="Texts - New module in 3D Slicer" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<p>For users:<br>
- Text nodes can be used to store additional metadata in the scene, such as generic text, or json/xml strings.<br>
- Files in txt, xml, or json format can be dragged and dropped into 3D Slicer and loaded by selecting “Text file” for the file description</p>
<p>For developers:<br>
- This module introduces vtkMRMLTextNode and vtkMRMLTextStorageNode into the Slicer core.<br>
- The new qMRMLTextWidget can be added to any module to provide an interface to edit the contents of vtkMRMLTextNode, or display it in a read-only format.</p>
<p>Suggestions and feedback are welcome.</p>
<p>Development was funded in part by CANARIE’s Research Software Program, OpenAnatomy, and Brigham and Women’s Hospital through NIH grant R01MH112748.</p>

---
