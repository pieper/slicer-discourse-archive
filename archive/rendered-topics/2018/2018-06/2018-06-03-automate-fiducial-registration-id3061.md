---
topic_id: 3061
title: "Automate Fiducial Registration"
date: 2018-06-03
url: https://discourse.slicer.org/t/3061
---

# Automate Fiducial Registration

**Topic ID**: 3061
**Date**: 2018-06-03
**URL**: https://discourse.slicer.org/t/automate-fiducial-registration/3061

---

## Post #1 by @Hikmat (2018-06-03 22:03 UTC)

<p>Operating system: Windows 10<br>
Slicer version: Slicer 4.8.1</p>
<p>Hi,</p>
<p>I am writing a simulator which requires the registration of CT and MRI images. I am satisfied with Fiducial Registration; however, the steps required to perform this procedure may be intensive to the user (Registration -&gt; Specialized -&gt; Fiducial Registration -&gt; Fixed Landmarks -&gt; Moving Landmarks -&gt; Save Transform -&gt; Apply)</p>
<p>I would like to automate this registration procedure (implement it programmatically) to simplify the U/I steps (I would still require the user to create the markups manually). Is there some code snippet for automating the Fiducial Registration module and setting its respective parameters? I went through the ScriptRepository Documentation but couldn’t find what I was looking for.</p>
<p>Thanks.</p>

---

## Post #2 by @lassoan (2018-06-04 14:07 UTC)

<p>Fiducial Registration module is a CLI module, which can be run from Python as described here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Running_a_CLI_from_Python" class="inline-onebox">Documentation/Nightly/Developers/Python scripting - Slicer Wiki</a></p>
<aside class="quote no-group" data-username="Hikmat" data-post="1" data-topic="3061">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/ecccb3/48.png" class="avatar"> Hikmat:</div>
<blockquote>
<p>I would like to automate this registration procedure (implement it programmatically) to simplify the U/I steps (I would still require the user to create the markups manually)</p>
</blockquote>
</aside>
<p>Once you’ve figured out a complete processing workflow and you would like to perform it many times or you would like inexperienced users to reproduce the workflow then writing a custom Python scripted module is a good idea. I would strongly recommend to not require users to create any nodes manually. You can save all the nodes that your module is using into a scripted parameter node - see more details <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ/Python_Scripting#How_to_save_user.27s_selection_of_parameters_and_nodes_in_the_scene.3F">here</a>.</p>

---

## Post #3 by @timeanddoctor (2018-06-06 11:11 UTC)

<p>Did you found the method for automating the Fiducial Registryation with CLI?</p>

---

## Post #4 by @Hikmat (2018-06-06 14:12 UTC)

<p>Yes, I did. Apologies for not updating the status quo, it’s just that I’m still thinking about how I want to go about this.</p>

---

## Post #5 by @brhoom (2018-10-15 16:48 UTC)

<p><strong>Related question,</strong></p>
<p>How to use this module from cmd. It is not clear how to provide the landmarks as input ordered list arguments and it would be nice to add this to the module wiki. I tried:</p>
<pre><code>   ~/sw/Slicer-4.8.1/Slicer --launch ~/sw/Slicer-4.8.1/lib/Slicer-4.8/cli-modules/FiducialRegistration --returnparameterfile transform.txt  --transformType  Rigid --saveTransform  --movingLandmarks -42.3584 -32.6622  24.675 -2.39974 -40.2918  -35.3744 -8.60695 -41.5944  --fixedLandmarks    -12.753 -180.318 -251.67 26.5668 -143.192 -246.78 -33.6808 -138.784
</code></pre>
<p>I also tried using [x y z ] or [x,y,z] and () in addition to provide the fixed and landmarks as fcsv files but nothing works</p>
<p>What is the correct format for providing the landmarks?</p>

---

## Post #6 by @brhoom (2018-10-16 16:26 UTC)

<p>Here is a python script example:</p>
<pre><code> # create a transform node and add it to the scene
 transformNode = slicer.vtkMRMLLinearTransformNode()
 slicer.mrmlScene.AddNode(transformNode) 

parameters = {}
parameters["saveTransform"]   = transformNode.GetID() 
parameters["movingLandmarks"] = movingMarkupNode.GetID() #  fiducial points  
parameters["fixedLandmarks"]  = fixedMarkupNode.GetID()        #  fiducial points  
fiduciaReg = slicer.modules.fiducialregistration
slicer.cli.runSync(fiduciaReg, None, parameters)    # run the registration</code></pre>

---

## Post #7 by @lassoan (2018-10-16 16:34 UTC)

<aside class="quote no-group" data-username="brhoom" data-post="5" data-topic="3061">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/brhoom/48/1228_2.png" class="avatar"> brhoom:</div>
<blockquote>
<p>What is the correct format for providing the landmarks?</p>
</blockquote>
</aside>
<p>You can run a CLI from the GUI and see in application log what command was used. If you enable developer mode in application settings then all input and output files are preserved after running a CLI module, so you can inspect file content, too.</p>

---

## Post #8 by @brhoom (2018-10-16 16:43 UTC)

<blockquote>
<p>see in application log</p>
</blockquote>
<p>Cool, this is really useful, in Ubuntu I found it in /tmp/Slicer-username/Slicer_version_date_time.log</p>
<p>Here is an example of the arguments</p>
<pre><code>        --returnparameterfile file.params --fixedLandmarks 1.854,-127.381,-260.861 --fixedLandmarks -3.282,-126.126,-261.026 --fixedLandmarks -6.907,-126.92,-261.026 --movingLandmarks -4.91273,5.92777,-58.4992 --movingLandmarks -7.72868,5.14361,-58.4387 --movingLandmarks -11.3224,4.54754,-57.7137 --saveTransform trsform.txt --transformType Rigid
</code></pre>
<p>so we need to use  --fixedLandmarks and  --fixedLandmarks multiple times.</p>

---

## Post #9 by @lassoan (2020-06-26 15:18 UTC)

<p>A post was split to a new topic: <a href="/t/automate-model-to-ct-registration/12234">Automate model to CT registration</a></p>

---
