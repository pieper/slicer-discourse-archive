---
topic_id: 789
title: "Capturing Mouse Input"
date: 2017-07-31
url: https://discourse.slicer.org/t/789
---

# Capturing Mouse Input

**Topic ID**: 789
**Date**: 2017-07-31
**URL**: https://discourse.slicer.org/t/capturing-mouse-input/789

---

## Post #1 by @moselhy (2017-07-31 06:01 UTC)

<p>Hello,</p>
<p>I would like to ask the user to input coordinates by clicking on a point in the volume. How do I achieve this?</p>
<p>I guess I would prompt them using a QMessageBox, but I would also like to change the pointer to something like this <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b22248c9ecc5b4fc6d8a0f526bfc9b9ceed69d2.jpeg" data-download-href="/uploads/short-url/fhKeS7LowiyRf45QritjYa6JcXw.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/6b22248c9ecc5b4fc6d8a0f526bfc9b9ceed69d2_2_32x26.jpg" alt="image" data-base62-sha1="fhKeS7LowiyRf45QritjYa6JcXw" width="32" height="26" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/6b22248c9ecc5b4fc6d8a0f526bfc9b9ceed69d2_2_32x26.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/6b22248c9ecc5b4fc6d8a0f526bfc9b9ceed69d2_2_48x39.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/6b22248c9ecc5b4fc6d8a0f526bfc9b9ceed69d2_2_64x52.jpg 2x" data-dominant-color="E4E4E4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1280×1024 29 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> and actually await the input…</p>
<p>Thanks</p>

---

## Post #2 by @Davide_Punzo (2017-07-31 09:28 UTC)

<p>Hi Mohamed,</p>
<p>you may try to do a segment editor effect. For example, you can take a look at the user-interactions available in the paint effect (works both in 2d and 3d: takes the input coordinates for left-click events) and create your own:<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/EditorEffects/qSlicerSegmentEditorPaintEffect.h" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/EditorEffects/qSlicerSegmentEditorPaintEffect.h" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/EditorEffects/qSlicerSegmentEditorPaintEffect.h</a></h4>
<pre><code class="lang-h">/*==============================================================================

  Copyright (c) Laboratory for Percutaneous Surgery (PerkLab)
  Queen's University, Kingston, ON, Canada. All Rights Reserved.

  See COPYRIGHT.txt
  or http://www.slicer.org/copyright/copyright.txt for details.

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.

  This file was originally developed by Csaba Pinter, PerkLab, Queen's University
  and was supported through the Applied Cancer Research Unit program of Cancer Care
  Ontario with funds provided by the Ontario Ministry of Health and Long-Term Care

==============================================================================*/

</code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/EditorEffects/qSlicerSegmentEditorPaintEffect.h" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>The editor has an effects factory, so you can register your new editor effect very simply, something like this:<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Punzo/SlicerAstro/blob/master/AstroVolume/qSlicerAstroVolumeModule.cxx#L413" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Punzo/SlicerAstro/blob/master/AstroVolume/qSlicerAstroVolumeModule.cxx#L413" target="_blank" rel="nofollow noopener">Punzo/SlicerAstro/blob/master/AstroVolume/qSlicerAstroVolumeModule.cxx#L413</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="403" style="counter-reset: li-counter 402 ;">
<li>      found = layoutDescription.find(*it);</li>
<li>      }</li>
<li>    }</li>
<li>  layoutNode-&gt;SetLayoutDescription(i, layoutDescription.c_str());</li>
<li>  }</li>
<li>
</li>
<li>
</li>
<li>// unregister RulerDisplayableManager</li>
<li>vtkMRMLThreeDViewDisplayableManagerFactory::GetInstance()-&gt;</li>
<li>  UnRegisterDisplayableManager("vtkMRMLRulerDisplayableManager");</li>
<li class="selected">vtkMRMLSliceViewDisplayableManagerFactory::GetInstance()-&gt;</li>
<li>  UnRegisterDisplayableManager("vtkMRMLRulerDisplayableManager");</li>
<li>
</li>
<li>// register AstroTwoDAxesDisplayableManager</li>
<li>vtkMRMLSliceViewDisplayableManagerFactory::GetInstance()-&gt;</li>
<li>  RegisterDisplayableManager("vtkMRMLAstroTwoDAxesDisplayableManager");</li>
<li>
</li>
<li>// register Astro Editor Effects in the Segmentation Editor</li>
<li>qSlicerSegmentEditorEffectFactory::instance()-&gt;registerEffect(new qSlicerSegmentEditorAstroCloudLassoEffect());</li>
<li>qSlicerSegmentEditorEffectFactory::instance()-&gt;registerEffect(new qSlicerSegmentEditorAstroContoursEffect());</li>
<li>
</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>Cheers,</p>
<p>Davide.</p>

