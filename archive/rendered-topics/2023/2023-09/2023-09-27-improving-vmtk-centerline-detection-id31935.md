# Improving vmtk-centerline detection

**Topic ID**: 31935
**Date**: 2023-09-27
**URL**: https://discourse.slicer.org/t/improving-vmtk-centerline-detection/31935

---

## Post #1 by @b_gop (2023-09-27 14:55 UTC)

<p>I am trying to get the centerline for a very intricate tree-like structure. While the centerline computation gets most of the structure, there are still branches that it does not cover despite there being endpoints on those branches. Are there any ways I can improve the coverge?</p>
<p>I went through <a href="http://lantiga.github.com/media/AntigaPhDThesis.pdf" rel="noopener nofollow ugc">http://lantiga.github.com/media/AntigaPhDThesis.pdf</a> and I get that:</p>
<ol>
<li>Voronoi smoothing can help with increasing branching coverage</li>
<li>It may help to change the sphere radius that has been hardcoded (r= k*d)</li>
</ol>
<p>But I am not sure how I can tune these parameters through the 3DSlicer UI.</p>
<p>Would anyone have any suggestions?</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2023-09-28 03:18 UTC)

<p>Do you use network extraction or centerline extraction?</p>
<p>If you use centerline extraction, you may need to move the automatically detected endpoints a bit closer (further up towards the parent branch) to make sure a path can be found to it.</p>
<p>You can enable “Developer mode” in application settings and then click on the “Edit” button in the “Extract Centerline” module GUI and then you can edit all the parameters.</p>
<p>Voronoi smoothing is not available since VTK-9.2 introduced some backward-incompatible changes, but it should not matter, as it generally just barely improved connectivity if at all.</p>

---

## Post #3 by @b_gop (2023-09-28 15:29 UTC)

<p>I use centerline extraction.</p>
<p>Okay, right.</p>
<p>As I am working on a big volume, it might not be possible to move all of the points manually. Can you suggest any methods to train a network to predict the endpoints better?</p>
<p>Thank you for your help!</p>

---

## Post #4 by @lassoan (2023-09-28 15:35 UTC)

<p>It should be possible to slightly adjust the automatic endpoint detection function to snap to the closest Voronoi surface point that has sufficiently large associated radius. For the implementation you can use VTK threshold filter to remove points of the Voronoi surface that has small associated radius, then use a locator to find closest point on this reduced surface. It would probably not take more than 15-20 lines of Python code in total. The <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html">script repository</a> and Bing Chat or ChatGPT should be able to give you all the code snippets you need but if you get stuck then you can ask us here.</p>

---

## Post #5 by @b_gop (2023-10-02 11:53 UTC)

<p>Thank you for your response!</p>
<p>A couple of questions:</p>
<ol>
<li>
<p>Wouldn’t removing points with small associated radius also remove connections of thin branch points?</p>
</li>
<li>
<p>Should these new points be used along with the automatic detection?</p>
</li>
<li>
<p>Do I simply use these new points for centerline detection or do is there any other intermediate step? I tried using just the new endpoints for the detection and also the new points combined with the automatically detected points. Each time there was barely a centerline formed and I received this error message on the console:</p>
</li>
</ol>
<p>[VTK] vtkvmtkSteepestDescentLineTracer (0000017EAB6FA3B0): Can’t find a steepest descent edge. Target not reached.<br>
[VTK] Warning: In vtkvmtkSteepestDescentLineTracer.cxx, line 240<br>
[VTK] vtkvmtkSteepestDescentLineTracer (0000017EAB6FA3B0): Degenerate descent detected. Target not reached.<br>
[VTK] Warning: In vtkvmtkSteepestDescentLineTracer.cxx, line 240</p>

---

## Post #6 by @lassoan (2023-10-02 13:49 UTC)

<aside class="quote no-group" data-username="b_gop" data-post="5" data-topic="31935">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/b_gop/48/67116_2.png" class="avatar"> b_gop:</div>
<blockquote>
<p>Wouldn’t removing points with small associated radius also remove connections of thin branch points?</p>
</blockquote>
</aside>
<p>It would not remove any connections, it would only make the centerline shorter by a fraction of a millimeter.</p>
<aside class="quote no-group" data-username="b_gop" data-post="5" data-topic="31935">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/b_gop/48/67116_2.png" class="avatar"> b_gop:</div>
<blockquote>
<p>Should these new points be used along with the automatic detection?</p>
</blockquote>
</aside>
<p>You would add this as a preprocessing step in centerline extraction: you would not use the raw input that the user provides (that may come from manual specification or automatic endpoint detection) but first you would snap the points to the Voronoi diagram.</p>
<aside class="quote no-group" data-username="b_gop" data-post="5" data-topic="31935">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/b_gop/48/67116_2.png" class="avatar"> b_gop:</div>
<blockquote>
<p>I tried using just the new endpoints for the detection and also the new points combined with the automatically detected points. Each time there was barely a centerline formed</p>
</blockquote>
</aside>
<p>There might be a bug in the implementation. Could you please send a link to your github repository/branch where you added this?</p>

---

## Post #7 by @b_gop (2023-10-03 11:44 UTC)

<p>You can find the implementation here: <a href="https://github.com/bhavika-g/vmtk.git" class="inline-onebox" rel="noopener nofollow ugc">GitHub - bhavika-g/vmtk</a></p>
<p>I misunderstood your suggestion earlier so I have made edits now, but the application/code seems to freeze for a very long time (24+ hours) at the “markupsNode.AddControlPoint(point[0], point[1], point[2])” line.</p>

---
