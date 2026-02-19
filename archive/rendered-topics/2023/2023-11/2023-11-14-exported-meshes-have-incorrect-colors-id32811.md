---
topic_id: 32811
title: "Exported Meshes Have Incorrect Colors"
date: 2023-11-14
url: https://discourse.slicer.org/t/32811
---

# Exported meshes have incorrect colors

**Topic ID**: 32811
**Date**: 2023-11-14
**URL**: https://discourse.slicer.org/t/exported-meshes-have-incorrect-colors/32811

---

## Post #1 by @jaimigray (2023-11-14 14:22 UTC)

<p>I’m exporting multiple models for my skull anatomy models. I cannot get Slicer to export my models with their colors. Anyone know how to get the models exported with their colors? I have tried exporting them in several different file formats with no success.</p>
<p>here are the models in 3D slicer with their original colors:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/68df4bf637f1c67efbf34461165c617c70af097b.png" data-download-href="/uploads/short-url/eXK4ddCX4qcuqx0HOqfXh5TQi15.png?dl=1" title="Screenshot 2023-11-14 091720" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/68df4bf637f1c67efbf34461165c617c70af097b_2_690x403.png" alt="Screenshot 2023-11-14 091720" data-base62-sha1="eXK4ddCX4qcuqx0HOqfXh5TQi15" width="690" height="403" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/68df4bf637f1c67efbf34461165c617c70af097b_2_690x403.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/68df4bf637f1c67efbf34461165c617c70af097b.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/68df4bf637f1c67efbf34461165c617c70af097b.png 2x" data-dominant-color="292824"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-11-14 091720</span><span class="informations">873×510 197 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>here are the models in Blender (in OBJ format) after export. The colors appear muted and the hex codes have changed:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8e35dde5605f264d7d851b2088dcd78475e56477.png" data-download-href="/uploads/short-url/ki3d0FdfeEMOjUSpKlS5gpLhyFV.png?dl=1" title="Screenshot 2023-11-14 091746" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8e35dde5605f264d7d851b2088dcd78475e56477_2_690x409.png" alt="Screenshot 2023-11-14 091746" data-base62-sha1="ki3d0FdfeEMOjUSpKlS5gpLhyFV" width="690" height="409" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8e35dde5605f264d7d851b2088dcd78475e56477_2_690x409.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8e35dde5605f264d7d851b2088dcd78475e56477_2_1035x613.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8e35dde5605f264d7d851b2088dcd78475e56477.png 2x" data-dominant-color="2B2B2A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-11-14 091746</span><span class="informations">1108×658 304 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2023-11-14 15:01 UTC)

<p>Are you certain those aren’t the correct colors?  It looks to me like they are just different lighting parameters.  Can you try adjusting the lights?  Can you give some examples of that numbers changed?</p>

---

## Post #3 by @jaimigray (2023-11-14 15:04 UTC)

<p>I have tried adjusting the lights. It’s definitely a change in color. For example, in Slicer I set the color of the frontal (the light blue bone) to <span class="hashtag-raw">#7de8e1</span>, and then when I import the file into Blender the hex code has changed to <span class="hashtag-raw">#709694</span></p>

---

## Post #4 by @muratmaga (2023-11-14 16:47 UTC)

<p>Are you exporting them via the OpenAnatomy extension? Do you have the same color problem if you export them at glTF?</p>

---

## Post #5 by @jaimigray (2023-11-14 17:28 UTC)

<p>The Openanatomy extension in glTF gets me closer to the true colors, but they are still distorted. Now my frontal has a hex code of <span class="hashtag-raw">#90F5F0</span>, still not the original code I assigned in slicer. Here’s a screenshot:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af0a6959332c0173372be5268e12f759d0fbdbf9.jpeg" data-download-href="/uploads/short-url/oYtRyPWbY1B4OKCv5g7TXkpp9SV.jpeg?dl=1" title="Screenshot 2023-11-14 122552" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af0a6959332c0173372be5268e12f759d0fbdbf9_2_690x454.jpeg" alt="Screenshot 2023-11-14 122552" data-base62-sha1="oYtRyPWbY1B4OKCv5g7TXkpp9SV" width="690" height="454" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af0a6959332c0173372be5268e12f759d0fbdbf9_2_690x454.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af0a6959332c0173372be5268e12f759d0fbdbf9_2_1035x681.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af0a6959332c0173372be5268e12f759d0fbdbf9.jpeg 2x" data-dominant-color="33322F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-11-14 122552</span><span class="informations">1232×811 49.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @jaimigray (2023-11-14 17:29 UTC)

