---
topic_id: 409
title: "Help With Accessing Module Logic In Python Scripted Modules"
date: 2017-05-31
url: https://discourse.slicer.org/t/409
---

# Help with Accessing Module Logic in Python Scripted Modules

**Topic ID**: 409
**Date**: 2017-05-31
**URL**: https://discourse.slicer.org/t/help-with-accessing-module-logic-in-python-scripted-modules/409

---

## Post #1 by @_jmichael (2017-05-31 22:08 UTC)

<p>Hi folks,<br>
I’m just getting started with slicer and python and I’m hoping to get some help regarding how to access the underlying logic of Slicer modules from within a python script? (i.e. the Python interactor or the python code of a scripted module)</p>
<p>Specifically, I’ve got a scripted module I made using the Extension Wizard (after working through <a href="https://www.slicer.org/w/images/c/c0/Slicer4_ProgrammingTutorial_Slicer4.5.pdf" rel="noopener nofollow ugc">these </a> <a href="https://docs.google.com/presentation/d/1JXIfs0rAM7DwZAho57Jqz14MRn2BIMrjB17Uj_7Yztc/edit#slide=id.g420896289_0102" rel="noopener nofollow ugc">two</a> tutorials on python and python modules). In the ‘run’ section of my scripted module, I’d like to call the Simple Filters module to use the ConnectedThresholdImageFilter and then call the Model Maker module to turn that segmentation into a model.</p>
<p>I’ve found <a href="http://www.na-mic.org/Wiki/index.php/AHM2012-Slicer-Python#CLI_Modules" rel="noopener nofollow ugc">this</a> example showing the use of the Model Maker module via python, but I’m hoping to have an understanding that’s more generalizable to other modules (i.e. are all modules accessed via “slicer.cli.run( …)”? How would I figure out which parameters need to be passed to the module if I didn’t know them in advance?).</p>
<p>Thanks in advance for your help!</p>

---

## Post #2 by @Fernando (2017-05-31 22:48 UTC)

<p>Hi Justin,</p>
<p>You can get the parameters of CLI modules as described in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Running_a_CLI_from_Python" rel="nofollow noopener">wiki</a>.</p>
<p>I think you can have access to the logic of Slicer modules like this:<br>
<code>&gt;&gt;&gt; slicer.vtkSlicerTransformLogic()</code><br>
<code>(vtkCommonCorePython.vtkSlicerTransformLogic)0x138f47738</code><br>
<code>&gt;&gt;&gt; slicer.modules.transforms.logic()</code><br>
<code>(vtkCommonCorePython.vtkSlicerTransformLogic)0x138f476d0</code></p>
<p>I don’t think you need to use the <code>Simple Filters</code> module if you’re doing Python. You can just use <code>SimpleITK</code> in your code.</p>

---

## Post #3 by @_jmichael (2017-06-02 03:39 UTC)

<p>Hi Fernando,<br>
Thanks so much for your help! I’ve been able to sort out the details of using the model maker CLI module to go from label map to model as well as using SimpleITK to perform the segmentation.</p>
<p>My only remaining hiccup is that in trying to connect the two, the filter in SimpleITK returns a scalar volume node while the model maker module requires a label-map to behave as intended (when I pass it a volume node it still runs but it appears to be trying to make a model out of the entire volume rather than the segmented area only). I can see the Volumes module can do this with the ‘Convert to Label Map’ button but I’m unsure how to call that button from a python script (unlike module maker, the Volumes appears to be a loadable module rather than a CLI one).</p>

---

## Post #4 by @Fernando (2017-06-02 08:11 UTC)

<p>Try looking in <code>slicer.modules.volumes.logic()</code></p>
<p>It’s what happens when you click on the button anyway: <a href="https://github.com/Slicer/Slicer/blob/eefeac9286f48552e8418a11f412b2823a09b407/Modules/Loadable/Volumes/qSlicerVolumesModuleWidget.cxx#L138" rel="nofollow noopener">https://github.com/Slicer/Slicer/blob/eefeac9286f48552e8418a11f412b2823a09b407/Modules/Loadable/Volumes/qSlicerVolumesModuleWidget.cxx#L138</a></p>
<p>I searched “Convert to label map” in the <a href="https://github.com/Slicer/Slicer" rel="nofollow noopener">3D Slicer repository</a> and found what I was looking for in the first result.</p>

---

## Post #5 by @lassoan (2017-06-02 14:19 UTC)

<p>Instead of maintaining a labelmap for editing and slice display and model(s) for 3D display and converting between manually, I would strongly recommend to use a segmentation node. With just 4 lines of Python code, you can create segmentation node from a labelmap, and after that the segmentation node takes care of all visualization and conversion:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Create_a_segmentation_from_a_labelmap_volume_and_display_in_3D" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Create_a_segmentation_from_a_labelmap_volume_and_display_in_3D</a></p>
<p>Using segmentation has many advantages compared to using labelmaps and models, including:</p>
<ul>
<li>you have only one node, which can be displayed in slice and 3D views: no need for “model making” etc.</li>
<li>you can directly edit the segmentation using the new Segment editor module (which is far more capable than the old Editor module)</li>
<li>when labelmap changes, all views in slice and 3D views are updated automatically</li>
<li>there are more visualization options for segmentation than for labelmaps and models (see in the Segmentations module)</li>
<li>segments may overlap</li>
</ul>

---

## Post #6 by @_jmichael (2017-06-02 19:24 UTC)

<p>Fernando, thanks again for your help! I’m also pretty new to github so I hadn’t realized you could search an entire repository. I’ve now got the pipeline of segmentation and model making working as intended.</p>
<p>Andras, I already had the model making process sorted out so I won’t bother re-factoring this time around but I looked at your suggested approach and I agree it seems much simpler. I’ll be sure to keep that in mind for future.</p>

---
