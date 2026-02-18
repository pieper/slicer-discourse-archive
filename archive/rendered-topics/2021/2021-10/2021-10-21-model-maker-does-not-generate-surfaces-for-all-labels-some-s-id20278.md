# Model Maker does not generate surfaces for all labels - some skipped

**Topic ID**: 20278
**Date**: 2021-10-21
**URL**: https://discourse.slicer.org/t/model-maker-does-not-generate-surfaces-for-all-labels-some-skipped/20278

---

## Post #1 by @asims (2021-10-21 04:00 UTC)

<p>Hi</p>
<p>I have a segmented CT volume that I am happy with. The segmentation contains 12 labels. I converted the segmentation to a label map - with 12 labels.</p>
<p>Then in model maker attempted to generate surface models for each of my regions. It seemed to process but only returned 1 out of the 12 models.</p>
<p>The stdout reported that labels 1-11 were skipped. The skip unnamed labels check box was cleared - so I expected it to make a model for each label.</p>
<p><strong>Made models from labels: 12</strong><br>
<strong>Skipped making models from labels: 1 2 3 4 5 6 7 8 9 10 11</strong></p>
<p>The behaviour was the same with generate all model or starting and end numbers (1, 12).</p>
<p>I am using Slicer  4.11.202110226<br>
Running on RH7.9<br>
The standard output follows.</p>
<p>Thank you for any comment.<br>
Andrew</p>
<p>Model Maker standard output:<br>
The input volume is: /tmp/Slicer-andrews/DAIJF_vtkMRMLLabelMapVolumeNodeB.nrrd<br>
The labels are:<br>
The starting label is: 1<br>
The ending label is: 12<br>
The model name is: Model<br>
Do joint smoothing flag is: 0<br>
Generate all flag is: 1<br>
Number of smoothing iterations: 10<br>
Number of decimate iterations: 0.25<br>
Split normals? 1<br>
Calculate point normals? 1<br>
Pad? 1<br>
Filter type: Sinc<br>
Input color hierarchy scene file: None<br>
Output model scene file: /tmp/Slicer-andrews/DAIJF_AxHfcGGEAIFDIA.mrml#vtkMRMLModelHierarchyNode1<br>
Color table file : /tmp/Slicer-andrews/DAIJF_vtkMRMLColorTableNodeB.ctbl<br>
Save intermediate models: 1<br>
Debug: 1<br>
Starting…<br>
Models file: /tmp/Slicer-andrews/DAIJF_AxHfcGGEAIFDIA.mrml<br>
Model Hierarchy ID: vtkMRMLModelHierarchyNode1<br>
Imported model scene file /tmp/Slicer-andrews/DAIJF_AxHfcGGEAIFDIA.mrml<br>
Got model hierarchy node vtkMRMLModelHierarchyNode1<br>
GenerateAll! set make mult to true<br>
useStartEnd = 0, numModelsToGenerate = 1, numFilterSteps 16<br>
Adding 1 pixel padding around the image, shifting origin.<br>
Colour table file name = /tmp/Slicer-andrews/DAIJF_vtkMRMLColorTableNodeB.ctbl<br>
Setting the colour node’s storage node id to vtkMRMLColorTableStorageNode1, it’s file name = /tmp/Slicer-andrews/DAIJF_vtkMRMLColorTableNodeB.ctbl<br>
Read colour file /tmp/Slicer-andrews/DAIJF_vtkMRMLColorTableNodeB.ctbl<br>
Using color node to get max label<br>
Setting histogram extentMax = 12<br>
Skipping 0<br>
Hist: Min = 1 and max = 12 (image scalar type = 4, max = 32767)<br>
GenerateAll flag is true, resetting the start and end labels from: 1 and 12 to 1 and 12<br>
GenerateAll: there are 1 models to be generated.<br>
Reset numFilterSteps to 16<br>
Marching cubes: Using end label = 12, start label = 1<br>
Image data extents: 0 511 0 511 0 1567<br>
Label 12 has 9.16065e+07 voxels.<br>
Got color name, set label name = Model_12_Skin (color name w/o spaces = Skin)<br>
Number of polygons = 4981096<br>
Writing intermediate file /tmp/Slicer-andrews/Model_12_Skin-MarchingCubes.vtk<br>
After decimation, number of polygons = 3735822<br>
Writing intermediate file /tmp/Slicer-andrews/Model_12_Skin-Decimated.vtk<br>
Writing intermediate file /tmp/Slicer-andrews/Model_12_Skin-Smoothed.vtk<br>
Writing model Model_12_Skin to file /tmp/Slicer-andrews/Model_12_Skin.vtk<br>
Adding model Model_12_Skin to the output scene, with filename /tmp/Slicer-andrews/Model_12_Skin.vtk<br>
Got colour: 0.678431 0.654902 0.623529 1<br>
Added display node: id = vtkMRMLModelDisplayNode2<br>
Setting model’s storage node: id = vtkMRMLModelStorageNode1<br>
…done adding model to output scene<br>
End of looping over labels<br>
<strong>Made models from labels: 12</strong><br>
<strong>Skipped making models from labels: 1 2 3 4 5 6 7 8 9 10 11</strong><br>
Writing to model scene output file: /tmp/Slicer-andrews/DAIJF_AxHfcGGEAIFDIA.mrml, to url: /tmp/Slicer-andrews/DAIJF_AxHfcGGEAIFDIA.mrml<br>
Models saved to scene file /tmp/Slicer-andrews/DAIJF_AxHfcGGEAIFDIA.mrml<br>
Cleaning up<br>
Deleting cubes<br>
Deleting hist<br>
Deleting smootherSinc<br>
Deleting decimator<br>
Deleting mcubes<br>
Deleting image threshold<br>
… done deleting image threshold<br>
Deleting image to structured points<br>
Deleting transform ijk to lps<br>
Deleting transformer<br>
Deleting normals<br>
Deleting stripper<br>
Deleting ici, no set input null<br>
Deleting reader<br>
Deleting model scene</p>