<p>I should add for these models, the hex codes are important. These models are part of a collection where the colors of the bones need to be comparable between models. These are models I have made over the years in different software - first Avizo, then VGStudio, and now Slicer.</p>

---

## Post #7 by @pieper (2023-11-14 18:45 UTC)

<p>In addition to glTF via OpenAnatomy, what other methods have you tried?</p>

---

## Post #8 by @jaimigray (2023-11-14 19:36 UTC)

<p>I’ve tried exporting as stl and ply models (these had no color at all).</p>

---

## Post #9 by @pieper (2023-11-14 21:40 UTC)

<p>It looks like that’s being done on purpose:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/PerkLab/SlicerOpenAnatomy/blob/ce61de8995aebdbf0ff0e7293f6d41aef1019568/OpenAnatomyExport/OpenAnatomyExport.py#L522-L542">
  <header class="source">

      <a href="https://github.com/PerkLab/SlicerOpenAnatomy/blob/ce61de8995aebdbf0ff0e7293f6d41aef1019568/OpenAnatomyExport/OpenAnatomyExport.py#L522-L542" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/PerkLab/SlicerOpenAnatomy/blob/ce61de8995aebdbf0ff0e7293f6d41aef1019568/OpenAnatomyExport/OpenAnatomyExport.py#L522-L542" target="_blank" rel="noopener">PerkLab/SlicerOpenAnatomy/blob/ce61de8995aebdbf0ff0e7293f6d41aef1019568/OpenAnatomyExport/OpenAnatomyExport.py#L522-L542</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="522" style="counter-reset: li-counter 521 ;">
          <li>colorRGB = displayNode.GetColor()</li>
          <li>if displayNode.GetInterpolation() == slicer.vtkMRMLDisplayNode.PBRInterpolation:</li>
          <li>  actor.GetProperty().SetColor(colorRGB[0], colorRGB[1], colorRGB[2])</li>
          <li>  actor.GetProperty().SetInterpolationToPBR()</li>
          <li>  actor.GetProperty().SetMetallic(displayNode.GetMetallic())</li>
          <li>  actor.GetProperty().SetRoughness(displayNode.GetRoughness())</li>
          <li>else:</li>
          <li>  if boostGouraudColor:</li>
          <li>    bf = colorRGB</li>
          <li>    colorHSV = [0, 0, 0]</li>
          <li>    vtk.vtkMath.RGBToHSV(colorRGB, colorHSV)</li>
          <li>    colorHSV[1] = min(colorHSV[1] * self.saturationBoost, 1.0)  # increase saturation</li>
          <li>    colorHSV[2] = min(colorHSV[2] * self.brightnessBoost, 1.0)  # increase brightness</li>
          <li>    colorRGB = [0, 0, 0]</li>
          <li>    vtk.vtkMath.HSVToRGB(colorHSV, colorRGB)</li>
          <li>  actor.GetProperty().SetColor(colorRGB[0], colorRGB[1], colorRGB[2])</li>
          <li>  actor.GetProperty().SetInterpolationToGouraud()</li>
          <li>  actor.GetProperty().SetAmbient(displayNode.GetAmbient())</li>
          <li>  actor.GetProperty().SetDiffuse(displayNode.GetDiffuse())</li>
          <li>  actor.GetProperty().SetSpecular(displayNode.GetSpecular())</li>
          <li>  actor.GetProperty().SetSpecularPower(displayNode.GetPower())</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>If you want to try a workaround you could force <code>boostGouraudColor</code> to be False in this line:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/PerkLab/SlicerOpenAnatomy/blob/ce61de8995aebdbf0ff0e7293f6d41aef1019568/OpenAnatomyExport/OpenAnatomyExport.py#L220">
  <header class="source">

      <a href="https://github.com/PerkLab/SlicerOpenAnatomy/blob/ce61de8995aebdbf0ff0e7293f6d41aef1019568/OpenAnatomyExport/OpenAnatomyExport.py#L220" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/PerkLab/SlicerOpenAnatomy/blob/ce61de8995aebdbf0ff0e7293f6d41aef1019568/OpenAnatomyExport/OpenAnatomyExport.py#L220" target="_blank" rel="noopener">PerkLab/SlicerOpenAnatomy/blob/ce61de8995aebdbf0ff0e7293f6d41aef1019568/OpenAnatomyExport/OpenAnatomyExport.py#L220</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="210" style="counter-reset: li-counter 209 ;">
          <li>modelNodes = vtk.vtkCollection()</li>
          <li>shNode.GetDataNodesInBranch(inputShFolderItemId, modelNodes, "vtkMRMLModelNode")</li>
          <li>planeNodes = vtk.vtkCollection()</li>
          <li>shNode.GetDataNodesInBranch(inputShFolderItemId, planeNodes, "vtkMRMLMarkupsPlaneNode")</li>
          <li>self._numberOfExpectedModels = modelNodes.GetNumberOfItems() + planeNodes.GetNumberOfItems()</li>
          <li>self._numberOfProcessedModels = 0</li>
          <li>self._gltfNodes = []</li>
          <li>self._gltfMeshes = []</li>
          <li></li>
          <li># Add models to a self._renderer</li>
          <li class="selected">self.addModelsToRenderer(inputShFolderItemId, boostGouraudColor = (outputFormat == "glTF"))</li>
          <li></li>
          <li>if self._exportToFile:</li>
          <li>  outputFileName = inputName</li>
          <li>  # import datetime</li>
          <li>  # dateTimeStr = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")</li>
          <li>  # outputFileName += dateTimeStr</li>
          <li>  outputFilePathBase = os.path.join(outputFolder, outputFileName)</li>
          <li>  if outputFormat == "glTF":</li>
          <li>    exporter = vtk.vtkGLTFExporter()</li>
          <li>    outputFilePath = outputFilePathBase+'.gltf'</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The module file would be someplace like ~/Downloads/Slicer-5.4.0-linux-amd64/slicer.org/Extensions-31938/SlicerOpenAnatomy/lib/Slicer-5.4/qt-scripted-modules/OpenAnatomyExport.py and you could just restart the application after editing that line to be something like <code>self.addModelsToRenderer(inputShFolderItemId, boostGouraudColor=False)</code></p>
