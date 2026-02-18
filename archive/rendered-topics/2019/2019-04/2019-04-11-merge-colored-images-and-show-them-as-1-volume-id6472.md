# Merge colored images and show them as 1 volume

**Topic ID**: 6472
**Date**: 2019-04-11
**URL**: https://discourse.slicer.org/t/merge-colored-images-and-show-them-as-1-volume/6472

---

## Post #1 by @katharina_hecker (2019-04-11 14:57 UTC)

<p>Hello everyone,<br>
is there a way to merge multiple colored png images into one volume and visualize this than in the 3D space?</p>
<p>I really need this feature since in these images, the colors are really important and I can´t segment pixel by pixel…</p>
<p>I would be very pleased if somebody could give me some advice to this topic!</p>
<p>Thank you for your understandings!</p>
<p>Greetings,<br>
Anna</p>

---

## Post #2 by @lassoan (2019-04-11 16:39 UTC)

<p>This should help: <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ#How_to_load_data_from_a_sequence_of_jpg.2C_tif.2C_or_png_files.3F" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/FAQ#How_to_load_data_from_a_sequence_of_jpg.2C_tif.2C_or_png_files.3F</a></p>

---

## Post #3 by @katharina_hecker (2019-04-15 15:16 UTC)

<p>Thank you Sir for the fast reply!</p>
<p>Is there a way to retain the colors of the images? When I create a scalar volume it automatically creates a grey 3D volume. I really need the colored volume out of theses images like there are in there<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/811575664cf980a77e5364689ddff77b8d6eeefe.png" data-download-href="/uploads/short-url/ipVzflNbq4WEEa7ZQsCzUypBBnM.png?dl=1" title="volume%20color%20problem" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/811575664cf980a77e5364689ddff77b8d6eeefe_2_639x500.png" alt="volume%20color%20problem" data-base62-sha1="ipVzflNbq4WEEa7ZQsCzUypBBnM" width="639" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/811575664cf980a77e5364689ddff77b8d6eeefe_2_639x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/811575664cf980a77e5364689ddff77b8d6eeefe_2_958x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/811575664cf980a77e5364689ddff77b8d6eeefe_2_1278x1000.png 2x" data-dominant-color="444356"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">volume%20color%20problem</span><span class="informations">1315×1028 47.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div> … Is there a solution for my problem?</p>
<p>Thanks in advance!</p>

---

## Post #4 by @lassoan (2019-04-15 15:32 UTC)

<p>If you just want to visualize them with their original color, apply spatial transforms, etc. then you don’t need to convert to scalar volume. What would you like to do with the image?</p>

---

## Post #5 by @katharina_hecker (2019-04-17 05:02 UTC)

<p>I just showed the view of one image. I would like to visualize the colored image stack in their original color in the 3D space (View 1). Since the pixels of the image stack are colored differently, I can´t segment pixel by pixel. It is also not possible to use the vector to scalar volume, since it is creating a Grey-colored 3D volume, where the original color is lost.</p>
<p>I hope that the issue is now understandable.<br>
Is there a way to solve this?</p>
<p>Thank you very much for all help!</p>

---

## Post #6 by @lassoan (2019-04-17 14:13 UTC)

<aside class="quote no-group" data-username="katharina_hecker" data-post="5" data-topic="6472">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/katharina_hecker/48/3431_2.png" class="avatar"> katharina_hecker:</div>
<blockquote>
<p>I would like to visualize the colored image stack in their original color in the 3D space (View 1)</p>
</blockquote>
</aside>
<p>If you have a full-color image then you can show a direct volume rendering of it by turning off “independent component” option in the volume renderer (it makes image components interpreted as RGBA). Type this in the Python console after enabling volume rendering:</p>
<pre><code>getNode('VolumeProperty').GetVolumeProperty().SetIndependentComponents(0)
</code></pre>
<p>Note that you need an RGBA image (not just RGB). The fourth (alpha) component controls opacity. If you only have an RGB image then you can create the “alpha” volume using “Vector to scalar volume” module, then append this alpha volume to the original RGB volume by copy-pasting this to the Python console:</p>
<pre><code>colorVolume = getNode('MyColorVolume') # RGB vector volume
alphaVolume = getNode('MyAlphaVolume') # scalar volume created from RGB volume using Vector to scalar volume module

append=vtk.vtkImageAppendComponents()
append.AddInputConnection(colorVolume.GetImageDataConnection())
append.AddInputConnection(alphaVolume.GetImageDataConnection())
append.Update()
colorVolume.SetAndObserveImageData(append.GetOutput())
</code></pre>
<p>For segmentation (if you want to create a surface mesh, 3D-printable model, etc), use the scalar volume created by “Vector to scalar volume” module.</p>

---

## Post #7 by @muratmaga (2019-08-07 17:38 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> This has been very useful for me to get a very old segmentation from VG Studio Max into Slicer. At the time, I only exported the colored slices (as oppose to exporting them to labelmaps) and I don’t think I have the original data anymore. Two questions:</p>
<ol>
<li>Is there a different way to manipulate transfer functions for RGBA images (so that I can have better control).</li>
<li>Is there a way for me to import this color stack as a segmentation?</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a534d79f2e4055fd88665fadac46677c67acaabe.jpeg" data-download-href="/uploads/short-url/nztZNcDjNkwVOJJbRXfwB68kbhk.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a534d79f2e4055fd88665fadac46677c67acaabe_2_505x500.jpeg" alt="image" data-base62-sha1="nztZNcDjNkwVOJJbRXfwB68kbhk" width="505" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a534d79f2e4055fd88665fadac46677c67acaabe_2_505x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a534d79f2e4055fd88665fadac46677c67acaabe_2_757x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a534d79f2e4055fd88665fadac46677c67acaabe.jpeg 2x" data-dominant-color="494B4D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">786×778 116 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @lassoan (2019-08-23 19:34 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="7" data-topic="6472">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<ul>
<li>Is there a different way to manipulate transfer functions for RGBA images (so that I can have better control).</li>
<li>Is there a way for me to import this color stack as a segmentation?</li>
</ul>
</blockquote>
</aside>
<p>If you convert RGBA images to scalars then it answers both questions. You can convert each color to an index like this:</p>
<pre data-code-wrap="python"><code class="lang-python">rgbVolumeNode = ... # input RGB volume

# Create a labelmap volume for the output
labelVolumeNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLabelMapVolumeNode')
imageData = vtk.vtkImageData()
imageData.SetDimensions(rgbVolumeNode.GetImageData().GetDimensions())
imageData.AllocateScalars(vtk.VTK_UNSIGNED_CHAR, 1)
labelVolumeNode.SetAndObserveImageData(imageData)
ijkToRas = vtk.vtkMatrix4x4()
rgbVolumeNode.GetIJKToRASMatrix(ijkToRas)
labelVolumeNode.SetIJKToRASMatrix(ijkToRas)
labelVolumeNode.CreateDefaultDisplayNodes()

rgb = slicer.util.arrayFromVolume(rgbVolumeNode)
label = slicer.util.arrayFromVolume(labelVolumeNode)
# Set label value (1, 2, ...) for each RGB combination
label[:] = 0
label[(rgb[:,:,:,0]==153) &amp; (rgb[:,:,:,1]==117) &amp; (rgb[:,:,:,2]==67)] = 1
label[(rgb[:,:,:,0]==122) &amp; (rgb[:,:,:,1]==108) &amp; (rgb[:,:,:,2]==11)] = 2
...
slicer.util.arrayFromVolumeModified(labelVolumeNode)
</code></pre>

---
