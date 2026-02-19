---
topic_id: 36378
title: "3D Rendering Add Custom Texture In Models"
date: 2024-05-24
url: https://discourse.slicer.org/t/36378
---

# 3D rendering add custom texture in models

**Topic ID**: 36378
**Date**: 2024-05-24
**URL**: https://discourse.slicer.org/t/3d-rendering-add-custom-texture-in-models/36378

---

## Post #1 by @hfri (2024-05-24 23:59 UTC)

<p>Hi, I would like to 3D render a segmentation (model) and instead of using simple colours I would like to define a custom texture. How can I apply a custom  texture that I have stored on my computer in .jpg/ .png/.exr format?<br>
Thanks!!</p>

---

## Post #2 by @muratmaga (2024-05-25 17:18 UTC)

<p>There is a module in SlicerMorph that allows you load OBJ files with texture. Try and see if works for you. You may have to modify the code to make it work with your custom texture,</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerMorph/SlicerMorph/blob/master/OBJFile/OBJFile.py">
  <header class="source">

      <a href="https://github.com/SlicerMorph/SlicerMorph/blob/master/OBJFile/OBJFile.py" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerMorph/SlicerMorph/blob/master/OBJFile/OBJFile.py" target="_blank" rel="noopener">SlicerMorph/SlicerMorph/blob/master/OBJFile/OBJFile.py</a></h4>


      <pre><code class="lang-py">import logging
import os
import unittest
import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *

