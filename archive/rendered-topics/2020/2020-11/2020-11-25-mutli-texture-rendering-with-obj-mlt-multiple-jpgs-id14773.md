---
topic_id: 14773
title: "Mutli Texture Rendering With Obj Mlt Multiple Jpgs"
date: 2020-11-25
url: https://discourse.slicer.org/t/14773
---

# Mutli texture rendering with obj + mlt + multiple jpgs

**Topic ID**: 14773
**Date**: 2020-11-25
**URL**: https://discourse.slicer.org/t/mutli-texture-rendering-with-obj-mlt-multiple-jpgs/14773

---

## Post #1 by @ezgimercan (2020-11-25 19:11 UTC)

<p>I have a 3D mesh in OBJ format created by a commercial stereophotogrammetry setup. It has an associated .mtl file and a couple JPGs for texture. My collaborators need to use texture to annotate some curves/points on these meshes in Slicer. Texture Model and similar python scripts work great when you have only 1 JPG file as a texture (and 1 array in the OBJ file for texture coordinates) but I was unable to replicate it with multiple textures.</p>
<p>I was also unsuccessful in implementing a python script (in and out of Slicer) for multi-texture rendering - where I read JPGs one by one, create vtkTexture objects, and use MapDataArrayToMultiTextureAttribute function from vtkPolyDataMapper. I tried EdgeClamping, changing texture coordinates from -1 to 1.1, different blending modes etc. No hope. If I use additive blending, then overlapping regions get very bright, if I “replace” option then only the last texture file is shown. In short, I’ve tried lots of combinations but nothing worked.</p>
<p>Then I found vtkOBJImporter class - I know, it does exactly what I need. It reads the .mtl and .jpgs and creates a beautiful vtkActor with the right texture mapping. It was like magic after days of reading texture blending and edge clamping. Now, my question is, how can I use this in Slicer? vtkOBJImporter gives me a RendererWindow (which I can put into a vtkRenderWindowInteractor outside the Slicer) but Slicer has its own renderWindow and renderer and interactor etc. Can I replace them? Can I get Actors and Mappers from Importer and push into Slicer’s renderer?</p>
<p>Any help with multi-texture rendering in Slicer would be appreciated. I really think the second option with vtkOBJImporter is simpler but if you have pointers on multi-texture blending I can provide data and code.</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2020-11-25 19:40 UTC)

<p>It is good to know that VTK can now import multi-textured OBJ files correctly.</p>
<p>You can add actors directly in the Slicer render window (see <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Accessing_views.2C_renderers.2C_and_cameras">examples in the script repository</a>), but that would not be usable for much (you would see the model but could not interact with it, you would need to add it to each view, implement slice intersections, etc.).</p>
<p>Since multi-textured models are so rare, I don’t think we will add support for them in Models module. But you should be able to easily convert such a mesh by reading using vtkOBJImporter then immediately writing it to a single-texture VTP using <a href="https://vtk.org/doc/nightly/html/classvtkSingleVTPExporter.html">vtkSingleVTPExporter</a>.</p>
<p>This all should not take more than a few lines of code, but even that could be hard to figure out for users. So, it would be nice if you could add this feature to <a href="https://github.com/SlicerIGT/SlicerIGT/tree/master/TextureModel">TextureModel</a> module. For example, add a “Import multiple textures” checkbox and if it is checked then run the OBJ through import &amp; single VTP export and use this generated VTP file as input.</p>

---

## Post #3 by @ezgimercan (2020-11-25 21:35 UTC)

<p>Thanks Andras, that’s a great idea.<br>
It works for my data and I will add it to TextureModel module.</p>

---

## Post #4 by @N96081127 (2021-03-30 19:26 UTC)

<p>Dear ezgimercan:<br>
I’m interested in reading multi-texture obj files through python like you. But after reading the article, the textures loading is still not very well. Is there any github code for me to learn VTK load multiple textures? thank you very much.</p>
<p>Sincerely,<br>
Yen-Hong Chen</p>

---

## Post #5 by @ezgimercan (2021-04-01 17:37 UTC)

<p>Hi Yen-Hong,<br>
You can see my updates to Texture Model module (included in Slicer IGT extension) here:</p><aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/ezgimercan/SlicerIGT/blob/22cf9e01c5e8e6663ab4948d3fd2cf7d1f7a0b21/TextureModel/TextureModel.py" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/ezgimercan/SlicerIGT/blob/22cf9e01c5e8e6663ab4948d3fd2cf7d1f7a0b21/TextureModel/TextureModel.py" target="_blank" rel="noopener nofollow ugc">ezgimercan/SlicerIGT/blob/22cf9e01c5e8e6663ab4948d3fd2cf7d1f7a0b21/TextureModel/TextureModel.py</a></h4>
<pre><code class="lang-py">import random
import os
import unittest
from __main__ import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
import logging

#
# TextureModel
#

class TextureModel(ScriptedLoadableModule):
  """Uses ScriptedLoadableModule base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def __init__(self, parent):
    ScriptedLoadableModule.__init__(self, parent)
    self.parent.title = "Texture Model"
    self.parent.categories = ["Surface Models"]
</code></pre>

  This file has been truncated. <a href="https://github.com/ezgimercan/SlicerIGT/blob/22cf9e01c5e8e6663ab4948d3fd2cf7d1f7a0b21/TextureModel/TextureModel.py" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
