---
topic_id: 31794
title: "Inserting A Unique Module To Pipeline Creator"
date: 2023-09-19
url: https://discourse.slicer.org/t/31794
---

# Inserting a unique Module to Pipeline Creator

**Topic ID**: 31794
**Date**: 2023-09-19
**URL**: https://discourse.slicer.org/t/inserting-a-unique-module-to-pipeline-creator/31794

---

## Post #1 by @scottcollins3d (2023-09-19 18:24 UTC)

<p>Hello. Is there a way to insert unique module into the Pipeline Creator extension? Specifically, I would like to add Volume Clip With Model as a custom step in a pipeline. Thanks.</p>

---

## Post #2 by @ebrahim (2023-09-20 17:32 UTC)

<p>A timely question – check out the <a href="https://discourse.slicer.org/t/update-to-slicer-pipelines/31797">Slicer Pipelines update announcement</a> just posted.</p>

---

## Post #3 by @scottcollins3d (2023-09-20 18:21 UTC)

<p>Terrific! Thanks so much for your reply.</p>

---

## Post #4 by @Harald_Scheirich (2023-09-20 18:27 UTC)

<p>A good example is probably how we added the <a href="https://github.com/KitwareMedical/SlicerPipelines/blob/main/PipelineModules/_PipelineModules/SurfaceToolboxWrapping.py" rel="noopener nofollow ugc">Surface Toolbox pipeline steps</a>.</p>
<p>To be able to add a new step you need to</p>
<ul>
<li>Write a function that executes your functionality</li>
<li>add the <code>@slicerpipelines</code> decorator</li>
</ul>
<p>See also the <a href="https://github.com/KitwareMedical/SlicerPipelines/blob/main/Documentation/PipelineCreator.md#creating-a-pipeline-in-source" rel="noopener nofollow ugc">Pipelines Documentation</a> you <em>could</em> even do this in the Python Console.</p>
<p>Any pipeline that you create though will need to be able to <em>call</em> the code that you wrote so you will also need to make it persistent within the slicer environment. Otherwise you would not be able to execute your pipeline after a new start. It should probably be added to the module that it is mainly utilizing. If that is not accessible you could probably add it to a custom module created via the Extension Wizard, or just add it to you <code>.slicerrc.py</code>. You could add the function to the module that you created once it’s been stored.</p>

---

## Post #5 by @Lorenzo_Pierpaoli (2023-10-20 10:38 UTC)

<p>Hi!<br>
sorry for hijacking this thread, I work in the medical field and have limited coding experience, is it possible to add the Model Maker module as a new pipeline step in the way you explained?</p>

---

## Post #6 by @Harald_Scheirich (2023-10-20 12:24 UTC)

<p>Hi Lorenzo, yes it should be, you would need to put the functionality you need from Model Maker into a python function. I don’t know enough about Model Maker to be a good resource here. In most cases it’s calling some function of the modules <code>logic()</code>.</p>
<p>Although it looks like the Model Maker is a CLI module this might require a bit more work than a normal Slicer module (<a href="https://github.com/Slicer/Slicer/blob/main/Docs/developer_guide/python_faq.md" rel="noopener nofollow ugc">https://github.com/Slicer/Slicer/blob/main/Docs/developer_guide/python_faq.md</a>)</p>
<p>Maybe if you provide more specifics some of what you need some other community member can help you with this</p>

---

## Post #7 by @Lorenzo_Pierpaoli (2023-10-23 06:54 UTC)

<p>hi Herald, thank you for your answer, I will read through the python FAQ and see if I can do something myself.<br>
The goal would be to have a pipeline step that takes a labelmap and exports .stl files of that segment with the desired amount of smoothing applied (this value would be chosen in the creation of the pipeline or if possible at every use of the pipeline). I’m having trouble finding the ModelMaker modules functions in the software repository (so that I could at least use them in a python script) could you please indicate me where to find them?<br>
thank you very much</p>

---

## Post #8 by @Harald_Scheirich (2023-10-24 20:06 UTC)

<p>We talked a bit internally and it seems that the Model Maker module as it’s a CLI module doesn’t quite follow the pattern of the currently implemented modules. We’re currently looking into whether we can set up an example using the the Model Maker module, this might take a bit though</p>
<p>As an option the current implementation for the Segmentations tool only exposes access to the first segmentation. It would be a lot easier to write an version that takes the index of a segmentation to write out. Would that be of help or is what you need only achievable within the modelmaker ?</p>

---

## Post #9 by @Lorenzo_Pierpaoli (2023-10-25 07:38 UTC)

<p>Hi, I think it would be only possible from the model maker module but let me briefly explain what I need to do so you can confirm that there isn’t another way to do this.<br>
I need two different segments from a head CT scan, one including all the solid parts and one including only the air around the face and in the upper airways (I do this with thresholding and a bit of postprocessing of the segments). Then I export them to a labelmap and use the model maker module to apply two different types of smoothing (sinc and laplacian) to the models and export a pair of stl for each segment (one for each smoothing option). All this can be automated with a pipeline up to the labelmap export. I’m not in the position to change the smoothing approach (i.e. using the segment smoothing option) because I need to follow specific guidelines in the stl creation.<br>
thank you  and your colleagues for your help.</p>

---

## Post #10 by @lassoan (2023-10-26 02:51 UTC)

<p>I would recommend using segmentations for converting labelmap to closed surface. It uses Windows sinc smoothing, as Laplacian smoothing shrinks volumes.</p>
<p>Model Maker uses mini-scenes, which is a special method for importing a large set of models, which is not used anywhere else and therefore not well supported. Model Maker module is not used much anymore, since segmentations take care of generating closed surface representation automatically (and have many other advantages).</p>
<p>If you want to specifically study the issues with Laplacian smoothing then you can turn off smoothing in the segmentation (in representation conversion parameters) and then apply various VTK filters yourself (it takes 4-5 lines of Python script to run a VTK smoothing filter on a model node).</p>

---

## Post #11 by @Lorenzo_Pierpaoli (2023-10-26 07:57 UTC)

<p>Hi, thank you for your answer.<br>
Correct me if I’m wrong but are you saying that if I create a segment in the “Segment editor” module with the smoothing switched on (lets say with the value of 0.10) and then export it through the “Segmentations” module “Export to files” function in STL format I would obtain the same STL produced by the Model Maker module when choosing the Sinc smoothing option with the value of 0.1? ( In the Model Maker case I would export the segments  without smoothing to a labelmap)</p>

---

## Post #12 by @lassoan (2023-10-26 12:12 UTC)

<p>Smoothing factor is not interpreted the same way (in segmentation we use a logarithmic scale to make it easier for users to cover a wide range) but the same VTK classes are used.</p>

---
