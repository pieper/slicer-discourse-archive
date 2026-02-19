---
topic_id: 15380
title: "Display Normal While Placing Fiducial"
date: 2021-01-07
url: https://discourse.slicer.org/t/15380
---

# Display normal while placing fiducial?

**Topic ID**: 15380
**Date**: 2021-01-07
**URL**: https://discourse.slicer.org/t/display-normal-while-placing-fiducial/15380

---

## Post #1 by @hherhold (2021-01-07 01:07 UTC)

<p>Is it possible (i.e., using VTK?) to display the current surface normal while placing a fiducial? I was chatting with an anthropologist who mentioned older applications used for landmarking 3D specimens. Some of them are able to interactively display the current surface normal while moving a landmark (fiducial) point on a surface. Sounds like this is considered a pretty useful check for the proper positioning of landmarks in sutures, etc.</p>
<p>Thanks!</p>
<p>-Hollister</p>

---

## Post #2 by @lassoan (2021-01-07 01:13 UTC)

<p>You can easily implement this (probably 20-30 lines of code): add an observer to the markups node, whenever it changes, get the point coordinates, use it as input for a probe filter that samples the surface, and use the result as an input to a glyph filter. The glyph filter output can be displayed as a polydata.</p>
<p>If this turns out to be a commonly needed feature then it can be nicely implemented as a custom markups measurement plugin.</p>

---

## Post #3 by @hherhold (2021-01-07 02:03 UTC)

<p>I will take a look. I will most likely (almost certainly) have questions… Dumb first question - this is in the C++ portion of the codebase, correct?</p>
<p>Thanks!!</p>
<p>-Hollister</p>

---

## Post #4 by @lassoan (2021-01-07 02:12 UTC)

<p>Markups module is implemented in C++ but you can implement everything that I described in Python, just by connecting a few VTK filters.</p>

---

## Post #5 by @hherhold (2021-01-07 02:18 UTC)

<p>Gotcha. Thanks, Andras!</p>
<p>Hope you are well.</p>
<p>-Hollister</p>

---

## Post #6 by @muratmaga (2021-01-07 05:44 UTC)

<aside class="quote no-group" data-username="hherhold" data-post="1" data-topic="15380">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar"> hherhold:</div>
<blockquote>
<p>Sounds like this is considered a pretty useful check for the proper positioning of landmarks in sutures, etc.</p>
</blockquote>
</aside>
<p>Not entirely sure about this. While the old IDAV Landmark Editor did indeed display the normal at selected mesh vertex, this information is not used anywhere in the analysis. It was mostly a way to remedy the poor rendering and performance of the software (sometimes points will fall inside mesh due discontinuity, and with a large arrow glyph it is easier to drag and move around the point than an invisible sphere).</p>

---

## Post #7 by @hherhold (2021-01-07 11:51 UTC)

<p>Hi Murat! I hope you are well.</p>
<p>Thanks a lot for this feedback! Yeah, the person in question is a long-time user of Landmark Editor. I brought up SlicerMorph during a 1-week class on Geometric morphometrics at AMNH, and showed them a bit of SlicerMorph and your overview YouTube video - he was very interested in converting to SlicerMorph.</p>
<p>I’ll pass this info along to him - do you mind if I bring him in on this conversation?</p>
<p>Thanks!!</p>
<p>-Hollister</p>

---

## Post #8 by @muratmaga (2021-01-07 20:22 UTC)

<p>Sure, but if these are specific to SlicerMorph, perhaps better to start a new thread with that tag (if you are also seeking community input).</p>
<p>Alternatively, if they are more of a feature request specific to SlicerMorph submit them as issues on our Github repo (<a href="https://github.com/SlicerMorph/SlicerMorph" class="inline-onebox" rel="noopener nofollow ugc">GitHub - SlicerMorph/SlicerMorph: Extensions to conduct 3D morphometrics in Slicer</a>)</p>

---

## Post #9 by @lassoan (2021-01-07 20:44 UTC)

