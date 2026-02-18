# qt.QFormBuilder?

**Topic ID**: 7551
**Date**: 2019-07-12
**URL**: https://discourse.slicer.org/t/qt-qformbuilder/7551

---

## Post #1 by @adamrankin (2019-07-12 15:30 UTC)

<p>Hello all,</p>
<p>Before I begin digging, does anyone know why this class may not be available in python?</p>
<p>Adam</p>

---

## Post #2 by @jcfr (2019-07-12 15:35 UTC)

<p>This rely on <a href="https://mevislab.github.io/pythonqt/" rel="nofollow noopener">PythonQt</a> to make the Qt classes available in Python and it looks like <a href="https://github.com/commontk/PythonQt/search?utf8=%E2%9C%93&amp;q=QFormBuilder&amp;type=" rel="nofollow noopener">this class is not wrapped</a>.</p>

---

## Post #3 by @lassoan (2019-07-12 16:17 UTC)

<p>We use qt.QUiLoader() instead. See how it is used in <a href="https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/util.py#L269" rel="nofollow noopener">slicer.util.loadUI</a>.</p>
<p>But it gets even better! Since Slicer-4.10.2 we have made it very easy to edit module GUI using Qt designer (launch designer from the module GUI, reload the GUI without restarting Slicer, template in ExtensionWizard, …). See <a href="https://github.com/PerkLab/PerkLabBootcamp/blob/master/Doc/day3_2_SlicerProgramming.pptx?raw=true" rel="nofollow noopener">Scripting and module development tutorial</a> (from slide 33).</p>

---

## Post #4 by @adamrankin (2019-07-12 19:07 UTC)

<p>I’m familiar with loadUI. The desired functionality from QFormBuilder is the save function to write a dynamically created widget to a .ui file.</p>

---

## Post #5 by @lassoan (2019-07-12 19:10 UTC)

<p>What is the use case? I’m just curious.</p>

---

## Post #6 by @adamrankin (2019-07-12 19:22 UTC)

<p>Not sure, just got asked if the class was available.</p>

---

## Post #7 by @jcfr (2019-07-12 20:20 UTC)

<p>If needed, you could either improve the PythonQt wrapping … or create a SlicerFormBuilder class to expose the feature to python.</p>

---
