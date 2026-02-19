---
topic_id: 3321
title: "New Guy With Roi Question"
date: 2018-06-27
url: https://discourse.slicer.org/t/3321
---

# New Guy With ROI Question

**Topic ID**: 3321
**Date**: 2018-06-27
**URL**: https://discourse.slicer.org/t/new-guy-with-roi-question/3321

---

## Post #1 by @Zenbiker (2018-06-27 19:41 UTC)

<p>Trying to create .stl file from ROI created: DICOM, Volume Rendering, Editor/Make Model.  When I select Make Model, the entire volume reappears attahed to the ROI and the .stl file is a representation of the entire volume. Watched multiple tutorials, don’t know what I’m missing.  Thanks in advance.</p>

---

## Post #2 by @cpinter (2018-06-27 23:35 UTC)

<p>Hi! If I understand correctly what you’re trying to do, then please read this topic first.</p><aside class="quote quote-modified" data-post="1" data-topic="524">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/b19c9b/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/save-volume-rendering-as-stl-file/524">Save volume rendering as STL file</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hello, I am a new user on 3D slicer. 
I was using the display preset feature under volume rendering, and I was wondering if there is a way to save what I was viewing as an .stl or 3D printable file. 
For example, I was viewing a sample MRI using the CT-cardiac3 preset display. 
When I tried to save that specific 3D preset displayed sample in a .stl file, the option was unavailable. 
I was only able to see .vp (volume property), .txt formats. 
Is there a way to accomplish what I desire in 3D slic…
  </blockquote>
</aside>

<p>You’ll probably need to use the Segment Editor module in the end. Let us know if you need help with segmentation.</p>

---

## Post #3 by @Zenbiker (2018-06-29 17:52 UTC)

<p>Thank you.  At the risk of being repetitive, I believe I am missing a step comparing the current Slicer build to the tutorial video I watched on YouTube.  In that video, DICOM data was loaded and Volume Rendering created the virtual model.  The Editor Module was used with “Enable Cropping” and “Display ROI”.  After cropping, the ROI was refined using preset features - I’ve been using CT-AA2.  Here is where I leave the rails:  At this point I have my ROI defined and designated with presets.  When I initiate the “Make Model” tool in Editor, the model is not just my ROI; the original volume I cropped away is incorporated into the .stl file.  Obviously the process has changed since the tutorial.  I will try Segment Editor; if I can’t make that work,  I’ll be back for another nudge in the proper direction.</p>
<p>Edit:  my solution was much more basic for now, and am posting hoping it helps another; in Editor, using the “Apply Paint” tool &amp; designating the areas in the ROI to be included in the final model before using the “Make Model” effect.  So much to learn, thank you again.</p>

---
