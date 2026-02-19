---
topic_id: 24150
title: "Jupyter Notebook"
date: 2022-07-01
url: https://discourse.slicer.org/t/24150
---

# Jupyter notebook

**Topic ID**: 24150
**Date**: 2022-07-01
**URL**: https://discourse.slicer.org/t/jupyter-notebook/24150

---

## Post #1 by @Isabella_Romero (2022-07-01 19:26 UTC)

<p>I am using Jupyter notebook to manage 3D slicer.<br>
I am trying to control 3D slicer using python commands to automate the use of one Module.<br>
I want to edit the buttons of the module so that I can insert the data from Jupyter. For example, when it says insert Input volume, instead of using the 3D slicer GUI, use python commands.<br>
Can anyone help me with this, thank you!!</p>

---

## Post #2 by @lassoan (2022-07-03 03:18 UTC)

<p>I would recommend to start with the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials">Scripting and module development tutorial</a> and then check out the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html">Python FAQ</a> for information on how to use CLI and Loadable modules from Python scripting. You can also find many examples in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html">script repository</a> and in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/index.html">modules section of the developer manual</a> and in Python-scripted module tests. Since all these documentations are indexed by search engines, you can also google any question that you have. If you don’t find answers to any specific question (e.g., how to access a certain feature of certain module from a Python script) then you can ask it here.</p>

---

## Post #3 by @Isabella_Romero (2022-07-13 07:18 UTC)

<p>Thank you for your answer Andras, I am going to check all the provided information</p>

---

## Post #4 by @Isabella_Romero (2022-07-14 07:18 UTC)

<p>Hi. I couldnt find the solution to my problem.<br>
I am going to explain it better. I am using the a module and I want to automate the process.<br>
For example, in this box I need to choose “Create new volume”. Do you know if there is any python code I can write instead of having to click it with the mouse.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a793808885e1c2f753cdedff134b7c41356bddfa.png" data-download-href="/uploads/short-url/nUrL4Po3XzfgcpPQGLWNSC1pHEm.png?dl=1" title="Captura de pantalla 2022-07-14 a las 9.18.15" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a793808885e1c2f753cdedff134b7c41356bddfa_2_690x142.png" alt="Captura de pantalla 2022-07-14 a las 9.18.15" data-base62-sha1="nUrL4Po3XzfgcpPQGLWNSC1pHEm" width="690" height="142" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a793808885e1c2f753cdedff134b7c41356bddfa_2_690x142.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a793808885e1c2f753cdedff134b7c41356bddfa.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a793808885e1c2f753cdedff134b7c41356bddfa.png 2x" data-dominant-color="C6D2E2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla 2022-07-14 a las 9.18.15</span><span class="informations">1006×208 33.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @rbumm (2022-07-15 17:47 UTC)

<p>If the YourExtension you want to automate has a YourExtensionLogic(ScriptedLoadableModuleLogic) class then you would need to find the settable parameters in that class.</p>
<p>Example: This code sets some necessary things in the LungCTAnalyzer extension logic from a Python script.</p>
<pre><code class="lang-auto">import LungCTAnalyzer

from LungCTAnalyzer import LungCTAnalyzerTest
from LungCTAnalyzer import LungCTAnalyzerLogic

logic = LungCTAnalyzerLogic()

# loadedVolumeNode and loadedMaskNode were created before
logic.inputVolume = loadedVolumeNode
logic.inputSegmentation = loadedMaskNode

logic.rightLungMaskSegmentID = loadedMaskNode.GetSegmentation().GetSegmentIdBySegmentName("right lung")
logic.leftLungMaskSegmentID = loadedMaskNode.GetSegmentation().GetSegmentIdBySegmentName("left lung")
logic.setDefaultThresholds(-1050,-990,-650,-400,0,3000)
            
logic.detailedSubsegments = True
logic.shrinkMasks = False
logic.countBullae = False
</code></pre>
<p>When ready, you would</p>
<pre><code class="lang-auto">logic.process()
</code></pre>
<p>to do the actual work.</p>

---

## Post #6 by @Isabella_Romero (2022-07-18 11:07 UTC)

<p>Thank you for your answer.</p>
<p>I am trying to use SlicerIGT (SegmentationUnet module) but there is no SlicerIGTLogic class, do you know any other way to achieve this?</p>

---

## Post #7 by @rbumm (2022-07-18 20:16 UTC)

<p>Gee this module is complicated. Could maybe <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> or <a class="mention" href="/u/lassoan">@lassoan</a> provide a starting point for Isabella?</p>

---

## Post #8 by @lassoan (2022-07-18 21:17 UTC)

<aside class="quote no-group" data-username="Isabella_Romero" data-post="6" data-topic="24150">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/isabella_romero/48/15865_2.png" class="avatar"> Isabella_Romero:</div>
<blockquote>
<p>I am trying to use SlicerIGT (SegmentationUnet module) but there is no SlicerIGTLogic class, do you know any other way to achieve this?</p>
</blockquote>
</aside>
<p>SlicerIGT is an extension. There is no logic for an extension but only modules have logic classes. SegmentationUNet module has a logic class - see <a href="https://github.com/SlicerIGT/aigt/blob/5c452a9dac1749768dc484af7f986b43ae91b47e/SlicerExtension/LiveUltrasoundAi/SegmentationUNet/SegmentationUNet.py#L349">here</a>.</p>

---
