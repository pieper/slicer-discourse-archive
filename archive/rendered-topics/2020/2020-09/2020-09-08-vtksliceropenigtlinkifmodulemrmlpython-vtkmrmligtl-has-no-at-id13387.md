# 'vtkSlicerOpenIGTLinkIFModuleMRMLPython.vtkMRMLIGTL' has no attribute 'ReceiveEvent'

**Topic ID**: 13387
**Date**: 2020-09-08
**URL**: https://discourse.slicer.org/t/vtksliceropenigtlinkifmodulemrmlpython-vtkmrmligtl-has-no-attribute-receiveevent/13387

---

## Post #1 by @luigi-palladino (2020-09-08 10:22 UTC)

<p>Hi,</p>
<p>I got this issue executing this code on Slicer 4.11.0-2019-09-25:</p>
<pre><code>    def addConnectorObservers(self):
       eventON = [slicer.vtkMRMLIGTLConnectorNode.ConnectedEvent, self.onStatus]
       self.cnode.AddObserver(eventON[0], eventON[1])
       eventOFF = [slicer.vtkMRMLIGTLConnectorNode.DisconnectedEvent, self.onStatus]
       self.cnode.AddObserver(eventOFF[0], eventOFF[1])
       eventWAIT = [slicer.vtkMRMLIGTLConnectorNode.ActivatedEvent, self.onStatus]
       self.cnode.AddObserver(eventWAIT[0], eventWAIT[1])
       eventRECEIVE = [slicer.vtkMRMLIGTLConnectorNode.ReceiveEvent, self.onStatus]#tof
       self.cnode.AddObserver(eventRECEIVE[0], eventRECEIVE[1]) #tof
</code></pre>
<p>And I got this error:</p>
<p><code>AttributeError: type object 'vtkSlicerOpenIGTLinkIFModuleMRMLPython.vtkMRMLIGTL' has no attribute 'ReceiveEvent'</code></p>
<p>Executing the same code on Slicer 4.8.1 it works fine.</p>
<p>Reading the doc it says that the VTK version was downgraded from 9.0 to 8.5.<br>
Could this be related to this issue?<br>
How could I fix this?</p>
<p>Thank you.</p>

---

## Post #2 by @Sunderlandkyl (2020-09-08 13:12 UTC)

<p>Between Slicer 4.8.1 and Slicer 4.10.2, the OpenIGTLinkIF module was reworked and moved to an extension. Probably the events were not migrated with the rest of the functionality. I’ll let you know when I’ve re-added the events.</p>

---
