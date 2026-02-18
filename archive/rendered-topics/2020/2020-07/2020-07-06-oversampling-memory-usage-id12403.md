# Oversampling memory usage

**Topic ID**: 12403
**Date**: 2020-07-06
**URL**: https://discourse.slicer.org/t/oversampling-memory-usage/12403

---

## Post #1 by @muratmaga (2020-07-06 20:34 UTC)

<p>This is a best-practice sort of a question.</p>
<p>We have to deal with segmenting thin bones in large volumes (e.g., 1024^3 or even larger) quite often. The typical suggestion on the forum has been to oversample the segmentation (eg., <a href="https://discourse.slicer.org/t/segmenting-narrow-bone-structures/9319" class="inline-onebox">Segmenting narrow bone structures</a>).</p>
<p>I am doing some tests on how to do this effectively, and the pattern emerging to me is that it is actually more memory effective to oversample the master volume prior to segmentation. Here is what I did:</p>
<p>I loaded MRHEAD.nrrd and used the cropvolume with isotropic voxel setting and 0.25 scaling. I fed the resultant cropped volume to segmentation, and did a threshold range of 97-max. Reported memory usage for this flow was 4800MB on windows.</p>
<p>In a new session, I loaded MRhead, and processed directly with threshold. Then I edited the segmentation geometry such that oversampling was 4, and isotropic voxel is selected. This took 2-3 times longer to process resampling, and in the end reported memory usage on windows was 20264MB.</p>
<p>I am a bit surprised with the result, as I thought the latter would be more memory efficient way of doing things… This is on windows, with 4.11.0-2020-06-16 r29150 / ce703c1</p>

---

## Post #2 by @lassoan (2020-07-06 20:49 UTC)

<p>This is expected, as memory usage is a combination of extents and resolution. When you use Crop volume module, you usually crop volume (reduce the extent) and change resolution. However, if you oversample the volume then you normally keep the original extent, so if you double the resolution along each axis then you end up using 8x more memory.</p>
<p>The key is to always reduce the extent when you increase resolution (reduce spacing) to keep the total number of voxels as low as possible.</p>
<p>If you work with very thin structures then you may consider surface editing. Dynamic modeler is a step towards that, as it allows you to extract and process thin surfaces. At some point, we’ll add a “Model editor” module that will operate on models (open surfaces, shells), similarly how “Segment editor” module operates now on closed surfaces (volumes).</p>

---

## Post #3 by @muratmaga (2020-07-06 20:54 UTC)

<p>In my tests, I did use the full extent of the volume for CropVolume oversampling (fit to volume option).</p>
<p>In the end these two approaches should result in similar memory footprints (since there is no change in the extends), but it appears segmentation geometry oversampling results in 4 times as large memory usage.</p>

---

## Post #4 by @hherhold (2020-07-06 21:17 UTC)

<p>One thing I experimented with a while back was basically disabling undo in Segment Editor. I don’t remember what kind of a savings I got in memory usage but it helped a bit (machine I was using was maxed out at 16GB).</p>

---

## Post #5 by @pieper (2020-07-06 22:29 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> how are you measuring memory usage?  If you used reciprocal factors in cropping and oversampling the resulting segmentation size would be the same and the only memory difference should be the extra large MRHead volume in memory at the same time.</p>
<p>The argument for resampling the reference volume would be that you can use a different filter (e.g. windowed sinc) which might give better, or at least different, results.  I think the Segment Editor uses linear interpolation for effects like thresholding.</p>

---

## Post #6 by @muratmaga (2020-07-06 22:58 UTC)

<p>I am looking at the Slicer memory usage reported by the windows task manager after the tasks are completed.</p>

---

## Post #7 by @muratmaga (2020-07-06 23:18 UTC)

<aside class="quote no-group" data-username="hherhold" data-post="4" data-topic="12403">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar"> hherhold:</div>
<blockquote>
<p>disabling undo in Segment Editor.</p>
</blockquote>
</aside>
<p>Where do you do that?</p>

---

## Post #8 by @muratmaga (2020-07-06 23:28 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="12403">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>This is expected, as memory usage is a combination of extents and resolution. When you use Crop volume module, you usually crop volume (reduce the extent) and change resolution. However, if you oversample the volume then you normally keep the original extent, so if you double the resolution along each axis then you end up using 8x more memory.</p>
</blockquote>
</aside>
<p>There is something weird going on here: This is my settings preview for oversampling:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8b2248dbabd965c7fe8d715b672785f13a815d09.png" alt="image" data-base62-sha1="jQPP0TrbhlbP8kFmkefn0g0DJ0d" width="657" height="403"><br>
This is the resultant geometry after oversampling is completed:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/323309f69503ea07e0247efbfdd7ce213c92a57e.png" alt="image" data-base62-sha1="7a5dSG219EjvtpMhOQKvrK3Oclo" width="651" height="402"></p>
<p>That would explain the increased memory usage and longer computation because the resultant spacing is not a factor of 4 but 16.<br>
This is with the latest preview on Linux.</p>

---

## Post #9 by @hherhold (2020-07-06 23:39 UTC)

<p>It’s been a little while, but I think my first pass was to comment out</p>
<pre><code>self.scriptedEffect.saveStateForUndo()
</code></pre>
<p>in various places in segment editor effects. I favored commenting it out where called rather than making the function do nothing as I wasn’t sure what other effects that might have. I also changed</p>
<pre><code>self.editor.setMaximumNumberOfUndoStates(10)
</code></pre>
<p>in SegmentEditor.py to zero as a later attempt. There wasn’t one overall location in the code that worked for everything. My goals were to reduce memory usage and speed up operations, particularly with island effects like remove small islands - saving the state was pretty expensive with tens of thousands of islands.</p>

---

## Post #10 by @lassoan (2020-07-06 23:40 UTC)

<p>This looks correct, oversampling factor of 4x means 64x more memory usage.</p>

---

## Post #11 by @muratmaga (2020-07-06 23:58 UTC)

<p>I don’t think it is correct. Or at least it is not resampling to the geometry that it is telling it will. Please look at the screenshots.<br>
Segmentation label geometry in the first shot is what it is supposed to be be (this is the 256x256x130 MRHead volume). So oversampling of factor of 4 gives those approximate dimension (although I am not sure why  it is no exactly 1024x1024x520). The second screenshot is after the resampling is completed and as you can see the oversampling factor set to 1.00.</p>
<p>You may want to give it a try and see for yourself.</p>

---

## Post #12 by @lassoan (2020-07-07 00:18 UTC)

<p>I see what you mean now. Yes, oversampling is applied twice (once to the whole segmentation geometry and then again for each segment). I’ve added a ticket for this: <a href="https://github.com/Slicer/Slicer/issues/5032">https://github.com/Slicer/Slicer/issues/5032</a></p>

---
