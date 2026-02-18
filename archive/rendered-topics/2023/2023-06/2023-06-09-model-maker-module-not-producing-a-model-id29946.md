# Model Maker module not producing a model

**Topic ID**: 29946
**Date**: 2023-06-09
**URL**: https://discourse.slicer.org/t/model-maker-module-not-producing-a-model/29946

---

## Post #1 by @devjklein (2023-06-09 15:42 UTC)

<p>Hi all, I am on version 5.2.2 on Windows 11 and trying to run Model Maker on a dataset that I segmented. In IO I pick my segmentation, I created a new ModelHierachy, and I click apply. The module runs, but no 3D surface appears in the 3D view. I can get surfaces using Show 3D in the Segmentations module, but I would like more granular control over the model using the Model Maker Parameters and the ability to edit the model using Surface Toolbox.</p>
<p>Here is my debug log:</p>
<pre><code class="lang-auto">Model Maker standard output:

The input volume is: C:/Users/USER/AppData/Local/Temp/Slicer/CJJFG_vtkMRMLSegmentationNodeB.nrrd
The labels are: 
The starting label is: -1
The ending label is: -1
The model name is: Model
Do joint smoothing flag is: 0
Generate all flag is: 1
Number of smoothing iterations: 10
Number of decimate iterations: 0.25
Split normals? 1
Calculate point normals? 1
Pad? 1
Filter type: Sinc
Input color hierarchy scene file: None
Output model scene file: C:/Users/USER/AppData/Local/Temp/Slicer/CJJFG_AAAAABDECCDCEDGA.mrml#vtkMRMLModelHierarchyNode1
Color table file : 
Save intermediate models: 0
Debug: 1

Starting...
Models file: C:/Users/USER/AppData/Local/Temp/Slicer/CJJFG_AAAAABDECCDCEDGA.mrml
Model Hierarchy ID: vtkMRMLModelHierarchyNode1
Imported model scene file C:/Users/USER/AppData/Local/Temp/Slicer/CJJFG_AAAAABDECCDCEDGA.mrml
Got model hierarchy node vtkMRMLModelHierarchyNode1
GenerateAll! set make mult to true
useStartEnd = 0, numModelsToGenerate = 1, numFilterSteps 13
Adding 1 pixel padding around the image, shifting origin.
Image scalar max as double = 255

WARNING: due to lack of color label information, using the full scalar range of the input image when calculating the histogram over the image: 254
Setting histogram extentMax = 254
Skipping 0
Hist: Min = 1 and max = 1 (image scalar type = 3, max = 255)
GenerateAll flag is true, resetting the start and end labels from: -1 and -1 to 1 and 1

GenerateAll: there are 1 models to be generated.
Reset numFilterSteps to 13
Marching cubes: Using end label = 1, start label = 1
Image data extents: 0 639 0 639 0 767
Label    1 has 2.49823e+07 voxels.
End of looping over labels
Made models from labels: 1
Writing to model scene output file: C:/Users/USER/AppData/Local/Temp/Slicer/CJJFG_AAAAABDECCDCEDGA.mrml, to url: C:/Users/David/AppData/Local/Temp/Slicer/CJJFG_AAAAABDECCDCEDGA.mrml
Models saved to scene file C:/Users/David/AppData/Local/Temp/Slicer/CJJFG_AAAAABDECCDCEDGA.mrml
Cleaning up
Deleting cubes
Deleting hist
Deleting transform ijk to lps
Deleting ici, no set input null
Deleting reader
Deleting model scene
</code></pre>
<p>This appears to generate an output, but I do not know how to access this and I would expect this output to appear in my current scene 3D view.</p>

---

## Post #2 by @pieper (2023-06-09 21:11 UTC)

<p>Probably segmenttions shouldn’t be selectable as input.  You can right click on the segmentation in the Data module and convert it to a labelmap and then run the Model Maker on the exported labelmap.</p>

---
