# [Newbie] Struggling with DICOM, MultiVolume and Sequences

**Topic ID**: 22134
**Date**: 2022-02-23
**URL**: https://discourse.slicer.org/t/newbie-struggling-with-dicom-multivolume-and-sequences/22134

---

## Post #1 by @TiPunch (2022-02-23 16:29 UTC)

<p>Hi,</p>
<p>I would like first to thank you for this great and powerful open-source software! In a world where every postprocessing tool can cost a kidney, it is a relief to see people who care about improving and sharing research.</p>
<p>I’m an absolute newbie in Slicer, and although I’m used to many programming tools, I’m pretty lost in what I’m trying to do.</p>
<p>My goal: postprocessing DCE-MRI acquisitions</p>
<p>My materials:</p>
<ul>
<li>T1 mapping: 3 <em>separate</em> series with different flip angles</li>
<li>DCE: 1 series with different time frames</li>
<li>“late” DCE: 1 *separate" series corresponding to a late time frame of the DCE-MRI acquisition</li>
</ul>
<p>My first problem: when using the T1 Mapping extension, I need an MRMLMultiVolume.</p>
<p>Regarding T1 Mapping, how can I “make” a MultiVolume from my separate series?<br>
When I use the MultiVolume Importer, it only requires a folder. Even when I select a specific subfolder with the distinct three series, it does not produce a valid MRMLMultiVolume. The only thing that I succeeded in achieving was creating a sequence with three time points, but I can’t convert it to an MRMLMultiVolume.</p>
<p>When I try to post-process the DCE series, I have the same problem, as it does not produce a valid MultiVolume.</p>
<p>Some help?</p>
<p>Thanks! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @fedorov (2022-02-23 17:13 UTC)

<p>MultiVolumeImporter should only be used if your input is a set of non-DICOM volumes. If you have a DICOM series with DCE or T1 sequence, you should import it into Slicer DICOM database, and load from DICOM browser as a multivolume. Depending on how the data was collected, you may see a single series corresponding to DCE acquisition, or you may have one timepoint per series. It is best to toggle “Advanced” checkbox in the DICOM browser, try Examine, and see if a multivolume is parsed from your DICOM content.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8fb226689bced59dc4832a5a64b5b2d264e8873c.png" alt="image" data-base62-sha1="kvbXHCASV6kB6PMEcbiXsMqDhcE" width="567" height="159"></p>

---

## Post #3 by @TiPunch (2022-02-23 18:32 UTC)

<p>Thank you !</p>
<p>I didn’t know that MultiVolume Importer was for non-DICOM files. Maybe I should convert to NIfTII first ?</p>
<p>In the DICOM Importer, I already tried to play the Advanced Options. However, my acquisitions are not recognized as MultiVolumes… That’s why I’m trying to find a work around <img src="https://emoji.discourse-cdn.com/twitter/confused.png?v=12" title=":confused:" class="emoji" alt=":confused:" loading="lazy" width="20" height="20"></p>

---

## Post #4 by @fedorov (2022-02-23 18:35 UTC)

<aside class="quote no-group" data-username="TiPunch" data-post="3" data-topic="22134">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tipunch/48/14418_2.png" class="avatar"> TiPunch:</div>
<blockquote>
<p>However, my acquisitions are not recognized as MultiVolumes… That’s why I’m trying to find a work around</p>
</blockquote>
</aside>
<p>That’s indeed a problem. Unfortunately, with multivolumes, it is very hard to debug without having access to the data. Most likely, your data should be parsed using a heuristic that is not part of the multivolume plugin. It could also be that the dataset is incomplete (for example, if a single slice is missing in one of the timepoints, it will not be parsed). If you share a de-identified sample, I can try to investigate.</p>
<p>Alternatively, indeed you could try to convert every timepoint into a separate volume, but I admit I have not used that non-DICOM load functionality in a long time.</p>

---

## Post #5 by @TiPunch (2022-02-23 21:48 UTC)

<p>I unfortunately can’t send any files for policy reasons, even after de-identification… I appreciate the time you’re taking to try finding a solution <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>I better understand how files are managed. I suppose the best solution is to retag files to construct time points. For the T1 mapping, as it consists of 3 separate acquisitions, there is no common series with different time points for the same slice.</p>
<p>The only frustrating thing is that I succeeded to obtain the right sequences in SequenceBrowser. There is only a small link missing !</p>
<p>Thanks again <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #6 by @fedorov (2022-02-23 21:51 UTC)

<aside class="quote no-group" data-username="TiPunch" data-post="5" data-topic="22134">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tipunch/48/14418_2.png" class="avatar"> TiPunch:</div>
<blockquote>
<p>it consists of 3 separate acquisitions, there is no common series with different time points for the same slice.</p>
</blockquote>
</aside>
<p>Did you try selecting all 3 series using Shift+click, and then parsing them in DICOM Browser?</p>

---

## Post #7 by @lassoan (2022-02-25 15:08 UTC)

<aside class="quote no-group" data-username="TiPunch" data-post="5" data-topic="22134">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tipunch/48/14418_2.png" class="avatar"> TiPunch:</div>
<blockquote>
<p>The only frustrating thing is that I succeeded to obtain the right sequences in SequenceBrowser. There is only a small link missing !</p>
</blockquote>
</aside>
<p>If you enable the “Advanced” view then you should be able to see the loadable for both “MultiVolume” and “Volume Sequence”. Could you attach a screenshot of the Advanced section after you clicked Examine? (scratch out patient name/id from the image but keep the rest of the “DICOM Data” column content)</p>

---

## Post #8 by @TiPunch (2022-02-28 10:00 UTC)

<p>Sorry for the late answer. I don’t have access to the images during the weekend.</p>
<p>I found that one of the 3 series I tried to merge had a different size. This is why no “MultIVolume” was recognized. Even when I resize the “wrong” volume, it doesn’t suggest a MultiVolume node.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/165c487144dbc60180fb4eac5c64d3c1d77723ac.png" data-download-href="/uploads/short-url/3bOdCBdLsH2jdDCbyuSyLbDynLK.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/165c487144dbc60180fb4eac5c64d3c1d77723ac.png" alt="image" data-base62-sha1="3bOdCBdLsH2jdDCbyuSyLbDynLK" width="690" height="201" data-dominant-color="E1ECF4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1162×339 10.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However, if I chose the two “correct” volumes (with different flip angles). A MultiVolume is recognized.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e81c35f371708cb2b0b95ad148ffce74851903cf.png" alt="image" data-base62-sha1="x7ldi6MHGWqwO1KqYJKBPCd3y8v" width="635" height="132"></p>
<p>There might be some mess in the DICOM Tags after resizing the “wrong” volume… It won’t be easy to correct them, and even though, I might obtain an incorrect mapping.</p>
<p>Thank you for your help!</p>

---
