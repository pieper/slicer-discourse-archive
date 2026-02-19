---
topic_id: 7217
title: "Fiducial Registration Wizard Custom Transformation Configura"
date: 2019-06-18
url: https://discourse.slicer.org/t/7217
---

# Fiducial registration Wizard - custom transformation configuration

**Topic ID**: 7217
**Date**: 2019-06-18
**URL**: https://discourse.slicer.org/t/fiducial-registration-wizard-custom-transformation-configuration/7217

---

## Post #1 by @zapaishchykova (2019-06-18 14:14 UTC)

<p>Hi everyone,<br>
I’m struggling with Fiducial Registration Wizard. So, what I’m trying to do is the following:<br>
The user adds few fiducial points and then User clicks on button and all “To fiducial” points are computed (1) - how do i access module  “place fiducial using transform” with my transform via python?</p>
<p>My next following question is how to configure a registration result(2) also via python? I create the new transormation result like following:</p>
<blockquote>
<pre><code>imageToProbe = slicer.vtkMRMLLinearTransformNode()
imageToProbe.SetName('ImageToProbe')
slicer.mrmlScene.AddNode(imageToProbe)
</code></pre>
</blockquote>
<p>Thank you all in advance!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/1342954fdf57b467b3f507f6cab1c51d5fe2c820.png" data-download-href="/uploads/short-url/2KnJ0kO4nHo3avXsNxkNDNeoU8g.png?dl=1" title="question2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/1342954fdf57b467b3f507f6cab1c51d5fe2c820_2_616x500.png" alt="question2" data-base62-sha1="2KnJ0kO4nHo3avXsNxkNDNeoU8g" width="616" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/1342954fdf57b467b3f507f6cab1c51d5fe2c820_2_616x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/1342954fdf57b467b3f507f6cab1c51d5fe2c820.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/1342954fdf57b467b3f507f6cab1c51d5fe2c820.png 2x" data-dominant-color="E8E1E2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">question2</span><span class="informations">913×740 44 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2019-06-18 15:02 UTC)

<p>All choices that the user makes on the GUI are saved in the <a href="https://github.com/SlicerIGT/SlicerIGT/blob/master/FiducialRegistrationWizard/MRML/vtkMRMLFiducialRegistrationWizardNode.h" rel="nofollow noopener">fiducial registration wizard parameter node</a> that you select at the top (by default, its name is “FiducialRegistrationWizard”). You can also change these selections form Python by modifying the node, for example, you can switch to similarity mode and change “Place ‘To’” transform like this:</p>
<pre><code class="lang-auto">w=getNode('FiducialRegistrationWizard')
w.SetRegistrationModeToSimilarity()
w.SetProbeTransformToNodeId(somTransform.GetID())
</code></pre>

---

## Post #3 by @zapaishchykova (2019-06-18 15:47 UTC)

<p>Dear Andras,<br>
Thanks for your suggestion!<br>
But, I can make this work after I select FiducialRegistrationWizard in UI, but directly from “clean start” in python script I get <code>NameError: global name 'getNode' is not defined</code></p>

---

## Post #4 by @lassoan (2019-06-18 16:16 UTC)

