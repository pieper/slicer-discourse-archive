# Seed grow script , argument size limit

**Topic ID**: 9250
**Date**: 2019-11-21
**URL**: https://discourse.slicer.org/t/seed-grow-script-argument-size-limit/9250

---

## Post #1 by @prorai (2019-11-21 14:22 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a><br>
Today i was using the seedgrow script , when i’m passing the seeds values , around 100+ seeds XYZ value.<br>
app just got crashed without any log info.<br>
before i’ve tried with around 80 seeds XYZ values, and it works all good for me.</p>

---

## Post #2 by @lassoan (2019-11-21 14:27 UTC)

<aside class="quote no-group" data-username="prorai" data-post="1" data-topic="9250">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/e8c25b/48.png" class="avatar"> prorai:</div>
<blockquote>
<p>Today i was using the seedgrow script</p>
</blockquote>
</aside>
<p>Which seedgrow script are you referring to?</p>

---

## Post #3 by @prorai (2019-11-21 14:29 UTC)

<p>I’m using the same script which have in your example database , and i’m passing seeds as parameters to it.</p>

---

## Post #4 by @lassoan (2019-11-21 14:50 UTC)

<p>Could you post the link here?</p>

---

## Post #5 by @prorai (2019-11-22 06:52 UTC)

<aside class="onebox githubgist">
  <header class="source">
      <a href="https://gist.github.com/lassoan/2d5a5b73645f65a5eb6f8d5f97abf31b" target="_blank" rel="nofollow noopener">gist.github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://gist.github.com/lassoan/2d5a5b73645f65a5eb6f8d5f97abf31b" target="_blank" rel="nofollow noopener">https://gist.github.com/lassoan/2d5a5b73645f65a5eb6f8d5f97abf31b</a></h4>
<h5>SegmentGrowCutSimple.py</h5>
<pre><code class="Python"># Generate input data
################################################

import SampleData

# Load master volume
sampleDataLogic = SampleData.SampleDataLogic()
masterVolumeNode = sampleDataLogic.downloadMRBrainTumor1()

# Create segmentation</code></pre>
This file has been truncated. <a href="https://gist.github.com/lassoan/2d5a5b73645f65a5eb6f8d5f97abf31b" target="_blank" rel="nofollow noopener">show original</a>

<p>
</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #6 by @lassoan (2019-11-22 14:27 UTC)

<p>There is nothing specific in the script that would prevent you from using many seeds, but the approach used in the example is certainly not optimal for 100+ seeds.</p>
<p>If spheres overlap then the behavior is somewhat unpredictable (regions that are in intersection of even number of spheres will be excluded).</p>
<p>If you have so many spheres then it also means that probably they are small, so creating sphere models for them is very inefficient.</p>
<p>Instead, you probably want to just set voxel values directly in the binary labelmap representation. You can compute voxel coordinates of binary labelmap representation in Segmentation nodes similarly to how voxel coordinates are computed for volume nodes in <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_volume_voxel_coordinates_from_markup_fiducial_RAS_coordinates">this example</a>.</p>

---

## Post #7 by @prorai (2019-11-22 15:04 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="9250">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Instead, you probably want to just set voxel values directly in the binary labelmap representation. You can compute voxel coordinates of binary labelmap representation in Segmentation nodes similarly to how voxel coordinates are computed for volume nodes</p>
</blockquote>
</aside>
<p>can i create a segment\3D model using this?</p>

---

## Post #8 by @lassoan (2019-11-22 15:06 UTC)

<p>Yes, that would work the same way.</p>

---
