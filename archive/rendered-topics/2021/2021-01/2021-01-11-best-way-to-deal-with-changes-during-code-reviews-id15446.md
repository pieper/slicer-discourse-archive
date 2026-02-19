---
topic_id: 15446
title: "Best Way To Deal With Changes During Code Reviews"
date: 2021-01-11
url: https://discourse.slicer.org/t/15446
---

# Best way to deal with changes during code reviews

**Topic ID**: 15446
**Date**: 2021-01-11
**URL**: https://discourse.slicer.org/t/best-way-to-deal-with-changes-during-code-reviews/15446

---

## Post #1 by @RafaelPalomar (2021-01-11 08:21 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a>, <a class="mention" href="/u/lassoan">@lassoan</a>, <a class="mention" href="/u/pieper">@pieper</a> I was just wondering what is the best way to integrate changes requested during a code review done in Github.</p>
<p>After accepting changes in Github your commits look like this (<strong>Approach 1</strong>):</p>
<pre><code class="lang-auto">Update qSlicerWidget.cxx
Update vtkMRMLApplicationlogic.cxx
ENH: add something in qSlicerWidget
ENH: add something in vtkMRMLApplicationLogic.cxx
</code></pre>
<p>Should I integrate the changes directly in the corresponding final commits? This leads to just (<strong>Approach 2</strong>):</p>
<pre><code class="lang-auto">ENH: add something in qSlicerWidget
ENH: add something in vtkMRMLApplicationLogic.cxx
</code></pre>
<p>here, we will lose the traceability of the code review.</p>
<p>Maybe I should leave the Update commits, but in order for you to squash them when you do the merge? (<strong>Approach 3</strong>)</p>
<pre><code class="lang-auto">Update qSlicerWidget.cxx
ENH: add something in qSlicerWidget
Update vtkMRMLApplicationlogic.cxx
ENH: add something in vtkMRMLApplicationLogic.cxx
</code></pre>

---

## Post #2 by @RafaelPalomar (2021-01-11 09:51 UTC)

<p>Also. How about change requests that were not directly applied in Github? Should there be new commits for this, or perhaps the changes should happen directly in the corresponding PR commits?</p>

---

## Post #3 by @lassoan (2021-01-11 20:01 UTC)

<p>You can submit all the changes as subsequent commits in the same PR. It makes it a bit easier to see what you changed in response to comments. When the changes are complex then sometimes we force-push to keep things simpler and avoid any potential merge conflicts.</p>
<p>When everything is fixed then we either ask you to squash the commits (especially if it is not trivial, for example you want to split the changes to a few commits), but typically we can just squash all the changes into a single commit before merging.</p>

---
