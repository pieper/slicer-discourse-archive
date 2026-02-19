---
topic_id: 16971
title: "Question On Using Slicergt Texture Mapping"
date: 2021-04-07
url: https://discourse.slicer.org/t/16971
---

# Question on using SlicerGT Texture mapping

**Topic ID**: 16971
**Date**: 2021-04-07
**URL**: https://discourse.slicer.org/t/question-on-using-slicergt-texture-mapping/16971

---

## Post #1 by @jackxiong (2021-04-07 03:47 UTC)

<p>Hi Andras, maybe this is a simple question, but I really need your help. I have the requirement of using gradient color jpg file make a texture mapping on 3D surface, I have draft code with pure vtk, and it got the expected result:</p>
<p>import vtk</p>
<h1><a name="p-57557-create-a-render-window-1" class="anchor" href="#p-57557-create-a-render-window-1" aria-label="Heading link"></a>Create a render window</h1>
<p>ren = vtk.vtkRenderer()<br>
renWin = vtk.vtkRenderWindow()<br>
renWin.AddRenderer(ren)<br>
renWin.SetSize(480,480)<br>
iren = vtk.vtkRenderWindowInteractor()<br>
iren.SetRenderWindow(renWin)</p>
<h1><a name="p-57557-generate-a-sphere-2" class="anchor" href="#p-57557-generate-a-sphere-2" aria-label="Heading link"></a>Generate a sphere</h1>
<p>sphere = vtk.vtkSphereSource()</p>
<h1><a name="p-57557-read-the-image-data-from-a-file-3" class="anchor" href="#p-57557-read-the-image-data-from-a-file-3" aria-label="Heading link"></a>Read the image data from a file</h1>
<p>reader = vtk.vtkJPEGReader()<br>
reader.SetFileName(“gradientColor.jpeg”)</p>
<h1><a name="p-57557-create-texture-object-4" class="anchor" href="#p-57557-create-texture-object-4" aria-label="Heading link"></a>Create texture object</h1>
<p>texture = vtk.vtkTexture()<br>
texture.SetInputConnection(reader.GetOutputPort())</p>
<p><span class="hashtag-raw">#Map</span> texture coordinates<br>
map_to_plane = vtk.vtkTextureMapToPlane()<br>
map_to_plane.SetInputConnection(sphere.GetOutputPort())</p>
<h1><a name="p-57557-create-mapper-and-set-the-mapped-texture-as-input-5" class="anchor" href="#p-57557-create-mapper-and-set-the-mapped-texture-as-input-5" aria-label="Heading link"></a>Create mapper and set the mapped texture as input</h1>
<p>mapper = vtk.vtkPolyDataMapper()<br>
mapper.SetInputConnection(map_to_plane.GetOutputPort())</p>
<h1><a name="p-57557-create-actor-and-set-the-mapper-and-the-texture-6" class="anchor" href="#p-57557-create-actor-and-set-the-mapper-and-the-texture-6" aria-label="Heading link"></a>Create actor and set the mapper and the texture</h1>
<p>actor = vtk.vtkActor()<br>
actor.SetMapper(mapper)<br>
actor.SetTexture(texture)</p>
<p>ren.AddActor(actor)</p>
<p>iren.Initialize()<br>
renWin.Render()<br>
iren.Start()</p>
<p>The result as below picture:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/54b9984fb905675a46a38bfcd2ce21da6feb3500.jpeg" data-download-href="/uploads/short-url/c5vK3HKOI1fdz632FvNkrmxfMje.jpeg?dl=1" title="图片" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/54b9984fb905675a46a38bfcd2ce21da6feb3500_2_470x500.jpeg" alt="图片" data-base62-sha1="c5vK3HKOI1fdz632FvNkrmxfMje" width="470" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/54b9984fb905675a46a38bfcd2ce21da6feb3500_2_470x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/54b9984fb905675a46a38bfcd2ce21da6feb3500.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/54b9984fb905675a46a38bfcd2ce21da6feb3500.jpeg 2x" data-dominant-color="312139"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">图片</span><span class="informations">482×512 22.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I have two questions here:<br>
The first one:<br>
When I try to use SlicerIGT extension Texture Model, it has not got the expected result. The steps as below:</p>
<p>v = slicer.util.getNode(‘View1’)<br>
v.SetBoxVisible(False)</p>
<h1><a name="p-57557-sphere-7" class="anchor" href="#p-57557-sphere-7" aria-label="Heading link"></a>Sphere</h1>
<p>sphereSource = vtk.vtkSphereSource()<br>
sphereSource.SetCenter(0,0,0)<br>
sphereSource.SetRadius(60.0)<br>
sphereSource.Update()<br>
sphereSource = sphereSource.GetOutput() # vtkPolyData()</p>
<h1><a name="p-57557-create-a-model-with-the-sphere-and-add-it-to-scene-8" class="anchor" href="#p-57557-create-a-model-with-the-sphere-and-add-it-to-scene-8" aria-label="Heading link"></a>Create a model with the sphere and add it to scene</h1>
<p>modelNode = slicer.mrmlScene.AddNewNodeByClass(‘vtkMRMLModelNode’)<br>
modelNode.SetAndObservePolyData(sphereSource)<br>
modelNode.CreateDefaultDisplayNodes()<br>
modelNode.SetName(‘My sphere’)</p>
<p>and then I come back to main UI in 3D Slicer and use the Texture model as below:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5f7cb3b7b80b5552a0ce1a97f34ec6aa7a08bbb7.jpeg" data-download-href="/uploads/short-url/dCIx15QYreRKm8qFqkgL0dOhv7h.jpeg?dl=1" title="图片" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5f7cb3b7b80b5552a0ce1a97f34ec6aa7a08bbb7_2_690x252.jpeg" alt="图片" data-base62-sha1="dCIx15QYreRKm8qFqkgL0dOhv7h" width="690" height="252" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5f7cb3b7b80b5552a0ce1a97f34ec6aa7a08bbb7_2_690x252.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5f7cb3b7b80b5552a0ce1a97f34ec6aa7a08bbb7_2_1035x378.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5f7cb3b7b80b5552a0ce1a97f34ec6aa7a08bbb7_2_1380x504.jpeg 2x" data-dominant-color="A8A6BF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">图片</span><span class="informations">1867×683 125 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But as you see, the result is not expected. What am I wrong here?</p>
<p>The second one is: How can I use python script to generate the texture mapping model? Should I use below code:</p>
<p>def showTextureOnModel(self, modelNode, textureImageNode):<br>
modelDisplayNode = modelNode.GetDisplayNode()<br>
modelDisplayNode.SetBackfaceCulling(0)<br>
textureImageFlipVert = vtk.vtkImageFlip()<br>
textureImageFlipVert.SetFilteredAxis(1)<br>
textureImageFlipVert.SetInputConnection(textureImageNode.GetImageDataConnection())<br>
modelDisplayNode.SetTextureImageDataConnection(textureImageFlipVert.GetOutputPort())</p>
<p>maybe the question is simple and stupid, but I really need your help and suggestion. And I cannot access the website: <a href="http://onedrive.live.com" rel="noopener nofollow ugc">onedrive.live.com</a>, is there another website for the SlicerIGT tutorial?</p>
<p>Thanks in advance!</p>

---

## Post #2 by @jackxiong (2021-04-08 01:27 UTC)

<p>Hi Buddies and experts in the community, anybody knows the solution? I don’t know how to convert the python script to 3D Slicer console(as the script in 1st section, it do the sphere texture mapping in pure vtk library very well, but I cannot convert the python script in 3D Slicer) .  I refer to the link <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Access_VTK_actor_properties" class="inline-onebox" rel="noopener nofollow ugc">Documentation/Nightly/ScriptRepository - Slicer Wiki</a>, but seems take no effect.</p>
<p>Your suggestions are appreciated<br>
Thanks again!</p>

---

## Post #3 by @jackxiong (2021-04-08 09:20 UTC)

<p>Never mind, I have already solved the problem, refer to below link <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Accessing_views.2C_renderers.2C_and_cameras" class="inline-onebox" rel="noopener nofollow ugc">Documentation/Nightly/ScriptRepository - Slicer Wiki</a>  convert python script &amp; run in 3D Slicer python console correctly.</p>

---
