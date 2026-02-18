# Seeking Guidance: Developing a Real-Time 3D Visualization System Using 3D Slicer and IGT

**Topic ID**: 41451
**Date**: 2025-02-02
**URL**: https://discourse.slicer.org/t/seeking-guidance-developing-a-real-time-3d-visualization-system-using-3d-slicer-and-igt/41451

---

## Post #1 by @Navneet (2025-02-02 13:09 UTC)

<p><strong>Hello 3D Slicer Community,</strong></p>
<p>I’m currently working on a project that involves real-time 3D visualization and tracking for image-guided surgery using <strong>3D Slicer</strong>. The goal is to create a system that integrates medical imaging data with tracking mechanisms to assist in procedures like brain tumor visualization and needle guidance.</p>
<p>I would greatly appreciate your insights, suggestions, or advice on the following aspects of the project:</p>

---

## Post #2 by @park (2025-02-02 14:12 UTC)

<p>Hi</p>
<p>I have similar experience as shown in the video.</p>
<p>—-</p>
<p>The first one is a basic image-guided navigation system.</p>
<div class="youtube-onebox lazy-video-container" data-video-id="lpnvMrpqjxs" data-video-title="Optical tracking using 3D Slicer + IGT" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=lpnvMrpqjxs" target="_blank" class="video-thumbnail" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/lpnvMrpqjxs/maxresdefault.jpg" title="Optical tracking using 3D Slicer + IGT" width="690" height="388">
  </a>
</div>

<p>—-</p>
<p>The second one combines image-guided navigation with simulation.<br>
This project was applied to focused ultrasound.</p>
<div class="youtube-onebox lazy-video-container" data-video-id="TRhmNf8oVCA" data-video-title="Real-time simulation-guided navigation system using 3D cGAN" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=TRhmNf8oVCA" target="_blank" class="video-thumbnail" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/TRhmNf8oVCA/maxresdefault.jpg" title="Real-time simulation-guided navigation system using 3D cGAN" width="690" height="388">
  </a>
</div>

<aside class="onebox allowlistedgeneric" data-onebox-src="https://www.sciencedirect.com/science/article/pii/S1053811923005621">
  <header class="source">
      <img src="https://sdfestaticassets-us-east-1.sciencedirectassets.com/shared-assets/103/images/favSD.ico" class="site-icon" width="" height="">

      <a href="https://www.sciencedirect.com/science/article/pii/S1053811923005621" target="_blank" rel="noopener nofollow ugc">sciencedirect.com</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:113/150;"><img src="https://ars.els-cdn.com/content/image/1-s2.0-S1053811923X00160-cov150h.gif" class="thumbnail" width="113" height="150"></div>

<h3><a href="https://www.sciencedirect.com/science/article/pii/S1053811923005621" target="_blank" rel="noopener nofollow ugc">Real-Time Acoustic Simulation Framework for tFUS: A Feasibility Study Using...</a></h3>

  <p>Transcranial focused ultrasound (tFUS), in which acoustic energy is focused on a small region in the brain through the skull, is a non-invasive therap…</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>If you think my experience would be helpful for your project, please feel free to contact me.</p>

---

## Post #3 by @Navneet (2025-02-02 15:47 UTC)

<p>Thank you for your response! Your experience with optical tracking and real-time simulation-guided navigation is exactly what I am looking for in my project. Your work with 3D Slicer and IGT sounds very impressive.<br>
I wanted to share an idea on how we could achieve tracking using a webcam. Below is a brief outline of the process:</p>

---

## Post #4 by @park (2025-02-03 13:33 UTC)

<p>Sorry to say, I cannot see the outline of your process.</p>

---

## Post #5 by @Navneet (2025-02-03 15:47 UTC)

<p>Oh sorry, I forgot to include the outline of my process earlier, so here it is:</p>
<h3><a name="p-122078-outline-of-the-process-1" class="anchor" href="#p-122078-outline-of-the-process-1" aria-label="Heading link"></a><strong>Outline of the Process:</strong></h3>
<p><strong>Step 1: Convert MRI Images to a 3D Model</strong></p>
<ul>
<li>I have patient MRI images that need to be converted into a 3D model.</li>
<li>Using 3D Slicer, I plan to segment the brain and tumor separately and generate a 3D model of the brain with the tumor.</li>
<li>The goal is to visualize the brain and tumor accurately in a 3D space for surgical planning.</li>
</ul>
<p><strong>Step 2: Align 3D Model with Patient’s Head Using a QR Marker</strong></p>
<ul>
<li>A QR marker is securely placed on the patient’s head to serve as a reference for real-time tracking.</li>
<li>The QR marker is tracked using the Plus Server in combination with 3D Slicer’s OpenIGTLink module.</li>
<li>Using fiducial registration, the MRI-based 3D model is aligned with the patient’s head position.</li>
</ul>
<p><strong>Step 3: Real-Time Tracking and Surgery Navigation</strong></p>
<ul>
<li>During surgery, the patient’s head movement is tracked in real time using the QR marker.</li>
<li>The aligned 3D model dynamically updates to reflect the live position of the patient’s head.</li>
<li>This setup aims to help surgeons visualize the tumor and surrounding anatomy precisely, enabling accurate navigation during surgery.</li>
</ul>
<hr>
<h3><a name="p-122078-request-for-support-2" class="anchor" href="#p-122078-request-for-support-2" aria-label="Heading link"></a><strong>Request for Support</strong></h3>
<p>I am seeking guidance from the 3D Slicer community on:</p>
<ol>
<li>Optimizing the workflow for real-time alignment and tracking using the QR marker.</li>
<li>Ensuring smooth integration between the Plus Server, OpenIGTLink, and 3D Slicer.</li>
<li>Any best practices or additional tools/modules to improve the accuracy and responsiveness of this setup.</li>
</ol>
<p>Thank you again for your support, and I look forward to hearing your thoughts!</p>

---

## Post #6 by @park (2025-02-03 23:10 UTC)

<p>Thanks for the sepcific request.</p>
<p>I think you following <a href="https://www.slicerigt.org/wp/user-tutorial/" rel="noopener nofollow ugc">this tutorial</a> step by step is very helpful to your project.</p>

---

## Post #7 by @Navneet (2025-02-04 04:26 UTC)

<p>Thank you for your response! very helpful for me</p>

---

## Post #9 by @Ziyu (2026-01-12 19:01 UTC)

<p>Hello, I can collaborate.</p>

---

## Post #10 by @Navneet (2026-01-12 19:05 UTC)

<p>Oh that’s nice. Yes we can collaborate</p>

---

## Post #11 by @Navneet (2026-01-24 20:07 UTC)

<p>oh yes we can collab</p>

---

## Post #12 by @kareem_abdelaziz (2026-01-25 12:39 UTC)

<p>Hey Iam working on something similar can I contact you?</p>

---
