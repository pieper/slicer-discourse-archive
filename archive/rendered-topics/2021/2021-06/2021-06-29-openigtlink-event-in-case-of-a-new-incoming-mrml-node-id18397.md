---
topic_id: 18397
title: "Openigtlink Event In Case Of A New Incoming Mrml Node"
date: 2021-06-29
url: https://discourse.slicer.org/t/18397
---

# OpenIGTLink event in case of a new incoming MRML node

**Topic ID**: 18397
**Date**: 2021-06-29
**URL**: https://discourse.slicer.org/t/openigtlink-event-in-case-of-a-new-incoming-mrml-node/18397

---

## Post #1 by @atracsys-sbt (2021-06-29 14:45 UTC)

<p>Hi,<br>
I’m coding a scripted module that handles an OpenIGTLink connection to a tracker and I experience some delay between the call to start the connection and when the incoming data is actually streamed.<br>
I have tried using the solution proposed <a href="https://discourse.slicer.org/t/igt-vtkmrmligtlconnectornode-best-way-to-know-how-long-to-wait-for-connection-and-node-access/5417/2">here</a> by <a class="mention" href="/u/lassoan">@lassoan</a> but it seems the ConnectedEvent is still sent prior to the actual streaming. With the code below, I still get 0 incoming MRML node at run time, but shortly after I can definitely see the incoming node in the Data tree of Slicer.</p>
<pre><code class="lang-auto">self.cnode = slicer.vtkMRMLIGTLConnectorNode()
self.cnode.SetName('PointerConnector')
slicer.mrmlScene.AddNode(self.cnode)
self.addObserver(self.cnode, slicer.vtkMRMLIGTLConnectorNode.ConnectedEvent, self.onConnected)
if self.cnode.Start() != 1:
   slicer.util.errorDisplay("Cannot connect to openIGTLink")

def onConnected(self, caller, event):
  if self.cnode.GetNumberOfIncomingMRMLNodes() == 0:
    slicer.util.errorDisplay("No data streamed")
  elif cnode.GetIncomingMRMLNode(0).GetClassName() != 'vtkMRMLLinearTransformNode':
    slicer.util.errorDisplay("Streamed data not a linear transform")
  else:
    self.pointerTransform = cnode.GetIncomingMRMLNode(0)
</code></pre>
<p>Thank you for any help,<br>
S.</p>

---

## Post #2 by @lassoan (2021-06-29 16:12 UTC)

<p>Establishing a connection and receiving messages are independent events. You can receive messages anytime after the connection is established. The server may send new transform names, images, etc. anytime, even several hours after the connection is established (whenever the server wants to send them).</p>
<p>If you want to get notified about a new node then you can add an observer to the MRML scene. See an example <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#show-volume-rendering-automatically-when-a-volume-is-loaded">here</a>.</p>

---

## Post #3 by @atracsys-sbt (2021-06-29 22:03 UTC)

<p>Thank you for your response.<br>
If I understand correctly, I should have in my module widget class:</p>
<pre><code class="lang-auto">class MyModuleWidget(ScriptedLoadableModuleWidget, VTKObservationMixin):
  ...
  def setup(self):
    ...
    slicer.mrmlScene.AddObserver(slicer.vtkMRMLScene.NodeAddedEvent, self.onNodeAdded)
    self.cnode = slicer.vtkMRMLIGTLConnectorNode()
    self.cnode.SetName('PointerConnector')
    slicer.mrmlScene.AddNode(self.cnode)
    self.cnode.Start()

  def onNodeAdded(self, caller, event, calldata):
    calledNode = calldata
    if isinstance(calledNode, slicer.vtkMRMLLinearTransformNode): # check new node class
      if self.cnode.GetNumberOfIncomingMRMLNodes() &gt; 0: # connection has at least one node
        if self.cnode.GetIncomingMRMLNode(0).GetID() == calledNode.GetID(): # check if nodes identical
          self.logic.process(self.phantomModel, self.pointerModel, calledNode)
</code></pre>
<p>However, by doing so I get an error on my callback:</p>
<pre><code class="lang-auto">TypeError: onNodeAdded() missing 1 required positional argument: 'calldata'
</code></pre>
<p>Is it possible to have a callback with calldata and as a member function of the widget class (using self to get cnode) ?</p>

---

## Post #4 by @lassoan (2021-06-30 01:05 UTC)

<p>You need to add the <code>@vtk.calldata_type(vtk.VTK_OBJECT)</code> decorator as it is shown in the example I referenced in my previous post.</p>

---
