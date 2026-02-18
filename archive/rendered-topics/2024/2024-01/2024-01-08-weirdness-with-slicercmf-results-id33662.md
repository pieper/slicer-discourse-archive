# Weirdness with SlicerCMF results

**Topic ID**: 33662
**Date**: 2024-01-08
**URL**: https://discourse.slicer.org/t/weirdness-with-slicercmf-results/33662

---

## Post #1 by @Inka_Saraswati (2024-01-08 05:58 UTC)

<p>I’m using SlicerCMF extension (non growing) to do registration between a DICOM image and its mirror image. It’s for a unilateral cleft lip cases, so I want to overlap the cleft area with a mirror image of the normal side.</p>
<p>After registration, it produced 3 outputs (Registration matrix, Registered Scan, and Registered Seg). In Pic A Output are the ones I marked with red, Ori ones are from the original non-mirrored data, while Copy at the ends mean that they are mirrored. Because the registration process required me to segment an area used for reference, I expected the output to produce a segment data as well (which I also need). <strong>However, the outputs are in the form of volume data. Is that how it is supposed to be?</strong> <strong>If I need a segmentation of the registered image, do I need to resegment?</strong></p>
<p>Pic A:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/050804f8eebd6eee030b0afc2b9db8969f372ab4.jpeg" data-download-href="/uploads/short-url/IvzgNRdbwIacR47TnhohuBAECM.jpeg?dl=1" title="Pic A" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/050804f8eebd6eee030b0afc2b9db8969f372ab4_2_690x391.jpeg" alt="Pic A" data-base62-sha1="IvzgNRdbwIacR47TnhohuBAECM" width="690" height="391" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/050804f8eebd6eee030b0afc2b9db8969f372ab4_2_690x391.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/050804f8eebd6eee030b0afc2b9db8969f372ab4_2_1035x586.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/050804f8eebd6eee030b0afc2b9db8969f372ab4_2_1380x782.jpeg 2x" data-dominant-color="8E8D92"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Pic A</span><span class="informations">1920×1088 140 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>To make things extra annoying, there’s a bug that causes the segmentations to not appear in this data despite turning on the eyes (probably my laptop is not powerful enough? would appreciate advice on this as well). But if I import some of the data individually (see Pic B, I imported the output Registered Seg as volume, along with the original non-mirrored segmentation), I can confirm that the data are there and the registration itself looks decent. I tried importing the Seg output data as a segmentation and it just won’t load/error. <strong>In Pic B, I imported Seg as Volume and it appears as this red weirdness and I don’t know what that means.</strong></p>
<p>Pic B:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/36fb8ecef9f54f2f20b58d4f183a76afb87c7a67.png" data-download-href="/uploads/short-url/7QoK6pq7qL7O6EgFUk9rLKhn5z1.png?dl=1" title="Pic B" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/36fb8ecef9f54f2f20b58d4f183a76afb87c7a67_2_690x392.png" alt="Pic B" data-base62-sha1="7QoK6pq7qL7O6EgFUk9rLKhn5z1" width="690" height="392" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/36fb8ecef9f54f2f20b58d4f183a76afb87c7a67_2_690x392.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/36fb8ecef9f54f2f20b58d4f183a76afb87c7a67_2_1035x588.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/36fb8ecef9f54f2f20b58d4f183a76afb87c7a67_2_1380x784.png 2x" data-dominant-color="989393"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Pic B</span><span class="informations">2880×1638 1.34 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Can anyone help me with this? Any help is appreciated, thank you.</p>
<p>I’m using Slicer 5.6.1.</p>

---

## Post #2 by @muratmaga (2024-01-08 20:52 UTC)

<aside class="quote no-group" data-username="Inka_Saraswati" data-post="1" data-topic="33662">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/inka_saraswati/48/67631_2.png" class="avatar"> Inka_Saraswati:</div>
<blockquote>
<p>If I need a segmentation of the registered image, do I need to resegment?</p>
</blockquote>
</aside>
<p>If you already have a segmentation of the registered image, simply apply the transform generated by the registration to put it in the same space</p>
<aside class="quote no-group" data-username="Inka_Saraswati" data-post="1" data-topic="33662">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/inka_saraswati/48/67631_2.png" class="avatar"> Inka_Saraswati:</div>
<blockquote>
<p>To make things extra annoying, there’s a bug that causes the segmentations to</p>
</blockquote>
</aside>
<p>This is not a bug. You have loaded your Output Registered… volume as a labelmap. Remove it, and when you load, make sure it labelmap option is not checked.</p>

---

## Post #3 by @Inka_Saraswati (2024-01-08 23:16 UTC)

