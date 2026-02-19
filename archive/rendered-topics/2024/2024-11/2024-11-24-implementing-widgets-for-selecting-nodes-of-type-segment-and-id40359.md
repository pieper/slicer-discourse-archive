---
topic_id: 40359
title: "Implementing Widgets For Selecting Nodes Of Type Segment And"
date: 2024-11-24
url: https://discourse.slicer.org/t/40359
---

# Implementing Widgets for Selecting Nodes of Type Segment and Beam

**Topic ID**: 40359
**Date**: 2024-11-24
**URL**: https://discourse.slicer.org/t/implementing-widgets-for-selecting-nodes-of-type-segment-and-beam/40359

---

## Post #1 by @shahrokh (2024-11-24 17:02 UTC)

<p>Hello Dear Developers and Users,</p>
<p>My question is probably very basic, so I would appreciate your guidance Or guide me on which tutorial I should refer to in order to implement functions for widgets that select nodes of different types, such as Beam, Segment, Volume, or Model.</p>
<p>I want to develop a module containing a widget for selecting one of the Beam nodes under the <strong>RTPlan</strong> node and a widget for selecting one of the Segment nodes under the <strong>Segmentation</strong> node. To do this, I created an Extension called <strong>moduleRTPlan</strong> in the <em>Extension Wizard</em>. Then, I added a module named <strong>BeamTry01</strong> to <strong>moduleRTPlan</strong>. Next, I switched to the <em>BeamTry01</em> module in the <em>Example</em> Category. At this stage, I clicked on <strong>Edit UI</strong> to enter the <strong>Qt Designer</strong> environment and removed all the default widgets that were created. Now, I have two questions:</p>
<ol>
<li>
<p>From the <strong>Slicer [MRML Widget]</strong> list, which widget is appropriate for a <strong>Beam</strong> node?</p>
</li>
<li>
<p>I understand that to create a widget for selecting one of the <strong>Segments</strong> under the <strong>Segmentation</strong> node, I should use a widget named <strong>qMRMLSegmentSelectorWidget</strong>.</p>
</li>
</ol>
<p>In the following figure, you can see that I used <strong>qMRMLSegmentSelectorWidget</strong> to select a Segment from the Segmentation node. To select a Beam from the available list for the RTPlan node, I used the <strong>ctkCollapsibleButton</strong> widget. However, unfortunately, the Segment selection widget is completely inactive, and the Beam selection widget does not show any Beams.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7fa520c8c27cc3febeeaf78e89d3e1e6cb49e271.png" data-download-href="/uploads/short-url/idcqhOXd7WyOnyfn2fogywLPLwt.png?dl=1" title="Picture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7fa520c8c27cc3febeeaf78e89d3e1e6cb49e271_2_690x388.png" alt="Picture" data-base62-sha1="idcqhOXd7WyOnyfn2fogywLPLwt" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7fa520c8c27cc3febeeaf78e89d3e1e6cb49e271_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7fa520c8c27cc3febeeaf78e89d3e1e6cb49e271_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7fa520c8c27cc3febeeaf78e89d3e1e6cb49e271.png 2x" data-dominant-color="C4C5C3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Picture</span><span class="informations">1280×720 179 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Please guide me.</p>
<p>Best regards.<br>
Shahrokh</p>

---

## Post #2 by @Mik (2024-11-30 12:16 UTC)

<p>If you are creating a new module, your main module widget should be derived from <code>qSlicerModule</code>.</p>
<p>Then you must connect signal <code>mrmlSceneChanged(vtkMRMLScene*)</code> from your module widget to the slot <code>setMRMLScene(vtkMRMLScene*)</code> of widgets where you want to choose a node or a segment of ROI (see <code>Signal/Slot editor</code> in Qt Designer).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac903ef143794c13be3ce5a370ab6aae25e9f7dd.png" data-download-href="/uploads/short-url/oCzayva5Z6dVyBOMjAchMFqsTsp.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac903ef143794c13be3ce5a370ab6aae25e9f7dd_2_690x376.png" alt="image" data-base62-sha1="oCzayva5Z6dVyBOMjAchMFqsTsp" width="690" height="376" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac903ef143794c13be3ce5a370ab6aae25e9f7dd_2_690x376.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac903ef143794c13be3ce5a370ab6aae25e9f7dd_2_1035x564.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac903ef143794c13be3ce5a370ab6aae25e9f7dd_2_1380x752.png 2x" data-dominant-color="E7E9E5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1047 319 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You can check ui files using Qt designer for example in the <code>ExternalBeamPlanning</code> module (<a href="https://github.com/SlicerRt/SlicerRT/blob/master/ExternalBeamPlanning/Resources/UI/qSlicerExternalBeamPlanningModule.ui" rel="noopener nofollow ugc">/Resourses/UI/qSlicerExternalBeamPlanning.ui</a>).</p>
<p>For qMRMLNodeComboBox widgets you should set a required types of nodes (vtkMRMLRTPlanNode or vtkMRMLRTBeamNode) you want to choose from.</p>

---

## Post #3 by @shahrokh (2024-12-01 06:51 UTC)

<p>Dear Mikhail Polkovnikov,</p>
<p>Thank you very much for your guidance. As mentioned in my issue titled <a href="https://discourse.slicer.org/t/understanding-ui-editing-and-python-file-generation-in-3dslicer-with-qt-designer/40369/5">Understanding UI Editing and Python File Generation in 3DSlicer with Qt Designer - Development - 3D Slicer Community</a>, the roadmap I have set for myself is to familiarize with the implementation of the components of the widgets that I need to use in my module. Then, I should connect these components together in the way you suggested. Completing these steps is time-consuming for me, but I will do my best to complete them.<br>
Best regards.<br>
Shahrokh</p>

---
