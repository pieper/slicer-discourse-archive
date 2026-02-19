---
topic_id: 4644
title: "Runtime Errors Due To Failure To Create Temp Folder"
date: 2018-11-05
url: https://discourse.slicer.org/t/4644
---

# Runtime errors due to failure to create temp folder

**Topic ID**: 4644
**Date**: 2018-11-05
**URL**: https://discourse.slicer.org/t/runtime-errors-due-to-failure-to-create-temp-folder/4644

---

## Post #1 by @fedorov (2018-11-05 20:02 UTC)

<p>I was helping a user who was not able to run certain functionality, and in the end it boiled down to failure to access the temp folder. This was with the latest nightly.</p>
<blockquote>
<p>Looking at the critical errors in the error log (see below), I see that the application failed to create folders in /tmp/folders, so I changed the permissions on that folder to allow everyone access, and then the images loaded without error.</p>
</blockquote>
<p>Should there be some extra check added to tell users if permissions are incompatible? Otherwise, it is not possible to figure this out without looking at the log, and beginner users will never think to look into it. In this particular case, the manifestation of the problem was failure to load a DICOM series with a plugin that did conversion and needed access to temp folder.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2f1a76f2314d91b797465e74d9d791eff6e3aab3.jpeg" data-download-href="/uploads/short-url/6IH8LfVIQbFKApSt4tGGqJsZ2VB.jpeg?dl=1" title="cpgepkkhpkkhmmea"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2f1a76f2314d91b797465e74d9d791eff6e3aab3_2_690x269.jpeg" alt="cpgepkkhpkkhmmea" data-base62-sha1="6IH8LfVIQbFKApSt4tGGqJsZ2VB" width="690" height="269" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2f1a76f2314d91b797465e74d9d791eff6e3aab3_2_690x269.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2f1a76f2314d91b797465e74d9d791eff6e3aab3_2_1035x403.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2f1a76f2314d91b797465e74d9d791eff6e3aab3.jpeg 2x" data-dominant-color="E7E7F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">cpgepkkhpkkhmmea</span><span class="informations">1319×515 168 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2018-11-06 16:58 UTC)

<p>Yes, it would be good to fix this.  I think this soft of issue crops up on macs when the user settings are migrated from one machine to another, or maybe also on OS upgrades.</p>

---

## Post #3 by @fedorov (2018-11-06 17:11 UTC)

<p>issue submitted <a href="https://issues.slicer.org/view.php?id=4652">https://issues.slicer.org/view.php?id=4652</a></p>

---
