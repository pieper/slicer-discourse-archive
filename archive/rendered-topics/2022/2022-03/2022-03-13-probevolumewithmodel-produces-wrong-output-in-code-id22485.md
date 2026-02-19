---
topic_id: 22485
title: "Probevolumewithmodel Produces Wrong Output In Code"
date: 2022-03-13
url: https://discourse.slicer.org/t/22485
---

# ProbeVolumeWithModel produces wrong output in code

**Topic ID**: 22485
**Date**: 2022-03-13
**URL**: https://discourse.slicer.org/t/probevolumewithmodel-produces-wrong-output-in-code/22485

---

## Post #1 by @Muhammed_Fatih_Talu (2022-03-13 16:36 UTC)

<p>When I use the GUI of the ProbeVolumeWithModel, there is no problem. It does great coloring.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a983f9697cdb283c4bca6feb5994dccc1439fb3c.png" alt="image" data-base62-sha1="obBrEG7TdEaGj6Lf1qAKwyl9ugs" width="609" height="291"></p>
<p>But, when I want to do the same with the following codes, it runs and produces a plane output. Why?</p>
<pre><code class="lang-auto"># Inputs
InputModelNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLModelNode")
OutputModelNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLModelNode", "Skull_Thickness")

#Parameters for ProbeVolumeWithModel
parameters = {}
parameters['InputVolume'] = DistanceMapNode.GetID()
parameters['InputModel'] = InputModelNode.GetID()
parameters['OutputModel'] = OutputModelNode.GetID()

probe = slicer.modules.probevolumewithmodel
slicer.cli.run(probe, None, parameters, wait_for_completion=True)
</code></pre>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6af476b06885b3b31ab0039aa1d3d7dcf653294f.png" alt="image" data-base62-sha1="fgan6XnwpW5ozdeACcfaRQczDpZ" width="490" height="387"></p>

---

## Post #2 by @pieper (2022-03-13 17:29 UTC)

<p>Check in the application log to see what’s different in the command line options when the module runs.</p>

---

## Post #3 by @Muhammed_Fatih_Talu (2022-03-13 19:11 UTC)

<p>Steve, thanks for reply.<br>
First, I was excited and examined the log file (as below).<br>
I thought I could find the step-by-step python codes of the process done in the log file.<br>
However, the log file unfortunately did not have detailed content.</p>
<pre><code class="lang-auto">[DEBUG][Qt] 13.03.2022 21:36:02 [] (unknown:0) - Switch to module:  "ProbeVolumeWithModel"
[DEBUG][Qt] 13.03.2022 21:36:20 [] (unknown:0) - Found CommandLine Module, target is  C:/ProgramData/NA-MIC/Slicer 4.13.0-2022-02-11/bin/../lib/Slicer-4.13/cli-modules/ProbeVolumeWithModel.exe
[DEBUG][Qt] 13.03.2022 21:36:20 [] (unknown:0) - ModuleType: CommandLineModule
[DEBUG][Qt] 13.03.2022 21:36:22 [] (unknown:0) - Probe Volume With Model command line: 

C:/ProgramData/NA-MIC/Slicer 4.13.0-2022-02-11/bin/../lib/Slicer-4.13/cli-modules/ProbeVolumeWithModel.exe --outputArrayName NRRDImage C:/Users/Administrator/AppData/Local/Temp/19/Slicer/BIBHG_vtkMRMLScalarVolumeNodeE.nrrd C:/Users/Administrator/AppData/Local/Temp/19/Slicer/BIBHG_vtkMRMLModelNodeE.vtk C:/Users/Administrator/AppData/Local/Temp/19/Slicer/BIBHG_vtkMRMLModelNodeF.vtk
[DEBUG][Qt] 13.03.2022 21:36:24 [] (unknown:0) - Probe Volume With Model standard output:

Done reading the file C:/Users/Administrator/AppData/Local/Temp/19/Slicer/BIBHG_vtkMRMLScalarVolumeNodeE.nrrd
[DEBUG][Qt] 13.03.2022 21:36:24 [] (unknown:0) - Probe Volume With Model completed without errors
</code></pre>

---

## Post #4 by @pieper (2022-03-13 19:53 UTC)

<p>Hi <a class="mention" href="/u/muhammed_fatih_talu">@Muhammed_Fatih_Talu</a> -</p>
<p>Yes, this is expected - the ProbeVolumeWithModel module is a <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Modules">C++ command line module</a> so when you run it from the GUI your widget selections are converted into command line arguments.  To call the same module from python you need to make sure your command has all the same arguments of the right types.  Both ways of running the module will log the command line in the log.</p>

---

## Post #5 by @Muhammed_Fatih_Talu (2022-03-14 06:00 UTC)

<p>I solved the problem.<br>
I was not getting the correct ID of InputModelNode.</p>
<p>instead of slicer.mrmlScene.GetFirstNodeByClass(“vtkMRMLModelNode”),<br>
I used slicer.mrmlScene.GetFirstNodeByName(“InputModel”).<br>
It runs perfect <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"><br>
Thanks every body.</p>

---

## Post #6 by @lassoan (2022-03-14 12:55 UTC)

<p>Image slices are displayed in 3D views as model nodes, therefore the first 3 model nodes are typically these slice plane nodes.</p>
<p><a class="mention" href="/u/pieper">@pieper</a> what do you think about adding a flag to GetFirstNodeByName method to include/exclude hidden nodes and by default make hidden nodes excluded? This would change the behavior of the method by default, but since this is a high-level convenience function, the expected behavior is probably to not consider hidden nodes.</p>

---

## Post #7 by @pieper (2022-03-14 13:24 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="22485">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a class="mention" href="/u/pieper">@pieper</a> what do you think about adding a flag to GetFirstNodeByName method to include/exclude hidden nodes and by default make hidden nodes excluded? This would change the behavior of the method by default, but since this is a high-level convenience function, the expected behavior is probably to not consider hidden nodes.</p>
</blockquote>
</aside>
<p>Yes, those convenience methods (also <code>getNode</code> in python) seem to regularly lead to some confusion; making them behave better could help.  Maybe in <code>slicer.util</code> we should provide a <code>pickNode</code> method that pops up a gui node combo box and use that in the script repository instead of teaching people to use the less reliable methods.</p>

---

## Post #8 by @lassoan (2022-03-14 16:12 UTC)

<p>This is a very interesting discussion, I’ve started a new topic for it to get some more visibility:</p>
<aside class="quote quote-modified" data-post="1" data-topic="22498">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/make-it-easier-to-select-input-nodes-for-python-scripts/22498">Make it easier to select input nodes for Python scripts</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    While discussing a <a href="https://discourse.slicer.org/t/probevolumewithmodel-produces-wrong-output-in-code/22485">problem due to selecting the wrong input node in a Python script</a>, we started to brainstorm about how to make it easier to select input nodes for Python scripts. 
The first idea was to <a href="https://discourse.slicer.org/t/probevolumewithmodel-produces-wrong-output-in-code/22485/6">change vtkMRMLScene::GetFirstNodeByName to return non-hidden node</a> by default. 
Then <a class="mention" href="/u/pieper">@pieper</a> raised the idea of <a href="https://discourse.slicer.org/t/probevolumewithmodel-produces-wrong-output-in-code/22485/7">adding a slicer.util.pickNode method to show a popup where the user can select a node</a>. 
I’ve created this topic to make this discussion more visible and get some more ideas and feedback …
  </blockquote>
</aside>


---
