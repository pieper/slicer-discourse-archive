# Debug Build errors 

**Topic ID**: 28961
**Date**: 2023-04-17
**URL**: https://discourse.slicer.org/t/debug-build-errors/28961

---

## Post #1 by @DRDMT (2023-04-17 13:02 UTC)

<p>Hello Team,<br>
How can we debug or find more information about the error messages created while building a module.<br>
I am just trying to create a new node.  When ever I call a New() method I get the error below:</p>
<pre><code class="lang-auto">6&gt;vtkSlicer&lt;Module&gt;Logic.cxx
6&gt;   Creating library C:/D/SE/&lt;Extension&gt;/build/lib/Slicer-5.3/qt-loadable-modules/Debug/vtkSlicer&lt;Module&gt;ModuleLogic.lib and object C:/D/SE/&lt;Extension&gt;/build/lib/Slicer-5.3/qt-loadable-modules/Debug/vtkSlicer&lt;Module&gt;ModuleLogic.exp
6&gt;vtkSlicer&lt;Module&gt;Logic.obj : error LNK2019: unresolved external symbol "__declspec(dllimport) public: static class vtkMRML&lt;Module&gt;Node * __cdecl vtkMRML&lt;Module&gt;Node::New(void)" (__imp_?New@vtkMRML&lt;Module&gt;Node@@SAPEAV1@XZ) referenced in function "protected: virtual void __cdecl vtkSlicer&lt;Module&gt;Logic::RegisterNodes(void)" (?RegisterNodes@vtkSlicer&lt;Module&gt;Logic@@MEAAXXZ)
6&gt;  Hint on symbols that are defined and could potentially match:
6&gt;    "__declspec(dllimport) public: static class vtkIntArray * __cdecl vtkIntArray::New(void)" (__imp_?New@vtkIntArray@@SAPEAV1@XZ)
6&gt;C:\D\SE\&lt;Extension&gt;\build\lib\Slicer-5.3\qt-loadable-modules\Debug\vtkSlicer&lt;Module&gt;ModuleLogic.dll : fatal error LNK1120: 1 unresolved externals
6&gt;Done building project "vtkSlicer&lt;Module&gt;ModuleLogic.vcxproj" -- FAILED.
</code></pre>
<p>Regards</p>

---

## Post #2 by @lassoan (2023-04-17 13:04 UTC)

<p>It seems that in the CMakeLists.txt you missed listing the library that provides the <code>vtkMRML&lt;Module&gt;Node</code> node. Follow the example of modules that register new node types.</p>

---

## Post #3 by @DRDMT (2023-04-17 19:19 UTC)

<p>Kindly could you give a link of one such module.  Also this is the CMakeLists.txt file in MRML folder right?</p>

---

## Post #4 by @lassoan (2023-04-17 19:20 UTC)

<p>Most modules are like that. Search for <code>RegisterNodes</code>.</p>

---
