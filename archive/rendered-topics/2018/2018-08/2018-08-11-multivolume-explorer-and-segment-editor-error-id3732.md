---
topic_id: 3732
title: "Multivolume Explorer And Segment Editor Error"
date: 2018-08-11
url: https://discourse.slicer.org/t/3732
---

# MultiVolume Explorer and Segment Editor Error

**Topic ID**: 3732
**Date**: 2018-08-11
**URL**: https://discourse.slicer.org/t/multivolume-explorer-and-segment-editor-error/3732

---

## Post #1 by @aginn (2018-08-11 16:10 UTC)

<p>Hi all - I am trying to load a cine-MRI (link to data is below). I was able to import it through the DICOM import, but the results look off.</p>
<p>Furthermore, when I go to “volume rendering,” there is no volume generated, but when I go to the “volume” module, it shows a volume is present.</p>
<p>Also, I am not able to use the segment editor module for some reason. It is not reading the correct pixel values. I attached a screenshot of an attempt to use thresholding in the “Segment Editor” module, but the results do not make sense. The parts that it thresholds appear to be random.</p>
<p>Any help would be appreciated - thanks in advance.</p>
<p>LINK: <a href="https://drive.google.com/drive/folders/1Av3KorE_H6tt77zmDwat37fWqx24bN_6?usp=sharing" rel="noopener nofollow ugc">https://drive.google.com/drive/folders/1Av3KorE_H6tt77zmDwat37fWqx24bN_6?usp=sharing</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0a5bf615d95ef5f023affc040e390cc877c28175.png" data-download-href="/uploads/short-url/1tDNElwb9AXes1K8j1WrjP1LJCl.png?dl=1" title="1_MultiVolumeExplorer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0a5bf615d95ef5f023affc040e390cc877c28175_2_690x329.png" alt="1_MultiVolumeExplorer" data-base62-sha1="1tDNElwb9AXes1K8j1WrjP1LJCl" width="690" height="329" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0a5bf615d95ef5f023affc040e390cc877c28175_2_690x329.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0a5bf615d95ef5f023affc040e390cc877c28175_2_1035x493.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0a5bf615d95ef5f023affc040e390cc877c28175_2_1380x658.png 2x" data-dominant-color="AAA9B4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1_MultiVolumeExplorer</span><span class="informations">2560×1224 265 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/0115b48a836c8e2580d12ba2106dfecb6bd82347.png" data-download-href="/uploads/short-url/9AYNVjyPpGTGFe6YfPRqwYHHSv.png?dl=1" title="2_VolumeRendering" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0115b48a836c8e2580d12ba2106dfecb6bd82347_2_690x334.png" alt="2_VolumeRendering" data-base62-sha1="9AYNVjyPpGTGFe6YfPRqwYHHSv" width="690" height="334" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0115b48a836c8e2580d12ba2106dfecb6bd82347_2_690x334.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0115b48a836c8e2580d12ba2106dfecb6bd82347_2_1035x501.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0115b48a836c8e2580d12ba2106dfecb6bd82347_2_1380x668.png 2x" data-dominant-color="ABAAB6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2_VolumeRendering</span><span class="informations">2560×1242 255 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cdda853bef5be11dc5ffa6f17b999b400f7bcc22.png" data-download-href="/uploads/short-url/tn43G5Tj5tNEWheuzR3U3pqcpk6.png?dl=1" title="3_SegmentEditor" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cdda853bef5be11dc5ffa6f17b999b400f7bcc22_2_690x344.png" alt="3_SegmentEditor" data-base62-sha1="tn43G5Tj5tNEWheuzR3U3pqcpk6" width="690" height="344" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cdda853bef5be11dc5ffa6f17b999b400f7bcc22_2_690x344.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cdda853bef5be11dc5ffa6f17b999b400f7bcc22_2_1035x516.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cdda853bef5be11dc5ffa6f17b999b400f7bcc22_2_1380x688.png 2x" data-dominant-color="838383"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3_SegmentEditor</span><span class="informations">2544×1270 306 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @fedorov (2018-08-11 19:09 UTC)

