---
topic_id: 13947
title: "How To Press Qtbutton"
date: 2020-10-09
url: https://discourse.slicer.org/t/13947
---

# How to press qtButton?

**Topic ID**: 13947
**Date**: 2020-10-09
**URL**: https://discourse.slicer.org/t/how-to-press-qtbutton/13947

---

## Post #1 by @aldoSanchez (2020-10-09 01:56 UTC)

<p>Hi<br>
today I’m trying to press a button by code.</p>
<p>and i know the name of the object is: setupLightkitButton<br>
i all ready try this:</p>
<blockquote>
<blockquote>
<blockquote>
<p>qt.QPushButton(‘setupLightkitButton’).click()<br>
qt.QPushButton(‘setupLightkitButton’).animateClick()<br>
qt.QPushButton(‘setupLightkitButton’).animateClick(True)<br>
light=qt.QPushButton(‘setupLightkitButton’)<br>
light.clicked(True)<br>
light.checked</p>
</blockquote>
</blockquote>
</blockquote>

---

## Post #2 by @aldoSanchez (2020-10-09 02:07 UTC)

<p>the only way I found was by edit the UI</p>

---

## Post #3 by @lassoan (2020-10-09 02:22 UTC)

<p>You should never use a module’s widget class from another module. See <a href="https://github.com/PerkLab/PerkLabBootcamp/blob/master/Doc/day3_2_SlicerProgramming.pptx?raw=true">Scripting and module development tutorial</a> on the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials">training page</a> for details.</p>
<p>Instead, you can call methods implemented in the other module’s logic. In some experimental modules developers may work quick-and-dirty and put logic that could be useful for other modules in the widget. In this case you can either fix that module (move the useful code part into the module’s logic where you can access it from your own module) or just copy-paste the code into your module.</p>
<p>In this specific case, Lights module in Sandbox extension is implemented relatively cleanly: the function that is launched when <code>setupLightKitButton</code> is clicked (<code>onSetupLighkit</code>) calls the <code>setLightkitInView</code> function in the logic. So, in your module, you don’t need to deal with the Light module’s widget, just access its logic (or instantiate a new LightsLogic class) and use it.</p>

---

## Post #4 by @aldoSanchez (2020-10-09 19:24 UTC)

<p>thanks for the PowerPoint it gives me a better understanding.</p>

---
