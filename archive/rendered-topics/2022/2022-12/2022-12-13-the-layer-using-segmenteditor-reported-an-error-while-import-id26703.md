# The layer using segmentEditor reported an error while importing dicom data

**Topic ID**: 26703
**Date**: 2022-12-13
**URL**: https://discourse.slicer.org/t/the-layer-using-segmenteditor-reported-an-error-while-importing-dicom-data/26703

---

## Post #1 by @FUFU (2022-12-13 07:53 UTC)

<p>When importing dicom data, the segmentEditor function was found to be faulty. When you use Paint and Erase, it will go to the next layer, not the current one.<br>
</p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b067f9cc147831e0c1d30c6c88e9f0cdd428ed9.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b067f9cc147831e0c1d30c6c88e9f0cdd428ed9.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b067f9cc147831e0c1d30c6c88e9f0cdd428ed9.mp4</a>
    </source></video>
  </div><p></p>
<p>The same goes for using slicer’s built-in segmentEditor</p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/26c69b5224aeedabf5830bf85459b6eb3b24562f.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/26c69b5224aeedabf5830bf85459b6eb3b24562f.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/26c69b5224aeedabf5830bf85459b6eb3b24562f.mp4</a>
    </source></video>
  </div><br>
Thank you!!!<p></p>

---

## Post #2 by @pieper (2022-12-13 13:19 UTC)

<p>Thanks for reporting.  That doesn’t happen for me with current releases and any of the data I use.  Are you able to replicate this issue with sample data and the regular Slicer release?</p>

---

## Post #3 by @FUFU (2022-12-14 01:26 UTC)

<p>I don’t have this problem with sample data, I do with this data</p>

---

## Post #4 by @pieper (2022-12-14 02:52 UTC)

<p>We may not be able to help if we cannot replicate the issue with data available to us.</p>

---

## Post #5 by @lassoan (2022-12-14 06:52 UTC)

<p>This can happen if the slice view is positioned exactly between two slices (probably a side effect of loading from and old scene). Hold down the Shift key and move the mouse in any other view (yellow or green) to ensure that the red slice view is not positioned right between two slices.</p>

---

## Post #6 by @FUFU (2022-12-15 07:08 UTC)

<p>Can I send you the data？</p>

---

## Post #7 by @lassoan (2022-12-15 14:36 UTC)

<p>Yes, sure, upload anywhere (dropbox, onedrive, etc.) and post the link here. Make sure the image does not contain patient information.</p>

---