<p>The DICOM dataset loaded as a MultiVolume node (4d dataset), which means you cannot use Slicer functionality that work with 3d data.</p>
<p>You can extract individual temporal frames from the miltivolume, and apply those operations. You can also check “Enable copying” which will give you a 3d volume with a copy of the currently selected frame. You can then use Volume rendering to render that frame, and if you toggle “Play” you will see Volume rendering of the temporal changes (as shown in this movie: <a href="https://www.slicer.org/w/images/0/04/BeatingHeart.mov">https://www.slicer.org/w/images/0/04/BeatingHeart.mov</a>).</p>

---

## Post #3 by @aginn (2018-08-11 23:54 UTC)

<p>Thank you! I will try this out.</p>
<p>Is that “Beating Heart” data set shown in the video available to the public for downloading?</p>

---

## Post #4 by @lassoan (2018-08-12 00:37 UTC)

<p>In recent nightly builds, you can load 4D image as volume Sequence (if you install Sequences extension). Sequence browser module provides a 3D proxy node that you can use for segmentation, volume rendering, etc. You can create a corresponding sequence node for 4D segmentation; or segment a single 3D volume and use Sequence Registration extension to automatically extend it to all other time points.</p>

---

## Post #5 by @lassoan (2018-08-12 00:43 UTC)

<p>If you install Sequences extension, then you’ll find two 4D cardiac CTs in Sample Data module that you can load by a single click.</p>

---

## Post #6 by @fedorov (2018-08-13 13:29 UTC)

<aside class="quote no-group" data-username="aginn" data-post="3" data-topic="3732">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/dfb087/48.png" class="avatar"> aginn:</div>
<blockquote>
<p>Is that “Beating Heart” data set shown in the video available to the public for downloading?</p>
</blockquote>
</aside>
<p>Yes, you can download the dataset in the Tutorials section of the module documentation page: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/MultiVolumeExplorer" class="inline-onebox">Documentation/Nightly/Modules/MultiVolumeExplorer - Slicer Wiki</a></p>

---

## Post #7 by @aginn (2018-08-15 03:51 UTC)

<p>Is there any information available such as the patient’s age? Furthermore, are there any good databases that 3D Slicer has access to that features patients with different cardiomyopathies?</p>
<p>Thank you!</p>

---

## Post #8 by @pieper (2018-08-15 11:56 UTC)

<p>There isn’t a lot of public cardiac data, but here’s one source:</p>
<p><a href="http://www.cardiacatlas.org/studies/sunnybrook-cardiac-data/" class="onebox" target="_blank">http://www.cardiacatlas.org/studies/sunnybrook-cardiac-data/</a></p>
<p>If anyone knows of other datasets for research please post.</p>

---

## Post #9 by @fedorov (2018-08-15 13:55 UTC)

<aside class="quote no-group" data-username="aginn" data-post="7" data-topic="3732">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/dfb087/48.png" class="avatar"> aginn:</div>
<blockquote>
<p>Is there any information available such as the patient’s age?</p>
</blockquote>
</aside>
<p>If you refer to the dataset linked from the documentation page, there is no further information available about the patient scanned.</p>

---

## Post #10 by @elham (2019-03-10 15:45 UTC)

<p>I have the same question. When I open shortaxis Cardiac MR Image, I can just see an image like what Aginn share here.<br>
Can I open these image through sequence? How can I do that?<br>
I think the problem is that slicer show DIOCOM image in sagital/coronal/axial coordinates but I need a shortaxis/longaxis coordinate.</p>

---

## Post #11 by @lassoan (2019-03-13 23:37 UTC)

<p>Do you have a single-slice time sequence (2D+t) or a volume sequence (3D+t)?</p>

---

## Post #12 by @elham (2019-03-29 07:10 UTC)

<p>I can open my cardiac shortaxis images through “brain strip rotation” module. That’s a module that rotate images and fit them in sagital/coronal/axial coordinate.</p>

---

## Post #13 by @lassoan (2019-03-29 20:18 UTC)

<aside class="quote no-group" data-username="elham" data-post="12" data-topic="3732">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/e/bbce88/48.png" class="avatar"> elham:</div>
<blockquote>
<p>I can open my cardiac shortaxis images through “brain strip rotation” module</p>
</blockquote>
</aside>
<p>I have never heard about this “brain strip rotation” module. Where did you find it?</p>
<p>Note that you can click “Rotate to volume plane” button to align slice views with volume axes (<a href="https://discourse.slicer.org/t/seemingly-distorting-images-from-input-images-mprs/4290/2" class="inline-onebox">Seemingly distorting images from input images (MPRs) - #2 by lassoan</a>).</p>

---

## Post #14 by @Lynx (2019-04-02 03:42 UTC)

<p>I’m now using a cine-mr too.  I want to how can I get result like this:<br>
<a href="https://www.slicer.org/w/images/0/04/BeatingHeart.mov" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.slicer.org/w/images/0/04/BeatingHeart.mov</a><br>
and I can’t get a volume when I go to volume rendering.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/5548daf74a87e6b2ee2c09f5e41d3cd6593afabe.png" data-download-href="/uploads/short-url/casFXIr3QkvRHjC84oLoXwbUBae.png?dl=1" title="%E5%9B%BE%E7%89%87" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/5548daf74a87e6b2ee2c09f5e41d3cd6593afabe.png" alt="%E5%9B%BE%E7%89%87" data-base62-sha1="casFXIr3QkvRHjC84oLoXwbUBae" width="690" height="183" data-dominant-color="E1E6E9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">%E5%9B%BE%E7%89%87</span><span class="informations">950×253 6.19 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I don’t what should I choose to generater a volume(I tried them all but all failed)</p>

---

## Post #15 by @fedorov (2019-04-02 14:38 UTC)

<p>You need to toggle “Enable copying” in MultiVolumeExplorer (red arrow), and then select the frame copy (yellow arrow) as “Volume” in the Volume Rendering module.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/860d83e9bb83e70bda44cddb6782a5d60a272d10.png" alt="image" data-base62-sha1="j7SW7nUwkJZy6jgCR6zkfaUs0Ja" width="543" height="451"></p>

---

## Post #16 by @Lynx (2019-04-04 01:54 UTC)

<p>Thank you. I think maybe there is something wrong with my data. I try out this way using a CT data and it turns out quite successfully. But the cine-MR just cannot come out a volume,  I check these data, their 'content time ’ are not the same, is that a problem?</p>

---

## Post #17 by @xiw (2021-02-05 08:49 UTC)

<p>Hi Andras, could you explain a bit more on how to use Sequence Registration extension to extend the 3D segmentation to the entire sequence？I have loaded my 4D .nii file and I have the segmentation for the 1st and 15th frames, but how should I automatically generate segmentation for the rest frames? Thank you.</p>

---

## Post #18 by @lassoan (2021-05-01 14:27 UTC)

<p>This has been discussed a number of times on this forum for 4D cardiac CTs. Let us know if you cannot find these topics and I’ll dig up a few links.</p>

---

## Post #19 by @Saima (2023-08-29 05:09 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="2" data-topic="3732">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>e. You can then use Volume rendering to render that fr</p>
</blockquote>
</aside>
<p>How can i perform the extraction for multivolume explorer using a script.</p>
<p>regards,<br>
Saima</p>

---

## Post #20 by @Saima (2023-08-29 05:09 UTC)

<p>Hi Fedorov,<br>
How can i do the above you explaned using scripting.</p>
<p>regards,<br>
saima</p>

---

## Post #21 by @Saima (2023-08-29 05:48 UTC)

<p>Hi Fedorov,<br>
I know that slicer modules are accessed like below:<br>
slicer.modules.multivolumeexplorer</p>
<p>how can i run the module and extract the 2 frame number and then click copy frame to copy the frame selected. How can this be performed using the script?</p>
<p>regards,<br>
Saima</p>

---

## Post #22 by @lassoan (2023-08-29 05:48 UTC)

<p>We are transitioning I use the more general Sequences modules instead of MultiVolume Explorer. You can find examples for using that module in the Slicer script repository.</p>

---

## Post #23 by @Saima (2023-08-31 02:04 UTC)

<p>Dear Andras,<br>
I have a nrrd file with two frames. i want to extract the number 1 frame from the nrrd file. I can do it using the multivolume explorer but how can I do it using the script.</p>
<p>i just know the following:<br>
slicer.modules.multivolumeexplorer.logic</p>
<p>regards,<br>
saima</p>

---
