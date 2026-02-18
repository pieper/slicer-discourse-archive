# qSlicerScalarVolumeDisplayWidget updates threshold bounds automatically for float volumes

**Topic ID**: 12058
**Date**: 2020-06-16
**URL**: https://discourse.slicer.org/t/qslicerscalarvolumedisplaywidget-updates-threshold-bounds-automatically-for-float-volumes/12058

---

## Post #1 by @rat01 (2020-06-16 17:50 UTC)

<p>I have a scenario where I’m dynamically updating a scalar float volume with a modified numpy array with every update of a slider. Specifically, I’m masking various regions of the original volume with NANs. I’m using NANs rather than a specific real value for the transparency in the slice views. The reason I’m doing this thing with NANs rather than using the mask volume segment editor effect is so that the volume quickly updates without the delay of creating a new volume, and to get around the organization overhead of creating and managing new volumes for each different way I mask the volume.</p>
<p>The problem here is that updating the volume data, which changes the scalar range of the volume, also seems to update the bounds of the threshold in the qSlicerScalarVolumeDisplayWidget automatically, even with the threshold in manual mode. I don’t want the bounds of threshold slider flying around while I’m using my widget to update the volume.</p>
<p>Does anyone know of a way around this? Is there any observer I can disable to stop the threshold widget from updating with the volume data?</p>

---

## Post #2 by @lassoan (2020-06-16 18:33 UTC)

<p>It would be practically impossible to write all the code in a software application to be prepared to work with NaN values - it would extremely costly to implement, hard to maintain (all features would need to be tested with NaN values occurring in various places), and the resulting code would be slower (as you would need to implement lots of extra checks to deal with NaNs). NaN values are usually occur as a side effect of computation errors and - except very special circumstances in specific parts of an application - you should avoid using them.</p>
<p>Specifically, in 3D Slicer, behavior is undefined if you add NaN values in a volume. If you have value that contains NaN then it is your responsibility to replace them by valid values before you set it in voxels of a volume.</p>
<aside class="quote no-group" data-username="rat01" data-post="1" data-topic="12058">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rat01/48/4587_2.png" class="avatar"> rat01:</div>
<blockquote>
<p>I’m using NANs rather than a specific real value for the transparency in the slice views.</p>
</blockquote>
</aside>
<p>Instead of setting values, to NaN, set values that you would like to mask out to a value that is higher or lower then values in the normal range. You can then use threshold feature of Volumes module to make those values transparent.</p>
<aside class="quote no-group" data-username="rat01" data-post="1" data-topic="12058">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rat01/48/4587_2.png" class="avatar"> rat01:</div>
<blockquote>
<p>The problem here is that updating the volume data, which changes the scalar range of the volume, also seems to update the bounds of the threshold in the qSlicerScalarVolumeDisplayWidget automatically</p>
</blockquote>
</aside>
<p>You can disable automatic scalar range computation by calling <code>volumeDisplayNode-&gt;AutoWindowLevelOff()</code> - see example <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Change_window.2Flevel_.28brightness.2Fcontrast.29_or_colormap_of_a_volume">here</a>.</p>

---

## Post #3 by @rat01 (2020-06-16 19:17 UTC)

<p>Thank you so much for your help <a class="mention" href="/u/lassoan">@lassoan</a>. This advice should help me solve this. I’ll avoid using NaNs for purposes like this from now on.</p>

---
