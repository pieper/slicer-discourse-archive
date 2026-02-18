# How to change number of points and cells in a surface model?

**Topic ID**: 2630
**Date**: 2018-04-19
**URL**: https://discourse.slicer.org/t/how-to-change-number-of-points-and-cells-in-a-surface-model/2630

---

## Post #1 by @shahrokh (2018-04-19 09:03 UTC)

<p>Hello Dear Developers and Users</p>
<p>I have several surface models. Specifications of one of  these surface models are:</p>
<p>Surface Area: 3492.57 mm^2<br>
Volume: 10828.02 mm^3<br>
Number of Points: 1029<br>
Number of Cells: 336</p>
<p>I want to be able to change these specifications especially Number of Points and Number of Cells. How can I do that?</p>
<p>For example, I want to change these specifications in all my surface models to the following:<br>
Number of Points: 1200<br>
Number of Cells: 400</p>
<p>What modules should I use in Slicer or SlicerSALT?</p>
<p>In summary, My ultimate goal is to same number of points and number of cells in surface models. Please guide me as soon as possible.</p>
<p>Thanks a lot,<br>
Shahrokh</p>

---

## Post #2 by @nirotu (2018-04-19 13:05 UTC)

<p>If no of cells is,same as no of triangles, you can use reduce option in meshmixer, a standalone softwate.</p>

---

## Post #3 by @lassoan (2018-04-19 13:33 UTC)

<p>The easiest way to achieve matching number of points is to add duplicate points to all models that have less points than the others. Would that be acceptable? Why do you need exact match of number of points?</p>
<p>Do you need correspondence between mesh points (do you expect 123th point in mesh A to be at the same anatomical location as point 123th in mesh B)? If yes, then what you need is a spatial correspondence between meshes: transformation that transforms points of one mesh to the other. This transformation is computed by spatial registration algorithms. Once you have transform between mesh A to B, you can apply that to points of mesh A and get a mesh that has the same shape as mesh B, but contains exactly the same number of points and cells, in the same order, as mesh A.</p>
<p>There are several ways of registering meshes in Slicer. For example, you can import your meshes to Segmentation node and use the methods described in this post: <a href="https://discourse.slicer.org/t/align-two-segments-to-each-other/2570/4?u=lassoan">align two segments to each other </a>.</p>

---

## Post #4 by @cpinter (2018-04-19 13:33 UTC)

<p>You can try to use the Decimation option in the Surface Toolbox module, however there you cannot exactly specify the number of triangles, only a reduction factor. It might still be possible to make them match.</p>
<p>What exactly you want to achieve with having exactly the same number of cells and points?</p>

---

## Post #5 by @shahrokh (2018-04-22 10:36 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="2630">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>spatial correspondence</p>
</blockquote>
</aside>
<p>Hello<br>
Dear Anil, Andras and Csaba</p>
<p>Thank you very much for your advice.<br>
My tomographic images (MRI) are nifti format. Before, I convert region segmented (using itk-snap) to binary images.<br>
I convert these binary images to the model by “Grayscale Model Maker” module using Threshold equal to 1. For example, I have given the specifications of one of theses models in the my first message.</p>
<p>Unfortunately, I can not work with SlicerIGT and If I did not get it wrong, as Andras pointed out, I used “Surface Registration” in “CMF Registration”module to register these models .<br>
In this module, I select “Surface Registration” for “Type of Registration”.<br>
I select one of the models as the Fixed Model and the other model as Moving Model.<br>
The outputs of this module are the “Transform” matrix and the transmitted model.<br>
If I did not get it wrong, how can I use this matrix to integrate the number of points and cells between models? In other words, what Slicer module should I use for this purpose.</p>
<p>Your sincerely;<br>
Shahrokh</p>

---

## Post #6 by @cpinter (2018-04-22 12:41 UTC)

<p>Please try doing the segmentation using Slicer’s Segment Editor module. It is a relatively new, much improved segmentation module that I think you will find at least as good as ITK-Snap.</p>
<p>Then you can register the segmentations using the Segment Registration module, for which you need to install the Segment Registration extension from Extension Manager.</p>
<p>Let us know how it goes.</p>

---

