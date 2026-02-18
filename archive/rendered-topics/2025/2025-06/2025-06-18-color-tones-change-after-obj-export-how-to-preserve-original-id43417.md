# Color tones change after OBJ export – how to preserve original shading?

**Topic ID**: 43417
**Date**: 2025-06-18
**URL**: https://discourse.slicer.org/t/color-tones-change-after-obj-export-how-to-preserve-original-shading/43417

---

## Post #1 by @JohnWick (2025-06-18 20:54 UTC)

<p>Dear 3D Slicer Developers and Community,</p>
<p>I am experiencing an issue when exporting one or more 3D models from 3D Slicer in OBJ format. While the original color itself (i.e., the RGB values) is preserved in the exported <code>.mtl</code> file, the rendered models appear significantly darker or have noticeably altered tones in external applications.</p>
<p>To illustrate the problem, I have attached a screenshot showing a side-by-side comparison of the same model in 3D Slicer and in an external viewer, along with the corresponding normalized RGB values from the <code>.mtl</code> file. It seems that the tone or brightness of the colors is not accurately preserved during export.</p>
<p>Has anyone encountered this before? Is there a known way to ensure that the visual appearance (including brightness and tone) of the colors set in Slicer are exported faithfully into the <code>.obj</code> + <code>.mtl</code> pair?</p>
<p>Any insights or suggestions on how to fix or work around this would be greatly appreciated.</p>
<p>Thank you in advance!</p>
<p>Best regards,<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9ed12519e794352bd0e25a5bdc2e9d844a5f06fc.png" data-download-href="/uploads/short-url/mEXwWcnW1HI1QsGLharJ021O0pK.png?dl=1" title="Screenshot 2025-06-18 223440" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9ed12519e794352bd0e25a5bdc2e9d844a5f06fc_2_676x500.png" alt="Screenshot 2025-06-18 223440" data-base62-sha1="mEXwWcnW1HI1QsGLharJ021O0pK" width="676" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9ed12519e794352bd0e25a5bdc2e9d844a5f06fc_2_676x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9ed12519e794352bd0e25a5bdc2e9d844a5f06fc_2_1014x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9ed12519e794352bd0e25a5bdc2e9d844a5f06fc.png 2x" data-dominant-color="A1A4A0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-06-18 223440</span><span class="informations">1059×783 218 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2025-06-19 02:19 UTC)

<p>What external application are you using to look at these model? The difference in rendering algorithms and shading might be the main reason you are not seeing them the same way.</p>

---

## Post #3 by @JohnWick (2025-06-19 09:57 UTC)

<p>Dear muratmaga,</p>
<p>Thank you for your response and for pointing out the potential role of rendering differences.</p>
<p>To clarify: we are using our own custom web-based OpenGL renderer to visualize the exported models. This renderer reads the <code>.obj</code> file along with its accompanying <code>.mtl</code> file, exactly as exported from 3D Slicer.</p>
<p>Upon inspecting the <code>.mtl</code> file, we observed that the normalized RGB values seem to be approximately one-third of the actual color intensity shown in 3D Slicer. This suggests that the brightness or tone is already altered in the exported <code>.mtl</code> file itself, even before rendering.</p>
<p>We would appreciate any insight into how 3D Slicer maps its internal color settings to the <code>.mtl</code> format upon export, and whether there is a recommended way to preserve the original appearance more accurately.</p>
<p>Best regards,</p>

---

## Post #4 by @JASON (2025-06-19 15:45 UTC)

<p><a class="mention" href="/u/johnwick">@JohnWick</a> I test and get the same result.  Export to OBJ from <code>Segmentations</code> module, or by converting the segmentation to model and export as OBJ will both result in the mtl file with RGB values that are exactly 1/3 the RGB values in Slicer.</p>
<p>If you install and export to OBJ using the <code>OpenAnatomy Export</code> module, the correct RGB values are used.</p>

---

## Post #5 by @JASON (2025-06-19 16:04 UTC)

<p>If you export to OBJ using python method <code>storageNode.WriteData()</code>, you get the same 1/3 RGB values:</p>
<pre><code class="lang-auto">outpath = r'X:\test1.obj'
modelNode = slicer.util.getNode('Segment_1')
storageNode = modelNode.GetStorageNode()
if not storageNode:
    storageNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLModelStorageNode")
    modelNode.SetAndObserveStorageNodeID(storageNode.GetID())
storageNode.SetFileName(outpath)
storageNode.SetWriteFileFormat('obj')
storageNode.WriteData(modelNode)
</code></pre>
<p>Export using VTK method <code>vtk.vtkOBJExporter()</code> will result in the correct RGB values being used :</p>
<pre><code class="lang-auto">outpath = r'X:\test2'

modelNode = slicer.util.getNode('Segment_1')
polyData = modelNode.GetPolyData()

