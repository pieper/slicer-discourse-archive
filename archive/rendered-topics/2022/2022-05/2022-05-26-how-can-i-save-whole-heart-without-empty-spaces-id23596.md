# How can I save whole heart without empty spaces?

**Topic ID**: 23596
**Date**: 2022-05-26
**URL**: https://discourse.slicer.org/t/how-can-i-save-whole-heart-without-empty-spaces/23596

---

## Post #1 by @Js165 (2022-05-26 15:21 UTC)

<p>I am facing this problem while saving/exporting the segmentation into a binary label map. The problem is with HEART only. The heart contains multiple substructures. When I am saving the whole Heart and multiple substructures, the whole heart is showing some empty spaces. The empty spaces mainly contain the substructures.<br>
<strong>I am getting below image of whole heart:</strong><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a448c9544ca26b38bedb9a425ae045e17cdbf144.png" alt="Screen Shot 2022-05-25 at 2.34.23 PM" data-base62-sha1="nrkfsE3b0hGegOk6WsOT1ylwrBi" width="385" height="334"></p>
<p><strong>When I select all the substructures of heart then I am getting the below result:</strong><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0ff90b8f768c6b247c07cadbc3b54a0a84d8e710.png" alt="Screen Shot 2022-05-25 at 2.35.54 PM" data-base62-sha1="2hiJO7OKxcsyjikYjI5D076ECju" width="356" height="318"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/8566a3588a97aa487684c2cbf3048c03b2610bef.png" alt="Screen Shot 2022-05-25 at 2.36.01 PM" data-base62-sha1="j27p5mi11sXqrvEUMJnzcFKph95" width="435" height="315"></p>
<p>I want whole heart should look like the below image without detailed information of substructures. Ignore the texts in it.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c754fa693ee7a0289b832e0df81c190b167c6d66.png" alt="Screen Shot 2022-05-25 at 2.37.42 PM" data-base62-sha1="srn53j37QfAVR927qmDo3CynZ0a" width="414" height="428"></p>
<p>Thanks in advance.</p>

---

## Post #2 by @lassoan (2022-05-27 03:25 UTC)

<p>To create a segment that is the union of all other segments, you can use Logical operators effect’s Fill option, with setting Editable region → Inside all segments.</p>

---

## Post #3 by @Js165 (2022-05-27 12:32 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Thanks for your suggestion. I tried “Hollow” option. It is giving me the result but other structures are also impacting. Most probably I am not selecting correct parameter. Could you please suggest correct parameter settings?</p>

---

## Post #4 by @lassoan (2022-05-27 12:59 UTC)

<p>“Hollow” effect changes a solid structure into a hollow structure. Based on what you described, this is not what you need.</p>
<p>Have you tried to use the “Logical operators” effect as I described above? If you want to keep other segments unchanged then set “Allow overlap” in Masking section.</p>

---

## Post #5 by @Js165 (2022-05-27 13:10 UTC)

<p>Yes, I tried and attached is the screenshot of the parameter selection. I am not getting expected result. Am I doing anything wrong here?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2ee51f71dcf474e4d2f2733dc4323772bb916ddc.jpeg" data-download-href="/uploads/short-url/6GQR8tdaowqRt1o5aM2ahEMbeMs.jpeg?dl=1" title="Screen Shot 2022-05-27 at 9.08.08 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2ee51f71dcf474e4d2f2733dc4323772bb916ddc_2_511x500.jpeg" alt="Screen Shot 2022-05-27 at 9.08.08 AM" data-base62-sha1="6GQR8tdaowqRt1o5aM2ahEMbeMs" width="511" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2ee51f71dcf474e4d2f2733dc4323772bb916ddc_2_511x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2ee51f71dcf474e4d2f2733dc4323772bb916ddc_2_766x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2ee51f71dcf474e4d2f2733dc4323772bb916ddc.jpeg 2x" data-dominant-color="E5E6E5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2022-05-27 at 9.08.08 AM</span><span class="informations">1010×988 158 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @lassoan (2022-05-27 13:14 UTC)

<p>Uncheck “Bypass masking” to make the filling operation respect masking settings.</p>

---

## Post #7 by @Js165 (2022-05-27 13:32 UTC)

