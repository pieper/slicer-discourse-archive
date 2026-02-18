# Strange creation of multiple desktops on Linux

**Topic ID**: 13085
**Date**: 2020-08-19
**URL**: https://discourse.slicer.org/t/strange-creation-of-multiple-desktops-on-linux/13085

---

## Post #1 by @PaoloZaffino (2020-08-19 12:47 UTC)

<p>Hi all,<br>
I am running Slicer in Arch Linux (gnome and wayland).<br>
When I load an image in slicer, a strange thing happens in gnome: multiple desktops are added to the system.<br>
In gnome there is always a new, fresh and empty desktop available, that is automatically created and added when in the last one appears at least a single window.<br>
In this case, it creates n empty desktops (they can be also 10-20), without a specific reason.<br>
Those desktops are destroyed when slicer is closed.</p>
<p>For me it is not a huge problem, I’m writing just to point it out.</p>
<p>Paolo</p>

---

## Post #2 by @cpinter (2020-08-19 12:53 UTC)

<p>Could this be related to the <a href="https://discourse.slicer.org/t/dropdown-menus-spawn-on-other-monitor/13003" class="inline-onebox">Dropdown menus spawn on other monitor</a> issue?<br>
Maybe not because that problem is kind of the reverse: open the popup on the primary monitor if the Slicer window is on a secondary one. But still it’s quite similar and the number of new screens seem to suggest there may be a connection.</p>
<p><a class="mention" href="/u/paolozaffino">@PaoloZaffino</a> does this happen more if you open dropdown menus such as the module history button? Do these desktops appear all at once, or gradually as you use Slicer?</p>

---

## Post #3 by @PaoloZaffino (2020-08-19 13:26 UTC)

<p>No, I think it is not related to that issue.</p>
<p>I explain better my situation:</p>
<p>I open slicer: it’s all ok.<br>
I drag an nrrd into slicer: the import window appears and I see the first “strange” desktop (any image loaded yet).<br>
I click load: I see for a second another windows (the progress bar I think) and when the volume is vislible in slicer I have in total 4 “strange” desktops (in addition to the usual empty one).</p>
<p>If I drag and load a second nrrd file I have 8 desktops that should not be there.</p>
<p>Paolo</p>

---

## Post #4 by @lassoan (2020-08-19 13:31 UTC)

<p>I did a web search and it seems that Qt-5.15 has compatibility issues with Wayland. If the issues are too annoying and we cannot implement workarounds then we may consider going back to Qt-5.12 on Linux.</p>
<p>The issue may be that popup windows do not get deleted properly. Maybe we can explicitly delete them, or avoid deleting and recreating popups and just hide/show them.</p>

---

## Post #5 by @PaoloZaffino (2020-08-19 13:37 UTC)

<p>For me it’s not a problem, it was just for pointing it out.</p>
<p>Any plan on the QT side to fix Wayland issues in the next releases?<br>
This could be the easiest solution.</p>
<p>Paolo</p>

---

## Post #6 by @lassoan (2020-08-19 13:43 UTC)

<p>Yes, eventually these errors will be fixed, but it does not seem to be a priority for Qt.</p>

---

## Post #7 by @jamesobutler (2020-08-19 14:12 UTC)

<p>Just a note that for the factory build machines the Linux platform is the only one on Qt 5.11.2 while macOS and Windows are both on Qt 5.15.0.</p>

---

## Post #8 by @chir.set (2020-08-19 14:18 UTC)

<aside class="quote no-group" data-username="PaoloZaffino" data-post="1" data-topic="13085">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/paolozaffino/48/81052_2.png" class="avatar"> PaoloZaffino:</div>
<blockquote>
<p>running Slicer in Arch Linux (gnome and wayland).</p>
</blockquote>
</aside>
<p>Sorry for a quick topic bifurcation.</p>
<p>When I use home built Slicer under KDE/Wayland in Arch, 2D views are just black after loading an .nrrd file, and Volume Rendering does not show anything with GPU rendering. Do these work for you ? There are no problems with KDE/X11.</p>
<p>More topic related, I don’t see any extra desktops/activities after loading an .nrrd file with KDE/Wayland.</p>

---

## Post #9 by @PaoloZaffino (2020-08-19 15:13 UTC)

<p><a class="mention" href="/u/chir.set">@chir.set</a> no other issue on my side, it works perfectly.<br>
I see just a bunch of additional desktops.</p>

---

## Post #10 by @PaoloZaffino (2020-09-14 07:23 UTC)

<p>Hi,<br>
a little update: right now I’m using the nightly version 2020-08-25 and the multi-desktop problem disappeared.</p>

---
