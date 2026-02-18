# Intrepreting Model to model distance results

**Topic ID**: 13881
**Date**: 2020-10-06
**URL**: https://discourse.slicer.org/t/intrepreting-model-to-model-distance-results/13881

---

## Post #1 by @muratmaga (2020-10-06 04:40 UTC)

<p>I have a mouse mandible and corresponding landmarks. I cloned the landmark set, and moved only one landmark quite a bit (the pink landmark is the original, and I moved to the tip of the incisor). Then I created a warping transform using Fiducial Registration wizard. I applied this transform to a clone of the original model and hardened it. Then I used to Model to Model distance to visualize the distances. In the first pass the source model was the deformed mandible, and the target  was the original, and the distance metric set to signed_closest_point. Then I set the scalar value range, I get a meaningful (i.e., matches the transformation I applied) representation (top image). When I swap the source model to be original and the target to be the deformed model, the calculated values doesn’t look similar (bottom image). In both cases I constrained the display range of scalar values of the resultant model to be -10 to 10.</p>
<p>Why are the heat maps so different? Or when such transformation is unknown, how does one decide what is the source model and what is the target?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b6d3f39d149cdd8e0c81b44439ee958a0a0a2a6.jpeg" data-download-href="/uploads/short-url/hBSMWzHjabL4BDvYIbSHmoJyVVQ.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7b6d3f39d149cdd8e0c81b44439ee958a0a0a2a6_2_690x333.jpeg" alt="image" data-base62-sha1="hBSMWzHjabL4BDvYIbSHmoJyVVQ" width="690" height="333" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7b6d3f39d149cdd8e0c81b44439ee958a0a0a2a6_2_690x333.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7b6d3f39d149cdd8e0c81b44439ee958a0a0a2a6_2_1035x499.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b6d3f39d149cdd8e0c81b44439ee958a0a0a2a6.jpeg 2x" data-dominant-color="8EA4A9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1280×618 164 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a66435554d4958081d32cd8be89331e5a003ab8c.jpeg" data-download-href="/uploads/short-url/nJXXeMhjjCj1gfaIv7qZO7L7T3u.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a66435554d4958081d32cd8be89331e5a003ab8c_2_690x338.jpeg" alt="image" data-base62-sha1="nJXXeMhjjCj1gfaIv7qZO7L7T3u" width="690" height="338" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a66435554d4958081d32cd8be89331e5a003ab8c_2_690x338.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a66435554d4958081d32cd8be89331e5a003ab8c_2_1035x507.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a66435554d4958081d32cd8be89331e5a003ab8c_2_1380x676.jpeg 2x" data-dominant-color="92AFA1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1781×875 332 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2020-10-06 13:23 UTC)

<p>Would probably help to have a small example dataset with only a few fiducials to exactly reproduce.  The calculation should be symmetric and not care which is source and target.</p>

---

## Post #3 by @smrolfe (2020-10-06 15:45 UTC)

<p>I believe <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/ModelToModelDistance" rel="noopener nofollow ugc">Model to model distance</a> uses the <a href="https://vtk.org/doc/nightly/html/classvtkDistancePolyDataFilter.html" rel="noopener nofollow ugc">vtkDistancePolyDataFilter</a> which calculates the distance from a point x on the source to the nearest point p on the target. I wouldn’t necessarily expect it to be symmetric, unless I am missing something?</p>

---

## Post #4 by @muratmaga (2020-10-06 16:21 UTC)

<p>Here it is: <a href="https://drive.google.com/file/d/1IpgGwanPqdnOEF9hJ6Tudr-FXgCUfLbf/view?usp=sharing" rel="noopener nofollow ugc">https://drive.google.com/file/d/1IpgGwanPqdnOEF9hJ6Tudr-FXgCUfLbf/view?usp=sharing</a></p>
<p>A scene with a single model, two sets of landmarks that vary position in only the first one. I didn’t add the others not to inflate the scene size, but will only take few clicks to replicate.</p>

---

## Post #5 by @muratmaga (2020-10-06 17:56 UTC)

<p>In this particular case where two models have the exact same vertex count, using the distance metric corresponding point to point gives symmetrical results:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d719f89fc54694c32a9fe7fd6be94bdb48c47496.png" alt="image" data-base62-sha1="uGSixYcRal3iI42jDItF5VGuwnQ" width="524" height="250"></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d7e6869ffd5981b1ce76a9d06de58dffca98f05.png" alt="image" data-base62-sha1="dl5epbzLXuXW07YzDwWuqAOq32J" width="483" height="242"></p>

---

## Post #6 by @lassoan (2020-10-06 18:16 UTC)

<p>By default, model to model distance computes <code>signed_closest_point</code>. It does not rely on point correspondence, just on point to surface distance, so it should not matter if vertex count is the same or not, and operation is not commutative.</p>
<p>If you warp a model, so points in the two models correspond to each other, then it may make sense to compute point-to-point distance, using the <code>corresponding_point_to_point</code> method.</p>
<p>The implementation of these metrics is very straightforward - you can find it here: <a href="https://github.com/NIRALUser/3DMetricTools/tree/master/ModelToModelDistance">https://github.com/NIRALUser/3DMetricTools/tree/master/ModelToModelDistance</a></p>

---

## Post #7 by @Manarshhjot_Singh1 (2021-01-31 21:25 UTC)

<p>How can we warp a model to have same of points in correspondence to the base model?</p>

---

## Post #8 by @muratmaga (2021-01-31 22:35 UTC)

<p>If you clone a model, and apply the warp to the cloned one, both models should have the same number of vertices and points correspond.</p>
<p>You can easily create such warp, by cloning an existing set of landmarks, then shifting one drastically in the cloned mode, and then use the Fiducial Registration Wizard from the SlicerIGT extension.</p>

---

## Post #9 by @MirandaJO98 (2021-02-01 11:38 UTC)

<aside class="quote no-group quote-modified" data-username="muratmaga" data-post="4" data-topic="13881" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Here it is: <a href="https://drive.google.com/file/d/1IpgGwanPqdnOEF9hJ6Tudr-FXgCUfLbf/view?usp=sharing" rel="noopener nofollow ugc">https://drive.google.com/file/d/1IpgGwanPqdnOEF9hJ6Tudr-FXgCUfLbf/view?usp=sharing/</a><a href="https://www.worktime.com/employee-monitoring" rel="noopener nofollow ugc">employee monitoring software</a></p>
<p>A scene with a single model, two sets of landmarks that vary position in only the first one. I didn’t add the others not to inflate the scene size, but will only take few clicks to replicate.</p>
</blockquote>
</aside>
<p>Thank You, Muratmaga!</p>

---
