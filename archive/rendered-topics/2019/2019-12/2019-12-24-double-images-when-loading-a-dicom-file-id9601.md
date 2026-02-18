# Double Images when loading a DICOM file

**Topic ID**: 9601
**Date**: 2019-12-24
**URL**: https://discourse.slicer.org/t/double-images-when-loading-a-dicom-file/9601

---

## Post #1 by @Ng_Hui_Sin (2019-12-24 05:20 UTC)

<p>Hi,<br>
I am using operating system of Windows 10. 3D slicer 4.10.2 was downloaded.<br>
I opened a DICOM file and expected the good resolution of the image.<br>
But the interface show double image for three plane and the resolution was bad.<br>
After adjusting the contrast, the resolution of the image does not meet my expectation (like what in a DICOM viewer.)</p>
<p>May i know what is the problem? Thank you in advance.</p>
<p>After loading a DICOM,<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/212528cf46f26d412fe49fdc6b67df46c9b514f2.png" data-download-href="/uploads/short-url/4JdmX2V9iClAQEfY9iXW6VPGi9Y.png?dl=1" title="3D Slicer DICOM loading problem" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/1/212528cf46f26d412fe49fdc6b67df46c9b514f2_2_690x387.png" alt="3D Slicer DICOM loading problem" data-base62-sha1="4JdmX2V9iClAQEfY9iXW6VPGi9Y" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/1/212528cf46f26d412fe49fdc6b67df46c9b514f2_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/1/212528cf46f26d412fe49fdc6b67df46c9b514f2_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/212528cf46f26d412fe49fdc6b67df46c9b514f2.png 2x" data-dominant-color="7A7979"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3D Slicer DICOM loading problem</span><span class="informations">1366×768 67.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>After adjusting the contrast,<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/61aabcca6e3e32d619f28ef8e5ad8aeda921a50a.png" data-download-href="/uploads/short-url/dW07jrPHGw47DRv5G3L1JSjV46u.png?dl=1" title="3D Slicer DICOM loading problem 2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/61aabcca6e3e32d619f28ef8e5ad8aeda921a50a_2_690x387.png" alt="3D Slicer DICOM loading problem 2" data-base62-sha1="dW07jrPHGw47DRv5G3L1JSjV46u" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/61aabcca6e3e32d619f28ef8e5ad8aeda921a50a_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/61aabcca6e3e32d619f28ef8e5ad8aeda921a50a_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/61aabcca6e3e32d619f28ef8e5ad8aeda921a50a.png 2x" data-dominant-color="848383"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3D Slicer DICOM loading problem 2</span><span class="informations">1366×768 150 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Comparing with the DICOM viewer,<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b15122665bc379d60df7ff183571ce77d89a8d8.png" data-download-href="/uploads/short-url/cZKAPlqcPiFyLwubgZf4YL2ZmBO.png?dl=1" title="3D Slicer DICOM loading problem 2 (DICOM viewer)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b15122665bc379d60df7ff183571ce77d89a8d8_2_690x387.png" alt="3D Slicer DICOM loading problem 2 (DICOM viewer)" data-base62-sha1="cZKAPlqcPiFyLwubgZf4YL2ZmBO" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b15122665bc379d60df7ff183571ce77d89a8d8_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b15122665bc379d60df7ff183571ce77d89a8d8_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b15122665bc379d60df7ff183571ce77d89a8d8.png 2x" data-dominant-color="4C4D51"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3D Slicer DICOM loading problem 2 (DICOM viewer)</span><span class="informations">1366×768 207 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Hope you can lend me your hand on this matter. Thank you.</p>

---

## Post #2 by @lassoan (2019-12-24 05:52 UTC)

<p>Please try if latest Slicer Preview Release loads the images correctly. If not, then follow <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM#Something_is_displayed.2C_but_it_is_not_what_I_expected">these instructions</a>.</p>

---

## Post #3 by @issakomi (2019-12-25 08:19 UTC)

