# Layered rendering with multiple renderers

**Topic ID**: 14630
**Date**: 2020-11-16
**URL**: https://discourse.slicer.org/t/layered-rendering-with-multiple-renderers/14630

---

## Post #1 by @fpsiddiqui91 (2020-11-16 08:29 UTC)

<p>Hello developers,</p>
<p>I am stuck in a problem that seems a bit basic but still could not solve it yet.</p>
<p>I am using multiple rendering layers to render different kinds of Fiber tracts (Red and orange) overlaid each other. As shown in the Figure below. Red fibers are rendered always on the top of the orange fibers as they are rendered on another renderer.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/896728dd676efa4c81b8589b68aeefdbc5bc46b5.png" alt="image" data-base62-sha1="jBwqMmqJ06qGsaVGrSD0ocDoadT" width="370" height="403"></p>
<p>This is what I needed and it worse really well. The problem rises when I visualize slices on the ordering window. Since the slices are rendered on the bottom layer, the red fibers are always rendered on the top and slices are not cutting those fibers. This is due to the fact that red fibers are rendered on the top.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d0de92fe9a1151a70d8294714f81e6bb5eae9284.png" alt="image" data-base62-sha1="tNKaXTzxjUbH6uhF0NHu44icLDm" width="414" height="424"></p>
<p>Now I want some suggestions on how to solve this problem? I want the slices to  cut all the fibers regardless of their rendering layers. Please note that I always want red fibers on the top of orange.</p>
<p>Are their any other method to achieve this?<br>
Thanks.</p>

---

## Post #2 by @fpsiddiqui91 (2020-11-16 17:00 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>  Can you help me with this, Thanks in advance, <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #3 by @lassoan (2020-11-16 17:12 UTC)

<p>By using layers, you would degrade your true 3D rendering to something like 2.5D rendering. If you want to make the red tracts always appear in front of orange then you can simply display red tracts using 1% larger diameter tubes than orange tubes.</p>

---

## Post #4 by @fpsiddiqui91 (2020-11-16 18:21 UTC)

<p>Thanks for your response <a class="mention" href="/u/lassoan">@lassoan</a> , the red tubes are actually center tubes and they lie between yellow tubes. Since the number of yellow tubes is very large. you cannot see the red ones due to occlusion. To remedy this, I rendered red tubes in another rendering layer. This is what I needed.</p>
<p>The problem occurs when I add slices. Since slices are not able to cut red tubes as they are in another rendering layer.</p>
<p>Do you have any solution such that the red tubes rendered on the top of yellow tubes and at the same time slices should be able to cut all the tubes?</p>
<p>I hope I am clear. looking forward to your response.</p>

---

## Post #5 by @lassoan (2020-11-16 18:40 UTC)

<p>If you add a layer then it improperly occludes <em>everything</em> - not just slices but everything else that Slicer can display (models, markups, segmentations, etc.). Adding a new rendering layer solves one problem and introduces many other problems that may be much harder to resolve.</p>
<p>Instead of breaking occlusion computation, I would suggest to experiment with the followings:</p>
<ul>
<li>Make sure the red tubes are always visible by making orange tubes semi-transparent.</li>
<li>Change coincident topology offset parameters in the mapper (for example, use <code>SetRelativeCoincidentTopologyPolygonOffsetParameters</code> to push back the orange tracts)</li>
<li>Ask for more advice on the <a href="https://discourse.vtk.org/">VTK forum</a>
</li>
</ul>

---

## Post #6 by @fpsiddiqui91 (2020-11-16 18:42 UTC)

<p>Thank you so much for your suggestions <a class="mention" href="/u/lassoan">@lassoan</a> . I will try them.</p>

---

## Post #7 by @fpsiddiqui91 (2021-01-27 16:25 UTC)

<p>Hello,</p>
<p>I have been busy with solving other problems in pipeline, now I am getting back to solve this problem. I have tried SetRelativeCoincidentTopology. It somehow add other artifacts like crossing tubes, pushing back the lines when altering the Z-buffer, hence loosing the actual depth perception.</p>
<p>Are there any other ideas to solve this problem?</p>
<p>I have also asked in VTK forum, but could not get any help there.</p>
<p>Thank you and looking forward to your response.</p>

---

## Post #8 by @lassoan (2021-01-27 16:56 UTC)

<p>I see that you posted on the <a href="https://discourse.vtk.org/t/rendering-a-polyline-on-the-top-of-other-lines/5069">VTK forum</a> we can continue the discussion here after you got some suggestions there.</p>

---

## Post #9 by @fpsiddiqui91 (2021-01-27 19:47 UTC)

<p>yes sure, I am waiting for the suggestions… but unfortunately no one replied yet. Do you have any suggestion <a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #10 by @lassoan (2021-01-27 21:10 UTC)

<p>People on the VTK forum are not that responsive. You can ask on the same topic every 3-4 days for 1-2 weeks, each time describing what you have tried in the meantime and how it worked. If you keep your posts short and clear, add nice illustrative images, and make it clear that you are making an effort then the chances that you get help are much higher.</p>
<p>If you want guaranteed response time then probably you need to ask for a paid consultation, for example you can use Kitware’s webshop to buy VTK expert’s time to help you.</p>
<p>I think your requirements are self-contradicting (you cannot have correct 3D composition but at the same time some structures “always on top”), that’s why it is very hard to solve it. There are several straightforward solutions if you redefine your requirements, for example if you just want to make sure that red fibers are always distinguishable then you can achieve that by changing color, radius, transparency; you can use multiple tube filters and you can also parameters by specifying point scalar arrays in the vtkTubeFilter input.</p>

---

## Post #11 by @fpsiddiqui91 (2021-01-27 21:18 UTC)

<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a> or your suggestion. Yes, my problem is indeed a bit contradicting. I do need my red tubes to be on the top and at the same time, I want the planes to cut the tubes. Changing the tube parameters (color.radius, transparency) won’t solve the problem, as it gets occluded by the orange poly lines.</p>
<p>Are there any other filters which I can use to render red tube and make it visible even if its occluded by orange polylines?</p>
<p>Thank you.</p>

---
