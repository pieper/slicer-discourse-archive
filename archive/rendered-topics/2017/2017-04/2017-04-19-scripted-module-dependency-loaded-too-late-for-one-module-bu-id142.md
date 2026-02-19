---
topic_id: 142
title: "Scripted Module Dependency Loaded Too Late For One Module Bu"
date: 2017-04-19
url: https://discourse.slicer.org/t/142
---

# Scripted module dependency loaded too late for one module but for another one not

**Topic ID**: 142
**Date**: 2017-04-19
**URL**: https://discourse.slicer.org/t/scripted-module-dependency-loaded-too-late-for-one-module-but-for-another-one-not/142

---

## Post #1 by @jcfr (2017-04-19 00:34 UTC)

<p>From: Christian Herz / <a href="http://slicer-devel.65872.n3.nabble.com/Scripted-module-dependency-loaded-too-late-for-one-module-but-for-another-one-not-tt4038485.html">http://slicer-devel.65872.n3.nabble.com/Scripted-module-dependency-loaded-too-late-for-one-module-but-for-another-one-not-tt4038485.html</a></p>
<p>Hi developers,</p>
<p>I noticed that there is something wrong with the order of when which dependency is loaded. It’s either a problem with my extensions or Slicer. Not sure about this.</p>
<p>We have a module Quantitative Reporting [1] which depends (not much longer) on SlicerProstate [2]. I have been working on factoring out some code into another repository and I noticed that the dependency is loaded to late into Slicer (even when I compile the python scripted module).</p>
<p>Here an example for reproduction:</p>
<ol>
<li>
<p>Execute the following in a directory that you want to use for testing this issue:</p>
<pre><code class="lang-auto">git clone https://github.com/QIICR/QuantitativeReporting.git
git clone https://github.com/SlicerProstate/mpReview.git
git clone https://github.com/SlicerProstate/SlicerProstate.git
</code></pre>
</li>
<li>
<p>Add the top-level directory of QuantitativeReporting to your current Slicer</p>
</li>
<li>
<p>Compile SlicerProstate</p>
</li>
<li>
<p>Add the <code>{SlicerProstate_Build_Directory}/lib/Slicer4.7/qt-scripted-modules</code></p>
</li>
<li>
<p>Restart Slicer</p>
</li>
</ol>
<p>—&gt; Everything should be fine. No errors visible in python console</p>
<p>Now try this:</p>
<ol>
<li>Delete <code>{SlicerProstate_Build_Directory}/lib/Slicer4.7/qt-scripted-modules</code> or delete <code>DistanceMapBasedRegistration.py</code> and skip steps 2-5.</li>
<li>Open CMakeLists.txt in toplevel directory of SlicerProstate for editing</li>
<li>Delete the following lines 21-24:</li>
</ol>
<pre><code class="lang-auto">add_subdirectory(QuadEdgeSurfaceMesher) 
add_subdirectory(SegmentationSmoothing) 
add_subdirectory(DistanceMapBasedRegistration) 
add_subdirectory(DWModeling)
</code></pre>
<ol start="4">
<li>Compile SlicerProstate</li>
<li>Add the <code>{SlicerProstate_Build_Directory}/lib/Slicer4.7/qt-scripted-modules</code>
</li>
<li>Restart Slicer</li>
</ol>
<pre><code class="lang-auto">&gt;&gt;&gt; Traceback (most recent call last):
File "&lt;string&gt;", line 1, in &lt;module&gt;
File "/Users/christian/sources/py/Reporting/QuantitativeReporting.py", line 8, in &lt;module&gt;
from SlicerProstateUtils.mixins import *
ImportError: No module named SlicerProstateUtils.mixins
</code></pre>
<p>When I add mpReview[3] (both depend on SlicerProstate) I only get errors from QuantitativeReporting but not form mpReview displayed.</p>
<p>I am not sure about the cause, but I assume that the cause why it’s is properly loaded in the first scenario is that <a href="http://DistanceMapBasedRegistration.py">DistanceMapBasedRegistration.py</a> coexists next to <a href="http://SlicerProstate.py">SlicerProstate.py</a>.</p>
<p>Hope someone can help me with that issue.</p>
<p>Thanks,<br>
Christian</p>
<p>[1] <a href="https://github.com/QIICR/QuantitativeReporting">https://github.com/QIICR/QuantitativeReporting</a><br>
[2] <a href="https://github.com/SlicerProstate/SlicerProstate">https://github.com/SlicerProstate/SlicerProstate</a><br>
[3] <a href="https://github.com/SlicerProstate/mpReview">https://github.com/SlicerProstate/mpReview</a></p>

---

