# Warning of observer from scripted module in Slicer 5.0.3

**Topic ID**: 24735
**Date**: 2022-08-13
**URL**: https://discourse.slicer.org/t/warning-of-observer-from-scripted-module-in-slicer-5-0-3/24735

---

## Post #1 by @wrc (2022-08-13 02:53 UTC)

<p>To show this warning:<br>
Modules-Developer Tools-Extension Wizard-Create Extension-Add Module<br>
Open the module just created, switch to another module, then back to this module, you can see the warning:</p>
<pre><code class="lang-auto">/Applications/Slicer.app/Contents/bin/Python/slicer/util.py:2486: UserWarning: does not have observer
  warn('does not have observer')
</code></pre>
<p>It comes from:</p>
<pre><code class="lang-auto">    if self._parameterNode is not None:
      self.removeObserver(self._parameterNode, vtk.vtkCommand.ModifiedEvent, self.updateGUIFromParameterNode)
</code></pre>
<p>This warning shows in Slicer 5.0.3, but not in the previous versions.</p>

---

## Post #2 by @danpak94 (2022-12-02 15:28 UTC)

<p>Hello, I am seeing the same warning. Have you found a solution?</p>

---

## Post #3 by @lassoan (2022-12-02 15:38 UTC)

<p>I think it has been fixed in the current version of Slicer (5.2.x or later).</p>

---

## Post #4 by @danpak94 (2022-12-02 16:49 UTC)

<p>Hi, thanks for the reply. I’m seeing the same warning on Slicer 5.2.1.</p>

---

## Post #5 by @lassoan (2022-12-02 20:32 UTC)

<p>I thought <a href="https://github.com/Slicer/Slicer/commit/3a8deba0d30e885272a0e91c257ac8d21771d861" class="inline-onebox">BUG: Fix VTKObservationMixin regression · Slicer/Slicer@3a8deba · GitHub</a> fixed these. <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> do you have any comments on this?</p>

---

## Post #6 by @Sunderlandkyl (2022-12-06 17:17 UTC)

<p>It’s an unrelated bug with the ScriptedModule template. Observers are already removed when exiting the module, however they are “removed” a second time when the user enters the module and setParameterNode() is called.</p>
<p>I’ve made a PR with a fix here: <a href="https://github.com/Slicer/Slicer/pull/6720" class="inline-onebox" rel="noopener nofollow ugc">BUG: Fix scripted module template observer warning by Sunderlandkyl · Pull Request #6720 · Slicer/Slicer · GitHub</a></p>

---

## Post #7 by @GeneRisi (2023-03-02 19:58 UTC)

<p>I am still getting this in Slicer 5.3.0 using Total Segmentator" in non-fast mode.</p>

---

## Post #8 by @lassoan (2023-03-03 05:59 UTC)

<p>The fix that <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> implemented in the module template had to be done in the TotalSegmentator module, too. It would be great if you could <a href="https://github.com/lassoan/SlicerTotalSegmentator/blob/main/TotalSegmentator/TotalSegmentator.py">edit the file</a> accordingly and if everything works well then send a pull request with the suggested changes.</p>

---
