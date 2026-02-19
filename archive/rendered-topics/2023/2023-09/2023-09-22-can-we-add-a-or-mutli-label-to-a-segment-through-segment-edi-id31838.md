---
topic_id: 31838
title: "Can We Add A Or Mutli Label To A Segment Through Segment Edi"
date: 2023-09-22
url: https://discourse.slicer.org/t/31838
---

# Can we add a or mutli Label to a segment through segment editor?

**Topic ID**: 31838
**Date**: 2023-09-22
**URL**: https://discourse.slicer.org/t/can-we-add-a-or-mutli-label-to-a-segment-through-segment-editor/31838

---

## Post #1 by @Benjamin-JZ (2023-09-22 06:37 UTC)

<p>i plan to make a  function which was a variable to record  made label of segment  by uesr.the best state was that  relationship was one to one  between label and segment.can we do it? please tell me which material i need look if the answer was yes.<br>
Thanks</p>

---

## Post #2 by @lassoan (2023-09-22 18:35 UTC)

<p>I don’t understand exactly what you want to do, but loading a labelmap volume as segmentation is very easy to do. You can find examples for this and many other segmentation related tasks in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#segmentations">script repository</a>.</p>

---

## Post #3 by @Benjamin-JZ (2023-09-26 03:00 UTC)

<p>no,no,i am sorry for not speak clearly, I mean, I want to create a new text label, not a label map type in 3Dslicer, because in fact, a label map can have multiple segments, right? But for each segment, I want to add an attribute to them and finally export these attributes as Json. Thank  <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #4 by @lassoan (2023-09-27 16:57 UTC)

<p>You can set “tags” (list of tag/value pairs) for each segment in a segmentation. This is written to the .seg.nrrd file but of course you can also write it out into another file in any format.</p>

---

## Post #5 by @Benjamin-JZ (2023-10-10 06:15 UTC)

<p>Hi,Lasso.I have seen document of 3DSlicer,But I seem had didn’t see usage of tags of segment.<br>
I plan the next step was that Can put Radio value into currently selection Segment_1 in below picture  when I press the get Value Button.(What I do now just print ) Could you give me a code demo?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8d9cce7b670cc4c75559b0ae8241adf13d9837c5.png" data-download-href="/uploads/short-url/kcLhlMKfkLyhf9pOJxdcWOldNZj.png?dl=1" title="1696917314389" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8d9cce7b670cc4c75559b0ae8241adf13d9837c5.png" alt="1696917314389" data-base62-sha1="kcLhlMKfkLyhf9pOJxdcWOldNZj" width="433" height="500" data-dominant-color="F4F5F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1696917314389</span><span class="informations">576×664 23.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>and finally do we have some exist abled API for export function? : )  : -) <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #6 by @lassoan (2023-10-10 10:26 UTC)

<p>You can call <code>mySegmentationNode.GetSegme tation().GetSegment("aSegmentID").SetTag("someTag", "some value")</code>. These tagged values are saved into the segmentation nrrd file.</p>

---

## Post #7 by @Benjamin-JZ (2023-10-13 01:29 UTC)

<p>Lasso,Thank you help! MySegmentationNode GetSegmetation(). This is missing n. It should be Getsegmentation(). haha. Anyway, I successfully combined the method you provided to give each segment_ 1/_ 2/_ 3 has set the corresponding Tag. However, after saving it as nrrd through export to file, I did not see the Tag when reading through ITK or Pydicom.</p>
<p>So I changed my mindset to complete the task and obtain each segment_ 1/_ Bounds of 2 and corresponding mask information. But I call activeSegment When GetBounds(), the console displays TypeError: GetBounds() takes exactly 1 argument (0 given), but I have looked at the function description but am still not quite sure what parameters to give (purpose: I want to obtain the boundaries of the real world coordinate system, that is, the Max and Min of the coordinate information xyz that is consistent with the dicom metadata, and what parameters should I pass to GetBounds to obtain these 6 information). Can you please explain how to obtain mask data from x/y/zMax  Min after solving this problem?</p>

---

## Post #8 by @Benjamin-JZ (2023-10-13 09:28 UTC)

