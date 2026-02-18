# 3D viewer stops working after segmentation

**Topic ID**: 9419
**Date**: 2019-12-06
**URL**: https://discourse.slicer.org/t/3d-viewer-stops-working-after-segmentation/9419

---

## Post #1 by @kgeary (2019-12-06 19:50 UTC)

<p>Hello,</p>
<p>I am trying to segment out different bone fragments from a CT scan of an ankle fracture. After creating the separate fragments (during which the 3D viewer worked the entire time) I attempted to export to .stl files. The .stl files do not open in the next software I need to use and the 3d viewer stopped working in slicer. I can only see 1/12 segments in 3d.</p>
<p>The eyeball is open for all of them, but I can only see my last segment.</p>
<p>Any thoughts?</p>

---

## Post #2 by @lassoan (2019-12-06 19:57 UTC)

<p>We would need to know a bit more to be able to help with this:</p>
<ul>
<li>How much physical memory do you have in your computer and how large is the image you are working on?</li>
<li>What Slicer version do you use?</li>
<li>Do you see any errors or warning in the application log?</li>
<li>Can you share any of the files or at least a few screenshots?</li>
<li>Does everything work well if you save the scene, restart Slicer, load the saved scene, and export the segments again?</li>
<li>Do you use “Export to files” feature?</li>
<li>Can another instance of Slicer load the saved STL files?</li>
<li>Have you tried exporting to OBJ format?</li>
<li>Which Segment Editor effects did you use? If you used “Grow from seed”, “Watershed”, or “Fill between slices”, have you clicked “Apply” when preview results were good?</li>
</ul>

---

## Post #3 by @kgeary (2019-12-06 20:21 UTC)

<p>I have 952 GB of memory on my laptop which is running Windows 10</p>
<p>I have Slicer 4.10.2</p>
<p>There are no errors or warnings popping up</p>
<p>I cannot share screenshots or images at this time</p>
<p>I did try to save, close, reopen and reload to no avail. the problem persists upon reopening. exporting did not improve either.</p>
<p>I used the export to files feature</p>
<p>I have not tried exporting to obj as this is not a supported file type for my next step.</p>
<p>I used threshold and scissors and were sure to click apply when necessary. the segments were all fine, but suddenly the 3d view just stopped working</p>

---

## Post #4 by @lassoan (2019-12-06 20:45 UTC)

<aside class="quote no-group" data-username="kgeary" data-post="3" data-topic="9419">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/e19b73/48.png" class="avatar"> kgeary:</div>
<blockquote>
<p>I have 952 GB of memory on my laptop which is running Windows 10</p>
</blockquote>
</aside>
<p>Do you know how much memory (RAM) your computer has? Things may start to stop working if you run out of memory. You can configure more virtual memory (that uses disk space to make up for lack of physical memory) in Windows settings, but it’s better to confirm first that this is the problem.</p>
<aside class="quote no-group" data-username="kgeary" data-post="3" data-topic="9419">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/e19b73/48.png" class="avatar"> kgeary:</div>
<blockquote>
<p>I have Slicer 4.10.2</p>
</blockquote>
</aside>
<p>Please also try with latest Slicer preview release.</p>
<aside class="quote no-group" data-username="kgeary" data-post="3" data-topic="9419">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/e19b73/48.png" class="avatar"> kgeary:</div>
<blockquote>
<p>I did try to save, close, reopen and reload to no avail. the problem persists upon reopening.</p>
</blockquote>
</aside>
<p>Do you mean that segments do not appear after reopening? They do not appear in slice views either, or just do not appear in 3D views?</p>
<aside class="quote no-group" data-username="kgeary" data-post="3" data-topic="9419">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/e19b73/48.png" class="avatar"> kgeary:</div>
<blockquote>
<p>I have not tried exporting to obj as this is not a supported file type for my next step.</p>
</blockquote>
</aside>
<p>Please try obj file export as well and try loading the STL and OBJ files back to Slicer (this helps in determining if 3D mesh generation failed or it is just a display issue).</p>
<aside class="quote no-group" data-username="kgeary" data-post="3" data-topic="9419">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/e19b73/48.png" class="avatar"> kgeary:</div>
<blockquote>
<p>suddenly the 3d view just stopped working</p>
</blockquote>
</aside>
<p>This would indicate a video card driver crash, but that should be fixed by restarting of the computer and Slicer. So, it is most likely there is something else.</p>

---
