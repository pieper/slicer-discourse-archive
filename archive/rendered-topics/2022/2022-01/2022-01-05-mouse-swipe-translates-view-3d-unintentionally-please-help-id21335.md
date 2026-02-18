# Mouse swipe translates view/3D unintentionally -- please help

**Topic ID**: 21335
**Date**: 2022-01-05
**URL**: https://discourse.slicer.org/t/mouse-swipe-translates-view-3d-unintentionally-please-help/21335

---

## Post #1 by @asdf (2022-01-05 02:51 UTC)

<p>Brand new to Slicer (4.13, Intel MacOS Catalina) and I’m having the following problem:</p>
<p>I have a volume loaded, and I’ve been working mostly in the Segmentation Editor. I’ve found that click+drag rotates the volume (in 2D or 3D panes), and Shift+click+drag translates the volume.</p>
<p>However, when I simply single-finger swipe on the trackpad, this ALSO causes the volume to translate (no Shift, no click). Usually it is the first time my cursor enters the view window of interest, then I wait a few seconds and do the exact same single-finger swipe, and nothing happens. This is driving me crazy because I am trying to segment and the minute I move the cursor over to what I want to trace, the volume moves. (It happens regardless of whether I have selected a segmentation tool or whether I’m just mousing over with the regular cursor).</p>
<p>I looked for the answer to this problem in the documentation (<a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html" class="inline-onebox" rel="noopener nofollow ugc">User Interface — 3D Slicer documentation</a>), I could not find the answer. Please help me, and thanks!</p>

---

## Post #2 by @lassoan (2022-01-05 05:22 UTC)

<aside class="quote no-group" data-username="asdf" data-post="1" data-topic="21335">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/ebca7d/48.png" class="avatar"> asdf:</div>
<blockquote>
<p>However, when I simply single-finger swipe on the trackpad, this ALSO causes the volume to translate</p>
</blockquote>
</aside>
<p>Tap-and-drag gesture is by default mapped to panning of the view (same as Shift + click-and-drag). This gesture requires that you tap your touchpad and then rest your finger there for a half second or so without moving. This normally does not interfere with the click-and-drag gesture.</p>
<p>Maybe you have enabled tap-to-click on your system? Or maybe you click in an unusual way (maybe you recently moved from another operating system, or switched from mouse to trackpad, …)? Or maybe something has changed in macOS (there have been some recent <a href="https://www.macrumors.com/2021/12/01/macos-12-1-beta-4-fixes-tap-to-click-issue/">related macOS bug</a> or maybe there was some intentional change).</p>
<p>If more people will report this error then we will change the event mapping, but until then you can disable the tap-and-drag by copy-pasting the text below into your <a href="https://slicer.readthedocs.io/en/latest/user_guide/settings.html#application-startup-file">Slicer startup file</a>:</p>
<pre data-code-wrap="python"><code class="lang-python">for sliceViewLabel in slicer.app.layoutManager().sliceViewNames():
    sliceViewWidget = slicer.app.layoutManager().sliceWidget(sliceViewLabel)
    w = sliceViewWidget.sliceView().displayableManagerByClassName("vtkMRMLCrosshairDisplayableManager").GetSliceIntersectionWidget()
    w.SetEventTranslation(w.WidgetStateIdle, vtk.vtkCommand.StartPanEvent, vtk.vtkEvent.AnyModifier, vtk.vtkWidgetEvent.NoEvent)
</code></pre>
<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/fedorov">@fedorov</a> <a class="mention" href="/u/che85">@che85</a> (and anyone else using macOS) - do you find that you accidentally activate tap-and-drag gesture when you use paint effect in Segment Editor?</p>

---

## Post #3 by @pieper (2022-01-05 21:52 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="21335">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/fedorov">@fedorov</a> <a class="mention" href="/u/che85">@che85</a> (and anyone else using macOS) - do you find that you accidentally activate tap-and-drag gesture when you use paint effect in Segment Editor?</p>
</blockquote>
</aside>
<p>I don’t recall ever having this trouble with the mac trackpad, but I don’t think I have tried using slicer with a trackpad in several months so maybe it’s something new.</p>

---

## Post #4 by @hherhold (2022-01-05 22:13 UTC)

<p>I haven’t noticed this at all. I use the touchpad sparingly (you can have my 3 button mouse when you pry it from my cold, dead fingers) but I just ran through some painting with the touchpad just now and it seems fine. This is MacOS 12.1, 2019 MBP 16". I don’t have any funky touchpad settings or gestures.</p>

---

## Post #5 by @asdf (2022-01-07 04:28 UTC)

<p>Hi all,</p>
<p>Thank you, editing the slicerrc.py worked!<br>
(No, was not new to trackpad and no, no tap-to-click set up on MacOS – will be interesting to see if other MacOS/trackpad users note this issue)</p>

---
