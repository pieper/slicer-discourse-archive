# Specific segments in a segmentation node fail to be written to a DICOM RT file

**Topic ID**: 25061
**Date**: 2022-09-02
**URL**: https://discourse.slicer.org/t/specific-segments-in-a-segmentation-node-fail-to-be-written-to-a-dicom-rt-file/25061

---

## Post #1 by @godfreyd (2022-09-02 22:34 UTC)

<p>Specific segments in a segmentation node, according to numeric order (e.g., <span class="hashtag">#17</span>), consistently fail to be written to a DICOM RT file, regardless of what image volume is used or how the segments are created.</p>
<p>Operating system: Windows 10 Enterprise<br>
Slicer version: 5.0.3 or 4.11.20200930<br>
Expected behavior: During DICOM export, all segments from a segmentation node are expected to export to the selected DICOM-RT file.<br>
Actual behavior:  Most segments export, but the 17th segment in the segmentation node consistently fails to export to the DICOM-RT file.  I’ve confirmed this via many attempts, exporting either manually or via the Python interpreter, employing three different MR volumes (including the sample Slicer MR Head volume). I’ve also tested multiple DICOM readers (including re-importing it back into Slicer). This behavior occurs, regardless of how the segments are created – segments can be either drawn or converted from labelmaps – and I have confirmed this on two versions of Slicer (v. 5.0.3 and 4.11).  Also, from one attempt with a larger number of segments, it appears that segments <span class="hashtag">#33</span>, and <span class="hashtag">#38</span> also fail to export (I would surmise that is likely consistent as well).  I’ve confirmed that the information regarding the missing structure(s) is not present in the DICOM-RT file’s header.  Any ideas for a work-around?</p>

---

## Post #2 by @godfreyd (2022-09-03 23:08 UTC)

<p>I’ve confirmed the same bug on a different computer, now, as well.  It can be verified easily on any dataset, e.g., by loading the sample MR-Head data, creating a new segmentation, adding &gt;17 segments, drawing/painting within them, placing the volume and segmentation nodes within a new subject and new study, and exporting to DICOM.  The 17th segment is never written to the DICOMRT structure file, as confirmed by reimporting the study, or viewing the DICOM metadata.  Screen captures attached…<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf1a8a11863561b638a5638f7cd49109bba851af.jpeg" data-download-href="/uploads/short-url/rgA3xwoDS7ETGEsCkYYeGoloFkz.jpeg?dl=1" title="1_20SegmentsCreated" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf1a8a11863561b638a5638f7cd49109bba851af_2_690x365.jpeg" alt="1_20SegmentsCreated" data-base62-sha1="rgA3xwoDS7ETGEsCkYYeGoloFkz" width="690" height="365" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf1a8a11863561b638a5638f7cd49109bba851af_2_690x365.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf1a8a11863561b638a5638f7cd49109bba851af_2_1035x547.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf1a8a11863561b638a5638f7cd49109bba851af_2_1380x730.jpeg 2x" data-dominant-color="7F7F81"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1_20SegmentsCreated</span><span class="informations">2433×1289 297 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6bcf4b5a7f4a05732c43f19a16dc542db7aa1cf9.jpeg" data-download-href="/uploads/short-url/fnJdm7UNb1MWL6R2YGd6OEg3wkV.jpeg?dl=1" title="2_ExportToDICOM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6bcf4b5a7f4a05732c43f19a16dc542db7aa1cf9_2_689x382.jpeg" alt="2_ExportToDICOM" data-base62-sha1="fnJdm7UNb1MWL6R2YGd6OEg3wkV" width="689" height="382" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6bcf4b5a7f4a05732c43f19a16dc542db7aa1cf9_2_689x382.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6bcf4b5a7f4a05732c43f19a16dc542db7aa1cf9_2_1033x573.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6bcf4b5a7f4a05732c43f19a16dc542db7aa1cf9_2_1378x764.jpeg 2x" data-dominant-color="858484"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2_ExportToDICOM</span><span class="informations">2362×1309 291 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/3027ee8af2a30933cd1f9a483cae938d47d233a4.jpeg" alt="3_DICOM_Export_Menu" data-base62-sha1="6S0tgH3xVW0kRrxOMQZah7vqojG" width="624" height="482"></p>

---

## Post #3 by @godfreyd (2022-09-03 23:09 UTC)

<p>Screen captures (continued)…<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a403cf20c57556ba55df34892ba3771fedd7a2cb.jpeg" data-download-href="/uploads/short-url/noWsTGyrNRKUPuXXlW5E6IZZC9t.jpeg?dl=1" title="4_Reload_DICOM_Study" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/4/a403cf20c57556ba55df34892ba3771fedd7a2cb_2_690x373.jpeg" alt="4_Reload_DICOM_Study" data-base62-sha1="noWsTGyrNRKUPuXXlW5E6IZZC9t" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/4/a403cf20c57556ba55df34892ba3771fedd7a2cb_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a403cf20c57556ba55df34892ba3771fedd7a2cb.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a403cf20c57556ba55df34892ba3771fedd7a2cb.jpeg 2x" data-dominant-color="F2F6F9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">4_Reload_DICOM_Study</span><span class="informations">735×398 30.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f905c8ebea679c2ab7046b83f174c3a295503db.jpeg" alt="5_17thSegmentMissing" data-base62-sha1="2dGse0GHwbqdoJwKJLCOf9hZMKL" width="680" height="454"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/590b454877e3bc2853242311072b335dfb9c446a.jpeg" data-download-href="/uploads/short-url/cHIDOe2cOQTJ8YhTuoDHKGj6E4i.jpeg?dl=1" title="6_17thSegmentMissingDICOMmetadata" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/590b454877e3bc2853242311072b335dfb9c446a_2_690x455.jpeg" alt="6_17thSegmentMissingDICOMmetadata" data-base62-sha1="cHIDOe2cOQTJ8YhTuoDHKGj6E4i" width="690" height="455" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/590b454877e3bc2853242311072b335dfb9c446a_2_690x455.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/590b454877e3bc2853242311072b335dfb9c446a_2_1035x682.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/590b454877e3bc2853242311072b335dfb9c446a_2_1380x910.jpeg 2x" data-dominant-color="F7F2F2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">6_17thSegmentMissingDICOMmetadata</span><span class="informations">2145×1415 442 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @pieper (2022-09-04 12:49 UTC)

<p>Thanks for reporting and the in depth investigation <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20">   Let’s see if anyone from the SlicerRT team can offer suggestions.</p>

---

## Post #5 by @godfreyd (2022-09-08 17:06 UTC)

<p>Steve,</p>
<p>Regrettably, I have yet to get a reply from anyone on the SlicerRT team, or anyone affiliated with Slicer at all, other than your reply above.  This radio silence is discouraging, as the bug appears simple to duplicate (and therefore presumably debug), and more importantly, we are about to begin a clinical trial in early October on a software we’ve developed that currently has dependencies on 3D Slicer and its SlicerRT extension.  If we can’t rely on Slicer to actually consistently write each and every created segment to DICOM-RT files, this is a huge problem on our end, as it would potentially corrupt our trial results.  Thus, if no workaround is found in the next several weeks, I’m afraid we’ll need to re-design our own software to exclude Slicer – perhaps instead employing the recently-released open-source SlicerRT alternative, DicomRTTool instead (?) (as described in the recently published paper in Practical Radiation Oncology: <a href="https://www.sciencedirect.com/science/article/pii/S1879850021000485" class="inline-onebox" rel="noopener nofollow ugc">Simple Python Module for Conversions Between DICOM Images and Radiation Therapy Structures, Masks, and Prediction Arrays - ScienceDirect</a>).  I’ll be returning to the issue in late September, when I need to decide upon a path forward and will hopefully have time to code a workaround if none is found by then.  Thanks for your previous reply, though.  I’m holding out some hope that someone on the Slicer team may attempt to at least dig a little bit into the issue by then.  I suspect it ought to be an easy fix, once its root is discovered.</p>

---

## Post #6 by @pieper (2022-09-08 18:06 UTC)

<p>Hi Devon -</p>
<p>Thanks for the extra context.  As far as I know right now there’s no dedicated funding supporting SlicerRT work but maybe someone in the community can find the time.  I agree that on the surface it appears to be a highly localized issue that is hopefully easy to fix.  Perhaps someone who wants to learn Slicer programming can take on this issue for practice.  Thanks for pointing out DicomRTTool which looks useful in its own right.</p>
<p>-Steve</p>

---

## Post #7 by @godfreyd (2022-09-08 18:42 UTC)

<p>Thanks for the quick reply, Steve.  The info you’ve provided regarding the current lack of funding for additional SlicerRT work is very helpful to know / be made aware of – any lack of response certainly makes much more sense given that.  With that in mind, once I have a bit of time again in a few weeks, I’ll probably take a brief stab at looking for the root of the issue, myself, as well, and will report back if I discover anything.  If nothing jumps out quickly, though, I’ll probably need to move ahead with migrating our software to an alternative solution, unfortunately.  Either way, I appreciate your having taken the time to comment on this!</p>
<p>Best,</p>
<p>Devon</p>

---

## Post #8 by @Sunderlandkyl (2022-09-08 19:23 UTC)

<p>Sorry I missed this while I was on vacation last week. I’m taking a look at it now.</p>
<p>If nobody responds to a SlicerRT problem here, you can also post an issue on the SlicerRT GitHub page: <a href="https://github.com/SlicerRt/SlicerRT" class="inline-onebox" rel="noopener nofollow ugc">GitHub - SlicerRt/SlicerRT: Open-source toolkit for radiation therapy research, an extension of 3D Slicer. Features include DICOM-RT import/export, dose volume histogram, dose accumulation, external beam planning (TPS), structure comparison and morphology, isodose line/surface generation, etc.</a></p>

---

## Post #9 by @godfreyd (2022-09-08 19:34 UTC)

<p>Great, thank you Kyle!  Apologies for my previous impatience – I’m about to take a few weeks off, myself : ).  If I can be of any assistance as you investigate, please feel free to let me know.  The link to SlicerRT’s GitHub page is also very helpful!</p>
<p>-Devon</p>

---

## Post #10 by @Sunderlandkyl (2022-09-09 16:38 UTC)

<p>Found the <a href="https://github.com/SlicerRt/plastimatch/commit/889a36f0340e4723e79747562683c45523caa338" rel="noopener nofollow ugc">problem</a>. The fix should be available in tomorrow’s build.</p>

---

## Post #11 by @godfreyd (2022-09-09 19:48 UTC)

<p>Excellent news!!  Thanks a ton, Kyle!</p>

---

## Post #12 by @godfreyd (2022-09-21 19:17 UTC)

<p>Apologies for the delay.  Just wanted to report that upon initial testing of the new preview release (build 5.1.0-2022-09-16), the problem I reported above does indeed appear to be fixed.  Thanks a ton, Kyle, for your efforts to quickly resolve the issue!</p>

---
