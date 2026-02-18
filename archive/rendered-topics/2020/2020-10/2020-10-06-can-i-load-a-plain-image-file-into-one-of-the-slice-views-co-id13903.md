# Can I load a plain image file into one of the Slice views, controlled by a loadable C++ extension?

**Topic ID**: 13903
**Date**: 2020-10-06
**URL**: https://discourse.slicer.org/t/can-i-load-a-plain-image-file-into-one-of-the-slice-views-controlled-by-a-loadable-c-extension/13903

---

## Post #1 by @kelvin-s (2020-10-06 19:45 UTC)

<p>In the Slicer main window, there are the red, green, and yellow slice views. I want to create an extension which can temporarily replace one of the slice views with a static image display, loaded from a regular image file (jpg png etc.). Preferably, I would like to have this image persist when changing the window layout (e.g. from Conventional to Red Slice Only), until closed through the extension.</p>
<p>If this is not possible, can I load an image into the slice view, then hide the Slice Selector slider to achieve the same visual effect?</p>
<p>My desired result looks something like this (the Red slice here is replaced with some arbitrary image file)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fbc152084864b25b597cb83497fb67a569046944.png" data-download-href="/uploads/short-url/zV81ZPdm1u2XQb8hQGniZNUw5PS.png?dl=1" title="Screenshot from 2020-10-06 12-16-59" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fbc152084864b25b597cb83497fb67a569046944_2_689x359.png" alt="Screenshot from 2020-10-06 12-16-59" data-base62-sha1="zV81ZPdm1u2XQb8hQGniZNUw5PS" width="689" height="359" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fbc152084864b25b597cb83497fb67a569046944_2_689x359.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fbc152084864b25b597cb83497fb67a569046944_2_1033x538.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fbc152084864b25b597cb83497fb67a569046944.png 2x" data-dominant-color="9E9FB0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-10-06 12-16-59</span><span class="informations">1231×642 92.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @ungi (2020-10-07 15:14 UTC)

<p>You could create a custom layout following example scripts here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository" rel="noopener nofollow ugc">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository</a><br>
and put a QT widget to where you want your static image. After that, you can set an icon or picture for the widget the same way as you would do in any QT application.</p>

---
