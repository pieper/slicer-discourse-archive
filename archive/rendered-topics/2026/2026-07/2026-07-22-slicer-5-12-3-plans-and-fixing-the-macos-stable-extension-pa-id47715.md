---
topic_id: 47715
title: "Slicer 5.12.3 plans and fixing the macOS stable extension packages"
date: 2026-07-22
url: https://discourse.slicer.org/t/47715
last_bumped: 2026-07-24T02:43:50.724Z
---

# Slicer 5.12.3 plans and fixing the macOS stable extension packages

**Topic ID**: 47715
**Date**: 2026-07-22
**URL**: https://discourse.slicer.org/t/slicer-5-12-3-plans-and-fixing-the-macos-stable-extension-packages/47715

---

## Post #1 by @ebrahim (2026-07-22 16:59 UTC)

<p>Yesterday we merged <a href="https://github.com/Slicer/Slicer/pull/9302">Slicer#9302</a> which worked out the cause of the issue with macOS C++ extension packages on Slicer 5.12, and which hopefully resolved  the issue.</p>
<p>Today there’s good evidence from the nightly packages that the issue is resolved:</p>
<ul>
<li>Yesterday’s MarkupsToModel: <a href="https://slicer-packages.kitware.com/#item/6a5fa0982eb3d967f03121e1" class="inline-onebox">SPKC</a> (see the large file size, indicating duplicated libraries)</li>
<li>Today’s: <a href="https://slicer-packages.kitware.com/#item/6a60ddab2eb3d967f0320816" class="inline-onebox">SPKC</a> (much smaller!)</li>
</ul>
<p>Time to cut Slicer 5.12.3? <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> <a class="mention" href="/u/jamesobutler">@jamesobutler</a> ? Any other commits we should include besides <a href="https://github.com/Slicer/Slicer/commit/2c4c53aaa487c1bfde9237b12a92f6a8b60b61b9">2c4c53a</a>?</p>
<p>I am thinking this time I will keep the <code>pre_release</code> attribute as True until we test that the problem is really resolved on macOS, preventing anything from becoming available on the download page until we are ready.</p>

---

## Post #2 by @pieper (2026-07-22 17:36 UTC)

<p>Confirmed - MarkupsToModel and SlicerRT work for me on today’s mac build.  Yes for 5.12.3 <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=15" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>

---

## Post #3 by @ebrahim (2026-07-23 14:12 UTC)

<p>Here is a signed and notarized macOS 5.12.3 package:</p>
<p><a href="https://slicer-packages.kitware.com/api/v1/file/hashsum/SHA512/2076f23458936a028d3d1a91686369b5979d3373012f11db0e90c30fdb34874eec2b150da4d5225b2ac6b1bf5552795e1783e621a8ae3c39c01983593b07283a/download" class="onebox" target="_blank" rel="noopener">https://slicer-packages.kitware.com/api/v1/file/hashsum/SHA512/2076f23458936a028d3d1a91686369b5979d3373012f11db0e90c30fdb34874eec2b150da4d5225b2ac6b1bf5552795e1783e621a8ae3c39c01983593b07283a/download</a></p>
<p>It is still marked as pre-release so it is not going to be available on the download page yet.<br>
Once we confirm the issue is really solved, I will remove the pre-release tag.</p>
<p>Can someone try this out on macOS and confirm that C++ extensions work?</p>

---

## Post #4 by @jamesobutler (2026-07-23 14:23 UTC)

<p>I’ve installed 5.12.3 along with SegmentEditorExtraEffects which pulls in MarkupsToModel that was previously impacted. I can confirm that on restart the MarkupsToModel now loads successfully and I can use the “Surface cut” segment editor effect successfully which utilizes the MarkupsToModel logic.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b392b8abcc60710355f761be8d7ca548ac20252d.jpeg" data-download-href="/uploads/short-url/pCzOBQT4wYOIMSjYO5AwsVsFQsZ.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b392b8abcc60710355f761be8d7ca548ac20252d_2_690x349.jpeg" alt="image" data-base62-sha1="pCzOBQT4wYOIMSjYO5AwsVsFQsZ" width="690" height="349" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b392b8abcc60710355f761be8d7ca548ac20252d_2_690x349.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b392b8abcc60710355f761be8d7ca548ac20252d_2_1035x523.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b392b8abcc60710355f761be8d7ca548ac20252d_2_1380x698.jpeg 2x" data-dominant-color="A6A3A5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1877×952 282 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @ebrahim (2026-07-23 14:27 UTC)

<p>Yay! Taking the patch release to the finish line</p>

---

## Post #6 by @muratmaga (2026-07-23 15:06 UTC)

<p>Yes, working for me too. Thank you.</p>

---

## Post #7 by @GeneRisi (2026-07-24 02:37 UTC)

<p>I downloaded it and was surprised to see that it is still an Intel processor app. Is the native version not ready yet?</p>

---

## Post #8 by @muratmaga (2026-07-24 02:43 UTC)

<p>That is planned for Slicer 6.0.</p>
<p>This release is meant to provide a bridge while the developers do many substantial changes to the core in preparation for Slicer 6.0, and break things for a while (in the preview versions). Given there is there is still rosetta support for at least a year, I think this is fine.</p>

---
