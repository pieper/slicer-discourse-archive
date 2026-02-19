---
topic_id: 33408
title: "Resources Available For Mpr In Slicer"
date: 2023-12-15
url: https://discourse.slicer.org/t/33408
---

# Resources available for MPR in Slicer

**Topic ID**: 33408
**Date**: 2023-12-15
**URL**: https://discourse.slicer.org/t/resources-available-for-mpr-in-slicer/33408

---

## Post #1 by @ndelgado (2023-12-15 23:46 UTC)

<p>What resources are available for using MPR in Slicer?</p>

---

## Post #2 by @Andinet_Enquobahrie (2023-12-16 10:19 UTC)

<p>I can think of two options</p>
<ol>
<li>
<p>Using the reformat widget for interactive manipulation of the slice orientation.</p>
</li>
<li>
<p>Thick slab reconstruction option</p>
</li>
</ol>
<aside class="quote quote-modified" data-post="1" data-topic="32432">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sam_horvath/48/3092_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/new-feature-thick-slab-reconstruction-from-slice-controllers-and-views/32432">New feature: Thick slab reconstruction from slice controllers and views</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Thick slab reconstruction (TSR) can now be enabled and modified from the slice controllers and slice views! 
Enabling thick slab reconstruction as well as selection of the composite method (min, max, mean or sum) has been available through the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository/volumes.html#thick-slab-reconstruction-and-maximum-minimum-intensity-volume-projections" rel="noopener nofollow ugc">python console</a>. 
Now these options are available through both the slice controller and the right-click context menu on the slice views.  If the interactive option is selected, the thickness, angle and position of the TSR can be adjusted by moving the slice…
  </blockquote>
</aside>


---

## Post #3 by @philippepellerin (2023-12-19 08:49 UTC)

<p>Where can I find the “reformat widget for interactive manipulation of the slice orientation.”?<br>
For many years I have used Osirix, thenafter Horos for some precise CT scan orientation with their MPR engine, which is precise and convenient. I can’t find a way to do the same with 3D slicer, maybe that this widget would be the solution? would you have a solution for doing a very acurate orientation and reslicing?<br>
Thank for any help, season greetings.</p>

---

## Post #4 by @bbkonk (2023-12-20 19:25 UTC)

<p>Is it possible to manipulate the MPR volumes in slicer similar to the below video? I’ve seen this capability in similar software. The Reformat Widget seems to get the job done, but is a little clunkier to work with.</p>
<p><a href="https://urldefense.com/v3/__https://ars.els-cdn.com/content/image/1-s2.0-S1936879819319909-mmc1.mp4__;!!May37g!KuFyPQFDBa1B2YqxCzbxTo89Ix4VIk6R5BoxH-LEG5bTNQ00LfhG4mN06CoYqyXi3An-pY347-TVZHZeD0E1Gl1tCXDp$" rel="noopener nofollow ugc">https://urldefense.com/v3/__https://ars.els-cdn.com/content/image/1-s2.0-S1936879819319909-mmc1.mp4__;!!May37g!KuFyPQFDBa1B2YqxCzbxTo89Ix4VIk6R5BoxH-LEG5bTNQ00LfhG4mN06CoYqyXi3An-pY347-TVZHZeD0E1Gl1tCXDp$</a></p>

---

## Post #5 by @Andinet_Enquobahrie (2023-12-22 11:50 UTC)

<p>Here is a demonstration of how you can use Reformat Widget for MPR in 3D Slicer</p>
<aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/15WnsSEcOZBV-zKf8sNwCBQ2Tdb4XhtIf/view?usp=sharing">
  <header class="source">

      <a href="https://drive.google.com/file/d/15WnsSEcOZBV-zKf8sNwCBQ2Tdb4XhtIf/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/15WnsSEcOZBV-zKf8sNwCBQ2Tdb4XhtIf/view?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/15WnsSEcOZBV-zKf8sNwCBQ2Tdb4XhtIf/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">Reformat-widget-demo.mp4</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>And Thick-Slab Reconstruction</p>
<aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1ZffG3o4GX1DR8R25MZIvNUiWpui5GejI/view?usp=sharing">
  <header class="source">

      <a href="https://drive.google.com/file/d/1ZffG3o4GX1DR8R25MZIvNUiWpui5GejI/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1ZffG3o4GX1DR8R25MZIvNUiWpui5GejI/view?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1ZffG3o4GX1DR8R25MZIvNUiWpui5GejI/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">ThickSlabReconstructionDemo-Slicer.mp4</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Hope this helps</p>
<p>Andinet</p>

---

## Post #6 by @philippepellerin (2023-12-26 09:04 UTC)

<p>Dear Andinet, thanks for your replay, It look as if the thick slab will do the job, but my computer don’t support the last issue of slicer, I hope that Santa Claus will bring me a new one.<br>
The reformat widget  lack of accurancy for my purpose.<br>
Season greetings</p>

---

## Post #7 by @pieper (2023-12-26 19:21 UTC)

<aside class="quote no-group" data-username="philippepellerin" data-post="6" data-topic="33408">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/philippepellerin/48/16062_2.png" class="avatar"> philippepellerin:</div>
<blockquote>
<p>, but my computer don’t support the last issue of slicer</p>
</blockquote>
</aside>
<p>Has this issue already been reported?  If so please cross-reference the issue here and note what kind of computer you have an what issues prevent the latest versions from working.</p>
<aside class="quote no-group" data-username="philippepellerin" data-post="6" data-topic="33408">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/philippepellerin/48/16062_2.png" class="avatar"> philippepellerin:</div>
<blockquote>
<p>The reformat widget lack of accurancy for my purpose.</p>
</blockquote>
</aside>
<p>Did you try going into the Reformat module?  It offers options control of the plane, although the interface may not be ideal for your purposes.</p>

---

## Post #8 by @philippepellerin (2023-12-27 11:01 UTC)

<p>Thanks for the suggestion. I tried it as well, but no, it does not fit my requirements.<br>
All the same, it is not a big deal to do the reslicing with Horos and then import the h5 file.<br>
Best.</p>

---

## Post #9 by @bbkonk (2024-01-10 18:05 UTC)

<p>Is there a way to re-orient the view using cross-hairs similar to other dicom viewers? The slicer arrows are challenging to manipulate</p>

---

## Post #10 by @bbkonk (2024-01-23 03:44 UTC)

<p>Just confirming: there’s no equivalent in slicer of the crosshair guided MPR tool here: (<a href="https://ars.els-cdn.com/content/image/1-s2.0-S1936879819319909-mmc1.mp4" rel="noopener nofollow ugc">https://ars.els-cdn.com/content/image/1-s2.0-S1936879819319909-mmc1.mp4</a>). I’ve seen this in some other viewers (e.g. RadiAnt) as well.</p>

---

## Post #11 by @rfenioux (2024-01-23 08:31 UTC)

<p>You can do this by clicking the slice intersection button, and checking the Interaction box in the dropdown menu</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d06e9b9a0f24e67d4499c9de2a15589481a707ae.png" alt="image" data-base62-sha1="tJShYOoWRthAw5N3myq4hDSYNcy" width="415" height="267"></p>

---

## Post #12 by @lassoan (2024-01-23 14:19 UTC)

<p>I would just add that after enabling slice intersections, if you don’t want to make slice intersection lines interactive then you can translate slice views by holding down shift key while moving the mouse, or rotate slice views by Ctrl + Alt + Left-click-and-drag.</p>

---

## Post #13 by @bbkonk (2024-01-23 14:22 UTC)

<p>Thank you both! I knew I had to be missing it</p>

---
