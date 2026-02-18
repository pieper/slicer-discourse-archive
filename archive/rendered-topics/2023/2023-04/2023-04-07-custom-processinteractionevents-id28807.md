# Custom processInteractionEvents

**Topic ID**: 28807
**Date**: 2023-04-07
**URL**: https://discourse.slicer.org/t/custom-processinteractionevents/28807

---

## Post #1 by @DRDMT (2023-04-07 22:28 UTC)

<p>Hello Team,</p>
<p>Kindly wanted to know from where is the function “processInteractionEvents()” triggered?  How can we use this function in our custom module to capture mouse move event?</p>
<p>Regards</p>

---

## Post #2 by @lassoan (2023-04-07 22:29 UTC)

<p>Probably triggering <code>processInteractionEvents</code> would not be a good solution.<br>
Could you describe what you would like to achieve?</p>

---

## Post #3 by @DRDMT (2023-04-09 19:44 UTC)

<p>Hello Andras Lasso Sir,</p>
<p>I am trying to include VTKWidget and MRML subdirectories in my loadable module. Also in the the vtkSlicerWidget’s processInteractionEvent want to capture the mousemove event to get information of the coordinates of the mouse in the view.  Say red view for now.</p>
<p>I am facing two main issues -</p>
<ol>
<li>I am unable to build once I create these folders and files using cmake</li>
</ol>
<p>The error I get is</p>
<pre><code class="lang-auto">---------------------------------------------
LNK1104	cannot open file '..\lib\Slicer-5.3\qt-loadable-modules\Debug\vtkSlicer&lt;MyModule&gt;ModuleMRML.lib'	qSlicer&lt;MyModule&gt;Module	C:\&lt;path to MyModule&gt;\LINK	1
--------------------------------------------------------------------------
MSB8066	Custom build for 'C:\&lt;Path&gt;\build\CMakeFiles\xyz56\vtkSlicer&lt;My Module&gt;ModuleVTKWidgetsHierarchy.stamp.txt.rule;C:\&lt;Path To MY Module&gt;\VTKWidgets\CMakeLists.txt' exited with code 1.	vtkSlicer&lt;MY Module&gt;ModuleVTKWidgets	C:\&lt;path&gt;VC\v170\Microsoft.CppCommon.targets	247	
--------------------------------------------------------------------
</code></pre>
<ol start="2">
<li>Locate the code from where processInteractionEvent gets triggered ( say from vtkMRMLAbstractWidget)</li>
</ol>
<p>Kindly looking forward to your support.</p>
<p>Regards</p>

---

## Post #4 by @lassoan (2023-04-10 01:56 UTC)

<p>If you just want to get the mouse cursor position then you <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-current-mouse-coordinates-in-a-slice-view">can observe the crosshair node</a>.</p>
<p>If you want to interactively collect mouse clicks then I would recommend to use markups module. You can create a markup node, activate/deactivate placement, etc. and observe the node changes. These are all quite straightforward, high-level operations, mostly just working with MRML nodes.</p>

---

## Post #5 by @DRDMT (2023-04-10 14:23 UTC)

<p>Hello Andras Lasso Sir,</p>
<p>Thank you.  Will also lookinto that, but to work with MRML nodes in c++ we would need to add MRML folder right? However, when I do that.  I am getting the below error:</p>
<pre><code class="lang-auto">---------------------------------------------
LNK1104	cannot open file '..\lib\Slicer-5.3\qt-loadable-modules\Debug\vtkSlicer&lt;MyModule&gt;ModuleMRML.lib'	qSlicer&lt;MyModule&gt;Module	C:\&lt;path to MyModule&gt;\LINK	1
--------------------------------------------------------------------------
MSB8066	Custom build for 'C:\&lt;Path&gt;\build\CMakeFiles\xyz56\vtkSlicer&lt;My Module&gt;ModuleVTKWidgetsHierarchy.stamp.txt.rule;C:\&lt;Path To MY Module&gt;\VTKWidgets\CMakeLists.txt' exited with code 1.	vtkSlicer&lt;MY Module&gt;ModuleVTKWidgets	C:\&lt;path&gt;VC\v170\Microsoft.CppCommon.targets	247	
--------------------------------------------------------------------
</code></pre>
<p>How can we solve this?</p>
<p>Regards</p>

---

## Post #6 by @lassoan (2023-04-11 04:46 UTC)

<p>I would recommend to look at how similar modules in implemented in other extensions. The list of all extensions and their github repository URL is available in the <a href="https://github.com/Slicer/ExtensionsIndex">Extensions Index</a>.</p>

---
