# Issue with VTK leaks

**Topic ID**: 954
**Date**: 2017-08-27
**URL**: https://discourse.slicer.org/t/issue-with-vtk-leaks/954

---

## Post #1 by @stevenagl12 (2017-08-27 23:28 UTC)

<p>So I am running the Slicer nightly build from August 22nd and having an issue where I cannot load mrml or mrb files. The loading bar stops at 99% and remains there for days afterwards. I’m using a desktop computer with 32GBs of RAM, an Intel i7-7700 CPU Processor and Windows 10. In addition, upon closing the Slicer application it gives warnings of a VTK leak:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d0b73a2c7f3c66a3d3498346e8554c287e87c7cf.png" alt="image" data-base62-sha1="tMnSkUvKyhR2FFEJXiL8aegaGYL" width="445" height="298"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8ebdda6297cd25e2f6093a12f49f28ec41eb9607.png" alt="image" data-base62-sha1="kmKyFgPcUnmRDdBKd4rT197mQ3t" width="454" height="283"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f513bb88804bf65d818793c5695a75593bf71369.png" alt="image" data-base62-sha1="yY3fW7Q28jyE5vsG35v7bZOpusN" width="475" height="313"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2b6bcf55c0290cc1dd37a7ccc194715db9968600.png" alt="image" data-base62-sha1="6c7vNvxNk04J73PmDfBZyHB76BW" width="482" height="193"></p>
<p>I’m aware of what a memory leak is, but as I’m still very new to computing, I have no idea of what to do about it?</p>

---

## Post #2 by @lassoan (2017-08-28 00:15 UTC)

<p>Could you test if the problem is reproducible with the latest nightly build?</p>
<p>Does the problem happen with one specific scene file or you cannot load scenes that you create from scratch?</p>
<p>If it does not work, can you share with us the scene that cannot be loaded? (you can upload to dropbox or onedrive and post the link)</p>

---

## Post #3 by @stevenagl12 (2017-08-28 14:33 UTC)

<p>So I have yet to see if the VTK leak occurs on the latest nightly build but I’ve tried loading both mrb and mrml files into the program and neither one is working. It still only goes to 99% and then becomes unresponsive. Attached is the link to a google drive file <a href="https://drive.google.com/file/d/0B7remrTspnWabE0xcEtfWjNYd1k/view?usp=sharing" rel="nofollow noopener">https://drive.google.com/file/d/0B7remrTspnWabE0xcEtfWjNYd1k/view?usp=sharing</a></p>

---

## Post #4 by @stevenagl12 (2017-08-28 15:02 UTC)

<p>The VTK leaks issue is still present.</p>

---

## Post #5 by @cpinter (2017-08-28 15:22 UTC)

<p>Based on a quick glance, this seems to be a terminology related endless loop when loading the segmentation. I’ll take a closer look.</p>

---

## Post #6 by @cpinter (2017-08-28 15:36 UTC)

<p>The problem is that we have a segment tag with this value<br>
"Œ<code>¦-þI@zˆIIÃöXÀ)Õ“™£“€Àœ!.ß\x12G@ïé</code>w\x1f"[À)Õ“™£“€ÀŒE·ê\b·B@\x16\x3©\xfq±[À)Õ“™£“€ÀÐóÌ»?å@@ì½â¬P’ZÀ)Õ“™£“€À|"<br>
and the parser hangs. <a class="mention" href="/u/stevenagl12">@stevenagl12</a> do you know what this tag might be?</p>

---

## Post #7 by @cpinter (2017-08-28 15:58 UTC)

<p>I committed a fix that allows loading your scene. It will be available in tomorrow’s nightly. The tags in the segments that caused the parser to fail look like this one:</p>
<pre><code>  Tags:
      TerminologyEntry: Segmentation category and type - 3D Slicer General Anatomy list~SRT^T-D0050^Tissue~SRT^T-D016E^Bone~^^~Anatomic codes - DICOM master list~^^~^^
      fN: 9
      fP: éHZF@_Ô±Þ XÀ³]áÆBvÀ,ÔàìéF@ÉÐßÍZÀ³]áÆBvÀø8`oB@ZÇýE]ZÀ³]áÆBvÀø8`oB@SYÂKêWÀ³]áÆBvÀØwGe¬ÕC@ .°ÁXÀ)Õ£À
