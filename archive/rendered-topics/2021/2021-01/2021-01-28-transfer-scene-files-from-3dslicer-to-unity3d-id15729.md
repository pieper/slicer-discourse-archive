# transfer scene files from 3DSlicer to Unity3D

**Topic ID**: 15729
**Date**: 2021-01-28
**URL**: https://discourse.slicer.org/t/transfer-scene-files-from-3dslicer-to-unity3d/15729

---

## Post #1 by @Amine_Ziane (2021-01-28 22:51 UTC)

<p>Hi, anybody know how to take the segmentation of the 3DSlicer scene and put those same segmentation on Unity3D with the same characteristics (size, dimension, position of objects), please? I need this for a Project in Zspace screen which works with Unity3D</p>

---

## Post #2 by @lassoan (2021-01-28 23:03 UTC)

<p>Slicer can export the segmentation to obj format (and some others) that Unity can use.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#export-segmentation-to-model-surface-mesh-file" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#export-segmentation-to-model-surface-mesh-file</a></p>
<p>The length unit is mm by default. You can change the scale in the export window but I would recommend keeping the default, as mm is used as length unit by DICOM and all clinical imaging software.</p>
<p>Note that while Unity is an awesome gaming engine, it is quite poor for medical imaging applications. For example, you may find that Unity cannot import the full-quality meshes with all details (it has a limit on maximum polygon count per mesh). If you run into this limitation but still want to work with Unity then you either need to split the mesh to multiple pieces or decimate it before exporting it to file in Slicer (export segments to model, decimate using Surface Toolbox module, then save the models using File / Save data).</p>

---

## Post #3 by @Amine_Ziane (2021-01-29 06:47 UTC)

<p>So let’s imagine I have a segmentation scene file and I want to put these segmentations in unity3D from slicer without changing the characteristics of the segmentations. So how do I do this? because concretely I think it is possible but I cannot find exactly what to do.</p>

---

## Post #4 by @lassoan (2021-01-29 16:04 UTC)

<p>You can use use SlicerOpenAnatomy extension’s OpenAnatomy export module, which can export a segmentation as a set of low-poly models by a single click of a button in OBJ or glTF format.</p>

---

## Post #5 by @mikebind (2021-01-29 16:41 UTC)

<p>Once you have the exported OBJ files, if you drop them into the Assets folder (or a subdirectory of the Assets folder if you want to keep things more organized) of your Unity project, Unity will automatically import them as assets.  Then you can add them to your scene within Unity.  It’s been a while since I’ve done it, but I recall the import process working smoothly.  You need both the .obj file and the associated .mtl file to bring along the associated color you have from Slicer.  The obj file holds the mesh and the mtl file holds the material properties, which includes color.</p>

---

## Post #6 by @mikebind (2021-01-29 16:46 UTC)

<p>About the scaling, the Slicer export has units of mm, and I think the Unity default might interpret numbers as meters, but scaling things in Unity is very easy, and if your objects are 1000x too big, just scale them down.  For what I was doing, only relative sizes mattered and all meshes were coming from Slicer, so I didn’t end up having to change anything.</p>

---

## Post #7 by @pll_llq (2021-01-29 19:09 UTC)

<p>If you want to avoid changing the segmentation to a mesh model and display the segmentation as a volume in unity - there are also several options to do this.</p>
<p>Basically speaking - you can export the segmentation as a sequence of 2D slices and import them into a 3D texture. The same way as volumetric clouds are rendered.</p>
<p>If you want to use DICOM you might need to write an import plugin that will read and convert the files to a texture sequence or a 3D texture, but if you just want simple visualisation you can export a sequence of images using the Screen Capture module and use the sequence with volume renderers like <a href="https://bitbucket.org/it-medex/volume-rendering-engine/src/master/" rel="noopener nofollow ugc">this one</a>.</p>
<p>There were a couple of very nice looking prototypes to do volume rendering of medical images in UE4 that appeared to show better performance - so Unity is not the only game engine that can give you this functionality.</p>
<p>Edit: there is a <a href="https://assetstore.unity.com/packages/tools/input-management/simple-dicom-loader-116915" rel="noopener nofollow ugc">Simple DICOM Loader</a> in the Unity Asset Store.</p>

---

