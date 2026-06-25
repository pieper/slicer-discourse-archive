---
topic_id: 47447
title: "A web-based volume path tracer"
date: 2026-06-24
url: https://discourse.slicer.org/t/47447
last_bumped: 2026-06-24T21:27:00.930Z
---

# A web-based volume path tracer

**Topic ID**: 47447
**Date**: 2026-06-24
**URL**: https://discourse.slicer.org/t/a-web-based-volume-path-tracer/47447

---

## Post #1 by @MikhailGorobets (2026-06-24 13:24 UTC)

<p>Hi everyone – I’ve been experimenting with browser-based medical volume rendering.<br>
It’s a volume path tracer that runs entirely in the browser. Under the hood it’s all C++ compiled to WebAssembly – Diligent Core’s WebGPU backend does the GPU rendering, Dear ImGui is the interface, and GDCM loads the DICOM data (experimental for now).<br>
Demo: <a href="https://grenzwert.net/wasm-modules/MedicalViewer/MedicalViewer" class="inline-onebox" rel="noopener nofollow ugc">MedicalViewer</a><br>
<strong>Chrome or Edge only</strong> – it relies on WebGPU features other browsers don’t fully support yet.</p>
<div class="d-image-grid">
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9ff17483bfd3350446df74913188903c339d425c.jpeg" data-download-href="/uploads/short-url/mOVerOG06r2mQLCSTlsP6HztQzG.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9ff17483bfd3350446df74913188903c339d425c_2_690x410.jpeg" alt="image" data-base62-sha1="mOVerOG06r2mQLCSTlsP6HztQzG" width="690" height="410" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9ff17483bfd3350446df74913188903c339d425c_2_690x410.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9ff17483bfd3350446df74913188903c339d425c_2_1035x615.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9ff17483bfd3350446df74913188903c339d425c_2_1380x820.jpeg 2x" data-dominant-color="22141A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1141 312 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/4591abc9c24ea5953f48458bdcfd0694ff2c5f34.jpeg" data-download-href="/uploads/short-url/9Vr2K3L8VDBUxyVykn96Nc4r8gc.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/4591abc9c24ea5953f48458bdcfd0694ff2c5f34_2_690x410.jpeg" alt="image" data-base62-sha1="9Vr2K3L8VDBUxyVykn96Nc4r8gc" width="690" height="410" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/4591abc9c24ea5953f48458bdcfd0694ff2c5f34_2_690x410.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/4591abc9c24ea5953f48458bdcfd0694ff2c5f34_2_1035x615.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/4591abc9c24ea5953f48458bdcfd0694ff2c5f34_2_1380x820.jpeg 2x" data-dominant-color="202224"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1141 300 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/9904c649cd2b9416d29469010b04fdd1f153b271.jpeg" data-download-href="/uploads/short-url/lPFhvFWVRFvTVd17M8XrAzZ6IFj.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/9904c649cd2b9416d29469010b04fdd1f153b271_2_613x500.jpeg" alt="image" data-base62-sha1="lPFhvFWVRFvTVd17M8XrAzZ6IFj" width="613" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/9904c649cd2b9416d29469010b04fdd1f153b271_2_613x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/9904c649cd2b9416d29469010b04fdd1f153b271_2_919x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/9904c649cd2b9416d29469010b04fdd1f153b271_2_1226x1000.jpeg 2x" data-dominant-color="300E19"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1565 475 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/82e8d576150e8cabb939c9d2705244167f7a1a24.jpeg" data-download-href="/uploads/short-url/iG4UKAlE4SMFaxXmWrB5RKkXvhy.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/82e8d576150e8cabb939c9d2705244167f7a1a24_2_356x500.jpeg" alt="image" data-base62-sha1="iG4UKAlE4SMFaxXmWrB5RKkXvhy" width="356" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/82e8d576150e8cabb939c9d2705244167f7a1a24_2_356x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/82e8d576150e8cabb939c9d2705244167f7a1a24_2_534x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/82e8d576150e8cabb939c9d2705244167f7a1a24_2_712x1000.jpeg 2x" data-dominant-color="5C243A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1232×1730 435 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</div>

---

## Post #2 by @muratmaga (2026-06-24 19:23 UTC)

<p>Nice work. Did you see <a class="mention" href="/u/pieper">@pieper</a>’s WebGPU examples: <a href="https://github.com/pieper/SlicerWGPU/tree/main" class="inline-onebox" rel="noopener nofollow ugc">GitHub - pieper/SlicerWGPU: Use wgpu, a rust-python WebGPU implementation, in 3D Slicer · GitHub</a></p>

---

## Post #3 by @MikhailGorobets (2026-06-24 21:27 UTC)

<p>Thanks! I haven’t seen those yet. On native platforms, I use the native graphics APIs through Diligent Core. In my project, WebGPU is used only for the Web version. WebGPU has quite a few drawbacks – from small but annoying limitations, like the lack of hardware trilinear filtering for fixed-point formats (R16_Unorm, etc), to more fundamental issues, such as the specification not really addressing behavior in a multithreaded environment</p>

---
