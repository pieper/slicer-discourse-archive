---
topic_id: 14059
title: "Adjust Window Level Tool Disabled"
date: 2020-10-15
url: https://discourse.slicer.org/t/14059
---

# Adjust Window Level Tool disabled

**Topic ID**: 14059
**Date**: 2020-10-15
**URL**: https://discourse.slicer.org/t/adjust-window-level-tool-disabled/14059

---

## Post #1 by @rohan_n (2020-10-15 17:38 UTC)

<p>I don’t know why, but for some reason one of the functions in my scripted module disables the ability of the user to use the Adjust Window Level mouse tool on the Red slice. Is there a simple command that re-enables the use of Adjust Window Level tool on the Red slice?<br>
Thanks,<br>
Rohan</p>

---

## Post #2 by @lassoan (2020-10-15 18:53 UTC)

<p>You can check if you <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Disable_certain_user_interactions_in_slice_views">modify enabled actions in the view</a>. If you don’t do anything like that then it may be a side effect of some operations, in which case you can comment out/deactivate parts of your code until you find the function that causes this behavior. Let us know what you find.</p>

---

## Post #3 by @rohan_n (2020-10-15 20:51 UTC)

<p>Thanks.<br>
Apparently the lines of code that enable or disable scrolling through slices with the mouse  have the unintended effect of disabling the Adjust Window Level tool. I fixed the problem by commenting out lines such as this.</p>
<pre><code>  #interactorStyle = slicer.app.layoutManager().sliceWidget('Red').sliceView().sliceViewInteractorStyle()
  #interactorStyle.SetActionEnabled(interactorStyle.BrowseSlice, False)
</code></pre>
<p>or this</p>
<pre><code>  #interactorStyle = slicer.app.layoutManager().sliceWidget('Red').sliceView().sliceViewInteractorStyle()
  #interactorStyle.SetActionEnabled(interactorStyle.BrowseSlice, True)</code></pre>

---

## Post #4 by @jcfr (2020-10-15 20:57 UTC)

<aside class="quote no-group" data-username="rohan_n" data-post="3" data-topic="14059">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rohan_n/48/78474_2.png" class="avatar"> rohan_n:</div>
<blockquote>
<p>enable or disable scrolling through slices with the mouse have the unintended effect of disabling the Adjust Window Level tool</p>
</blockquote>
</aside>
<p>I suspect this is related to this issue. See <a href="https://github.com/Slicer/Slicer/issues/5175" class="inline-onebox">Calling vtkMRMLSliceViewInteractorStyle::SetActionEnabled systematically disable SetCursorPosition · Issue #5175 · Slicer/Slicer · GitHub</a></p>
<p>If you would like to help address the root cause, the issue report contains enough details to help you move forward the process.</p>

---