<p>It is better to keep the discussion on the forum, as markups are very actively developed, we are still making many design decisions in these weeks, so it is good if we hear about user needs (to ensure we choose design options that make it easier to implement them in the future).</p>
<p><a class="mention" href="/u/sunderlandkyl">@sunderlandkyl</a> is working on the new ROI (box, sphere, curved box) widget. For this, we will improve interaction handles, which currently only supports translation and rotation along the centerpoint, but will support additional handles (to edit ROI/slice intersection).</p>
<p><a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> is working on making the widgets customizable/extensible in extensions. It should make it easy to add a custom widget representation class in Python. Displaying an arrow at each markup point could be a custom widget representation.</p>
<p>Since we already have orientation as part of markups, displaying markups with an oriented widget should not be too hard to implement in Slice core either.</p>
<p>And there are also markups measurements, which we are improving and could be used to additional pieces of information in views.</p>
<p>So, just keep the discussion visible here on the forum and describe what you need - we are listening.</p>

---

## Post #10 by @hherhold (2021-01-07 21:12 UTC)

<p>Yep, totally agreed - he’s keen on joining in on discourse. I was mostly wondering (if Murat mentioned) if this was more a SlicerMorph issue or a generalized Slicer markups issue. Sorry if that wasn’t clear - early morning post before I’d finished my coffee.</p>
<p>Thanks!</p>
<p>-Hollister</p>

---

## Post #11 by @muratmaga (2022-06-19 18:06 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/smrolfe">@smrolfe</a> This issue, i.e. ability to see the normal vector where a control point is placed on a 3D model, came up during a slicermorph training, looks a couple of our users want to see this functionality. Can we do a prototype?</p>

---

## Post #12 by @lassoan (2022-06-21 06:05 UTC)

<p>This feature is available now for planes. Would that be sufficient?</p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/30d0fb2162b8bd09845a49de8bda0e46d17ee7f8.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/30d0fb2162b8bd09845a49de8bda0e46d17ee7f8.mp4">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/30d0fb2162b8bd09845a49de8bda0e46d17ee7f8.mp4</a>
    </source></video>
  </div><p></p>
<p>Do you know what the normals would be used for?</p>

---

## Post #13 by @muratmaga (2022-06-21 16:22 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="12" data-topic="15380">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Would that be sufficient?</p>
</blockquote>
</aside>
<p>I think it would be sufficient. Would continue to update the normal once a point is placed, if the position of the point modified? (in the plane tool it doesn’t, which makes sense).</p>
<aside class="quote no-group" data-username="lassoan" data-post="12" data-topic="15380">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Do you know what the normals would be used for?</p>
</blockquote>
</aside>
<p>I think they want to use it as a visual guide to understand how curvature is changing and help them position the curves more accurately on the models. I personally do not see the value, but it is a common request for people migrating to SlicerMorph from old IDAV Landmark Editor software.</p>

---

## Post #14 by @hherhold (2022-06-21 16:29 UTC)

<p>I believe the idea is to use the normal to see when a point sliding along the surface begins to drop into a suture between two bones. (Researcher in question is an anthropologist.)</p>

---

## Post #15 by @hherhold (2022-06-21 16:31 UTC)

<p>In thinking about this more, maybe you’d actually be better off rotating your slice views to do this and placing landmarks in the slice view. This may be more of an issue of adapting to slicer’s workflow rather than adding features? Just thinking out loud.</p>

---

## Post #16 by @muratmaga (2022-06-21 16:34 UTC)

<p>While that’s an option, it won’t work well with 3D models, only with volumes. Most people doing semilandmarking would be using a 3D model.</p>

---

## Post #17 by @hherhold (2022-06-21 16:35 UTC)

<p>Oh, yeah, I see - so they would <em>only</em> be using a model, not a model <em>and</em> the volume dataset. I basically never use only models, so didn’t realize that.</p>

---

## Post #18 by @muratmaga (2022-07-01 20:21 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> are you planning to expose this for pointlists?</p>

---

## Post #19 by @lassoan (2022-07-01 20:44 UTC)

<p>We store normal for point lists and that normal could be used for orienting the point glyphs. It would not be hard to implement this (maybe 1-2 weeks of work for an experienced Slicer developer). However, I am not aware of any plans for adding this feature.</p>

---
