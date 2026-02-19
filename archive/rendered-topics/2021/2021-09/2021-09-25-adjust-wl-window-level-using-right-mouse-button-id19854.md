---
topic_id: 19854
title: "Adjust Wl Window Level Using Right Mouse Button"
date: 2021-09-25
url: https://discourse.slicer.org/t/19854
---

# Adjust WL (window level) using right mouse button

**Topic ID**: 19854
**Date**: 2021-09-25
**URL**: https://discourse.slicer.org/t/adjust-wl-window-level-using-right-mouse-button/19854

---

## Post #1 by @szymswiat (2021-09-25 21:01 UTC)

<p>Operating system: n/a<br>
Slicer version: 4.13<br>
Expected behavior: n/a<br>
Actual behavior: n/a</p>
<p>Is there a way to bind window/level scaling to right mouse button and make it permanent (at least within active module)? For now when segmenting image, one have to switch between e.g. ‘Paint’ or ‘Draw’ tool and ‘Adjust window/level’ which is more than annoying.<br>
These functionalities should be enabled simultaneously:</p>
<ul>
<li>‘Paint’ or ‘Draw’ under left mouse button</li>
<li>‘Adjust window/level’ under right mouse button</li>
</ul>
<p>If there is no option to bind mouse buttons as described above how can override current behavior from scripted module? I have developed scripted module that combines ‘Volumes’ and ‘Segment Editor’ widgets along with my own widget, I could implement it here, but I have no idea how to do it.</p>
<p>Thanks for help.</p>

---

## Post #2 by @lassoan (2021-09-26 00:15 UTC)

<p>You have many options to configure appearance of your segmentation to ensure that underlying structures are well visible without keeping adjusting the window/level. You can reduce the fill opacity of the segmentation or just show the contour.</p>
<p>You can also quickly switch between mouse modes by right-clicking in a view (in recent Slicer Preview Releases). We can also add keyboard shortcuts for making the switch between mouse modes even faster.</p>
<p>But if none of these are what you would like then you can add/reconfigure all keyboard/mouse gestures any way you want. I’ve added a <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#add-shortcut-to-adjust-window-level-in-any-mouse-mode">short script to the script repository</a> that maps Ctrl+Right-click-and-drag to window/level adjustment. You can add this code snippet to your Slicer startup file to persistently enable this shortcut. It requires <em>tomorrow’s</em> Slicer Preview Release, because I had to add a few missing APIs.</p>

---

## Post #3 by @szymswiat (2021-09-26 16:51 UTC)

<p>I tried to use your snippet but unfortunately it does not change anything <img src="https://emoji.discourse-cdn.com/twitter/confused.png?v=10" title=":confused:" class="emoji" alt=":confused:">. I executed it inside custom scripted module, then in .slicerrc.py and finally in slicer console. Right mouse button still scales size of slice instead of adjusting WL.</p>
<p>Of course I’m using newest preview version of Slicer. With older one I received errors, as expected.</p>

---

## Post #4 by @lassoan (2021-09-26 17:58 UTC)

<p>The example code snippet uses Ctrl + Right-click-and-drag. On macOS, Ctrl may be called Cmd.</p>

---

## Post #5 by @szymswiat (2021-09-26 18:45 UTC)

<p>Oh sorry, my mistake…<br>
Works well with Ctrl.</p>
<p>Thank you for your support.</p>

---

## Post #6 by @szymswiat (2021-10-02 23:31 UTC)

<p>Hi Andras,</p>
<p>I found out that proposed shortcut does not work when Draw tool in Segment Editor is active. I’ve tried to setup different shortcuts e.g. right mouse button without modifier, but result is the same. Shortcut works with the rest of tools from Segment Editor.</p>
<p>Could you help us with this issue?</p>
<p>Thanks,<br>
Szymon</p>

---

## Post #7 by @lassoan (2021-10-04 03:39 UTC)

<p>I’ve updated the effects in Segment Editor to ignore mouse button push events if a modifier (Ctrl/Alt/Shift) modifier is pressed. The Slicer Preview Release that you download tomorrow or later will contain these changes and that will allow you to use Ctrl + Right-click-and-drag while in a Segment Editor effect.</p>

---

## Post #8 by @szymswiat (2021-10-20 22:51 UTC)

<p>I’ve tested new configuration and unfortunately there is no way to use Right Mouse Button + any modifier and work with Draw Tool. Clicking RMB causes Draw Tool to end its drawing cycle. Apart of that when executing below scenario, WL mode stays active after releasing modifier + RMB:</p>
<ul>
<li>enter Draw Tool mode</li>
<li>start drawing on image</li>
<li>press e.g. Ctrl + RMB to adjust WL</li>
<li>Draw Tool ends its cycle (inserts created shape to segments)</li>
<li>release Ctrl + RMB</li>
<li>WL mode is still active</li>
</ul>
<p>Good thing is that it is working well with Middle Mouse Button <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=10" title=":wink:" class="emoji" alt=":wink:"> and I think it’s enough for us.</p>

---

## Post #9 by @lassoan (2021-10-21 02:53 UTC)

<p>The fix that was implemented two weeks ago had a small bug. I’ve fixed it now, it’ll be available in the Slicer Preview Release that you download on Friday or later.</p>

---