<p>I have attached before and after effects based on your suggestion. Whole segment is filling instead of only Heart.<br>
<strong>Before</strong><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e6307330f201c76881f510c87785cc1c2debab12.jpeg" data-download-href="/uploads/short-url/wQlCy6AFt7yldixr2lWBUOgN65c.jpeg?dl=1" title="Screen Shot 2022-05-27 at 9.29.48 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e6307330f201c76881f510c87785cc1c2debab12_2_690x235.jpeg" alt="Screen Shot 2022-05-27 at 9.29.48 AM" data-base62-sha1="wQlCy6AFt7yldixr2lWBUOgN65c" width="690" height="235" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e6307330f201c76881f510c87785cc1c2debab12_2_690x235.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e6307330f201c76881f510c87785cc1c2debab12_2_1035x352.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e6307330f201c76881f510c87785cc1c2debab12_2_1380x470.jpeg 2x" data-dominant-color="7F8183"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2022-05-27 at 9.29.48 AM</span><span class="informations">1920×655 98 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<strong>After</strong><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e933e773c6a218e914ec05a1682898a19f2ae4d.jpeg" data-download-href="/uploads/short-url/24W9vJmnMwEJtOH0XddeD2CqPuJ.jpeg?dl=1" title="Screen Shot 2022-05-27 at 9.30.05 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0e933e773c6a218e914ec05a1682898a19f2ae4d_2_690x279.jpeg" alt="Screen Shot 2022-05-27 at 9.30.05 AM" data-base62-sha1="24W9vJmnMwEJtOH0XddeD2CqPuJ" width="690" height="279" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0e933e773c6a218e914ec05a1682898a19f2ae4d_2_690x279.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0e933e773c6a218e914ec05a1682898a19f2ae4d_2_1035x418.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0e933e773c6a218e914ec05a1682898a19f2ae4d_2_1380x558.jpeg 2x" data-dominant-color="788F7A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2022-05-27 at 9.30.05 AM</span><span class="informations">1920×778 82.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @lassoan (2022-05-27 14:48 UTC)

<p>It works well for me. Use the latest Slicer Stable Release (Slicer-5.0.x) and follow these steps:</p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/91108a3f8ac9a4fd91e64ca68e157aa8b5921e31.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/91108a3f8ac9a4fd91e64ca68e157aa8b5921e31.mp4">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/91108a3f8ac9a4fd91e64ca68e157aa8b5921e31.mp4</a>
    </source></video>
  </div><p></p>

---

## Post #9 by @Js165 (2022-05-27 17:32 UTC)

<p>Thanks for sharing the video. My Slicer package is stable version and up to date. I tried in Mac and Linux but there is no change in result. Here is the latest outcome.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/19bae1bc5184f4938bcc00eb76da728ec0123790.png" alt="a" data-base62-sha1="3FCkpamAFFSxQaCFb9TbJaVb6Mw" width="608" height="281"></p>

---

## Post #10 by @lassoan (2022-05-27 17:37 UTC)

<p>What is your exact Slicer version?</p>
<p>Could you try it on a sample data set, creating the segmentation from scratch, to see if there is something special about your segmentation? Or save your scene as a .mrb file, upload it somewhere, and post the link here, so that I can try to reproduce the behavior on my computer?</p>

---

## Post #11 by @Js165 (2022-05-27 17:39 UTC)

<p>I am using Slicer version 5.1.0 and 5.0.2. I tried both versions.</p>

---

## Post #12 by @Js165 (2022-05-27 17:44 UTC)

<p>This is the answer of your next question: Sure, I will share the details soon.</p>

---

## Post #13 by @Js165 (2022-05-29 14:20 UTC)

<p>I’ve uploaded the sample data and corresponding segmentation file. Please use this link <a href="https://easyupload.io/0klfow" rel="noopener nofollow ugc">https://easyupload.io/0klfow</a> to download those files. The problem is with only “Whole Heart”. I have attached few screenshots for your reference. <strong>The problem is arising when I am saving the segmentation into labelmap.</strong></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/139fe27cc139c149bd751ab8d1c0ef724ce1cd55.png" alt="1" data-base62-sha1="2NBCEcQyPGxgv5twE6Lapmje6sR" width="408" height="329"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/11c530f2e5b33371b21308385da3f600bba31b83.png" alt="2" data-base62-sha1="2xcB1FyBfFot7eCv3QFZaWNrPA7" width="381" height="413"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a6a498beb78e58339ee307d1aec73204dc22c0e1.png" alt="3" data-base62-sha1="nMbUdMNjshds57QmPnIqugX26aZ" width="341" height="321"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc4652d6c9f534ee0e9101007bf264a5b3d41fe1.png" alt="4" data-base62-sha1="t964r6GOMAzjHcRPUYLoAt03AVX" width="350" height="295"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/875bde4462f9d64b94cf1fe428dfe2c4ca8cb66b.png" alt="6" data-base62-sha1="jjrhGE441emXqTc8t7btgWgEdhp" width="407" height="372"></p>

