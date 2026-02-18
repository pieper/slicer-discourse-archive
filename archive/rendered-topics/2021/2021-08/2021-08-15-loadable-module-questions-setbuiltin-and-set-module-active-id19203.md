# Loadable module questions: `setBuiltIn()` and set module active

**Topic ID**: 19203
**Date**: 2021-08-15
**URL**: https://discourse.slicer.org/t/loadable-module-questions-setbuiltin-and-set-module-active/19203

---

## Post #1 by @keri (2021-08-15 17:09 UTC)

<p>Hi,</p>
<p>I’m becoming familiar with creating loadable modules.</p>
<p>I write some module and I think it should be built in. I can see that there is a method <code>setBuiltIn()</code> that is provided by <code>qSlicerLoadableModule</code>. I tried to:</p>
<pre><code class="lang-cpp">qSlicerStackLoadModule::qSlicerStackLoadModule(QObject* _parent)
  : Superclass(_parent)
  , d_ptr(new qSlicerStackLoadModulePrivate)
{
  setBuiltIn(true);
}
</code></pre>
<p>but can’t understand what that brings up. What <code>setBuiltIn(true)</code> changes?</p>
<p>Also how to programmatically set some module active? i.e. display my module in Slicer app’s module tab via C++ when some signal is emited.</p>

---

## Post #2 by @lassoan (2021-08-16 05:34 UTC)

<p>The built-in property is set when the module is loaded, <a href="https://github.com/Slicer/Slicer/blob/0094e9a35bd266cc8b0e677858dabce797c9928f/Base/Logic/vtkSlicerApplicationLogic.cxx#L780-L819">based on its location in the install tree</a>. The value is not expected to change, therefore if you change it then it will be ignored at most places, but the inconsistency between the initial and current value may cause some issues. If you want to add a “built-in” module then you need to add it to Slicer in your <a href="https://blog.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/">custom application</a> and not install it as an extension. Modules that are in extensions bundled with the custom application probably show up as built-in, too.</p>

---

## Post #3 by @lassoan (2021-08-16 14:49 UTC)

<p>2 posts were split to a new topic: <a href="/t/how-to-initialize-module-widget-at-application-startup/19211">How to initialize module widget at application startup</a></p>

---
