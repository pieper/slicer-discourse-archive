---
topic_id: 25426
title: "Ik Solution Failed And The Robot Cant Move To The Entry Poin"
date: 2022-09-25
url: https://discourse.slicer.org/t/25426
---

# IK solution failed and the robot can't move to the Entry point

**Topic ID**: 25426
**Date**: 2022-09-25
**URL**: https://discourse.slicer.org/t/ik-solution-failed-and-the-robot-cant-move-to-the-entry-point/25426

---

## Post #1 by @xiaosnowqiang (2022-09-25 05:59 UTC)

<p>Hello guys,I have go throught the ROSIGTLTutorial-ISMR2019 recently, after follow the steps of Fiducial Registration Wizard  the relationship between the robot and the patient<br>
on rviz and 3D Slicer are Confirmed.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae2c042031467c4aaee057d015dd8f63214c8992.png" data-download-href="/uploads/short-url/oQNnNUyOOp3YCOaBQzJPByyoSbM.png?dl=1" title="图片" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/ae2c042031467c4aaee057d015dd8f63214c8992_2_690x263.png" alt="图片" data-base62-sha1="oQNnNUyOOp3YCOaBQzJPByyoSbM" width="690" height="263" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/ae2c042031467c4aaee057d015dd8f63214c8992_2_690x263.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae2c042031467c4aaee057d015dd8f63214c8992.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae2c042031467c4aaee057d015dd8f63214c8992.png 2x" data-dominant-color="6B637E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">图片</span><span class="informations">717×274 87.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
So i continue the tutorial to execution of the plan<br>
（1）copy the plan and rename as Plan Reference<br>
（2）copy the ReferenceToRas and rename as RasToFeference and invert the transform<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6b0be39c7bf270261bea73c5bfdd3c1a7b8a5be.png" data-download-href="/uploads/short-url/zck7W4iJBDGKY5g8HWMdkMMkte6.png?dl=1" title="图片" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f6b0be39c7bf270261bea73c5bfdd3c1a7b8a5be_2_690x204.png" alt="图片" data-base62-sha1="zck7W4iJBDGKY5g8HWMdkMMkte6" width="690" height="204" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f6b0be39c7bf270261bea73c5bfdd3c1a7b8a5be_2_690x204.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6b0be39c7bf270261bea73c5bfdd3c1a7b8a5be.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6b0be39c7bf270261bea73c5bfdd3c1a7b8a5be.png 2x" data-dominant-color="CACEDD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">图片</span><span class="informations">846×251 23.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
（3）Open “RasToReference” transform in “Transforms” and Apply “RasToReference” transform to “Plan-Reference”<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/33c1e8867340d7bd793ce48ea3c5e3987ba5f18e.png" data-download-href="/uploads/short-url/7nRNs1uUAXfm6opHl1E5YRVuqHY.png?dl=1" title="图片" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33c1e8867340d7bd793ce48ea3c5e3987ba5f18e_2_690x187.png" alt="图片" data-base62-sha1="7nRNs1uUAXfm6opHl1E5YRVuqHY" width="690" height="187" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33c1e8867340d7bd793ce48ea3c5e3987ba5f18e_2_690x187.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/33c1e8867340d7bd793ce48ea3c5e3987ba5f18e.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/33c1e8867340d7bd793ce48ea3c5e3987ba5f18e.png 2x" data-dominant-color="CECBE2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">图片</span><span class="informations">997×271 22.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
When all the steps done，the 3D Slicer sense as show below<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/88c998e849a9cdbc740270a7bc5a044b4ec9e0bb.png" alt="图片" data-base62-sha1="jw4R5cCt3NQEYdd0bXq9jOHHmFt" width="614" height="477"><br>
And finally Send “Plan-Reference” in “I/O Configuration”，and from the ros node message the Plan is sent to ROS, but the robot didn’t moves to the<br>
entry, and then the target the message like the below picture<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f8e14b7304edcab2a38acbff6e8bf0488e6cbc56.png" data-download-href="/uploads/short-url/zvH6thhZiQjoc9ufPnbL0xcOYAu.png?dl=1" title="图片" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f8e14b7304edcab2a38acbff6e8bf0488e6cbc56.png" alt="图片" data-base62-sha1="zvH6thhZiQjoc9ufPnbL0xcOYAu" width="690" height="493" data-dominant-color="431B2E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">图片</span><span class="informations">728×521 83.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
And i also change the OMPL planner in Rviz and Moveit but it also can’t solve .<br>
Can someone tell me why ,and thanks in advance.<br>
Best wishes,<br>
-Jian</p>

---

## Post #2 by @lassoan (2022-09-26 18:24 UTC)

<p>The error indicate that the robot cannot physically reach the target position/orientation. It is either because you need to move the robot closer, in a better orientation; or the robot has not been registered correctly to the patient. It is hard to tell which one is the case here from the screenshots and high-level description.</p>

---