<p><a class="mention" href="/u/jaimigray">@jaimigray</a> Your use case sounds valid, so probably it would be good to expose an advanced option in the GUI to disable this feature.  <a class="mention" href="/u/mhalle">@mhalle</a> <a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #10 by @muratmaga (2023-11-14 21:45 UTC)

<p><a class="mention" href="/u/jaimigray">@jaimigray</a> you can also enable developer mode (under application settings-&gt;Developer), and then when you restart the application, you will see these buttons for Python scripted modules like Open Anatomy. You can then click Edit and make the change <a class="mention" href="/u/pieper">@pieper</a> suggested, save and hit restart.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4efbc366ea8f23b683008aa1893d2ecbf9ab88ca.png" alt="image" data-base62-sha1="bgIDRTQj7OlIHRjU3wURRMAadke" width="627" height="422"></p>

---

## Post #11 by @lassoan (2023-11-14 22:57 UTC)

<p>Matching model appearance between applications is very hard, because they use different lighting models with potentially very different parametrization. I implemented color “boosting” by experimentation as described here:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/PerkLab/SlicerOpenAnatomy/blob/ce61de8995aebdbf0ff0e7293f6d41aef1019568/OpenAnatomyExport/OpenAnatomyExport.py#L144-L150">
  <header class="source">

      <a href="https://github.com/PerkLab/SlicerOpenAnatomy/blob/ce61de8995aebdbf0ff0e7293f6d41aef1019568/OpenAnatomyExport/OpenAnatomyExport.py#L144-L150" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/PerkLab/SlicerOpenAnatomy/blob/ce61de8995aebdbf0ff0e7293f6d41aef1019568/OpenAnatomyExport/OpenAnatomyExport.py#L144-L150" target="_blank" rel="noopener">PerkLab/SlicerOpenAnatomy/blob/ce61de8995aebdbf0ff0e7293f6d41aef1019568/OpenAnatomyExport/OpenAnatomyExport.py#L144-L150</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="144" style="counter-reset: li-counter 143 ;">
          <li># Slicer uses Gouraud lighting model by default, while glTF requires PBR.</li>
          <li># Material properties conversion in VTK makes the model appear in glTF very dull, faded out,</li>
          <li># therefore if we export models with Gouraud lighting we adjust the saturation and brightness.</li>
          <li># By testing on a few anatomical atlases, saturation increase by 1.5x and no brightness</li>
          <li># change seems to be working well.</li>
          <li>self.saturationBoost = 1.5</li>
          <li>self.brightnessBoost = 1.0</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>This may be inaccurate, if someone has time to dig into how to better convert colors between different lighting models then it would be awesome. For example, here someone seems to have an idea of a better approximation (but maybe that only addresses RGB/sRGB color space and not Gouraud/PBR lighting model difference): <a href="https://stackoverflow.com/a/66479140" class="inline-onebox">glTF - setting colors - baseColorFactor - Stack Overflow</a></p>
