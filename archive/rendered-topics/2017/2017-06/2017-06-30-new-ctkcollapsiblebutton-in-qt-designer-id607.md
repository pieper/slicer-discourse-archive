# New ctkCollapsibleButton in qt designer

**Topic ID**: 607
**Date**: 2017-06-30
**URL**: https://discourse.slicer.org/t/new-ctkcollapsiblebutton-in-qt-designer/607

---

## Post #1 by @Marine (2017-06-30 14:19 UTC)

<p>Hello everyone !</p>
<p>I’m having trouble making my module’s interface.<br>
I would like to add a new collapsible button but when I chose to add a ctkCollapsiblebutton with the widget box in qt designer, the button added is not the same as the one present by default.</p>
<p>The one present by default (the first one) doesn’t have any red sign and has a vertical layout already provided (the new one has not).</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/37646e5f7aaf357c9ae5c2d1e16994b797448d3d.png" data-base62-sha1="7U1qSNdhFCGLYmRzvF13yAaoFxX" width="337" height="35"></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d09452cbb0c24450723ac22fcdd70dff5e25a71a.png" data-base62-sha1="tLb5UoySuHVr3vvuFgmCeHa3dCa" width="399" height="184"></p>
<p>How can I have the same collapsible button as the one by default in the interface ? I’ve already tried to add a vertical layout to the new button but the results are not convincing…</p>
<p>Thanks !</p>

---

## Post #2 by @finetjul (2017-06-30 14:42 UTC)

<p>Hi Marine,</p>
<p>By default, a ctkCollapsibleButton comes without a layout. So you are experiencing the correct behavior.</p>
<p>To set the layout, you should not use the Layout item in the left panel of Designer, but instead, you need to right click your ctkCollapsibleButton and select “Lay out” in the context menu.</p>
<p>Hth,<br>
Julien.<br>
p.s. if that still does not work, you can always copy/paste the existing collapsible button. And then remove its contents.</p>

---

## Post #3 by @Marine (2017-07-03 07:55 UTC)

<p>The right click thing didn’t work because even though I had the “lay out” in the context menu I couldn’t change it (it was “locked”).<br>
But the copy/past worked, I had to disable the global layout in order to past the button and to enable it after. I’m new to qt designer and didn’t know you could copy/past widget like that.</p>
<p>Thanks for your help !</p>

---
