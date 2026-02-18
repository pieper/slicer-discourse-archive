# Texts module does not observe changed nodes

**Topic ID**: 12533
**Date**: 2020-07-14
**URL**: https://discourse.slicer.org/t/texts-module-does-not-observe-changed-nodes/12533

---

## Post #1 by @joachim (2020-07-14 14:39 UTC)

<p>I’m working on <a href="https://discourse.slicer.org/t/text-annotations/11558/18">adding Markdown and HTML support</a> for the <em>Texts</em> module. This module works on <code>vtkMRMLTextNode</code> nodes. If I change such a node outside the <em>Texts</em> module GUI by adding an attribute using the <em>Data</em> module or programmatically, the changes are not reflected in <code>qMRMLTextWidget</code>; the function <code>qMRMLTextWidget::updateWidgetFromMRML()</code> is never called. Is this a bug?</p>
<p><code>vtkMRMLNode::SetAttribute()</code> should fire a <code>ModifiedEvent</code> according to documentation. But how do <code>qSlicerTextsModuleWidget</code> and <code>qMRMLTextWidget</code> observe these events?</p>

---

## Post #2 by @Sunderlandkyl (2020-07-14 14:49 UTC)

<p>qMRMLTextWidget currently only observers TextModifiedEvent (<a href="https://github.com/Slicer/Slicer/blob/73ca5332aeeee92f8b8ad015f3a03ee8d50c0b99/Modules/Loadable/Texts/Widgets/qMRMLTextWidget.cxx#L147" rel="nofollow noopener">https://github.com/Slicer/Slicer/blob/73ca5332aeeee92f8b8ad015f3a03ee8d50c0b99/Modules/Loadable/Texts/Widgets/qMRMLTextWidget.cxx#L147</a>).</p>
<p>If you change <code>vtkMRMLTextNode::TextModifiedEvent</code> to <code>vtkCommand::ModifiedEvent</code> it should observe the other changes.</p>

---

## Post #3 by @joachim (2020-07-14 15:03 UTC)

<p>Thank you! I’ll take a look at the <code>QVTK_OBJECT</code> macro.</p>

---
