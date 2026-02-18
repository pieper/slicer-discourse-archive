# There are some problems with the Windows version

**Topic ID**: 12484
**Date**: 2020-07-11
**URL**: https://discourse.slicer.org/t/there-are-some-problems-with-the-windows-version/12484

---

## Post #1 by @KIM_TY (2020-07-11 09:14 UTC)

<p>Thank you for providing us with a great program called 3D slicer for free.</p>
<p>There are some problems with the Windows version.</p>
<p>This is the same problem with MSI, ASUS gaming laptop, and high-performance PC.(window 10 pro)</p>
<ul>
<li>Version 4.10.2 does not have an editor. &lt;-Unable to make tensor image.</li>
</ul>
<p>4.11.X</p>
<ul>
<li>
<p>There is no slicerDcm2nii in the 4.11.x version coming out after June 2020.</p>
</li>
<li>
<p>Install SlicerDMRI extension is currently unavailable. &lt;- Installation is possible, but there is no change.</p>
</li>
<li>
<p>The program terminates in sliderDMRI loading while loading the Dicom file.&lt;- If uninstall the sliderDMRI, can load it normally.</p>
</li>
<li>
<p>When start the 3D slider:<br>
There are other DICOM listener running.<br>
Do you want to end them?<br>
There is an error.</p>
</li>
</ul>
<p>I would like to express my infinite gratitude to those who make this program.</p>

---

## Post #2 by @jamesobutler (2020-07-11 11:27 UTC)

<aside class="quote no-group" data-username="KIM_TY" data-post="1" data-topic="12484">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kim_ty/48/7283_2.png" class="avatar"> KIM_TY:</div>
<blockquote>
<p>Version 4.10.2 does not have an editor. &lt;-Unable to make tensor image.</p>
</blockquote>
</aside>
<p>This other thread(linked below) has a lot of good details about this that can help guide you.</p>
<aside class="quote" data-post="1" data-topic="10408">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/b2d939/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/where-can-i-found-editor-module/10408">Where can I found Editor module</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi 
I am beginner in 3D Slicer. I want to segment the Brain Corpus callosum and Cerebellum. In training movies I  found the “Editor” models that can be helpful but in latest installed version (4.10.2 r28257) and in extensions ,  I can’t find Editor module to use. Only I can see Segment Editor that seems its function is different to " Editor" model.Please help how to find and integrate “Editor” . 
Thanks in advance
  </blockquote>
</aside>

<aside class="quote no-group" data-username="KIM_TY" data-post="1" data-topic="12484">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kim_ty/48/7283_2.png" class="avatar"> KIM_TY:</div>
<blockquote>
<p>There is no slicerDcm2nii in the 4.11.x version coming out after June 2020.</p>
</blockquote>
</aside>
<p>Are you saying the SlicerDcm2nii extension is unavailable on the extensions manager?  Or after you install it, it doesn’t function/you can’t use it? It might be this issue related to the time you check for the extension.</p>
<aside class="quote quote-modified" data-post="4" data-topic="11946">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/extension-manager-problems/11946/4">Extension manager problems</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    It is also a timing issue - between about 1am-10am EST, extensions are not available yet for the latest Slicer Preview Release (see some more information and solution <a href="https://discourse.slicer.org/t/is-it-possible-to-do-a-segmentation-of-the-lumbar-spine-from-ct-data-and-use-the-3d-model-igs-for-further-finite-element-analysis-in-abaqus-or-febio/10444/17">here</a>). 

You need to do this only once. All recent (not more than a few months old) Slicer Preview Releases can work from the same DICOM database. If you open the same database with an older Slicer version (e.g., 4.10) then it will downgrade the database. I would suggest not to mix Slicer-4.10 and 4.11 and just use recent Slicer-4.…
  </blockquote>
</aside>

<p>As it relates to SlicerDMRI, it looks like code maintenance on it hasn’t been that frequent over the past year so there is likely a good chance that extension could be broken or breaking other things.</p>
<ul>
<li>It appears many tests are failing for it because it is trying to look for testing datasets within the Slicer source code that have been moved to SlicerTestingData (<a href="https://github.com/SlicerDMRI/SlicerDMRI/issues/130" class="inline-onebox" rel="noopener nofollow ugc">Update broken testing data usage · Issue #130 · SlicerDMRI/SlicerDMRI · GitHub</a>)</li>
<li>On Windows there are build errors building a test which look familiar to what me and <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> ran into during the transition to using an updated Visual studio toolkit. We ended up just disabling the tests which could probably be done again in the short term to fix the build issue.</li>
</ul>
<aside class="quote no-group" data-username="KIM_TY" data-post="1" data-topic="12484">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kim_ty/48/7283_2.png" class="avatar"> KIM_TY:</div>
<blockquote>
<p>When start the 3D slider:<br>
There are other DICOM listener running.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/lassoan">@lassoan</a> might know more about this topic, but you can disable it by pasting this code in the Slicer python console and then restart.</p>
<p><code>slicer.app.settings().setValue("DICOM/RunListenerAtStart", False)</code></p>

---

## Post #3 by @Sam_Horvath (2020-07-13 14:11 UTC)

<p>I have put up a pull request on SlicerDMRI to disable the broken tests.</p>

---

## Post #4 by @lassoan (2020-07-13 14:19 UTC)

<p>[quote=“jamesobutler, post:2, topic:12484”]</p>
<aside class="quote no-group" data-username="KIM_TY" data-post="1" data-topic="12484">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kim_ty/48/7283_2.png" class="avatar"> KIM_TY:</div>
<blockquote>
<p>When start the 3D slider:<br>
There are other DICOM listener running.</p>
</blockquote>
</aside>
<p>This means that DCMTK toolkit’s DICOM store SCP process (storescp.exe) is running. If you haven’t started it and you haven’t installed any other software that uses it then most likely 3D Slicer started it, because you enabled it in the DICOM module. In Slicer-4.11, you can enable/disable it by clicking on “Storage listener” checkbox in DICOM module’s networking section.</p>

---