<p>Thanks for the reply.</p>
<p>If you notice in Pic A, I have already applied the registration matrix on the outputs and the registration definitely works (you can see that there is a slant in the images). Also, there is indeed a bug. Sometimes the segmentations appear, and sometimes they do not appear (when the eyes are checked)  in the same data, specifically when there are lots of components like this. For example, in Pic A, ori segmentation and ori cut are checked but the segmentations do not appear anywhere. My question is, I need a segmentation of the output, and I thought Output Registration Seg would be a segmentation but as you can see it is labelled as volume and appear as volume, not segmentation. Can I get a segmentation output without resegmenting the output volume?</p>
<p>Because of the bug, I uploaded some items individually in Pic B (please note that in Pic B, I have already hardened the registration matrix to the Output). Ori segmentation and ori cut appear as they should (as you can see the registration with the red is decent). I uploaded Output Registration Seg as volume (if I try to upload as segmentation, it wouldn’t load). I don’t understand why it appeared red and not typical black and white (considering it’s the same data as shown in Pic A) and not a segmentation (as I need, despite it being named Seg).</p>
<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="33662">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>You have loaded your Output Registered… volume as a labelmap. Remove it, and when you load, make sure it labelmap option is not checked.</p>
</blockquote>
</aside>
<p>I also don’t understand what you mean by removing labelmap, I can’t find it, can you help? This is what I chose when uploading:</p>
<p>Pic C:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d7681fb31726b9b6d6a50ae169e4e0c0ef57cdba.png" data-download-href="/uploads/short-url/uJzJU9PECcNTdg2MBKjeDJ5DRDY.png?dl=1" title="Pic D" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d7681fb31726b9b6d6a50ae169e4e0c0ef57cdba_2_690x120.png" alt="Pic D" data-base62-sha1="uJzJU9PECcNTdg2MBKjeDJ5DRDY" width="690" height="120" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d7681fb31726b9b6d6a50ae169e4e0c0ef57cdba_2_690x120.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d7681fb31726b9b6d6a50ae169e4e0c0ef57cdba_2_1035x180.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d7681fb31726b9b6d6a50ae169e4e0c0ef57cdba_2_1380x240.png 2x" data-dominant-color="EDEDED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Pic D</span><span class="informations">1472×256 19.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @muratmaga (2024-01-09 00:17 UTC)

<aside class="quote no-group" data-username="Inka_Saraswati" data-post="3" data-topic="33662">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/inka_saraswati/48/67631_2.png" class="avatar"> Inka_Saraswati:</div>
<blockquote>
<p>I also don’t understand what you mean by removing labelmap, I can’t find it, can you help? This is what I chose when uploading:</p>
</blockquote>
</aside>
<p>If you click on the Show Options, there will be field that says LabelMap. Make sure it is not selected. It think Slicer is confused because you have the “Seg” Keyword in it, and it is trying to load it as a labelmap/segmentation, as opposed to a regular volume.</p>
<aside class="quote no-group" data-username="Inka_Saraswati" data-post="3" data-topic="33662">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/inka_saraswati/48/67631_2.png" class="avatar"> Inka_Saraswati:</div>
<blockquote>
<p>sometimes they do not appear (when the eyes are checked)</p>
</blockquote>
</aside>
<p>If they visibility (eyes) are checked, but the segmentaiton is not appearing, it is quite likely that they are not in the spatial coordinate system with the volume you are trying to display them on. This is not a bug, but an indication of there is something of an issue with your workflow in applying registrations to subsequent data.</p>

---

## Post #5 by @luciacev (2024-01-09 01:22 UTC)

<p>Inka,<br>
Have you watched the <a href="https://www.youtube.com/@DCBIA/videos" rel="noopener nofollow ugc">https://www.youtube.com/@DCBIA/videos</a> video 3G tutorial on regional registration using the  SlicerCMF CMR Reg module? Hope the video tutorial will help you. If you still run into issues please email me at luciacev@umich.edu and we can schedule a Zoom to help you troubleshoot your issue.<br>
Lucia</p>

---

## Post #6 by @Inka_Saraswati (2024-01-09 06:25 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> I deselected the labelmap and it fixed the view to appear black and white, as expected from regular volume. Does this mean that SlicerCMF produces no segmentations? Which means that if I need a registered segmentation, I need to resegment the output volume?</p>
<p>However I am 99% sure (the remaining 1% is purely because I am new to Slicer although I do have much experience with medical images and I did try to familiarise myself as much as possible with Slicer) that there is a bug, I think my laptop is just not powerful enough to show all the components because there are so many. That is neither here or there though, at this stage I am not trying to fix “the bug”, but the behaviours I noticed are: 1) there is no rhyme or reason about when the segmentations decide to appear (with the eyes checked). Particularly, if the segmentation somehow decide to appear and I checked off the eye, then I re-check the eye the next second, the segmentation wouldn’t reappear. 2) As can be seen in Pic B, the ori segmentation and ori cut are in the exact same space as Output Registered Seg MAX, so they should be visible in Pic A too. And I can confirm that they DID appear in the same space in Pic A, I just didn’t take screenshots and I couldn’t make them reappear with any kind of certainty (except by uploading them individually, like I did in Pic B). Maybe this is not a bug, but I really, really do not think it’s a space issue. I’m writing this mainly because I like being thorough.</p>
<p>Thank you for the reply though, you did help!</p>
<p><a class="mention" href="/u/luciacev">@luciacev</a> I did follow the tutorial and I still have questions, I sent you an email! Thank you!</p>

---

## Post #7 by @muratmaga (2024-01-09 06:35 UTC)

<aside class="quote no-group" data-username="Inka_Saraswati" data-post="6" data-topic="33662">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/inka_saraswati/48/67631_2.png" class="avatar"> Inka_Saraswati:</div>
<blockquote>
<p>However I am 99% sure (the remaining 1% is purely because I am new to Slicer although I do have much experience with medical images and I did try to familiarise myself as much as possible with Slicer) that there is a bug, I think my laptop is just not powerful enough to show all the components because there are so many.</p>
</blockquote>
</aside>
<p>It might or may not be a bug. If you can reproduce the behavior with clear instructions using one of the Slicer sample dataset, someone may look into it. Otherwise, from your description it is still not clear whether that’s a bug or a workflow problem.</p>
<p>I am not familiar with CMF, so I dont know if it supposed to produce segmentation or not. <a class="mention" href="/u/luciacev">@luciacev</a> might help.</p>

---

## Post #8 by @luciacev (2024-01-10 02:37 UTC)

<p>I suggested times to Zoom by email. Please let me know what works for you.</p>

---
