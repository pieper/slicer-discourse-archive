# "Color Scalar Bar" reworked and upgraded, now it’s called "Color Legend"

**Topic ID**: 21567
**Date**: 2022-01-22
**URL**: https://discourse.slicer.org/t/color-scalar-bar-reworked-and-upgraded-now-it-s-called-color-legend/21567

---

## Post #1 by @Mik (2022-01-22 07:56 UTC)

<p>Starting from version <a href="https://github.com/Slicer/Slicer/pull/5828/commits/170a0e0edd448fd2c5d8e47ac6de591293fc8354" rel="noopener nofollow ugc">30530 build 2022-01-15</a> “Color Scalar Bar” section from “Colors” module was replaced with “Color Legend” section.</p>
<p>The “Color Legend” section has been also added to the “Volume”, “Model” and “Markups” modules to control visibility and behavior of color legend.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/6755ea30878f4e57abb5e25ea985518b838bea3e.jpeg" data-download-href="/uploads/short-url/eK9fz7FnRdhsnN7COOaH5Wc2NCm.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6755ea30878f4e57abb5e25ea985518b838bea3e_2_690x376.jpeg" alt="image" data-base62-sha1="eK9fz7FnRdhsnN7COOaH5Wc2NCm" width="690" height="376" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6755ea30878f4e57abb5e25ea985518b838bea3e_2_690x376.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6755ea30878f4e57abb5e25ea985518b838bea3e_2_1035x564.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6755ea30878f4e57abb5e25ea985518b838bea3e_2_1380x752.jpeg 2x" data-dominant-color="747574"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1047 132 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>New major features:</p>
<ol>
<li>
<p>More unified API. Each Volume, Model, Markups or any other displayable node now can have an individual color legend by means of <a href="https://apidocs.slicer.org/master/classvtkMRMLColorLegendDisplayNode.html" rel="noopener nofollow ugc">vtkMRMLColorLegendDisplayNode</a>.</p>
</li>
<li>
<p>Displayed LUT is in sync with range of displayed values of primary display node;</p>
</li>
<li>
<p>Resizable title of color legend;</p>
</li>
<li>
<p>Control of visibility of color legend on each slice or 3D view.</p>
</li>
<li>
<p>Color legend can by added to any displayable node (if the node has a primary display node) by means of <a href="http://apidocs.slicer.org/master/classvtkSlicerColorLogic.html#ab3c6cd1c528e5c826dba15826043a4ea" rel="noopener nofollow ugc">Color module logic</a> and AddDefaultColorLegendDisplayNode method.</p>
</li>
<li>
<p>The access to a low level <a href="https://vtk.org/doc/nightly/html/classvtkScalarBarActor.html" rel="noopener nofollow ugc">vtkScalarBarActor</a> for developers and experienced users is described <a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/colors.html#access-scalar-bar-actor" rel="noopener nofollow ugc">here</a>.</p>
</li>
</ol>
<p>There are still some features that must be added. <a href="https://github.com/Slicer/Slicer/issues/6111" rel="noopener nofollow ugc">Issue</a> to check the progress is here.</p>
<p>Any other required or recommended features can added to the issue or in this topic.</p>

---

## Post #2 by @lassoan (2022-01-28 04:48 UTC)

<p><a class="mention" href="/u/mik">@Mik</a> Thank you very much! This feature was missing for a very long time and it will make an impact in many projects.</p>

---

## Post #3 by @park (2022-09-26 02:27 UTC)

<p>Hi Mik</p>
<p>Thank you for your development about color scalar bar</p>
<p>I try to plot the scalar bar on “View1” (i.e., 3D view).<br>
“View1” was selected in the View panel, but the color bar is not displayed in the 3D view as shown in the example above.</p>
<p>Is there a way to solve this problem ?</p>
<p>Best,</p>

---

## Post #4 by @Mik (2022-09-26 09:48 UTC)

<p>For what data are you trying to display color legend in 3D: scalar volume, model or something else? Currently there is a limitation of showing color legends in 3D.</p>

---

## Post #5 by @park (2022-09-26 09:56 UTC)

<p>It is scalar volume.</p>
<p>I made a volume rendering plot using scientific data (as colormap)<br>
And I would like to make color legend of this volume rendering</p>
<p>As far as I search, the color legend in 3D look likt only for model. Is it right?</p>

---