## Post #8 by @Amine_Ziane (2021-02-01 22:39 UTC)

<p>Thank you everyone, you have helped me a lot.<br>
I have another question. How do I PRECISELY transfer the volume rendering of the sections I have on 3DSlicer to Unity3D without changing the orientation, the scale etc … PLEASE ??</p>

---

## Post #9 by @aldoSanchez (2021-02-03 23:58 UTC)

<p>yes I have a complete Proyecto fist you need to create a 3D model and save it as .ply file and go to  this website so you don’t need Blender to convert to fix the file<br>
this is because is the format that unity needs.<br>
<a href="https://products.aspose.app/3d/conversion/ply-to-fbx" class="onebox" target="_blank" rel="noopener nofollow ugc">https://products.aspose.app/3d/conversion/ply-to-fbx</a></p>
<p>after converting your 3d model format you can drag it in unity I guess you want to do an AR or something like it, if that’s the case feel free to ask me</p>

---

## Post #10 by @Amine_Ziane (2021-02-04 01:22 UTC)

<p>thanks , Basically I have MRI sections that I transferred from 3Dslicer to unity3D and now I want to have the volume rendering of these images in unity3D, how do I do that?</p>

---

## Post #11 by @Amine_Ziane (2021-02-04 01:23 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7e2fdc3f51fa330fa4188fe698348fcbfa8cb0bf.png" data-download-href="/uploads/short-url/i0iHuTgNXrqA1X6WWhZHOLtqutx.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7e2fdc3f51fa330fa4188fe698348fcbfa8cb0bf.png" alt="image" data-base62-sha1="i0iHuTgNXrqA1X6WWhZHOLtqutx" width="690" height="257" data-dominant-color="2E2E2E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">712×266 21.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #12 by @Amine_Ziane (2021-02-04 01:24 UTC)

<p>they are in .PNG format</p>

---

## Post #13 by @aldoSanchez (2021-02-04 01:55 UTC)

<p>pleas open Slicer and see the name of your file you can see these by going to Data in Modules</p>
<p>after that pleas change the name of your file mi file name is aseg.presurf-IXI061-A<br>
so try this:<br>
You can open python code by crl+3</p>
<pre data-code-wrap="python"><code class="lang-python">nodo='aseg.presurf-IXI061-A'

sliceLogic = slicer.app.layoutManager().sliceWidget('Red').sliceLogic()
compositeNode = sliceLogic.GetSliceCompositeNode()
compositeNode.SetLinkedControl(1)
#link the slice control
slicer.util.getNode('vtkMRMLSliceNodeRed').SetUseLabelOutline(1);
#Thickness line 
labelMapNode=getNode(nodo)
labelMapNode.GetDisplayNode().SetSliceIntersectionThickness(1)

#####3d

seg=slicer.mrmlScene.AddNewNodeByClass('vtkMRMLSegmentationNode')
slicer.modules.segmentations.logic().ImportLabelmapToSegmentationNode(getNode(nodo), seg)
seg.CreateClosedSurfaceRepresentation()
</code></pre>
<p>After this code you will have a 3d model<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a641906205ce9702f083a81cc67af1d44ccc5378.png" data-download-href="/uploads/short-url/nILJhiJ4aaENIqt5TNsrR7t4Ptm.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a641906205ce9702f083a81cc67af1d44ccc5378_2_690x387.png" alt="image" data-base62-sha1="nILJhiJ4aaENIqt5TNsrR7t4Ptm" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a641906205ce9702f083a81cc67af1d44ccc5378_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a641906205ce9702f083a81cc67af1d44ccc5378_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a641906205ce9702f083a81cc67af1d44ccc5378.png 2x" data-dominant-color="87878A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1366×768 241 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You will have to go to segment edit click segmentation<br>
after click go to this menu<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/58aab3cc336f4b3b3f9fad8567341884c95656da.png" alt="image" data-base62-sha1="cEnKdz6PbM7bNxy9lYwaLuuMDVg" width="247" height="252"><br>
and you will have you 3d protect in stl file</p>

---

## Post #14 by @lassoan (2021-02-04 03:14 UTC)