## Post #7 by @lassoan (2018-04-22 13:28 UTC)

<p>If you already have a segmentation then you can load it into Slicer as a labelmap volume node and import that into a segmentation node (using Segmentations module).</p>
<p>After registration is completed, apply and harden the transform to the first model to get another model that has the same number of points and cells as the first model, but the shape of the second model.</p>

---

## Post #8 by @shahrokh (2018-04-23 11:47 UTC)

<p>Hello<br>
Dear Andras and Csaba</p>
<p>Sorry about that I can not to do it.<br>
At firstly, I mentioned that I did the steps that Andras pointed out, but unfortunately I did not succeed.<br>
I will explain all the processes that I do.</p>
<p>Process <span class="hashtag">#1:</span> Add Data<br>
At it, I add sample1_C1_group04.nii and sample1_C1_group05.nii. For doing it, I choose these files and tick “LabelMap”option in the window of “Add data into the scene”. I think that I do these step as mentioned Andras.</p>
<p>Process <span class="hashtag">#2:</span> “Model Maker” module<br>
In “Model Maker”, I do the following steps:<br>
1- In Input Volume, I select my first LabelMapVolume with the name ample1_C1_group04<br>
2- I create new ModelHierarchy<br>
3- I named it to ModelS1C1G4<br>
4- I set “Start Label” and “End Label” to 1<br>
5- I set “Smooth” to 0 and then “Apply”.<br>
6- I do steps above for my second LabelMapVolume with the name ample1_C1_group05<br>
After doing it, I have two models with the names of ModelS1C1G4 and ModelS1C1G5 with the following specifications:<br>
ModelS1C1G4:<br>
Surface Area: 3816.23 mm^2<br>
Volume: 133300.13 mm^3<br>
Number of Points: 1479<br>
Number of Cells: 541<br>
ModelS1C1G5:<br>
Surface Area: 2940.01 mm^2<br>
Volume:  9805.02 mm^3<br>
Number of Points: 1168<br>
Number of Cells: 449<br>
After doing, I can clearly see these two models, seperately.<br>
Note: I want that “Number of Points” and “Number of Cells” of ModelS1C1G5 are same as  ModelS1C1G4.</p>
<p>Process <span class="hashtag">#3:</span> “Model Registration” module<br>
At it, as mentioned Andras it, I want to calculate transform matrix; so I do the following steps:<br>
1- In “Input fixed (dense) model”, I select ModelS1C1G4.<br>
2- In “Input moving (sparse) model”, I select ModelS1C1G5.<br>
3- I create new LinearTransorm with the name of “LinearTransform_3”<br>
4- In part of “Advanced”, I select “Rigid” for “Transform type”.<br>
5- I click “Apply”.<br>
6- After doing it, I get 1.18665655941 in “Mean distance after registration”.</p>
<p>Process <span class="hashtag">#4:</span> “Transforms” module;<br>
1- I select “LinearTransform_3” in “Active Transform”<br>
2- In the part of “Apply transform”, firstly I select ModelS1C1G4 and apply “LinearTransform_3” to it.<br>
3- In “Data” module, I select  ModelS1C1G4 and then right click and select “Harden Transform”</p>
<p>After doing these steps, I expect to be equal to “Number of Points” and “Number of Cells” of  ModelS1C1G5 with ModelS1C1G4; but unfortunately, that did not happen.</p>
<p>I’m really confused. Please guide me to solve it.</p>
<p>Thanks a lot;<br>
Shahrokh.</p>

---

## Post #9 by @lassoan (2018-04-23 13:08 UTC)

<p>The main point is that when you apply a transform to a model, number of points or cells of that model does not change (compared to the original, non-transformed model).</p>
<p>I would recommend to not use Model Maker (unnecessary, Segmentations take care of conversions between various representations) and use Segment Registration for alignment (since it can do non-linear warping to better match the meshes).</p>

---

## Post #10 by @shahrokh (2018-04-23 13:38 UTC)

