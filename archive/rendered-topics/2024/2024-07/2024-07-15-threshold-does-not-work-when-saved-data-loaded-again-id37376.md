# Threshold does not work when saved data loaded again

**Topic ID**: 37376
**Date**: 2024-07-15
**URL**: https://discourse.slicer.org/t/threshold-does-not-work-when-saved-data-loaded-again/37376

---

## Post #1 by @Figaya (2024-07-15 11:33 UTC)

<p>Hello,</p>
<p>The threshold does not apply when I perform the following steps:</p>
<ol>
<li>Load MRHead sample data.</li>
<li>Go to the Segment Editor module.</li>
<li>Add a segment.</li>
<li>Open the Threshold effect (<strong>DO NOT</strong> APPLY THE THRESHOLD NOW).</li>
<li>Press CTRL+S and save the scene into an .mrb bundle.</li>
<li>Close the scene, selecting the discard modifications option in the pop-up.</li>
<li>Click on Data, choose the .mrb bundle file you previously saved, and load it.</li>
<li>You will see the same GUI state with the Threshold effect opened on the segment you created.</li>
<li>Click the Apply button for the Threshold.</li>
<li>You should see that no threshold is applied to the segment.</li>
</ol>
<p>Is this a bug or something?</p>

---

## Post #2 by @lassoan (2024-07-15 11:40 UTC)

<p>Thank you for reporting. I believe this has been already fixed in recent Slicer versions, but let us know if you can still reproduce it with the latest Slicer Preview Release.</p>

---

## Post #3 by @Figaya (2024-07-17 11:59 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>I’ve tested in the latest preview version <code>5.7.0 revision 32947 built 2024-07-16</code> but it is still reproducible.</p>
<p>Thank you.</p>

---

## Post #4 by @allie_qd (2025-01-27 21:18 UTC)

<p>I am also having this problem!</p>

---
