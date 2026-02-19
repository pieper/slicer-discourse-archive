---
topic_id: 4432
title: "Cannot Run The Registration In Python Interactor"
date: 2018-10-17
url: https://discourse.slicer.org/t/4432
---

# Cannot run the registration in python interactor

**Topic ID**: 4432
**Date**: 2018-10-17
**URL**: https://discourse.slicer.org/t/cannot-run-the-registration-in-python-interactor/4432

---

## Post #1 by @Navodini_Wijethilake (2018-10-17 12:20 UTC)

<p>Hey!!<br>
I was trying to run the registration code in the below link in the python interactor, but it doesn’t work.<br>
Can somebody please help me to find the terminal I have to use for this?<br>
<a href="https://www.slicer.org/wiki/Documentation/4.1/Modules/BRAINSFit" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/4.1/Modules/BRAINSFit</a></p>

---

## Post #2 by @cpinter (2018-10-17 15:02 UTC)

<p>Here’s an example<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/SlicerRt/SlicerRT/blob/master/Testing/Python/IGRTWorkflow_SelfTest.py#L372-L405" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerRt/SlicerRT/blob/master/Testing/Python/IGRTWorkflow_SelfTest.py#L372-L405" target="_blank">SlicerRt/SlicerRT/blob/master/Testing/Python/IGRTWorkflow_SelfTest.py#L372-L405</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="372" style="counter-reset: li-counter 371 ;">
<li>scene = slicer.mrmlScene
</li>
<li>slicer.util.selectModule('BRAINSFit')
</li>
<li>brainsFit = slicer.modules.brainsfit
</li>
<li>
</li>
<li># Hide isodose
</li>
<li>shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)
</li>
<li>self.assertIsNotNone( shNode )
</li>
<li>day2IsodoseShItemID = shNode.GetItemByDataNode(slicer.util.getNode(self.day2IsodosesName))
</li>
<li>shNode.SetDisplayVisibilityForBranch(day2IsodoseShItemID, 0)
</li>
<li>
</li>
<li># Register Day 2 CT to Day 1 CT using rigid registration
</li>
<li>self.delayDisplay("Register Day 2 CT to Day 1 CT using rigid registration.\n  It may take a few minutes...",self.delayMs)
</li>
<li>
</li>
<li>parametersRigid = {}
</li>
<li>day1CT = slicer.util.getNode(self.day1CTName)
</li>
<li>parametersRigid["fixedVolume"] = day1CT.GetID()
</li>
<li>
</li>
<li>day2CT = slicer.util.getNode(self.day2CTName)
</li>
<li>parametersRigid["movingVolume"] = day2CT.GetID()
</li>
<li>
</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/SlicerRt/SlicerRT/blob/master/Testing/Python/IGRTWorkflow_SelfTest.py#L372-L405" target="_blank">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
<br>
You need to make sure that the parameters are optimal. Follow a recipe from the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Registration/RegistrationLibrary">registration library</a> if it helps.</p>

---

## Post #3 by @cpinter (2018-10-17 15:03 UTC)

<aside class="quote no-group" data-username="Navodini_Wijethilake" data-post="1" data-topic="4432">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/aeb1de/48.png" class="avatar"> Navodini_Wijethilake:</div>
<blockquote>
<p>find the terminal</p>
</blockquote>
</aside>
<p>View / Python interactor or the yellow/blue snake icon on the toolbar.</p>

---