<p>Thanks a lot Andras.</p>
<p>Also,Csaba had also mentioned to use “Segment Registration” module in his message; but unfortunately, I can not find “Segment Registration” module; even I search “Segment Registration” in “Extension Manager” on Slicer. It was not.<br>
I work with Slicer version 4.6.2 r25516.<br>
Should I install this module (Segment Registration)?<br>
OR<br>
is it installed by default on Slicer? If Ok, what version is there?</p>
<p>Thanks a lot.<br>
Shahrokh</p>

---

## Post #11 by @lassoan (2018-04-23 13:45 UTC)

<p>Wow, Slicer 4.6 - that was released two years ago! We are making huge improvements to Slicer week by week, so a two-year-old version is completely outdated. You should always use at least the latest stable version(currently Slicer-4.8), and if you don’t find something there or something is not working as expected then try a recent nightly (not older than 1-2 weeks).</p>

---

## Post #12 by @shahrokh (2018-04-23 13:54 UTC)

<p><img src="https://emoji.discourse-cdn.com/twitter/blush.png?v=5" title=":blush:" class="emoji" alt=":blush:"></p>
<p>Dear Andras and Csaba,</p>
<p>Really excuse me, I download Slicer-4.9.0-2018-01-10-linux-amd64 and install  “Segment Registration” module. I really hope that my problems will be solved.<br>
Thanks thanks thanks<br>
Shahrokh</p>

---

## Post #13 by @cpinter (2018-04-23 14:38 UTC)

<p>Excellent, thanks for the update! I also hope it will work for your use case. Let us know if not.</p>

---

## Post #14 by @shahrokh (2018-04-25 09:36 UTC)

