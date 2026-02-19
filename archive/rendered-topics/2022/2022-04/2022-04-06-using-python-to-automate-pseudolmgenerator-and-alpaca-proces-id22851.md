---
topic_id: 22851
title: "Using Python To Automate Pseudolmgenerator And Alpaca Proces"
date: 2022-04-06
url: https://discourse.slicer.org/t/22851
---

# Using python to automate pseudoLMGenerator and ALPACA processes

**Topic ID**: 22851
**Date**: 2022-04-06
**URL**: https://discourse.slicer.org/t/using-python-to-automate-pseudolmgenerator-and-alpaca-processes/22851

---

## Post #1 by @Erik.Meilak (2022-04-06 15:41 UTC)

<p>Hello, I am trying to automate some processes which use the modules pseudoLMGenerator and ALPACA but cannot find any of the functions which are available in the GUI.</p>
<p>For example if I try and set the base mesh in the pseudoLMGenerator I expected to find something along the lines of:<br>
slicer.modules.pseudolmgenerator.logic().setBaseMesh() but not such function or anything similar is available after inputting slicer.modules.pseudolmgenerator.logic().</p>
<p>I have similar issues when trying to automate the ALPACA module also. My question is, is it possible to automate all GUI functions through python scripting and if so how do I find the documentation describing the correct syntax for scripting for these particular modules?</p>
<p>Thanks in advance for any help. Happy to provide further details/screenshots if needed.</p>

---

## Post #2 by @smrolfe (2022-04-06 18:08 UTC)

<p>It is possible to automate ALPACA and the pseudoLMGenerator. You will need to read through the module’s code to see how to do this, but in general:</p>
<ul>
<li>parameters such as input files/folders set in the GUI will be defined in the <code>setup()</code> function of the widget class</li>
<li>the widget class contains functions that handle GUI interactions, such as button presses</li>
<li>the logic class contains functions to run the algorithms. The input parameters can be passed directly, without needing to set GUI parameters.</li>
</ul>
<p>For the PseudoLMGenerator module, there are multiple steps run by separate button presses. Looking at the button callbacks, you will find the logic functions called and input/output arguments.</p>
<p>ALPACA can be run in batch mode using a single call to the logic function <a href="https://github.com/SlicerMorph/SlicerMorph/blob/dbd661146ef45b6f8d2f7778f9a4e8b65c28ff9b/ALPACA/ALPACA.py#L854" rel="noopener nofollow ugc">here</a>.</p>
<p>I’m happy to help here with any specific questions. You also might find these <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials" rel="noopener nofollow ugc">tutorials</a> helpful.</p>

---

## Post #3 by @Erik.Meilak (2022-04-11 09:52 UTC)

<aside class="quote no-group" data-username="Erik.Meilak" data-post="1" data-topic="22851">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/e/fbc32d/48.png" class="avatar"> Erik.Meilak:</div>
<blockquote>
<p>slicer.modules.pseudolmgenerator.</p>
</blockquote>
</aside>
<p>Hi Sara, thank you for replying so quickly. I am trying to use the module code ( <a href="https://github.com/SlicerMorph/SlicerMorph/blob/dbd661146ef45b6f8d2f7778f9a4e8b65c28ff9b/PseudoLMGenerator/PseudoLMGenerator.py#L105" class="inline-onebox" rel="noopener nofollow ugc">SlicerMorph/PseudoLMGenerator/PseudoLMGenerator.py at dbd661146ef45b6f8d2f7778f9a4e8b65c28ff9b · SlicerMorph/SlicerMorph · GitHub</a> )<br>
to understand how to programmatically use the pseudoLMGenerator but I’m afraid I’m struggling to get it working.</p>
<p>To define the base mesh I try the following command:<br>
slicer.modules.PseudoLMGeneratorWidget.modelSelector(modelNode)</p>
<p>Where modelNode is a loaded model. However I am met with the following error:<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
TypeError: ‘qMRMLNodeComboBox’ object is not callable</p>
<p>Would you be able to give example code on defining the base model for the pseudoLMGenerator followed by executing the “get subsample number” command? Many thanks for your help!</p>

---

## Post #4 by @smrolfe (2022-04-15 17:15 UTC)

<p>You won’t need to set the widget elements, like the <code>modelSelector</code> to automate this module. The steps you will need are in the button callback functions.</p>
<p>I can help you with a code snippet, but first can you give me an idea of what you are trying to do? In a typical workflow, pseudo-landmarks are placed only once on an atlas model and transferred to other specimens using <code>ALPACA</code> or <code>projectSemiLM</code>. Both of these modules preserve the relationship between the pseudo-landmarks, which running the <code>pseudoLMGenerator</code> multiple times can not do.</p>

---

## Post #5 by @Erik.Meilak (2022-04-20 08:39 UTC)

<p>I am trying to generate pseudo landmarks for a mesh which are then used for input as “Source Landmarks” in the ALPACA registration process. I have managed to do the entire process manually using the GUI but it is automating the process that is eluding me.<br>
You mention button callback functions, where would I find documentation/examples of these functions?</p>

---

## Post #6 by @Erik.Meilak (2022-04-20 10:46 UTC)

<p>To put it another way, would you be able to give example code that is able to execute all the actions demonstrated in the following slicermorph youtube tutorials using the python interface?</p>
<p>PseudoLMGenerator and MarkupEditor tutorial: <a href="https://www.youtube.com/watch?v=yvI65oyxYpA" class="inline-onebox" rel="noopener nofollow ugc">PseudoLMGenerator and MarkupEditor tutorial - YouTube</a><br>
Demo of ALPACA module in SlicerMorph tutorial: <a href="https://www.youtube.com/watch?v=ZRikzsUBeAE" class="inline-onebox" rel="noopener nofollow ugc">Demo of ALPACA module in SlicerMorph - YouTube</a></p>

---
