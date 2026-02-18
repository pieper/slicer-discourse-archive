# Straighten the vessel segments in a network

**Topic ID**: 13456
**Date**: 2020-09-12
**URL**: https://discourse.slicer.org/t/straighten-the-vessel-segments-in-a-network/13456

---

## Post #1 by @Deepa (2020-09-12 07:25 UTC)

<p>Hi All,</p>
<p>I have got a network of blood vessels and I’m looking for ways to straighten each segment/branch in the network. I found some discussions on straightening single segments, I’m not sure if it is possible to straighten segments in a network.</p>
<p>Any suggestions on how to do this in Slicer, if possible, will be really helpful.</p>

---

## Post #3 by @Deepa (2020-09-18 16:10 UTC)

<p>This is a kind reminder</p>

---

## Post #4 by @Deepa (2020-09-22 12:48 UTC)

<p>Hi All,</p>
<p>I would like to know if this is possible in Slicer.</p>

---

## Post #5 by @lassoan (2020-09-22 13:39 UTC)

<p>Yes, there are many ways to do this in Slicer. Since of course it is impossible to straighten an entire network (straightening one vessel segment determines how you need to warp the entire 3D space, so if you have multiple vessel segments then you would have contradicting space warping requirements), you need to tell us how you want your straightened network segments to be represented.</p>
<p>For example, <a class="mention" href="/u/pieper">@pieper</a> worked recently on placenta vascular network flattening (<a href="http://people.csail.mit.edu/abulnaga/publication/abulnaga-2019-placenta/abulnaga-2019-placenta.pdf">http://people.csail.mit.edu/abulnaga/publication/abulnaga-2019-placenta/abulnaga-2019-placenta.pdf</a>), if that’s what you are after. Or, you can straighten each vessel segment and concatenate them into an artificial tree. Or, you can design a template and register to that template using landmark points (e.g., specific vessel branching points).</p>

---

## Post #6 by @Deepa (2020-09-22 15:15 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Thanks a lot for the details.<br>
I’d like to do the following<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a6e3bec4e4525572cab1d066ac280309521503d.jpeg" data-download-href="/uploads/short-url/aCrvvD6toACTrPwSc1Q0bqqgABn.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4a6e3bec4e4525572cab1d066ac280309521503d_2_345x181.jpeg" alt="image" data-base62-sha1="aCrvvD6toACTrPwSc1Q0bqqgABn" width="345" height="181" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4a6e3bec4e4525572cab1d066ac280309521503d_2_345x181.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4a6e3bec4e4525572cab1d066ac280309521503d_2_517x271.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4a6e3bec4e4525572cab1d066ac280309521503d_2_690x362.jpeg 2x" data-dominant-color="5E6275"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1509×796 166 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The image on the left has the curves that we generate after using the extract centerline module.<br>
For instance, the Network properties table returns the lengths of the centerline path in each branch<br>
of the blood vessel. I would like to convert these curves paths to straight lines shown in the right image. i.e the length of each line segment shown in the right will be equal to the centerline length/branch length computed from the left.</p>
<p>I had a look at the reference shared above. From what I understand the optimization algorithm flattens the entire 3D volume.  But I am interested in straightening only the line segments ( i.e centerline curves displayed).</p>
<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="13456">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Or, you can straighten each vessel segment and concatenate them into an artificial tree. Or, you can design a template and register to that template using landmark points (e.g., specific vessel branching points).</p>
</blockquote>
</aside>
<p>Could you please explain a bit more on how to do this? I think I must proceed in this direction.</p>

---

## Post #7 by @Deepa (2020-09-27 16:24 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> This is a kind reminder.</p>

---

## Post #8 by @lassoan (2020-09-28 03:59 UTC)

<p>What you show in the screenshot is not the same that you describe (in the screenshot, vessel branching points are simply connected with a straight line; length of vessel segments are not preserved). If you want to preserve vessel segment lengths then it makes the problem much harder! You might find solutions in scientific papers or in software libraries but there is a good chance that you need to implement it yourself. But probably it makes more sense to apply more commonly used analysis methods.</p>

---

## Post #9 by @Deepa (2020-09-28 06:06 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a></p>
<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="13456">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>in the screenshot, vessel branching points are simply connected with a straight line; length of vessel segments are not preserved</p>
</blockquote>
</aside>
<p>Yes, I agree with your point. I was trying to find a way to preserve the lengths.</p>
<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="13456">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>. But probably it makes more sense to apply more commonly used analysis methods.</p>
</blockquote>
</aside>
<p>By this are you referring to the centerline extraction results? Could you please clarify?</p>
<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="13456">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You might find solutions in scientific papers or in software libraries but there is a good chance that you need to implement it yourself.</p>
</blockquote>
</aside>
<p>I’ve been trying to use optimization. It’s not working unfortunately for large networks</p>

---

## Post #10 by @lassoan (2020-09-28 13:32 UTC)

<aside class="quote no-group quote-modified" data-username="Deepa" data-post="9" data-topic="13456">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/deepa/48/5634_2.png" class="avatar"> Deepa:</div>
<blockquote>
<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="13456">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>. But probably it makes more sense to apply more commonly used analysis methods.</p>
</blockquote>
</aside>
<p>By this are you referring to the centerline extraction results? Could you please clarify?</p>
</blockquote>
</aside>
<p>I mean that you can research the scientific literature for papers that work on similar problems and try to use similar methods that they do.</p>

---
