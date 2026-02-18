# Display vtkMarchingCubes in 3d view

**Topic ID**: 1471
**Date**: 2017-11-16
**URL**: https://discourse.slicer.org/t/display-vtkmarchingcubes-in-3d-view/1471

---

## Post #1 by @TTrambi (2017-11-16 17:27 UTC)

<p>Hi I’m at slicer develoment and i got a basic question:</p>
<p>I’m reading in dicom data and after some processing I convert it to vtk using the vtkImageImport.<br>
Then I create a mesh via the vtkMarchingCubes and save it to a .stl file.</p>
<p>So, my question is, how can i display my vtkMarchingCube or volume in the 3d view of slicer?</p>

---

## Post #2 by @lassoan (2017-11-16 17:35 UTC)

<p>You can use <a href="http://apidocs.slicer.org/master/classvtkSlicerModelsLogic.html#a90951d618e0de9f6048efaedfc79427c">Models module logic</a> to create a model node from vtkPolyData object:</p>
<pre><code>slicer.modules.models.logic().AddModel(myPolyData)
</code></pre>
<p>Note that you don’t need to implement low-level features such as loading image from DICOM or model generation using marching cubes. If you tell us know what the end goal of your project is then we can give you specific advice about how to achieve that in Slicer.</p>

---

## Post #3 by @TTrambi (2017-11-20 15:06 UTC)

