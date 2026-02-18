# Disconnect signal

**Topic ID**: 7226
**Date**: 2019-06-18
**URL**: https://discourse.slicer.org/t/disconnect-signal/7226

---

## Post #1 by @tbillah (2019-06-18 22:40 UTC)

<p>I am connected to a figure like below:</p>
<pre><code class="lang-auto">    mainwindow = slicer.util.mainWindow()
    figureHandle= slicer.util.findChildren(mainwindow, className="qMRMLPlotView")[0]

</code></pre>
<p>Now, I would like to disconnect when File → Close Scene is selected. Is there a signal emitted when Close Scene is selected? For example, I am looking for something like below:</p>
<blockquote>
<p>figureHandle.disconnect(‘when scene is closed’)</p>
</blockquote>

---

## Post #2 by @jcfr (2019-06-19 02:41 UTC)

<p>The signals associated with the scene are documented here: <a href="http://apidocs.slicer.org/v4.10/classvtkMRMLScene.html#a8ccb4e378bdb987a4e95ac6cc1067c94" rel="nofollow noopener">http://apidocs.slicer.org/v4.10/classvtkMRMLScene.html#a8ccb4e378bdb987a4e95ac6cc1067c94</a></p>
<p>The relevant signal to observe is <code>vtkMRMLScene::EndCloseEvent</code></p>
<p>For example:</p>
<pre><code class="lang-auto">def onSceneEndCloseEvent(caller, eventId):
  print("Scene close")

slicer.mrmlScene.AddObserver(slicer.vtkMRMLScene.EndCloseEvent, onSceneEndCloseEvent)
</code></pre>
<p>To learn more about efficient way for managing VTK object connections, see also:</p>
<ul>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ/Python_Scripting#How_can_I_access_callData_argument_in_a_VTK_object_observer_callback_function" rel="nofollow noopener"> How can I access callData argument in a VTK object observer callback function</a></li>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ/Python_Scripting#How_to_manage_VTK_object_connections_.3F" rel="nofollow noopener"> How to manage VTK object connections ?</a></li>
</ul>

---
