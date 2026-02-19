---
topic_id: 24725
title: "Showing Mouse Interaction Toolbar In Custom Module"
date: 2022-08-12
url: https://discourse.slicer.org/t/24725
---

# Showing mouse interaction toolbar in custom module

**Topic ID**: 24725
**Date**: 2022-08-12
**URL**: https://discourse.slicer.org/t/showing-mouse-interaction-toolbar-in-custom-module/24725

---

## Post #1 by @Vincebisca (2022-08-12 09:05 UTC)

<p>Hello everyone,</p>
<p>As part of the development of a custom interface in 3D Slicer, I would like to show the mouse interaction toolbar. Indeed, I use the following structure to determine which toolbars are shown in the interface, but I do not manage to show the mouse interaction :</p>
<pre><code>keepToolbars = [
  slicer.util.findChild(slicer.util.mainWindow(), 'MainToolBar'),
  slicer.util.findChild(slicer.util.mainWindow(), 'ViewToolBar'),
  slicer.util.findChild(slicer.util.mainWindow(), 'ViewersToolBar'),
  slicer.util.findChild(slicer.util.mainWindow(), 'ModuleToolBar')]
slicer.util.setToolbarsVisible(not singleModule, keepToolbars)
slicer.util.setMenuBarsVisible(singleModule)
slicer.util.setApplicationLogoVisible(not singleModule)
slicer.util.setModuleHelpSectionVisible(not singleModule)
slicer.util.setModulePanelTitleVisible(not singleModule)
slicer.util.setDataProbeVisible(not singleModule)
slicer.util.setViewControllersVisible(singleModule)
</code></pre>
<p>I tried several writings to get it via the findChild function but it never worked… Is there a place that I missed where the name and structure of these widgets are listed?</p>
<p>Thank you in advance ! Sorry if the question is dumb, I have really low programing skills.</p>
<p>Vincent</p>

---

## Post #2 by @jamesobutler (2022-08-12 14:11 UTC)

<p>If you right click on the toolbar area, you get a menu to show/hide certain toolbars with the name of the toolbar provided. You can use the name of the toolbar (e.g. “Mouse Interaction”) and do a search in the Slicer repository to find where it is used.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1b179cb589b0a64c517aebbfafd682e98fcc733b.png" alt="image" data-base62-sha1="3RFtN07qiUYXjhC4qvE7stipHOX" width="475" height="285"></p>
<p>When I remove toolbars for my custom application, I fully remove the toolbar that I don’t need rather than just hiding because you can just right click the toolbar area and show it again.</p>
<pre data-code-wrap="python"><code class="lang-python">toolbar = slicer.util.mainWindow().findChild(qt.QToolBar, "ModuleSelectorToolBar")
slicer.util.mainWindow().removeToolBar(toolbar)
</code></pre>

---

## Post #3 by @Vincebisca (2022-08-12 15:40 UTC)

<p>Ok, I thought to have searched for the toolbar name everywhere in the documentations and stuff but obviously I didn’t think about searching directly in the GitHub repositery. Told you, I’m not a programmer…</p>
<p>I didn’t understand the second part, what is the difference between hiding and removing? Right clicking in the toolbar area can be useful for specific things sometimes so I’d rather keep it for the moment, but you mean that if you remove the toolbar, it doesn’t appear anymore in the rightclick?</p>

---

## Post #4 by @jamesobutler (2022-08-12 15:57 UTC)

<p>Yes, if you <code>removeToolbar</code> then it won’t show up in the menu when you right-click on the toolbar area. Hiding it will only uncheck the option in that shown right-click menu, but the user can still show it again.</p>

---

## Post #5 by @Vincebisca (2022-08-12 16:29 UTC)

<p>Oh ok ! I’ll remember that for later then ! Thank you !</p>

---
