# How to adjust the ROI

**Topic ID**: 15713
**Date**: 2021-01-28
**URL**: https://discourse.slicer.org/t/how-to-adjust-the-roi/15713

---

## Post #1 by @slicer365 (2021-01-28 13:42 UTC)

<p>As this picture shows, the ROI is a cube, and sometimes it may be better to change it to a sphere. Of course, this function PRISM rendering can be implemented, but it will be more convenient if you can directly adjust the ROI. Or is there a corresponding script code to achieve.The other is whether it can make the image of the ROI content disappear, and the image outside the ROI can be displayed<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/7153ba8f7bf2c32fcf92524f8c692b0694a7b545.jpeg" data-download-href="/uploads/short-url/gaxldm6UtUd4LZgsF6F8Hj9vUqx.jpeg?dl=1" title="捕获" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7153ba8f7bf2c32fcf92524f8c692b0694a7b545_2_690x353.jpeg" alt="捕获" data-base62-sha1="gaxldm6UtUd4LZgsF6F8Hj9vUqx" width="690" height="353" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7153ba8f7bf2c32fcf92524f8c692b0694a7b545_2_690x353.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7153ba8f7bf2c32fcf92524f8c692b0694a7b545_2_1035x529.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/7153ba8f7bf2c32fcf92524f8c692b0694a7b545.jpeg 2x" data-dominant-color="ABABAF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">捕获</span><span class="informations">1365×699 105 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2021-01-28 13:52 UTC)

<p>It’s not real-time like the ROI, but you can get install the Segment Editor Extra Effects and then use the Mask Volume to make arbitrary shapes.</p>

---

## Post #3 by @slicer365 (2021-01-28 13:58 UTC)

<p>Thanks for your reply, Doctor , I would like to know if I can change the ROI to a sphere, I think this setting should be easier, but I don’t know how to adjust the script</p>

---

## Post #4 by @lassoan (2021-01-28 14:17 UTC)

<p>Currently, you can simulate sphere ROI by interacting with markups points or rectangular ROI (see example script <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Specify_a_sphere_by_multiple_of_markups_points">here</a>). You can use PRISM (or create a custom module with a streamlined GUI for making things simpler for the users) to clip with that ROI.</p>
<p>In a few weeks we will have sphere ROI (you can monitor status of this <a href="https://github.com/Slicer/Slicer/issues/5061">here</a>), which solves the first part of the problem. I am not sure if non-rectangular ROIs will be supported by volume rendering module or you will need an external module, because there are just so many special cuts and effects that you can imagine that we cannot add everything the volume rendering module directly. Probably we’ll make PRISM module more user friendly instead.</p>
<p>What is your use case? How do you plan to use spherical clipping? Is there any additional volume rendering effects (special coloring, highlighting, etc.) that you would ideally would like to use?</p>

---

## Post #5 by @slicer365 (2021-01-28 15:41 UTC)

<p>Dear professor, do you consider replacing the ROI in Volume Rendering with the sphere tool in PRISM rendering? I believe this is a favorite of many users. Because sometimes we need to simulate the skull window. Of course I know that mask volume or Clip volume with ROI can be used, but that is complicated,and that is the real cut, not hiding, sometimes we just need to hide part of it.</p>

---

## Post #6 by @lassoan (2021-01-28 16:12 UTC)

<p>In the long term, probably we will need custom volume rendering methods for each rendering use case. These specialized methods will have more inputs than just a volume and ROI (for example they may take additional points, lines, volumes, segmentations, sliders, checkboxes, combo boxes, etc.) and many of the parameters that are currently shown in Volume rendering module will not be necessary to modify.</p>
<p>To get there, the current plan is to:</p>
<ul>
<li>keep Volume rendering module more or less as is</li>
<li>use PRISM module to allow specification and testing of advanced volume rendering methods</li>
<li>create custom modules for each major rendering scenario with a simple user interface, which exposes all the necessary options and only those. For example we could have separate modules for 4D cardiac echo, 4D endovascular CT, brain MRI surgical planning, brain MRI real-time surgical guidance. These would be simple and small Python scripted modules that could be easily cloned and customized easily for new applications. These modules can be small because they are all just thin wrappers around features provided by other lower-level modules.</li>
</ul>
<p>We already have such a custom volume rendering module for 4D cardiac echo, which we will refine and can use as a template for other modules. Until these specialized modules come out, you can use PRISM directly (any suggestions are welcome about how to make it more convenient) or you can implement your own custom module that allows users to choose input nodes and parameters and sets up volume rendering accordingly.</p>

---

## Post #7 by @MirandaJO98 (2021-02-01 11:32 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="15713">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>keep Volume rendering module more or less as is</p>
</blockquote>
</aside>
<p>So it means “Do not change at all”, right?</p>

---

## Post #8 by @lassoan (2021-02-01 17:11 UTC)

<p>Changes will be driven by fulfilling needs of specific applications. Right now, it does not look like that changes in the Volume rendering module will be required, because we want to offer very high flexibility for module developers to customize the volume rendering experience, which a C++ module is less suitable for. Trying to address all volume visualization needs by improving a Volume rendering module is not realistic anyway, because optimal visualization often includes preprocessing, combination with models, markups, etc. and we would not want volume rendering module to be intertwined with so many other modules.</p>
<p>As specialized volume rendering modules will be developed, time to time we will review what is common between them and if make sense then move commonly needed features into Volume rendering module. So, some Volume rendering module changes and improvements are expected, but these probably will not be very visible to users.</p>

---
