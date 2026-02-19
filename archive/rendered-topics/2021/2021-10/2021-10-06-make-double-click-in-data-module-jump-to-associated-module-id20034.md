---
topic_id: 20034
title: "Make Double Click In Data Module Jump To Associated Module"
date: 2021-10-06
url: https://discourse.slicer.org/t/20034
---

# Make double-click in Data module jump to associated module

**Topic ID**: 20034
**Date**: 2021-10-06
**URL**: https://discourse.slicer.org/t/make-double-click-in-data-module-jump-to-associated-module/20034

---

## Post #1 by @joachim (2021-10-06 11:43 UTC)

<p>Every node in the <em>Data</em> view window (often?) has a custom module associated, accessible by right clicking the item and selecting <em>Edit properties…</em>.</p>
<p>Would it be a good idea to let double clicking an item jump to its associated module (just like <em>Edit properties…</em>) instead of edit its name as now? Name editing could be done in the right click menu or pressing <em>F2</em> on the keyboard. Editing a name is not something I do frequently, but I frequently jump between modules.</p>
<p>What do you think?</p>

---

## Post #2 by @lassoan (2021-10-06 12:30 UTC)

<p>Interesting idea. I agree that now rename is needed less frequently that editing other properties.</p>
<p>Let’s see what others think.<br>
<a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/cpinter">@cpinter</a> <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/muratmaga">@muratmaga</a> <a class="mention" href="/u/jamesobutler">@jamesobutler</a></p>

---

## Post #3 by @jamesobutler (2021-10-06 13:17 UTC)

<p>This would apply for all tabs in the “Data” module, including “Subject Hierarchy”, “Transform Hierarchy” and “All nodes”?</p>
<div class="md-table">
<table>
<thead>
<tr>
<th style="text-align:center">Subject Hierarchy</th>
<th style="text-align:center">Transform Hierarchy</th>
<th style="text-align:center">All nodes</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/878e356ead48a55d8705f3f1fb51c06f267c20af.png" alt="image" data-base62-sha1="jlb8DqgsatToB2u1eJFAATqkvtd" width="480" height="144"></td>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
</tr>
</tbody>
</table>
</div>

---

## Post #4 by @lassoan (2021-10-06 14:15 UTC)

<p>It would only makes sense for the Data module (all the other modules are already for editing properties of the item). You raised a good point - this would introduce inconsistency in the behavior subject hierarchy tree: some places it would jump to another module, while other places it would edit the item name.</p>

---

## Post #5 by @muratmaga (2021-10-06 14:25 UTC)

<p>I think this is a good idea, but I am not sure if the double-click is the right behavior to do that. Maybe an another icon (-&gt;Arrow?) that when clicked takes you to the module (equivalent of edit properties).</p>

---

## Post #6 by @lassoan (2021-10-06 14:26 UTC)

<p>Or maybe Ctrl + Left-click? This is the shortcut used in MS Office software to follow a link instead of set the cursor at the clicked position.</p>

---

## Post #7 by @joachim (2021-10-06 14:34 UTC)

<p>For me this behaviour would make sense for every item in every tab of <em>Data</em>, even the hidden nodes under <em>All nodes</em>.</p>
<p>I would appreciate a double-click behaviour. Changing the name is not something I often do (and it happens that I get into name editing accidentally instead of selecting a data item, which is a bit annoying). Ctrl-Left-click can also be a good idea. An arrow icon will probably introduce more clutter in the UI.</p>

---

## Post #8 by @jamesobutler (2021-10-06 14:37 UTC)

<p>I would expect that jumping between modules with this ctrl+left-click shortcut would likely only be used by <a class="mention" href="/u/joachim">@joachim</a> and others specifically told about it.</p>
<aside class="quote no-group" data-username="joachim" data-post="1" data-topic="20034">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/a87d85/48.png" class="avatar"> joachim:</div>
<blockquote>
<p>but I frequently jump between modules.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/joachim">@joachim</a> What have you found frustrating about the current navigation capabilities in Slicer? Which of the toolbar options do you utilize?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7a3d23fa5223c3211da488e999bbf492e9164301.png" alt="image" data-base62-sha1="hrnf9rWCuHW3QGSCbalSSPcgfPb" width="377" height="40"></p>
<p>Do you take advantage of “Favorite Modules” toolbar by customizing it to your needs?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9d24f8f6f0d492eb869c0f06f61606e3177cbb66.png" alt="image" data-base62-sha1="mqaaUZ8M9VceiG2k6joFDLeFD7w" width="216" height="35"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a1c730a61810091cad8ac99fd308a47c6d11ad23.png" alt="image" data-base62-sha1="n59Doz2rSQzWoZGU2DzpwkOCsYX" width="670" height="92"></p>
<p>When inspecting a node in the “Data” module and you are wanting to jump to the associated module, do you already know the module where you are wanting to go? Or do you not know yet and want Slicer to take you to the module that can manipulate that node?</p>
<p>Adding the shortcut to the Data module is just one solution to improving navigation between modules, but I’m curious if there is a better solution to improve behavior so that all users will benefit.</p>

