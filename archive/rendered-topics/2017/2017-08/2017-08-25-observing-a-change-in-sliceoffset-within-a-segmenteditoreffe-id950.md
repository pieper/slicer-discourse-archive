# Observing a change in SliceOffset within a SegmentEditorEffect class

**Topic ID**: 950
**Date**: 2017-08-25
**URL**: https://discourse.slicer.org/t/observing-a-change-in-sliceoffset-within-a-segmenteditoreffect-class/950

---

## Post #1 by @moselhy (2017-08-25 21:53 UTC)

<p>Hello,</p>
<p>I am trying to detect changes in slice offsets e.g. <code>slicer.app.layoutManager().sliceWidget('Red').sliceLogic().GetSliceOffset()</code> and call a method within a SegmentEditorEffect class. I want to use the AddObserver method but I couldn’t find an event to attach to in these classes, even though I think one is there but I don’t know it:</p>
<p><a href="http://apidocs.slicer.org/master/classvtkMRMLSliceLogic.html" class="onebox" target="_blank" rel="nofollow noopener">http://apidocs.slicer.org/master/classvtkMRMLSliceLogic.html</a><br>
<a href="http://apidocs.slicer.org/master/classvtkMRMLScene.html" class="onebox" target="_blank" rel="nofollow noopener">http://apidocs.slicer.org/master/classvtkMRMLScene.html</a><br>
<a href="http://apidocs.slicer.org/master/classqMRMLSliceView.html" class="onebox" target="_blank" rel="nofollow noopener">http://apidocs.slicer.org/master/classqMRMLSliceView.html</a></p>

---

## Post #2 by @lassoan (2017-08-25 22:12 UTC)

<p>In general, if you want to get notified about changes in a VTK object, such as a MRML node, add an observer the “modified” event (vtk.vtkCommand.ModifiedEvent).</p>

---

## Post #3 by @moselhy (2017-08-28 17:16 UTC)

<p>Thank you for that. However, when I try to set a sample method to a sliceLogic node, it executes 6 times when I change the Slice Offset. Here is how to reproduce this:</p>
<pre><code>def sampleMethod(caller, event):
  print("This is a sample method")

color = "Red"
import SampleData
SampleData.SampleDataLogic().downloadMRBrainTumor1()
sliceLogic = slicer.app.layoutManager().sliceWidget(color).sliceLogic()
sliceLogic.AddObserver(vtk.vtkCommand.ModifiedEvent, sampleMethod)
sliceLogic.SetSliceOffset(sliceLogic.GetSliceOffset() + 0.01)
</code></pre>
<p>I want it only to execute once when <code>sliceLogic.SetSliceOffset(sliceLogic.GetSliceOffset() + 0.01)</code> is called, how do I achieve this?</p>

---

## Post #4 by @jcfr (2017-08-28 19:58 UTC)

<p>This happens because the underlying  <code>sliceNode</code> is effectively modified few times.</p>
<p>The preferred way to update the offset is to set property on the node itself. (see below)</p>
<p>Waiting we fix the code to effectively trigger on Modified event, here is a workaround</p>
<pre><code class="lang-python">import SampleData
from slicer.util import NodeModify

SampleData.SampleDataLogic().downloadMRBrainTumor1()

def sampleMethod(caller, event):
  print("This is a sample method")

color = "Red"

sliceNode = slicer.mrmlScene.GetNodeByID("vtkMRMLSliceNode%s" % color)
sliceNode.AddObserver(vtk.vtkCommand.ModifiedEvent, sampleMethod)

with NodeModify(sliceNode):
  sliceNode.SetSliceOffset(sliceNode.GetSliceOffset() + 0.01)
</code></pre>
<p>Note also that using the method <code>vtkMRMLSliceLogic::SetSliceOffset</code> provided by the logic is deprecated. I found out by looking at a comment in  the implementation, we will need to update the documentation:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/fd625e782864941805c7880f6e58a7ba98380f59/Libs/MRML/Logic/vtkMRMLSliceLogic.cxx#L1916-L1922" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/fd625e782864941805c7880f6e58a7ba98380f59/Libs/MRML/Logic/vtkMRMLSliceLogic.cxx#L1916-L1922" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/fd625e782864941805c7880f6e58a7ba98380f59/Libs/MRML/Logic/vtkMRMLSliceLogic.cxx#L1916-L1922</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="1916" style="counter-reset: li-counter 1915 ;">
<li>void vtkMRMLSliceLogic::SetSliceOffset(double offset)</li>
<li>{</li>
<li>
</li>
<li>// this method has been moved to vtkMRMLSliceNode</li>
<li>// the API stays for backwards compatibility</li>
<li>
</li>
<li>vtkMRMLSliceNode *sliceNode = this-&gt;GetSliceNode();</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #5 by @lassoan (2017-08-29 14:00 UTC)

<p>Note that it is normal t get multiple node Modified events, often because of changing of properties that are not relevant for you, and potentially triggered by other modules.</p>
<p>So, if performance is an issue, then you have many options to deal with this. For example:</p>
<ul>
<li>Option A: Check if relevant properties of the observed node are changed and only perform your lengthy processing if needed (you need to store the properties that you used for the last processing)</li>
<li>Option B: Do a delayed update. Instead of calling processing method directly, create a QTimer that calls the processing method when the time is up. When you get a modified event, reset the QTimer. Typically a delay of about 1 second or less works well. This method is used in the <code>Grow from seeds</code> segment editor effect.</li>
</ul>

---

## Post #6 by @moselhy (2017-08-29 14:01 UTC)

<p>I did exactly option A, thanks.</p>
<p>Also, jcfr’s method of using the SliceNode’s <code>SetSliceOffset</code> method only calls ModifiedEvent once, which works without having to use a workaround.</p>

---
