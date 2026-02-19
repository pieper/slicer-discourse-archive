---
topic_id: 12997
title: "Create 3D Dicom Volume Rendering Slicelet"
date: 2020-08-14
url: https://discourse.slicer.org/t/12997
---

# Create 3d dicom volume rendering slicelet

**Topic ID**: 12997
**Date**: 2020-08-14
**URL**: https://discourse.slicer.org/t/create-3d-dicom-volume-rendering-slicelet/12997

---

## Post #1 by @Chintha_Siva_Prasad (2020-08-14 12:52 UTC)

<p>Operating system: Ubuntu 19.10<br>
Slicer version:4.10</p>
<p>How can I create .py(slicelet) that can render a 3d dicom volume?</p>

---

## Post #2 by @pieper (2020-08-14 14:49 UTC)

<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Slicelets" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Slicelets</a></p>

---

## Post #3 by @lassoan (2020-08-14 15:01 UTC)

<p>You can also find useful code snippets that load volume and display it using volume rendering in the script repository: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository</a></p>

---

## Post #4 by @Chintha_Siva_Prasad (2020-08-14 17:55 UTC)

<p>Actually I want four 3d volume rendering windows.So that I can load four volumes in each of the window.How can I create the layoutWidget(four 3d windows)? is there a built-in layout?<br>
Even if I created the layoutWidget, how can I load the volumes to respective windows?<br>
How can i write the logic that load the dicom to volume?I am too confused in this scenario.Please help me…</p>

---

## Post #5 by @Chintha_Siva_Prasad (2020-08-14 18:13 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b3277f824cd14468b6f66b4fe0083a7cc3adaaf8.png" data-download-href="/uploads/short-url/pyS5FzElmHLQqfnsDVYRhE6L1lS.png?dl=1" title="question" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b3277f824cd14468b6f66b4fe0083a7cc3adaaf8_2_689x146.png" alt="question" data-base62-sha1="pyS5FzElmHLQqfnsDVYRhE6L1lS" width="689" height="146" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b3277f824cd14468b6f66b4fe0083a7cc3adaaf8_2_689x146.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b3277f824cd14468b6f66b4fe0083a7cc3adaaf8_2_1033x219.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b3277f824cd14468b6f66b4fe0083a7cc3adaaf8.png 2x" data-dominant-color="FCFAF9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">question</span><span class="informations">1231×262 45.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
And also<br>
Getting this error while loading the DICOM too…</p>

---

## Post #6 by @pieper (2020-08-14 18:29 UTC)

<p>If you want four 3D views you need to make a custom layout using XML like here:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Customize_viewer_layout" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Customize_viewer_layout</a></p>
<p>Then make volume rendering display node for each and set the corresponding view node id to the view where you want it to appear.</p>
<p>To load dicom to volumes, follow the examples here:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#DICOM_2" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#DICOM_2</a></p>
<p>As a side note, when asking questions, it’s best to try narrowing down to a. specific question with a small snippet of code with the context to show what you tried and what happened.  Your screenshot only shows the error, not the input.</p>

---

## Post #7 by @mikebind (2020-08-14 18:30 UTC)

<p>That last error indicates that something you entered in the python interactor tried to iterate over a boolean value.  We can’t see what you entered, so we can’t tell what caused the error.</p>
<p>The Irregular volume geometry message is just a warning and did not cause the error.</p>

---

## Post #8 by @lassoan (2020-08-15 03:58 UTC)

<p>Without seeing your code, we can only guess. My guess would be that you use Slicer Stable version and you are trying an example code snippets provided for latest Slicer Preview version.</p>

---

## Post #9 by @Chintha_Siva_Prasad (2020-08-15 06:08 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b3277f824cd14468b6f66b4fe0083a7cc3adaaf8.png" data-download-href="/uploads/short-url/pyS5FzElmHLQqfnsDVYRhE6L1lS.png?dl=1" title="question" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b3277f824cd14468b6f66b4fe0083a7cc3adaaf8_2_689x146.png" alt="question" data-base62-sha1="pyS5FzElmHLQqfnsDVYRhE6L1lS" width="689" height="146" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b3277f824cd14468b6f66b4fe0083a7cc3adaaf8_2_689x146.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b3277f824cd14468b6f66b4fe0083a7cc3adaaf8_2_1033x219.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b3277f824cd14468b6f66b4fe0083a7cc3adaaf8.png 2x" data-dominant-color="FCFAF9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">question</span><span class="informations">1231×262 45.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
sorry for the incovinience…<br>
this is the code I used</p>

---