class OBJFile(ScriptedLoadableModule):
  def __init__(self, parent):
    ScriptedLoadableModule.__init__(self, parent)
    parent.title = 'OBJFile'
    parent.categories = ['Testing.TestCases']
    parent.dependencies = []
    parent.contributors = ["Chi Zhang (SCRI), Steve Pieper (Isomics), A. Murat Maga (UW)"]
    parent.helpText = '''
    This module is used to import OBJ file while automatically map.
    '''
    parent.acknowledgementText = '''
    Thanks to:

    Steve Pieper and Andras Lasso (functions from TextureModel module of SlicerIGT used in this script to map texture)
</code></pre>



  This file has been truncated. <a href="https://github.com/SlicerMorph/SlicerMorph/blob/master/OBJFile/OBJFile.py" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @muratmaga (2024-05-25 17:19 UTC)

<p>You can also use the TextureModel from IGT Extension. Load the 3D model, load the texture file (as a volume), and use the textureModel to apply the texture to the 3d model in the scene.</p>

---

## Post #4 by @hfri (2024-05-27 16:49 UTC)

<p>I have tried it with the texture module. My texture file is in .jpg format and I have imported it as a volume. Unfortunately it does not work that the model takes over this texture. Do you have any tips for the texture files?</p>

---

## Post #5 by @muratmaga (2024-05-27 17:05 UTC)

<p>Can you successfully apply that texture to the model in some other software (e.g., Meshlab)? The alternative is to apply it as vertex color (i.e., bake the texture) in other software and bring it to Slicer.</p>
<p>If you share your model and texture, perhaps people can give other suggestions.</p>

---

## Post #6 by @tsehrhardt (2024-05-28 18:47 UTC)

<p>You can try this in Blender. You will need to UV unwrap your model and bake the texture–even if it’s not a perfect unwrap (since CT models tend to be hi-poly) your texture might transfer well enough.</p>

---

## Post #7 by @lassoan (2024-05-29 14:30 UTC)

<p>Texture mapping works nicely in Slicer. If you have any trouble then we can help but we need more information. Sharing some example files would be the easiest. You can upload them anywhere (dropbox, onedrive, etc.) and post the link here.</p>

---

## Post #8 by @hfri (2024-05-29 15:36 UTC)

<p>Thanks so much for your help, I very much appreciate it!</p>
<p>Here’s a link to the structure on which I would like to apply the texture (also in dropbox).</p>
<p><a href="https://www.dropbox.com/scl/fo/yikk0px4wtba2b56cny0x/ALpjk0Dpj_1vE26L3XekruM?rlkey=g8spbupgx0leyhd6bz4dxfgwy&amp;dl=0" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.dropbox.com/scl/fo/yikk0px4wtba2b56cny0x/ALpjk0Dpj_1vE26L3XekruM?rlkey=g8spbupgx0leyhd6bz4dxfgwy&amp;dl=0</a></p>

---

## Post #9 by @lassoan (2024-05-29 21:05 UTC)

<p>The problem was that your model did not have any texture coordinates. You can add it in any modeling software, or you can go with basic mappings in Slicer, by copy-pasting this code snippet into the Python interactor:</p>
<pre data-code-wrap="python"><code class="lang-python">modelNode = getNode("structure")
textureMapper = vtk.vtkTextureMapToSphere()
textureMapper.SetInputData(modelNode.GetPolyData())
textureMapper.Update()
modelNode.SetAndObservePolyData(textureMapper.GetOutput())
</code></pre>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e628f539848506bc0942710c59c76c31b1912a3c.jpeg" alt="image" data-base62-sha1="wQ5zlxaVpCa6hbT5TUV7JK6KhJy" width="610" height="350"></p>
<p>The texture preview image you have uploaded (Metal041A.png) looks nice but not square shaped, so you will have some transparent regions in the textured model. If you use the color, etc. image (Metal041A_1K-JPG_Color.jpg) component then it will not look very nice. Maybe the best is to crop the preview image to square shape.</p>
<p>If you just want to show a simple metallic surface then you don’t need to do any texture mapping, but you can simply enable PBR interpolation (physics-based rendering) in Models module and enable “Image-based lighting” in Lights module (provided by Sandbox extension).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/919da469170a3dae679a39f784fbfaa3af6e248b.png" data-download-href="/uploads/short-url/kMaYLCVf9PvwYJqlkWOCXfEsxez.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/919da469170a3dae679a39f784fbfaa3af6e248b_2_248x500.png" alt="image" data-base62-sha1="kMaYLCVf9PvwYJqlkWOCXfEsxez" width="248" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/919da469170a3dae679a39f784fbfaa3af6e248b_2_248x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/919da469170a3dae679a39f784fbfaa3af6e248b_2_372x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/919da469170a3dae679a39f784fbfaa3af6e248b_2_496x1000.png 2x" data-dominant-color="3A3D3F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">805×1622 66.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/714659270f22a611c2fe5aeac6883e55d9aae571.png" data-download-href="/uploads/short-url/ga4FP985cmUX212tnRjH1LK90Fb.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/714659270f22a611c2fe5aeac6883e55d9aae571_2_266x500.png" alt="image" data-base62-sha1="ga4FP985cmUX212tnRjH1LK90Fb" width="266" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/714659270f22a611c2fe5aeac6883e55d9aae571_2_266x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/714659270f22a611c2fe5aeac6883e55d9aae571_2_399x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/714659270f22a611c2fe5aeac6883e55d9aae571_2_532x1000.png 2x" data-dominant-color="3C3D3D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">852×1596 64.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1cd1712b8e4430bff9c3108beaa44184f226fa91.jpeg" data-download-href="/uploads/short-url/46W5ZROVcR1WOQcLU80hND7mDhT.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1cd1712b8e4430bff9c3108beaa44184f226fa91_2_430x500.jpeg" alt="image" data-base62-sha1="46W5ZROVcR1WOQcLU80hND7mDhT" width="430" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1cd1712b8e4430bff9c3108beaa44184f226fa91_2_430x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1cd1712b8e4430bff9c3108beaa44184f226fa91.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1cd1712b8e4430bff9c3108beaa44184f226fa91.jpeg 2x" data-dominant-color="A29FC1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">610×708 60.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @hfri (2024-05-30 15:23 UTC)

<p>Thanks so much, this is incredibly helpful!</p>

---
