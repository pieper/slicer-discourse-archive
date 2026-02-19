---
topic_id: 7797
title: "Package Imp Deprecated"
date: 2019-07-29
url: https://discourse.slicer.org/t/7797
---

# Package imp deprecated

**Topic ID**: 7797
**Date**: 2019-07-29
**URL**: https://discourse.slicer.org/t/package-imp-deprecated/7797

---

## Post #1 by @Alex_Vergara (2019-07-29 13:56 UTC)

<p>The package imp is <a href="https://docs.python.org/3/library/imp.html" rel="noopener nofollow ugc">deprecated</a> in python since version 3.4 and will be removed. This is critical as the button reload of the modules strongly depends on this package. I didn’t succeed to replace it with the recommended importlib, but maybe somebody has already created something.</p>

---

## Post #2 by @Alex_Vergara (2019-07-31 09:26 UTC)

<p>I have tried overriding the onReload method, it runs without error but it does not do what it is intended, the submodules are still not reloaded:</p>
<pre><code class="lang-python">def onReload(self):
        """
        Override reload scripted module widget representation.
        """
        logging.debug("Reloading Dosimetry4D")
        submoduleNames=['Dosimetry4DLogic', 'Dosimetry4DTest', 'fit_values', 'PhysicalUnits']
        import importlib
        for submoduleName in submoduleNames:
            module = importlib.import_module(".".join(['Logic', submoduleName]))
            importlib.reload(module)
            
        if isinstance(self, ScriptedLoadableModuleWidget): # Mandatory for now, reloading the widget
            ScriptedLoadableModuleWidget.onReload(self)
</code></pre>

---

## Post #3 by @Alex_Vergara (2019-08-06 13:18 UTC)

<p>I made it to work with the following:</p>
<pre><code class="lang-python">import importlib
mod = importlib.import_module('Logic', __name__)
importlib.reload(mod)
__submoduleNames__=['Dosimetry4DLogic', 'Dosimetry4DTest', 'fit_values', 'PhysicalUnits']

# and then...
    def onReload(self):
        """
        Override reload scripted module widget representation.
        """
        logging.info("Reloading Dosimetry4D")
        importlib.reload(mod)
        for submoduleName in __submoduleNames__:
            mod1 = importlib.import_module('.'.join(['Logic',submoduleName]), __name__)
            importlib.reload(mod1)

        if isinstance(self, ScriptedLoadableModuleWidget):
             ScriptedLoadableModuleWidget.onReload(self)
</code></pre>

---
