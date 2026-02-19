---
topic_id: 36686
title: "Apply Paint Using Code"
date: 2024-06-10
url: https://discourse.slicer.org/t/36686
---

# Apply paint using code

**Topic ID**: 36686
**Date**: 2024-06-10
**URL**: https://discourse.slicer.org/t/apply-paint-using-code/36686

---

## Post #1 by @Cagatay (2024-06-10 13:24 UTC)

<p>I want to put sphere brushes (i want to use paint) on scenes with given coordinates. But i couldnt find a way to use paint effect from segment editor in code. How can i use paint in code and paint the scene just in code().I’ve tried <a href="https://gist.github.com/lassoan/2d5a5b73645f65a5eb6f8d5f97abf31b#file-segmentgrowcutsimple-py-L10-L34" rel="noopener nofollow ugc">this</a>. but it uses grow from seeds and i dont want that. I just want to paint.</p>
<p>I also tried this but giving me error.</p>
<pre><code class="lang-auto">segmentEditorWidget.setActiveEffectByName("Paint")
effect = segmentEditorWidget.activeEffect()
effect.setParameter("BrushRelativeDiameter", "1")  # Brush size relative to the volume size
effect.setParameter("BrushSphere", "1")  # Use a spherical brush
effect.paintApply((255, 255, 674))
</code></pre>

---

## Post #2 by @lassoan (2024-06-10 13:25 UTC)

<p>The code section you have found is perfect, that’s all you need to do. You can ignore the rest of the script.</p>

---

## Post #3 by @Cagatay (2024-06-11 06:54 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/46897c62e90e595840491ca6209d68e0ee43ff05.png" data-download-href="/uploads/short-url/a3ZZ4E8a1AD9xFruCfvB8j0UY73.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/46897c62e90e595840491ca6209d68e0ee43ff05_2_690x324.png" alt="image" data-base62-sha1="a3ZZ4E8a1AD9xFruCfvB8j0UY73" width="690" height="324" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/46897c62e90e595840491ca6209d68e0ee43ff05_2_690x324.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/46897c62e90e595840491ca6209d68e0ee43ff05_2_1035x486.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/46897c62e90e595840491ca6209d68e0ee43ff05_2_1380x648.png 2x" data-dominant-color="97979A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1919×903 210 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I can see the spheres in the 3d view. But i cant see them on the slice views. I tried many times, but it doesnt appear.</p>
<pre><code class="lang-auto">
masterVolumeNode = volumeNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLScalarVolumeNode")

segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
segmentationNode.CreateDefaultDisplayNodes() # only needed for display
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(masterVolumeNode)

# Create seed segment inside tumor
tumorSeed = vtk.vtkSphereSource()
tumorSeed.SetCenter(255, 255, 494)
tumorSeed.SetRadius(10)
tumorSeed.Update()
segmentationNode.AddSegmentFromClosedSurfaceRepresentation(tumorSeed.GetOutput(), "Tumor", [1.0,0.0,0.0])

# Create seed segment outside tumor
backgroundSeedPositions = [[255, 260, 494], [255, 265, 494], [255, 270, 494], [255, 275, 494], [255, 280, 494], [255, 285, 494]]
append = vtk.vtkAppendPolyData()
for backgroundSeedPosition in backgroundSeedPositions:
  backgroundSeed = vtk.vtkSphereSource()
  backgroundSeed.SetCenter(backgroundSeedPosition)
  backgroundSeed.SetRadius(10)
  backgroundSeed.Update()
  append.AddInputData(backgroundSeed.GetOutput())

append.Update()
backgroundSegmentId = segmentationNode.AddSegmentFromClosedSurfaceRepresentation(append.GetOutput(), "Background", [0.0,1.0,0.0])
</code></pre>
<p>This is the code i tried last, coordinates are close to the center in the green slice view but i cant see any paint in slice.<br>
Is there a way to solve this? Or how can i use paint effect? Thanks.</p>

---

## Post #4 by @cpinter (2024-06-11 08:56 UTC)

