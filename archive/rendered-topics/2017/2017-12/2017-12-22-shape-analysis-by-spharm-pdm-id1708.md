---
topic_id: 1708
title: "Shape Analysis By Spharm Pdm"
date: 2017-12-22
url: https://discourse.slicer.org/t/1708
---

# Shape analysis by SPHARM-PDM

**Topic ID**: 1708
**Date**: 2017-12-22
**URL**: https://discourse.slicer.org/t/shape-analysis-by-spharm-pdm/1708

---

## Post #1 by @sodaGH (2017-12-22 11:25 UTC)

<p>Operating system: windows7_64<br>
Slicer version: 4.4.0<br>
Expected behavior: I want to do the shape analysis by SPHARM-PDM<br>
Actual behavior:</p>
<ol>
<li>I have apply the shape analysis module, when I load the output.csv file in ShapePopulationViewer, it pop up error like this:<br>
ERROR: In …\VTKv6\Rendering\FreeType\vtkTextActor.cxx, line 364<br>
vtkTextActor (0000000008811FE0): vtkTextActor::SetInput was passed an uninitialized string</li>
</ol>
<p>ERROR: In …\VTKv6\Rendering\FreeType\vtkTextActor.cxx, line 364<br>
vtkTextActor (00000000089219D0): vtkTextActor::SetInput was passed an uninitialized string</p>
<p>ERROR: In …\VTKv6\Rendering\FreeType\vtkTextActor.cxx, line 364<br>
vtkTextActor (0000000008A610C0): vtkTextActor::SetInput was passed an uninitialized string</p>
<p>ERROR: In …\VTKv6\Rendering\FreeType\vtkTextActor.cxx, line 364<br>
vtkTextActor (0000000008811FE0): vtkTextActor::SetInput was passed an uninitialized string</p>
<p>ERROR: In …\VTKv6\Rendering\FreeType\vtkTextActor.cxx, line 364<br>
vtkTextActor (00000000089219D0): vtkTextActor::SetInput was passed an uninitialized string</p>
<p>ERROR: In …\VTKv6\Rendering\FreeType\vtkTextActor.cxx, line 364<br>
vtkTextActor (0000000008A610C0): vtkTextActor::SetInput was passed an uninitialized string</p>
<p>ERROR: In …\VTKv6\Rendering\FreeType\vtkTextActor.cxx, line 364<br>
vtkTextActor (0000000008811FE0): vtkTextActor::SetInput was passed an uninitialized string</p>
<p>ERROR: In …\VTKv6\Rendering\FreeType\vtkTextActor.cxx, line 364<br>
vtkTextActor (00000000089219D0): vtkTextActor::SetInput was passed an uninitialized string</p>
<p>ERROR: In …\VTKv6\Rendering\FreeType\vtkTextActor.cxx, line 364<br>
vtkTextActor (0000000008A610C0): vtkTextActor::SetInput was passed an uninitialized string</p>

---

## Post #2 by @laurapascal (2017-12-22 16:27 UTC)

<p>Hello,</p>
<p>Thank you for showing your interest in SPHARM-PDM Extension!</p>
<p>The issue could be due by the use of the version 4.4 of Slicer. I highly recommend you to use the new release 4.8 of Slicer that you can download <a href="http://download.slicer.org/" rel="nofollow noopener">here</a>.</p>
<p>If you need any more help, I will be happy to help you!</p>

---

## Post #3 by @sodaGH (2017-12-23 03:24 UTC)

<p>Hi Laura :</p>
<p>Thanks for your reply!</p>
<p>I want to use SPHARM-PDM to do the shape analysis of hippocampus on my brain MRI data. I’m new to this field and not familiar with this software. I did the shape analysis on my data and it generated several file folders such as “BatchMake_Scripts”, “EulerFiles”, “Mesh”, “OutputGroupFile” and “Template”.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8bccee078b7f10eba18d440490763d2a7bbc0329.png" alt="image" data-base62-sha1="jWJqz2j5NUhh1Q11PLOiflcno6J" width="372" height="287"></p>
<p>Now I want to do the following feature selection and classification steps, but I don’t know which file to choose. I want to know in which file the shape analysis information was stored and how should I use it.</p>
<p>Thanks for your reading. Looking forward to your reply!</p>

---

## Post #4 by @sodaGH (2017-12-24 04:48 UTC)