## Post #2 by @fedorov (2017-04-19 17:50 UTC)

<p><a class="mention" href="/u/che85">@che85</a> wow, I have to say I had to re-read this many times!</p>
<p>I don’t know what’s going on, but maybe the problem can be narrowed down a bit better:</p>
<ul>
<li>
<p>I think it would be more consistent (and that is how the factories work) to build each of the extensions, and add paths to the built directories for all of the modules</p>
</li>
<li>
<p>can you reproduce the problem if you just take SlicerProstate, and then try to import from python console SlicerProstateUtils.mixins first compiling SlicerProstate with DistanceMapRegistration “added”, and then cleaning it up and building it without that directory?</p>
</li>
</ul>
<p>It is a bit difficult to follow because of many pieces involved.</p>

---

## Post #3 by @che85 (2017-04-19 18:07 UTC)

<p>I thought about this to, but this would make it even more complicated, right?</p>
<p>I don’t know how dependencies are resolved right now when starting Slicer, but when there is a dependency defined for a module and the dependency hasn’t been loaded yet, the load process of that module should be moved to the end of the list for modules that need to be loaded. In the end if the dependency still couldn’t be resolved, it should simply throw an error.</p>
<p>Maybe JC can tell us more about that loading process?</p>
<blockquote>
<p>I think it would be more consistent (and that is how the factories work) to build each of the extensions, and add paths to the built directories for all of the modules</p>
</blockquote>
<p>Loading SlicerProstateUtils.mixins from the python console works in any case.</p>
<blockquote>
<p>can you reproduce the problem if you just take SlicerProstate, and then try to import from python console SlicerProstateUtils.mixins first compiling SlicerProstate with DistanceMapRegistration “added”, and then cleaning it up and building it without that directory?</p>
</blockquote>

---

## Post #4 by @che85 (2017-04-19 18:49 UTC)

<p>Ok here a quick update for simpler reproduction. Thanks to <a class="mention" href="/u/fedorov">@fedorov</a>:</p>
<ol>
<li>
<p>Download and install Slicer nightly build from <a href="http://download.slicer.org/" rel="nofollow noopener">http://download.slicer.org/</a></p>
</li>
<li>
<p>Open Extension Manager</p>
</li>
<li>
<p>Install extensions <strong>Quantitative</strong> Reporting and <strong>mpReview</strong></p>
</li>
<li>
<p>Restart Slicer<br>
When you open the Python console, <strong>no errors</strong> should be displayed.</p>
</li>
<li>
<p>Go to directory  {Slicer_Install_DIR}/Extensions-#####/SlicerProstate/lib/Slicer4.7/qt-scripted-modules extension</p>
</li>
<li>
<p>Delete <a href="http://DistanceMapBasedRegistration.py" rel="nofollow noopener">DistanceMapBasedRegistration.py</a> and DistanceMapBasedRegistration.pyc</p>
</li>
<li>
<p>Restart Slicer<br>
<strong>Notice the error in the python console</strong></p>
</li>
</ol>

---

## Post #5 by @ihnorton (2017-04-20 15:19 UTC)

