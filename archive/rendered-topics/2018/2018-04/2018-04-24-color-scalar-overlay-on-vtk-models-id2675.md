# Color scalar overlay on VTK models

**Topic ID**: 2675
**Date**: 2018-04-24
**URL**: https://discourse.slicer.org/t/color-scalar-overlay-on-vtk-models/2675

---

## Post #1 by @priya.vada4 (2018-04-24 17:18 UTC)

<p>Hi</p>
<p>Is it possible to overlay a color scalar value from an RGB image on a VTK model in Slicer?</p>
<p>I tried to setup the color scalar in the following way but when the model is displayed in Slicer, it does not show the image scalar and defaults to another color table.</p>
<pre><code>vtkSmartPointer&lt;vtkUnsignedCharArray&gt; ColorArray = vtkSmartPointer&lt;vtkUnsignedCharArray&gt;::New();
ColorArray-&gt;SetName("ModelColor");
ColorArray-&gt;SetNumberOfComponents(3);
...ColorArray initialized here...
this-&gt;ModelPoly-&gt;GetPointData()-&gt;SetScalars(ColorArray);
</code></pre>
<p>Thanks</p>

---

## Post #3 by @adamrankin (2018-04-24 18:03 UTC)

<p>In the model module, have you scrolled down to the Scalars collapsible button to enable scalar colorization?</p>

---

## Post #4 by @RafaelPalomar (2018-04-25 05:03 UTC)

<p>Hello Priya.</p>
<p>When you say color scalar from an RGB image, does that mean that you want to apply a texture to a model? If so, you can have a look at <a href="https://discourse.slicer.org/t/gpu-based-projective-texture-mapping-in-a-loadable-module/941">GPU-based Projective Texture Mapping in a Loadable Module</a> and see if you find some answers there.</p>
<p>If what you really want is applying scalar color values, you can have a look at <a href="https://github.com/RafaelPalomar/vtkColorCellsRGBA" rel="nofollow noopener">https://github.com/RafaelPalomar/vtkColorCellsRGBA</a> for an example on mapping RGBA scalars to a model (this is a VTK example, but you can use it in 3D Slicer. To enable the visualization of scalars you can use the Models module as suggested by <a class="mention" href="/u/adamrankin">@adamrankin</a> or programmatically by calling vtkMRMLModelDisplayNode::ScalarVisibilityOn() (<a href="http://apidocs.slicer.org/master/classvtkMRMLDisplayNode.html#a9dd055841d24d46216c72f5cce97e6e8" rel="nofollow noopener">http://apidocs.slicer.org/master/classvtkMRMLDisplayNode.html#a9dd055841d24d46216c72f5cce97e6e8</a>) from the vtkMRMLModelDisplayNode corresponding to your vtkMRMLModelNode.</p>
<p>I hope this helps.<br>
Rafael.</p>

---

## Post #5 by @priya.vada4 (2018-04-26 19:01 UTC)

<p>Thank you, Adam and Rafael.</p>
<p>I am looking to apply a texture on the model. I still seem to have a problem displaying texture on the model.</p>
<p>I have computed the color at every point and I am trying to save the texture as a scalar for the model. I am able to display the texture as a scalar field on the model. However, the color mapping seems completely off and the original colors of the texture are not displayed. As a check, when I use the <code>this-&gt;ModelDisplayNode-&gt;SetAndObserveColorNodeID("vtkMRMLColorTableNodeGrey");</code> the texture shows correctly on the model, although in grayscale. I have set AutoScalarRange to zero and disabled the choice of the ColorNode but still the original colors of the texture are not being displayed.</p>
<p>Thanks</p>

---

## Post #6 by @lassoan (2018-04-26 19:23 UTC)

<p>This topic should answer your questions, but feel free to follow up here, if something is not clear:</p>
<aside class="quote" data-post="1" data-topic="2521">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/displaying-textured-3d-models/2521">Displaying textured 3D models</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    I have a PLY made from a stereophotogrammatic scanner. It also has a texture file in jpg format. I tried setting the option for these texture files to “scalar overlay” and asked it to apply to the model I already loaded. When I do that, nothing happens, no error message nor the trace of the texture files as far as I can tell. There is no scalar listed under the “Scalar” tab of the models module. 
This is with 4.8.1 on windows.
  </blockquote>
</aside>


---
