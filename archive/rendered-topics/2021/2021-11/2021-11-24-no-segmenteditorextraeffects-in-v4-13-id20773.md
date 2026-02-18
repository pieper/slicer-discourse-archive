# No segmentEditorExtraEffects in v4.13

**Topic ID**: 20773
**Date**: 2021-11-24
**URL**: https://discourse.slicer.org/t/no-segmenteditorextraeffects-in-v4-13/20773

---

## Post #1 by @bserrano (2021-11-24 13:35 UTC)

<p>Problem report for Slicer 4.13.0-2021-11-24 win-amd64: [please describe expected and actual behavior]</p>
<p>I cannot find segmentEditorExtraEffects, SlicerIGT and SlicerVMTK in the newest version 4.13, revision 30427. The reason why I am using this version is because I could not find the Sandbox extension in version 4.11, revision 29738. How can I get all packages in one version?</p>
<p>Thanks <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=10" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #2 by @rbumm (2021-11-24 20:03 UTC)

<p>Open up “Install slicer extensions” from the “Welcome” screen, search for “SegmentEditorExtraEffects” and install - does that not work for you? I get this in today’s Slicer preview  build:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d7774135bd7c61cfe6632614f65d9ab8c630d7d9.png" data-download-href="/uploads/short-url/uK69Oc3ZLubnLRwXSqD22gcvJsl.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d7774135bd7c61cfe6632614f65d9ab8c630d7d9_2_690x473.png" alt="image" data-base62-sha1="uK69Oc3ZLubnLRwXSqD22gcvJsl" width="690" height="473" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d7774135bd7c61cfe6632614f65d9ab8c630d7d9_2_690x473.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d7774135bd7c61cfe6632614f65d9ab8c630d7d9.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d7774135bd7c61cfe6632614f65d9ab8c630d7d9.png 2x" data-dominant-color="EAEDE9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">867×595 103 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @bserrano (2021-11-25 07:41 UTC)

<p>Thanks for your reply. But the extension does not appear in v4.13. It’s “unavailable”</p>

---

## Post #4 by @rbumm (2021-11-25 08:49 UTC)

<p>I was actually testing against a downloaded 4.13.0-2021-11-24 r30427 / ed8a169. Here it worked.<br>
Did you build Slicer or download the installer?</p>

---

## Post #5 by @bserrano (2021-11-25 08:57 UTC)

<aside class="quote no-group" data-username="rbumm" data-post="2" data-topic="20773">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>SegmentEditorExtraEffects</p>
</blockquote>
</aside>
<p>I am using 4.13.0-2021-11-24 r30429 / 00d2939. I downloaded the installer from the website <a href="https://download.slicer.org/" rel="noopener nofollow ugc">https://download.slicer.org/</a>.</p>
<p>This is what I get:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a3f7aa44a0559e2a1457f25c33578f377477d0f.jpeg" data-download-href="/uploads/short-url/3KcpSUrNk1UFgGDRphFDoqq9mO3.jpeg?dl=1" title="imagen" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1a3f7aa44a0559e2a1457f25c33578f377477d0f_2_690x151.jpeg" alt="imagen" data-base62-sha1="3KcpSUrNk1UFgGDRphFDoqq9mO3" width="690" height="151" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1a3f7aa44a0559e2a1457f25c33578f377477d0f_2_690x151.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1a3f7aa44a0559e2a1457f25c33578f377477d0f_2_1035x226.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1a3f7aa44a0559e2a1457f25c33578f377477d0f_2_1380x302.jpeg 2x" data-dominant-color="C7C5D1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">imagen</span><span class="informations">1929×424 179 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/5724b1798bbc9181a2d489d8ece8d1e2978a9ecd.png" data-download-href="/uploads/short-url/cqU9BlKNmzfT23fWRtpiXnE1fpH.png?dl=1" title="imagen" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/5724b1798bbc9181a2d489d8ece8d1e2978a9ecd_2_690x104.png" alt="imagen" data-base62-sha1="cqU9BlKNmzfT23fWRtpiXnE1fpH" width="690" height="104" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/5724b1798bbc9181a2d489d8ece8d1e2978a9ecd_2_690x104.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/5724b1798bbc9181a2d489d8ece8d1e2978a9ecd_2_1035x156.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/5724b1798bbc9181a2d489d8ece8d1e2978a9ecd_2_1380x208.png 2x" data-dominant-color="E6E6E6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">imagen</span><span class="informations">1911×289 12.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I am not able to download sandbox in version 4.11.20210226 r29738 / 7a593c8 either.</p>

---

## Post #6 by @bserrano (2021-11-25 10:07 UTC)

<p>I can find it now! I guess I just needed to wait</p>

---

## Post #7 by @rbumm (2021-11-25 11:59 UTC)

<p>Pls explain the solution in a bit more detail, for other users. Thank you.<br>
Are you working behind a firewall?</p>

---

## Post #8 by @jamesobutler (2021-11-25 12:58 UTC)

<p>The issue is likely regarding the time when the Slicer preview build finishes and is available to download versus when each extension finishes and is available to download. This time difference is not an issue for people in the USA as the build time is not during regular work hours. For example it is 8am on the east coast and most extensions are built and available to download however there are some extensions just now finishing up but the entire process will be over soon. See the CDash column for start times of the preview build and each extension <a href="https://slicer.cdash.org/index.php?project=SlicerPreview" rel="noopener nofollow ugc">here</a>.</p>
<p>See the linked post below about the topic which also includes a link to a Slicer GitHub issue that tracks it as well.</p>
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


---