---

## Post #14 by @lassoan (2022-05-29 20:00 UTC)

<p>Thank you, by loading the linked file I was able to reproduce the unexpected behavior. There was a bug in Logical operator effect and so the mask was only applied if you performed some editing operation (e.g., use the Paint effect) before.</p>
<p>I’ve submitted a fix, so tomorrow’s Slicer Preview Release will not have this issue. As a workaround, use Paint effect to draw a small scribble somewhere (you can undo it or erase it right after it) and then use the Logical operators effect.</p>
<p>Note: Do not save segmentations in Nifti files. They are intended for brain images only and have many issues and limitations. For example they cannot store overlapping segments.</p>

---

## Post #15 by @Js165 (2022-05-29 23:47 UTC)

<p>Thanks for the update! I will try tomorrow’s Slicer Preview Release and update here.</p>

---

## Post #16 by @Js165 (2022-05-30 16:25 UTC)

<p>Hi,<br>
Update on the issue: I tried with recent release (version 5.1.0 revision 30976 built 2022-05-30) but I didn’t find any changes in the result.</p>

---

## Post #17 by @lassoan (2022-05-30 18:46 UTC)

<p>Slicer 5.1.0-2022-05-29 r30976 version works well. See this video successfully testing it on your data:</p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d66cb5de1d84849ce7c2da4312d6239ea20ecb7.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d66cb5de1d84849ce7c2da4312d6239ea20ecb7.mp4">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d66cb5de1d84849ce7c2da4312d6239ea20ecb7.mp4</a>
    </source></video>
  </div><p></p>

---

## Post #18 by @Js165 (2022-05-31 15:55 UTC)

<p>Thanks so much! This version has partially solved my issue. I want the effect will only be applied to the “whole heart”, not to other organs. For example, I am unable to detach esophagus from whole heart.</p>
<p>Not the RED circle portion<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0dbd52ed1ee9a91fb676b66f81433810b43a0786.png" alt="2022_05_31_0jy_Kleki" data-base62-sha1="1XxPzjgAXN4dX45bl47NLmwWdaS" width="223" height="307"></p>

---

## Post #19 by @lassoan (2022-06-01 19:30 UTC)

<p>You can hide the segments that you are not interested in and choose <code>editable region</code> → <code>inside visible segments</code>.</p>

---

## Post #20 by @Js165 (2022-06-01 20:30 UTC)

<p>Thanks so much! I tried that option too and there is no improvements on the issue.<br>
Here, I attached the screenshot. I created <strong>segment 9</strong> for applying logical operation. You can see all other segments are not visible. segment 9 contains all the organs. I just want heart will display here.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d47812f6bae785d2c6a5d50e0631ad14b4a6a523.png" data-download-href="/uploads/short-url/ujAtPXA18naOmtU1Bd13YLr6mzN.png?dl=1" title="mm" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d47812f6bae785d2c6a5d50e0631ad14b4a6a523_2_690x368.png" alt="mm" data-base62-sha1="ujAtPXA18naOmtU1Bd13YLr6mzN" width="690" height="368" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d47812f6bae785d2c6a5d50e0631ad14b4a6a523_2_690x368.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d47812f6bae785d2c6a5d50e0631ad14b4a6a523_2_1035x552.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d47812f6bae785d2c6a5d50e0631ad14b4a6a523.png 2x" data-dominant-color="BBBDD4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">mm</span><span class="informations">1286×686 139 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>My goal is to <strong>FILL the empty regions inside the heart</strong>. For example, I am showing the empty regions of heart.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/31f0bc9d2b47ad2caecb3068463298e150ebe23e.png" data-download-href="/uploads/short-url/77NaFYqUNMrgKDhXLD4qyEBKj6u.png?dl=1" title="nn" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/31f0bc9d2b47ad2caecb3068463298e150ebe23e_2_690x376.png" alt="nn" data-base62-sha1="77NaFYqUNMrgKDhXLD4qyEBKj6u" width="690" height="376" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/31f0bc9d2b47ad2caecb3068463298e150ebe23e_2_690x376.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/31f0bc9d2b47ad2caecb3068463298e150ebe23e_2_1035x564.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/31f0bc9d2b47ad2caecb3068463298e150ebe23e.png 2x" data-dominant-color="B8B9D5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">nn</span><span class="informations">1287×703 136 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
