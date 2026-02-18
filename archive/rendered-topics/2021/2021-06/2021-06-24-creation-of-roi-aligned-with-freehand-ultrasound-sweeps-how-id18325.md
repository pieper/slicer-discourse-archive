# Creation of ROI aligned with freehand ultrasound sweeps -- how to rotate the ROI?

**Topic ID**: 18325
**Date**: 2021-06-24
**URL**: https://discourse.slicer.org/t/creation-of-roi-aligned-with-freehand-ultrasound-sweeps-how-to-rotate-the-roi/18325

---

## Post #1 by @AurelieS (2021-06-24 14:59 UTC)

<p>Hi,</p>
<p>I think my question is quite a beginner question, but since a year now I am doing freehand 3D ultrasound and I just realised that the ROI I am using has a lot of impact on my volume reconstruction.<br>
I am therefore trying to adjust the ROI the more possible to the axis of my sweeps.<br>
However I cannot find how to rotate the ROI ? I tried applying a transform to the ROI, but then the volume reconstruction did not work anymore …</p>
<p>Thanks in advance for your help,<br>
Cheers,<br>
Aurélie</p>

---

## Post #2 by @lassoan (2021-06-25 18:19 UTC)

<p>Currently in the Volume Reconstructor module in Slicer you cannot specify axis directions. I’ve submitted an issue to make sure it gets implemented:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/IGSIO/SlicerIGSIO/issues/11">
  <header class="source">

      <a href="https://github.com/IGSIO/SlicerIGSIO/issues/11" target="_blank" rel="noopener">github.com/IGSIO/SlicerIGSIO</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/IGSIO/SlicerIGSIO/issues/11" target="_blank" rel="noopener">Allow defining rotated ROI using Markups ROI</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-06-25" data-time="18:14:47" data-timezone="UTC">06:14PM - 25 Jun 21 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">We need to add support to markups ROI. It would allow specifying rotated ROIs.
<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">
https://github.com/IGSIO/SlicerIGSIO/blob/837b01ea2702fafa19a7fbba0c492bcc339e91dd/VolumeReconstruction/Logic/vtkSlicerVolumeReconstructionLogic.cxx#L245-L247</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Would you like to give it a try and implement it. We can help you getting started, but it requires basic C++ programming skills.</p>
<p>Alternatively, you can rotate your entire reference coordinate system by applying adding a custom transformation. For example, you can add <code>ReferenceToRotatedReference</code>) and send all transforms and images in <code>RotatedReference</code> instead of <code>Reference</code>.</p>

---

## Post #3 by @AurelieS (2021-06-28 09:11 UTC)

<p>Thank you for your quick answer.<br>
I apologize but I do not think I have the skills to implement this in Slicer …</p>
<p>As you offered, I applied a custom transformation to my full trial and the volume reconstruction worked well !<br>
However, my ROI and the axis of my sweeps change for each acquisition I do, since I am sweeping different muscles of different sizes in different body positions … . so it would be a lot easier for me if it was possible to directly adjust the ROI size and orientation.</p>
<p>How can I be kept updated if that becomes possible someday?<br>
Thanks again,<br>
Cheers,<br>
Aurélie</p>

---

## Post #4 by @lassoan (2021-06-28 14:06 UTC)

<aside class="quote no-group" data-username="AurelieS" data-post="3" data-topic="18325">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/87869e/48.png" class="avatar"> AurelieS:</div>
<blockquote>
<p>How can I be kept updated if that becomes possible someday?</p>
</blockquote>
</aside>
<p>Watch the issue referenced above. I think you can set automatic email notification when the state of the issue changes.</p>

---

## Post #5 by @AurelieS (2023-03-02 13:46 UTC)

<p>Dear Andras,<br>
I see that this issue has been resolved on the 21st of November 2021.<br>
Has it been developped only on PlusServer (as a code line) or also directly in the 3D Slicer GUI ?<br>
Thanks in advance for your help.<br>
Best regards,<br>
Aurélie Sarcher</p>

---

## Post #6 by @lassoan (2023-03-02 19:29 UTC)

<p>You can rotate the ROI in the Slicer GUI. Right-click on it and in “Interaction options” submenu enable “Rotation”</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ea84829c6422809b3ff35ecc3c517e40bf74e78e.jpeg" data-download-href="/uploads/short-url/xsDD3fgvS2jotWbJAJx1KHbwDng.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ea84829c6422809b3ff35ecc3c517e40bf74e78e_2_690x143.jpeg" alt="image" data-base62-sha1="xsDD3fgvS2jotWbJAJx1KHbwDng" width="690" height="143" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ea84829c6422809b3ff35ecc3c517e40bf74e78e_2_690x143.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ea84829c6422809b3ff35ecc3c517e40bf74e78e_2_1035x214.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ea84829c6422809b3ff35ecc3c517e40bf74e78e_2_1380x286.jpeg 2x" data-dominant-color="34353D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1614×336 81.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
