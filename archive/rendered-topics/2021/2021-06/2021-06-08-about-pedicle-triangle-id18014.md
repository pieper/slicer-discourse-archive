# About pedicle triangle

**Topic ID**: 18014
**Date**: 2021-06-08
**URL**: https://discourse.slicer.org/t/about-pedicle-triangle/18014

---

## Post #1 by @jumbojing (2021-06-08 13:22 UTC)

<h1><a name="p-60783-pediclescrewsimulator-1" class="anchor" href="#p-60783-pediclescrewsimulator-1" aria-label="Heading link"></a>PedicleScrewSimulator</h1>
<h2><a name="p-60783-about-the-pedicle-tirangle-2" class="anchor" href="#p-60783-about-the-pedicle-tirangle-2" aria-label="Heading link"></a>About the Pedicle Tirangle</h2>
<p>The author mainly made improvements to <a href="https://github.com/lassoan/PedicleScrewSimulator/blob/master/PedicleScrewSimulator/PedicleScrewSimulatorWizard/LandmarksStep.py" rel="noopener nofollow ugc">LandmarksStep.py</a> of this project.We proposed the concept of <strong>the Pedicle Tirangle</strong>, which refers to the three points of the same vertebral body: <strong>the Vertebral Anterior Point (VAP)</strong> and <strong>the Pedicle Isthmus Point(PIP)</strong> of the left and right, formed by  As shown in the figure below: the VAP refers to the anterior midpoint of the vertebral body, and the PIP is based on the largest transverse diameter of the vertebral canal as the coronal plane, and the midpoint of the pedicle on both sides of the plane.  According to these three points, the plug-in forms the axis of the pedicle by connecting the VAP and the lPIP and rPIP, respectively. In addition, we also designs a preliminary estimate of the length and radius of the pedicle screw.<br>
<img src="https://user-images.githubusercontent.com/10215735/121105248-508ae080-c836-11eb-9a7b-1e3dfc32a47f.png" alt="image" width="600" height="500"></p>
<p><img src="https://user-images.githubusercontent.com/10215735/121105290-6b5d5500-c836-11eb-952d-26c1bf34d70d.png" alt="image" width="616" height="500"></p>
<p>作者主要是针对这个项目的<a href="https://github.com/lassoan/PedicleScrewSimulator/blob/master/PedicleScrewSimulator/PedicleScrewSimulatorWizard/LandmarksStep.py" rel="noopener nofollow ugc">LandmarksStep.py</a> 进行了改进,我们提出了<strong>the Pedicle Tirangle</strong>的概念,它是指同一椎体的三个点:即椎前点和左右最窄点,所形成的三角形.如下图所示:椎前点是指椎体前中点,椎弓根最窄点则是以椎管最大横径为冠状面,在该平面两侧椎弓根的中点.取得这三个点以后,插件通过分别连接椎前点和左右最窄点,形成椎弓根的轴线.同时插件还设计了椎弓根螺钉长度和半径的初步估算.</p>
<p><a href="https://github.com/jumbojing/PedicleScrewSimulator" rel="noopener nofollow ugc">jumbojing/PedicleScrewSimulator: 3D Slicer module for pedicle screw insertion training (github.com)</a></p>
<p>【pedicle triangle-哔哩哔哩】<a href="https://b23.tv/KyVcMO" rel="noopener nofollow ugc">https://b23.tv/KyVcMO</a></p>

---

## Post #2 by @lassoan (2021-06-08 19:37 UTC)