</code></pre>
<p>Unfortunately storing binary data in segment tags is not supported. Do you know where these tags came from?</p>

---

## Post #8 by @lassoan (2017-08-28 16:03 UTC)

<p>If you need to store binary data in a segment tag then you have to encode it as ASCII string (e.g., base64 method) before you set in the segment and decode after you get from the segment.</p>

---

## Post #9 by @stevenagl12 (2017-08-28 16:08 UTC)

<p>I have no idea where they came from. I saved the files as an mrb when I was running a segmentation. Then when I had an issue with those files loading, I extracted the mrml files from those and tried to load them, but the same issue happened.</p>

---

## Post #10 by @stevenagl12 (2017-08-28 16:09 UTC)

<p>My PI tried to look at the files on his linux system and he got:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/5213659419f705b8e46a049d94c1ab0a5c3c9ffc.png" data-download-href="/uploads/short-url/bI4I1hhEmR3rt0hPSc5tlp9H6Bm.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/5213659419f705b8e46a049d94c1ab0a5c3c9ffc_2_690x388.png" alt="image" data-base62-sha1="bI4I1hhEmR3rt0hPSc5tlp9H6Bm" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/5213659419f705b8e46a049d94c1ab0a5c3c9ffc_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/5213659419f705b8e46a049d94c1ab0a5c3c9ffc_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/5213659419f705b8e46a049d94c1ab0a5c3c9ffc_2_1380x776.png 2x" data-dominant-color="DFE0E8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 217 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #11 by @cpinter (2017-08-28 16:12 UTC)

<p>The valid-looking fN and fP tag names suggest that someone/something added them deliberately. It would be interesting to know where they came from.</p>
<p>Loading is now fixed, but if there are any subsequent tags in the segmentation after the one containing the binary value, those will probably be lost (this is not the case in your scene).</p>

---

## Post #12 by @cpinter (2017-08-28 16:12 UTC)

<aside class="quote no-group" data-username="stevenagl12" data-post="10" data-topic="954">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/stevenagl12/48/3391_2.png" class="avatar"> stevenagl12:</div>
<blockquote>
<p>My PI tried to look at the files on his linux system and he got</p>
</blockquote>
</aside>
<p>Yes, this is the issue I fixed. Please consider this solved.</p>

---

## Post #13 by @stevenagl12 (2017-08-28 16:14 UTC)

<p>Ok, is there an easy way for me to access the segmentations I have already saved, or do you mean you corrected the issue for the future with the nightly build?</p>

---

## Post #14 by @cpinter (2017-08-28 16:15 UTC)

<p>This is what I mean:</p>
<aside class="quote no-group" data-username="cpinter" data-post="7" data-topic="954">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>I committed a fix that allows loading your scene. It will be available in tomorrow’s nightly</p>
</blockquote>
</aside>

---

## Post #15 by @cpinter (2017-08-28 16:16 UTC)

<p>Do you use any extensions that work with segmentations and might have added these fN and fP tags?</p>

---

## Post #16 by @stevenagl12 (2017-08-28 16:20 UTC)

<p>I use a lot of extensions such as the segment editor extra effects, slicer pathology, Airway Segmenter, OpenCAD, Slicer Open CV, Markups to Models, and several others as I don’t have a programming background yet to do a lot of the stuff on my own. So mostly I rely on modules and extensions that others have made.</p>

---

## Post #17 by @cpinter (2017-08-28 16:21 UTC)

<p>Great! Can you please provide a full list of installed extensions? I’d like to track down this fP tag. Thanks</p>

---

## Post #18 by @stevenagl12 (2017-08-28 16:25 UTC)

<p>Currently I have: Markupstomodel, openCAD, segmenteditorextraeffects, slicer-airwaysegmentation, sliceropencv, and slicerpathology.</p>

---

## Post #19 by @cpinter (2017-08-28 16:54 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> These tags come from the SurfaceCut effect. Probably the value that is set is corrupted and this could be prevented by some check.</p>

---

## Post #20 by @lassoan (2017-08-28 17:07 UTC)

<p>Thanks for the investigation I’ll take care of the Surface Cut effect fix.</p>

---

## Post #21 by @lassoan (2017-08-28 20:03 UTC)

<p>I’ve fixed the error in Surface Cut effect. Point positions are now saved in text format, not as binary data.</p>

---
