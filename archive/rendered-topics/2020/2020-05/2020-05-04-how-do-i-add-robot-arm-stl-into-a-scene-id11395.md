# How do I add robot arm STL into a scene?

**Topic ID**: 11395
**Date**: 2020-05-04
**URL**: https://discourse.slicer.org/t/how-do-i-add-robot-arm-stl-into-a-scene/11395

---

## Post #1 by @CHRIS_HUYNH (2020-05-04 08:58 UTC)

<p>Hi,</p>
<p>I’ve just created a scene for a phantom spine I’m working with seen below.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a71915e22ed174005fa48887ea13b5d435ff1d00.png" data-download-href="/uploads/short-url/nQdtWvHZ6rrYJQoRv01xhi0ZIju.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a71915e22ed174005fa48887ea13b5d435ff1d00_2_690x460.png" alt="image" data-base62-sha1="nQdtWvHZ6rrYJQoRv01xhi0ZIju" width="690" height="460" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a71915e22ed174005fa48887ea13b5d435ff1d00_2_690x460.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a71915e22ed174005fa48887ea13b5d435ff1d00_2_1035x690.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a71915e22ed174005fa48887ea13b5d435ff1d00_2_1380x920.png 2x" data-dominant-color="A2A1BC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">3000×2000 795 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I want to now add an ABB IRB 120 robotic arm into the scene with all its links connected in correct order similar to Junichi Tokuda’s example seen below<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/caf596d922b4df6b6ace76fdedd44b9e69240776.png" data-download-href="/uploads/short-url/sXsCxkpWF1ObxY6nY6AwpRr6ch8.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/caf596d922b4df6b6ace76fdedd44b9e69240776_2_500x500.png" alt="image" data-base62-sha1="sXsCxkpWF1ObxY6nY6AwpRr6ch8" width="500" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/caf596d922b4df6b6ace76fdedd44b9e69240776_2_500x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/caf596d922b4df6b6ace76fdedd44b9e69240776.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/caf596d922b4df6b6ace76fdedd44b9e69240776.png 2x" data-dominant-color="8F85D1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">618×617 76.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I have the stl files for the abb irb 120 robotic arm, but when I drag &amp; drop an arm link.stl file into the 3D Slicer space, it doesn’t load or show up in the 3D viewer, but shows up in the Models tab. How do I fix this issue and import each arm link stl file into 3D slicer such that they are joined together in order?</p>

---

## Post #2 by @joachim (2020-05-04 10:34 UTC)

<p>Maybe they are placed too far away or use different coordinate systems so you don’t see both? You can try to center the 3D scene using the <em>Center the 3D view on the scene</em>-button.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/551439ba9fdc23736afdcbaf2002743a3eccf321.png" alt="Center3DScene" data-base62-sha1="c8DUUwwOrQLq2gOLaKDCWWxZLJn" width="453" height="191"></p>

---

## Post #3 by @lassoan (2020-05-04 18:41 UTC)

<p>Also make sure the STL uses mm as coordinate system units (or scale it using a transforms module).</p>
<p>Note that you can also animate the robot (simulate rotation around each joint) if you load each section of the robot as a separate model, with the rotation joint in the origin. You just need to create a hierarchy of transforms in Transforms module and add each model at the appropriate level in the transform tree.</p>
<p>I’ve uploaded a short video of ABB IRB 120 robot visualization in Slicer:</p>
<div class="lazyYT" data-youtube-id="yS3SKqNztJU" data-youtube-title="Medical robot visualization using 3D Slicer" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque">
  <a href="https://www.youtube.com/watch?v=yS3SKqNztJU" target="_blank" rel="nofollow ugc noopener">
    <img src="https://img.youtube.com/vi/yS3SKqNztJU/hqdefault.jpg" width="480" height="270" title="Medical robot visualization using 3D Slicer">
  </a>
</div>

<p>You can download the Slicer scene from <a href="https://1drv.ms/u/s!Arm_AFxB9yqHu5J0yW1ck3H1-A_Xxg?e=QfbPPd">here</a>.</p>

---

## Post #4 by @CHRIS_HUYNH (2020-05-05 07:58 UTC)

<p>Hi Mr Lasso,</p>
<p>I’ve done what you recommended and it works. Also thank you for the upload of the irb120.mrml file. I do however want to try it out for myself to develop a better understanding of the transforms, how to set up my robotic arm and how to fix any issues that I encounter.</p>
<p>The model of each link of the IRB 120 robotic arm has imported into 3D slicer, but the joints are not connected. Is there a tutorial or guide that illustrates how to get these joints connected and how to have the transforms set up properly in a hierachy of transforms for each joint?</p>

---
