# Measuring angles on stack with defined reference plane

**Topic ID**: 21891
**Date**: 2022-02-10
**URL**: https://discourse.slicer.org/t/measuring-angles-on-stack-with-defined-reference-plane/21891

---

## Post #1 by @Igor_S (2022-02-10 12:59 UTC)

<p>Hello,<br>
a beginner’s question.<br>
How could i measure an angle on CT examination (from two lines / from a line and a point) that are defined on different slices and measured in reference plane: for instance HKA line (which is defined as an angle between femoral and tibial mehanical axis in coronal plane) but in a custom coronal/paracoronal planes.<br>
Furthermore, how could i define a custom plane by two lines (not three points)?</p>
<p>Thank you for your answers.</p>

---

## Post #2 by @mikebind (2022-02-10 16:23 UTC)

<p>There is an angle measurement tool in Slicer used by placing 3 control points.  These points can be arbitrarily placed in 3D and do not need to be placed on the same slice view.  Using two lines to define a plane is problematic because there is not any plane which contains two non-parallel and non-intersecting lines. If the two lines do intersect, then the three points defining the plane containing both lines can be the intersection point plus any one other point from each line.  If you need to identify the intersection point, then I’m not sure you’re really better off defining the plane using two intersecting lines than you are choosing the three points of the angle measurement tool.  What isn’t working well for your purposes using the angle measurement tool?</p>

---

## Post #3 by @Igor_S (2022-02-10 18:14 UTC)

<p>I know about the tool but I’m interested in an angle between two separate lines. I’ve found the script in the repository and it works, but the problem is that I don’t really know what angle it measures (I’m only interested in angle that is projected from lines to the custom specified plane).</p>
<p>I want to specify the custom plane for the projection of angles (for the HKA case plane that is paralel to line that connects center of femoral head to center of ankle and also paralel to line that connects posterior femoral condyles) and measure angle from lines that are projected on this custom plane.</p>
<p>Is this possible?</p>

---

## Post #4 by @lassoan (2022-02-10 19:09 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="2" data-topic="21891">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>There is an angle measurement tool in Slicer used by placing 3 control points.</p>
</blockquote>
</aside>
<p>There are 3 plane placement modes: <code>point normal</code>, <code>three points</code>, and <code>plane fit</code>. If you want to fit to two lines then that is basically a 4-point fit, so the <code>plane fit</code> mode should work well.</p>
<aside class="quote no-group" data-username="Igor_S" data-post="3" data-topic="21891">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/igor_s/48/14237_2.png" class="avatar"> Igor_S:</div>
<blockquote>
<p>I know about the tool but I’m interested in an angle between two separate lines. I’ve found the script in the repository and it works, but the problem is that I don’t really know what angle it measures (I’m only interested in angle that is projected from lines to the custom specified plane).</p>
</blockquote>
</aside>
<p>I would recommend to use the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#measure-angle-between-two-markup-lines">angle between lines</a> script, just <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#project-a-line-to-a-plane">project the lines to the plane</a> before you compute the angles.</p>

---

## Post #5 by @Igor_S (2022-02-10 20:26 UTC)

<p>I’m sorry I’ve been trying to evoke the <code>plane fit</code> mode for some time but without success. Where to I change the default <code>three points</code> mode to plane fit.</p>

---

## Post #6 by @mikebind (2022-02-10 20:32 UTC)

<p>In the Markups module, with the plane selected, you can change the type here:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/28fed33a5ecd646d3c8d2595724da7fe379bb592.png" data-download-href="/uploads/short-url/5QF3Fas7P8Tk3lqnVxlqEKXJxqW.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/28fed33a5ecd646d3c8d2595724da7fe379bb592_2_271x500.png" alt="image" data-base62-sha1="5QF3Fas7P8Tk3lqnVxlqEKXJxqW" width="271" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/28fed33a5ecd646d3c8d2595724da7fe379bb592_2_271x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/28fed33a5ecd646d3c8d2595724da7fe379bb592_2_406x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/28fed33a5ecd646d3c8d2595724da7fe379bb592.png 2x" data-dominant-color="EFF0F2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">511×940 110 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #7 by @lassoan (2022-02-10 20:33 UTC)

<p>Plane fit is available in recent Slicer Preview Releases, probably not in the current Slicer Stable Release.</p>

---

## Post #8 by @Igor_S (2022-02-12 16:00 UTC)

<p>It works with Preview version!</p>
<p>Thank you.</p>

---

## Post #9 by @esomjai (2023-04-27 11:38 UTC)

<p>Hi there,<br>
I came across this thread when looking for a solution to measure angles between a reference plane and axis (established line between landmarks). I tried the angle measurement tool and the recommended line-line intersection, but I get different results. I am concerned as to the directionality of the angle measurements in each process.<br>
Please see reference pictures.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d29bf273370b474fb49522c8f3c4a3093b6e2010.jpeg" data-download-href="/uploads/short-url/u38nNwGl2rAdKu9BpwJwp6BqGL6.jpeg?dl=1" title="angle measurement tool.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d29bf273370b474fb49522c8f3c4a3093b6e2010.jpeg" alt="angle measurement tool.PNG" data-base62-sha1="u38nNwGl2rAdKu9BpwJwp6BqGL6" width="630" height="499" data-dominant-color="BEACB1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">angle measurement tool.PNG</span><span class="informations">781×619 67.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/74acade562673550b049a0d54c7913b97b2b76e5.jpeg" data-download-href="/uploads/short-url/gE9lIgHPOrbpsP96vM0VT47jrg1.jpeg?dl=1" title="with line projection.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/74acade562673550b049a0d54c7913b97b2b76e5.jpeg" alt="with line projection.PNG" data-base62-sha1="gE9lIgHPOrbpsP96vM0VT47jrg1" width="518" height="500" data-dominant-color="C4B4B6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">with line projection.PNG</span><span class="informations">729×703 55.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thank you for your time and assistance.</p>

---

## Post #10 by @lassoan (2023-05-02 19:28 UTC)

<p>Angle between a plane and a line is always &lt;90deg. In your screenshot you marked an angle &gt;90deg. You need some extra reference direction, point, or plane that specifies the plane for your angle measurement.</p>

---
