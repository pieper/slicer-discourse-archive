---
topic_id: 1290
title: "Slice View Performance"
date: 2017-10-26
url: https://discourse.slicer.org/t/1290
---

# Slice view performance

**Topic ID**: 1290
**Date**: 2017-10-26
**URL**: https://discourse.slicer.org/t/slice-view-performance/1290

---

## Post #1 by @adamrankin (2017-10-26 19:00 UTC)

<p>Hello all,</p>
<p>I’m helping someone develop a Guidelet for her research, and I’m running into some very poor performance. We use SlicerIGT to connect to two Plus servers for a combined 2 images and 6 transforms. With some models and resliced views in 3D mode, we’re getting about 9 updates per second and stuttering rendering of the 3D scene.</p>
<p>So, some questions:<br>
The volume reslice driver seems like massive overkill to render a slice with a world transform (or transform chain). My performance analysis puts it at ~8% total CPU samples. Is there a less expensive way to render a slice in the 3D view with a non-identity IJKtoRAS?</p>
<p>Are their any performance optimization options for OpenIGTLink handling receiving of data. It’s a bit hard to tell as I’m  new to performance reports, but it looks like there’s a lot of redundant observed event triggers.</p>
<p>Any help is much appreciated.</p>
<p>Adam</p>

---

## Post #2 by @cpinter (2017-10-26 19:18 UTC)

<p>This is more like a troubleshooting question than a real answer but do you use two layout managers or one?<br>
If the guidelet opens in a new window instead of using Slicer’s main window then there are performance issues. That’s why the guidelet people here implemented their programs to alter Slicer’s main window instead of opening a new one (if what I heard a while back is still valid).</p>

---

## Post #3 by @adamrankin (2017-10-26 19:34 UTC)

<p>No, single layout manager. The Guidelet does not open into a new window, and is derived from the SlicerIGT Guidelet class.</p>

---

## Post #4 by @pieper (2017-10-26 19:41 UTC)

<p>Hi <a class="mention" href="/u/adamrankin">@adamrankin</a> -  If you have an easy way to replicate the issue (like a self test with dummy data) we could try various profiling and optimization options.</p>

---

## Post #5 by @adamrankin (2017-10-26 19:43 UTC)

<p>Well, sadly not easy, as it requires the connections to Plus servers to see the performance dip. I could record some sample data to replay, but it would still require running the two servers and the Guidelet.</p>

---

## Post #6 by @adamrankin (2017-10-26 20:10 UTC)

<p>Instead of using the volume reslice driver, I think I can continuously update the IJKtoRAS of the slice and let the Slicer infrastructure take care of rendering it in the right place.</p>
<p>Edit: nevermind, it doesn’t work. Only a sliver is visible.</p>

---

## Post #7 by @lassoan (2017-10-26 20:25 UTC)

<p>Do you see better performance with setting SliceToRAS matrix and the slice image? That’s interesting, because volume reslice driver does exactly that.</p>
<p>Extra modified events should not cause too much performance decrease, because data processing is performed only when the rendering pipeline requests the data, and rendering is not triggered directly modified events. Modified events usually just call scheduleRender, which eventually triggers an actual rendering update.</p>

---

## Post #8 by @lassoan (2017-10-26 20:26 UTC)

<p>I think you need to update SliceToRAS and not IJKToRAS (IJKToRAS is probably a computed transform).</p>

---

## Post #9 by @adamrankin (2017-10-26 20:31 UTC)

<p>I am seeing a lot of function calls relating to reslicing that are not just setting a matrix. A lot of data copying and interpolation. Reslicing accounts for almost 10% of samples in my performance analysis, and it should be simply copying memory to the GPU and updating the world transform.</p>
<p>I’m seeing if I can export my performance analysis for others to look at, as I am new at this and am probably reading it wrong.</p>

---

## Post #10 by @adamrankin (2017-10-26 20:36 UTC)

<p>I’m not sure yet regarding modified, but when I connect/disconnect the OpenIGTLink connector nodes via GUI, I can see an immediate performance drop/recovery for each connector connected.</p>
<p>When I connect the plus server with the US image and tracker, the update per second of a transform from the first connector goes from ~42u/s to ~9u/s.</p>

---

## Post #11 by @adamrankin (2017-10-27 14:44 UTC)

<p>I guess let me rephrase some:</p>
<p>What is the cheapest way to render a slice in the slice view (with no reslicing, just as is, ignoring all transforms, scaling to fit window) and the same slice in the 3D view with the world transform applied?</p>

---

## Post #12 by @pieper (2017-10-27 15:09 UTC)

<p>Linear transforms don’t really add any extra processing expense to slice view reslicing.  It sounds like the issue is more likely to be in the event processing so the performance analysis is critical.  You could try some experiments like selectively disabling certain features (like the 2D or 3D displays) to isolate where the time is being spent.</p>

---

## Post #13 by @adamrankin (2017-10-27 15:58 UTC)

<p>Some information:</p>
<p>Attaching a screenshot, still figuring out if I can export the report with symbols.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/836b52739e7a6549bf92871d0ecf6ccc849fe263.png" data-download-href="/uploads/short-url/iKAu4N8lCtFU2vx69VMYDpRQprB.png?dl=1" title="perf_screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/836b52739e7a6549bf92871d0ecf6ccc849fe263_2_690x373.png" alt="perf_screenshot" data-base62-sha1="iKAu4N8lCtFU2vx69VMYDpRQprB" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/836b52739e7a6549bf92871d0ecf6ccc849fe263_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/836b52739e7a6549bf92871d0ecf6ccc849fe263_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/836b52739e7a6549bf92871d0ecf6ccc849fe263_2_1380x746.png 2x" data-dominant-color="DCDFE2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">perf_screenshot</span><span class="informations">1936×1048 103 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Edit: what I’m concerned about is the ~6% of samples being used by image reslicing.</p>

---

## Post #14 by @lassoan (2017-10-27 16:58 UTC)

<p>How much refresh rate improvement do you think you would get by reducing resampling time to 0sec?</p>
<p>In general, resampling is needed because foreground, background, and labelmap volumes have to be resampled to a common grid so that they can be composited. This could be changed by creating a smarter 3D displayable manager for slices, which would not do any resampling if only layer is visible. When there are multiple visible layers, this smarter displayable manager may implement compositing in the render window instead of computing the composited image in CPU.</p>

---

## Post #15 by @adamrankin (2017-10-27 17:36 UTC)

<p>A few, but in conjunction with identifying the OpenIGTLinkIF slow performance, up to “real-time” refresh rate. Right now if I can get it up to ~15fps, that would be great.</p>

---
