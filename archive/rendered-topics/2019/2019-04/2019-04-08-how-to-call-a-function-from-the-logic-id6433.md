# How to call a function from the logic

**Topic ID**: 6433
**Date**: 2019-04-08
**URL**: https://discourse.slicer.org/t/how-to-call-a-function-from-the-logic/6433

---

## Post #1 by @siaeleni (2019-04-08 15:46 UTC)

<p>Hello,</p>
<p>I was wondering how can I call correctly a function that is in the ModuleNameLogic inherited by ScriptedLoadableModuleLogic in python?<br>
Currently, I try the following with no success:</p>
<pre><code class="lang-auto">slicer.modules.moduleName.logic().Test()
</code></pre>
<p>My current code seems like the following and I want to call from Python Interactor the Test() method:</p>
<pre><code class="lang-auto">&gt; class ModuleName(ScriptedLoadableModule):
&gt;     def __init__(self, parent):
&gt;     ScriptedLoadableModule.__init__(self, parent)
&gt; 
&gt; 
&gt; class ModuleNameWidget(ScriptedLoadableModuleWidget):
&gt;   
&gt;   def setup(self):
&gt;     ScriptedLoadableModuleWidget.setup(self)
&gt; 
&gt; 
&gt; class ModuleNameLogic(ScriptedLoadableModuleLogic):
&gt;   
&gt;   def Test(self):
&gt;     print("Test is called")
&gt;     pass
</code></pre>
<p>Thanks for your help</p>

---

## Post #2 by @pieper (2019-04-08 20:03 UTC)

<p>Hi <a class="mention" href="/u/siaeleni">@siaeleni</a> -</p>
<p>You should be able to do:</p>
<pre><code class="lang-auto">ModuleNameLogic().Test()
</code></pre>
<p>if you are in a different module file or in the python interactor you might need to call <code>import ModuleName</code> first.</p>
<p>(As an aside, the other ‘logic’ class <code>slicer.modules.moduleName.logic</code> is actually the C++ loadable module instance corresponding to the scripted module, but it’s really just an internal structure and doesn’t have any particular utility here).</p>
<p>-Steve</p>

---

## Post #3 by @lassoan (2019-04-08 20:29 UTC)

<p>I usually create a single logic instance in the widget that I can access via the widget class:</p>
<pre><code>slicer.modules.screencapture.widgetRepresentation().self().logic
</code></pre>
<p>Should we update updating the scripted module template to create a logic instance in the widget’s constructor instead of creating a new logic instance each time? This would make the Python and C++ modules a bit more consistent.</p>

---

## Post #4 by @siaeleni (2019-04-09 15:15 UTC)

<p>I created an instance and use that to access to the logic methods.Thanks a lot!</p>

---
