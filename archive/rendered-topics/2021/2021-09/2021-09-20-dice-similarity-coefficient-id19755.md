---
topic_id: 19755
title: "Dice Similarity Coefficient"
date: 2021-09-20
url: https://discourse.slicer.org/t/19755
---

# Dice similarity coefficient

**Topic ID**: 19755
**Date**: 2021-09-20
**URL**: https://discourse.slicer.org/t/dice-similarity-coefficient/19755

---

## Post #1 by @akmal871026 (2021-09-20 06:10 UTC)

<p>Hi all,</p>
<p>Anyone know how to calculate the dice similarity coefficient using 3D slicer?</p>

---

## Post #2 by @lassoan (2021-09-21 16:42 UTC)

<p>You can use Segment Comparison module (in SlicerRT extension).</p>

---

## Post #3 by @Chicago_Girl (2023-08-04 14:45 UTC)

<p>Hi,<br>
is the module name “SlicerRT” or “Segment comparison module”? I can’t find either of them.</p>

---

## Post #4 by @akmal871026 (2023-08-04 15:52 UTC)

<p>Dear <a class="mention" href="/u/chicago_girl">@Chicago_Girl</a> as attached<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3bbc9195335baf30e384165972df3fb01d4abc6d.png" data-download-href="/uploads/short-url/8wsaZwFv5RKPWl06gGWsK0QWgC9.png?dl=1" title="Untitled" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3bbc9195335baf30e384165972df3fb01d4abc6d_2_234x500.png" alt="Untitled" data-base62-sha1="8wsaZwFv5RKPWl06gGWsK0QWgC9" width="234" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3bbc9195335baf30e384165972df3fb01d4abc6d_2_234x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3bbc9195335baf30e384165972df3fb01d4abc6d_2_351x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3bbc9195335baf30e384165972df3fb01d4abc6d.png 2x" data-dominant-color="F8F8F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Untitled</span><span class="informations">373×797 16.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @Gonzalo_Rojas_Costa (2023-10-28 20:53 UTC)

<p>What is the “reference segment” image and “compare segment” one?</p>
<p>Sincerely</p>
<p>Gonzalo Rojas Costa</p>

---

## Post #6 by @akmal871026 (2023-10-29 01:45 UTC)

<p>Dear <a class="mention" href="/u/gonzalo_rojas_costa">@Gonzalo_Rojas_Costa</a>,</p>
<p>The reference segment is your ground truth labeling, while the compare segment is your volume segmentation</p>
<p>but I think both must be in .nrrd format.</p>

---

## Post #7 by @Paria_sh_2000 (2023-10-30 07:36 UTC)

<p>Dear MOHD AKMAL MASUD<br>
I want to calculate the dice similarity coefficient using 3D slicer. However,<br>
I cannot find how to upload the test and reference segment. when I click on a reference segment and when I want to select a segmentation which has two options: rename new segmentations or delete current segmentation. I do not know what to do to find my prepared reference segment.<br>
I would be grateful if you guide me with this.</p>

---

## Post #8 by @akmal871026 (2023-10-30 07:39 UTC)

<p>You have to upload in data module first.</p>

---

## Post #9 by @Paria_sh_2000 (2023-10-30 07:50 UTC)

<p>I already uploaded my data. I clicked on the Data then chose file to add then I selected two pictures one of them is mask and another is reference.</p>

---

## Post #10 by @Paria_sh_2000 (2023-10-30 08:10 UTC)

<aside class="quote no-group" data-username="akmal871026" data-post="8" data-topic="19755">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/akmal871026/48/11642_2.png" class="avatar"> akmal871026:</div>
<blockquote>
<p>upload in data module</p>
</blockquote>
</aside>
<p>Could you guide step by step please, I tried everything still can’t make comparison.</p>

---

## Post #11 by @akmal871026 (2023-10-30 08:11 UTC)

<p>I need to remote yourself by anydesk or teamviewer apps. If can, let me know</p>

---

## Post #13 by @Paria_sh_2000 (2023-10-30 09:12 UTC)

<p>Hello</p>
<p>Whenever you have time, inform me and I’d be grateful to access to my laptop and I’ll give you my anydesk address.</p>
<p>Kind regards<br>
Paria</p>

---

## Post #14 by @akmal871026 (2023-10-30 12:28 UTC)

<p>Ok, i will let you know</p>

---

## Post #15 by @cpinter (2023-10-30 12:39 UTC)

<p>The segmentation needs to be loaded as a “segmentation” node in Slicer, not volume. What is the file format you are using?</p>

---

## Post #16 by @Paria_sh_2000 (2023-11-07 14:22 UTC)

<p>Hello Everyone<br>
I want to calculate the dice similarity coefficient using 3D slicer. However,<br>
I cannot find how to upload the test and reference segment. when I click on a reference segment and when I want to select a segmentation which has two options: rename new segmentations or delete current segmentation. I do not know what to do to find my prepared reference segment.<br>
I would be grateful if someone could help me out.</p>

---

## Post #17 by @Paria_sh_2000 (2023-11-11 08:54 UTC)

<p>Hello Dear MOHD AKMAL MASUD</p>
<p>Sorry for reaching you at the weekends. I tried very hard and I’m quite frustrated, still I couldn’t find a problem that why I cannot calculate the dice coeffiency. Could you please connect to my computer as remote and take a look. I really appreciate it.</p>
<p>Best regards,<br>
Paria</p>