<p>Thank you for sharing these developments.</p>
<p>The extension was originally developed for pedicle screw placement training (for example, measurement of the screw length is intentionally not developed - that is one of the skills that the trainees have to learn), but obviously with some changes the module can be adapted to become a surgical planning tool. We need figure out a way how to manage these two variants:</p>
<ul>
<li>Option A: convert the current training module to a surgical planning module (the module could no longer be used for training)</li>
<li>Option B: develop the planning module completely separately from the training module (two separate modules that do not share any code)</li>
<li>Option C: have a separate training and planning module, but share some code</li>
<li>Option D: keep a single module but let the user choose between “training” or “surgical planning” modes</li>
</ul>
<p>It seems that you have now implemented Option A, which means that we lose a number of features. I would particularly miss the beautiful screw models and animated screw insertion. I believe this sophisticated graphics and animation is that makes so many people like this module.</p>
<p>Option B. would be the easiest short-term solution. It would mean that we would have full training and planning modules, without losing any features or having to invest time into refactoring. The disadvantage is that this would double the cost of long-term maintenance (each bug and enhancement would need to be implemented twice, in both modules).</p>
<p>Option C. Would be similar to B in term of user experience but it would require some work right now to refactor the modules. Unlike option B, this option would not double the maintenance effort in the long term.</p>
<p>Option D. Would require significant redesign now (introducing the two operation modes), it might be a bit confusing for users, and it may make a bit more difficult to optimize the user experience in the long term (for example, each change to make the module more friendly for surgical planning may make the module less optimal for training).</p>
<p><a class="mention" href="/u/jumbojing">@jumbojing</a> What are your long term plans with this extension? Do you plan to continue using and developing it? What features do you plan to add? Do you plan to use it with surgical navigation (tool guidance with optical tracker)? Do you plan to add real-time imaging (ultrasound or surface scanner)? Do you plan to use it on patients?</p>
<p><a class="mention" href="/u/ungi">@ungi</a> Do you think it would be important to preserve a training module (with visual alignment and insertion of realistic screw models)?</p>

---

## Post #3 by @jumbojing (2021-06-08 23:24 UTC)

<p>这个extension是我们开发的经皮三维导向穿刺系统的一部分,该导向系统,还包括导向设备和定向模板.借助这个系统实现精准的微创手术的术中定位是我们的目的.<br>
目前分享的这一部分,是在探索一种新的经皮椎弓根穿刺的简洁而统一的影像学的解决方案.<br>
好吧…因为时间和能力的问题,我放弃了您说是的那些测量和"the beautiful screw models and animated screw insertion".关于测量的部分,我们的插件给出了一个解决方案,包括螺钉长度和直径的估算.那个’美丽的动画’,计算出了穿刺轴线后,让"美丽的螺钉动态插入"似乎也没那么难吧.<br>
选项的话,我更倾向于<strong>D</strong>.毕竟目的不同,我不太了解培训…</p>
<blockquote>
<p>This extension is part of the percutaneous three-dimensional guided puncture system developed by us. The guiding system also includes a guiding device and a directional template. With this system, it is our goal to achieve precise intraoperative positioning for minimally invasive surgery.<br>
This part of the current sharing is exploring a new concise and unified imaging solution for percutaneous pedicle puncture.<br>
Well… because of time and ability issues, I gave up those measurements and “the beautiful screw models and animated screw insertion” as you said. Regarding the measurement part, our plug-in gives a solution, including screws Estimation of length and diameter. That “beautiful animation”, after calculating the puncture axis, it seems that “beautiful screw dynamic insertion” is not that difficult.<br>
For the option, I prefer <strong>D</strong>. After all, the purpose is different, and I don’t know much about training…</p>
</blockquote>

---

## Post #4 by @ungi (2021-06-09 00:07 UTC)

<p>I haven’t used this module, and I don’t know anyone actively using it. So I don’t know how important it is to preserve the original training functions.</p>

---

## Post #5 by @lassoan (2021-06-09 04:30 UTC)

<p>Thanks for the additional information. If you don’t want to deal with the training use case then option D will not work, because that would mean a tight integration of training and planning/guidance module.</p>
<p>Based on what you describe, C seemed to be the best option - have two separate modules that share some of the code. I’ve updated your pull request and merged your changes accordingly (creating a new PedicleScrewPlanner module, which shares implementation of some steps with the simulator module).</p>

---

## Post #6 by @slicer365 (2021-06-10 08:02 UTC)

<p>About this topic ,there are two modules in Training,what is the difference between them ,the Planner seems don’t work well.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0ab171d7355e875df4ad562e4c7730eb805b1380.png" alt="捕获" data-base62-sha1="1wAWMSwgmCP01QlPyBA3qFxfDmo" width="487" height="79"></p>

---

## Post #7 by @jumbojing (2021-06-10 08:11 UTC)

<p>具体哪里出问题了呢?</p>
<blockquote>
<p>What exactly went wrong?</p>
</blockquote>

---

## Post #8 by @slicer365 (2021-06-10 08:14 UTC)

<p>Could you help explain the difference between the two modules?</p>

---

## Post #9 by @jumbojing (2021-06-10 08:16 UTC)

<p><a href="https://github.com/jumbojing/PedicleScrewSimulator-1" rel="noopener nofollow ugc">jumbojing/PedicleScrewSimulator-1: 3D Slicer module for pedicle screw insertion training (github.com)</a></p>

---

