---
topic_id: 14348
title: "Hardware Suggestion And Graphic Cards Ubuntu Or Macos"
date: 2020-10-31
url: https://discourse.slicer.org/t/14348
---

# Hardware suggestion and graphic cards (Ubuntu or MacOS)

**Topic ID**: 14348
**Date**: 2020-10-31
**URL**: https://discourse.slicer.org/t/hardware-suggestion-and-graphic-cards-ubuntu-or-macos/14348

---

## Post #1 by @Marco (2020-10-31 18:14 UTC)

<p>New user here.<br>
I work as a neuroradiologist and love to create 3D models for teaching and research.<br>
The work that the developer are doing with this software is awesome.</p>
<p>I currently use 3D Slicer on a small desktop (Intel NUC i5-8259U, 16GB, 512SSD, Ubuntu 20.04) and on a MacBook Pro (i5-7360U, 8GB, 256SSD, Catalina); I usually make segmentations from DICOM images of interventional procedures to show anatomy and needles/catheters, and performances are quite poor on both especially with “show 3D” activated.<br>
But how to improve them?</p>
<ul>
<li>buying a eGPU that I could use for both?</li>
<li>buying a better desktop PC (maybe the new XPS 8940 i7-10700, RTX 2060)?</li>
<li>buying a 16" MBP with discrete GPU?</li>
</ul>
<p>I’m especially doubtful about graphic cards, OpenGL, drivers (GeForce 1660ti/2060 or Quadro P1000/P2000? Or maybe AMD? Are they compatible with Linux/Ubuntu?), and that’s the reason to consider the 16" MBP.<br>
I am open to all the OS but if I could choose I would go with Linux/Ubuntu.</p>
<p>Thank you very much to anyone who will offer some suggestions.<br>
Marco</p>

---

## Post #2 by @manjula (2020-10-31 18:24 UTC)

<p>Hi you can get a idea,</p>
<aside class="quote no-group" data-username="manjula" data-post="1" data-topic="9937">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar"><a href="https://discourse.slicer.org/t/3d-slicer-hardware-requirements/9937/1">3D Slicer Hardware requirements</a></div>
<blockquote>
<p>As i understand 3D Slicer is mainly built on VTK and ITK. I understand answers to the following will depend on the type of data and size of data and what you are going to do with it but in general is it possible to tell,</p>
</blockquote>
</aside>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#system-requirements">
  <header class="source">

      <a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#system-requirements" target="_blank" rel="noopener nofollow ugc">slicer.readthedocs.io</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#system-requirements" target="_blank" rel="noopener nofollow ugc">Getting Started — 3D Slicer  documentation</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @hherhold (2020-10-31 20:37 UTC)

<p>Just as a data point:</p>
<p>I recently upgraded to a MacBook Pro 16" with the upgraded Radeon Pro 5500M 8BG graphics card and 64GB of memory. I also got a 2TB drive. My needs were specifically geared towards using Slicer.</p>
<p>I do micro-CT of living and fossil insects. My datasets range from 500MB to 3GB in size, and the models I produce are in the tens of millions of polygons (20-50 million polys in a model is not uncommon). I do a lot of segmentation by hand, and I find my setup to be pretty useable. I could have gone for a super powerful dell with a NVIDIA P5000, but that would have been significantly more expensive, and I tend to prefer unix based environments.</p>
<p>I’ve thought about an external GPU, but not taken the plunge. Interested to hear from anyone who has and how it’s worked out.</p>
<p>Hope this helps. Happy to discuss further.</p>

---

## Post #4 by @Marco (2020-10-31 22:30 UTC)