<p>This may be fixed in the current ITK master (5.1), at least it is for some images with very similar error. A sample image were interesting.</p>

---

## Post #4 by @Ng_Hui_Sin (2020-01-04 10:01 UTC)

<p>It able to load the DICOM which download from slicer.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/927c19e8270084c48812e11c3c6999e42d8ed213.png" data-download-href="/uploads/short-url/kTRAY5AkCQjMT6L9gbMeRZxBzx1.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/927c19e8270084c48812e11c3c6999e42d8ed213_2_690x387.png" alt="image" data-base62-sha1="kTRAY5AkCQjMT6L9gbMeRZxBzx1" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/927c19e8270084c48812e11c3c6999e42d8ed213_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/927c19e8270084c48812e11c3c6999e42d8ed213_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/927c19e8270084c48812e11c3c6999e42d8ed213.png 2x" data-dominant-color="88878D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1366×768 213 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Nothing changes when follow the ’ I would expect to see a different image’<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/72d69b7ebdc08415e42dc294805999e582a15a8a.png" data-download-href="/uploads/short-url/gnUe0flHE8XjU12y8w4mwRU8O8O.png?dl=1" title="3D Slicer Prob" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/72d69b7ebdc08415e42dc294805999e582a15a8a_2_690x387.png" alt="3D Slicer Prob" data-base62-sha1="gnUe0flHE8XjU12y8w4mwRU8O8O" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/72d69b7ebdc08415e42dc294805999e582a15a8a_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/72d69b7ebdc08415e42dc294805999e582a15a8a_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/72d69b7ebdc08415e42dc294805999e582a15a8a.png 2x" data-dominant-color="8E8D94"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3D Slicer Prob</span><span class="informations">1366×768 107 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>After patching using volume patcher,<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8e262cb8079b556c6724012b95d807630288d666.png" data-download-href="/uploads/short-url/khvAyKsfOMPwSVTe46IzUQEcYm2.png?dl=1" title="3D Slicer Prob 3 (After DICOM patcher)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8e262cb8079b556c6724012b95d807630288d666_2_690x387.png" alt="3D Slicer Prob 3 (After DICOM patcher)" data-base62-sha1="khvAyKsfOMPwSVTe46IzUQEcYm2" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8e262cb8079b556c6724012b95d807630288d666_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8e262cb8079b556c6724012b95d807630288d666_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8e262cb8079b556c6724012b95d807630288d666.png 2x" data-dominant-color="DDE3E9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3D Slicer Prob 3 (After DICOM patcher)</span><span class="informations">1366×768 105 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Try loading the data by selecting one of the files in the [Add Data Dialog], same thing appear.</p>
<p>Here i share the cleaned series.<br>
<a href="https://drive.google.com/open?id=1SmWrZlXoHsbQ5tFFLJ08IeBUNZg-PNK4" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/open?id=1SmWrZlXoHsbQ5tFFLJ08IeBUNZg-PNK4</a></p>
<p>Hope you can help me in this.<br>
Thank you so much.</p>

---

## Post #5 by @lassoan (2020-01-04 19:14 UTC)

<p>ITK toolkit (that Slicer uses to load DICOM images) cannot load these images correctly, most probably because the image is compressed and ITK chooses incorrect data type.</p>
<p>While we fix the issue, you can import this data set into Slicer by following these steps:</p>
<ul>
<li>install SlicerDcm2nii extension in Extension Manager and restart Slicer</li>
<li>switch to module: Diffusion / Import and Export / Diffusion-weighted DICOM import (DCM2niixGUI)</li>
<li>set “Input Directory” to the folder that contains your DICOM files and click Apply</li>
</ul>
<p><a class="mention" href="/u/thewtex">@thewtex</a> Does this error look familiar to you? Has it been fixed in recent ITK versions?</p>

---

## Post #6 by @thewtex (2020-01-05 00:40 UTC)