displayNode = modelNode.GetDisplayNode()
color = displayNode.GetColor()
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputData(polyData)
actor = vtk.vtkActor()
actor.SetMapper(mapper)
actor.GetProperty().SetColor(color)
renderer = vtk.vtkRenderer()
renderer.AddActor(actor)
renderWindow = vtk.vtkRenderWindow()
renderWindow.AddRenderer(renderer)
renderWindowInteractor = vtk.vtkRenderWindowInteractor()
renderWindowInteractor.SetRenderWindow(renderWindow)
exporter = vtk.vtkOBJExporter()
exporter.SetRenderWindow(renderWindow)
exporter.SetFilePrefix(outpath)
exporter.Write()
</code></pre>

---

## Post #6 by @pieper (2025-06-19 16:12 UTC)

<p>The reason for that is in this block of code:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/main/Libs/MRML/Core/vtkMRMLModelStorageNode.cxx#L722-L732">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/main/Libs/MRML/Core/vtkMRMLModelStorageNode.cxx#L722-L732" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/main/Libs/MRML/Core/vtkMRMLModelStorageNode.cxx#L722-L732" target="_blank" rel="noopener">Libs/MRML/Core/vtkMRMLModelStorageNode.cxx</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/Slicer/Slicer/blob/main/Libs/MRML/Core/vtkMRMLModelStorageNode.cxx#L722-L732" rel="noopener"><code>main</code></a>
</div>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="722" style="counter-reset: li-counter 721 ;">
          <li>if (displayNode)</li>
          <li>{</li>
          <li>  double color[3] = { 0.5, 0.5, 0.5 };</li>
          <li>  displayNode-&gt;GetColor(color);</li>
          <li>  // OBJ exporter sets the same color for ambient, diffuse, specular</li>
          <li>  // so we scale it by 1/3 to avoid having too bright material.</li>
          <li>  double colorScale = 1.0 / 3.0;</li>
          <li>  actor-&gt;GetProperty()-&gt;SetColor(color[0] * colorScale, color[1] * colorScale, color[2] * colorScale);</li>
          <li>  actor-&gt;GetProperty()-&gt;SetSpecularPower(3.0);</li>
          <li>  actor-&gt;GetProperty()-&gt;SetOpacity(displayNode-&gt;GetOpacity());</li>
          <li>}</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I imagine different renderers make different use of these parameters, but if anyone knows of a definitive standard for OBJ/MTL or a test suite that defines how interchange should be handled then I think we should change Slicer’s behavior to match those standards.</p>

---

## Post #7 by @JohnWick (2025-06-19 19:44 UTC)

<p><a class="mention" href="/u/jason">@JASON</a> and <a class="mention" href="/u/pieper">@pieper</a> Thank you very much for your clear explanation — I really appreciate the detailed guidance!<br>
It seems to be a general issue; for that reason, I export the models in OBJ format and then multiply the <em>Kd</em> values in each <code>.mtl</code> file using the following code:</p>
<pre><code>import os

# Folder containing the .mtl files
folder = r"path"

# Loop over all .mtl files
for filename in os.listdir(folder):
  if filename.endswith(".mtl"):
      filepath = os.path.join(folder, filename)

      # Read the file lines
      with open(filepath, "r") as file:
          lines = file.readlines()

      # Modify Kd line
      new_lines = []
      for line in lines:
          if line.startswith("Kd "):
              parts = line.strip().split()
              # Convert to float and multiply by 3, with max value capped at 1.0
              kd_values = [min(1.0, float(x) * 3) for x in parts[1:]]
              new_line = "Kd " + " ".join(f"{v:.3f}" for v in kd_values) + "\n"
              new_lines.append(new_line)
          else:
              new_lines.append(line)

      # Write the modified lines back to the file
      with open(filepath, "w") as file:
          file.writelines(new_lines)
</code></pre>

---

## Post #8 by @JASON (2025-06-20 00:45 UTC)

<aside class="quote no-group" data-username="pieper" data-post="6" data-topic="43417">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>but if anyone knows of a definitive standard for OBJ/MTL or a test suite that defines how interchange should be handled</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/pieper">@pieper</a> The comment warns :</p>
<pre><code class="lang-auto">722. // OBJ exporter sets the same color for ambient, diffuse, specular
723. // so we scale it by 1/3 to avoid having too bright material.
</code></pre>
<p>but the actual behavior is the output .mtl only writes the 1/3 RGB value to the diffuse property and has <code>0 0 0</code> for ambient and specular.</p>
<pre><code class="lang-auto"># wavefront mtl file written by the visualization toolkit

