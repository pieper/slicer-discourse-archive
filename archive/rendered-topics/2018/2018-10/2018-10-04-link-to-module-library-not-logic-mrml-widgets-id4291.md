# Link to module library (not logic, mrml, widgets)

**Topic ID**: 4291
**Date**: 2018-10-04
**URL**: https://discourse.slicer.org/t/link-to-module-library-not-logic-mrml-widgets/4291

---

## Post #1 by @adamrankin (2018-10-04 23:15 UTC)

<p>Hello all,</p>
<p>Has anyone linked to a module library? I am trying to call a function in the public interface of the module class, and when I have</p>
<pre><code class="lang-auto">...
set(MODULE_TARGET_LIBRARIES
  vtkSlicer${MODULE_NAME}ModuleLogic
  qSlicerVirtualRealityModuleWidgets
  qSlicerVirtualRealityModule
  )
...
</code></pre>
<p>the <code>qSlicerVirtualRealityModule</code> target does not exist.</p>
<p>So, has anyone done something like this?</p>
<p>Cheers,<br>
Adam</p>

---

## Post #2 by @lassoan (2018-10-05 03:30 UTC)

<p>Targets listed in <code>Slicer_TARGETS</code> CMake variable are exported to the targets file <a href="https://github.com/Slicer/Slicer/blob/a335e39f30bdd75b7af7dd2b5b58b0ef68104e76/CMake/SlicerExtensionGenerateConfig.cmake#L114-L115">here</a>. Each library is added to <code>Slicer_TARGETS</code>, for example Qt libraries are added <a href="https://github.com/Slicer/Slicer/blob/a335e39f30bdd75b7af7dd2b5b58b0ef68104e76/CMake/SlicerMacroBuildModuleQtLibrary.cmake#L237">here</a>. Try to find out why module library target is not exported: is it not included in <code>Slicer_TARGETS</code>, or there are no exported symbols, …?</p>

---

## Post #3 by @adamrankin (2018-10-05 17:06 UTC)

<p>The library is exported (.lib file exists).</p>
<p>Adding the .lib file manually to the linker inputs results in a successful compile (dumpbin also shows symbol exists in exports).</p>
<p>Target does not exist in CMake, investigating CMake system now.</p>

---

## Post #4 by @adamrankin (2018-10-05 18:13 UTC)

<p>The following line exists in the Qt module macro</p>
<pre><code class="lang-auto">set_property(GLOBAL APPEND PROPERTY Slicer_TARGETS ${MODULEQTLIBRARY_NAME})
</code></pre>
<p>but is not present in the loadable module CMake.</p>
<p>Presumably this means it is not exported by design? Could it be exported?</p>
<p>Update: I have added the export line to the macro, and the target is included in the XYZTargets.cmake file (as expected).</p>
<p>Edit: compilation fails however, as it most likely has PRIVATE interface_libraries that should be public?</p>
<pre><code class="lang-auto">Severity	Code	Description	Project	File	Line	Suppression State
Error	LNK1181	cannot open input file 'qSlicerBaseQTCLI.lib'	vtkSlicerVideoPassthroughModuleLogic	C:\d\Slcr\SARR\VideoPassthrough\Logic\LINK	1	
Error	LNK1181	cannot open input file 'qSlicerBaseQTApp.lib'	qSlicerVideoPassthroughModule	C:\d\Slcr\SARR\VideoPassthrough\LINK	1	
Error	LNK1181	cannot open input file 'vtkAddonPythonD.lib'	vtkSlicerVideoPassthroughModuleLogicPythonD	C:\d\Slcr\SARR\VideoPassthrough\Logic\LINK	1	
Error	LNK1181	cannot open input file 'qSlicerBaseQTCLI.lib'	vtkSlicerVideoPassthroughModuleLogicPython	C:\d\Slcr\SARR\VideoPassthrough\Logic\LINK	1	
Error	LNK1181	cannot open input file 'vtkSlicerCamerasModuleLogic.lib'	qSlicerVideoPassthroughModuleGenericCxxTests	C:\d\Slcr\SARR\VideoPassthrough\LINK	1	
</code></pre>

---

## Post #5 by @lassoan (2018-10-05 18:18 UTC)

<p>I think it could make sense to make Qt module class (derived from qSlicerLoadableModule) available for other modules. Some features that require Qt and not related to the module widget are implemented in the module class and may be needed to be accessed from other modules.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> what do you think?</p>

---

## Post #6 by @adamrankin (2018-10-05 19:21 UTC)

<p>Talked to <a class="mention" href="/u/jcfr">@jcfr</a>, he suggested not to expose the module to protect the design decision of MRML/logic/widget reusability.</p>
<p>I will use a workaround to get the view via Qt methods (find by children by name/class) as the VR subsystem is a “special” snowflake.</p>

---

## Post #7 by @lassoan (2018-10-05 19:26 UTC)

<p>SlicerVirtualReality is not the only extension that uses module class for module-specific functions that may be useful for other modules. For example, Sequence Browser module uses the module class, too (for managing sequence browser toolbar). Any other logic that requires Qt but it should be available regardless of a module widget must live in the module class.</p>
<p>I agree that it is better if we don’t need to expose the module class, but only if we don’t need uglier workarounds to achieve what we need.</p>

---