---

## Post #9 by @lassoan (2021-10-06 14:45 UTC)

<p>“Edit properties…” switches to a different module and also selects that node in that module, which is particularly useful if there are many nodes in the scene. So, easier module switching (e.g., using favorite modules) is not a complete replacement.</p>
<p>Double-click performs the default action (top-most action in the context menu, displayed in bold) in Windows Explorer and some other software, so there is some precedence for performing different action for the same mouse gesture in a tree of items.</p>
<p>Ctrl + click would be indeed non-discoverable, but adding a hint to the context menu (I think there is a standard way of displaying keyboard shortcut on the right side of menu items) could help.</p>

---

## Post #10 by @muratmaga (2021-10-06 15:05 UTC)

<aside class="quote no-group" data-username="joachim" data-post="7" data-topic="20034">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/a87d85/48.png" class="avatar"> joachim:</div>
<blockquote>
<p>I would appreciate a double-click behaviour. Changing the name is not something I often do (and it happens that I get into name editing accidentally instead of selecting a data item, which is a bit annoying). Ctrl-Left-click can also be a good idea. An arrow icon will probably introduce more clutter in the UI.</p>
</blockquote>
</aside>
<p>But double click to rename is an established behavior (both in OSes and Slicer), and we have no idea how many people are using it. We do not have an easy way communicating changing established behaviors (no release notes), so I am reluctant. But we do have these icons that are not used for anything as far as I can tell.</p>
<p>Would it be possible that the double-clicking the name stays as rename, and clicking the icons takes you to the module.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b82d3ccf30a0cb076261dbb3d361d1f347715788.png" alt="image" data-base62-sha1="qhiM5aiSkjJk7jONzvGHkiKJYk8" width="354" height="172"></p>

---

## Post #11 by @lassoan (2021-10-06 19:00 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="10" data-topic="20034">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>We do not have an easy way communicating changing established behaviors (no release notes)</p>
</blockquote>
</aside>
<p>We provide very detailed, extensive release notes for each stable release. In the meantime documentation is updated in sync with code changes and major features are announced using the <a href="https://discourse.slicer.org/tag/feature">feature tag</a> here. Of course, we cannot rely on people reading documentation or release notes, so everything should be possible to discover by just using the software.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="10" data-topic="20034">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>But double click to rename is an established behavior (both in OSes and Slicer),</p>
</blockquote>
</aside>
<p>Yes, double-click to rename is a common behavior, but for example, in one of the most frequently used software on Windows, the File explorer, double-click opens the file in the default program associated with the file (exact same behavior as open a node in the default module in Slicer). I’m not sure I would want to use double-click for “Edit properties…” just want to point out that there is strong precedent.</p>

---

## Post #12 by @jamesobutler (2021-10-06 19:20 UTC)

<p>Yes, if Slicer was to follow the rename action as in File Explorer on Windows, it would happen on single-left click of a selected item. That’s often 2 subsequent clicks (1 left-click to select, 1 left-click to rename the selection) but not a true double left-click action.</p>
<p>For Qt, double left-click is an established action that edits cells in QTableWidget and QTreeWidget objects. Therefore it would be tough for me to advocate mapping it to a different action such as the “Edit properties…” action which goes to a different module with the node pre-selected.</p>

---

## Post #13 by @pieper (2021-10-06 20:18 UTC)

<p>I would like doubleclick to do Edit Properties.  I think clicking twice and jiggling the mouse should trigger rename (or picking rename from the context menu).  This behavior would mimic the windows and mac.</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="12" data-topic="20034">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>File Explorer on Windows, it would happen on single-left click of a selected item</p>
</blockquote>
</aside>
<p>For me on windows and mac the rename sequence is: click once to select, click and second time and move the mouse.  I believe the movement is required in order to minimize mis-interpretation of double clicks as renames.</p>

---

## Post #14 by @jamesobutler (2021-10-06 20:25 UTC)

<p>For me on Windows rename is select with single left-click, followed by single-left click again with no jigging of mouse required.</p>

---

## Post #15 by @pieper (2021-10-06 20:28 UTC)

<p>You’re right, it’s just a delay.  But it is a second click, because the item has to be selected first.</p>

---

## Post #16 by @joachim (2021-10-07 08:31 UTC)

<p>Unintentionally renaming can be frustrating (ideally rename an object one and only one time, I guess). I rarely use that toolbar to navigate, instead I click <em>Edit properties…</em> or <em>Ctrl-F</em> for navigation/manipulation. I use the <em>Data</em> module for navigation. So in my case a double-click feature for the <em>Data</em> module would be great.</p>
<p>But this was just a suggestion from me.</p>

---

## Post #17 by @muratmaga (2021-10-07 09:26 UTC)

