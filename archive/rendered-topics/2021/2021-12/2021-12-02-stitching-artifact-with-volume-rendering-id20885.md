---
topic_id: 20885
title: "Stitching Artifact With Volume Rendering"
date: 2021-12-02
url: https://discourse.slicer.org/t/20885
---

# Stitching artifact with volume rendering

**Topic ID**: 20885
**Date**: 2021-12-02
**URL**: https://discourse.slicer.org/t/stitching-artifact-with-volume-rendering/20885

---

## Post #1 by @Hao_Li (2021-12-02 13:56 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/673f976ba22148939d0b60e60e7120f4e4231cca.jpeg" data-download-href="/uploads/short-url/eJnqggC3nTSbKCxa72ajUhyKiLg.jpeg?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/673f976ba22148939d0b60e60e7120f4e4231cca_2_690x423.jpeg" alt="Screenshot" data-base62-sha1="eJnqggC3nTSbKCxa72ajUhyKiLg" width="690" height="423" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/673f976ba22148939d0b60e60e7120f4e4231cca_2_690x423.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/673f976ba22148939d0b60e60e7120f4e4231cca_2_1035x634.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/673f976ba22148939d0b60e60e7120f4e4231cca_2_1380x846.jpeg 2x" data-dominant-color="5D5D64"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">1506×924 138 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Hi! I’ve ran into some problems with Radeon RX 6900 XT graphic card, Ryzen9 5900X, 128G RAM,  using slicer versions 4.11.20210226 and 4.13.0-2021-12-01.</p>
<p>The volumes seem to have stiched in wrong orders in 3D. There is no problem using Nvidia graphic cards 3090, 1080Ti and 1070 using same settings opening same files.</p>
<p>Another issue is regarding 3D volume rendering of different file sizes. The file shown in figure is around 11Gb. Certain files around 4-8Gb can not be rendered, nothing is shown in the 3D window when the volume rendering eye is clicked. Same is with all files I’ve tried between 12-16Gb. The same files are fine when rendered in Nvidia cards 3090 and 1080Ti. 3090 can render files larger than 24Gb.</p>
<p>Many thanks!</p>
<p>Best regards<br>
Hao Li</p>

---

## Post #2 by @pieper (2021-12-02 15:32 UTC)

<p>Thanks for reporting, it can be hard to know when mixing different hardware and drivers will lead to trouble, particularly for large datasets where hardware limits might come into play.  In this case it might be the dimensions of the volumes - maybe volumes that pass certain sizes in one dimension lead to this kind of issue.</p>
<p>Slicer delegates volume rendering to VTK, so the best way to document and perhaps fix these issues is to supply pure-VTK scripts and sample data the VTK developers with information about how to replicate the issues (exactly which card/driver combinations lead to the issues).  See <a href="https://discourse.slicer.org/t/trying-to-diagnose-an-issue-with-virtualgl-and-slicer/17685/27">this thread</a> for a somewhat similar issue.  The issues may be fixable or they may at least be detectable so the user is warned of possible failure modes.</p>
<p>In the mean time, probably best is to use the CropVolume module to either resize or subset the volume of interest so that it can be rendered on the available hardware.</p>

---

## Post #3 by @lassoan (2021-12-02 16:16 UTC)

<p>Stitching artifacts while rendering large volumes AMD GPUs can be solved by adjusting the number of partitions by copy-pasting a few lines of Python code as shown here:</p>
<aside class="quote quote-modified" data-post="18" data-topic="16390">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/stitching-artifact-with-volume-rendering-large-volumes-feb-17-2021-nightly/16390/18">Stitching artifact with volume rendering large volumes (Feb 17 2021 nightly)</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    OKAY!  (1,1,2) seems to work! 
THANKS A MILLION!! 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1ffed7dc4554e393f1678ba0f87ce78f78a90ebc.jpeg" data-download-href="/uploads/short-url/4z2NDD3c70dm3OsiXndQuzzuqks.jpeg?dl=1" title="image" rel="noopener nofollow ugc">[image]</a>
  </blockquote>
</aside>

<p>I would recommend to go with NVidia if you need to render large volumes. Either AMD drivers are lower quality, or maybe NVidia drivers are just as bad but VTK is tested more with NVidia and so VTK contains more fixes or workarounds for NVidia bugs.</p>

---

## Post #4 by @Hao_Li (2021-12-03 13:57 UTC)

<p>Hi!</p>
<p>Thank you for reply!<br>
Maybe it was a mistake to buy AMD graphic card, all Nvidia ones were sold out :S.</p>
<p>Sorry to bother you again. I’m not very technical, I’ve copied and pasted the lines in the Python Interactor and got a few red messages… I’m sure I’ve missed something there…</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/eac863047d46203dc0a760db3f5d650b106e85e1.jpeg" data-download-href="/uploads/short-url/xuZ3oDAVBYkAq18b0GM19RfKFDH.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eac863047d46203dc0a760db3f5d650b106e85e1_2_690x388.jpeg" alt="image" data-base62-sha1="xuZ3oDAVBYkAq18b0GM19RfKFDH" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eac863047d46203dc0a760db3f5d650b106e85e1_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eac863047d46203dc0a760db3f5d650b106e85e1_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eac863047d46203dc0a760db3f5d650b106e85e1_2_1380x776.jpeg 2x" data-dominant-color="AEAFC4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 164 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Regarding large volumes, I suppose it depends on pixels/voxels? The scan I’m working with is a small cube around 20 x 20 x 20mm.</p>
<p>Warmest regards from Uppsala Sweden</p>

---

## Post #5 by @mikebind (2021-12-03 17:34 UTC)

