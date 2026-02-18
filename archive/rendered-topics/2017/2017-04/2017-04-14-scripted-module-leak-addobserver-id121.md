# Scripted Module Leak - Addobserver

**Topic ID**: 121
**Date**: 2017-04-14
**URL**: https://discourse.slicer.org/t/scripted-module-leak-addobserver/121

---

## Post #1 by @DanC (2017-04-14 19:20 UTC)

<p>Hi all.<br>
My scripted module is giving me vtkDebugLeaks on termination of the Slicer Program.<br>
It happens when I add an observer.</p>
<p>slicer.mrmlScene.AddObserver(“ModifiedEvent”, self.sliceModifiedCallback)</p>
<p>Is there a way to remove the observer upon program close?<br>
Thanks!</p>

---

## Post #2 by @Johan_Andruejol (2017-04-14 19:35 UTC)

<p>Hello Dan,</p>
<p>You can remove an observer by using its tag. You get the tag when you add the observer <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#How_can_I_access_callData_argument_in_a_VTK_object_observer_callback_function" rel="nofollow noopener"><code>[1]</code></a>.<br>
For example:<br>
<code>self.observerTag = slicer.mrmlScene.AddObserver(vtk.vtkCommand.ModifiedEvent, self.sliceModifiedCallback)</code></p>
<p>You can then remove the observation by doing:<br>
<code>slicer.mrmlScene.RemoveObserver(self.example)</code>.</p>
<p>If you have a lot of events to observe, I would suggest that you take a look at the <a href="https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/util.py#L690" rel="nofollow noopener"><code>VTKObservationMixin</code></a>. This should make it easier for you.</p>
<p>Thanks !<br>
Johan<br>
[1]: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#How_can_I_access_callData_argument_in_a_VTK_object_observer_callback_function" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#How_can_I_access_callData_argument_in_a_VTK_object_observer_callback_function</a><br>
[2]: <a href="https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/util.py#L690" rel="nofollow noopener">https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/util.py#L690</a></p>

---

## Post #3 by @DanC (2017-04-14 19:42 UTC)

<p>Thanks for the reply Johan.<br>
I’ve actually seen that reference and was trying to figure out how to apply this to the module.</p>
<p>Is there a special method that will be called upon program close?<br>
Where should I place<br>
slicer.mrmlScene.RemoveObserver(self.observerTag )</p>
<p>Thanks.</p>

---

## Post #4 by @Johan_Andruejol (2017-04-14 20:19 UTC)

<p>DanC,</p>
<p>You could listen to the Qt signal sent by the <a href="https://github.com/Slicer/Slicer/blob/master/Base/QTCore/qSlicerModuleFactoryManager.h#L104" rel="nofollow noopener"><code>qSlicerModuleFactoryManager::moduleAboutToBeUnloaded(QString)</code></a>. This signal should be sent when the application closes.<br>
You can access the <code>qSlicerModuleFactoryManager</code> using the slicer application like so:<br>
<code>slicer.app.moduleManager().factoryManager()</code>.</p>
<p>Johan</p>

---

## Post #5 by @DanC (2017-04-14 20:42 UTC)

<p>Thanks.<br>
That solved the problem.</p>
<pre><code>moduleManager = slicer.app.moduleManager()
moduleManager.connect( 'moduleAboutToBeUnloaded(QString)', self.removeObserver )
</code></pre>
<p>def removeObserver(self):<br>
self.redRenderer.RemoveObserver(self.observerTag )</p>

---

## Post #6 by @lassoan (2017-04-14 21:59 UTC)

<p>Most often you remove observers in the cleanup() method of the module widget class. If you want to have observers only while the module is active then add observers in enter() and remove observers in exit() method of the widget class.</p>
<p>You can also use <a href="https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/util.py#L690">VTKObservationMixin</a>, which makes adding observation simpler and automatically removes all observers when the owner class is deleted. See for example <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/SegmentEditor/SegmentEditor.py">Segment editor module</a> and <a href="https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/tests/test_slicer_util_VTKObservationMixin.py">VTKObservationMixin tests</a>.</p>

---
