---
topic_id: 10459
title: "Dicom Import Can Be Attempted Before Creating Database"
date: 2020-02-27
url: https://discourse.slicer.org/t/10459
---

# DICOM import can be attempted before creating database

**Topic ID**: 10459
**Date**: 2020-02-27
**URL**: https://discourse.slicer.org/t/dicom-import-can-be-attempted-before-creating-database/10459

---

## Post #1 by @muratmaga (2020-02-27 06:05 UTC)

<p>Actually on this note I should mention that behavior of DICOMBrowser for the new users of Slicer is confusing. See the screenshot below. Even though there is an error message indicating that the DICOM DB needs to be created/specified, you can still click the import tab, and actually go through the import process (but end of with 0 patients imported).</p>
<p>Either make the error message much more visible, or gray out the import tab until a database is created. I am not sure if this is <a class="mention" href="/u/patrick">@Patrick</a> issue, but during the workshop this threw off a lot of new users…</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/6406747625e030a11c2f099aa38cf4da8de7e174.png" data-download-href="/uploads/short-url/egRzKH9TGwowi6R5VXSwTO8LE5m.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/6406747625e030a11c2f099aa38cf4da8de7e174_2_690x203.png" alt="image" data-base62-sha1="egRzKH9TGwowi6R5VXSwTO8LE5m" width="690" height="203" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/6406747625e030a11c2f099aa38cf4da8de7e174_2_690x203.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/6406747625e030a11c2f099aa38cf4da8de7e174_2_1035x304.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/6406747625e030a11c2f099aa38cf4da8de7e174_2_1380x406.png 2x" data-dominant-color="F1F0E6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2497×736 70.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2020-02-27 18:25 UTC)

<p>Thanks for reporting this <a class="mention" href="/u/muratmaga">@muratmaga</a>.  As far as I know this is new behavior with the redesign of the module.  <a class="mention" href="/u/lassoan">@lassoan</a> was there a reason not to auto-create a database in the user’s Documents folder?</p>

---

## Post #3 by @lassoan (2020-02-27 19:59 UTC)

<p>There were lots of issues in the old DICOM browser with actions automatically happening (and failing) and showing error popups, blocking the user (or automatic scripts) or covering other popups. The main design now is that we never block the GUI, show high-level errors/warnings on the GUI and let the users dig into the logs if they want to know more about the exact underlying issues.</p>
<p>I agree that we should give earlier feedback to the user that DICOM database has not been created yet. Maybe we could even try to automatically create one when needed. We must be very careful to do these at the user interface level to make sure we never block any test or batch processing scripts by GUI popups.</p>

---

## Post #4 by @pieper (2020-02-28 19:17 UTC)

<p>Yes, why don’t we just disable the import button if there’s no valid database?</p>

---