<p><img src="https://emoji.discourse-cdn.com/twitter/disappointed_relieved.png?v=5" title=":disappointed_relieved:" class="emoji" alt=":disappointed_relieved:"></p>
<p>Hello<br>
Dear Andras and Csaba</p>
<p>As mentioned you, at now, I work with Slicer-4.8.1-linux-amd64 and install “Segment Registration” module. Unfortunately I can not same “Number of Points” and “Number of Cells” between two models.</p>
<p>This may be better to point out my purpose. Please look at my post with titled “Shape analysis between non-similar objects?” in “3D Slicer Forum”.<br>
Briefly, suppose I have 5 groups with names A, B, C, D and E and in each group there are 8 meat samples (with size 2x2x2 cm^3 each sample, approximately). Each group was subjected to different laboratory procedures (physicochemical methods) and these procedures had a significant effect on the surface of the samples that it is recognizable by any observer.<br>
I get MRI images from these samples separately. I put meat samples from each group on the flat surface  (one chess score sheet) and after MRI acquisition, I cropped sample slice images and convert to binary segmented images using softwares such as itksnap, Seg3D and Slicer. Now I want to 3D surface analysis the effects of these procedures on the surface of these meat samples using SlicerSALT (SPHARM). At that time, Beatriz guide me that I have to check if correspondence is good across all meat samples. (I thank  Beatriz for all patiently guidance). Unfortunately, I did not understand how I can match meat samples.</p>
<p>At now, I want to same number of points and cells between two extracted models from MRI samples.</p>
<p>As mentioned Andras and Csaba, I download Slicer-4.8.1-linux-amd64 and install “Segment Registration” module.</p>
<p>For example, I do the following steps for two samples (binary segmented images):</p>
<p><strong><span class="hashtag">#1:</span> Load data as LabelMap (WITH tick “LabelMap”) :</strong><br>
File menu → Add data → Choose File(s) to Add: sample1_C1_group04.nii and sample1_C1_group04.nii</p>
<p><strong><span class="hashtag">#2:</span> Load data as volume (WITHOUT tick “LabelMap”):</strong><br>
File menu → Add data → Choose File(s) to Add: sample1_C1_group04.nii and sample1_C1_group04.nii<br>
Rename sample1_C1_group04.nii to Volume_sample1_C1_group04<br>
Rename sample1_C1_group05.nii to Volume_sample1_C1_group05</p>
<p><strong><span class="hashtag">#3:</span> Segmentations module:</strong><br>
In “Active segmentation” → Create new Segmentation with the name MySegmentation<br>
In “Export/import models and labelmaps” → in “Operation”, choose “Import” and in “Input type”choose “Labelmap” and select sample1_C1_group04 and in “Input node” and finally click on “Import” and again select sample1_C1_group05 in “Input node” and finally click on “Import”</p>
<p><strong><span class="hashtag">#4:</span> “Data” module:</strong><br>
In “Subject hierarchy” tab → right click on  “MySegmentation” and click on “Export visible segments to models”</p>
<p><strong><span class="hashtag">#5:</span> “Segment Registration” module:</strong><br>
In “Fixed image”		select	Volume_sample1_C1_group04<br>
In “Fixed segmentation”	select	MySegmentation<br>
In “Fixed segment” 		select	sample1_C1_group04<br>
In “Moving image” 		select	Volume_sample1_C1_group05<br>
In “Moving segmentation” 	select	MySegmentation<br>
In “Moving segment” 	select	sample1_C1_group05</p>
<p>in “Results” and “Applied registration on moving study, select “Deformable” defult and I can not changed it.<br>
Click on “Perform registration”<br>
After doing it, the options of “Applied registration on moving study” in “Results” could be changed.<br>
At this time, I get messages in “Log messages” window; as following:</p>
<p><em>Performing registration workflow</em><br>
<em>Cropping moving volume</em><br>
<em>Pre-aligning segmentations</em><br>
<em>Fixed segment bounds: [16.945327758789062, 59.18786621093749, -94.15547943115234, -79.90632629394531, -141.16146850585938, -102.09896850585938]</em><br>
<em>Moving segment bounds: [158.5375518798828, 200.83857727050778, -95.2843017578125, -77.4457015991211, -124.57463836669922, -100.2640151977539]</em><br>
<em>Moving to fixed segment translation: [-141.62146759033203, -0.6659011840820312, -9.210891723632812]</em><br>
<em>Resampling fixed volume</em><br>
<em>Creating contour labelmaps</em><br>
<em>Performing distance based registration</em><br>
<em>Setting up result visualization</em><br>
<em>Performing registration workflow</em><br>
<em>Cropping moving volume</em><br>
<em>Pre-aligning segmentations</em><br>
<em>Fixed segment bounds: [16.945327758789062, 59.18786621093749, -94.15547943115234, -79.90632629394531, -141.16146850585938, -102.09896850585938]</em><br>
<em>Moving segment bounds: [158.5375518798828, 200.83857727050778, -95.2843017578125, -77.4457015991211, -124.57463836669922, -100.2640151977539]</em><br>
<em>Moving to fixed segment translation: [-141.62146759033203, -0.6659011840820312, -9.210891723632812]</em><br>
<em>Warning: In /home/kitware/Dashboards/Package/Slicer-481/Libs/MRML/Core/vtkMRMLTransformNode.cxx, line 1515</em><br>
<em>vtkMRMLLinearTransformNode (0x6932680): vtkMRMLTransformNode::SetAndObserveMatrixTransformToParent method is deprecated. Use vtkMRMLTransformNode::SetMatrixTransformToParent instead</em></p>
<p>_DeserializeImageGeometry: Failed to de-serialize geometry string _</p>
<p><em>ApplyTransformOnReferenceImageGeometry: Failed to get reference image geometry</em></p>
<p><em>Resampling fixed volume</em><br>
_Found CommandLine Module, target is  /home/sn/Slicer-4.8.1-linux-amd64/lib/Slicer-4.8/cli-modules/ResampleScalarVolume _<br>
_ModuleType: CommandLineModule _<br>
_Resample Scalar Volume command line: _</p>
<p>_/home/sn/Slicer-4.8.1-linux-amd64/lib/Slicer-4.8/cli-modules/ResampleScalarVolume --spacing 1,1,1 --interpolation lanczos /tmp/Slicer/CCJDG_vtkMRMLScalarVolumeNodeB.nrrd /tmp/Slicer/CCJDG_vtkMRMLScalarVolumeNodeE.nrrd _<br>
_ _<br>
<em>Resample Scalar Volume completed without errors</em><br>
_ _<br>
<em>Loaded volume from file: /tmp/Slicer/CCJDG_vtkMRMLScalarVolumeNodeE.nrrd. Dimensions: 47x20x44. Number of components: 1. Pixel type: unsigned short.</em></p>
<p><em>Creating contour labelmaps</em><br>
<em>Performing distance based registration</em><br>
<em>Traceback (most recent call last):</em><br>
_  File “/home/sn/.config/NA-MIC/Extensions-26813/SlicerProstate/lib/Slicer-4.8/qt-scripted-modules/DistanceMapBasedRegistration.py”, line 249, in onApplyButton_<br>
_    logic.run(self.parameterNode)_<br>
_  File “/home/sn/.config/NA-MIC/Extensions-26813/SlicerProstate/lib/Slicer-4.8/qt-scripted-modules/DistanceMapBasedRegistration.py”, line 356, in run_<br>
_    (bbMin,bbMax) = self.getBoundingBox(fixedLabelNodeID, movingLabelNodeID)_<br>
_  File “/home/sn/.config/NA-MIC/Extensions-26813/SlicerProstate/lib/Slicer-4.8/qt-scripted-modules/DistanceMapBasedRegistration.py”, line 501, in getBoundingBox_<br>
_    unionLabelImage = (cast.Execute(fixedLabelImage) + cast.Execute(movingLabelImage)) &gt; 0_<br>
_  File “/home/sn/Slicer-4.8.1-linux-amd64/lib/Python/lib/python2.7/site-packages/SimpleITK/SimpleITK.py”, line 4254, in <strong>add</strong>_<br>
_    return Add( self, other )_<br>
_  File “/home/sn/Slicer-4.8.1-linux-amd64/lib/Python/lib/python2.7/site-packages/SimpleITK/SimpleITK.py”, line 11002, in Add_<br>
_    return <em>SimpleITK.Add(*args)</em><br>
<em>RuntimeError: Exception thrown in SimpleITK Add: /home/kitware/Dashboards/Package/Slicer-481-package/ITKv4/Modules/Core/Common/include/itkImageToImageFilter.hxx:241:</em><br>
<em>itk::ERROR: AddImageFilter(0x6675f10): Inputs do not occupy the same physical space! _<br>
<em>InputImage Origin: [1.2437664e+02, 9.9558647e+01, -1.4970284e+02], InputImage_1 Origin: [-1.7810860e+01, 9.4871147e+01, -1.3251534e+02]</em><br>
_	Tolerance: 1.5625000e-06</em></p>
<p><em>Setting up result visualization</em></p>
<p><strong><span class="hashtag">#5:</span> “Data” module:</strong><br>
In “Transform hierarchy” and in “Deformable Transform” list, right click on “Volume_sample1_C1_group05”  and select “Harden transform”</p>
<p><strong><span class="hashtag">#6:</span> “Models” module:</strong><br>
Unfortunately, I see that “Number of Points” and “Number of Cells” are NOT the same. Why?!</p>
<p>Please guide me;<br>
Shahrokh</p>

