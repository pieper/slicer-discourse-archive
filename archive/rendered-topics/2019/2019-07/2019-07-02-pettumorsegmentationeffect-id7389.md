# PETTumorSegmentationEffect

**Topic ID**: 7389
**Date**: 2019-07-02
**URL**: https://discourse.slicer.org/t/pettumorsegmentationeffect/7389

---

## Post #1 by @Mgi (2019-07-02 20:53 UTC)

<p>Operating system: Windows<br>
Slicer version: 4.10.2</p>
<p>In my slicer version there isn´t the “PETTumorSegmentationEffect” recommended by the wiki for segmentation in PET images.</p>
<p>Another one, my image of PET display with background black. How I could change that?</p>
<p>Thanks!</p>

---

## Post #2 by @fedorov (2019-07-02 20:55 UTC)

<aside class="quote no-group" data-username="Mgi" data-post="1" data-topic="7389">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/b19c9b/48.png" class="avatar"> Mgi:</div>
<blockquote>
<p>In my slicer version there isn´t the “PETTumorSegmentationEffect” recommended by the wiki for segmentation in PET images.</p>
</blockquote>
</aside>
<p>You need to install the PETTumorSegmentation extension: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/PETTumorSegmentation" class="inline-onebox">Documentation/Nightly/Extensions/PETTumorSegmentation - Slicer Wiki</a></p>
<aside class="quote no-group" data-username="Mgi" data-post="1" data-topic="7389">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/b19c9b/48.png" class="avatar"> Mgi:</div>
<blockquote>
<p>Another one, my image of PET display with background black. How I could change that?</p>
</blockquote>
</aside>
<p>You can use Volumes module to pick a different lookup table.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a0cf2fe69da34fa10d3df5a072076104f590b31c.png" data-download-href="/uploads/short-url/mWAi4XFdd1kdn7DzcfTmjt3ICaE.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a0cf2fe69da34fa10d3df5a072076104f590b31c_2_428x500.png" alt="image" data-base62-sha1="mWAi4XFdd1kdn7DzcfTmjt3ICaE" width="428" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a0cf2fe69da34fa10d3df5a072076104f590b31c_2_428x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a0cf2fe69da34fa10d3df5a072076104f590b31c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a0cf2fe69da34fa10d3df5a072076104f590b31c.png 2x" data-dominant-color="EEEEED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">506×590 64.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @Mgi (2019-07-03 15:11 UTC)

<p>Dear,<br>
It doesn´t appear in my extension manager, it´s possible that this extension don´t be compatible with x64bit?</p>
<p>Thanks!</p>

---

## Post #4 by @fedorov (2019-07-03 15:27 UTC)

<p>It looks like the module has build issues on all platforms with the nightly:</p>
<p><a href="http://slicer.cdash.org/index.php?project=SlicerPreview&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=PETTumor" class="onebox" target="_blank" rel="nofollow noopener">http://slicer.cdash.org/index.php?project=SlicerPreview&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=PETTumor</a></p>
<p>Based on the error, looks like it has not been migrated to ITK5: <a href="https://github.com/InsightSoftwareConsortium/ITK/blob/master/Documentation/ITK5MigrationGuide.md" rel="nofollow noopener">https://github.com/InsightSoftwareConsortium/ITK/blob/master/Documentation/ITK5MigrationGuide.md</a></p>
<p><a class="mention" href="/u/chribaue">@chribaue</a> not sure if you are aware of this?</p>
<p><a class="mention" href="/u/mgi">@Mgi</a> at this point, your best bet is probably to try latest stable build. I checked, and at least on Mac, the extension is available in the stable build.</p>

---

## Post #5 by @Mgi (2019-07-26 17:33 UTC)

<p>Dear Fedorov,</p>
<p>I want to normalize some PET images by the SUVmáx, that´s possible with the PETDICOM extension in 3Dslicer?</p>
<p>If the answer is negative you could recommend to me another extensions</p>
<p>Thank you!</p>

---

## Post #6 by @Mgi (2019-07-26 17:46 UTC)

<p>Dear,</p>
<p>Do you have some documents where explain how to normalize using the PET DICOM extension?</p>
<p>Thank you! Regards</p>

---

## Post #7 by @Mgi (2019-07-31 14:11 UTC)

