---
topic_id: 25044
title: "Adding Observer Within C Loadable Crashes Slicer"
date: 2022-09-01
url: https://discourse.slicer.org/t/25044
---

# Adding Observer within c++ loadable crashes Slicer

**Topic ID**: 25044
**Date**: 2022-09-01
**URL**: https://discourse.slicer.org/t/adding-observer-within-c-loadable-crashes-slicer/25044

---

## Post #1 by @leo (2022-09-01 16:25 UTC)

<p>Hello all!<br>
So I was trying to implement this line of code from Python in c++:</p>
<pre><code class="lang-auto">id = crosshairNode.AddObserver(slicer.vtkMRMLCrosshairNode.CursorPositionModifiedEvent, onMouseMoved)
</code></pre>
<p>and my first guess was this one:</p>
<pre><code class="lang-auto">  vtkNew&lt;vtkMRMLScene&gt; scene;
    vtkMRMLVolumeNode* volumeNode = vtkMRMLVolumeNode :: SafeDownCast( scene-&gt;GetNodeByID("MRHead"));
    vtkMRMLVolumeNode* inputVolumeNode;
    vtkMRMLCrosshairNode* crosshairNode;
    vtkSmartPointer&lt;vtkCallbackCommand&gt; callback;
   crosshairNode -&gt; AddObserver( vtkMRMLCrosshairNode:: CursorPositionModifiedEvent, callback)
</code></pre>
<p>this crashes my application immediately.</p>
<p>I also tried to add an observer this way, which actually did not crash, but I don’t know if the observer was actually listening.</p>
<p>I tried to create an event handler that had the NodeCallback Type:</p>
<pre><code class="lang-auto">vtkNew&lt;vtkMRMLCoreTestingUtilities::vtkMRMLNodeCallback&gt; eventHandler() {
 vtkNew&lt;vtkMRMLCoreTestingUtilities::vtkMRMLNodeCallback&gt; callback;
   
 qDebug() &lt;&lt; "... handler";
    
 return callback;
}
      scene-&gt;AddObserver(vtkCommand :: AnyEvent, eventHandler());
</code></pre>
<p>I woul be really glad for any help.</p>

---