---

## Post #15 by @cpinter (2018-04-25 16:27 UTC)

<p>I’m not familiar with the shape analysis methods you’re trying to use, but ensuring an exact match between number of vertices seems like a very unrealistic goal.</p>
<p>Surface models are mostly used for 3D visualization, and analysis is almost always done on labelmaps, so such limitations have not been needed. But even if you achieve the same number of vertices somehow, it’s very hard to ensure that if you set a correspndence between each pair of vertex, they will really correspond spatially. As the shape and size of triangles is not a priority to keep consistent, there will be a “drift” eventually when you want to set up correspondence.<br>
You can use regularization methods to keep triangles the same size and shape, but then the smallest difference in your samples will result in a difference in number of vertices.</p>
<p>Have you considered using labelmaps or even other representations such as simplex meshes?</p>

---

## Post #16 by @shahrokh (2018-04-29 08:32 UTC)

<p>Hello<br>
Dear Csaba  and Andras</p>
<p>Thanks a lot for your replies. According with your guidance, I want to use labelmap volumes. I have some questions about it.<br>
1- Can I do comparison the surfaces of labelmaps between several groups?<br>
2- Can I create a average labmap volume from existing labmaps in a group?<br>
3- Can I compare between surface features of MRI (meat) samples  such as shrinkage?<br>
4- Can I compute distance between two labelmaps just like as “ModelToModelDistance” module?</p>
<p>The point I should mention is that MRI images taken from meat samples are in following conditions:<br>
a- The dimensions of the meat samples are not exactly the same. Their volume is almost equal to 8.0 cm^3 but certainly their dimensions are not same.<br>
b- The orientation of meat fibers is not the same.<br>
However, I think as two signals can be different in the frequency spectra, two surfaces can also be different in features such as spherical harmonics. In other words, I imagine MRI meat samples like as 3D signals that I want to extract fundamental frequencies and compare between them. How can I do it?</p>
<p>Also you mention to use simplex mesh. Please guide me to understand difference between simplex mesh and mesh available in 3DSlicer. At it, please give me more guidance.</p>
<p>Thanks a lot;<br>
Shahrokh</p>

