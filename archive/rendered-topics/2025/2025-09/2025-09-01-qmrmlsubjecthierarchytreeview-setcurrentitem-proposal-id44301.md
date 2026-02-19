---
topic_id: 44301
title: "Qmrmlsubjecthierarchytreeview Setcurrentitem Proposal"
date: 2025-09-01
url: https://discourse.slicer.org/t/44301
---

# qMRMLSubjectHierarchyTreeView::setCurrentItem proposal

**Topic ID**: 44301
**Date**: 2025-09-01
**URL**: https://discourse.slicer.org/t/qmrmlsubjecthierarchytreeview-setcurrentitem-proposal/44301

---

## Post #1 by @aymeric.chataigner (2025-09-01 14:45 UTC)

<p>Dear Slicer developers,</p>
<p>I would like to get some feedback on a potential fix in qMRMLSubjectHierarchyTreeView: <a href="https://github.com/Slicer/Slicer/commit/1fdee41a7c916c79957f608f1fb85106d623bbfa" class="inline-onebox" rel="noopener nofollow ugc">ENH: qMRMLSubjectHierarchyTreeView: call setCurrentIndex rather than … · Slicer/Slicer@1fdee41 · GitHub</a></p>
<p>In my custom 3d slicer app I load a case which:</p>
<ul>
<li>contains only 2 volumes in the data tree</li>
<li>sets the current item of a qMRMLSubjectHierarchyCombobox to the last volume (this combobox is used in my custom module)</li>
</ul>
<p><strong>Scenario 1:</strong></p>
<ul>
<li>Load the case.</li>
<li>Remove the last volume from the data tree.</li>
<li>Result: the combobox displays None.</li>
</ul>
<p><strong>Scenario 2:</strong></p>
<ul>
<li>Load the case.</li>
<li>Click on the combobox and click on the last volume (which is already selected)</li>
<li>Remove the last volume from the data tree.</li>
<li>Result: the combobox displays the first volume.</li>
</ul>
<p><strong>Analysis</strong></p>
<p>When the last volume is removed from the data tree, this method is called:</p>
<p>QAbstractItemView::rowsAboutToBeRemoved</p>
<p>This method checks the current index:</p>
<p>if the current index is valid then the next index is selected (previous volume =&gt; scenario 2)</p>
<p>if the current index is NOT valid then no index is selected (None =&gt; scenario 1)</p>
<p>In scenario 1 there is no current index because qMRMLSubjectHierarchyCombobox simply calls qMRMLSubjectHierarchyTreeView which calls only selectionModel()-&gt;select which does not set the current index.</p>
<p>As you can see in this commit , this-&gt;selectionModel()-&gt;setCurrentIndex selects the item AND set the current index.</p>
<p>Do you see any case where an item must be selected without being the current index ?</p>
<p>Do you see any other issue ?</p>
<p>Best regards</p>

---

## Post #2 by @lassoan (2025-09-02 05:23 UTC)

<p>Both behaviors are very useful. The developer should be able to choose between them using the <a href="https://apidocs.slicer.org/main/classqMRMLNodeComboBox.html#a54e8994dfb8e4cff016f1c082cb9b385"><code>noneEnabled</code> flag the same way as in the node combobox</a>.</p>

---

## Post #3 by @aymeric.chataigner (2025-09-02 08:28 UTC)

<p>noneEnabled is already set to True in my qMRMLSubjectHierarchyCombobox.</p>
<p>Unfortunately I do not find any way to create a reproducer in 3D Slicer.</p>
<p>According to me, removing a row of the subject hierarchy tree should always lead to the same behavior in a qMRMLSubjectHierarchyCombobox, it should not change if the user already clicked on an item or not.</p>
<p>Please let me know if this commit could be interesting or if I have to implement a fix only in my custom app.</p>
<p>Regards</p>

---

## Post #4 by @lassoan (2025-09-02 11:28 UTC)

<aside class="quote no-group quote-modified" data-username="aymeric.chataigner" data-post="3" data-topic="44301">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/aymeric.chataigner/48/4977_2.png" class="avatar"> aymeric.chataigner:</div>
<blockquote>
<p>behavior in a qMRMLSubjectHierarchyCombobox … should not change if the user already clicked on an item or not.</p>
</blockquote>
</aside>
<p>Yes, I agree. If this is not the case then it is a bug that should be fixed.</p>
<p>This widget is intended to mirror the behavior of qMRMLNodeComboBox, making it suitable as a drop-in replacement.</p>

---

## Post #5 by @cpinter (2025-09-03 09:41 UTC)

<aside class="quote no-group" data-username="aymeric.chataigner" data-post="1" data-topic="44301">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/aymeric.chataigner/48/4977_2.png" class="avatar"> aymeric.chataigner:</div>
<blockquote>
<p>simply calls qMRMLSubjectHierarchyTreeView which calls only selectionModel()-&gt;select which does not set the current index.</p>
</blockquote>
</aside>
<p>If this is the case, then I think it is a bug, and your change is well justified. I can’t think of a case when we want to set selection only in the view without setting the same selection in the model.</p>
<p>Thanks for the investigation!</p>

---

## Post #6 by @aymeric.chataigner (2025-09-04 07:41 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="5" data-topic="44301">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>ction only in the view without setting the same selection in the model.</p>
</blockquote>
</aside>
<p>Here is the pull request: <a href="https://github.com/Slicer/Slicer/pull/8692" class="inline-onebox" rel="noopener nofollow ugc">BUG: Manage correctly row deletion in qMRMLSubjectHierarchyCombobox by achataigner · Pull Request #8692 · Slicer/Slicer · GitHub</a></p>

---

## Post #7 by @cpinter (2025-09-05 10:33 UTC)

<p>(I cannot approve the PR unless you request me specifically as reviewer, so need to wait until someone with higher rights approves it)</p>

---

## Post #8 by @aymeric.chataigner (2025-09-08 07:39 UTC)

<p>Ok I just added a comment in the PR to know if you can review it</p>

---
