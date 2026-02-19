---
topic_id: 6363
title: "Python Scripted Module Development Reload Feature For Multip"
date: 2019-04-02
url: https://discourse.slicer.org/t/6363
---

# Python scripted module development reload feature for multiple files

**Topic ID**: 6363
**Date**: 2019-04-02
**URL**: https://discourse.slicer.org/t/python-scripted-module-development-reload-feature-for-multiple-files/6363

---

## Post #1 by @michalikthomas (2019-04-02 08:42 UTC)

<p>Is there a way how to customize/override default development feature - “Reload” - behavior, during scripted module development? I separated code into multiple files but “Reload” seems to reload just the root python file, not the whole folder.</p>

---

## Post #2 by @pieper (2019-04-02 21:23 UTC)

<p>It’s a very good question - I did the original scripted module reload code many years ago and it took a while to sort out all the tweaks needed to get it working, so I never went back and looked into the options multiple-file reload, which is too bad because it tends to make me put more than I should in the main scripted module file.</p>
<p>Probably the same techniques that work for the main module would also work for imported files and maybe there’s even a way to discover the dependencies automatically and reload them all or maybe the scripted module could provide a list of code to reload.  It may also be that with the python3 transition there will be new ways to do this, I haven’t looked.  Would love to see a PR for this.</p>

---

## Post #3 by @jcfr (2019-04-02 21:55 UTC)

<p>It may be worth revisiting the approach by looking at the autoreload module from ipython.</p>
<p>See <a href="https://github.com/ipython/ipython/blob/master/IPython/extensions/autoreload.py" rel="nofollow noopener">https://github.com/ipython/ipython/blob/master/IPython/extensions/autoreload.py</a></p>

---

## Post #4 by @lassoan (2019-04-03 01:01 UTC)

<p>Reloading is implemented fully in Python, so you can override the default implementation and reload additional modules, too. Since there are usually dependencies between classes, you typically need to click reload 2-3 times to update all referenced objects in al objects.</p>
<p>Example:</p>
<pre><code class="lang-auto">class ValveAnnulusAnalysisWidget(ScriptedLoadableModuleWidget):
  ...
  def onReload(self):
    logging.debug("Reloading ValveAnnulusAnalysis")
    packageName='HeartValveLib'
    submoduleNames=['util', 'LeafletModel', 'SmoothCurve', 'ValveRoi', 'PapillaryModel', 'ValveModel', 'HeartValves']
    import imp
    f, filename, description = imp.find_module(packageName)
    package = imp.load_module(packageName, f, filename, description)
    for submoduleName in submoduleNames:
      f, filename, description = imp.find_module(submoduleName, package.__path__)
      try:
          imp.load_module(packageName+'.'+submoduleName, f, filename, description)
      finally:
          f.close()
    ScriptedLoadableModuleWidget.onReload(self)
</code></pre>

---

## Post #5 by @michalikthomas (2019-04-10 20:00 UTC)

<p>Thank you, <a class="mention" href="/u/lassoan">@lassoan</a>, for your example. Could you please add more information about how modules are registered and initiated within mentioned scripted module? I wasn’t able to me this work.</p>
<p>My scripted module structure looks as follows:</p>
<pre><code>CustomScriptedModule/
    CustomScriptedModule.py
    CustomScriptedModuleLib/
        __init__.py
        CustomScriptedModuleWidget.py
        OtherModule1.py
        OtherModule2.py
        ...
</code></pre>
<p>Init file contains:</p>
<pre><code>from CustomScriptedModuleWidget import *
from OtherModule1 import *
from OtherModule2 import *
...</code></pre>

---

## Post #6 by @lassoan (2019-04-10 20:31 UTC)

<p>Replace “HeartValveLib” by “CustomScriptedModuleLib”; ‘util’ by ‘OtherModule1’, ‘LeafletModel’ by ‘OtherModule2’, etc.</p>
<p>You must keep the module widget class in CustomScriptedModule.py. If you want to simplify widget creation, then choose “scripteddesigner” module template in the Extension Wizard and use Qt Designer to create your GUI.</p>

---

## Post #7 by @michalikthomas (2019-04-10 21:01 UTC)

<p>Thanks, this works perfectly.</p>

---

## Post #8 by @pieper (2019-04-11 19:39 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="6363">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>you can override the default implementation and reload additional modules</p>
</blockquote>
</aside>
<p>This looks nice <a class="mention" href="/u/lassoan">@lassoan</a> - any reason not to make <code>submoduleNames</code> an property and move this implementation into <code>ScriptedLoadableModuleWidget</code> ?</p>

---

## Post #9 by @lassoan (2019-04-11 19:47 UTC)

<p>Yes, it would be nice to add this to the module base class. There could be a list of tuples set in the module widget class constructor to define package and submodule names to reload - something like this:</p>
<pre><code>self.packagesToReload = (
  ('packageName1', ('submoduleNameA', 'submoduleNameB')),
  ('packageName2', ('submoduleNameA', 'submoduleNameB', 'submoduleNameC'))
  )</code></pre>

---

## Post #10 by @pieper (2019-04-11 20:04 UTC)

<p>Sounds good - I’ll probably do that next time I run into this.   (Unless someone beats me to it!)</p>

---

## Post #11 by @Alex_Vergara (2019-07-29 13:53 UTC)

<p>IDK if you are aware that the package imp is <a href="https://docs.python.org/3/library/imp.html" rel="nofollow noopener">deprecated</a> in python since version 3.4 and will be removed. it is recommended to move to importlib library. However, I did not succeed yet to make it work properly while reloading.</p>

---

## Post #12 by @lassoan (2019-07-29 18:29 UTC)

<p>Thank you for looking into this. Probably we’ll get to this when imp is actually removed, starts to misbehave, or we need to rework module loading for some other reason anyway.</p>

---

## Post #13 by @pieper (2020-04-21 16:55 UTC)

<p>In some experimental code I found a handy workaround for this.  I put this in my module’s Logic class so that every time I reload the module I get a fresh copy of the Lib code.</p>
<pre><code class="lang-auto">  def __init__(self):
    import VudoLib, VudoLib.Vudo
    self.VudoModule = importlib.reload(VudoLib.Vudo)
</code></pre>
<p>It should probably be made conditional on being in debug mode, since it loads the Lib twice at startup, but that’s usually a very small penalty in practice.  The import has to happen before the reload because reload only works on something that’s already been loaded.  I didn’t find anything that actually does the initial load via an api.</p>

---