<p>Hi <a class="mention" href="/u/fedorov">@fedorov</a>, I did install the 3Dslicer versions 4.8.1 and 4.6.2 on windows, because I though those are stable build. I load a PET serie, the “PETTumorSegmentationEffect” button appear but it didn’t serve when I used didn’t segment. What version should I use?</p>

---

## Post #8 by @fedorov (2019-07-31 15:05 UTC)

<p>You should use the latest stable, which is 4.10.2</p>

---

## Post #9 by @Mgi (2019-07-31 15:27 UTC)

<p>I have this version 4.10.2 on windows but it doesn´t appear the “PETTumorSgementationEffect” button in Editor Module neither PETIndic module.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c60ef20937a68d052e9f27131ba8a8d553a93c95.png" data-download-href="/uploads/short-url/sg6yHeAU3aDhzRTINWEWUIYavpr.png?dl=1" title="slicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c60ef20937a68d052e9f27131ba8a8d553a93c95_2_690x492.png" alt="slicer" data-base62-sha1="sg6yHeAU3aDhzRTINWEWUIYavpr" width="690" height="492" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c60ef20937a68d052e9f27131ba8a8d553a93c95_2_690x492.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c60ef20937a68d052e9f27131ba8a8d553a93c95_2_1035x738.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c60ef20937a68d052e9f27131ba8a8d553a93c95.png 2x" data-dominant-color="CECED0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer</span><span class="informations">1149×820 78.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @fedorov (2019-08-02 02:43 UTC)

<p><a class="mention" href="/u/mgi">@Mgi</a> you are right - the effect button is missing!</p>
<p><a class="mention" href="/u/chribaue">@chribaue</a> any suggestions? There are no errors in the log, or in the python console.</p>

---

## Post #11 by @jamesobutler (2019-08-02 10:44 UTC)

<p>For visibility, JC issued a PR back in April to update this extension with ITKv5 and python3 support and tagged you <a class="mention" href="/u/fedorov">@fedorov</a> (also received a response from <a class="mention" href="/u/chribaue">@chribaue</a> ). It would be a good time to review this PR. <a href="https://github.com/QIICR/PETTumorSegmentation/pull/18" rel="nofollow noopener">https://github.com/QIICR/PETTumorSegmentation/pull/18</a></p>
<p>Paired with this, JC suggested to create a branch for Slicer 4.10 code. <a href="https://github.com/QIICR/PETTumorSegmentation/issues/17" rel="nofollow noopener">https://github.com/QIICR/PETTumorSegmentation/issues/17</a></p>

---

## Post #12 by @fedorov (2019-08-02 13:38 UTC)

<p>Thanks a lot <a class="mention" href="/u/jamesobutler">@jamesobutler</a> - I completely missed those issues! Now that I did look into this, I also see this issue, <a href="https://github.com/QIICR/PETTumorSegmentation/issues/16" rel="nofollow noopener">https://github.com/QIICR/PETTumorSegmentation/issues/16</a>, which explains why the user was looking into 4.6.2. It looks like <a class="mention" href="/u/chribaue">@chribaue</a> did not find time to get to this. I am not sure if the team has resources to support this extension, let’s wait until Christian responds. It appears to me from those issues and the PR that they are not trivial.</p>

---

## Post #13 by @chribaue (2019-08-02 13:51 UTC)

<p>We do have an upcoming project where resources will become available to fix above mentioned issues.</p>
<p>The extension used to work on Slicer 4.10.0. Why it’s not working in Slicer 4.10.2, I do not know. Switching to ITKv5 and python3 will indeed not be trivial as can see from <a href="https://github.com/QIICR/PETTumorSegmentation/pull/18" rel="nofollow noopener">https://github.com/QIICR/PETTumorSegmentation/pull/18</a>. For now, I can only refer interested users to use the extension with Slicer 4.10.0.</p>

---

## Post #14 by @fedorov (2019-08-02 13:57 UTC)

<aside class="quote no-group" data-username="chribaue" data-post="13" data-topic="7389">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chribaue/48/1373_2.png" class="avatar"> chribaue:</div>
<blockquote>
<p>For now, I can only refer interested users to use the extension with Slicer 4.10.0.</p>
</blockquote>
</aside>
<p>For the reference, 4.10 packages are available here: <a href="http://slicer.kitware.com/midas3/folder/5380">http://slicer.kitware.com/midas3/folder/5380</a> (following “older releases” link on <a href="https://downloads.slicer.org">https://downloads.slicer.org</a>).</p>

---
