# Warnings detected during DICOM load

**Topic ID**: 10614
**Date**: 2020-03-10
**URL**: https://discourse.slicer.org/t/warnings-detected-during-dicom-load/10614

---

## Post #1 by @Taehyeong (2020-03-10 12:41 UTC)

<p>Import CT dicom image included structure~ . message find out!!<br>
Warnings detected during load.  Examine data in Advanced mode for details.  Load anyway?<br>
Could not load: 19: ARIA RadOnc Structure Sets as a Scalar Volume</p>
<p>How to import the structure?<br>
already installed slicer RT</p>

---

## Post #2 by @pieper (2020-03-10 14:34 UTC)

<p><a href="https://www.slicer.org/wiki/Documentation/4.10/FAQ/DICOM" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/4.10/FAQ/DICOM</a></p>

---

## Post #3 by @lassoan (2020-03-10 15:13 UTC)

<aside class="quote no-group" data-username="Taehyeong" data-post="1" data-topic="10614">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/90db22/48.png" class="avatar"> Taehyeong:</div>
<blockquote>
<p>Could not load: 19: ARIA RadOnc Structure Sets as a Scalar Volume</p>
</blockquote>
</aside>
<p>If structure set is attempted to be loaded by Scalar Volume plugin (as the error message suggests) then it means SlicerRT did not recognize the series - most likely it was not installed (or the installation was incorrect/incomplete).</p>
<p>Try to uninstall SlicerRT and install it again (wait until the “Restart” button becomes enabled in Extension manager, don’t close the window and restart the button manually).</p>
<p>If that fails then follow further instructions in the DICOM FAQ as Steve suggested above.</p>

---