<p>Hi, thanks for your helping me out.</p>
<p>I’m working on an automatic breast cancer segmenation module from dce-mri, using the same method as the Segment CAD module (<a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/SegmentCAD" class="inline-onebox" rel="noopener nofollow ugc">Documentation/Nightly/Modules/SegmentCAD - Slicer Wiki</a>), but my plan is to segment the tumor instead of giving a label map.</p>
<p>So, i have to read in the dicom data manually because of some problems with the files. The files are from the cancerwiki (<a href="https://wiki.cancerimagingarchive.net/display/Public/Breast-MRI-NACT-Pilot" rel="noopener nofollow ugc">https://wiki.cancerimagingarchive.net/display/Public/Breast-MRI-NACT-Pilot</a>) and i dont think there is another way then read in all the dcm files manually because they are not in correct order and not sort by timepoint.</p>
<p>Now I’m running into some trouble with the segmentation as you can see on my appended picture. You can see the tumor on the left part, but there is a big chest part showing up and all the blood vessels.<br>
My idea is to remove the chest part with the by removing the largest part with vtkPolyDataConnectivityFilter and use the itk Hessian3DToVesselnessMeasureImageFilter, but i dont know how to remove one polydata from another polydata and how i can use my vtkPolyData with itk.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1b10527f1d725eb52a98cf066175d83f289b2995.png" data-download-href="/uploads/short-url/3RpRroDqTrpWsSFOfWI0R3LcWtT.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1b10527f1d725eb52a98cf066175d83f289b2995_2_690x382.png" alt="image" data-base62-sha1="3RpRroDqTrpWsSFOfWI0R3LcWtT" width="690" height="382" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1b10527f1d725eb52a98cf066175d83f289b2995_2_690x382.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1b10527f1d725eb52a98cf066175d83f289b2995.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1b10527f1d725eb52a98cf066175d83f289b2995.png 2x" data-dominant-color="9597C5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">903×500 85.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2017-11-20 15:58 UTC)

<p>I’ve successfully loaded UCSF-BR-01 using DICOM module:</p>
<ul>
<li>drag-and-drop the folder to Slicer application window</li>
<li>click OK to import as DICOM</li>
<li>open DICOM browser module to load the imported data</li>
<li>choose which data sets to show using Data module</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9ef9a6f8317da3d20c6837711e0a943f09a1a130.jpeg" data-download-href="/uploads/short-url/mGmjHs0qeuzaVCb8foZ6DIGGkKI.jpg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/9ef9a6f8317da3d20c6837711e0a943f09a1a130_2_690x373.jpg" alt="image" data-base62-sha1="mGmjHs0qeuzaVCb8foZ6DIGGkKI" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/9ef9a6f8317da3d20c6837711e0a943f09a1a130_2_690x373.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/9ef9a6f8317da3d20c6837711e0a943f09a1a130_2_1035x559.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/9ef9a6f8317da3d20c6837711e0a943f09a1a130_2_1380x746.jpg 2x" data-dominant-color="7C7E84"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1040 507 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>It loaded everything perfectly, even segmentations and time sequences (Sagittal-IR_3DFGRE volume). After adjusting segment colors and making 3D display semi-transparent:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/9320077a34e2e51fe27290a2f862f8aad35ab0d2.jpeg" data-download-href="/uploads/short-url/kZwOffsMYIJiijcngkiJklbNXZo.jpg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/9320077a34e2e51fe27290a2f862f8aad35ab0d2_2_690x373.jpg" alt="image" data-base62-sha1="kZwOffsMYIJiijcngkiJklbNXZo" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/9320077a34e2e51fe27290a2f862f8aad35ab0d2_2_690x373.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/9320077a34e2e51fe27290a2f862f8aad35ab0d2_2_1035x559.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/9320077a34e2e51fe27290a2f862f8aad35ab0d2_2_1380x746.jpg 2x" data-dominant-color="878689"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1040 528 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>You can very easily segment the tumor yourself, using Segment editor module. While simple thresholding is available in the module (<code>Threshold</code> effect), you probably want to use <code>Grow from seeds</code> effect for tumor segmentation. Just paint inside and outside the tumor with different segments and use <code>Grow from seeds</code> to create a complete segmentation.</p>

---

## Post #5 by @TTrambi (2017-11-21 00:38 UTC)

<p>Thank you once again.</p>
<p>Further, how can i change the time point in the slice view when i’ve loaded in the 4-dimensional data?<br>
(drag and drop is only supported at version 4.9)</p>
<p>As I mentioned, i want to implement an automatic segmentation module, so i dont want to place a seed. Can you please explain to me how i can cut vktPolyData out of vtkPolydata.</p>

---

## Post #6 by @lassoan (2017-11-21 02:14 UTC)

<aside class="quote no-group" data-username="TTrambi" data-post="5" data-topic="1471">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ttrambi/48/894_2.png" class="avatar"> TTrambi:</div>
<blockquote>
<p>Can you please explain to me how i can cut vktPolyData out of vtkPolydata.</p>
</blockquote>
</aside>
<p>Boolean operations on meshes are extremely difficult to implement. Maybe not even possible to implement in a way that is guaranteed to work for any geometry, within reasonable time. VTK has some Boolean mesh filters, but of course they very often fail for complex geometries (and unfortunately, randomly fail even for simple ones). I would not recommend to use them.</p>
<p>Fortunately, you don’t need to implement vtkPolyData cutting, as your inputs are volumes, and segmentation can be represented as labelmaps. Implementing Boolean operations on labelmaps is quick and guaranteed to work correctly all the time.</p>
<p>You can use the <code>Logical operators</code> effect of Segment Editor as described <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script">here</a>.</p>
<aside class="quote no-group" data-username="TTrambi" data-post="5" data-topic="1471">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ttrambi/48/894_2.png" class="avatar"> TTrambi:</div>
<blockquote>
<p>i want to implement an automatic segmentation module, so i dont want to place a seed</p>
</blockquote>
</aside>
<p>I guess you mean you don’t want to place a seed manually. You can create seeds automatically. For example, in some cases you can create seeds by thresholding (using Thresholding effect), followed by splitting of islands to segments (using Islands effect). Or, you may defining seeds for an atlas and then registering that atlas to your patient image and generate seeds by applying the computed transform to the atlas seeds. Of course, there are many approaches to automatic segmentation - not all of them are based on region growing.</p>

---

## Post #7 by @lassoan (2017-11-21 02:21 UTC)

<aside class="quote no-group" data-username="TTrambi" data-post="5" data-topic="1471">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ttrambi/48/894_2.png" class="avatar"> TTrambi:</div>
<blockquote>
<p>how can i change the time point in the slice view when i’ve loaded in the 4-dimensional data?</p>
</blockquote>
</aside>
<p>If you use Slicer 4.8 or older then 4D DICOM files are always loaded as MultiVolume and you can browse time points using MultiVolumeExplorer module.</p>
<p>If you use a recent nightly build then in menu: Edit/Application settings/DICOM you can choose between loading 4D volumes as Multivolume nodes or as Volume Sequence nodes. Loading as Volume Sequence node requires installation of Sequences extension and you may find it slightly easier to browse the time points, as you can use the Sequence browser toolbar instead of switching between modules.</p>

---

## Post #8 by @MGM (2018-03-09 17:32 UTC)

<p>Hi <a class="mention" href="/u/ttrambi">@TTrambi</a></p>
<p>I saw in your first post, that you usefully saved to .stl , using vtkMarchingCubes.<br>
I would like to know what method you used ?</p>
<p>because, I’m tried to do the same thing, just to save as vtk file.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a>, any idea ?</p>
<p>Thank you for your time</p>

---

## Post #9 by @lassoan (2018-03-09 17:45 UTC)

<p>You can choose file format in the Save data dialog.</p>

---

## Post #10 by @MGM (2018-03-13 16:19 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>it’s working with vtkPolyDataWriter <img src="https://emoji.discourse-cdn.com/twitter/ok_hand.png?v=5" title=":ok_hand:" class="emoji" alt=":ok_hand:"></p>
<p>now, I’m looking for another way, so I can get a small file size.</p>
<p>Thanks</p>

---

## Post #11 by @lassoan (2018-03-15 04:37 UTC)

<p>Typically you can reduce the number of points to 10-20% of the original number by applying decimation, without negligible visible difference. You can apply decimation in Segmentations module when you create the closed surface representation from binary labelmap representation (click Update button in Closed surface representation row in Representations section in Segmentations module); or if you already have a model node then you can use Surface Toolbox module.</p>

---