<aside class="quote no-group" data-username="joachim" data-post="16" data-topic="20034">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/a87d85/48.png" class="avatar"> joachim:</div>
<blockquote>
<p>Unintentionally renaming can be frustrating (ideally rename an object one and only one time, I guess). I rarely use that toolbar to navigate, instead I click <em>Edit properties…</em> or <em>Ctrl-F</em> for navigation/manipulation. I use the <em>Data</em> module for navigation. So in my case a double-click feature for the <em>Data</em> module would be great.</p>
</blockquote>
</aside>
<p>I am not sure how double clicking can cause unintentional renaming. The worst it would do, you will initiate an unintentional renaming action, but unless start typing nothing will get renamed.</p>
<p>Actually intentional renaming is not all that uncommon either. Typical use cases would be when cloning a node in which you want to have a meaningful ID or similarly loading the same dataset multiple times into scene etc…</p>
<p>I still like the idea of being able to go to the module that’s associated with data type more directly then right click + edit properties. And you are right that even if you do rename things, you probably do it once in a session, whereas you may need to go back and forth through same modules multiple times. So assigning a common action like double cick to more common use cases make sense.</p>

---

## Post #18 by @cpinter (2021-10-07 10:08 UTC)

<p>I use the double-click rename frequently, and if I do then others probably do as well. I imagine it would be quite annoying for about a week (while the movement is still wired in me) that when I double-click the module is switched, and then I have to go back. It is for sure more annoying than the “accidental renaming” that has been mentioned, which only requires another click anywhere else, while the shown GUI does not change at all, nor any renaming happens.</p>
<p>The more OS-like renaming interaction (click wait click) makes sense though, and I don’t remember if I had to get used to double-click rename or it was straightforward immediately - it was a loong time ago - and also don’t know if Qt supports this interaction, but for new users the OS-style rename is probably easier. And then we have double-click free, but I’m not sure yet if I’d go down that road.</p>
<p>I like <a class="mention" href="/u/muratmaga">@muratmaga</a> 's idea about double-clicking the icon. I’m not sure from the top of my head that clicking on that can be handled separately in the Qt model-view scheme, need to check.</p>
<p>Ctrl-left-click also sounds like a good option, and I agree that we could establish some shortcuts and show them in the context menu. Also if someone wants to do Slicer efficiently with hotkeys they check the <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#mouse-keyboard-shortcuts">hotkeys page</a> in the documentation, I think that can be expected from every non-casual user. In a past project I made an infographic with a keyboard with colored keys on it and some text around, and it proved quite handy.</p>
<p>In summary, I like the “double-clicking the icon” idea best, mainly because it would not change current behavior, and those icons are the same as the module icons in most cases, so it is very intuitive to link these identical icons with this “go to corresponting module” action. However I’m not strongly opposed to other alternatives.</p>

---

## Post #19 by @jamesobutler (2021-10-07 11:41 UTC)

<aside class="quote no-group" data-username="joachim" data-post="16" data-topic="20034">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/a87d85/48.png" class="avatar"> joachim:</div>
<blockquote>
<p>I rarely use that toolbar to navigate, instead I click <em>Edit properties…</em> or <em>Ctrl-F</em> for navigation/manipulation. I use the <em>Data</em> module for navigation.</p>
</blockquote>
</aside>
<p>Interesting. What type of nodes are you typically editing where you jump to the corresponding module?</p>

---

## Post #20 by @joachim (2021-10-07 12:43 UTC)

<p>There is a signal <a href="https://doc.qt.io/qt-5/qabstractitemview.html#doubleClicked" rel="noopener nofollow ugc"><code>QAbstractItemView::doubleClicked(const QModelIndex&amp; )</code></a> that can be used. Or use <a><code>QGuiApplication::keyboardModifiers()</code></a> inside <a href="https://doc.qt.io/qt-5/qabstractitemview.html#pressed" rel="noopener nofollow ugc"><code>QAbstractItemView::pressed(const QModelIndex&amp; )</code></a>. I guess.</p>

---

## Post #21 by @joachim (2021-10-07 12:53 UTC)

<p>For example:</p>
<ul>
<li>Edit segmentation</li>
<li>Look at volume properties</li>
<li>See Annotation values, like lengths</li>
</ul>
<p>The <em>Data</em> module also makes it easier to learn how Slicer works.</p>

---

## Post #22 by @lassoan (2021-10-07 13:06 UTC)

<p>Good news: there seem to be a <code>SelectedClicked</code> option for edit trigger, which is probably the same as the File Explorer style renaming. We could switch everywhere to using this shortcut for item renaming.</p>
<p>Double-click would become available for performing other frequently used action. In Data module, “Edit properties…” would be a very useful action, but in other modules it would not make much sense. “Center the node in all views” would make a lot of sense elsewhere, but in fact it would be useful in Data module, too. Maybe just executing the top-most context menu action on double-click would be the most consistent and flexible behavior.</p>

---
