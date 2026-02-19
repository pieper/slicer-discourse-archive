---
topic_id: 15375
title: "Improving The Exposure Of Vtkslicermodulelogic S To Other Co"
date: 2021-01-06
url: https://discourse.slicer.org/t/15375
---

# Improving the exposure of `vtkSlicerModuleLogic`s to other components

**Topic ID**: 15375
**Date**: 2021-01-06
**URL**: https://discourse.slicer.org/t/improving-the-exposure-of-vtkslicermodulelogic-s-to-other-components/15375

---

## Post #1 by @RafaelPalomar (2021-01-06 11:18 UTC)

<p>The purpose of this post is to frame the discussion around improving the exposure of <code>vtkSlicerModuleLogic</code>s to other Slicer components (e.g., displayable managers). After having a look at the code, my understanding of the <strong>current situation</strong> is as follows:</p>
<ul>
<li>Each <code>vtkSlicerModuleLogic</code> is created and kept by its corresponding <code>qSlicerModule</code>, as a member variable.</li>
<li>A logic object can be obtained by the <code>qSlicerAbstractCoreModule::logic()</code> method or <code>qSlicerAbstractModuleRepresentation::logic()</code> (for module widgets).</li>
<li>
<code>vtkSlicerModuleLogic</code>s are very flexible components and it is desirable that they can be more easily exposed to other components (possibly in other modules).</li>
</ul>
<p>The <strong>plan for improving</strong> the exposure of  <code>vtkSlicerModuleLogic</code>s could be as follows:</p>
<ul>
<li>Keeping an association between <code>qSlicerModule</code>s and <code>vtkSlicerModuleLogic</code>s in <strong><code>vtkMRMLApplicationLogic</code></strong>, which is a more reachable component.</li>
<li>Remove <code>qSlicerAbstractCoreModule::logic()</code> and <code>qSlicerAbstractModuleRepresentation::logic()</code>. For consistency, the only way to access the module logics will be <code>vtkMRMLApplicationLogic::GetModuleLogic(const char* moduleName)</code>.</li>
<li>Lifecycle of <code>vtkSlicerModuleLogic</code>s will still be managed by <code>qSlicerModule</code>s. There will be only 1 logic per module.</li>
</ul>
<p><a class="mention" href="/u/lassoan">@lassoan</a>, <a class="mention" href="/u/jcfr">@jcfr</a>, <a class="mention" href="/u/pieper">@pieper</a>, does it look to you like a  good course of action?</p>

---

## Post #2 by @jcfr (2021-01-06 13:56 UTC)

<p>Thanks for working on this and for the detailed summary. Beside of one nitpick outlined below, it all makes sense.</p>
<blockquote>
<ul>
<li>Remove <code>qSlicerAbstractCoreModule::logic()</code> and <code>qSlicerAbstractModuleRepresentation::logic()</code> . For consistency, the only way to access the module logics will be <code>vtkMRMLApplicationLogic::GetModuleLogic(const char* moduleName)</code> .</li>
</ul>
</blockquote>
<p>I suggest we keep these.</p>
<p>The use of <code>vtkMRMLApplicationLogic::GetModuleLogic(const char* moduleName)</code> should be considered to access module logic from displayable managers/application code/scripts.</p>
<p>And I still think a module <code>Foo</code> should still access <code>FooLogic</code> using the existing accessors.</p>

---

## Post #3 by @pieper (2021-01-07 21:33 UTC)

<p>Yes, we shouldn’t remove the old API or we could break extensions.  But having this extra non-gui method to access the logics sounds great.</p>

---