---

## Post #3 by @Nicole_Aucoin (2017-07-31 13:25 UTC)

<p>You can use the Markups module to go into fiducial placement mode, see<br>
the “Adding<br>
Fiducials via Mouse Clicks” section here:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Markups" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Modules/Markups</a></p>
<p>Nicole</p>

---

## Post #4 by @lassoan (2017-07-31 13:55 UTC)

<p>Modules in VMTK extension uses fiducials as seeds. You can check out how add a widget to your module that can create/select fiducials: <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/CenterlineComputation/CenterlineComputation.py#L74-L86">https://github.com/vmtk/SlicerExtension-VMTK/blob/master/CenterlineComputation/CenterlineComputation.py#L74-L86</a></p>
<p>You can tune it to create/select fiducial list by default and only show the place widget with a single button to place widget.</p>
<p>See also these examples:</p>
<ul>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Switching_to_markup_fiducial_placement_mode">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Switching_to_markup_fiducial_placement_mode</a></li>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Manipulating_objects_in_the_slice_viewer">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Manipulating_objects_in_the_slice_viewer</a></li>
</ul>

---

## Post #5 by @moselhy (2017-07-31 21:46 UTC)

<p>When I execute <code>self.promptSeedSelect("background")</code><br>
It is returning <code>[0,0,0]</code>. Is there any way I can force the program to wait for a mouse click when the user clicks ‘Ok’?</p>
<pre><code>  def promptSeedSelect(self, seed):
    c = ctk.ctkMessageBox()
    c.setIcon(qt.QMessageBox.Information)
    c.setText("Click on a point in the %s to select the seed" % seed)
    c.setStandardButtons(qt.QMessageBox.Ok)
    c.setDefaultButton(qt.QMessageBox.Ok)
    answer = c.exec_()
    if answer == qt.QMessageBox.Cancel:
      logging.info("Terminating...")
      self.logic = None
      return

    logging.info("Coords are: " + self.drawFiducial(seed))

  def drawFiducial(self, seed):
    ras = [0.0,0.0,0.0]

    fidNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', seed)
    selectionNode = slicer.mrmlScene.GetNodeByID("vtkMRMLSelectionNodeSingleton")
    selectionNode.SetReferenceActivePlaceNodeID(fidNode.GetID())
    interactionNode = slicer.mrmlScene.GetNodeByID("vtkMRMLInteractionNodeSingleton")
    # For multiple clicks, change this to 1
    placeModePersistence = 0
    interactionNode.SetPlaceModePersistence(placeModePersistence)
    interactionNode.SetCurrentInteractionMode(1)

    fidNode.GetNthFiducialPosition(0, ras)

    return ras</code></pre>

---

## Post #6 by @Nicole_Aucoin (2017-07-31 22:14 UTC)

<p>You need to add an observer on the fiducial list node for the<br>
slicer.vtkMRMLMarkupsNode.MarkupAddedEvent<br>
and then you can get the last fiducial position since it’s then been added.</p>
<p>Nicole</p>

---

## Post #7 by @moselhy (2017-08-04 04:58 UTC)

