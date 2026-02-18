# GPU-based Projective Texture Mapping in a Loadable Module

**Topic ID**: 941
**Date**: 2017-08-25
**URL**: https://discourse.slicer.org/t/gpu-based-projective-texture-mapping-in-a-loadable-module/941

---

## Post #1 by @thaenel (2017-08-25 00:09 UTC)

<p>Hello everyone,</p>
<p>I want to create my first Slicer extension. At the moment I am doing research on the design of the extension (mostly reading Slicer API documentation), after this is done I’ll inform you about my plan.</p>
<h2>Task</h2>
<p>One loadable module that I want to include, requires me to perform <a href="https://en.wikipedia.org/wiki/Projective_texture_mapping" rel="nofollow noopener"><em>Projective Texture Mapping</em></a>. In short, this is the projection of a 2D image onto a 3D surface. Because the texture and its position in the scene is changing in real time, I decided to implement this algorithm with an GPU-based approach similar to <a href="https://en.wikipedia.org/wiki/Shadow_mapping#Algorithm_overview" rel="nofollow noopener"><em>Shadow Mapping</em></a>. Therefore I need to perform two render passes:</p>
<ol>
<li>render the 3D surface with a viewport that is aligned with the 2D image in world space to obtain a depth buffer</li>
<li>render the 3D surface with the desired viewport, project its fragments/vertices onto the 2D image to obtain the color and only draw them if their distance to the image plane matches the one in the depth buffer</li>
</ol>
<h2>Problem</h2>
<p>Unfortunately implementing such a custom rendering processes isn’t that easy as I thought it would be. If I were to implement this with VTK, I would try to replace the shaders of <a href="http://www.vtk.org/doc/nightly/html/classvtkOpenGLPolyDataMapper.html" rel="nofollow noopener"><code>vtkOpenGLPolyDataMapper</code></a> as described <a href="http://www.vtk.org/Wiki/Shaders_In_VTK" rel="nofollow noopener">here</a>.</p>
<p>As far as I know slicer encapsulates VTK, so that there is <strong>no direct access to the underlying <code>vtkMappers</code> or <code>vtkActors</code></strong>.</p>
<p>Does anyone have an idea on how to approach this problem?</p>
<h2>What I’ve got so far</h2>
<ul>
<li>2D RGB image represented as a <code>vtkMRMLVectorVolumeNode</code>
</li>
<li>3D surface represented as a <code>vtkMRMLModelNode</code>
</li>
<li>orientation and position of the image and the surface represeneted as a <code>vtkMRMLLinearTransformNode</code>
</li>
<li>obtain a <code>vtkRenderer</code> from the <code>vtkMRMLModelDisplayableManager</code>
</li>
<li>add a new <code>vtkActor</code> with a <code>vtkPolyDataMapper</code> to the <code>vtkRenderer</code>
</li>
<li>use custom shaders for the <code>vtkPolyDataMapper</code>
</li>
</ul>
<h2>Open questions</h2>
<ul>
<li>Are there any easier alternatives?</li>
<li>How do i get the <code>vtkMRMLModelDisplayableManager</code>?</li>
<li>Do I need to add new Actors and Mappers to the obtained Renderer or can I use existing ones?</li>
<li>What is the best way to perform the 2 render passes?</li>
</ul>
<p>Thank in advance,<br>
Tobias</p>

---

## Post #2 by @lassoan (2017-08-25 02:48 UTC)

<p>Model displayable manager can already apply texture to a model. See this module as an example: <a href="https://github.com/SlicerIGT/SlicerIGT/tree/master/TextureModel">https://github.com/SlicerIGT/SlicerIGT/tree/master/TextureModel</a></p>
<p>I guess VTK can compute the texture coordinates, so you should be able to implement projective mapping.</p>
<p>If this method is not fast enough or there are other limitations then you have to implement a custom displayable manager. You can use the model displayable manager as a starting point.</p>

---

## Post #3 by @pieper (2017-08-25 13:03 UTC)

<p>I’d suggest getting this to work in pure VTK first with a simple example and then you can adapt it to work in Slicer.</p>
<p>Did you look at this class?</p>
<p><a href="http://www.vtk.org/doc/nightly/html/classvtkProjectedTexture.html" class="onebox" target="_blank">http://www.vtk.org/doc/nightly/html/classvtkProjectedTexture.html</a></p>
<p>You can also have a look at how vtk8 with the OpenGL2 back end exposes render passes.</p>
<p>It seems that to do projected textures correctly you probably need to use some shader code - there’s some nice detail here:</p>
<aside class="onebox stackexchange">
  <header class="source">
      <a href="https://stackoverflow.com/questions/22732717/opengl-projective-texture-mapping-via-shaders" target="_blank">stackoverflow.com</a>
  </header>
  <article class="onebox-body">
      <a href="https://stackoverflow.com/users/3475956/avrdan" target="_blank">
    <img alt="Avrdan" src="https://www.gravatar.com/avatar/daa5822321f7420af55aaea42d9aaefd?s=128&amp;d=identicon&amp;r=PG&amp;f=1" class="thumbnail onebox-avatar" width="128" height="128">
  </a>
<h4>
  <a href="https://stackoverflow.com/questions/22732717/opengl-projective-texture-mapping-via-shaders" target="_blank">OpenGL Projective Texture Mapping via Shaders</a>
</h4>

<div class="tags">
  <strong>c++, opengl, mapping, textures</strong>
</div>

<div class="date">
  asked by
  
  <a href="https://stackoverflow.com/users/3475956/avrdan" target="_blank">
    Avrdan
  </a>
  on <a href="https://stackoverflow.com/questions/22732717/opengl-projective-texture-mapping-via-shaders" target="_blank">03:03PM - 29 Mar 14 UTC</a>
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #4 by @lassoan (2017-08-25 13:20 UTC)

<aside class="quote no-group quote-modified" data-username="pieper" data-post="3" data-topic="941">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Did you look at this class?</p>
<p><a href="http://www.vtk.org/doc/nightly/html/classvtkProjectedTexture.html" class="inline-onebox">VTK: vtkProjectedTexture Class Reference</a></p>
</blockquote>
</aside>
<p>It seems that this class can compute texture coordinates that the model displayable manager needs for texture display. So, you can get everything working with a short Python script, which sets up the vtkProjectedTexture filter parameters. Of course, this will be slower than a direct shader implementation but may be already usable.</p>

---
