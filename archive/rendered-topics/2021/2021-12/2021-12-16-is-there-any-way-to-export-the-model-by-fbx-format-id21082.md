# Is there any way to export the model by FBX format?

**Topic ID**: 21082
**Date**: 2021-12-16
**URL**: https://discourse.slicer.org/t/is-there-any-way-to-export-the-model-by-fbx-format/21082

---

## Post #1 by @slicer365 (2021-12-16 02:53 UTC)

<p>Is there any way to export the model in FBX format？</p>
<p>FBX files can contain multiple models at the same time, and contain other more information.</p>

---

## Post #2 by @lassoan (2021-12-16 18:04 UTC)

<p>Autodesk has very tight control over FBX, so it is generally avoided in open-source software.</p>
<p>You can save segmentations as VTK multi-block file format to preserve all metadata. You can export all segments into a single OBJ file, where each segment uses a different material, so you can easily separate them. Or you can use OpenAnatomy extension to export to glTF (which can be a single file, each segment stored in a separate object).</p>

---

## Post #3 by @slicer365 (2021-12-17 00:16 UTC)

<p>Thanks for your reply, my purpose：<br>
After I make a model through Slicer, I need to share the model with friends, but in many cases their mobile phone does not support direct viewing of stl or obj, etc. So I send it through the open web page,  <a href="https://3dviewer.net/" rel="noopener nofollow ugc">https://3dviewer.net/</a></p>
<p>But this webpage cannot support importing multiple models into one scene at the same time.</p>
<p>I am used to converting multiple models into one FBX  file through Blender, and then I can selectively hide part of the structure.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f975bbfd61074b76675afc9e0ff9d611e89a8fc7.jpeg" data-download-href="/uploads/short-url/zAP8m8wsjTaPXWfZGLmiiXyFm63.jpeg?dl=1" title="1639700410(1)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f975bbfd61074b76675afc9e0ff9d611e89a8fc7_2_517x277.jpeg" alt="1639700410(1)" data-base62-sha1="zAP8m8wsjTaPXWfZGLmiiXyFm63" width="517" height="277" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f975bbfd61074b76675afc9e0ff9d611e89a8fc7_2_517x277.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f975bbfd61074b76675afc9e0ff9d611e89a8fc7_2_775x415.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f975bbfd61074b76675afc9e0ff9d611e89a8fc7.jpeg 2x" data-dominant-color="D6E9E9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1639700410(1)</span><span class="informations">839×450 76.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
If it is to synthesize an OBJ model, then it is impossible to select and hide different structures</p>
<p>For web 3D visualization, do you have any suggestions? I particularly like the display of this effect, but I cannot create such a platform.  <a href="https://yun.gradient3d.com/scene/share.php?ID=86e12f12-615b-49f9-9e76-3493b3e51a55&amp;&amp;code=123456" rel="noopener nofollow ugc">Demo</a></p>

---

## Post #4 by @lassoan (2021-12-17 00:34 UTC)

<p><a href="http://3dviewer.net">3dviewer.net</a> takes glTF. As I wrote above, you can export a glTF using SlicerOpenAnatomy extensions’ “OpenAnatomy Export” module. <a href="http://3dviewer.net">3dviewer.net</a> displays it like this (you can turn on/off visibility of each segment):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/26a4ab6b2f8de06c439ff1b5ce72e56e911149a9.jpeg" data-download-href="/uploads/short-url/5vQWHNkn3Dyuj52ybkr7k05e6St.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/26a4ab6b2f8de06c439ff1b5ce72e56e911149a9_2_690x362.jpeg" alt="image" data-base62-sha1="5vQWHNkn3Dyuj52ybkr7k05e6St" width="690" height="362" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/26a4ab6b2f8de06c439ff1b5ce72e56e911149a9_2_690x362.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/26a4ab6b2f8de06c439ff1b5ce72e56e911149a9_2_1035x543.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/26a4ab6b2f8de06c439ff1b5ce72e56e911149a9_2_1380x724.jpeg 2x" data-dominant-color="F5F0F1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1184 259 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Segment names are not saved into the model but probably you can add this by editing the module. It is just a short Python script (OpenAnatomyExport.py).</p>

---

## Post #6 by @pieper (2021-12-17 13:29 UTC)

<p><a class="mention" href="/u/slicer365">@slicer365</a> you don’t need to write a script to get started, just install the OpenAnatomy extension and export your scene.  If you find that this works for you but the missing model names are an issue, then post example and example scene and the exported gltf and maybe someone can edit the python script for you. (It would be a good learning exercise for someone wanting to improve their Slicer development skills).</p>

---

## Post #7 by @lassoan (2021-12-17 20:23 UTC)

