# Scalar range not updating for live stream volume

**Topic ID**: 16122
**Date**: 2021-02-21
**URL**: https://discourse.slicer.org/t/scalar-range-not-updating-for-live-stream-volume/16122

---

## Post #1 by @jamesobutler (2021-02-21 18:53 UTC)

<p>I am live streaming a volume over OpenIGTLink into Slicer (latest preview) using the SlicerOpenIGTLink (latest) extension. I’m noticing that the scalar range for the volume node is not updating for new image data. The below image is what the volumes module displays after the first frame is received.  Then when the second frame is received it does not update. Maybe this is an issue with code in the SlicerOpenIGTLink extension? This is a very very low frame rate live stream from a camera device. For example it would be a 5 second exposure and then a 10 second exposure capture where the scalar max for the second would be approximately double the first.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e30357374c9f101649c0eb681e35e59a79e9d68.png" alt="image" data-base62-sha1="b9GwPCpf5YejCA01UCyzg7GQUNa" width="512" height="384"></p>
<p><strong>My Current Workaround:</strong><br>
I can force update it with a hacky workaround by doing:</p>
<pre data-code-wrap="python"><code class="lang-python">volume_array = slicer.util.arrayFromVolume(live_stream_node)
slicer.util.updateVolumeFromArray(live_stream_node, volume_array)
</code></pre>
<p>After update:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b2aa9a57aa975ae5a018f89271cf0b46aa7649a1.png" alt="image" data-base62-sha1="puyvikj8I7ZvdgPytw2jNZNJbYB" width="447" height="419"></p>
<p>cc: <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a></p>

---

## Post #2 by @lassoan (2021-02-21 22:51 UTC)

<p>Updating the scalar range is an expensive operation, so it should be only performed when the Volume Information section is visible (volumes module is active and information section is not collapsed). But if it is visible then it should be updated.</p>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> could you have a look? VTK caches scalar range, so maybe a <code>Modified()</code> call is missed at some level, and that’s why VTK does not recompute the value it but returns the last one.</p>

---

## Post #3 by @jamesobutler (2021-02-21 23:03 UTC)

<p>What I’m looking to do is set the Lower threshold based on some percentage of the current max scalar value in the image. So even if the Volumes modules was not visible I would want to do something like the following.</p>
<pre><code class="lang-python">_, max_value = live_stream_node.GetImageData().GetScalarRange()
min_value = max_value * 0.04
live_stream_node.GetDisplayNode().SetThreshold(min_value, max_value)
</code></pre>
<p>However this is not working as GetScalarRange is still returning the range of the image data from the first frame instead of the image data of the current frame. The threshold range is limited to the scalar range, so when I attempt to set the upper threshold for the second frame which is higher than the first frame, the max threshold gets rejected as the value is outside the range.</p>

---

## Post #4 by @lassoan (2021-02-21 23:10 UTC)

<p>This confirms that the issue is that the scalar array is not marked as modified.</p>

---

## Post #5 by @jamesobutler (2021-02-22 00:13 UTC)

<p>Some additional information from debugging:<br>
What also seems to update the scalar range is if the image dimensions change. So if my 1024x1024 live stream image becomes a 512x512 image it will force the scalar range to be updated.</p>

---

## Post #6 by @Sunderlandkyl (2021-02-23 21:12 UTC)

<p>This commit in OpenIGTLinkIO should cause the scalar range to update: <a href="https://github.com/IGSIO/OpenIGTLinkIO/commit/32feaaa5fcff433dec4f071cf7aaa9106e5e5124" class="inline-onebox" rel="noopener nofollow ugc">ENH: Mark received image data scalars as modified · IGSIO/OpenIGTLinkIO@32feaaa · GitHub</a></p>

---