<p>Thank you. When I did that, the code runs fine but then I couldn’t get it to capture the input a second time if the user chooses to. Here is my full code:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/moselhy/SlicerPhantomSegmenter/blob/master/PhantomSegmenter/PhantomSegmenter.py" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/moselhy/SlicerPhantomSegmenter/blob/master/PhantomSegmenter/PhantomSegmenter.py" target="_blank" rel="nofollow noopener">moselhy/SlicerPhantomSegmenter/blob/master/PhantomSegmenter/PhantomSegmenter.py</a></h4>
<pre><code class="lang-py">import os, sys
import unittest
import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
import logging
import dicom
from dicom.filereader import InvalidDicomError
from DICOMScalarVolumePlugin import DICOMScalarVolumePluginClass
import PythonQt

#
# PhantomSegmenter
#

class PhantomSegmenter(ScriptedLoadableModule):
  """Uses ScriptedLoadableModule base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def __init__(self, parent):
</code></pre>

  This file has been truncated. <a href="https://github.com/moselhy/SlicerPhantomSegmenter/blob/master/PhantomSegmenter/PhantomSegmenter.py" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>To reproduce my problem, select this extension from Slicer’s Extension Wizard, then add a breakpoint to <a href="https://github.com/moselhy/PhantomSegmenter/blob/master/PhantomSegmenter/PhantomSegmenter.py#L265" rel="nofollow noopener">line 265</a> and set a watch with the following:<br>
slicer.mrmlScene.GetNodeByID(“vtkMRMLInteractionNodeSingleton”).GetCurrentInteractionMode()</p>
<p>You’ll see that it shows 1 in the debugger, which we want, but then when it exits the call stack, it spontaneously switches to 2, which does not allow placement of a fiducial.</p>

---

## Post #8 by @lassoan (2017-08-04 05:16 UTC)

<p>To facilitate placement of multiple markups, use <a href="http://apidocs.slicer.org/master/classqSlicerMarkupsPlaceWidget.html#a4832089c5d68137535a8948bfe6d6e7a">qSlicerMarkupsPlaceWidget.setPlaceMultipleMarkups(ForcePlaceMultipleMarkups)</a>.</p>
<p>As I see, you have commented out the markup place widget, while you shouldn’t have, because that widget is exactly what you need (it makes sure that the correct markup list is selected, placement mode is active, and single/multiple markup placement option is selected). Just add this widget to the GUI and modify the place multiple markups mode:</p>
<pre><code>self.seedFiducialsNodeSelector.markupsPlaceWidget().placeMultipleMarkups = slicer.qSlicerMarkupsPlaceWidget.ForcePlaceMultipleMarkups</code></pre>

---

## Post #9 by @moselhy (2017-08-04 21:47 UTC)

<p>Thank you for all your help so far. The reason I commented out the widget is because it would require more manual work from the user. I just want the user to be able to choose whether to add more markups or to stop adding more, using this dialog<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f750be63c45682ab63370bdb31b720696313b3ec.png" alt="image" data-base62-sha1="zhQVwt2TZfaaMXPiP8EcneI61qc" width="263" height="133"></p>
<p>When the user clicks “Add More”, it should create a new fiducial and set an observer to it and show this dialog when the user places a markup, and so on, until the user clicks “Save All”, then it would move to the next step. However, the problem I mentioned above happens when the user clicks “Add More”, and I don’t know why…</p>

---

## Post #10 by @lassoan (2017-08-05 02:39 UTC)

<p>Instead of the “Add more” button, use the place widget, configured to show only a single place button, with single markup place mode. It works reliably, used in many modules.</p>
<pre><code>w = slicer.qSlicerMarkupsPlaceWidget()
w.buttonsVisible = False
w.placeButton().show()
w.setMRMLScene(slicer.mrmlScene)
w.setCurrentNode(getNode('F'))
w.placeMultipleMarkups = slicer.qSlicerMarkupsPlaceWidget.ForcePlaceSingleMarkup
w.show()
</code></pre>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c84741f028d6ecea5299cc0c9825333455533e06.png" alt="image" data-base62-sha1="szKa5xnW9AAmd5f9ozpp7mGn6v4" width="233" height="134"></p>

---
