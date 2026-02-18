# Observe camera node events in a loadable module logic

**Topic ID**: 17879
**Date**: 2021-05-31
**URL**: https://discourse.slicer.org/t/observe-camera-node-events-in-a-loadable-module-logic/17879

---

## Post #1 by @Mik (2021-05-31 06:02 UTC)

<p>Are there any specific requirements to observe vtkMRMLCameraNode events in C++ module logic?</p>
<p>Python code works as it should, and i can see “update beam” message</p>
<pre><code class="lang-auto">def updateBeamFromCamera(caller=None, event=None):
  print("update beam")

cameraObs = threeDcamera.AddObserver( vtk.vtkCommand.ModifiedEvent, updateBeamFromCamera)
</code></pre>
<p>But i can’t observe any camera node events in C++ module.</p>
<p>Did i miss something obvious?</p>
<p>Here is a part of C++ code</p>
<pre><code class="lang-auto">//-----------------------------------------------------------------------------
void vtkSlicerSomeLogic::RegisterNodes()
{
  vtkMRMLScene* scene = this-&gt;GetMRMLScene(); 
  if (!scene)
  {
    vtkErrorMacro("RegisterNodes: Invalid MRML scene");
    return;
  }
  if (!scene-&gt;IsNodeClassRegistered("vtkMRMLCameraNode"))
  {
    vtkWarningMacro("OnMRMLSceneNodeAdded: camera registered");
    scene-&gt;RegisterNodeClass(vtkSmartPointer&lt;vtkMRMLCameraNode&gt;::New());
  }
}

//---------------------------------------------------------------------------
void vtkSlicerSomeLogic::OnMRMLSceneNodeAdded(vtkMRMLNode* node)
{
  if (!node || !this-&gt;GetMRMLScene())
  {
    vtkErrorMacro("OnMRMLSceneNodeAdded: Invalid MRML scene or input node");
    return;
  }

  if (node-&gt;IsA("vtkMRMLCameraNode"))
  {
    vtkWarningMacro("OnMRMLSceneNodeAdded: Observe camera events");
    // Observe camera events
    vtkNew&lt;vtkIntArray&gt; events;
    events-&gt;InsertNextValue(vtkCommand::ModifiedEvent);
    vtkObserveMRMLNodeEventsMacro(node, events);
  }
}

//----------------------------------------------------------------------------
void vtkSlicerSomeLogic::ProcessMRMLNodesEvents(vtkObject* caller, unsigned long event, void* callData)
{
  Superclass::ProcessMRMLNodesEvents(caller, event, callData);

  vtkMRMLScene* mrmlScene = this-&gt;GetMRMLScene();
  if (!mrmlScene)
  {
    vtkErrorMacro("ProcessMRMLNodesEvents: Invalid MRML scene");
    return;
  }
  if (mrmlScene-&gt;IsBatchProcessing())
  {
    return;
  }

  if (caller-&gt;IsA("vtkMRMLCameraNode"))
  {
    vtkMRMLCameraNode* cameraNode = vtkMRMLCameraNode::SafeDownCast(caller);
    if (event == vtkCommand::ModifiedEvent)
    {
      vtkWarningMacro("ProcessMRMLNodesEvents: Camera modified");
    }
    else
    {
      vtkWarningMacro("ProcessMRMLNodesEvents: Other events");
    }
  }
}
</code></pre>

---

## Post #2 by @lassoan (2021-05-31 18:52 UTC)

<aside class="quote no-group" data-username="Mik" data-post="1" data-topic="17879">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/958977/48.png" class="avatar"> Mik:</div>
<blockquote>
<p><code>scene-&gt;RegisterNodeClass(vtkSmartPointer&lt;vtkMRMLCameraNode&gt;::New());</code></p>
</blockquote>
</aside>
<p>This would re-register the vtkMRMLCameraNode class, this must not be done.</p>
<aside class="quote no-group" data-username="Mik" data-post="1" data-topic="17879">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/958977/48.png" class="avatar"> Mik:</div>
<blockquote>
<pre><code class="lang-auto">if (node-&gt;IsA("vtkMRMLCameraNode"))
  {
    vtkWarningMacro("OnMRMLSceneNodeAdded: Observe camera events");
    // Observe camera events
    vtkNew&lt;vtkIntArray&gt; events;
    events-&gt;InsertNextValue(vtkCommand::ModifiedEvent);
    vtkObserveMRMLNodeEventsMacro(node, events);
  }
</code></pre>
</blockquote>
</aside>
<p>This would add observer to the last added camera node. Instead of this, you should either observe all the camera nodes or one that the user selected.</p>

---

## Post #3 by @Mik (2021-05-31 20:27 UTC)

<p>Thank you! I understood what was the problem.</p>
<p>Another question. Should i remove observe from previously observed camera if i change one camera to the other or it is an automatic process?</p>
<p>for example</p>
<pre><code class="lang-auto">//----------------------------------------------------------------------------
void vtkMRMLMyCustomNode::SetAndObserveCameraNode(vtkMRMLCameraNode* node)
{
  if (node &amp;&amp; this-&gt;Scene != node-&gt;GetScene())
  {
    vtkErrorMacro("SetAndObserveCameraNode: Cannot set reference");
    return;
  }

  if(vtkMRMLCameraNode* previouslyObservedNode = this-&gt;GetCameraNode())
  {
    vtkUnObserveMRMLObjectMacro(previouslyObservedNode );
  }

  this-&gt;SetNodeReferenceID(CAMERA_REFERENCE_ROLE, (node ? node-&gt;GetID() : nullptr));

  if (node)
  {
    vtkNew&lt;vtkIntArray&gt; events;
    events-&gt;InsertNextValue(vtkCommand::ModifiedEvent);
    vtkObserveMRMLObjectEventsMacro(node, events);
  }
}
</code></pre>

---

## Post #4 by @lassoan (2021-05-31 21:18 UTC)

<aside class="quote no-group" data-username="Mik" data-post="3" data-topic="17879">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/958977/48.png" class="avatar"> Mik:</div>
<blockquote>
<p>Another question. Should i remove observe from previously observed camera if i change one camera to the other or it is an automatic process?</p>
</blockquote>
</aside>
<p><code>vtkObserveMRMLObjectEventsMacro</code> only adds the observer, never removes it, so you either need to use <code>vtkUnObserveMRMLObjectEventsMacro</code> for the previously observed node; or use <code>vtkSetAndObserveMRMLObjectMacro</code>, which automatically removes the previous observation.</p>

---
