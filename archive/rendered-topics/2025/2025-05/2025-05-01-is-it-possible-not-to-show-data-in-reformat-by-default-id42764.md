# Is it possible not to show data in reformat by default

**Topic ID**: 42764
**Date**: 2025-05-01
**URL**: https://discourse.slicer.org/t/is-it-possible-not-to-show-data-in-reformat-by-default/42764

---

## Post #1 by @muratmaga (2025-05-01 19:08 UTC)

<p>I have datasets that I manually aligned or rigidly registered. Every time I load these back into Slicer, they come in “Reformat” view, as opposed to the axial/sagittal/coronal. Is there a way to disable this behavior globally? I mean if I want the “reformat” view, I can use the “Rotate the volume to plane” in slice controllers.</p>
<p>This is also quite confusing behavior for the new people…</p>

---

## Post #2 by @pieper (2025-05-06 21:10 UTC)

<p>I’m not sure what these images are, but if “patient” orientation is not an issue, you could just set the directions to identity and then axial/sag/cor mode would not be a reformat.</p>

---

## Post #3 by @mikebind (2025-05-07 16:54 UTC)

<p>If you can find what this setting is and set a default for it in slicerrc or in whatever method for loading you want to use, I think having this unchecked should prevent switching away from the default axial/sagittal/coronal<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/29113716b8b7898a9f91196cbe69b34f2224d4ee.png" data-download-href="/uploads/short-url/5RisuWLxz1aG0NSkl6hgEkViQYm.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/29113716b8b7898a9f91196cbe69b34f2224d4ee_2_690x201.png" alt="image" data-base62-sha1="5RisuWLxz1aG0NSkl6hgEkViQYm" width="690" height="201" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/29113716b8b7898a9f91196cbe69b34f2224d4ee_2_690x201.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/29113716b8b7898a9f91196cbe69b34f2224d4ee_2_1035x301.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/29113716b8b7898a9f91196cbe69b34f2224d4ee_2_1380x402.png 2x" data-dominant-color="CFD7DC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1580×462 23.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This method definitely works for me once everything is already loaded, but I haven’t investigated how to force a default for it.</p>
<p>Alternatively, you could set up that Slicer does whatever it wants on load, and you force it back to axial/sagittal/coronal afterwards by script or button press.</p>

---

## Post #4 by @muratmaga (2025-05-13 16:54 UTC)

<p>Thanks <a class="mention" href="/u/mikebind">@mikebind</a>.</p>
<p>Not sure what that setting meant to do but, on previews it that doesn’t seem to have any effect (enabled or disabled data always comes up as reformat).</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a>?</p>

---

## Post #5 by @muratmaga (2025-05-13 16:54 UTC)

<p>But then I will</p>
<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="42764" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>I’m not sure what these images are, but if “patient” orientation is not an issue, you could just set the directions to identity and then axial/sag/cor mode would not be a reformat.</p>
</blockquote>
</aside>
<p>But then I will loose my alignment? Won’t I?</p>

---

## Post #6 by @mikebind (2025-05-13 18:59 UTC)

<p>If “Reset view orientation on show” is checked for an image volume, then, if I show it by clicking on the eye icon in the Data module, the slice views reorient as if I had clicked the “Rotate to volume plane” button on each slice view.  With it unchecked, the slice views do not reorient when the volume is shown.  It looks like similar behavior can be specified on load with <code>slicer.util.loadVolume(filename, properties{"show": False})</code> .   This loads the image, but does not reorient the slice views (and also doesn’t automatically show the image in the slice views; there doesn’t appear to be a simple way to disentangle these two behaviors (showing and reorienting) during loading).  Likewise, if you load using the Add Data dialog, if you expand the Options, and uncheck “Show”, the slice views will not reorient.</p>
<p>Are you loading a MRML scene or a separate image file (nrrd, etc)?  If it is a scene, check the slice orientations before saving the scene, if they are “Reformat” then reloading as reformat should be the expected behavior.  If you are loading from a separate image file, I think Slicer defaults to aligning the slice views with the image axes because basic segmentation tools work more intuitively when slice views show image planes (oblique slices can lead to striping artifacts and triangles due to slicing through segmentation labelmap voxels at an angle).  You can avoid the automatic reorienting using the “Options” → uncheck “Show” in the Add Data dialog.</p>

---

## Post #7 by @muratmaga (2025-05-13 20:45 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="6" data-topic="42764">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>Are you loading a MRML scene or a separate image file (nrrd, etc)? If it is a scene, check the slice orientations before saving the scene, if they are “Reformat” then reloading as reformat should be the expected behavior.</p>
</blockquote>
</aside>
<p>I am simply loading the NRRD in new Slicer sessions with these options set (or unset). I will try the data suggestion.</p>

---

## Post #8 by @lassoan (2025-05-14 04:39 UTC)

<p>“Reset orientation on show” option is persistent - it is remembered even when you restart the application. If you prefer not to align slice views to the volume axes when you show the volume then it is enough to disable this option once (using right-click menu in Data module).</p>

---

## Post #9 by @muratmaga (2025-05-14 04:55 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="42764">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>“Reset orientation on show” option is persistent -</p>
</blockquote>
</aside>
<p>Thanks. I do have comment on both “Reset orientation on show” and “reset FOV”. Since these cannot be set on a per object basis, but rather global settings, I don’t think they belong to that right-click context menu. I think they should go to the Application Settings somewhere like Views.</p>
<p>Or if that’s considered too buried to change quickly, then somewhere in the Data module perhaps. It is just an awkward place to change an application behavior.</p>

---

## Post #10 by @lassoan (2025-05-14 05:47 UTC)

<p>We could indeed add the “Reset … on show” options to Application settings as well. We added to the right-click menu of the eye button first, because it tunes the behavior of left-clicking the eye icon and we assumed that users will find it easier there. But you are not the first user who asked about how to enable or disable this option.</p>
<p>Would you have found the option easier if it was in the Application settings / Views / Slice viewer defaults?</p>

---

## Post #11 by @muratmaga (2025-05-14 06:49 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="42764">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Would you have found the option easier if it was in the Application settings / Views / Slice viewer defaults?</p>
</blockquote>
</aside>
<p>I would, since I vaguely remembered this feature once from the forum, but couldn’t remember where it was. First place I looked was the Application Settingsm specifically Views, and I didn’t find there. Then <a class="mention" href="/u/mikebind">@mikebind</a> reminded me that it is through the visibility options.</p>

---

## Post #12 by @pieper (2025-05-14 17:40 UTC)

<p>If we add it to the Application Settings, let’s also leave it in the <code>eye</code> right click for consistentency.  Maybe add a separator and put global optinons after the separator and per-volume options above.  I don’t think a per-volume setting for this behavior makes sense, but I suppose it could be added.</p>

---

## Post #13 by @mikebind (2025-05-14 19:18 UTC)

<p>I indeed assumed that this was a per-volume setting because of where it was.  I hadn’t realized it was a global setting.  I don’t see any real need for it to be per-volume either, just assumed that from the UI access method.</p>

---