---

## Post #17 by @lassoan (2018-04-29 13:57 UTC)

<aside class="quote no-group" data-username="shahrokh" data-post="16" data-topic="2630">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shahrokh/48/1499_2.png" class="avatar"> shahrokh:</div>
<blockquote>
<p>1- Can I do comparison the surfaces of labelmaps between several groups?</p>
</blockquote>
</aside>
<p>Segment statistics module provides surface area measurement for each individual segment.</p>
<aside class="quote no-group" data-username="shahrokh" data-post="16" data-topic="2630">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shahrokh/48/1499_2.png" class="avatar"> shahrokh:</div>
<blockquote>
<p>2- Can I create a average labmap volume from existing labmaps in a group?</p>
</blockquote>
</aside>
<p>You can, for example by aligning segments to each other, export them to labelmap, computing distance map (using Simple Filters module), average distance maps, and threshold it at 0.</p>
<aside class="quote no-group" data-username="shahrokh" data-post="16" data-topic="2630">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shahrokh/48/1499_2.png" class="avatar"> shahrokh:</div>
<blockquote>
<p>3- Can I compare between surface features of MRI (meat) samples  such as shrinkage?</p>
</blockquote>
</aside>
<p>Segment statistics gives you segment volume, so you can easily compute shrinkage.</p>
<aside class="quote no-group" data-username="shahrokh" data-post="16" data-topic="2630">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shahrokh/48/1499_2.png" class="avatar"> shahrokh:</div>
<blockquote>
<p>4- Can I compute distance between two labelmaps just like as “ModelToModelDistance” module?</p>
</blockquote>
</aside>
<p>Yes, I think difference of distance maps should provide that. Or, apply model to model distance on the segment exported to a model node.</p>
<p>Check out <a href="http://salt.slicer.org/">SlicerSalt shape analysis toolbox</a>. You may also experiment with simple PCA-based modeling, but for that you need to wrap ITK filters in a Slicer CLI module, as I don’t seem to find any module that wraps ITK’s PCA filters (<a href="https://itk.org/Doxygen/html/classitk_1_1ImagePCAShapeModelEstimator.html" class="inline-onebox">ITK: itk::ImagePCAShapeModelEstimator&lt; TInputImage, TOutputImage &gt; Class Template Reference</a> and others).</p>

---

## Post #18 by @cpinter (2018-04-30 15:30 UTC)

<aside class="quote no-group" data-username="shahrokh" data-post="16" data-topic="2630">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shahrokh/48/1499_2.png" class="avatar"> shahrokh:</div>
<blockquote>
<p>4- Can I compute distance between two labelmaps just like as “ModelToModelDistance” module?</p>
</blockquote>
</aside>
<p>You can also use the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/SegmentComparison">Segment Comparison module</a> from the SlicerRT extension.<br>
Of course it only makes sense after you established spatial correspondence, for example using the <a href="https://github.com/SlicerRt/SegmentRegistration">Segment Registration extension</a>.</p>
<p>Simplex mesh is a very special class of mesh that has been developed at Inria. It is a hexagon-based mesh that is designed to be regular. As far as I know there is no support for it in Slicer at this point, and it never became a standard representation, but if you like its features then it may be of interest. Keep in mind that adding its support in Slicer might be a huge project. Here’s a <a href="https://hal.inria.fr/inria-00074456/PDF/RR-2214.pdf">paper about it</a>.</p>

---