<p>For better consistency of colors between Slicer and Blender you can set shading to PBR in models module in Slicer. We then don’t modify the RGB color codes in OpenAnatomy export. Overall appearance will be still very different in Slicer and Blender because default lights in the scene are very different in the two applications.</p>
<aside class="quote no-group" data-username="jaimigray" data-post="6" data-topic="32811">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jaimigray/48/67886_2.png" class="avatar"> jaimigray:</div>
<blockquote>
<p>I should add for these models, the hex codes are important.</p>
</blockquote>
</aside>
<p>You can choose to encode some information in various color fields, but colors may not remain exactly the same when you import/export into a software or convert to a different mesh file format. Most mesh file formats allow you to define parts of a mesh in more robust ways, I would recommend relying on those mechanisms instead of color similarity.</p>
<p><a class="mention" href="/u/mhalle">@mhalle</a> has been working a lot on storing anatomical atlases, maybe he can give you further advice.</p>

---

## Post #12 by @tsehrhardt (2023-11-15 16:54 UTC)

<p>What about writing per vertex color instead of a material file? That seems to give me the most consistency between applications for models that just need solid color.</p>

---

## Post #13 by @jaimigray (2023-11-15 17:33 UTC)

<p>Is there a way to do this in Slicer? This is how I color my models in VGStudio (as PLY files), and the colors are always consistent when exported into other software</p>

---

## Post #14 by @lassoan (2023-11-15 17:43 UTC)

<p>I don’t think standard OBJ can store per-vertex color, but for for example PLY can, so a PLY option could be added to OpenAnatomy exporter if that solved some problem.</p>
<p>However, if the main need is to identify parts of a mesh then it is more robust to rely on materials in OBJ files (one material for each segment, as we do it now) or use mesh hierarchy in glTF files. Color component values may change because the color space of the application may not be the same as the color space of the file (and there is often not even an accurate correspondence of colors between different color spaces).</p>

---

## Post #15 by @muratmaga (2023-11-15 17:44 UTC)

<aside class="quote no-group" data-username="jaimigray" data-post="13" data-topic="32811" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jaimigray/48/67886_2.png" class="avatar"> jaimigray:</div>
<blockquote>
<p>Is there a way to do this in Slicer? This is how I color my models in VGStudio (as PLY files), and the colors are always consistent when exported into other software</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a> this actually would be something I would second too.</p>

---

## Post #16 by @lassoan (2023-11-15 17:52 UTC)