<p><a class="mention" href="/u/che85">@che85</a> there are multiple stages in the module initialization process: registration, instantiation, and loading. Instantiation is when the scripted module is parsed, so any <code>import</code> dependencies must be resolveable at that time. However, instantiation is done alphabetically, with no dependency resolution – because the module factory does not know anything about dependencies (the module itself supplies the <code>dependencies</code> function).  QuantitativeReporting works “by accident” when you have DistanceMapBasedRegistration in place because DMBR is in the same directory where SlicerProstateUtils is installed, so that the parent directory is added to PYTHONPATH before attempting to instantiate QuantitativeReporting (During instantiation, the path for each module is <a href="https://github.com/Slicer/Slicer/blob/master/Base/QTGUI/qSlicerScriptedLoadableModuleFactory.cxx#L49-L87">added to PYTHONPATH</a>). When you remove it, SlicerProstate comes later alphabetically, so the path is not available when QR is instantiated – as <a class="mention" href="/u/fedorov">@fedorov</a> noted, the import works fine in the python console once Slicer starts.</p>
<p>Anyway, there’s probably a few ways this could be fixed, including:</p>
<ul>
<li>add all the additionalModulePaths to PYTHONPATH (not sure what this would break, there’s a lot of existing logic for adding to PYTHONPATH in various places, including for regular loadable modules).</li>
<li>add the path during registration rather than instantiation (simplest fix I can think of). Try this patch:</li>
</ul>
<details>
<summary>
patch to test</summary>
<pre><code class="lang-auto">diff --git a/Base/QTGUI/qSlicerScriptedLoadableModuleFactory.cxx b/Base/QTGUI/qSlicerScriptedLoadableModuleFactory.cxx
index 9ca65a503..939160247 100644
--- a/Base/QTGUI/qSlicerScriptedLoadableModuleFactory.cxx
+++ b/Base/QTGUI/qSlicerScriptedLoadableModuleFactory.cxx
@@ -43,6 +43,24 @@
 //----------------------------------------------------------------------------
 bool ctkFactoryScriptedItem::load()
 {
+#ifdef Slicer_USE_PYTHONQT
+  if (!qSlicerCoreApplication::testAttribute(qSlicerCoreApplication::AA_DisablePython))
+    {
+    // By convention, if the module is not embedded, "&lt;MODULEPATH&gt;" will be appended to PYTHONPATH
+    if (!qSlicerCoreApplication::application()-&gt;isEmbeddedModule(this-&gt;path()))
+      {
+      QDir modulePathWithoutIntDir = QFileInfo(this-&gt;path()).dir();
+      QString intDir = qSlicerCoreApplication::application()-&gt;intDir();
+      if (intDir ==  modulePathWithoutIntDir.dirName())
+        {
+        modulePathWithoutIntDir.cdUp();
+        }
+      qSlicerCorePythonManager * pythonManager = qSlicerCoreApplication::application()-&gt;corePythonManager();
+      pythonManager-&gt;appendPythonPaths(QStringList() &lt;&lt; modulePathWithoutIntDir.absolutePath());
+      }
+    }
+#endif
+
   return true;
 }

@@ -59,24 +77,6 @@ qSlicerAbstractCoreModule* ctkFactoryScriptedItem::instanciator()
   module-&gt;setInstalled(qSlicerUtils::isPluginInstalled(this-&gt;path(), app-&gt;slicerHome()));
   module-&gt;setBuiltIn(qSlicerUtils::isPluginBuiltIn(this-&gt;path(), app-&gt;slicerHome()));

-#ifdef Slicer_USE_PYTHONQT
-  if (!qSlicerCoreApplication::testAttribute(qSlicerCoreApplication::AA_DisablePython))
-    {
-    // By convention, if the module is not embedded, "&lt;MODULEPATH&gt;" will be appended to PYTHONPATH
-    if (!qSlicerCoreApplication::application()-&gt;isEmbeddedModule(module-&gt;path()))
-      {
-      QDir modulePathWithoutIntDir = QFileInfo(module-&gt;path()).dir();
-      QString intDir = qSlicerCoreApplication::application()-&gt;intDir();
-      if (intDir ==  modulePathWithoutIntDir.dirName())
-        {
-        modulePathWithoutIntDir.cdUp();
-        }
-      qSlicerCorePythonManager * pythonManager = qSlicerCoreApplication::application()-&gt;corePythonManager();
-      pythonManager-&gt;appendPythonPaths(QStringList() &lt;&lt; modulePathWithoutIntDir.absolutePath());
-      }
-    }
-#endif
-
   bool ret = module-&gt;setPythonSource(this-&gt;path());
   if (!ret)
     {
</code></pre>
</details>
<p>Related:<br>
<a href="http://www.na-mic.org/Bug/view.php?id=4242" class="onebox" target="_blank">http://www.na-mic.org/Bug/view.php?id=4242</a><br>
<a href="http://www.na-mic.org/Bug/view.php?id=4051" class="onebox" target="_blank">http://www.na-mic.org/Bug/view.php?id=4051</a></p>

---

## Post #6 by @che85 (2017-04-20 21:50 UTC)

<p><a class="mention" href="/u/ihnorton">@ihnorton</a>, <a class="mention" href="/u/fedorov">@fedorov</a> I applied the patch and compiled Slicer under Ubuntu and indeed it works! I don’t get those errors anymore. When can I expect this to be available in the nightly?</p>
<p>Thanks a lot.<br>
Christian</p>

---

## Post #7 by @jcfr (2017-04-20 22:17 UTC)

<p><a class="mention" href="/u/ihnorton">@ihnorton</a> Good catch. Moving the update of python path at load time makes sense.</p>

---

## Post #8 by @ihnorton (2017-04-21 02:43 UTC)

<p>Since I got <img src="https://emoji.discourse-cdn.com/twitter/thumbsup.png?v=5" title=":thumbsup:" class="emoji" alt=":thumbsup:"> from Jc I’ll commit tomorrow if there’s no objection.</p>
<p><a href="https://github.com/Slicer/Slicer/pull/705" class="onebox" target="_blank">https://github.com/Slicer/Slicer/pull/705</a></p>

---
