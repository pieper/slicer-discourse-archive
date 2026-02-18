# Shift + mouse wheel does not change brush size

**Topic ID**: 8539
**Date**: 2019-09-23
**URL**: https://discourse.slicer.org/t/shift-mouse-wheel-does-not-change-brush-size/8539

---

## Post #1 by @Ash_Alarfaj (2019-09-23 20:52 UTC)

<p>Problem report for Slicer 4.10.2 macosx-amd64: [please describe expected (( if I press shift + mouse up/down the brush size change ))and actual behavior ((this shortcut did not work)) ]</p>

---

## Post #2 by @lassoan (2019-09-23 21:02 UTC)

<p>You need to interact in a view first to bring that view into focus. For example, you can right-click in a view.</p>

---

## Post #3 by @Ash_Alarfaj (2019-09-25 09:33 UTC)

<p>Hi Andras<br>
thank you for replay, its doesn’t work even ctr+mouse weels for zooming. I’ve worked for a long time on 3Dslicer and this is a new laptop MacBook pro. The programme had worked nicely with MacBook air and PC but I don’t know why not working properly with MacBook pro≥</p>
<p>regards</p>

---

## Post #4 by @Ash_Alarfaj (2019-09-25 12:50 UTC)

<p>Hi Andras</p>
<p>I think there is a bug with this version because I’ve tried in my older mac the older version and it is worked properly  with shift or ctrl +mouse wheel.</p>
<p>regards</p>

---

## Post #5 by @jamesobutler (2019-09-25 22:44 UTC)

<p>I think this is <a href="https://issues.slicer.org/view.php?id=4661" rel="nofollow noopener">https://issues.slicer.org/view.php?id=4661</a> which is still listed as an open issue.</p>
<p>Previously reported by <a class="mention" href="/u/ash_alarfaj">@Ash_Alarfaj</a> back in November 2018 <a href="https://discourse.slicer.org/t/brush-size-control-by-key/4899" class="inline-onebox">Brush size control by key</a></p>

---

## Post #6 by @lassoan (2019-09-26 00:49 UTC)

<p>It would be nice if someone who uses a Mac could investigate why VTK does not emit mouse wheel events on MacOSX (there is nothing MacOSX-specific behavior specified at Slicer level - see <a href="https://github.com/Slicer/Slicer/blob/e7d30cb5e2e0a816e98ea8d3695bd2122cbbe530/Modules/Loadable/Segmentations/EditorEffects/qSlicerSegmentEditorPaintEffect.cxx#L1099-L1120" rel="nofollow noopener">here</a>).</p>
<p>Until the behavior is changed, workarounds are available. For example: Use Ctrl +/- keyboard shortcut for approximate brush sizing and use right-click-and-drag to fine-tune physical brush size (brush size is defined in view size by default, therefore zooming in/out the view results in changing in physical brush size change).</p>

---