<p>—update—<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a6297cd2da6b94ed0b9c298a08e385c06e3f1776.png" alt="image" data-base62-sha1="nHW96uLiHxMXiwDdLkbzNGoNZNI" width="334" height="141"></p>
<p>I tried to obtain the properties inside through the GetRepresentation method of the vtkSegment class. That is, under Representations in the above figure. However, I call segment GetRepresentation ('extent ')</p>
<p>Segment GetRepresentation ('spating ') returns None. When I pass in the self parameter, the display error must be a string. This feels like I can see but cannot touch it.<br>
<img src="https://emoji.discourse-cdn.com/twitter/sob.png?v=12" title=":sob:" class="emoji only-emoji" alt=":sob:" loading="lazy" width="20" height="20"> <img src="https://emoji.discourse-cdn.com/twitter/sob.png?v=12" title=":sob:" class="emoji only-emoji" alt=":sob:" loading="lazy" width="20" height="20"> <img src="https://emoji.discourse-cdn.com/twitter/sob.png?v=12" title=":sob:" class="emoji only-emoji" alt=":sob:" loading="lazy" width="20" height="20"><br>
my version was 5.0.3.<br>
Please tell me how to get these. <img src="https://emoji.discourse-cdn.com/twitter/crab.png?v=12" title=":crab:" class="emoji" alt=":crab:" loading="lazy" width="20" height="20"> <img src="https://emoji.discourse-cdn.com/twitter/crab.png?v=12" title=":crab:" class="emoji" alt=":crab:" loading="lazy" width="20" height="20"></p>

---

## Post #9 by @lassoan (2023-10-13 18:34 UTC)

<aside class="quote no-group" data-username="Benjamin-JZ" data-post="7" data-topic="31838">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/benjamin-jz/48/65776_2.png" class="avatar"> Benjamin-JZ:</div>
<blockquote>
<p>However, after saving it as nrrd through export to file, I did not see the Tag when reading through ITK or Pydicom</p>
</blockquote>
</aside>
<p>pydicom is not related. ITK may discard metadata that it does not know about (have a look at the metadata dictionary, though, you may find it there). You can surely use pynrrd to read all metadata, including segment tags.</p>
<p>Make sure you use the “Save” function to store all segmentation metadata. “Export to files” feature removes all custom metadata.</p>
<aside class="quote no-group" data-username="Benjamin-JZ" data-post="8" data-topic="31838">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/benjamin-jz/48/65776_2.png" class="avatar"> Benjamin-JZ:</div>
<blockquote>
<p>Segment GetRepresentation ('spating ') returns None.</p>
</blockquote>
</aside>
<p>That’s the correct behavior, because there is no such representation. You can find working examples of getting representations in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#segmentations">script repository</a>.</p>

---

## Post #10 by @Benjamin-JZ (2023-10-17 03:28 UTC)

<p>Thank you, lasso. I tried the way you said. It was to read the Segmentation node saved through the save method through pynrrd, and it does contain the tags I added. But it seems that each tag cannot correspond to its own Extent area, because the attribute Extent area accumulates information about all Segments. Whether it’s a segment_ 1 or Segment_ 2. Their Extents are the same.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b48bf7dbc8d726ff61c93aa9746496f2a14e0105.png" alt="image" data-base62-sha1="pLbP9UTZJGGukXBrExevnFYuIqp" width="272" height="116"></p>
<p>Part2: I also obtained Bounds for each Segment. I found that it is also consistent with the previous Extent situation, so I tested it several times and found that it seems to be a Segment_1/_2/_3  under a Segmentation actually share a Representation (OrientImageData), right? I tried clicking on the button, segment. RemoveRepresentation (“Binary labelmap”), and then SetMasterRepresentationToBinaryLabelmap() to add a new Rep, but it didn’t take effect and I couldn’t even draw with a brush 0__0</p>
<p>Overall, I would like to record segmentation_1. Segmentation_2 independent Bounds information.Like the following picture<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a85e2d93de2cdacc0d4e62393130833f301f9f8f.png" alt="image" data-base62-sha1="o1rZpFRLs69m9DlTJyPxC0Cz2dp" width="316" height="266"></p>

---

## Post #11 by @lassoan (2023-10-17 03:39 UTC)

<aside class="quote no-group" data-username="Benjamin-JZ" data-post="10" data-topic="31838">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/benjamin-jz/48/65776_2.png" class="avatar"> Benjamin-JZ:</div>
<blockquote>
<p>the attribute Extent area accumulates information about all Segments. Whether it’s a segment_ 1 or Segment_ 2. Their Extents are the same.</p>
</blockquote>
</aside>
<p><code>Extent</code> refers to the start/end extent of the image. In a VTK image, start extent can be anything (0, positive, or negative), while in a NRRD image it is always (0,0,0). Extent is stored in the segment metadata so that we can save and load any vtkImageData object without losing the original extent.</p>
<p>If you need the effective extent of a segment (extent of the bounding of non-zero voxels of the segment) then you need to store it in the segment tags yourself.</p>

---