## Post #6 by @Mik (2022-09-26 10:12 UTC)

<p>Correct. Color legend can be shown in 3D for models.</p>

---

## Post #7 by @lassoan (2022-09-26 21:24 UTC)

<p><a class="mention" href="/u/mik">@Mik</a> submitted a <a href="https://github.com/Slicer/Slicer/pull/6550">pull request</a> that will allow displaying color legend of volumes shown slice views to be shown in 3D views as well. It’ll be available in the Slicer Preview Release within a few days.</p>
<aside class="quote no-group" data-username="park" data-post="5" data-topic="21567">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/park/48/5717_2.png" class="avatar"> park:</div>
<blockquote>
<p>I made a volume rendering plot using scientific data (as colormap)<br>
And I would like to make color legend of this volume rendering</p>
</blockquote>
</aside>
<p>If you enable “Synchronize with Volumes module” in Volume rendering module’s Advanced / Volume Properties section then the same color legend applies to volume rendering and slice views. However, if you use any other volume rendering preset then there is no GUI for making the volume rendering’s Scalar Color Mapping appear as a color legend, but you can achieve it by copy-pasting this Python script into the Python console in Slicer:</p>
<pre data-code-wrap="python"><code class="lang-python"># Get colormap from first volume rendering property node
colorMapOfVolumeRendering = getNode('*Prop*').GetColor()

# Add color node
colorNode = slicer.mrmlScene.CreateNodeByClass("vtkMRMLProceduralColorNode")
colorNode.UnRegister(None)  # to prevent memory leaks
colorNode.SetHideFromEditors(False)
slicer.mrmlScene.AddNode(colorNode)
colorMap = colorNode.GetColorTransferFunction()
colorMap.DeepCopy(colorMapOfVolumeRendering)

# Add an empty displayable node (you can only show a color legend if it belongs to a displayable node)
displayableNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLModelNode", "volume")
displayableNode.CreateDefaultDisplayNodes()
displayNode = displayableNode.GetDisplayNode()

# Display color legend
displayNode.SetAndObserveColorNodeID(colorNode.GetID())
colorLegendDisplayNode = slicer.modules.colors.logic().AddDefaultColorLegendDisplayNode(displayableNode)
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/6407fb82f616726b2d8abcc36f9bdb93f4300925.jpeg" data-download-href="/uploads/short-url/egUQF6d1BeWcIOiNWiQ7y6vCDzf.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/6407fb82f616726b2d8abcc36f9bdb93f4300925.jpeg" alt="image" data-base62-sha1="egUQF6d1BeWcIOiNWiQ7y6vCDzf" width="690" height="343" data-dominant-color="8B7C8E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">708×352 91 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><a class="mention" href="/u/mik">@mik</a> if you have time you might consider adding display of color legend for volume rendering (but instead of creating a separate color node, take the colormap from the volume property node). However, I’m not sure how often users want to display color legend for volume rendering.</p>

---

## Post #8 by @Mik (2022-10-05 15:14 UTC)

<p>The color legend for volume rendering should be displayed only in 3D?</p>

---

## Post #9 by @JulianEG (2026-01-26 19:24 UTC)

<p><a class="mention" href="/u/mik">@Mik</a> I am having an issue with a module that used the old VTKScaleBar, I was wondering if you could help me to update it to Color Legend. The module is BoneThicknessMapping (version f98136b 22.02.2023).</p>
<p>When I try to run it, the phython console shows the following:</p>
<p>Traceback (most recent call last):</p>
<p>File “C:/Users/Asus/AppData/Local/NA-MIC/Slicer 5.2.2/NA-MIC/Extensions-31382/BoneThicknessMapping/lib/Slicer-5.2/qt-scripted-modules/BoneThicknessMapping.py”, line 521, in click_execute</p>
<p>BoneThicknessMappingLogic.set_scalar_colour_bar_state(0)</p>
<p>File “C:/Users/Asus/AppData/Local/NA-MIC/Slicer 5.2.2/NA-MIC/Extensions-31382/BoneThicknessMapping/lib/Slicer-5.2/qt-scripted-modules/BoneThicknessMapping.py”, line 936, in set_scalar_colour_bar_state</p>
<p>ctkBar = slicer.util.findChildren(colorWidget, name=‘VTKScalarBar’)[0]</p>
<p>IndexError: list index out of range</p>
<p>[Qt] This function is deprecated. Use lookFromAxis(const ctkAxesWidget::Axis&amp; axis) instead.</p>
<p>The section of code referenced is this (starting from line 933):</p>
<pre><code class="lang-auto">@staticmethod
def set_scalar_colour_bar_state(state, color_node_id=None):
    colorWidget = slicer.modules.colors.widgetRepresentation()
    ctkBar = slicer.util.findChildren(colorWidget, name='VTKScalarBar')[0]
    ctkBar.setDisplay(state)
    if state == 0 or color_node_id is None: return
    slicer.util.findChildren(colorWidget, 'ColorTableComboBox')[0].setCurrentNodeID(color_node_id)
    slicer.util.findChildren(colorWidget, 'UseColorNameAsLabelCheckBox')[0].setChecked(True)
