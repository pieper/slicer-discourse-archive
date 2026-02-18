# Can the robot be shown as its actual physical size？

**Topic ID**: 25558
**Date**: 2022-10-05
**URL**: https://discourse.slicer.org/t/can-the-robot-be-shown-as-its-actual-physical-size/25558

---

## Post #1 by @xiaosnowqiang (2022-10-05 12:40 UTC)

<p>Hello guys ，today I try to configuration my own robot in slicer with transforms module. And the configuration has finished and I can simulate rotation around each joint by receive the transform from MATLAB code. The below GIF can see the result of my simulate.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bdf12183a5928baff42a38275c0049ebf280440d.gif" alt="GIF67" data-base62-sha1="r6iRtw6WD4d44y6GIVMPoO7kAuF" width="378" height="339" class="animated"><br>
But the big problem is each part link of STL files  uses m as coordinate system units which is not the Slicer units mm[I don’t know how to change the robot unit becuase the robot stl files download from the flexiv robotic company website]. When I load a MRI image  to slicer and use the Volume Rendering module，because  the robot is too tiny size the MRI model direct covered the robot.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c956acc2465f8bcfed5069bc5d12aae758cd89d8.jpeg" alt="I6VQNL@FVL3IC1@1B~1UT$S" data-base62-sha1="sJ7FDqvzvKs4t4PtJk59zMIDnba" width="381" height="346"><br>
So i just wonder if the 3D slicer can rescale the robot size to the actual physical size without change the configuration.<br>
Hope someone can help me with this,<br>
Best,<br>
-jian</p>

---

## Post #2 by @muratmaga (2022-10-05 21:32 UTC)

<aside class="quote no-group" data-username="xiaosnowqiang" data-post="1" data-topic="25558">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/xiaosnowqiang/48/16426_2.png" class="avatar"> xiaosnowqiang:</div>
<blockquote>
<p>link of STL files uses m as coordinate system units</p>
</blockquote>
</aside>
<p>If you are certain, simply create a linear transform with first three diagonal elements set to 1000 1000 1000 (mm to meters scaling), and put your robot model under that transform.</p>

---

## Post #3 by @xiaosnowqiang (2022-10-06 02:04 UTC)

<p>Thank you for your kindness reply, and I’m a novice and didn’t understand this usage before. It’s great. It solves my problem.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/439b6c5e08c72a789698760e9bfd26b2bde6b009.png" data-download-href="/uploads/short-url/9E4YYhSsjhFChPXX3IuEt4w2Hnr.png?dl=1" title="图片" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/439b6c5e08c72a789698760e9bfd26b2bde6b009.png" alt="图片" data-base62-sha1="9E4YYhSsjhFChPXX3IuEt4w2Hnr" width="517" height="321" data-dominant-color="D2D2E5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">图片</span><span class="informations">974×606 56.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/afb90999a3d6ea05c2f1786e9dd641a3d9bb62e1.png" data-download-href="/uploads/short-url/p4vZTDDezD1u8ZVihiaVDlAWna9.png?dl=1" title="图片" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/afb90999a3d6ea05c2f1786e9dd641a3d9bb62e1_2_517x234.png" alt="图片" data-base62-sha1="p4vZTDDezD1u8ZVihiaVDlAWna9" width="517" height="234" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/afb90999a3d6ea05c2f1786e9dd641a3d9bb62e1_2_517x234.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/afb90999a3d6ea05c2f1786e9dd641a3d9bb62e1_2_775x351.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/afb90999a3d6ea05c2f1786e9dd641a3d9bb62e1.png 2x" data-dominant-color="CBCBE0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">图片</span><span class="informations">839×381 31.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @slicer365 (2023-06-26 00:14 UTC)

<p>Can you share the robot model?</p>

---

## Post #5 by @lassoan (2023-06-26 15:05 UTC)

<p>Note that there is a new extension - SlicerROS2 - that automatically retrieves the robot model from ROS2 and displays it in real-time in Slicer. See more information <a href="https://projectweek.na-mic.org/PW39_2023_Montreal/Projects/Slicerros2/">here</a>.</p>

---

## Post #6 by @xiaosnowqiang (2023-06-30 10:43 UTC)

<p>Hello, sorry for this delay reply.The robot model from this link: <a href="https://github.com/xiaosnowqiang/flexiv_ros2" rel="noopener nofollow ugc">xiaosnowqiang/flexiv_ros2: ROS2 integration of RDK for Flexiv robots. (github.com)</a></p>

---
