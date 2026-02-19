---
topic_id: 10143
title: "Script Repository Add A Texture Mapped Plane To The Scene As"
date: 2020-02-06
url: https://discourse.slicer.org/t/10143
---

# Script repository "Add a texture mapped plane to the scene as a model" has error

**Topic ID**: 10143
**Date**: 2020-02-06
**URL**: https://discourse.slicer.org/t/script-repository-add-a-texture-mapped-plane-to-the-scene-as-a-model-has-error/10143

---

## Post #1 by @mikebind (2020-02-06 19:05 UTC)

<p>From an empty scene, pasting the code from the “Add a texture mapped plane to the scene as a model” section from the script repository (<a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Add_a_texture_mapped_plane_to_the_scene_as_a_model" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Add_a_texture_mapped_plane_to_the_scene_as_a_model</a>) into the python interactor and running it doesn’t show anything in the 3D view.   I’m running 4.11.0-2020-01-08.</p>
<p>I see that there is an error in the log<br>
AttributeError: ‘MRMLCorePython.vtkMRMLModelDisplayNode’ object has no attribute ‘SetAndObserveTextureImageData’</p>
<p>I guess this might be related to the VTK version 6 update? If it’s just not functional at this point, might want to make a note of that on the Script Repository page.  Though, thinking about it, someone must have figured out how to do this, because the slice views visible in the 3D view accomplishes the same functionality (getting an image displayed on a plane in the 3D view) and more.  A functional demo script in the repository would helpful.  Thanks!</p>

---

## Post #2 by @lassoan (2020-02-06 20:31 UTC)

<p>It was an ancient code snippet. I’ve updated it now to match current Slicer API.</p>
<p>You may also consider using <a href="https://github.com/SlicerIGT/SlicerIGT/blob/master/TextureModel">TextureModel</a> module in SlicerIGT, which can take care of loading and properly aligning the texture that comes from surface scanners and can also set texture information in point scalars so that it can be used by filters and saved in VTK mesh files.</p>
<div class="lazyYT" data-youtube-id="PeyfyCs2tJg" data-youtube-title="Importing of color surface scans into 3D Slicer" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>

---
