# Reload button loads dependent modules

**Topic ID**: 7135
**Date**: 2019-06-12
**URL**: https://discourse.slicer.org/t/reload-button-loads-dependent-modules/7135

---

## Post #1 by @brhoom (2019-06-12 10:31 UTC)

<p>It would be nice to have the feature in the title. My workaround is to modify the file</p>
<pre><code>  bin/python/slicer/ScriptedLoadableModule.py                               
</code></pre>
<p>and add these lines in onReload(self) function</p>
<pre><code>   myModules = ["myModules1","myModules2","myModules3"]
   if self.moduleName in myModules:
      print("Reloading myMainModule ............")
      slicer.util.reloadScriptedModule("myMainModule")
</code></pre>
<p>just before</p>
<pre><code>     slicer.util.reloadScriptedModule(self.moduleName)</code></pre>

---

## Post #2 by @lassoan (2019-06-12 13:56 UTC)

<p>If your module requires reloading of additional modules or packages then you can override onReload method in your module.</p>
<p>Reloading multiple files is typically not very robust, because there can be cross-references between various modules and packages and so you may need to repeat reloading 2-3x until all references to old implementations are replaced. For good results, you may need to have hand-crafted code that reloads the right pieces in a particular order, maybe multiple times, maybe with some additional initialization steps. This cannot be easily automated and added to the base class.</p>

---