<p>I see you decided to go a different way. This should work as well, but I never used <code>AddSegmentFromClosedSurfaceRepresentation</code> so not sure what it does exactly. When I do this, I tend to create a model node and use <code>slicer.vtkSlicerSegmentationsModuleLogic.ImportModelToSegmentationNode</code>.</p>
<p>As your code does not specify a closed surface representation, the default binary labelmap should be created from the added polydata segments, so not sure. It is always possible that the locations are not correct, so please verify by showing the slices in 3D (or volume render). I’d also check the representations part in the Segmentations module and see what is the master, and also check which representation is shown in 2D (in Display / Advanced I believe). Try to show the closed surface representation in 2D if it is the master for some reason.</p>

---

## Post #5 by @Cagatay (2024-06-11 12:59 UTC)

<p>Thanks for the reply.</p>
<p>With these 3d spheres, this point markup F1 on the screen, when i put my cursor, looks like around 255,255,494 as you can see in the image(bottom-left). But it doesnt show on the axial slice any paint while showing on the 3d.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/02d679b9cf422a2e18fbc319d228c8d7092777c9.png" data-download-href="/uploads/short-url/p6sVsP46OdxlXblVajXd38pGFr.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/02d679b9cf422a2e18fbc319d228c8d7092777c9_2_570x500.png" alt="image" data-base62-sha1="p6sVsP46OdxlXblVajXd38pGFr" width="570" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/02d679b9cf422a2e18fbc319d228c8d7092777c9_2_570x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/02d679b9cf422a2e18fbc319d228c8d7092777c9_2_855x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/02d679b9cf422a2e18fbc319d228c8d7092777c9.png 2x" data-dominant-color="CACCCB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">963×844 125 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>When i look at one slice and sphere paints in 3d, it looks like im giving the coordinates wrong. Where should i get the coordinates from?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/313bb561d450204cdea896280d879fd7bb731ece.png" alt="image" data-base62-sha1="71xjTPg6oG3RCpPqDwUjKs8OMrk" width="637" height="312"></p>
<p>My main goal is to put 2d sphere brushes on some axial slices at the corners. So that it looks quarter sphere on the 3d. So my main goal is to put 2d spheres with paint on axial slice with code, but i cant find any example using paint effect. It should look like this.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2f317f0dccb087031b162623fdf01f04dce87fb6.jpeg" data-download-href="/uploads/short-url/6Juu9VC6wAJptDs1mzwLgjWIdpk.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2f317f0dccb087031b162623fdf01f04dce87fb6.jpeg" alt="image" data-base62-sha1="6Juu9VC6wAJptDs1mzwLgjWIdpk" width="648" height="500" data-dominant-color="5D635E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">810×625 49.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a005cefc54ccf6e7d9093a8abee7e52fe9f89add.jpeg" data-download-href="/uploads/short-url/mPCQ4Z684RBJylgdnnGdPnokrBX.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a005cefc54ccf6e7d9093a8abee7e52fe9f89add_2_690x409.jpeg" alt="image" data-base62-sha1="mPCQ4Z684RBJylgdnnGdPnokrBX" width="690" height="409" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a005cefc54ccf6e7d9093a8abee7e52fe9f89add_2_690x409.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a005cefc54ccf6e7d9093a8abee7e52fe9f89add.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a005cefc54ccf6e7d9093a8abee7e52fe9f89add.jpeg 2x" data-dominant-color="4B4C4F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">968×574 80 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @lassoan (2024-06-11 16:28 UTC)

<p>It seems that the centerpoint coordinates are not set correctly. If you create an example scene from one of the Slicer sample data sets and share that with us (saved as .mrb, uploaded to dropbox/onedrive/googledrive) and corresponding code snippet then we can tell where things went wrong.</p>
<p>What would you like to segment?</p>

---

## Post #7 by @Cagatay (2024-06-12 08:26 UTC)

<aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1lPqGQr63QxN5sivbGb71bbwDWs1iqPx4/view?usp=sharing">
  <header class="source">

      <a href="https://drive.google.com/file/d/1lPqGQr63QxN5sivbGb71bbwDWs1iqPx4/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1lPqGQr63QxN5sivbGb71bbwDWs1iqPx4/view?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1lPqGQr63QxN5sivbGb71bbwDWs1iqPx4/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">Pictures.mrml</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<pre><code class="lang-auto"># Generate input data
################################################

masterVolumeNode = volumeNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLScalarVolumeNode")

# Load master volume

# Create segmentation
segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
segmentationNode.CreateDefaultDisplayNodes() # only needed for display
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(masterVolumeNode)

 