<p>To access <code>getNode</code> from a module, you would need to import the function into the namespace or write <code>slicer.util.getNode</code>. However, <code>getNode</code> is only intended for testing and quick interaction using the Python console.</p>
<p>In a Slicer module, you usually ask the user to choose input nodes (using a `qMRMLNodeComboBox’) and/or create nodes that you need. See <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Tutorials_for_software_developers" rel="nofollow noopener">programming tutorials</a> (in particular, PerkLab tutorials) to get familiar with some of the important concepts.</p>

---

## Post #5 by @zapaishchykova (2019-06-18 20:27 UTC)

<p>What i’m trying to do in a script is:</p>
<pre><code>w = slicer.vtkMRMLFiducialRegistrationWizardNode()
w.SetRegistrationModeToSimilarity()
w.SetProbeTransformToNodeId(transformNode.GetID())
</code></pre>
<p>But weirdly it does only work from the console, not from the module itself. What am I doing wrong? (also it returns different id for w and for p)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/741d59bd4eb49e6b2984f673872e759ca1a03a24.png" data-download-href="/uploads/short-url/gzcgJcIjIUzJm6M7j99qYbHP15O.png?dl=1" title="question" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/741d59bd4eb49e6b2984f673872e759ca1a03a24.png" alt="question" data-base62-sha1="gzcgJcIjIUzJm6M7j99qYbHP15O" width="690" height="188" data-dominant-color="F6F3F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">question</span><span class="informations">1147×313 17.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @lassoan (2019-06-18 21:05 UTC)

<p>You need to add the created node to the scene.<br>
The node that you created was not known to the scene. The node that you later retrieved successfully was the one created by the fiducial registration wizard module (if you open the module GUI and no parameter node has been created yet, then the module GUI creates one for the user’s convenience).</p>
<p>I would recommend to use <code>slicer.mrmlScene.AddNewNodeByClass()</code>. This method creates a new node (that respects any default node properties set in the scene), it adds the created node to the scene, and passes the ownership of the new node to the scene (so that you don’t need to manually UnRegister the created node).</p>

---

## Post #7 by @zapaishchykova (2019-06-18 22:21 UTC)

<p>I just don’t get it - when I create nodes like you suggested they are not automatically selected on the UI, I mean they exist in the drop down but i couldn’t find anywhere method to select from the dropdown. Also, it still doesn’t change\add my fiducials using transforms:</p>
<pre><code>    fidReg = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLFiducialRegistrationWizardNode", "Fiducial")
    toFids = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsFiducialNode", "ProbeF")
    imageToProbe = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLinearTransformNode", "ImageToProbe")

    fidReg.SetRegistrationModeToSimilarity()
    fidReg.SetProbeTransformToNodeId(imageToProbe.GetID())</code></pre>

---

## Post #8 by @lassoan (2019-06-18 22:39 UTC)

<p>You can use the fiducial registration wizard module GUI for testing and troubleshooting, but it should not be necessary to select a specific node in the node selector fiducial registration, because the user will use <em>your</em> module’s GUI (that shows all the controls he needs and only those).</p>
<p>Can you explain what is the end goal that you would like to achieve?</p>

---

## Post #9 by @zapaishchykova (2019-06-18 23:15 UTC)

<p>In general I’m trying to simplify a calibration for US probe, but more specific - user needs to jump between several modules a lot of times. For this, I extracted buttons from Fiducial registration wizard and placed them on the my new module canvas. I want to avoid user interaction with all these extra settings from fiducial wizard module. For example, generate automatically all “To” points after user had specifies all “From”. I don’t want to show to users all possible options from Fiducial GUI and restrict it as much as possible. That’s why I want to select from the created nodes</p>

---

## Post #10 by @lassoan (2019-06-19 00:06 UTC)

<p>That’s great. I think we’ve planned to implement such a module but did not end up doing it (<a class="mention" href="/u/ungi">@ungi</a> can you confirm?).</p>
<p>It seems that you are on a good path. You create a vtkMRMLFiducialRegistrationWizardNode from your module and add the minimum necessary buttons to your module GUI. All algorithms (add a fiducial point based on a transform, compute registration, etc.) are implemented in the <a href="https://github.com/SlicerIGT/SlicerIGT/blob/master/FiducialRegistrationWizard/Logic/vtkSlicerFiducialRegistrationWizardLogic.h" rel="nofollow noopener">fiducial registration wizard module logic</a> (accessible as <code>slicer.modules.fiducialregistrationwizard.logic()</code>). For example, you can add fiducials or compute registration result by calling logic methods. You module or your users will not use fiducial registration wizard module widget (GUI) at all.</p>

---

## Post #11 by @ungi (2019-06-19 06:15 UTC)

<p>Correct. We were thinking about a simple ultrasound calibration module. But nobody implemented it yet. Ultrasound calibration is not needed very often. And those users who need a simple GUI (doctors) should probably use a different calibration method, like the one with N-shaped wires. So, there was never a very strong reason to implement a simplified module.</p>

---

## Post #12 by @zapaishchykova (2019-06-19 08:27 UTC)

<p>Thank you, Andras!<br>
But I really looked into module logic and i could not find there a method to compute the transformations or for the change of transform type. This function names are just not self-explanatory to me. I added buttons for user to set up From by mouse clicks:</p>
<pre><code>imageF = slicer.qSlicerMarkupsPlaceWidget()
imageF.setMRMLScene(slicer.mrmlScene)
markupsNodeID = slicer.modules.markups.logic().AddNewFiducialNode('ImageF')
imageF.setCurrentNode(slicer.mrmlScene.GetNodeByID(markupsNodeID))
imageF.placeButton().show()
imageF.show()
fiducialFormLayout.addWidget(imageF)
</code></pre>
<p>Next, after all points are selected on the sequence, i want to place fiducials using transform, but it does not work from the python script, only works from the console:</p>
<pre><code>    fidReg = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLFiducialRegistrationWizardNode", "Fiducial")
    toFids = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsFiducialNode", "ProbeF")
    imageToProbe = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLinearTransformNode", "ImageToProbe")

    fidReg.SetRegistrationModeToSimilarity()
    fidReg.SetProbeTransformToNodeId(imageToProbe.GetID())
</code></pre>
<p>What i’m missing here?</p>

---

## Post #13 by @lassoan (2019-06-19 16:40 UTC)

<p>All computation parameters are stored in the fiducial registration wizard node, so you can set registration mode, etc. there. Logic functions are only needed for actions: computing transformation (using <code>UpdateCalibration</code>, if auto-update is disabled) and adding fiducials (<code>AddFiducial</code>).</p>
<aside class="quote no-group" data-username="zapaishchykova" data-post="12" data-topic="7217">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/zapaishchykova/48/66121_2.png" class="avatar"> zapaishchykova:</div>
<blockquote>
<p>i want to place fiducials using transform</p>
</blockquote>
</aside>
<p>See how to add fiducial using the module logic <a href="https://github.com/SlicerIGT/SlicerIGT/blob/6c0ee5cc173fbb26b26236d7be11e6c052cfe654/FiducialRegistrationWizard/qSlicerFiducialRegistrationWizardModuleWidget.cxx#L87-L103">here</a>.</p>
<aside class="quote no-group" data-username="zapaishchykova" data-post="12" data-topic="7217">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/zapaishchykova/48/66121_2.png" class="avatar"> zapaishchykova:</div>
<blockquote>
<p>i could not find there a method to compute the transformations</p>
</blockquote>
</aside>
<p>See how to compute the registration transform <a href="https://github.com/SlicerIGT/SlicerIGT/blob/6c0ee5cc173fbb26b26236d7be11e6c052cfe654/FiducialRegistrationWizard/qSlicerFiducialRegistrationWizardModuleWidget.cxx#L106-L116">here</a>.</p>

---

## Post #14 by @zapaishchykova (2019-06-19 17:46 UTC)

<p>I don’t have attribute slicer.qSlicerFiducialRegistrationWizardModuleWidget() to access all the logic,<br>
neither methods that you linked in github are not accesible from slicer.modules.fiducialregistrationwizard.logic()</p>

---

## Post #15 by @lassoan (2019-06-19 23:37 UTC)

<p>You don’t need to access the GUI. That is only for the user and the fiducial registration wizard module.</p>
<p>I’ve just checked on Slicer-4.10.2 and both <code>AddFdiucial</code> and <code>UpdateCalibration</code> methods of the logic object are available from Python. Did you get an error message when you tried to use them?</p>

---

## Post #16 by @zapaishchykova (2019-06-20 11:50 UTC)

<p>But you provided <a href="https://github.com/SlicerIGT/SlicerIGT/blob/6c0ee5cc173fbb26b26236d7be11e6c052cfe654/FiducialRegistrationWizard/qSlicerFiducialRegistrationWizardModuleWidget.cxx#L87-L103" rel="nofollow noopener">this</a> link as an example how to add transformed fiducial using the module logic. So I want still user to add  “From” fiducials, but avoid the user to select the transformation and place fiducials “To” using transforms via code. I don’t see how <code>AddFdiucial</code>  and  <code>UpdateCalibration</code>  methods can help me here, for this i need to access logic from qSlicerFiducialRegistrationWizardModuleWidget.</p>

---

## Post #17 by @lassoan (2019-06-20 12:33 UTC)

<aside class="quote no-group" data-username="zapaishchykova" data-post="16" data-topic="7217">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/zapaishchykova/48/66121_2.png" class="avatar"> zapaishchykova:</div>
<blockquote>
<p>But you provided <a href="https://github.com/SlicerIGT/SlicerIGT/blob/6c0ee5cc173fbb26b26236d7be11e6c052cfe654/FiducialRegistrationWizard/qSlicerFiducialRegistrationWizardModuleWidget.cxx#L87-L103">this</a> link as an example how to add transformed fiducial using the module logic</p>
</blockquote>
</aside>
<p>It is not necessary to call methods of any other module’s <em>widget</em>. All the features that are meant to be used by other modules are implemented in a module’s <em>logic</em>.</p>
<p>The code snippets that I linked show examples of how to use the logic to add new fiducial from transform. I did not suggest to try and call those widget methods from another module.</p>
<p>You already know the transform and markup fiducial nodes in your module (most probably your module creates them and uses them; but if you want, you may also expose it on your module GU). Therefore, based on the example that I linked, to add a fiducial you just need to call this logic method:</p>
<pre><code>slicer.modules.fiducialregistrationwizard.logic().AddFiducial(probeToTransformNode, toMarkupsNode)
</code></pre>

---

## Post #18 by @zapaishchykova (2019-06-20 12:50 UTC)

<p>Oh finally i get it!<br>
Thank you so much for your help and patience!</p>

---

## Post #19 by @mholden8 (2019-06-20 13:54 UTC)

<p>A while ago I played around with making a simple interface for ultrasound calibration in Slicer using the pointer-based method: <a href="https://github.com/mholden8/UltrasoundCalibrationWizard/tree/master/PointerBasedUSCalibration" rel="nofollow noopener">https://github.com/mholden8/UltrasoundCalibrationWizard/tree/master/PointerBasedUSCalibration</a>. <a class="mention" href="/u/zapaishchykova">@zapaishchykova</a> you may consider using it as a starting point, but I cannot recall how well it works…</p>

---
