---
topic_id: 19892
title: "How To Disable Crosshair With Mouse Drag Drop"
date: 2021-09-28
url: https://discourse.slicer.org/t/19892
---

# How to disable Crosshair with mouse drag&drop?

**Topic ID**: 19892
**Date**: 2021-09-28
**URL**: https://discourse.slicer.org/t/how-to-disable-crosshair-with-mouse-drag-drop/19892

---

## Post #1 by @jumbojing (2021-09-28 06:01 UTC)

<p>在我的插件中,只需要(opt+cmd)旋转crosshair,(shift)选择定位这些操作,可是这个mouse drag&amp;drop会干扰我的有效操作,我想禁用,该怎么做?</p>
<blockquote>
<p>In my plug-in, I only need (Opt+cmd)+drag to rotate the crosshair and (Shift)+click to select the location, but this mouse drag&amp;drop will interfere with my effective operation. I want to disable it, what should I do?</p>
</blockquote>
<p><a class="mention" href="/u/lassoan">@lassoan</a>@Juicy@jamesobutler <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a></p>

---

## Post #2 by @jumbojing (2021-09-28 09:31 UTC)

<p>我可能没说清楚吧…在我应用(Opt+cmd)+drag to rotate the crosshair后, cursor似乎粘滞了,移动鼠标时,slice会随着光标偏移,无法应用(Opt+cmd)+drag to rotate the crosshair, 很烦人, 我该怎么办?</p>
<blockquote>
<p>I may not make it clear…After I applied (Opt+cmd)+drag to rotate the crosshair, the cursor seems to be sticky. When I move the mouse, the slice will shift (offset) with the cursor and cannot be applied (Opt+cmd)  +drag to rotate the crosshair, very annoying, what should I do?</p>
</blockquote>

---

## Post #3 by @lassoan (2021-09-28 13:27 UTC)

<p>You can disable all keyboard shortcuts that you don’t need. If you create conflicts by using inconsistent shortcuts in various widgets then you may end up with inconsistent states (and widgets may stuck in a state).</p>
<p>If you run into any problems without modifying the keyboard/mouse gesture mapping then let us know. If you only have problems with your own customizations then make one change at a time and see what causes the breaking change and avoid that.</p>

---