<p>I’ve updated the OpenAnatomy Exporter module to export model names and all the hierarchy folders, which displayed well in <a href="http://3dviewer.net">3dviewer.net</a> and other gltTF viewers.</p>
<p>See a model loaded into the interactive 3D viewer GUI by <a href="https://3dviewer.net/#model=https://raw.githubusercontent.com/lassoan/Test/master/SPL-Abdominal-Atlas.gltf">clicking here</a>. You can click on the volume to find the clicked object’s name, show/hide individual objects or group of objects, etc.</p>
<p><a href="https://3dviewer.net/#model=https://raw.githubusercontent.com/lassoan/Test/master/SPL-Abdominal-Atlas.gltf"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2ceefc000f896365c147f478427dde845684f2bf.jpeg" alt="image" data-base62-sha1="6pv1SIx8EUwbpn1nRmUerCC3Zz9" width="690" height="440"></a></p>
<p>The viewer can be embedded in any site, for example here is the SPL abdominal atlas exported using OpenAnatomy Exporter module (it is an interactive viewer, click-and-drag to rotate):</p>
<p>The viewer can be embedded, too:</p>
<pre><code class="lang-auto">&lt;iframe width="640" height="480" style="border:1px solid #eeeeee;" 
src="https://3dviewer.net/embed.html#model=https://raw.githubusercontent.com/lassoan/Test/master/SPL-Abdominal-Atlas.gltf"&gt;
&lt;/iframe&gt;
</code></pre>
<iframe width="640" height="480" src="https://3dviewer.net/embed.html#model=https://raw.githubusercontent.com/lassoan/Test/master/SPL-Abdominal-Atlas.gltf"></iframe>
<p>3dviewer is nice because it is free and open-source (see <a href="https://github.com/kovacsv/Online3DViewer">github page</a>), so it can be easily used in any project and customized and extended as needed.</p>
<p>There are a few more sample atlas files (head, knee, abdominal) <a href="https://github.com/PerkLab/SlicerOpenAnatomy/releases/tag/SampleData">here</a>.</p>

---

## Post #8 by @slicer365 (2021-12-18 01:27 UTC)

<p>Sorry，how can  I  get the new  OpenAnatomy?</p>
<p>I have downloaded again the extention,but it is still the old version.</p>

---

## Post #9 by @lassoan (2021-12-18 02:06 UTC)

<p>The Extensions Manager updates the extensions every night. If you want to get the update immediately then you need to download and update this file on your computer manually:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/PerkLab/SlicerOpenAnatomy/blob/master/OpenAnatomyExport/OpenAnatomyExport.py">
  <header class="source">

      <a href="https://github.com/PerkLab/SlicerOpenAnatomy/blob/master/OpenAnatomyExport/OpenAnatomyExport.py" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/PerkLab/SlicerOpenAnatomy/blob/master/OpenAnatomyExport/OpenAnatomyExport.py" target="_blank" rel="noopener">PerkLab/SlicerOpenAnatomy/blob/master/OpenAnatomyExport/OpenAnatomyExport.py</a></h4>


    <pre><code class="lang-py">import os
import re
import unittest
from unittest.runner import TextTestResult
import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
import logging

#
# OpenAnatomyExport
#

class OpenAnatomyExport(ScriptedLoadableModule):
  """Uses ScriptedLoadableModule base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def __init__(self, parent):
    ScriptedLoadableModule.__init__(self, parent)
    self.parent.title = "OpenAnatomy Export"
</code></pre>


  This file has been truncated. <a href="https://github.com/PerkLab/SlicerOpenAnatomy/blob/master/OpenAnatomyExport/OpenAnatomyExport.py" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #10 by @slicer365 (2021-12-18 04:05 UTC)

<p>Thank you very much! <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=10" title=":+1:" class="emoji" alt=":+1:"> <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=10" title=":+1:" class="emoji" alt=":+1:"> <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=10" title=":+1:" class="emoji" alt=":+1:"> <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=10" title=":+1:" class="emoji" alt=":+1:"></p>

---

## Post #11 by @lassoan (2022-01-26 20:08 UTC)

<p>I would just add that with this viewer it is very easy to share 3D models using Dropbox, to be viewed on desktop computer or on a phone:</p>
<ul>
<li>Copy the file into your Dropbox</li>
<li>Right-click on it and choose <code>Copy dropbox link</code></li>
<li>Prepend the <code>https://3dviewer.net/#model=</code> to the link to create a link that you can send anyone to view the model anywhere, even on a phone</li>
</ul>
<p>The model is not uploaded to any server when it is viewed (it remains on Dropbox) and only those people can access it who know the link.</p>
<h3><a name="p-73010-example-1" class="anchor" href="#p-73010-example-1" aria-label="Heading link"></a>Example</h3>
<p>Dropbox download link:<br>
<code>https://www.dropbox.com/s/38arwo2uhzu0ydg/SPL-Abdominal-Atlas.gltf?dl=0</code></p>
<p>Link to view the model:<br>
<code>https://3dviewer.net/#model=https://www.dropbox.com/s/38arwo2uhzu0ydg/SPL-Abdominal-Atlas.gltf?dl=0</code></p>

---

## Post #12 by @slicer365 (2022-01-27 00:55 UTC)

<aside class="quote no-group quote-modified" data-username="lassoan" data-post="11" data-topic="21082">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a href="https://3dviewer.net/#model=https://www.dropbox.com/s/38arwo2uhzu0ydg/SPL-Abdominal-Atlas.gltf?dl=0" class="inline-onebox" rel="noopener nofollow ugc">Online 3D Viewer</a></p>
</blockquote>
</aside>
<p>However it is hard to change model’s transparent.</p>

---

## Post #13 by @lassoan (2022-01-27 00:59 UTC)

<aside class="quote no-group" data-username="slicer365" data-post="12" data-topic="21082">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/slicer365/48/67549_2.png" class="avatar"> slicer365:</div>
<blockquote>
<p>However it is hard to change model’s transparent.</p>
</blockquote>
</aside>
<p>It takes a single click to show/hide an object or an entire branch of the tree. If you really want to change transparency instead of quickly toggling visibility then you could add that feature to the web viewer (<a href="http://3dviewer.net">3dviewer.net</a> is open-source) or have a look at <a href="https://github.com/PerkLab/SlicerOpenAnatomy/#gltf-viewers">other web viewers</a> that might better match what you want to do.</p>

---