<p>hi <a class="mention" href="/u/laurapascal">@laurapascal</a></p>
<p>I followed your advice and installed 3D Slicer V4.8. After applying shape analysis module, it generated 3 subfolders:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a13cae8ea8befc783227c801af03e20df55cb55.png" alt="image" data-base62-sha1="azjJM1drBR1n9vqqGrAWNtrfSjb" width="330" height="166"></p>
<p>Can you guide me what should I do next in order to get the shape analysis results? My next step is feature selection and classification, which file stores the shape information I need?<br>
Thanks for your reading and reply!</p>

---

## Post #5 by @laurapascal (2017-12-29 04:57 UTC)

<p>Hi <a class="mention" href="/u/sodagh">@sodaGH</a>,</p>
<p>In each folder you will find the results of each step of the SPHARM-PDM process. The final results are contained in the folder named <em>step3_ParaToSPHARMMesh</em>. In this folder, you will find the corresponding shape population composed by models which have the same number of points at corresponding position.</p>
<p>You will find 3 similar groups composed by the same corresponding shape population where each group is based on a different model registration:</p>
<ul>
<li>the <em>input_rootname_pp_surf_SPHARM</em> VTK models which are not registered between them.</li>
<li>the <em>input_rootname_pp_surf_SPHARM_ellalign</em> VTK models which are registered with the sphere used to create them.</li>
<li>the <em>input_rootname_pp_surf_SPHARM_procalign</em> VTK models which are registered with a template that you can specify by using the <em>Registration Template Option</em>.</li>
</ul>
<p>In order to statistically compare the regional differences between two models, you can apply the module <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/ModelToModelDistance" rel="nofollow noopener">ModelToModelDistance</a> (available as a module of 3DSilcer): it will compute a distance map between two models with the option corresponding_point_to_point (which will compute the euclidean distance for each corresponding point of your two models). You can then visualize the distance map in <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/ShapePopulationViewer" rel="nofollow noopener">ShapePopulationViewer</a> (available in SlicerSALT and 3DSlicer) by displaying the attribute <em>PointToPointVector</em>.</p>
<p>In order to classify 3D models according to their morphological variation, you can use the extension <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/ShapeVariationAnalyzer" rel="nofollow noopener">ShapeVariationAnalyzer</a><br>
(available in 3DSilcer). This classifier can be used to identify shapes, help to provide a diagnosis, or evaluate the staging of a disease.</p>
<p>If you have any additional questions, I will be happy to answer them!</p>

---

## Post #6 by @stevenagl12 (2019-04-19 01:05 UTC)

<p>Can you create an average shape from these results, or does it automatically generate an average shape?</p>

---

## Post #7 by @bpaniagua (2019-04-24 18:36 UTC)

<p>Hi Steven,</p>
<p>You can currently create an average from the PDMs generated from SPHARM using <a href="https://github.com/NIRALUser/SPHARM-PDM/blob/master/Modules/CLI/MetaMeshTools/MeshMath.cxx" rel="nofollow noopener">MeshMath</a>. We are currently porting some of the MeshMath functionality into the SurfaceToolbox. I will keep everybody posted with how that goes.</p>
<p>Thank you,<br>
Beatriz</p>

---

## Post #8 by @Shivi23 (2023-04-09 18:09 UTC)

<p>Hello,</p>
<p>I am trying to follow this advice and use ShapeVariationAnalyzer for my research. However, after adding the extension I do not see it showing up in Modules. Please help … I have seen some posts saying that ShapeVariationAnalyzer does not work for some versions of Slicer is this true? And if so, what is the next best too to classify 3D models according to their morphological variation? I have already ran my data to create SPHARM outputs and I want to use them to classify 3D models according to their morphological variation. Please help. Thanks!</p>

---

## Post #9 by @mturja-vf-ic-bd (2023-05-02 19:17 UTC)

<p>Dear Shrivani,</p>
<p>I am writing to inform you that we are currently working on a Slicer extension named “<a href="https://github.com/mturja-vf-ic-bd/SlicerDeepLearningUI" rel="noopener nofollow ugc">SurfaceLearning</a>” which we believe would be a suitable solution for your specific use-case. The purpose of this deep learning module is to classify shapes, such as the hippocampus, brain surface, etc. It comes equipped with a range of popular deep learning models, including ResNet, EfficientNet, and DenseNet, as well as a simpler CNN-based classifier.</p>
<p>If you are interested in giving “SurfaceLearner” a try, I would be delighted to guide you through the process of using it. Please feel free to respond to this message or reach out to me via email at <a href="mailto:mturja@cs.unc.edu">mturja@cs.unc.edu</a>.</p>
<p>Best,<br>
Turja.</p>

---
