# Access widget class from the test class in a Slicer plugin

**Topic ID**: 11585
**Date**: 2020-05-17
**URL**: https://discourse.slicer.org/t/access-widget-class-from-the-test-class-in-a-slicer-plugin/11585

---

## Post #1 by @brhoom (2020-05-17 09:45 UTC)

<p>Dear all,</p>
<p>Is it possible to access a widget class element from the test class in a slicer plugin? I know this is not how the test class works but I am controlling the logic functions with an extra variable taht indicates if the call from the widget class or from the test class.</p>
<p>When I try this:</p>
<pre><code>class myClassTest(ScriptedLoadableModuleTest):
     def setUp(self):
           slicer.mrmlScene.Clear(0)   
           self.logic = myClassLogic()
           self.widg  = myClassWidget()
</code></pre>
<p>It creates a new instance of the widget instead of accessing the current widget.</p>

---

## Post #2 by @cpinter (2020-05-17 13:22 UTC)

<p>I don’t believe there is a direct way to access it from the test class but you can get it through the slicer module:</p>
<p><code>volumeRenderingWidget = slicer.modules.volumerendering.widgetRepresentation()</code></p>

---

## Post #3 by @brhoom (2020-05-18 16:31 UTC)

<p>Thanks for your quick answer.</p>

---

## Post #4 by @brhoom (2020-05-19 13:18 UTC)

<p>It seems the widget get new instance every time one click reload and test without destroying the old instance. This code gets the last instance:</p>
<p>In the widget class:</p>
<pre><code>    self.mainCollapsibleBtn = ctk.ctkCollapsibleButton()
    self.mainCollapsibleBtn.setWindowTitle("mainCollapsibleBtn")
</code></pre>
<p>In the test class:</p>
<pre><code>  widg   = slicer.modules.myModule.widgetRepresentation()
  wObjs = [x for x in widg.children()[1:] if x.windowTitle =="mainCollapsibleBtn"][-1].children()
  #getting the classes information
  for x in wObjs[1:]:
      print(x.className())
  #endfor x
</code></pre>
<p>By getting the classes information one can access the desirable class e.g.</p>
<pre><code>   myButton = wObjs[3]</code></pre>

---

## Post #5 by @lassoan (2020-05-19 23:41 UTC)

<aside class="quote no-group" data-username="brhoom" data-post="4" data-topic="11585">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/brhoom/48/1228_2.png" class="avatar"> brhoom:</div>
<blockquote>
<p>It seems the widget get new instance every time one click reload and test without destroying the old instance.</p>
</blockquote>
</aside>
<p>Slicer releases all references to the old widget, but if you keep references to it then it will not be destroyed. It is a debug/development feature anyway, so you don’t need worry about old widgets hanging around (if it becomes to confusing then just restart the application), but it makes sense to at least <a href="https://github.com/Slicer/Slicer/blob/a18612bb2584018822347ff4db16439b5c578e00/Utilities/Templates/Modules/Scripted/TemplateKey.py#L104-L108">remove all observers in the widget’s <code>cleanup()</code> method</a>.</p>
<p>By the way, you should never ever need to use <code>children()</code> or <code>findWidget</code> on your own module’s GUI. You have direct access to all widgets (something like <code>module.xyz.widgetRepresentation().self().ui.abcWidget</code>, if you follow the current Python scripted module template).</p>

---
