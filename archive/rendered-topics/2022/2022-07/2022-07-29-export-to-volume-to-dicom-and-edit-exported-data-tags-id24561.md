# Export to Volume to DICOM and Edit Exported Data Tags

**Topic ID**: 24561
**Date**: 2022-07-29
**URL**: https://discourse.slicer.org/t/export-to-volume-to-dicom-and-edit-exported-data-tags/24561

---

## Post #1 by @rhodesdante (2022-07-29 12:35 UTC)

<p>I am trying to edit ultrasound volumes such that on subsequent uses, they are automatically loaded in with my desired window/level–different from the one Slicer selects automatically. My thought process is as follows.</p>
<ol>
<li>Export the desired volume to DICOM format</li>
<li>Load in the volume as a DICOM file</li>
<li>Change the preferred window/level settings in a DICOM tag so that when I re-save, Slicer automatically renders it using the <a href="https://discourse.slicer.org/t/recent-improvements-in-window-level-management/7284">new settings.</a>
</li>
</ol>
<p>I am not sure how to accomplish the third step. Can I edit DICOM tags directly in Slicer? If so, how do I actually go about finding the correct tags?</p>
<p>If anyone knows how I might achieve this goal through this method (or another one) please let me know. Thank you!</p>

---

## Post #2 by @mikebind (2022-07-29 18:18 UTC)

<p>There is a “Create a DICOM Series”  module which allows you to choose a window center and width when exporting an image volume (but also requires that you fill in everything else from scratch).  If you have any python experience at all, pydicom is pretty easy to use.</p>
<p>You might find some additional helpful information in this discussion: <a href="https://discourse.slicer.org/t/modify-additional-dicom-tags-in-export/13830/7" class="inline-onebox">Modify additional DICOM tags in export - #7 by mikebind</a></p>

---

## Post #3 by @rhodesdante (2022-08-01 18:30 UTC)

<p>This seems to have worked well so far, thank you! I appreciate you linking to your previous post</p>

---