</code></pre>
<p>And it is called upon in other sections such as this (lines 581 and 582):</p>
<pre><code class="lang-auto">    # update scalar bar
    BoneThicknessMappingLogic.set_scalar_colour_bar_state(1, colourNodeId)
</code></pre>
<p>Hope you can help and thank you for your time regardless!</p>

---

## Post #10 by @Mik (2026-01-29 04:00 UTC)

<p>Is this module BoneThicknessMapping compile and run without problems? I mean i hope it isn’t abandoned.</p>
<p>You just want to show color legend for a model node or volume, or you want a properly working button within the module?</p>

---

## Post #11 by @Mik (2026-01-29 09:00 UTC)

<p>One more question. Do you need color legend for calculated model node or for the input volume node as well?</p>

---

## Post #12 by @Mik (2026-01-29 10:36 UTC)

<p>I have made a <a href="https://github.com/Auditory-Biophysics-Lab/Slicer-BoneThicknessMapping/pull/8" rel="noopener nofollow ugc">PR</a> to upgrade that module. Can you download and check that this upgrade is that what you need.</p>

---

## Post #13 by @JulianEG (2026-01-29 17:42 UTC)

<p>Thank you for all your help. I ran the module with the modifications but it doesn’t seem to work. What I get on the console is the following:</p>
<hr>
<p>Traceback (most recent call last):</p>
<p>File “C:/Users/Asus/AppData/Local/NA-MIC/Slicer 5.2.2/NA-MIC/Extensions-31382/BoneThicknessMapping/lib/Slicer-5.2/qt-scripted-modules/BoneThicknessMapping.py”, line 521, in click_execute</p>
<p># BoneThicknessMappingLogic.set_scalar_colour_bar_state(0)</p>
<p>File “C:/Users/Asus/AppData/Local/NA-MIC/Slicer 5.2.2/NA-MIC/Extensions-31382/BoneThicknessMapping/lib/Slicer-5.2/qt-scripted-modules/BoneThicknessMapping.py”, line 936, in set_scalar_colour_bar_state</p>
<p>colorLegendNode = slicer.modules.colors.logic().GetColorLegendDisplayNode(displayable_node)</p>
<p>IndexError: list index out of range</p>
<p>[Qt] This function is deprecated. Use lookFromAxis(const ctkAxesWidget::Axis&amp; axis) instead.</p>
<hr>
<p>The IndexError persists, which makes me think that the issue is not due to the change from VTKScalarBar to ColorLegend but lies somewhere else.</p>
<p>This results in the progress bar when using the module not moving from 0% (status:initializing execution). The issue is the same as described on this post <a href="https://discourse.slicer.org/t/bonethicknessmapping-does-not-work/30738" class="inline-onebox">BoneThicknessMapping does not work</a> . This other post seems to describe the same problem and according to them it worked properly in 3dslicer 4.1.1 <a href="https://discourse.slicer.org/t/bone-thickness-mapping-not-functioning/29453" class="inline-onebox">Bone Thickness Mapping not functioning</a> .</p>
<p>Thank you anyway for your help and time.</p>

---

## Post #14 by @Mik (2026-01-29 18:04 UTC)

<p>I’m working with Slicer-5.9. Can you check that update with a newer Slicer version rather then 5.2?</p>

---

## Post #15 by @JulianEG (2026-01-29 19:13 UTC)

<p>It does work now! In 3D Slicer version 5.10 and using your upgrade script. Thanks a lot!</p>

---

## Post #16 by @Mik (2026-01-30 05:19 UTC)

<p>If there are bugs in new color legend with displayed color table, let me know.</p>

---
