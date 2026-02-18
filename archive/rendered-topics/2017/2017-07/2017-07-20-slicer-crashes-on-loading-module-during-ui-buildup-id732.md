# Slicer crashes on loading module (during UI buildup)

**Topic ID**: 732
**Date**: 2017-07-20
**URL**: https://discourse.slicer.org/t/slicer-crashes-on-loading-module-during-ui-buildup/732

---

## Post #1 by @mschwier (2017-07-20 19:56 UTC)

<p>Operating system: Windows 10, 64 Bit<br>
Slicer version:4.7.0-2017-07-07<br>
Expected behavior: Show module UI<br>
Actual behavior: Slicer crashes</p>
<p>Hi together, I am pretty new to Slicer (just started to work with Andrey Fedorov) and currently looking into the T1Mapping Extension ([<a href="https://github.com/QIICR/T1Mapping/tree/master/T1Mapping" rel="nofollow noopener">https://github.com/QIICR/T1Mapping/tree/master/T1Mapping</a>]). After it compiled fine it unfortunately crashes as soon as I try to load the module (select it under “All Modules”). I tracked the crash until “qSlicerCLIModuleUIHelper::updateUi” and from there it goes into “ButtonGroupWidgetWrapper::checkedValue()” for the IO parameter “modelName” which is a string-enumeration. Inside “ButtonGroupWidgetWrapper::checkedValue()” the call to “this-&gt;ButtonGroup-&gt;checkedButton()” returns a NULL pointer which causes the following assert to fail and crash the app.</p>
<p>I cannot figure out what is wrong. The T1Mapping source code is unaltered. I did notice that the string-enumeration did not declare a default, which I thought could be a problem, but adding a default in the xml didn’t change anything.</p>
<p>I would be happy if someone has an idea what could be wrong.</p>
<p>Michael</p>

---

## Post #2 by @ihnorton (2017-07-20 20:11 UTC)

<p>The simple fix is to set a <code>&lt;default&gt;</code> element for the modelName <code>string-enumeration</code>. The correct fix for Slicer core is probably to remove <a href="https://github.com/Slicer/Slicer/blob/dfe8e7e0da17ecf56ba965b6a592738085dfd608/Base/QTCLI/qSlicerCLIModuleUIHelper.cxx#L140">this assert</a>, because returning NULL is part of the buttongroup interface. Try this patch:</p>
<pre><code class="lang-auto">diff --git a/Base/QTCLI/qSlicerCLIModuleUIHelper.cxx b/Base/QTCLI/qSlicerCLIModuleUIHelper.cxx
index 651163024..5f3bb93c7 100644
--- a/Base/QTCLI/qSlicerCLIModuleUIHelper.cxx
+++ b/Base/QTCLI/qSlicerCLIModuleUIHelper.cxx
@@ -137,8 +137,11 @@ QButtonGroup* ButtonGroupWidgetWrapper::buttonGroup()const
 QString ButtonGroupWidgetWrapper::checkedValue()
 {
   QAbstractButton* button = this-&gt;ButtonGroup-&gt;checkedButton();
-  Q_ASSERT(button);
-  return button-&gt;text();
+
+  if (button)
+    return button-&gt;text();
+  else
+    return QString("");
 }

 //-----------------------------------------------------------------------------
</code></pre>

---

## Post #3 by @mschwier (2017-07-20 20:35 UTC)

<p>Thank you for the answer. It works now! I actually had tried to add the <code>&lt;default&gt;</code> element before, but only build the solution, while it apparently required a complete re-build to make the changes in the xml take effect.</p>

---

## Post #4 by @ihnorton (2017-07-20 20:36 UTC)

<p>If you want to submit that patch for your first PR to Slicer, please go for it. (also, hi neighbor <img src="https://emoji.discourse-cdn.com/twitter/wave.png?v=5" title=":wave:" class="emoji" alt=":wave:">)</p>

---

## Post #5 by @mschwier (2017-07-21 12:06 UTC)

<p>OK, I’ll try to do that, good exercise, thx <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---