---

## Post #18 by @akmal871026 (2023-11-11 08:55 UTC)

<p>Yes sure. Tonight, at 9pm Malaysia time.</p>

---

## Post #19 by @Paria_sh_2000 (2023-11-11 08:56 UTC)

<p>Sure thank you very much.</p>

---

## Post #21 by @akmal871026 (2023-11-11 13:02 UTC)

<p>Okay, I will remote just a minute. Give me dinner first</p>

---

## Post #22 by @Paria_sh_2000 (2023-11-11 17:44 UTC)

<p>I’m still waiting for you…</p>

---

## Post #23 by @akmal871026 (2023-11-11 23:01 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9bf6c5cf34b746158331d3bb0b231b81ab350ee6.png" data-download-href="/uploads/short-url/mfIIod6qOqX0FJ03UXlKGRsoHyu.png?dl=1" title="image.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9bf6c5cf34b746158331d3bb0b231b81ab350ee6_2_562x304.png" data-base62-sha1="mfIIod6qOqX0FJ03UXlKGRsoHyu" alt="image.png" width="562" height="304" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9bf6c5cf34b746158331d3bb0b231b81ab350ee6_2_562x304.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9bf6c5cf34b746158331d3bb0b231b81ab350ee6_2_843x456.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9bf6c5cf34b746158331d3bb0b231b81ab350ee6_2_1124x608.png 2x" data-dominant-color="938C8C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.png</span><span class="informations">1920×1040 29.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #24 by @akmal871026 (2023-11-11 23:39 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f3d08853babf147c453d1e1edad12df185e8a71d.png" data-download-href="/uploads/short-url/yMSNRl8GeXn7mlm7B8MLcqjKgAB.png?dl=1" title="Untitled.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f3d08853babf147c453d1e1edad12df185e8a71d_2_690x370.png" data-base62-sha1="yMSNRl8GeXn7mlm7B8MLcqjKgAB" alt="Untitled.png" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f3d08853babf147c453d1e1edad12df185e8a71d_2_690x370.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f3d08853babf147c453d1e1edad12df185e8a71d_2_1035x555.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f3d08853babf147c453d1e1edad12df185e8a71d_2_1380x740.png 2x" data-dominant-color="9D9B9E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Untitled.png</span><span class="informations">1920×1032 107 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9bf6c5cf34b746158331d3bb0b231b81ab350ee6.png" data-download-href="/uploads/short-url/mfIIod6qOqX0FJ03UXlKGRsoHyu.png?dl=1" title="image.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9bf6c5cf34b746158331d3bb0b231b81ab350ee6_2_690x373.png" alt="image.png" data-base62-sha1="mfIIod6qOqX0FJ03UXlKGRsoHyu" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9bf6c5cf34b746158331d3bb0b231b81ab350ee6_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9bf6c5cf34b746158331d3bb0b231b81ab350ee6_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9bf6c5cf34b746158331d3bb0b231b81ab350ee6_2_1380x746.png 2x" data-dominant-color="938C8C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.png</span><span class="informations">1920×1040 29.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #25 by @Paria_sh_2000 (2023-11-13 08:30 UTC)

<p>Sorry , I waited for you so long but you didn’t reply. Then I slept. I tried to do it again based on your picture but it seems that I don’t have the option as compare!!<br>
Please help me I’m really desperate <img src="https://emoji.discourse-cdn.com/twitter/sob.png?v=12" title=":sob:" class="emoji" alt=":sob:" loading="lazy" width="20" height="20"></p>

---

## Post #26 by @akmal871026 (2023-11-13 08:49 UTC)

<p>Ok, tonight. 9 pm malaysian.</p>
<p>Last night I fever.</p>

---

## Post #27 by @Paria_sh_2000 (2023-11-13 08:56 UTC)

<p>Thank you very much. Hope you get better​:seedling:<img src="https://emoji.discourse-cdn.com/twitter/cherry_blossom.png?v=12" title=":cherry_blossom:" class="emoji" alt=":cherry_blossom:" loading="lazy" width="20" height="20"></p>

---

## Post #28 by @Paria_sh_2000 (2023-11-13 09:52 UTC)

<p>Can we remote tomorrow?</p>

---

## Post #30 by @akmal871026 (2023-11-18 09:50 UTC)

<p>Can. Tonight 9.00 pm malaysia</p>

---

## Post #31 by @akmal871026 (2023-11-18 12:26 UTC)

<p>Provide your anydesk ID and let your computer open</p>

---

## Post #33 by @muratmaga (2023-11-19 05:22 UTC)

<p><a class="mention" href="/u/paria_sh_2000">@Paria_sh_2000</a> <a class="mention" href="/u/akmal871026">@akmal871026</a> in case you are not aware, you can do direct messaging on the discourse.</p>

---

## Post #34 by @danial_s (2023-11-24 19:20 UTC)

<p>Dear Akmal<br>
Hope you are doing well.<br>
Can I use your instruction for having two different image sets? one is for KVCT and other for CBCT? Both are for one patient and same time!<br>
Thank you in advance</p>

---

## Post #35 by @akmal871026 (2023-11-24 19:23 UTC)

<p>I dont know what you mean.</p>

---

## Post #36 by @danial_s (2023-11-24 19:25 UTC)

<p>I have two image sets of one patient and i want to know what the dice coefficient of each organ is. one image is planning CT and the other is daily CBCT</p>

---
