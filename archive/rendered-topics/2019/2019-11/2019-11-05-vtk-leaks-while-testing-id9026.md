---
topic_id: 9026
title: "Vtk Leaks While Testing"
date: 2019-11-05
url: https://discourse.slicer.org/t/9026
---

# VTK leaks while testing

**Topic ID**: 9026
**Date**: 2019-11-05
**URL**: https://discourse.slicer.org/t/vtk-leaks-while-testing/9026

---

## Post #1 by @Alex_Vergara (2019-11-05 08:57 UTC)

<p>Basically I have this code for setting a default volume in the views</p>
<pre><code class="lang-python">        mainWindow = slicer.util.mainWindow()
        if mainWindow is not None:
            layoutManager = slicer.app.layoutManager()
            if layoutManager is not None:
                
                sliceLogic = layoutManager.sliceWidget('Red').sliceLogic()
                CompositeNode = sliceLogic.GetSliceCompositeNode()
                CompositeNode.SetLinkedControl(1)
                sliceLogic.StartSliceCompositeNodeInteraction(1)
                CompositeNode.SetBackgroundVolumeID(minCTID)
                CompositeNode.SetForegroundVolumeID(minSPECTID)
                sliceLogic.EndSliceCompositeNodeInteraction()

                layoutManager.setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutFourUpView)
                slicer.util.resetSliceViews()
</code></pre>
<p>It works like a charm in normal mode, but when testing with <code>--no-main-window</code> it creates the following error</p>
<pre><code class="lang-bash">3: Test checkAttributes_positive passed!
3: 
3: **************************************
3: 
3: ok
3: runTest (slicer.ScriptedLoadableModule.ScriptedLoadableModuleTest) ... No test is defined in ScriptedLoadableModuleTest
3: ok
3: 
3: ----------------------------------------------------------------------
3: Ran 2 tests in 0.732s
3: 
3: OK
3: vtkDebugLeaks has detected LEAKS!
3: Class "vtkObserverManager" has 1 instance still around.
3: Class "vtkMRMLSliceCompositeNode" has 1 instance still around.
3: Class "vtkCommand or subclass" has 2 instances still around.
3: 
3/4 Test #3: py_Dosimetry4DTest ...............***Failed   10.47 sec
</code></pre>
<p>As you can see the test passed, but the VTK leaks breaks the workflow<br>
Without the above code, the VTK leaks are not present. However that code is not intended to run at all in no window mode, that is why I check if there is a main window. However, the check is failing as it creates the composite nodes. How is this possible?? Is there a way to NOT run a piece of code in no window mode??</p>

---

## Post #2 by @lassoan (2019-11-05 14:02 UTC)

<p>Have you included the complete test here? If there is no main window then the script above should not do anything.</p>

---

## Post #3 by @jamesobutler (2019-11-05 14:44 UTC)

<p>I get the exact vtkDebugLeaks message only if I have implemented code in python such as <code>slicer.mrmlScene.CreateNodeByClass("vtkMRMLSliceCompositeNode")</code>.</p>
<p>See <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MemoryManagement#Python_scripts_and_scripted_modules" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MemoryManagement#Python_scripts_and_scripted_modules</a></p>

---

## Post #4 by @Alex_Vergara (2019-11-05 14:48 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> I found out that I was doing in the test</p>
<pre><code class="lang-python">    def makeSlicerLinkedCompositeNodes():
        # Set linked slice views  in all existing slice composite nodes and in the default node
        sliceCompositeNodes = slicer.util.getNodesByClass('vtkMRMLSliceCompositeNode')
        defaultSliceCompositeNode = slicer.mrmlScene.GetDefaultNodeByClass('vtkMRMLSliceCompositeNode')
        if not defaultSliceCompositeNode:
            defaultSliceCompositeNode = slicer.mrmlScene.CreateNodeByClass('vtkMRMLSliceCompositeNode')
            slicer.mrmlScene.AddDefaultNode(defaultSliceCompositeNode)
        sliceCompositeNodes.append(defaultSliceCompositeNode)
        for sliceCompositeNode in sliceCompositeNodes:
            sliceCompositeNode.SetLinkedControl(True)
</code></pre>
<p>without checking properly if there was a Slicer window, this was the problem. So I changed the function to check for mainwindow first. Sorry for bothering you.</p>

---
