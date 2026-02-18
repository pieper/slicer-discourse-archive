# Sound feedback navigation

**Topic ID**: 690
**Date**: 2017-07-14
**URL**: https://discourse.slicer.org/t/sound-feedback-navigation/690

---

## Post #1 by @robmbar (2017-07-14 14:02 UTC)

<p>I’m developing a navigation module and I want to implement some sound feedback during the navigation. I found this video regarding LumpNav module and this is what I intend to implement:</p>
<div class="lazyYT" data-youtube-id="gSz8IHmogMo" data-youtube-title="LumpNav sound navigation" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<p>I tried to look for the python code of this implementation but, in python script of LumpNav and SlicerSoundControl modules, I couldn’t find the python code regarding this sound feedback implementation. Can someone provide the python code to implement this sound feedback?</p>
<p>Thank you!</p>

---

## Post #2 by @ihnorton (2017-07-14 17:10 UTC)

<p>The simplest option is to use the existing BreachWarningNode infrastructure. See initialization here:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/SlicerIGT/LumpNav/blob/master/LumpNav/LumpNav.py#L417-L421" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerIGT/LumpNav/blob/master/LumpNav/LumpNav.py#L417-L421" target="_blank" rel="nofollow noopener">SlicerIGT/LumpNav/blob/master/LumpNav/LumpNav.py#L417-L421</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="417" style="counter-reset: li-counter 416 ;">
<li>self.breachWarningNode.SetPlayWarningSound(True)</li>
<li>self.breachWarningNode.SetWarningColor(1,0,0)</li>
<li>self.breachWarningNode.SetOriginalColor(self.tumorModel_Needle.GetDisplayNode().GetColor())</li>
<li>self.breachWarningNode.SetAndObserveToolTransformNodeId(self.cauteryTipToCautery.GetID())</li>
<li>self.breachWarningNode.SetAndObserveWatchedModelNodeID(self.tumorModel_Needle.GetID())</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>C++ code here:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/SlicerIGT/SlicerIGT/blob/master/BreachWarning/MRML/vtkMRMLBreachWarningNode.cxx" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerIGT/SlicerIGT/blob/master/BreachWarning/MRML/vtkMRMLBreachWarningNode.cxx" target="_blank" rel="nofollow noopener">SlicerIGT/SlicerIGT/blob/master/BreachWarning/MRML/vtkMRMLBreachWarningNode.cxx</a></h4>
<pre><code class="lang-cxx">
// BreachWarning MRML includes
#include "vtkMRMLBreachWarningNode.h"

// Other MRML includes
#include "vtkMRMLAnnotationRulerNode.h"
#include "vtkMRMLDisplayNode.h"
#include "vtkMRMLModelNode.h"
#include "vtkMRMLNode.h"
#include "vtkMRMLTransformNode.h"

// VTK includes
#include &lt;vtkNew.h&gt;
#include &lt;vtkIntArray.h&gt;
#include &lt;vtkCommand.h&gt;

// Other includes
#include &lt;sstream&gt;

// Constants
</code></pre>

  This file has been truncated. <a href="https://github.com/SlicerIGT/SlicerIGT/blob/master/BreachWarning/MRML/vtkMRMLBreachWarningNode.cxx" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>The actual sound is in Qt, a QSound played when the observed vtkMRMLBreachWarningNode <code>WarningSoundPlaying</code> property is true:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/SlicerIGT/SlicerIGT/blob/master/BreachWarning/qSlicerBreachWarningModule.cxx#L164-L188" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerIGT/SlicerIGT/blob/master/BreachWarning/qSlicerBreachWarningModule.cxx#L164-L188" target="_blank" rel="nofollow noopener">SlicerIGT/SlicerIGT/blob/master/BreachWarning/qSlicerBreachWarningModule.cxx#L164-L188</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="164" style="counter-reset: li-counter 163 ;">
<li>}
</li>
<li>
</li>
<li>//------------------------------------------------------------------------------
</li>
<li>void qSlicerBreachWarningModule::updateWarningSound()
</li>
<li>{
</li>
<li>Q_D(qSlicerBreachWarningModule);
</li>
<li>if (d-&gt;WarningSound.isNull())
</li>
<li>{
</li>
<li>  qWarning("Warning sound object is invalid");
</li>
<li>  return;
</li>
<li>}
</li>
<li>if (d-&gt;ObservedLogic==NULL)
</li>
<li>{
</li>
<li>  qWarning("ObservedLogic is invalid");
</li>
<li>  return;
</li>
<li>}
</li>
<li>bool warningSoundShouldPlay = d-&gt;ObservedLogic-&gt;GetWarningSoundPlaying();
</li>
<li>if (warningSoundShouldPlay)
</li>
<li>{
</li>
<li>  d-&gt;WarningSound-&gt;setLoops(1);
</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/SlicerIGT/SlicerIGT/blob/master/BreachWarning/qSlicerBreachWarningModule.cxx#L164-L188" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Hope that helps.</p>

---

## Post #3 by @robmbar (2017-07-14 19:48 UTC)

<p>Thank you for your answer! I am developing my module in Python. I have already looked to BreachWarning module but it only plays the beep sound when the tip touches the model. I am looking for an approach like is shown in video that adjusts the frequency of beep sound according to the distance to the model.</p>

---

## Post #4 by @lassoan (2017-07-14 20:07 UTC)

<p>To create the demo, I’ve added a few lines of Python code to LumpNav to create a transform based on the distance computed by a BreachWarning node.<br>
I’ll add that code to the SoundNav module in a few days - you can <a href="https://github.com/SlicerIGT/SlicerSoundControl/issues/1">track its status here</a>.</p>

---

## Post #5 by @pieper (2017-07-14 20:11 UTC)

<p>You may also want to look at the research described here:</p>
<p><a href="https://na-mic.org/wiki/Project_Week_25/Improving_Depth_Perception_in_Interventional_Augmented_Reality_Visualization/Sonification" class="onebox" target="_blank">https://na-mic.org/wiki/Project_Week_25/Improving_Depth_Perception_in_Interventional_Augmented_Reality_Visualization/Sonification</a></p>

---
