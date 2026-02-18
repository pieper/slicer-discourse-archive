# How to disable synchronous marking of axial and sagittal slice

**Topic ID**: 29253
**Date**: 2023-05-02
**URL**: https://discourse.slicer.org/t/how-to-disable-synchronous-marking-of-axial-and-sagittal-slice/29253

---

## Post #1 by @PolinaPostnikova (2023-05-02 18:35 UTC)

<p>Hello. Could you please tell me how to disable synchronous marking of axial and sagittal slice on MRI?</p>
<p>Thanx</p>

---

## Post #2 by @lassoan (2023-05-02 18:39 UTC)

<p>Can you explain a bit more what you mean by “synchronous marking”?</p>
<p>Would you like markup points that are placed in an axial view only appear in that view and not in the sagittal view? You can do that by drag-and-dropping the markup from the data tree (in Data module) to the view you would like the markups to appear.</p>
<p>Can you tell more about your workflow? What is your end goal?</p>

---

## Post #3 by @PolinaPostnikova (2023-05-03 08:07 UTC)

<p>Dear Andras, thanks for your reply!<br>
Could you please send instructions on where to find the data tree and Data module?<br>
I’m segmenting an MRI of the spine to train a neural network. Now, when I segment the axial slice, the sagittal slice is automatically segmented (but not correctly, since the sagittal slice is not a reconstruction of the axial slice, but a separate scan). I would like to segment them separately from each other.</p>

---

## Post #4 by @lassoan (2023-05-06 18:11 UTC)

<aside class="quote no-group" data-username="PolinaPostnikova" data-post="3" data-topic="29253">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/d78d45/48.png" class="avatar"> PolinaPostnikova:</div>
<blockquote>
<p>where to find the data tree and Data module?</p>
</blockquote>
</aside>
<p>You can switch modules using the <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#application-overview">toolbar</a>. I usually click on the search icon (magnifier) and type the module name.</p>
<aside class="quote no-group" data-username="PolinaPostnikova" data-post="3" data-topic="29253">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/d78d45/48.png" class="avatar"> PolinaPostnikova:</div>
<blockquote>
<p>Now, when I segment the axial slice, the sagittal slice is automatically segmented (but not correctly, since the sagittal slice is not a reconstruction of the axial slice, but a separate scan)</p>
</blockquote>
</aside>
<p>It should be all correct, probably you don’t need to do anything differently. Slicer automatically shows reformatted views of the axial slices in not just axial but in coronal and sagittal planes as well. This helps with doing the segmentation more consistently and accurately.</p>
<p>If you still have questions then maybe you could share a few screenshots mark how you would like to change the visualization.</p>

---
