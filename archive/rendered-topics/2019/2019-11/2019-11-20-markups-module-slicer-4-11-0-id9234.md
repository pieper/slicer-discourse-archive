---
topic_id: 9234
title: "Markups Module Slicer 4 11 0"
date: 2019-11-20
url: https://discourse.slicer.org/t/9234
---

# Markups Module Slicer 4.11.0

**Topic ID**: 9234
**Date**: 2019-11-20
**URL**: https://discourse.slicer.org/t/markups-module-slicer-4-11-0/9234

---

## Post #1 by @rprueckl (2019-11-20 17:42 UTC)

<p>Hi,</p>
<p>currently, I don’t know really where to report bugs or feature requests, so I’m doing it here:<br>
Slicer 4.11.0-2019-11-19:</p>
<p><strong>1:</strong><br>
In the markups module, when I create a MarkupsLine, a 2D projection is always visible in one slice view, even when projection is turned off:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d23898b62d6f3c3542c16b1a3219b45101746055.png" data-download-href="/uploads/short-url/tZHwD64iRplwDGsS0bPBFcmWUrr.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d23898b62d6f3c3542c16b1a3219b45101746055_2_459x500.png" alt="image" data-base62-sha1="tZHwD64iRplwDGsS0bPBFcmWUrr" width="459" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d23898b62d6f3c3542c16b1a3219b45101746055_2_459x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d23898b62d6f3c3542c16b1a3219b45101746055_2_688x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d23898b62d6f3c3542c16b1a3219b45101746055_2_918x1000.png 2x" data-dominant-color="3F3F46"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1066×1161 80.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><strong>2:</strong><br>
When I disable the visibility of both control points of a MarkupsLine, the line should ideally stay visible in the 3d view, as it does in the slice view. Currently, it disappears from the 3d view:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/424d6864c57ad37a1f655b524329cf4108b146fe.png" data-download-href="/uploads/short-url/9sxmdXoiussypIE3FpXp9aRlxOS.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/424d6864c57ad37a1f655b524329cf4108b146fe_2_459x500.png" alt="image" data-base62-sha1="9sxmdXoiussypIE3FpXp9aRlxOS" width="459" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/424d6864c57ad37a1f655b524329cf4108b146fe_2_459x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/424d6864c57ad37a1f655b524329cf4108b146fe_2_688x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/424d6864c57ad37a1f655b524329cf4108b146fe_2_918x1000.png 2x" data-dominant-color="3F3F46"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1066×1161 81 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><strong>3:</strong><br>
Ideally, the Glyph sizes for the control points and the lines in between (this applies for MarkupsLine, MarkupsAngle, MarkupsCurve, MarkupsClosedCurve) could be adjusted independently.</p>
<p>BTW: I find the new Markups Module very well designed!</p>

---

## Post #2 by @lassoan (2019-11-20 18:23 UTC)

<aside class="quote no-group" data-username="rprueckl" data-post="1" data-topic="9234">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rprueckl/48/4240_2.png" class="avatar"> rprueckl:</div>
<blockquote>
<p>In the markups module, when I create a MarkupsLine, a 2D projection is always visible in one slice view, even when projection is turned off:</p>
</blockquote>
</aside>
<p>Most likely it is not a projection but the line actually crosses that slice.</p>
<aside class="quote no-group" data-username="rprueckl" data-post="1" data-topic="9234">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rprueckl/48/4240_2.png" class="avatar"> rprueckl:</div>
<blockquote>
<p>When I disable the visibility of both control points of a MarkupsLine, the line should ideally stay visible in the 3d view, as it does in the slice view.</p>
</blockquote>
</aside>
<p>I agree, line visibility should be adjustable independently from point visibility.</p>
<aside class="quote no-group" data-username="rprueckl" data-post="1" data-topic="9234">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rprueckl/48/4240_2.png" class="avatar"> rprueckl:</div>
<blockquote>
<p>Glyph sizes for the control points and the lines in between (this applies for MarkupsLine, MarkupsAngle, MarkupsCurve, MarkupsClosedCurve) could be adjusted independently</p>
</blockquote>
</aside>
<p>I agree, this would be nice to have.</p>
<aside class="quote no-group" data-username="rprueckl" data-post="1" data-topic="9234">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rprueckl/48/4240_2.png" class="avatar"> rprueckl:</div>
<blockquote>
<p>currently, I don’t know really where to report bugs or feature requests</p>
</blockquote>
</aside>
<p>We are in the process of transitioning Slicer fully to github. Once that’s done (hopefully within days), we can start using GitHub’s issue tracker. Until then I use this <a href="https://1drv.ms/x/s!Arm_AFxB9yqHuOwEoD572qECck1T5w?e=MUBhgh">spreadsheet</a> to track markups module developments.</p>
<p>Right now, as far as I know, all Slicer core developers have other priorities, so if you can implement any of the fixes or enhancements and send pull requests that would be great help.</p>

---