<aside class="quote no-group" data-username="jaimigray" data-post="13" data-topic="32811">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jaimigray/48/67886_2.png" class="avatar"> jaimigray:</div>
<blockquote>
<p>This is how I color my models in VGStudio (as PLY files), and the colors are always consistent when exported into other software</p>
</blockquote>
</aside>
<p>How do you use the per-vertex colors? In what software, for what purpose? Only rendering or also for processing? Do you need to show/hide individual structures?</p>
<aside class="quote no-group" data-username="jaimigray" data-post="13" data-topic="32811">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jaimigray/48/67886_2.png" class="avatar"> jaimigray:</div>
<blockquote>
<p>Is there a way to do this in Slicer?</p>
</blockquote>
</aside>
<p>It would take maybe 20-30 lines of Python code in the OpenAnatomy exporter to add a vertex color array and set a different value for each segment. It could be a good task for someone who wants to learn a bit of VTK and Python scripting (probably chatgpt/bingchat can generate the code and it would just need to be copied into the Slicer module).</p>

---

## Post #17 by @jaimigray (2023-11-15 18:03 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="16" data-topic="32811">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>How do you use the per-vertex colors? In what software, for what purpose? Only rendering or also for processing? Do you need to show/hide individual structures?</p>
</blockquote>
</aside>
<p>I use the per-vertex colors mostly for my Sketchfab models, see here: <a href="https://skfb.ly/oAtAS" class="inline-onebox" rel="noopener nofollow ugc">Colors of Skull Anatomy - A 3D model collection by Blackburn Lab (@ufherps) - Sketchfab</a><br>
These models are made up of multiple mesh files. I import the models into Blender to do any clean-up and to animate them, and then Blender has a handy Sketchfab plugin to upload directly to Sketchfab. Without the vertex colors (or material colors), extra steps are required to color the meshes in Blender. It would be a big time-saver if I could just keep the original colors on the mesh from the segmentation software, like VGStudio allows.</p>

---

## Post #18 by @jaimigray (2023-11-15 18:07 UTC)

<p>VGstudio also lets me write per-vertex colors onto meshes using volume renders, allowing me to create meshes as per-vertex colored PLY files. This feature is really useful for creating meshes with density heat-maps, or for creating some nice shading effects that can make the meshes look more bone-like</p>

---

## Post #19 by @lassoan (2023-11-15 19:24 UTC)

<aside class="quote no-group" data-username="jaimigray" data-post="18" data-topic="32811">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jaimigray/48/67886_2.png" class="avatar"> jaimigray:</div>
<blockquote>
<p>VGstudio also lets me write per-vertex colors onto meshes using volume renders,</p>
</blockquote>
</aside>
<p>It sounds like the feature you are looking for is provided by “Probe volume with model” module. It can write the values of the input volume directly into the mesh.</p>

---

## Post #20 by @muratmaga (2023-11-16 16:06 UTC)

<p>I tried this, but I don’t think the chosen transfer function for volume rendering has any impact on the outcome of the model generated. There is a texture, but that texture is independent of the transfer function specified.</p>

---

## Post #21 by @mikebind (2023-11-16 16:29 UTC)

<p>The values for the texture are drawn from the volume voxel values, not from the rendering.  If you convert the segmentation to a labelmap volume and probe that, the label values would be on the mesh (although I suspect there is interpolation involved, which might result in undesired fractional values of labels near boundaries, and it would be label values and not color values which would be stored).  I don’t know if you could probe an RGB volume and get out all three scalar values using “Probe volume with model”.  It looks like that may be within the capabilities of vtkProbeFilter, but was probably not the imagined use case when the Slicer module was being put together.</p>

---

## Post #22 by @lassoan (2023-11-16 19:19 UTC)

<p>Correct, volume rendering transfer functions do not affect probing. If you probe a scalar volume then you can apply transfer functions on the values by a couple of lines of Python code (get the array and run each value through the color transfer function).</p>
<p>We played with this a bit on RGB volumes (cryosection data) and the <a href="https://discourse.slicer.org/t/retain-image-color-in-volume-rendering/12294/24">result was pretty disappointing</a>. It was not surprising, because segment surfaces tend to have fairly uniform color (non-uniformities are usually under the surface). Therefore, we did not continue exploring “saving volume rendering as colored surface”.</p>
<p>If you have examples of surface rendering beautifully displaying volume rendering results then we can revisit this. Can you share a few examples that shows the volume rendering and colored surface rendering?</p>

---