---

## Post #2 by @muratmaga (2021-10-21 04:05 UTC)

<p>Is there a reason why you are using the model maker as oppose to directly exporting them as model from the Segmentations module?</p>

---

## Post #3 by @asims (2021-10-21 04:07 UTC)

<p>No - rusty and perhaps lack of awareness of the different methods. Will try.</p>
<p>Thanks</p>

---

## Post #4 by @asims (2021-10-21 22:23 UTC)

<p>Was able to generate models and output STL surfaces from the Segmentations module, however this resulted in a voxel based surface mesh with steps rather than a smoothed and decimated surface.</p>
<p>What is the preferred module for smoothing, and decimating surfaces prior to export?</p>
<p>I will look further into the documentation.</p>

---

## Post #5 by @muratmaga (2021-10-21 23:51 UTC)

<p>You can export an unsmoothened surface from the segmentaiton (there is no option for decimation that I know of at that step).<br>
For further decimation and smoothing of export models, you can use the SUrface Toolbox module.</p>

---

## Post #6 by @lassoan (2021-10-22 18:51 UTC)

<aside class="quote no-group" data-username="asims" data-post="4" data-topic="20278">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/8797f3/48.png" class="avatar"> asims:</div>
<blockquote>
<p>Was able to generate models and output STL surfaces from the Segmentations module, however this resulted in a voxel based surface mesh with steps rather than a smoothed and decimated surface.</p>
</blockquote>
</aside>
<p>The surface generated from labelmaps is smoothed by default. You can enable decimation by <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#panels-and-their-use">adjusting conversion parameters</a>, but since it require a little extra computation time it is usually not desired during interactive segmentation, and if you do it only once then Surface toolbox module offers more decimation options.</p>

---
