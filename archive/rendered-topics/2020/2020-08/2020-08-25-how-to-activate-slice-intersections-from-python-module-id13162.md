# How to activate slice intersections from python module?

**Topic ID**: 13162
**Date**: 2020-08-25
**URL**: https://discourse.slicer.org/t/how-to-activate-slice-intersections-from-python-module/13162

---

## Post #1 by @mikebind (2020-08-25 18:48 UTC)

<p>Hello, I’m having a hard time figuring out how to turn on the “Slice Intersections” from a scripted python module (equivalent to clicking the checkbox at the bottom of the crosshair menu on the toolbar).  I’ve searched the discourse forum and the github repository, but as far as I can tell, all the hits I am getting relate to options for showing slice intersections for things like models, which I understand happens through display nodes. It may be similar for the “Slice Intersections” setting I want, but I don’t know how to find out what display node I am looking for.  It is a setting which applies to all 2D slice nodes, so I don’t expect it to be associated with any particular slice node, but I’m not sure what else to look for.  The layout manager?  It doesn’t seem to be there either. Anyway, I expect it is easy to set, I just can’t find the command.  Thanks for any help you can provide!</p>

---

## Post #2 by @jamesobutler (2020-08-25 19:53 UTC)

<p>The Slicer script repository is very helpful for figuring out how to do common tasks in python. The following details usage of turning on/off slice intersections.<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Toolbar_functions" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Toolbar_functions</a></p>

---

## Post #3 by @pieper (2020-08-25 20:04 UTC)

<p>Another hint: if you see something in the GUI and want to learn how to script it, you can usually search for the text of the label or tooltip using either github or grep through a local checkout.  From there you can usually trace back to the implementation in just a step or two.  This is also a good way to learn more about how Slicer is implemented.</p>

---

## Post #4 by @mikebind (2020-08-25 20:36 UTC)

<p>Thanks very much.  I have used the script repository many times to find solutions, but somehow didn’t think of it this time.  <a class="mention" href="/u/pieper">@pieper</a>, I did try to take exactly your suggested approach this time, but because there are very many instances of “slice intersection” or “sliceIntersection” in the code which are not related to this setting, I couldn’t find the relevant one.</p>

---

## Post #5 by @pieper (2020-08-25 20:49 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="4" data-topic="13162">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>there are very many instances of “slice intersection” or “sliceIntersection” in the code which are not related to this setting, I couldn’t find the relevant one.</p>
</blockquote>
</aside>
<p>Very true, it’s not always obvious.  Sometimes it helps to search for the tooltip text, which is more unique, to find the widget, then find where a slot if connected to it, and the slot usually just sets a property on a mrml node.</p>

---
