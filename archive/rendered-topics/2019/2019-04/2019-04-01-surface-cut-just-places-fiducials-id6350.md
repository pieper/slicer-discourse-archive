# Surface Cut just places fiducials

**Topic ID**: 6350
**Date**: 2019-04-01
**URL**: https://discourse.slicer.org/t/surface-cut-just-places-fiducials/6350

---

## Post #1 by @chir.set (2019-04-01 09:46 UTC)

<p>I’m following this <a href="https://www.youtube.com/watch?v=xZwyW6SaoM4" rel="nofollow noopener">tutorial</a>. Surface Cut behaves differently by just placing fiducial points without linking them. No free form segment can be hence be created. Please see this screen <a href="https://mega.nz/#!sUcm3ArA!AK4W4BNR1LXn0Y5v4kv7t9HJnjYL_TiU_ab0yDXCvrg" rel="nofollow noopener">capture</a>.</p>
<p>I’m using Slicer built on Linux, with Python 2.7.15 (2.7.13 does not compile here). The same is observed with the latest nightly build from your repository.</p>
<p>Please advise.</p>

---

## Post #2 by @jamesobutler (2019-04-01 13:32 UTC)

<p>It is likely that you are using an old version of the SegmentEditorExtraEffects extension.  If you are using a Slicer nightly build on Linux, are you also updating your extensions frequently?  If not, you should make this part of your routine as the nightly/preview builds have pretty regular bug fixes and improvements.  From the Extensions manager, you can click on the wrench icon in the top right of the window and select “Check for updates”. Then proceed to press the buttons below each extension to update the out-of-date extension.</p>
<p>What you’re describing here was fixed a couple weeks ago (see <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/issues/18" rel="nofollow noopener">Missing model creation for surface cut and draw tube effects</a> in the SegmentEditorExtraEffects repo).</p>
<p>Let us know how this works after attempting to install the latest version of the extension!</p>

---

## Post #3 by @chir.set (2019-04-01 13:43 UTC)

<p>Following this <a href="https://discourse.slicer.org/t/segment-editor-extra-effect-not-working/6347">thread</a>, I found out that the MarkupsToModel module was missing, and Surface Cut depends on it.</p>
<p>After building and installing MarkupsToModel, the problem gets resolved.</p>

---