<p>It looks like improved handling of the pixel type is required.</p>
<p>There have been many improvements since Slicer’s current version of ITK:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/b6bf2d30c99f731644182f750a4abd8e3c8204ca/SuperBuild/External_ITK.cmake#L36" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/b6bf2d30c99f731644182f750a4abd8e3c8204ca/SuperBuild/External_ITK.cmake#L36" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/b6bf2d30c99f731644182f750a4abd8e3c8204ca/SuperBuild/External_ITK.cmake#L36</a></h4>
<pre class="onebox"><code class="lang-cmake"><ol class="start lines" start="26" style="counter-reset: li-counter 25 ;">
<li>if(NOT DEFINED ITK_DIR AND NOT Slicer_USE_SYSTEM_${proj})</li>
<li>
</li>
<li>  ExternalProject_SetIfNotDefined(</li>
<li>    Slicer_${proj}_GIT_REPOSITORY</li>
<li>    "${EP_GIT_PROTOCOL}://github.com/InsightSoftwareConsortium/ITK"</li>
<li>    QUIET</li>
<li>    )</li>
<li>
</li>
<li>  ExternalProject_SetIfNotDefined(</li>
<li>    Slicer_${proj}_GIT_TAG</li>
<li class="selected">    "ff48670261e3bd16ee1c6f5494834f65183a98dd" # pre-v5.1b01 (2019-08-26)</li>
<li>    QUIET</li>
<li>    )</li>
<li>
</li>
<li>  set(EXTERNAL_PROJECT_OPTIONAL_CMAKE_CACHE_ARGS)</li>
<li>
</li>
<li>  if(Slicer_USE_PYTHONQT OR Slicer_BUILD_ITKPython)</li>
<li>    # XXX Ensure python executable used for ITKModuleHeaderTest</li>
<li>    #     is the same as Slicer.</li>
<li>    #     This will keep the sanity check implemented in SlicerConfig.cmake</li>
<li>    #     quiet.</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>with credit to <a class="mention" href="/u/issakomi">@issakomi</a>, who has significant relevant experience. It is worth a bump to ITK 5.1rc01.</p>

---

## Post #7 by @lassoan (2020-01-05 04:43 UTC)

<p>Thank you <a class="mention" href="/u/thewtex">@thewtex</a> , I confirm that the image loads correctly when switching to ITK 5.1rc01.</p>

---

## Post #8 by @lassoan (2020-01-06 15:37 UTC)

<p>Fix is on the way. You can monitor the status of ITK version update that will fix this issue <a href="https://github.com/Slicer/Slicer/pull/1295">here</a>.</p>

---

## Post #9 by @Ng_Hui_Sin (2020-01-07 00:32 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="9601">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>SlicerDcm2nii</p>
</blockquote>
</aside>
<p>Hi Sir, thank you for you reply. This is the outcome after trying SlicerDcm2nii extension. Image appear single now but the contrast is till not in expection.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/cafba4532325e4e4125a73b160a7ea8db7438aff.jpeg" data-download-href="/uploads/short-url/sXFAxgYAH6EpNXD0IeEEMf7aSN9.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cafba4532325e4e4125a73b160a7ea8db7438aff_2_690x387.jpeg" alt="image" data-base62-sha1="sXFAxgYAH6EpNXD0IeEEMf7aSN9" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cafba4532325e4e4125a73b160a7ea8db7438aff_2_690x387.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cafba4532325e4e4125a73b160a7ea8db7438aff_2_1035x580.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/cafba4532325e4e4125a73b160a7ea8db7438aff.jpeg 2x" data-dominant-color="94939A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1366×768 209 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you so much for you help.</p>

---

## Post #10 by @lassoan (2020-01-07 01:20 UTC)

<p>The contrast of the image looks excellent. You can adjust display window width/level by left-click-and-drag in slice viewers.</p>

---

## Post #11 by @Ng_Hui_Sin (2020-01-08 14:33 UTC)

<p>Okay. Really thanks for you help.</p>

---