## Post #10 by @Chintha_Siva_Prasad (2020-08-15 06:13 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/382cbc17884769789d4e4585d0f5e9c1f1c47317.png" data-download-href="/uploads/short-url/80WA5tMQbwQcOMuF4gEqEGumQdN.png?dl=1" title="Screenshot from 2020-08-15 11-43-00" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/382cbc17884769789d4e4585d0f5e9c1f1c47317.png" alt="Screenshot from 2020-08-15 11-43-00" data-base62-sha1="80WA5tMQbwQcOMuF4gEqEGumQdN" width="690" height="94" data-dominant-color="36122B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-08-15 11-43-00</span><span class="informations">806×110 12.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
this image is more clear to understand the error</p>

---

## Post #11 by @lassoan (2020-08-15 13:50 UTC)

<p>Code snippets on the “Nightly” script repository page is for latest Slicer Preview version.</p>

---

## Post #12 by @Chintha_Siva_Prasad (2020-08-15 16:38 UTC)

<p>I had even checked the stable version code.But it didn’t tell how to get the volumenode of the loaded DICOM directory. How can I get the volume node of DICOM in stable version?</p>

---

## Post #13 by @lassoan (2020-08-15 17:44 UTC)

<p>I’ve just tried this <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_load_DICOM_files_into_the_scene_from_a_folder">DICOM file loading script</a> with the latest Slicer Preview release and it works well. List of volume node IDs are returned in <code>loadedNodeIDs</code> variable.</p>

---

## Post #14 by @Chintha_Siva_Prasad (2020-08-16 05:55 UTC)

<p>but its not working in the stable release…</p>

---

## Post #15 by @lassoan (2020-08-16 14:33 UTC)

<p>I would recommend to use the latest Preview Release. It should work well and contains many important improvements and fixes and we will release it as the new stable version in a couple of weeks. If you have any issue with the latest Preview Release then let us know.</p>

---

## Post #16 by @Chintha_Siva_Prasad (2020-08-16 15:10 UTC)

<p>OK I will use the preview version</p>

---

## Post #17 by @Chintha_Siva_Prasad (2020-08-17 07:05 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/721a1354d625af2289f52de32ecc492f60ccc6ca.png" data-download-href="/uploads/short-url/ghoiu82pK82n6JUX0yLk11RFd5U.png?dl=1" title="dicomcoDe" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/721a1354d625af2289f52de32ecc492f60ccc6ca_2_690x382.png" alt="dicomcoDe" data-base62-sha1="ghoiu82pK82n6JUX0yLk11RFd5U" width="690" height="382" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/721a1354d625af2289f52de32ecc492f60ccc6ca_2_690x382.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/721a1354d625af2289f52de32ecc492f60ccc6ca_2_1035x573.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/721a1354d625af2289f52de32ecc492f60ccc6ca.png 2x" data-dominant-color="F5F8F5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">dicomcoDe</span><span class="informations">1145×635 84.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
with this code I had created a layout with consists of two 3d windows…<br>
How to load a dicom volume into these windows?</p>

---

## Post #18 by @pieper (2020-08-17 20:55 UTC)

<aside class="quote no-group" data-username="Chintha_Siva_Prasad" data-post="17" data-topic="12997">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chintha_siva_prasad/48/7766_2.png" class="avatar"> Chintha_Siva_Prasad:</div>
<blockquote>
<p>with this code I had created a layout with consists of two 3d windows…<br>
How to load a dicom volume into these windows?</p>
</blockquote>
</aside>
<p>For each of the volume display nodes for the volumes you set it to only appear in the corresponding view by setting the <code>ViewNodeIDs</code> instance variable.</p>
<p>It works like this example:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Change_markup_fiducial_display_properties" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Change_markup_fiducial_display_properties</a></p>

---

## Post #19 by @Chintha_Siva_Prasad (2020-08-18 05:04 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/73a421263b20a611a7b065f47b0b86b0d649417e.png" data-download-href="/uploads/short-url/gv0yp4UBYKd94d79T0SIYIv5PTo.png?dl=1" title="whatever" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/73a421263b20a611a7b065f47b0b86b0d649417e_2_690x367.png" alt="whatever" data-base62-sha1="gv0yp4UBYKd94d79T0SIYIv5PTo" width="690" height="367" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/73a421263b20a611a7b065f47b0b86b0d649417e_2_690x367.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/73a421263b20a611a7b065f47b0b86b0d649417e_2_1035x550.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/73a421263b20a611a7b065f47b0b86b0d649417e.png 2x" data-dominant-color="F4F5F3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">whatever</span><span class="informations">1180×629 95.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
i had configured the display nodes and view nodes, but the volume is not appearing in the view node</p>

---
