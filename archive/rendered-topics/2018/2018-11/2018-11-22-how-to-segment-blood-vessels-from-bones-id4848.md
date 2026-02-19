---
topic_id: 4848
title: "How To Segment Blood Vessels From Bones"
date: 2018-11-22
url: https://discourse.slicer.org/t/4848
---

# How to segment blood vessels from bones?

**Topic ID**: 4848
**Date**: 2018-11-22
**URL**: https://discourse.slicer.org/t/how-to-segment-blood-vessels-from-bones/4848

---

## Post #1 by @sglee2357 (2018-11-22 15:20 UTC)

<p>Hi, I’m quite new to this field so I kinda lost in here.</p>
<p><strong>I’m trying to do blood vessel segmentation and center-line extraction from 3D CT images</strong> (DICOM format).<br>
(chest, abdomen, leg CTs usually)</p>
<p>So far, below is what I could do <strong>almost everything by hand</strong>: I first used threshold to segment bones &amp; vessels from the others <strong>and then manually erased bones for every slice</strong> so that only vessels are segmented.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7ba7a96fbd1820e5abec0d7572d1e109d8a53950.png" data-download-href="/uploads/short-url/hDTWrUPL10Eih3Td6iYXKNBaOYw.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7ba7a96fbd1820e5abec0d7572d1e109d8a53950_2_563x500.png" alt="image" data-base62-sha1="hDTWrUPL10Eih3Td6iYXKNBaOYw" width="563" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7ba7a96fbd1820e5abec0d7572d1e109d8a53950_2_563x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7ba7a96fbd1820e5abec0d7572d1e109d8a53950_2_844x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7ba7a96fbd1820e5abec0d7572d1e109d8a53950_2_1126x1000.png 2x" data-dominant-color="6F6F90"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1297×1150 172 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I want to do this automatically as much as possible, and <strong>the first problem for me is how to get rid of bones away in a smarter way after thresholding.</strong> (Although there might be many problems to solve)</p>
<p><strong>Is there any good way to do it?</strong></p>
<ul>
<li>The CT image that I have is acquired using contrast agent and I know what it is from the image files.<br>
Can I use that information for segmenting between vessels and bones?</li>
<li>Or is there any good algorithm that is already implemented so that I can readily use for this purpose?</li>
</ul>
<hr>
<p>I have been desperately looking for examples with similar problems but in all the examples that I could found there were no bones in the problem and thus segmentation was done somewhat simply.<br>
(one of the examples I found: [<a href="https://youtu.be/DJ2032yo5Co" rel="noopener nofollow ugc">https://youtu.be/DJ2032yo5Co</a>])</p>
<p>I tried vesselness filtering in the VMTKExtension for the 3D Slicer, but what I get was like below.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/31ca5e07512544e450e77e9a667dcf9dc1b84696.png" data-download-href="/uploads/short-url/76sXTgF0Ca7HNSo9voRxu4L6Ink.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/31ca5e07512544e450e77e9a667dcf9dc1b84696_2_690x412.png" alt="image" data-base62-sha1="76sXTgF0Ca7HNSo9voRxu4L6Ink" width="690" height="412" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/31ca5e07512544e450e77e9a667dcf9dc1b84696_2_690x412.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/31ca5e07512544e450e77e9a667dcf9dc1b84696_2_1035x618.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/31ca5e07512544e450e77e9a667dcf9dc1b84696_2_1380x824.png 2x" data-dominant-color="61536A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1658×990 200 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>Could you give me some advice on this?</strong></p>
<ul>
<li>Is this behavior normal? (= Is vesselness filtering not good to separate between vessels and bones?)</li>
<li>Or, can I get clear result if I use it correctly?<br>
(Actually, I don’t know what it actually does and how to use it, as I couldn’t find documentation on this)</li>
</ul>
<hr>
<p>Thank you very much for any help and thoughts <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @cpinter (2018-11-22 15:54 UTC)

<p>Thanks for the detailed and well illustrated description of your question!</p>
<p>I’d keep trying with VMTK, it is for this very purpose. If you put the seed point inside the vessel, then it shouldn’t go out and grow a region within the bones as we can see in the second screenshot.<br>
Note that the output of the vesselness filtering step is a volume containing probabilities between 0 and 1 so to get a definitive segmentation you need to threshold it. Try setting the vesselvess volume as foreground image in the 2D viewers and change the window/level or threshold in the Volumes module for that volume (need to select the volume first). See if you can get a scalar range where it shows up nicely.</p>
<p>This is what I got with the CTA cardio sample dataset with 4.10:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1df9a334417c750304244b42fb462829476d6db.jpeg" data-download-href="/uploads/short-url/tWCR8Q03HqwmSjEOCwGQ36AR1y3.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d1df9a334417c750304244b42fb462829476d6db_2_470x500.jpeg" alt="image" data-base62-sha1="tWCR8Q03HqwmSjEOCwGQ36AR1y3" width="470" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d1df9a334417c750304244b42fb462829476d6db_2_470x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d1df9a334417c750304244b42fb462829476d6db_2_705x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1df9a334417c750304244b42fb462829476d6db.jpeg 2x" data-dominant-color="99929B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">759×806 255 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @chir.set (2018-11-22 16:30 UTC)

<p>You may also use Simple Region Growing with a <em>few</em> Fiducial points to create a Label Map. The latter can be converted to a Segmentation object and then you may create the 3D model in the Segment Editor. Alternatively, you may use Model Maker with the Label Map to create a model.</p>
<p>Here is a result with CTA-Cardio, two seeds and default Simple Region Growing parameters.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/6909b7ee3ebb0038117c70c2bea82b4cd27a23cc.jpeg" data-download-href="/uploads/short-url/eZcXhpxChMv07fuVPjdK2mmyVMU.jpeg?dl=1" title="Screenshot_20181122_172359" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/6909b7ee3ebb0038117c70c2bea82b4cd27a23cc_2_690x395.jpeg" alt="Screenshot_20181122_172359" data-base62-sha1="eZcXhpxChMv07fuVPjdK2mmyVMU" width="690" height="395" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/6909b7ee3ebb0038117c70c2bea82b4cd27a23cc_2_690x395.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/6909b7ee3ebb0038117c70c2bea82b4cd27a23cc_2_1035x592.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/6909b7ee3ebb0038117c70c2bea82b4cd27a23cc_2_1380x790.jpeg 2x" data-dominant-color="9290A2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_20181122_172359</span><span class="informations">2512×1440 459 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I tried VMTK of old, it worked very well with normal blood vessels, but not with severely diseased ones.</p>

---

## Post #4 by @lassoan (2018-11-22 16:43 UTC)

<p>You can also use <em>Fast marching</em> (in SegmentEditorExtraEffects) or <em>Grow from seeds</em> effects.</p>
<p>If the only problem is separation from bones and bones are not connected to vasculature, then you can also use <em>Islands</em> effect. For example select “Keep selected island” method and the click on the vessel in one of the slice views - it will remove all disconnected segments, such as bones.</p>

---

## Post #5 by @chir.set (2018-11-22 20:11 UTC)

<p>Here is the result with Fast Marching :</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/170d40790c676069506e6f6d644905b7981fc48d.png" data-download-href="/uploads/short-url/3hVnaMgaTJbxyghZXDwf2LWG6kJ.png?dl=1" title="Screenshot_20181122_205921" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/170d40790c676069506e6f6d644905b7981fc48d_2_690x382.png" alt="Screenshot_20181122_205921" data-base62-sha1="3hVnaMgaTJbxyghZXDwf2LWG6kJ" width="690" height="382" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/170d40790c676069506e6f6d644905b7981fc48d_2_690x382.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/170d40790c676069506e6f6d644905b7981fc48d_2_1035x573.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/170d40790c676069506e6f6d644905b7981fc48d.png 2x" data-dominant-color="A29FA4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_20181122_205921</span><span class="informations">1332×739 258 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This method is quite direct, I admit I was pleasantly surprised. Just a few Level Tracing seeds and it computes right away. Now it’s much resource consuming as it always compute 100% Segment Volume on initialization. It consumed 5 over 8 GB swap space without prior cropping of CTA-Cardio ! Perhaps it’s internally mandatory. An initial result would appear much faster it could start at 5%.</p>
<p>Thanks for this useful guidance.</p>

---

## Post #6 by @lassoan (2018-11-22 23:52 UTC)

<p>I’ve checked the memory consumption of Fast marching and it was indeed unreasonably high. The root cause was a memory leak that I’ve now fixed. The fix is available in nightly Slicer version that you download tomorrow or later.</p>

---

## Post #7 by @sglee2357 (2018-11-23 01:23 UTC)

<p>Wow, thank you so much for your detailed answer. I am a bit relieved by the fact that I was doing wrong and my poor result was not the fault of VMTKExtension <img src="https://emoji.discourse-cdn.com/twitter/laughing.png?v=6" title=":laughing:" class="emoji" alt=":laughing:"> I’ll try with the CTA Cardio as you suggested. I never expected I could get such a kind response. Thank you so much <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=6" title=":grinning:" class="emoji" alt=":grinning:"></p>

---

## Post #8 by @sglee2357 (2018-11-23 01:30 UTC)

<p>Wow I am very surprised by the result. I will definitely try all of your suggestions. I feel like I kinda found some hope here. Thank you so much for your detailed feedback <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=6" title=":grinning:" class="emoji" alt=":grinning:"></p>

---

## Post #9 by @sglee2357 (2018-11-23 01:41 UTC)

<p>Thank you so much for your help! All of suggestions and bug fix are a great help to me. I am very amazed at such a fast and kind response on an open source platform. <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=6" title=":grinning:" class="emoji" alt=":grinning:"></p>

---

## Post #10 by @chir.set (2018-11-23 08:06 UTC)

<p>This indeed fixes the memory issue. Thanks.</p>

---
