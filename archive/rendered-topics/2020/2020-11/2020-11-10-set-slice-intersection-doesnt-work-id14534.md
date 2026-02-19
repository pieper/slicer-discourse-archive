---
topic_id: 14534
title: "Set Slice Intersection Doesnt Work"
date: 2020-11-10
url: https://discourse.slicer.org/t/14534
---

# Set slice intersection doesn't work

**Topic ID**: 14534
**Date**: 2020-11-10
**URL**: https://discourse.slicer.org/t/set-slice-intersection-doesnt-work/14534

---

## Post #1 by @mau_igna_06 (2020-11-10 22:13 UTC)

<p>This works on the python console:</p>
<pre><code class="lang-auto">nodes = slicer.util.getNodesByClass('vtkMRMLSliceCompositeNode')
for node in nodes:#Corrected this line and the one below because of bad indentation
  node.SetSliceIntersectionVisibility(True)
</code></pre>
<p>But if I append it to the onEntry function of my extension it doesn’t work. Why does this happen?</p>

---

## Post #2 by @lassoan (2020-11-10 22:19 UTC)

<p>When you enter your module, <code>enter()</code> method is called, not <code>onEntry</code>. Indentation in your code snippet is also incorrect (second line should be indent level should be the same as the first). If these hints don’t help then set up a debugger and place a breakpoint in the method and inspect what is happening exactly when the method is executed.</p>

---

## Post #3 by @mau_igna_06 (2020-11-10 22:48 UTC)

<p>Hi Andras. Thanks for your answer. I took your advice of using Code to debug and I tried it in this case but I didn’t had success finding the cause of this error (I checked that the code executes not too early like the other day).</p>
<p>Here it is the line that is causing trouble if you want to check it out:<br>
</p><aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/mauigna06/PedicleScrewSimulator/blob/d4dc0c67de9b0e0e6d750511456617289d86ae33/PedicleScrewSimulator/PedicleScrewSimulatorWizard/ScrewStep.py#L854" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/mauigna06/PedicleScrewSimulator/blob/d4dc0c67de9b0e0e6d750511456617289d86ae33/PedicleScrewSimulator/PedicleScrewSimulatorWizard/ScrewStep.py#L854" target="_blank" rel="noopener nofollow ugc">mauigna06/PedicleScrewSimulator/blob/d4dc0c67de9b0e0e6d750511456617289d86ae33/PedicleScrewSimulator/PedicleScrewSimulatorWizard/ScrewStep.py#L854</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="844" style="counter-reset: li-counter 843 ;">
<li>#self.fiducial.addItem("Select an insertion site")</li><li>#self.fiducial.addItems(self.fiduciallist)</li><li></li><li>super(ScrewStep, self).onEntry(comingFrom, transitionType)</li><li></li><li>lm = slicer.app.layoutManager()</li><li>if lm == None:</li><li>  return</li><li>lm.setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutFourUpView)</li><li></li><li class="selected">nodes = slicer.util.getNodesByClass('vtkMRMLSliceCompositeNode')</li><li>for node in nodes:</li><li>  node.SetSliceIntersectionVisibility(True)</li><li> </li><li>pNode = self.parameterNode()</li><li>pNode.SetParameter('currentStep', self.stepid)</li><li>logging.debug("Current step: {0}".format(pNode.GetParameter('currentStep')))</li><li>self.approach = str(pNode.GetParameter('approach'))</li><li></li><li>qt.QTimer.singleShot(0, self.killButton)</li><li></li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #4 by @lassoan (2020-11-11 15:51 UTC)

<aside class="quote no-group" data-username="mau_igna_06" data-post="3" data-topic="14534">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p><code>nodes = slicer.util.getNodesByClass('vtkMRMLSliceCompositeNode')</code></p>
</blockquote>
</aside>
<p>Do you mean you get an error message when you run this line?<br>
What is the error message?</p>

---

## Post #5 by @mau_igna_06 (2020-11-11 20:22 UTC)

<p>When I said error I refer to an unexpected behaviour (that is: nothing happens).<br>
The problem is when I execute those lines nothing happens and it should show the slice intersections.</p>

---

## Post #6 by @lassoan (2020-11-11 22:22 UTC)

<p>Take advantage of your debugger. Step through your code, see how many composite nodes it finds. Add breakpoints to all the lines in all the files where <code>SetSliceIntersectionVisibility</code> is called (maybe after you enable visibility somewhere else it gets disabled). Add breakpoints at various other places in the code and iterate through the composite nodes and see if intersection visibility is still enabled - you should be able then find what makes the intersections hidden.</p>

---

## Post #7 by @mau_igna_06 (2020-11-12 17:56 UTC)

<p>Thank you Andras. I was able to find the problem: The onEntry function of Step5 was called before it was needed on the onExit function of Step4 so then the changes I setted up were being overwritten</p>

---