newmtl mtl1
Ka 0 0 0
Kd 0.3333333333333333 0.3333333333333333 0.3333333333333333
Ks 0 0 0
Ns 3
Tr 1
illum 3
</code></pre>
<p>I think the most complete solution would be to set the specular, SpecularPower, ambient from the vtkProperty of the Slicer material. These are editable from UI in the <code>models</code> module.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/09d9749e3e36edb5d225360f909ddee00ba5e364.png" data-download-href="/uploads/short-url/1p8c07hpOQpKxKSI6tk0XNRajXK.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/09d9749e3e36edb5d225360f909ddee00ba5e364.png" alt="image" data-base62-sha1="1p8c07hpOQpKxKSI6tk0XNRajXK" width="438" height="172"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">438×172 7.51 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But the most straight-forward interpretation should be to map the label / model ‘<code>color</code>’ property to the mtl <code>diffuse</code> property at a 1:1 ratio.  I think it is reasonable to leave specular &amp; ambient values to <code>0 0 0,</code> as the exporter does now.</p>
<p>If you are making a change to the OBJ exporter, I would also consider altering the material name from the default value ‘<code>mtl1</code>’ to a unique name that matches the file output.</p>
<p>spleen.obj &gt; <code>spleen.mtl</code> contains:<br>
<code>newmtl spleen</code></p>
<p>This way, the material names are unique and identifiable to the to object it is assigned.  It’s difficult to manage many materials with the same name ‘<code>mtl1</code>’ in the external DCC application. I’ve made scripts to reassign material names in the DCC to match objects, but this would be a convenient default behavior.</p>

---

## Post #9 by @pieper (2025-06-20 00:51 UTC)

<p>Excellent suggestions <a class="mention" href="/u/jason">@JASON</a> .  <a class="mention" href="/u/lassoan">@lassoan</a>, git indicates this comment came from you; do you have thoughts on the topic?</p>

---

## Post #10 by @lassoan (2025-06-27 22:21 UTC)

<p>I’ve implemented material parameter adjustment on export because without that the meshes looked very bright, washed-out in Blender. The main problem is that Blender - and probably most other modern rendering engines - use physically based rendering (PBR), which works very differently than OBJ’s simple Phong-style model. It may not be possible to convert materials between these models in a way that preserves appearance across any lighting conditions.</p>
<p><a class="mention" href="/u/johnwick">@JohnWick</a> and <a class="mention" href="/u/jason">@JASON</a> what software and renderers do you use? What material properties do you set in the display node (Models module / 3D Display / Advanced → Ambient, Diffuse, Specular, Power)? What lights do you set up in the other software? Do you set custom lights in Slicer (in Sandbox extension’s Lights module)? Can you propose an algorithm that combines the model color and material properties into .mtl file content in a way that you get consistent appearance in Slicer and the other software?</p>

---

## Post #11 by @JASON (2025-06-28 00:19 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Thanks for the reply. In my experience, if the OBJ export writes the mtl with diffuse color the same as segment’s color (as the Open Anatomy module does), this allows the same color to be imported into the external 3D software correctly.</p>
<p>One observation that is likely related to reports of colors looking ‘washed-out’ in Blender is that the color Slicer uses from the color-picker is in sRGB color space, but Blender interprets the color as being linear.</p>
<p>OBJ is an older format and predates the use of linear color space rendering, so sRGB colors in mtl is the norm. Autodesk 3D softwares allows for color management that can automatically map colors &amp; textures from sRGB to linear.</p>
<p>Blender will map sRGB textures to linear, but doesn’t do the same for colors in mtl files during OBJ import. A user can get around this by approximating sRGB to linear conversion by applying a gamma value of 2.2.</p>
<pre><code class="lang-auto">import bpy
for mat in bpy.data.materials:
    if not mat.use_nodes: continue
    for node in mat.node_tree.nodes:
        if node.type == 'BSDF_PRINCIPLED':
            color_input = node.inputs.get("Base Color")
            if color_input and not color_input.is_linked:
                c = color_input.default_value
                color_input.default_value = (pow(c[0], 2.2), pow(c[1], 2.2), pow(c[2], 2.2), c[3])
                mat.update_tag()
            break
</code></pre>
<p>A robust OBJ export solution might include options for linear or sRGB color output.</p>
<p>Here is a segmentation in Slicer (top), and initial import in Blender (left) where the colors are incorrectly interpreted as linear.  On the bottom right is Blender after running the above script with the gamma shift.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/9613949e930219c7d7c928a74d37b573cd412e4b.jpeg" data-download-href="/uploads/short-url/lpDzrzVied5AqQz1JdZPhfvitvl.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/9613949e930219c7d7c928a74d37b573cd412e4b_2_685x500.jpeg" alt="image" data-base62-sha1="lpDzrzVied5AqQz1JdZPhfvitvl" width="685" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/9613949e930219c7d7c928a74d37b573cd412e4b_2_685x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/9613949e930219c7d7c928a74d37b573cd412e4b_2_1027x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/9613949e930219c7d7c928a74d37b573cd412e4b_2_1370x1000.jpeg 2x" data-dominant-color="383A35"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1401 99.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #12 by @pieper (2025-06-28 13:31 UTC)

<p>Thanks <a class="mention" href="/u/jason">@JASON</a> that’s really helpful <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=14" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<p>I agree that obj is probably just too simplistic to satisfy modern use cases, but the issue of default lighting in the different places you want to import the data makes it hard (or impossible really) for Slicer to export something that will look the same everywhere.</p>
<p>But I guess we could provide some more export options that could help and maybe gltf or USD would be more expressive formats.  Did anything ever happen with <a href="https://discourse.vtk.org/t/universal-scene-description-usd-scene-importer-exporter/6452/4">this thread?</a></p>

---
