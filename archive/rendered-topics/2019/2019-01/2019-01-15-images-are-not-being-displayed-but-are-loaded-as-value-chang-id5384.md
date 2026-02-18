# Images are not being displayed but are loaded as value changes when mouse is moved.

**Topic ID**: 5384
**Date**: 2019-01-15
**URL**: https://discourse.slicer.org/t/images-are-not-being-displayed-but-are-loaded-as-value-changes-when-mouse-is-moved/5384

---

## Post #1 by @Lucy_Upchurch (2019-01-15 21:46 UTC)

<p>Operating system: Windows Server 2016<br>
Slicer version: 4.11<br>
Expected behavior: To see images<br>
Actual behavior:Displays black image<br>
OpenGL: 4.6</p>
<p>Here are the specs about my computer:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/93bb5e6218857d5a1a7b668d38ad6b29417e0fc2.png" alt="image" data-base62-sha1="l4TCFxJVDNJsw3rGowMKR0g0zJg" width="590" height="222"></p>
<p>Even though you cannot see the image, the image is loaded as the values change when I move my mouse around in the box where the image is displayed.</p>
<p>Is there a setting in Slicer that needs to be set or included in my path for the graphics to work correctly?</p>
<p>Thanks.</p>

---

## Post #2 by @lassoan (2019-01-16 05:19 UTC)

<p>Medical images have typically much larger dynamic range than what could be displayed, therefore intensity window/level operation is performed automatically when loading a volume. The intensity window may be incorrect for extraordinary image content (e.g., there is a small but very bright region in the image). You can adjust window/level by left-mouse click-and-drag up/down/left-right; or using Volumes module). If you share an image then we can see if we can make the automatic window/level algorithm more robust.</p>

---

## Post #3 by @Lorensen (2019-01-16 06:35 UTC)

<p>Lucy,</p>
<p>Long time no see.</p>
<p>Still at Duke?</p>
<p>Bill</p>

---
