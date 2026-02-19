---
topic_id: 9535
title: "Can You Put A Module Listing Under Two Different Categories"
date: 2019-12-17
url: https://discourse.slicer.org/t/9535
---

# Can you put a module listing under two different categories?

**Topic ID**: 9535
**Date**: 2019-12-17
**URL**: https://discourse.slicer.org/t/can-you-put-a-module-listing-under-two-different-categories/9535

---

## Post #1 by @muratmaga (2019-12-17 21:01 UTC)

<p>As part of the SlicerMorph, we want to bundle bunch of extensions that are likely to be use to our users but may get overlooked. A particular example is Fiducial Registration tools within IGT. I would like to make them aware of it, by somehow cross-referencing through the SlicerMorph module list?</p>
<p>Is that possible?</p>

---

## Post #2 by @pieper (2019-12-17 21:47 UTC)

<p>A module can declare itself to be in more than one menu category, e.g. with <code>    self.parent.categories = ["Wizards", "SlicerMorph"]</code> in the module class <code>__init__</code> method, but I’m not sure you can easily change another modules categories.</p>
<p>One way to do something effectively the same would be to put stub modules in the SlicerMorph category that are programmed to redirect to the desired module (e.g. call <code>selectModule("otherModule")</code> in their module’s <code>enter</code> method.).  Or you can make another module selector organized they way you want it and add it as a toolbar.</p>

---

## Post #3 by @muratmaga (2019-12-17 21:48 UTC)

<p>Thanks Steve. What you suggested is what I was looking for…</p>

---

## Post #4 by @pieper (2019-12-17 22:02 UTC)

<p>Sounds good Murat - do you need an example of how to do it?</p>

---

## Post #5 by @muratmaga (2019-12-17 22:50 UTC)

<p>That will be great!!!</p>

---

## Post #6 by @pieper (2019-12-19 20:38 UTC)

<p>Here’s an easy working example for adding some shortcuts to an existing module category.</p>
<p>This might be considered a hack, so I’m going to just put it here as a workaround for now and not in the script repository.  If we like the idea we should probably make something like this part of the module selector API.</p>
<pre><code class="lang-auto">
def addMenuShortcuts(targetCategory, modulesToMap):
    menu = mainWindow().moduleSelector().modulesMenuComboBox().menu()
    for action in menu.actions():
        if action.text == targetCategory:
            submenu = action.menu()
    for module in modulesToMap:
      action = qt.QAction(module, submenu)
      action.connect("triggered()", lambda module=module : slicer.util.selectModule(module))
      submenu.addAction(action)

addMenuShortcuts("SlicerMorph", ["Animator",])
</code></pre>

---

## Post #7 by @lassoan (2019-12-19 20:42 UTC)

<p>You may also create a “Welcome” module for SlicerMorph, which shows a list of modules (maybe illustrated with nice thumbnails), maybe shortcuts to data loading, sample data download, and documentation. You can set it as “home” module in application settings (or from Python script) so that when Slicer starts then it shows this module by default.</p>

---
