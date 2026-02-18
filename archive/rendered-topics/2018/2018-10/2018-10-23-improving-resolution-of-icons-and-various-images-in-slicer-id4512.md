# Improving resolution of icons and various images in Slicer

**Topic ID**: 4512
**Date**: 2018-10-23
**URL**: https://discourse.slicer.org/t/improving-resolution-of-icons-and-various-images-in-slicer/4512

---

## Post #1 by @jamesobutler (2018-10-23 19:08 UTC)

<p>With Slicer 4.10.0 and the transition to Qt5, there is greatly improved scaling of widgets for higher DPI monitors (I know a user with a 4K monitor), however various icons in those scaled widgets now appear blurry.  Icons that are primarily rectangular shapes scale well, but anything that has curves or is angled now looks blurry.  A likely issue is the usage of the png format for the icons which doesn’t scale well.</p>
<p>It appears that icons such as the <a href="https://github.com/Slicer/Slicer/blob/0eeeb13d4d0112cecb276dd19e896ed870ff1238/Modules/Loadable/Markups/Resources/Icons/MarkupsMouseModePlace.png" rel="nofollow noopener">markups place fiducial png</a> or any of the other icons in the toolbar such as <a href="https://github.com/Slicer/Slicer/blob/0eeeb13d4d0112cecb276dd19e896ed870ff1238/Modules/Scripted/SegmentEditor/Resources/Icons/SegmentEditor.png" rel="nofollow noopener">segment editor png</a> are pngs that are 21x21px in size. Even the 3D Slicer logo at the heading above all modules in the left side bar area appears blurry.</p>
<p>The slice offset text in the slice windows also appears smaller relative to the space it occupies in the colored header of the individual slice window.</p>

---

## Post #2 by @jcfr (2018-10-23 19:20 UTC)

<p>Thanks for the feedback.</p>
<p>To illustrate, would you be able to share a screenshot ?</p>

---

## Post #3 by @rkikinis (2018-10-23 19:34 UTC)

<p>Hi,</p>
<p>I don’t know about the rest, but at least for the Slicer logo there is a variety of versions. Check out the following page.<br>
<a href="https://www.slicer.org/wiki/Slicer3:Slicer3Brand" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Slicer3:Slicer3Brand</a></p>
<p>Best<br>
Ron</p>

---

## Post #4 by @jamesobutler (2018-10-23 23:05 UTC)

<p>Here’s a 1080p screenshot and a 2160p(4K) screenshot.  I guess you’ll have to really view them in their native screen size since viewing the 4K in fullscreen mode on a 1080p screen will just scale it back down and then look normal. It’s not unusable, but something I clearly noticed when viewing it on a 4K screen.  Or maybe it is just poor Windows scaling… I feel like you would just need to see on 4K in person using a Windows machine<br>
.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/87a4a5e3af8adb44539e7339f9811299bcce205b.png" data-download-href="/uploads/short-url/jlXdlmCSMvQR1t61GYd5wJZjPmz.png?dl=1" title="1080p" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/87a4a5e3af8adb44539e7339f9811299bcce205b_2_690x373.png" alt="1080p" data-base62-sha1="jlXdlmCSMvQR1t61GYd5wJZjPmz" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/87a4a5e3af8adb44539e7339f9811299bcce205b_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/87a4a5e3af8adb44539e7339f9811299bcce205b_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/87a4a5e3af8adb44539e7339f9811299bcce205b_2_1380x746.png 2x" data-dominant-color="7B7B81"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1080p</span><span class="informations">1920×1040 64.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
