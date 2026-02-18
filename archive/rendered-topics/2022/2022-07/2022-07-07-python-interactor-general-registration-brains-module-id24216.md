# python interactor - General Registration (BRAINS) module

**Topic ID**: 24216
**Date**: 2022-07-07
**URL**: https://discourse.slicer.org/t/python-interactor-general-registration-brains-module/24216

---

## Post #1 by @Noemi_Garau (2022-07-07 03:09 UTC)

<p>Dear all,<br>
I’m working with a large amount of CT scans and I need to apply rigid registration between series acquired at different time points. Using simpleITK I’m still not able to reach results good enough in a reasonable time compared to those obtained through the General Registration (BRAINS) module. Therefore I’m trying to apply it through python interactive module. Is the approach reported below correct? How can I save the obtained transformation so to apply it in a second moment so to avoid saving the transformed image?</p>
<pre><code class="lang-python">scene = slicer.mrmlScene
slicer.util.selectModule('BRAINSFit')
brainsFit = slicer.modules.brainsfit

t0 = slicer.util.loadVolume('fixed.mha')
t1 = slicer.util.loadVolume('moving.mha')

shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)

parametersRigid = {}
parametersRigid["fixedVolume"] = t0.GetID()
parametersRigid["movingVolume"] = t1.GetID()

linearTransform = slicer.vtkMRMLLinearTransformNode()
linearTransform.SetName('t12t0Rigid')
slicer.mrmlScene.AddNode( linearTransform )

parametersRigid["linearTransform"] = linearTransform.GetID()
parametersRigid["useRigid"] = True
parametersRigid["samplingPercentage"] = 0.0002

cliBrainsFitRigidNode = None
cliBrainsFitRigidNode = slicer.cli.run(brainsFit, None, parametersRigid)
waitCount = 0
delayMs =700
while cliBrainsFitRigidNode.GetStatusString() != 'Completed' and waitCount &lt; 200:
         delayDisplay( "Register Day 2 CT to Day 1 CT using rigid registration... %d" % waitCount, delayMs )
         waitCount += 1
delayDisplay("Register Day 2 CT to Day 1 CT using rigid registration finished",delayMs)
</code></pre>

---

## Post #2 by @caioath (2022-07-10 13:11 UTC)

<p>Hi</p>
<p>Your code seems to work fine. Are you getting any errors?</p>
<p>If the script is “skipping” the registration, you might try</p>
<p><code>cliBrainsFitRigidNode = slicer.cli.runSync(brainsFit, None, parametersRigid)</code></p>
<p>instead of</p>
<aside class="quote no-group" data-username="Noemi_Garau" data-post="1" data-topic="24216">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/noemi_garau/48/15911_2.png" class="avatar"> Noemi_Garau:</div>
<blockquote>
<p><code>cliBrainsFitRigidNode = slicer.cli.run(brainsFit, None, parametersRigid)</code></p>
</blockquote>
</aside>
<p>For saving the transformation you can use</p>
<p><code>saveNode(linearTransform, PATH_TO_SAVE_TRANSFORM)</code></p>
<p>Caio</p>

---

## Post #3 by @xuec (2024-08-28 11:39 UTC)

<p>Hi, Sorry for hijacking the thread, but I am wondering, how could I save the transformation image as well as the transformation matrix? Thanks</p>

---
