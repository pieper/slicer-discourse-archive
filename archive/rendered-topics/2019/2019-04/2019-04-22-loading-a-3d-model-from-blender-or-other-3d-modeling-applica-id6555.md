# Loading a 3D model from Blender or other 3D modeling applications (STL, 3DS, FBX file format) into the scene programmatically using Python

**Topic ID**: 6555
**Date**: 2019-04-22
**URL**: https://discourse.slicer.org/t/loading-a-3d-model-from-blender-or-other-3d-modeling-applications-stl-3ds-fbx-file-format-into-the-scene-programmatically-using-python/6555

---

## Post #1 by @Hadi-Fooladi (2019-04-22 15:12 UTC)

<p>Hi,</p>
<p>I have a polygonal 3d model file and I want to import it to the scene. I can do it through user interface but I wanted to know how can I achieve this through code.</p>
<p>Thanks,<br>
Hadi</p>

---

## Post #2 by @Sam_Horvath (2019-04-22 15:48 UTC)

<p>Hi:</p>
<p>slicer.util.loadModel("/path/to/file.ext")   will work for this purpose.</p>
<p>See: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/IO#How_to_load_files_programmatically" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/IO#How_to_load_files_programmatically</a></p>
<p>Supported data formats can be found here:<br>
<a href="https://www.slicer.org/wiki/Documentation/4.10/SlicerApplication/SupportedDataFormat" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/4.10/SlicerApplication/SupportedDataFormat</a></p>

---
