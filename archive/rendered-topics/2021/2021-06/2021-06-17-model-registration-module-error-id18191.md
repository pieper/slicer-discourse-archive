---
topic_id: 18191
title: "Model Registration Module Error"
date: 2021-06-17
url: https://discourse.slicer.org/t/18191
---

# Model Registration Module Error

**Topic ID**: 18191
**Date**: 2021-06-17
**URL**: https://discourse.slicer.org/t/model-registration-module-error/18191

---

## Post #1 by @sfglio (2021-06-17 18:33 UTC)

<p>How can I fix the following error message?</p>
<p>Traceback (most recent call last):<br>
File “/Applications/Slicer.app/Contents/Extensions-29959/SlicerIGT/lib/Slicer-4.13/qt-scripted-modules/ModelRegistration.py”, line 167, in onApplyButton<br>
logic.run(inputSourceModel, inputTargetModel, outputSourceToTargetTransform, self.typeSelector.currentIndex, self.iterationSpin.value )<br>
File “/Applications/Slicer.app/Contents/Extensions-29959/SlicerIGT/lib/Slicer-4.13/qt-scripted-modules/ModelRegistration.py”, line 185, in run<br>
self.delayDisplay(‘Running iterative closest point registration’)<br>
AttributeError: ‘ModelRegistrationLogic’ object has no attribute ‘delayDisplay’</p>
<p>I am using the latest nighty version of slicer…</p>
<p>Kind regards</p>

---

## Post #2 by @jamesobutler (2021-06-17 21:24 UTC)

<p><code>delayDisplay</code> in the ScriptedModuleLogic class had been deprecated due to <code>delayDisplay</code> being for testing purposes and had been in the ScriptedModuleTest class in addition to being available from anywhere using <code>slicer.util.delayDisplay</code>. The deprecation of <code>delayDisplay</code> in the Logic class was enforced as it was removed in favor of only having the other locations. This was <a href="https://github.com/Slicer/Slicer/commit/71f236bfacffec1d6c01036840dfc8d89be0563c" class="inline-onebox" rel="noopener nofollow ugc">ENH: Move testing methods in scripted logic class to test class · Slicer/Slicer@71f236b · GitHub</a>.</p>
<p>Therefore the ModelRegistration module needs to be updated here:</p><aside class="onebox githubblob">
  <header class="source">

      <a href="https://github.com/SlicerIGT/SlicerIGT/blob/5cb6a0eda5a38cf4f4d04c475e9cbca7227ad200/ModelRegistration/ModelRegistration.py#L185" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerIGT/SlicerIGT/blob/5cb6a0eda5a38cf4f4d04c475e9cbca7227ad200/ModelRegistration/ModelRegistration.py#L185" target="_blank" rel="noopener nofollow ugc">SlicerIGT/SlicerIGT/blob/5cb6a0eda5a38cf4f4d04c475e9cbca7227ad200/ModelRegistration/ModelRegistration.py#L185</a></h4>



  <pre class="onebox">    <code class="lang-py">
      <ol class="start lines" start="175" style="counter-reset: li-counter 174 ;">
          <li>class ModelRegistrationLogic(ScriptedLoadableModuleLogic):</li>
          <li>  """This class should implement all the actual</li>
          <li>  computation done by your module.  The interface</li>
          <li>  should be such that other python code can import</li>
          <li>  this class and make use of the functionality without</li>
          <li>  requiring an instance of the Widget</li>
          <li>  """</li>
          <li>
          </li>
<li>  def run(self, inputSourceModel, inputTargetModel, outputSourceToTargetTransform, transformType=0, numIterations=100 ):</li>
          <li>
          </li>
<li class="selected">    self.delayDisplay('Running iterative closest point registration')</li>
          <li>
          </li>
<li>    icpTransform = vtk.vtkIterativeClosestPointTransform()</li>
          <li>    icpTransform.SetSource( inputSourceModel.GetPolyData() )</li>
          <li>    icpTransform.SetTarget( inputTargetModel.GetPolyData() )</li>
          <li>    icpTransform.GetLandmarkTransform().SetModeToRigidBody()</li>
          <li>    if transformType == 1:</li>
          <li>      icpTransform.GetLandmarkTransform().SetModeToSimilarity()</li>
          <li>    if transformType == 2:</li>
          <li>      icpTransform.GetLandmarkTransform().SetModeToAffine()</li>
          <li>    icpTransform.SetMaximumNumberOfIterations( numIterations )</li>
      </ol>
    </code>
  </pre>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @sfglio (2021-06-18 18:58 UTC)

<p>Thank you for your reply. But what exactly needs to be updated in L185 asking as a python newbie? Is that something I can fix?</p>
<p>In my script it looks exactly as indicated above.</p>

---

## Post #4 by @jamesobutler (2021-06-18 19:18 UTC)

<p>You could change it to</p>
<pre><code class="lang-python">slicer.util.delayDisplay('Running iterative closest point registration')
</code></pre>
<p>If you’re able to contribute this change by submitting a PR to <a href="https://github.com/SlicerIGT/SlicerIGT" class="inline-onebox" rel="noopener nofollow ugc">GitHub - SlicerIGT/SlicerIGT: Modules supporting image-guided interventions in 3D Slicer.</a> that would be helpful! Then other people that download the extension won’t experience the same issue you have found.</p>

---

## Post #5 by @sfglio (2021-06-18 20:43 UTC)

<p>Yes this works. I tried to open a PR in <a href="https://github.com/SlicerIGT/SlicerIGT" rel="noopener nofollow ugc">GitHub - SlicerIGT/SlicerIGT: Modules supporting image-guided interventions in 3D Slicer.</a><br>
[/quote] however I only managed to open an issue there…sorry</p>

---
