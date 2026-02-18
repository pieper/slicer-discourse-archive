# Selection boxes in save dialog box is invisible in Dark mode

**Topic ID**: 13442
**Date**: 2020-09-11
**URL**: https://discourse.slicer.org/t/selection-boxes-in-save-dialog-box-is-invisible-in-dark-mode/13442

---

## Post #1 by @muratmaga (2020-09-11 15:15 UTC)

<p>Is this the contrast on my screen, or others have the same issue? Selection boxes are not visible. People who don’t know that they are there will probably miss them. (also this is from a 4K screen. I think the  gray edge is too thin. I can actually see the faint trace of it the attached screen capture, but not during in the application).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/195f04a464d9b9c8f811d28a63b8e73928b9d202.png" data-download-href="/uploads/short-url/3CrvKNej8QYusqYSm1dHq8HFIoq.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/195f04a464d9b9c8f811d28a63b8e73928b9d202_2_690x388.png" alt="image" data-base62-sha1="3CrvKNej8QYusqYSm1dHq8HFIoq" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/195f04a464d9b9c8f811d28a63b8e73928b9d202_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/195f04a464d9b9c8f811d28a63b8e73928b9d202_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/195f04a464d9b9c8f811d28a63b8e73928b9d202_2_1380x776.png 2x" data-dominant-color="33343A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">3840×2160 418 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @jamesobutler (2020-09-11 19:14 UTC)

<p>It appears in light mode that border of the checkbox is <span class="hashtag">#c8c8c8</span> and based on the values specified for Dark Mode, this color appears to be defined by <code>QPalette::Mid</code> (see <a href="https://github.com/Slicer/Slicer/blob/c565268cf68c09b54e0e65fbfed5bd5faa404401/Base/QTGUI/qSlicerStyle.cxx#L228-L232" rel="nofollow noopener">here</a>). Oddly in the Slicer light style these are the same value when they shouldn’t be. Read about QPalette <a href="https://doc.qt.io/qt-5/qpalette.html#ColorRole-enum" rel="nofollow noopener">ColorRoles</a>.</p>
<p>It is harder to see in dark mode because <code>QPalette::Mid</code> is closer to <code>QPalette::Base</code>(the filled color), than it is in light mode.  This is a weird case of a widget (QCheckbox) that is using the color of <code>QPalette::Base</code> even though it is within another widget (QTableWidget) which also uses <code>QPalette::Base</code> by default for its contents.  Setting it to use the <code>QPalette::AlternateBase</code> could potentially work assuming that this widget continues to not use alternatingRowColors.</p>

---

## Post #3 by @jamesobutler (2020-09-14 01:18 UTC)

<p>Tracking this issue now at <a href="https://github.com/Slicer/Slicer/issues/5185" rel="nofollow noopener">https://github.com/Slicer/Slicer/issues/5185</a></p>

---
