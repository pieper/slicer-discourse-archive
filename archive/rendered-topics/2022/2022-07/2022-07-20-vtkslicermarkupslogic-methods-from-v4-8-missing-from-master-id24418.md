# vtkSlicerMarkupsLogic methods from v4.8 missing from master version

**Topic ID**: 24418
**Date**: 2022-07-20
**URL**: https://discourse.slicer.org/t/vtkslicermarkupslogic-methods-from-v4-8-missing-from-master-version/24418

---

## Post #1 by @mosenco (2022-07-20 18:17 UTC)

<p>I’m trying to upgrade the code of modules developed for slicer4.6 with python 2.7 into slicer5.0.3 with python3.9</p>
<p>All went good until i found out that some methods are missing in the new slicer version.</p>
<pre><code class="lang-auto">mlogic = slicer.modules.markups.logic()
  
mlogic.SetDefaultMarkupsDisplayNodeTextScale(1.3)
mlogic.SetDefaultMarkupsDisplayNodeGlyphScale(1.5)
mlogic.SetDefaultMarkupsDisplayNodeColor(0.39, 0.78, 0.78) 
mlogic.SetDefaultMarkupsDisplayNodeSelectedColor(0.39, 1.0, 0.39)
</code></pre>
<p>slicer gives me errors saying slicer.modules.markups.logic() doesnt have any of those methods. and that’s true! In slicer 5.0.3 all those methods are gone.</p>
<p>What can i do? Are those methods moved somewhere else with different names?</p>

---

## Post #2 by @lassoan (2022-07-20 18:20 UTC)

<p>See description of the API change here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MigrationGuide#Markups" class="inline-onebox">Documentation/Nightly/Developers/Tutorials/MigrationGuide - Slicer Wiki</a></p>

---

## Post #3 by @jamesobutler (2022-07-20 19:39 UTC)

<blockquote>
<ul>
<li>GetDefaultMarkups…() and SetDefaultMarkups…() methods are removed. Instead default display node can be accessed by GetDefaultMarkupsDisplayNode() method and default values can be get/set in that class.</li>
</ul>
</blockquote>
<pre data-code-wrap="python"><code class="lang-python">slicer.modules.markups.logic().GetDefaultMarkupsDisplayNode()
</code></pre>

---