<p>Thank you Herhold for your answer.</p>
<p>That would be nice as the laptop is great and I could work both at home (32" USB-C monitor) and everywhere else, but it is quite expensive compared to a desktop setup. The XPS I mentioned is 3x/4x cheaper than the MBP 16" you mentioned and roughly as powerful (or maybe more).</p>
<p>Considering that my datasets are 500MB-2GB and that this is more like an hobby than my actual work, my specific doubts are:</p>
<ul>
<li>is Quadro better than GeForce because of OpenGL (in the same price range)?</li>
<li>is NVIDIA really better than AMD? Or should I go AMD with Linux because of open source drivers?</li>
<li>if I understand well, CPU is more important than GPU even when showing 3D models during multiple segmentations. Is a 1660ti or 2060 enough or would I see a consistent improvement with a 2070?</li>
<li>can I expect Slicer and Ubuntu to work flawlessly with the XPS I mentioned? Or would Windows work better?</li>
<li>does anyone have experience with Mac or Ubuntu and eGPU for Slicer?</li>
</ul>

---

## Post #5 by @hherhold (2020-10-31 22:42 UTC)

<aside class="quote no-group" data-username="Marco" data-post="4" data-topic="14348">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/a698b9/48.png" class="avatar"> Marco:</div>
<blockquote>
<p>is Quadro better than GeForce because of OpenGL (in the same price range)?</p>
</blockquote>
</aside>
<p>Quadro cards tend to be more powerful.</p>
<aside class="quote no-group" data-username="Marco" data-post="4" data-topic="14348">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/a698b9/48.png" class="avatar"> Marco:</div>
<blockquote>
<p>is NVIDIA really better than AMD? Or should I go AMD with Linux because of open source drivers?</p>
</blockquote>
</aside>
<p>Ho boy, that’s like Ford vs Chevy, or take your pick on industry rivalries. Same on the subject of open source drivers. I would say that if you’re ever planning on doing any kind of machine learning, you should seriously consider NVIDIA. TensorFlow and things like that tend to be NVIDIA-only or at least NVIDIA-preferred. Would be nice if someone would weigh in on this - I do not do machine learning, largely because I have an AMD GPU.</p>
<aside class="quote no-group" data-username="Marco" data-post="4" data-topic="14348">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/a698b9/48.png" class="avatar"> Marco:</div>
<blockquote>
<p>if I understand well, CPU is more important than GPU even when showing 3D models during multiple segmentations. Is a 1660ti or 2060 enough or would I see a consistent improvement with a 2070?</p>
</blockquote>
</aside>
<p>Really, both are important, but if you’re pushing lots of triangles, you want a fast GPU. Also, if you’re doing volume rendering, a GPU is basically required. When you’re segmenting, a fast CPU is good for the segmentation part, and a fast GPU is good for the display of the 3D model. There are things you can do to speed things up (subsampling, decimation, turn off smoothing, etc) and there are a lot of people here who can help you out on that.</p>
<aside class="quote no-group" data-username="Marco" data-post="4" data-topic="14348">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/a698b9/48.png" class="avatar"> Marco:</div>
<blockquote>
<p>can I expect Slicer and Ubuntu to work flawlessly with the XPS I mentioned? Or would Windows work better?</p>
</blockquote>
</aside>
<p>I don’t have any experience with Slicer on Linux but on Windows and Mac it’s fine. In my experience, cross-platform applications tend to be more solid.  “Better” is probably relative. Plenty of people here use Linux.</p>
<p>Hope this helps.</p>

---

## Post #6 by @muratmaga (2020-10-31 22:58 UTC)

<aside class="quote no-group" data-username="Marco" data-post="4" data-topic="14348">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/a698b9/48.png" class="avatar"> Marco:</div>
<blockquote>
<p>is Quadro better than GeForce because of OpenGL (in the same price range)?</p>
</blockquote>
</aside>
<p>Not necessarily.</p>
<p>Marketing difference is Quadro aimed for data center deployment (designed for dense installation) or commercial usage, long-term driver support and some difference in floating point operations (which may cause a difference in performance if you are doing that a lot). Also Quadro driver supports openGL over remote desktop quite good (not an option if you are using Geforce).</p>
<p>If you don’t need the large amount of RAM that Quadro offers, equivalent geforce works well.</p>
<p>As for eGPU, I have no experience. Is there even a Mac driver for those cards?</p>
<p>AMD continues to cap the <a href="https://opengl.gpuinfo.org/displayreport.php?id=5399">GL_MAX_3D_TEXTURE_SIZE</a> at 2K, even for their high-end cards. For Slicer, this means you cannot render a 3D volume on GPU if one of the dimensions is 2049 voxels or larger. Most new Nvidia cards this is 16K or more.</p>
<p>If you are using Linux, I think Nvidia has a much better driver support, at least for Centos and Ubuntu that I am familiar with. Whether the XPS works flawlessly with Linux, you need to check whether Linux is supported by Dell for that particular line. Mostly likely it will work, but occasionally driver weird issues arises (e.g., I had an ideapad from Lenovo that I couldn’t get the wifi card recognized, or the backlight didn’t work).</p>

---

## Post #7 by @hherhold (2020-10-31 23:15 UTC)

<p>Yep, go with Murat’s advice - he’s far more knowledgeable.</p>
<p>I do know there are eGPUs for Macs, but they are AMD based. Never tried one, but would like to.</p>

---

## Post #8 by @manjula (2020-10-31 23:32 UTC)

<aside class="quote no-group" data-username="Marco" data-post="4" data-topic="14348">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/a698b9/48.png" class="avatar"> Marco:</div>
<blockquote>
<p>can I expect Slicer and Ubuntu to work flawlessly with the XPS I mentioned? Or would Windows work better?</p>
</blockquote>
</aside>
<p>Slicer works flawlessly on Linux. (I am using with mint, ubuntu ). have a large swap space around 100 Gb. Also I have used on dell before but not the one that you mentions.</p>
<p>On Linux definitely Nvidia performs better.</p>

---

## Post #9 by @lassoan (2020-11-01 15:32 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="6" data-topic="14348">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Quadro driver supports openGL over remote desktop quite good (not an option if you are using Geforce).</p>
</blockquote>
</aside>
<p>NVidia started to ease up on this about 1-2 years ago. Now I don’t think it is nothing actively disabling remote desktop usage anymore. There may be still some driver incompatibilities. Also, shared usage in a server may violate licensing terms.</p>
<p>In the past we had more compatibility issues with Quadro cards in Slicer. Maybe because it is tested by magnitudes less users on much smaller subset of applications. Also, if someone reports an issue with a Quadro card, it is less likely that we (or VTK or other open-source software developers) can reproduce and debug the issue, because most developers use GeForce cards, too.</p>

---

## Post #10 by @Marco (2020-11-01 16:55 UTC)

<p>Thanks a lot for your support, it helps a lot.</p>
<p>I will go for the desktop i7 + GeForce + Ubuntu as it is open source and seems cost-effective; if anything goes wrong with drivers plan B is switch to Windows.</p>

---

## Post #11 by @muratmaga (2020-11-04 21:16 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="14348">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>NVidia started to ease up on this about 1-2 years ago. Now I don’t think it is nothing actively disabling remote desktop usage anymore.</p>
</blockquote>
</aside>
<p>What I meant by remote rendering is that in a RDP session, I still cannot start Slicer from cold, if the remote computer has a Geforce card installed. If the remote computer has an Quadro, you can launch Slicer from cold and use GPU accelerated rendering. This is with 451.xx series drivers on windows 10 pros.</p>

---

## Post #12 by @lassoan (2020-11-04 21:19 UTC)

<p>You may need to install some extra packages - see <a href="https://www.khronos.org/news/permalink/nvidia-provides-opengl-accelerated-remote-desktop-for-geforce-5e88fc2035e342.98417181">https://www.khronos.org/news/permalink/nvidia-provides-opengl-accelerated-remote-desktop-for-geforce-5e88fc2035e342.98417181</a></p>

---

## Post #13 by @muratmaga (2020-11-04 21:28 UTC)

<p>Wow, I got really excited, and installed as instructed but still doesn’t work for me. Splash screen comes and nothing else.</p>

---

## Post #14 by @lassoan (2020-11-04 21:43 UTC)

<p>Do you use it on a shared server or to connect to a personal computer? I did not play with this much, as for a personal computer VNC, AnyDesk, etc. work similarly well as RDP. For a shared server you might need to do some extra steps to allow sharing GPU between multiple users.</p>

---

## Post #15 by @muratmaga (2020-11-04 22:18 UTC)

<p>It is between my two windows laptops (one with geforce other with quadro). It is not a big deal, I just wanted to give it a quick try…</p>

---

## Post #16 by @hherhold (2021-03-05 17:49 UTC)

<p>Resurrecting this thread after a long hiatus, sorry…</p>
<p>I’m not so sure about the 2048 restriction on AMD cards. I’m using a GL caps viewer on my 2016 MacBook Pro with an AMD Radeon Pro 5500M and the max texture 3D size is 16384. This is also backed up here:  <a href="https://feedback.wildfiregames.com/report/opengl/feature/GL_MAX_3D_TEXTURE_SIZE" class="inline-onebox" rel="noopener nofollow ugc">OpenGL capabilities report: GL_MAX_3D_TEXTURE_SIZE</a></p>

---

## Post #17 by @muratmaga (2021-03-05 17:59 UTC)

<p>It might be.</p>
<p>I am not a Mac user, we got one in the lab and when I searched the <a href="https://opengl.gpuinfo.org" rel="noopener nofollow ugc">https://opengl.gpuinfo.org</a> for Radeon GPUs, all the ones that I looked were capped at 2K. This was by no means an exhaustive search. ANd I see that most of them are reported either on Windows or Linux, there is a curious lack of MacOS listing.</p>
<p>It will be great, if you can verify that your Radeon can render volumes that is 2049 or more in at least one dimensions.</p>
<p>Easiest would be resample MRhead extensively, or use data from MorphoSource.</p>

---

## Post #18 by @hherhold (2021-03-05 18:10 UTC)

<p>Yeah, here’s an AMD entry for MacOS that is relatively recent, and is 16k:</p>
<p><a href="https://opengl.gpuinfo.org/displayreport.php?id=3777" class="onebox" target="_blank" rel="noopener nofollow ugc">https://opengl.gpuinfo.org/displayreport.php?id=3777</a></p>
<p>I’ll make an example dataset using MRHead and make it like 100 x 100 x 3000 and see what happens.</p>
<p>Thanks!!</p>

---

## Post #19 by @hherhold (2021-03-05 19:01 UTC)

<p>OK, here’s MRHead, cropped and resampled to 351x440x4096. So 2048 is not a global AMD limit.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/93f011a6b3774132022d9249392db55b7fa4dea4.jpeg" data-download-href="/uploads/short-url/l6Ix4O8XYR8OItzVOYdKxi1aIxS.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/93f011a6b3774132022d9249392db55b7fa4dea4_2_690x275.jpeg" alt="image" data-base62-sha1="l6Ix4O8XYR8OItzVOYdKxi1aIxS" width="690" height="275" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/93f011a6b3774132022d9249392db55b7fa4dea4_2_690x275.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/93f011a6b3774132022d9249392db55b7fa4dea4_2_1035x412.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/93f011a6b3774132022d9249392db55b7fa4dea4_2_1380x550.jpeg 2x" data-dominant-color="A5A6BE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">3382×1352 452 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