## Post #10 by @drvarunagarwal (2021-06-10 10:30 UTC)

<p>Hi,</p>
<p>I have trying to install planner but can’t find in the extension manager.<br>
Please advise how to install</p>
<p>thanks</p>

---

## Post #11 by @jumbojing (2021-06-10 10:46 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a555f3361e94218b09c266e5df4920c601dbe708.jpeg" data-download-href="/uploads/short-url/nACVDWkkXiZ2lhX7O8eAMR1N0xy.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a555f3361e94218b09c266e5df4920c601dbe708_2_690x190.jpeg" alt="image" data-base62-sha1="nACVDWkkXiZ2lhX7O8eAMR1N0xy" width="690" height="190" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a555f3361e94218b09c266e5df4920c601dbe708_2_690x190.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a555f3361e94218b09c266e5df4920c601dbe708_2_1035x285.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a555f3361e94218b09c266e5df4920c601dbe708_2_1380x380.jpeg 2x" data-dominant-color="F5F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2858×788 125 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>在"training"类别里,或者搜索"pedicle"</p>
<blockquote>
<p>find in the “training” category, or search for “pedicle”</p>
</blockquote>

---

## Post #12 by @drvarunagarwal (2021-06-10 10:50 UTC)

<p>But it shows pedicle screw simulator</p>

---

## Post #13 by @jumbojing (2021-06-10 10:52 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/16fac7066a4a9a19d642785844c7751117725d70.jpeg" data-download-href="/uploads/short-url/3hhN8wCPfmW5sst5llLQsAKBd04.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/16fac7066a4a9a19d642785844c7751117725d70_2_690x224.jpeg" alt="image" data-base62-sha1="3hhN8wCPfmW5sst5llLQsAKBd04" width="690" height="224" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/16fac7066a4a9a19d642785844c7751117725d70_2_690x224.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/16fac7066a4a9a19d642785844c7751117725d70_2_1035x336.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/16fac7066a4a9a19d642785844c7751117725d70.jpeg 2x" data-dominant-color="BEBFC1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1156×376 75.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>下载安装后又2个模块</p>
<blockquote>
<p>there are 2 modules after downloading and installing</p>
</blockquote>

---

## Post #14 by @drvarunagarwal (2021-06-10 11:09 UTC)

<p>Found it<br>
my bad</p>
<p>it is working nicely.<br>
How to select screw width?</p>

---

## Post #15 by @jumbojing (2021-06-10 11:12 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b8b1803b2dfd018bb821d01341edec9184a2ff8.png" data-download-href="/uploads/short-url/hCUJD4wKs7iUXswdI3NZKDYzDeM.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b8b1803b2dfd018bb821d01341edec9184a2ff8_2_690x286.png" alt="image" data-base62-sha1="hCUJD4wKs7iUXswdI3NZKDYzDeM" width="690" height="286" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b8b1803b2dfd018bb821d01341edec9184a2ff8_2_690x286.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b8b1803b2dfd018bb821d01341edec9184a2ff8_2_1035x429.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b8b1803b2dfd018bb821d01341edec9184a2ff8.png 2x" data-dominant-color="E5E7E8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1306×542 66.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>插件会自动估算(目前还不稳定),修改直径在这里</p>
<p>The plug-in will automatically estimate the diameter (currently not stable), modify the diameter here.</p>

---

## Post #16 by @drvarunagarwal (2021-06-10 11:13 UTC)

<p>thanks</p>
<p>Have u tried automated palcement?<br>
that means auto determining VAP and PIP?</p>

---

## Post #17 by @jumbojing (2021-06-10 11:15 UTC)

<p>auto determining VAP and PIP?<br>
No.You need to manually select “VAP and PIP”.</p>

---

## Post #18 by @drvarunagarwal (2021-06-10 11:17 UTC)

<p>Is the auto placement possible?</p>

---

## Post #19 by @jumbojing (2021-06-10 11:19 UTC)

<p>可能,不过要用到类似人脸识别这样的技术,目前还做不到</p>
<blockquote>
<p>Possibly, but it is not possible now to use technologies like face recognition…</p>
</blockquote>

---

## Post #20 by @jumbojing (2021-06-10 11:23 UTC)

<p>一个椎体,选择3点,确定穿刺角度,螺钉长度和螺钉直径,只能做这些</p>
<blockquote>
<p>A vertebral body, choose 3 points(vap,lpip and rpip), determine the puncture angle, screw length and screw diameter, you can only do these</p>
</blockquote>

---