start_value = 170
increment = 40
num_iterations = 20

paint_positions = []

for i in range(num_iterations):
    third_element = start_value + i * increment
    paint_positions.extend([
        [0, 0, third_element],
        [0, 511, third_element],
        [511, 0, third_element],
        [511, 511, third_element]
    ])

append = vtk.vtkAppendPolyData()
for paint_position in paint_positions:
  print(paint_position)
  paintSphere = vtk.vtkSphereSource()
  paintSphere.SetCenter(paint_position)
  paintSphere.SetRadius(10)
  paintSphere.Update()
  append.AddInputData(paintSphere.GetOutput())
  
append.Update()

segmentationNode.AddSegmentFromClosedSurfaceRepresentation(append.GetOutput(), "Paint", [1.0,0.0,0.0])

# Run filter
################################################

# Create segment editor to get access to effects
segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
# To show segment editor widget (useful for debugging): segmentEditorWidget.show()
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)

segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
segmentEditorWidget.setSegmentationNode(segmentationNode)
segmentEditorWidget.setSourceVolumeNode(masterVolumeNode)

 
# Clean up and show results
################################################

# Clean up
slicer.mrmlScene.RemoveNode(segmentEditorNode)

# Make segmentation results nicely visible in 3D
segmentationDisplayNode = segmentationNode.GetDisplayNode()
</code></pre>
<p>I am segmenting successfully using threshold in other code but i need to put spheres around the corners before exporting this segmentation model  as you can see in the previous photos with 4 green quarter spheres, i did that manually but i have to do it in code. I couldnt manage to do that. Seems simple actually, just 4 paint brush in some slices corners in axial view <img src="https://emoji.discourse-cdn.com/twitter/expressionless.png?v=12" title=":expressionless:" class="emoji" alt=":expressionless:" loading="lazy" width="20" height="20"></p>

---

## Post #8 by @lassoan (2024-06-12 12:35 UTC)

<p>The problem is that you specified the  sphere center positions in voxel (IJK) coordinate system. In the code snippet above the positions are expected in patient (RAS) coordinate system. You can find examples in the script repository how to convert. Alternatively, in a special case like this when you want to paint borders you can get segmentation as a numpy array and modufy that using voxel indices (see examples in script repository).</p>

---

## Post #9 by @Cagatay (2024-06-12 17:31 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c771639727fa823156cf81bd3a8cd17938961e63.png" data-download-href="/uploads/short-url/sslWZvD0Gi1y3uMaXfWSOgZQGFt.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c771639727fa823156cf81bd3a8cd17938961e63_2_690x174.png" alt="image" data-base62-sha1="sslWZvD0Gi1y3uMaXfWSOgZQGFt" width="690" height="174" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c771639727fa823156cf81bd3a8cd17938961e63_2_690x174.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c771639727fa823156cf81bd3a8cd17938961e63_2_1035x261.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c771639727fa823156cf81bd3a8cd17938961e63.png 2x" data-dominant-color="665B72"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1273×322 70.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Thank you very much. Now i converted coordinates and it puts the spheres on axial slices and i can see it. But what i really want is  put sphere brushes with paint on corners so only quarter of sphere is shown in 3d view, like above two images with green quarter spheres.</p>

---

## Post #10 by @lassoan (2024-06-13 01:42 UTC)

<p>You can set the segment geometry to not include the entire spheres. By the way, if you drew 4 tubes instead of hundreds of spheres then processing could be 100x faster. Or, if you just want to fill the corners then you can use numpy to modify the segment (e.g., <code>segArray[0:5, 0:5] = 1</code>).</p>

---

## Post #11 by @Cagatay (2024-06-19 08:04 UTC)

<p>I want to fill the corners with sphere paint brush in axial slice.</p>
<blockquote>
<p>segArray[0:5, 0:5] = 1</p>
</blockquote>
<p>i didnt understand this. Are these 0 and 5 signify slice number? and what does assigning 1 do?</p>

---

## Post #12 by @lassoan (2024-06-19 11:39 UTC)

<p><code>segArray</code> is a numpy array. The code sets the corner voxels to 1 in all axial slices (I think you can use any positive value). See a complete example <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#read-and-write-a-segment-as-a-numpy-array">here</a>.</p>

---
