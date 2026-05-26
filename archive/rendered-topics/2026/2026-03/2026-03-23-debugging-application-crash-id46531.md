---
topic_id: 46531
title: "Debugging application crash"
date: 2026-03-23
url: https://discourse.slicer.org/t/46531
last_bumped: 2026-04-05T21:29:45.372Z
---

# Debugging application crash

**Topic ID**: 46531
**Date**: 2026-03-23
**URL**: https://discourse.slicer.org/t/debugging-application-crash/46531

---

## Post #1 by @sogo (2026-03-23 05:39 UTC)

<p>I am in process of merging our organization’s SW pipeline based on top of Slicer-4.11 into Slicer-5.10. While I am able to merge and resolve merge conflicts, my application is crashing on startup. I was following the startup routines from,</p>
<pre><code class="lang-auto">

qSlicerApplicationHelper::postInitializeApplication

if (enableMainWindow)
{
window.reset(new SlicerMainWindowType); &lt;----
}
</code></pre>
<p>So far I am able to trace the crash until this function, this→Modified() call:</p>
<pre><code class="lang-auto">//----------------------------------------------------------------------------
void vtkMRMLSliceLogic::SetSliceNode(vtkMRMLSliceNode* newSliceNode)
{
  if (this-&gt;SliceNode == newSliceNode)
  {
    return;
  }

  // Observe the slice node for general properties like slice visibility.
  // But the slice layers will also notify us when things like transforms have
  // changed.
  // This class takes care of passing the one slice node to each of the layers
  // so that users of this class only need to set the node one place.
  vtkSetAndObserveMRMLNodeMacro(this-&gt;SliceNode, newSliceNode);

  this-&gt;UpdateSliceCompositeNode();

  for (LayerListIterator iterator = this-&gt;Layers.begin(); iterator != this-&gt;Layers.end(); ++iterator)
  {
    vtkMRMLSliceLayerLogic* layer = *iterator;
    if (layer != nullptr)
    {
      layer-&gt;SetSliceNode(newSliceNode);
    }
  }

  this-&gt;Modified();   &lt;----
}
</code></pre>
<p>I further traced this to this function:</p>
<pre><code class="lang-auto">//---------------------------------------------------------------------------
void vtkMRMLAbstractLogic::Modified()
{
  if (this-&gt;GetDisableModifiedEvent())
  {
    ++this-&gt;Internal-&gt;ModifiedEventPending;
    return;
  }
  this-&gt;Superclass::Modified();
}
</code></pre>
<p>I understand this→Superclass::Modified() is a call routines connected to observers. But I am not able to find what routines this caller calls which is causing the crash. Some hints I was able to find were,</p>
<p>1- It crashes on setting first vtk MRML slice node ‘Red’.</p>
<p>2- I believe the invoke event that triggers crash is <code>vtkCommand::ModifiedEvent</code>. I find this in vtkObject clas, function, <code>vtkTypeBool vtkSubjectHelper::InvokeEvent(unsigned long event, void* callData, vtkObject* self)</code> in call <code>elem-&gt;Command-&gt;Execute(self, event, callData);</code>. The event# is 33.</p>
<p>I wanted to ask is there a way to find what routines the callback calls that can be checked for possible crash.</p>

---

## Post #2 by @pieper (2026-03-23 12:13 UTC)

<p>Have you hooked up a debugger to get a stack trace?  The observer pattern means that code dynamically adds callback functions to be called when data is modified, and from there many things can happen and your code needs to be careful not to get in an event loop or work with data that isn’t yet fully configured.</p>

---

## Post #3 by @sogo (2026-03-24 04:40 UTC)

<p>Hi Pieper, I am thinking to hookup debugger but currently I am in release mode so will have to build in debug mode. For now, is there any way to know which functions are using callback for a ModifiedEvent, it should be statically defined (hardcoded) instead of dynamic?</p>

---

## Post #4 by @sogo (2026-03-28 05:42 UTC)

<p>Update on this. I was able to use stack trace and fix the problem. Thank you Pieper for the idea. Closing this thread.</p>

---

## Post #5 by @Nancy_Casper (2026-04-04 06:49 UTC)

<p>That’s a tough one to track down, especially when it’s an intermittent crash. Since there’s no clear error message, it usually points toward a memory management issue or a conflict with a specific module. A good first step is to check the Slicer log files right after a crash happens - sometimes the very last entry gives a hint of what was being loaded. If you’re on Windows, you might also want to try running Slicer through a debugger like Visual Studio to see if you can catch the specific exception. Sometimes just disabling any recently added extensions one by one can help narrow down if a specific tool is causing the instability. Stay patient, these debugging marathons can be a real test!</p>

---

## Post #6 by @sogo (2026-04-05 21:29 UTC)

<p>Hi <a class="mention" href="/u/nancy_casper">@Nancy_Casper</a> Thank you for the response. I was able to track down using stack trace as suggested by Pieper.</p>

---
