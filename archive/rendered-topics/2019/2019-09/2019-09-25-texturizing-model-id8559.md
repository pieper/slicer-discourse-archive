---
topic_id: 8559
title: "Texturizing Model"
date: 2019-09-25
url: https://discourse.slicer.org/t/8559
---

# Texturizing model

**Topic ID**: 8559
**Date**: 2019-09-25
**URL**: https://discourse.slicer.org/t/texturizing-model/8559

---

## Post #1 by @rprueckl (2019-09-25 10:46 UTC)

<p>Hi,</p>
<p>I want to texturize a 3d model, but do not want to install the SlicerIGT extension. So, I tried to implement the application of the texture similar to this:<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/SlicerIGT/SlicerIGT/blob/00ff9bf070d538d5c713bfc375f544ee4e8033bc/TextureModel/TextureModel.py#L139-L145" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerIGT/SlicerIGT/blob/00ff9bf070d538d5c713bfc375f544ee4e8033bc/TextureModel/TextureModel.py#L139-L145" target="_blank" rel="nofollow noopener">SlicerIGT/SlicerIGT/blob/00ff9bf070d538d5c713bfc375f544ee4e8033bc/TextureModel/TextureModel.py#L139-L145</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="139" style="counter-reset: li-counter 138 ;">
<li>def showTextureOnModel(self, modelNode, textureImageNode):</li>
<li>  modelDisplayNode = modelNode.GetDisplayNode()</li>
<li>  modelDisplayNode.SetBackfaceCulling(0)</li>
<li>  textureImageFlipVert = vtk.vtkImageFlip()</li>
<li>  textureImageFlipVert.SetFilteredAxis(1)</li>
<li>  textureImageFlipVert.SetInputConnection(textureImageNode.GetImageDataConnection())</li>
<li>  modelDisplayNode.SetTextureImageDataConnection(textureImageFlipVert.GetOutputPort())</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>My code looks like this:</p>
<pre><code class="lang-auto">// assign as texture to model
vtkMRMLModelNode* modelNode = ...
vtkMRMLModelDisplayNode* modelDisplayNode = vtkMRMLModelDisplayNode::SafeDownCast(modelNode-&gt;GetDisplayNode());
modelDisplayNode-&gt;SetBackfaceCulling(0);
vtkSmartPointer&lt;vtkImageFlip&gt; textureImageFlipVert = vtkImageFlip::New();
textureImageFlipVert-&gt;SetFilteredAxis(1);
textureImageFlipVert-&gt;SetInputConnection(textureNode-&gt;GetImageDataConnection());
modelDisplayNode-&gt;SetTextureImageDataConnection(textureImageFlipVert-&gt;GetOutputPort());
</code></pre>
<p>The problem is, that VTK warns me that instances of <code>vtkImageFlip</code> are still around on program exit. What is the proper way to achieve my goal in this case? Ideally, I would be able to remove the volume node from the scene again after the application to the model, as I don’t need it anymore then.</p>

---

## Post #2 by @lassoan (2019-09-25 20:22 UTC)

<aside class="quote no-group" data-username="rprueckl" data-post="1" data-topic="8559">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rprueckl/48/4240_2.png" class="avatar"> rprueckl:</div>
<blockquote>
<p>The problem is, that VTK warns me that instances of <code>vtkImageFlip</code> are still around on program exit.</p>
</blockquote>
</aside>
<p><code>vtkSmartPointer&lt;vtkImageFlip&gt; textureImageFlipVert = vtkImageFlip::New();</code> is the problem. A <code>vtkSmartPointer</code> must be initialized with a <code>vtkSmartPointer&lt;&gt;::New</code>.</p>
<p>A proper solution would be to add better support for textured models in Slicer core.</p>
<ul>
<li>Add node reference to vtkMRMLModelNode to be able to refer to a vtkMRMLVolumeNode to store texture. This would ensure that if you save and load the scene, the texture would remain on the model node. This could be implemented in about 10-20 lines.</li>
<li>Add GUI to models module to select a texture volume. Minor edit, 20-30 lines of code.</li>
<li>Add function to models module to convert texture image to point or cell scalars. This is what is implemented in SlicerIGT, so it should not be too hard to port it to C++.</li>
</ul>

---

## Post #3 by @rprueckl (2019-09-26 07:00 UTC)

<p>Ooh, sometimes blindness overcomes me… Thanks!</p>
<p>I will look into that, maybe I can provide a draft implementation for that.<br>
One question to this:</p>
<blockquote>
<ul>
<li>Add node reference to vtkMRMLModelNode to be able to refer to a vtkMRMLVolumeNode to store texture. This would ensure that if you save and load the scene, the texture would remain on the model node. This could be implemented in about 10-20 lines.</li>
</ul>
</blockquote>
<p>Is setting a reference enough for that? After loading, of course the reference to the correct volume node would be there, but I guess that the texture is not applied automatically then? Can you point me to an example where a node association between two nodes is re-established after loading a scene? Thanks.</p>

---