<aside class="quote no-group" data-username="Amine_Ziane" data-post="10" data-topic="15729">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/amine_ziane/48/8989_2.png" class="avatar"> Amine_Ziane:</div>
<blockquote>
<p>I want to have the volume rendering</p>
</blockquote>
</aside>
<p>Implementing medical image viewer in Unity is a huge pain. You essentially need to redevelop everything from scratch. You find a few very basic volume rendering packages that you should be able to set up a simple demo with it, but they are nowhere near to what real users would expect as a minimum requirement for a clinical software.</p>
<p>I would only recommend Unity for very special use cases, for example for building simulation-based training applications, where the emphasis is on fluid computer-game-like immersive experience and you don’t need clinical-grade visualization and tools.</p>

---

## Post #17 by @Amine_Ziane (2021-02-04 16:39 UTC)

<p>I have this error</p>
<pre><code class="lang-auto">&gt;&gt;&gt; #####3d
&gt;&gt;&gt; seg=slicer.mrmlScene.AddNewNodeByClass('vtkMRMLSegmentationNode')
&gt;&gt;&gt;slicer.modules.segmentations.logic().ImportLabelmapToSegmentationNode(getNode(nodo), seg)
Traceback (most recent call last):
File "&lt;console&gt;", line 1, in &lt;module&gt;
TypeError: arguments do not match any overloaded methods
&gt;&gt;&gt; seg.CreateClosedSurfaceRepresentation()
True
</code></pre>

---

## Post #18 by @lassoan (2021-02-05 04:33 UTC)

<p>First argument of <code>ImportLabelmapToSegmentationNode</code> must be a labelmap volume. See more examples <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Segmentations">here</a>.</p>

---

## Post #19 by @Amine_Ziane (2021-02-07 18:44 UTC)

<p>Yes I know but I have to do this on unity3D even if the result is not perfect but I have to show something to my professor</p>

---

## Post #20 by @Amine_Ziane (2021-02-07 19:08 UTC)

<p>Actually I already have my images in unity3D so now from unity3D I have to do the volume rendering, thanks to a plugin I guess</p>

---

## Post #21 by @Amine_Ziane (2021-02-07 21:30 UTC)

<p>Or how use the surface rendering instead of volume rendering in unity3D ?</p>

---

## Post #22 by @lassoan (2021-02-07 21:57 UTC)

<p>You would load the image into Slicer, use Segment Editor to segment all the structures that you are interested in, and export the segmentation to OBJ files (see step-by-step instructions <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#use-cases">here</a>). You can import the OBJ files into Unity.</p>

---

## Post #23 by @Amine_Ziane (2021-02-08 23:02 UTC)

<p>hum okey thanks a lot and if i just want to export the top right file to unity, what do i do?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/09a38218739d4f539099447d8d269cc21992b77d.jpeg" data-download-href="/uploads/short-url/1ngBWalxHGzyJuJ4BQ4lYbr4DBX.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/09a38218739d4f539099447d8d269cc21992b77d_2_690x341.jpeg" alt="image" data-base62-sha1="1ngBWalxHGzyJuJ4BQ4lYbr4DBX" width="690" height="341" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/09a38218739d4f539099447d8d269cc21992b77d_2_690x341.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/09a38218739d4f539099447d8d269cc21992b77d_2_1035x511.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/09a38218739d4f539099447d8d269cc21992b77d_2_1380x682.jpeg 2x" data-dominant-color="B9B6B7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2032×1005 310 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #24 by @mikebind (2021-02-10 22:39 UTC)

<p>It looks like that is showing a volume rendering, which is different than a segmentation.  If you only care about capturing that outer visible surface, then the quickest approach will be to create a segment via thresholding. Open the segment editor module, create a new segment, and then choose the threshold tool.  Choose a threshold minimum value which is larger than the voxel values for air and a threshold maximum value which is greater than the voxel values at the skin surface, and then click apply.  That should basically create a segment which contains all voxels which are non-air.  If you click “Show 3D” on the segmentation and then hide the volume rendering, you should be able to see your segment in the 3D view (where your volume rendering is now).  That segmentation can be exported to OBJ files as described above and then imported into Unity.</p>
<p>If you actually only need the skin surface, the segment you generate this way may contain a lot of unnecessary internal structure (which you can get rid of by using other segmentation tools), but this is the quickest way I can think of to get an approximation of what you are asking for.</p>

---
