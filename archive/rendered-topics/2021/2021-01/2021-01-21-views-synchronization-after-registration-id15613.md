# Views synchronization after registration

**Topic ID**: 15613
**Date**: 2021-01-21
**URL**: https://discourse.slicer.org/t/views-synchronization-after-registration/15613

---

## Post #1 by @LaurennLam (2021-01-21 16:01 UTC)

<p>Hi all,</p>
<p>I’d like to know if it’s possible to have two slice’s synchronize views in Slicer ?<br>
Explanations:<br>
I have two volumes. One is registered to the other. The main idea is to display those two volumes into separate views. Then, synchronize the slices: when I slice on the view 1, it also moves the slice on view 2 but on the correct slice. Slices are registered.<br>
I tried to resample the registered image to the first one, but I didn’t find a way to synchronize them.</p>
<p>Is there any way to do that ?</p>
<p>Thanks,<br>
Best,<br>
Laurenn</p>

---

## Post #2 by @muratmaga (2021-01-21 16:07 UTC)

<p>Yes, use the linked view (green highlight).<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7d5320293bef695263f9b666ed725d737c663d37.png" alt="image" data-base62-sha1="hSFMkXiIgIDUbFtJM8cNFMpI5pB" width="167" height="150"></p>

---

## Post #3 by @LaurennLam (2021-01-21 17:07 UTC)

<p>I tried, but without success.<br>
The sliders are not linked.</p>

---

## Post #4 by @lassoan (2021-01-21 21:53 UTC)

<p>Synchronization only happens between views that have the same orientation (for example, an axial view will only move other axial views) and if they are in the same view group (view group is predefined in the view layout; usually 3 orthogonal views are in the same group, but it can be changed in “View controllers” module’s Advanced section).</p>
<p>Probably the simplest is to use “Compare volumes” to set up the view layout. The module also has a couple of additional tools for volume comparison such as automatic fade and reveal cursor.</p>
<p>You may also find <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#view-cross-reference">view cross-referencing</a> useful.</p>

---

## Post #5 by @LaurennLam (2021-01-22 13:02 UTC)

<p>Thanks for the support Andras.<br>
Do you know if it’s possible to synchronize two volume but not with the same slice number ?<br>
I mean, can I define that I want to synchronize volumes, volume one on slice 10 and volume 2 on slice 40 for example ?</p>

---

## Post #6 by @lassoan (2021-01-22 14:26 UTC)

<p>Yes - for this you can align the two images using one of the many registration methods available in Slicer. I would recommend <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html#semi-automatic-registration">semi-automatic registration</a>, but if really all the misalignment between the volumes is just a shift along one axis then you can use manual alignment (using translation slider in Transforms module).</p>

---

## Post #7 by @LaurennLam (2021-01-22 14:42 UTC)

<p>Great ! Thanks Andras !</p>

---