## Post #3 by @rprueckl (2019-11-21 09:27 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="9234">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Most likely it is not a projection but the line actually crosses that slice.</p>
</blockquote>
</aside>
<p>The only difference when “2D Projection” is activated is, that the control points are shown throughout the slices. There is no difference for the display of the line itself. It is always shown with a fade and (as far as I have seen) there is no way to disable this. It would be really cool to have more control:</p>
<ul>
<li>fading rate (in number of slices (1-inf))</li>
<li>e.g. dashed line display</li>
<li>display the intersection point of the line with the current slice (e.g. select from available glyphs)</li>
</ul>
<p>Currently, it is not really intuitive what the changes in color and transparency mean. A suggestion for clarification would be the following: Display the projected points with a small symbol indicating in which direction the point is located (in the example image L for left and R for right from the current slice, or arrows corresponding to the direction of the scrollbar of the slice view). A cross marks the intersection of the line with the current slice:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/641ff47eceb4b1681adee2e7c8385aac410cac17.png" alt="lineprojections" data-base62-sha1="ehKd2WWMQqb06HMMSGOHQqTiYgD" width="615" height="423"></p>
<p>Another suggestion would be to vary the size of the projected points with the distance to them. This would probably give you a good feeling of distance during scrolling and whether you are scrolling towards or away from a specific point.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="9234">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Right now, as far as I know, all Slicer core developers have other priorities, so if you can implement any of the fixes or enhancements and send pull requests that would be great help.</p>
</blockquote>
</aside>
<p>Currently, we are working on the first release of our software. For this, we use what is already there (4.10.2 release right now). Once we have established the initial set of functionality and released that one, we are planning to refine. In this stage, we will also make adaptations to the slicer code if necessary or helpful, which we will contribute.<br>
I just want to deposit things that pop into my eyes now, so that it is somewhere noted on a list <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #4 by @lassoan (2019-11-21 13:48 UTC)

<aside class="quote no-group" data-username="rprueckl" data-post="3" data-topic="9234">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rprueckl/48/4240_2.png" class="avatar"> rprueckl:</div>
<blockquote>
<p>The only difference when “2D Projection” is activated is, that the control points are shown throughout the slices.</p>
</blockquote>
</aside>
<p>Yes. Maybe 2D projection should be renamed to “Control point projection”. Or change the behavior to project lines to the slice the same way as points.</p>
<aside class="quote no-group" data-username="rprueckl" data-post="3" data-topic="9234">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rprueckl/48/4240_2.png" class="avatar"> rprueckl:</div>
<blockquote>
<p>Another suggestion would be to vary the size of the projected points with the distance to them.</p>
</blockquote>
</aside>
<p>Changing the size of the projected points or adding arrows are good ideas.</p>
<aside class="quote no-group" data-username="rprueckl" data-post="3" data-topic="9234">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rprueckl/48/4240_2.png" class="avatar"> rprueckl:</div>
<blockquote>
<p>A cross marks the intersection of the line with the current slice</p>
</blockquote>
</aside>
<p>I agree it would be often useful.</p>
<p>Of course it is not possible to implement all ideas (implementation, maintenance, and usability would suffer), but we can certainly selectively implement some of these.</p>
<aside class="quote no-group" data-username="rprueckl" data-post="3" data-topic="9234">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rprueckl/48/4240_2.png" class="avatar"> rprueckl:</div>
<blockquote>
<p>It would be really cool to have more control:</p>
<ul>
<li>fading rate (in number of slices (1-inf))</li>
</ul>
</blockquote>
</aside>
<p>You have full control over how color and opacity changes depending on signed distance from the slice: either using <a href="https://apidocs.slicer.org/master/classvtkMRMLMarkupsDisplayNode.html#a447cc0476faf08e18fb031a57bb361b4">SetLineColorFadingStart/End/Saturation/HueOffset…()</a> methods (to still use a linear ramp but with custom fadeout properties) or by using <a href="https://apidocs.slicer.org/master/classvtkMRMLMarkupsDisplayNode.html#a09c3ed7c1e3307f1c7090f7102b98efb">SetLineColorNodeID</a> (to use an arbitrary non-linear distance/color mapping).</p>
<aside class="quote no-group" data-username="rprueckl" data-post="3" data-topic="9234">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rprueckl/48/4240_2.png" class="avatar"> rprueckl:</div>
<blockquote>
<p>Currently, we are working on the first release of our software. For this, we use what is already there (4.10.2 release right now). Once we have established the initial set of functionality and released that one, we are planning to refine. In this stage, we will also make adaptations to the slicer code if necessary or helpful, which we will contribute.</p>
</blockquote>
</aside>
<p>Sounds good!</p>

---

## Post #5 by @rprueckl (2019-11-26 14:01 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="9234">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Of course it is not possible to implement all ideas (implementation, maintenance, and usability would suffer), but we can certainly selectively implement some of these.</p>
</blockquote>
</aside>
<p>Sure, I just want to provide input for discussions about possible features.</p>

---
