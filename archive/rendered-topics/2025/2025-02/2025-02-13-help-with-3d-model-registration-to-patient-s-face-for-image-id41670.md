---
topic_id: 41670
title: "Help With 3D Model Registration To Patient S Face For Image"
date: 2025-02-13
url: https://discourse.slicer.org/t/41670
---

# Help with 3D Model Registration to Patient’s Face for Image-Guided Surgery in 3D Slicer

**Topic ID**: 41670
**Date**: 2025-02-13
**URL**: https://discourse.slicer.org/t/help-with-3d-model-registration-to-patient-s-face-for-image-guided-surgery-in-3d-slicer/41670

---

## Post #1 by @Navneet (2025-02-13 08:45 UTC)

<p>Hello everyone,</p>
<p>I am working on an <strong>image-guided surgery project</strong> using <strong>3D Slicer</strong>, where I need to <strong>register a 3D MRI model to a patient’s face in real time</strong>. The goal is to <strong>track the patient’s face using a webcam and markers (QR codes, ArUco, or AprilTags) and update the 3D model accordingly</strong>.</p>
<p>The system should work <strong>automatically</strong>—detect the marker, register the face, and continuously update the <strong>MRI model’s position in real-time</strong> as the patient moves.</p>
<p>Has anyone worked on <strong>real-time registration and tracking in 3D Slicer</strong>? Any guidance, example scripts, or best practices would be greatly appreciated!</p>
<p>Thanks in advance!</p>

---

## Post #2 by @pieper (2025-02-13 13:57 UTC)

<p>Yes, it’s definitely possible to do.  Here’s a prototype:</p>
<aside class="onebox githubrepo" data-onebox-src="https://github.com/pieper/facenav">
  <header class="source">

      <a href="https://github.com/pieper/facenav" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/70e4b5c496e0c9c6d733b61ba5a7bbeb/pieper/facenav" class="thumbnail">

  <h3><a href="https://github.com/pieper/facenav" target="_blank" rel="noopener">GitHub - pieper/facenav</a></h3>

    <p><span class="github-repo-description">Contribute to pieper/facenav development by creating an account on GitHub.</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The engineering questions are things like accuracy, performance, etc. while the clinical questions include line of sight requirements, changes in the patient’s face (swelling, muscle tone) and draping requirements.</p>

---

## Post #3 by @Navneet (2025-02-14 07:06 UTC)

<p>thank you so much this will be gonna helpful for me</p>

---