<p>The line right above the line generating the error is incomplete. You need something like this:</p>
<p><code>vrMapper = vrDisplayableManager.GetVolumeMapper(getNode('1637L_9um_PR1000'))</code></p>
<p>whereas you have this:</p>
<p><code>vrMapper = vrDisplayableManager.GetVolumeMapper</code></p>
<p>Give that a try!</p>

---

## Post #6 by @pieper (2021-12-03 17:55 UTC)

<p>And in terms of volume size we mean pixels, not physical units.  Look at the Dimensions in the Volumes module under Volume Information</p>

---

## Post #7 by @Hao_Li (2021-12-07 12:50 UTC)

<p>Hi! Thank you for the replies!</p>
<p>I have tried, without understanding what I did …</p>
<blockquote>
<blockquote>
<blockquote>
<p>vrMapper = vrDisplayableManager.GetVolumeMapper(getNode(‘1637L_9um_PR1000’))<br>
vrMapper.SetPartitions(2,2,2)<br>
vrMapper.SetPartitions(4,4,4)<br>
vrMapper.SetPartitions(1,1,4)<br>
vrMapper.SetPartitions(1,1,2)<br>
vrMapper.SetPartitions(1,2,2)<br>
vrMapper.SetPartitions(2,2,1)<br>
vrMapper.SetPartitions(4,2,1)<br>
vrMapper.SetPartitions(4,2,2)<br>
vrMapper.SetPartitions(3,2,2)<br>
vrMapper.SetPartitions(3,2,2)<br>
vrMapper.SetPartitions(3,2,1)</p>
</blockquote>
</blockquote>
</blockquote>
<p>And clicked on the “eye” button a few times in between, nothing seemed to have changed <img src="https://emoji.discourse-cdn.com/twitter/dizzy_face.png?v=12" title=":dizzy_face:" class="emoji" alt=":dizzy_face:" loading="lazy" width="20" height="20"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7d9e9f821461c850979afea88c61ae9addabfff4.jpeg" data-download-href="/uploads/short-url/hVhwZIvHPrsKyDep6diLg2DQfUo.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7d9e9f821461c850979afea88c61ae9addabfff4_2_690x388.jpeg" alt="image" data-base62-sha1="hVhwZIvHPrsKyDep6diLg2DQfUo" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7d9e9f821461c850979afea88c61ae9addabfff4_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7d9e9f821461c850979afea88c61ae9addabfff4_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7d9e9f821461c850979afea88c61ae9addabfff4_2_1380x776.jpeg 2x" data-dominant-color="A0A1B3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 173 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>My image dimensions are 1950 x 1830 x 1600.</p>
<p>Are there are other saves I can try?</p>
<p>Best regards<br>
Hao Li</p>

---

## Post #8 by @pieper (2021-12-07 12:58 UTC)

<p>You could try cropping or resizing to see what sizes work, and see if you can work with any resolution loss.  You might also be able to crop into two pieces and use the multivolume mode to show both, but there will probably be as seam where they abut.</p>
<p>When there’s a volume rendering issue like this it’s probably in the VTK layer.  Best way to work towards a fix is to share a pure-VTK example that demonstrates the issue clearly and post it as a VTK issue.  As a rule the VTK community wants everything to work well, but hardware/driver issues are known to be very hard to fix.  Maybe there’s a workaround that could be applied in Slicer.</p>
<p>You might be able to start by dropping your data into an example like this:</p>
<p><a href="https://kitware.github.io/vtk-examples/site/Cxx/VolumeRendering/SmartVolumeMapper/" class="onebox" target="_blank" rel="noopener">https://kitware.github.io/vtk-examples/site/Cxx/VolumeRendering/SmartVolumeMapper/</a></p>

---

## Post #9 by @hherhold (2021-12-07 13:01 UTC)

<p>I think you need to restart slicer in between each setPartitions() attempt. Let me know if this isn’t clear - replying on phone, sorry for short post.</p>

---

## Post #10 by @Hao_Li (2021-12-08 09:42 UTC)

<p>Hi! Thank you for all helps! I have tested to restart after every setPartitions attempts and with eyes on and off. No difference seem to be noticed.</p>
<p>I have a general feeling it’s the driver of radeon rx 6900 xt which is the problem.</p>
<p>The file I have demonstrated is around 11Gb, it can be visualized, although not correctly.</p>
<p>I have tested another file around 7Gb, which cannot be visualized at all using GPU, nothing seemed to happen (CPU works slow but shows 3D correctly). Nvidia cards acted in the same way before 2019 Dec. A driver update after that date solved the problem. Hopefully AMD will eventually update their drivers and everything will work wonder <img src="https://emoji.discourse-cdn.com/twitter/dizzy_face.png?v=10" title=":dizzy_face:" class="emoji" alt=":dizzy_face:">  I’ll give up for now.</p>
<p>Best regards<br>
Hao Li</p>

---

## Post #11 by @davide445 (2021-12-10 17:50 UTC)

<p><a class="mention" href="/u/hao_li">@Hao_Li</a> I was thinking to get an RX 6800 XT or 6900 XT for a project using also the VR module.<br>
Might I ask if you are under Windows, or Linux, and if have had also the opportunity to test in VR<br>
And finally you was using Normal or Adaptive quality.</p>

---

## Post #12 by @Hao_Li (2021-12-10 20:18 UTC)

<p>Hi! I ran slicer with 6900XT on windows 10 Pro under Normal quality. I did not have the possibility to test VR. It was very buggy with 6900XT. Probably data I was working with are very large.</p>
<p>I also run slicer with Nvidia 3090, 1080TI and 1070. Even with 3090, Adaptive quality feels slow.</p>

---
