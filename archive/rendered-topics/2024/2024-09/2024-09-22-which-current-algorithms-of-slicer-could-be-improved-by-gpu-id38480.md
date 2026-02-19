---
topic_id: 38480
title: "Which Current Algorithms Of Slicer Could Be Improved By Gpu"
date: 2024-09-22
url: https://discourse.slicer.org/t/38480
---

# Which current algorithms of Slicer could be improved by GPU use?

**Topic ID**: 38480
**Date**: 2024-09-22
**URL**: https://discourse.slicer.org/t/which-current-algorithms-of-slicer-could-be-improved-by-gpu-use/38480

---

## Post #1 by @mau_igna_06 (2024-09-22 13:25 UTC)

<p>Faster 3D view rendering?<br>
Faster segment editor effects?<br>
Other things?</p>
<p>Please mention which changes would be more impactful in terms of community reach and performance<br>
Would this changes need VTK changes first and which changes would not?</p>

---

## Post #2 by @muratmaga (2024-09-22 16:25 UTC)

<p>For me definitely, better performance in large polydata models. In my subjective experience, with a powerful GPU volume rendering works well, but polydata rendering doesn’t seem to scale up that well.</p>

---

## Post #3 by @mau_igna_06 (2024-09-22 16:56 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="38480">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>polydata rendering doesn’t seem to scale up that well.</p>
</blockquote>
</aside>
<p>According to <a href="https://www.kitware.com/webgpu-occlusion-culling-in-vtk/" rel="noopener nofollow ugc">this blog</a> it may be possible to speed up PolyData rendering for 100M plus triangle scenes using VTK’s WebGPU implementation</p>

---

## Post #4 by @chir.set (2024-09-22 17:00 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="38480">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>better performance in large polydata models</p>
</blockquote>
</aside>
<p>AFAIK, only ‘Volume rendering’ invokes GPU computation in Slicer, so if polydata or segmentation objects could benefit from GPU, +1.</p>
<p>There have been much talks about AVX-512 recently on phoronix in other domains than visualisation, seeming to confirm speed gains. It’s a CPU extension, not GPU computation. I don’t know if Slicer already makes use of this, but it could be a speed improvement pathway to consider.</p>

---

## Post #5 by @muratmaga (2024-09-22 17:33 UTC)

<aside class="quote no-group" data-username="mau_igna_06" data-post="3" data-topic="38480">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>According to <a href="https://www.kitware.com/webgpu-occlusion-culling-in-vtk/" rel="noopener nofollow ugc">this blog </a> it may be possible to speed up PolyData rendering for 100M plus triangle scenes using VTK’s WebGPU implementation</p>
</blockquote>
</aside>
<p>I don’t think that’s simple drag and drop replacement, and will probably require extensive reengineering both on VTK and Slicer side. We had a grant proposal to do that, but unfortunately it wasn’t reviewed favorably.</p>

---

## Post #6 by @lassoan (2024-09-23 03:01 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="4" data-topic="38480">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>There have been much talks about AVX-512 recently on phoronix in other domains than visualisation</p>
</blockquote>
</aside>
<p>We could enable usage of latest instruction sets when building Slicer, but then we would lose compatibility with older, less capable hardware. It would be nice if someone tested Slicer built for latest CPUs and see if the performance gain is significant. My limited experience is the improvements are up to maybe 10-20% in the best case, so it is not really worth the trouble.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="38480">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>polydata rendering doesn’t seem to scale up that well</p>
</blockquote>
</aside>
<p>Polydata rendering is fully GPU accelerated. VTK uses OpenGL API to upload the polydata to the GPU and the driver renders it utilizing both CPU and GPU. You should see an enormous difference between rendering speed of large models on discrete NVIDIA GPU vs. some integrated graphics hardware. If that is not the case then there may be a bug that we should fix.</p>
<p>OpenGL API inefficiencies and complexities might also add some overhead, which might be improved in the WebGPU backend.</p>
<aside class="quote no-group" data-username="mau_igna_06" data-post="1" data-topic="38480">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>Faster 3D view rendering?<br>
Faster segment editor effects?<br>
Other things?</p>
</blockquote>
</aside>
<p>Why are you asking? What do you have in mind?</p>

---

## Post #7 by @mau_igna_06 (2024-09-23 11:05 UTC)

<p>I just was wondering if there was some low-hanging fruits for improving something using WebGPU inside Slicer</p>

---

## Post #8 by @muratmaga (2024-09-24 03:42 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="38480">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>but then we would lose compatibility with older, less capable hardware</p>
</blockquote>
</aside>
<p>I am not sure avx-512 specifically available outside of Intel CPUs. For example this is a 3rd generation EPYC server, which has been recently purchased at our institute, and it doesn’t list avx-512 extension.</p>
<p>For CPU only systems, I read openSWR is pretty complaint but wasn’t able to test: <a href="https://www.openswr.org/" rel="noopener nofollow ugc">https://www.openswr.org/</a></p>
<pre><code class="lang-auto">processor       : 127
vendor_id       : AuthenticAMD
cpu family      : 25
model           : 1
model name      : AMD EPYC 7763 64-Core Processor
stepping        : 1
microcode       : 0xa0011d3
cpu MHz         : 2445.497
cache size      : 512 KB
physical id     : 1
siblings        : 64
core id         : 63
cpu cores       : 64
apicid          : 127
initial apicid  : 127
fpu             : yes
fpu_exception   : yes
cpuid level     : 16
wp              : yes
flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf rapl pni pclmulqdq monitor ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb cat_l3 cdp_l3 invpcid_single hw_pstate ssbd mba ibrs ibpb stibp vmmcall fsgsbase bmi1 avx2 smep bmi2 invpcid cqm rdt_a rdseed adx smap clflushopt clwb sha_ni xsaveopt xsavec xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local clzero irperf xsaveerptr rdpru wbnoinvd amd_ppin arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold v_vmsave_vmload vgif v_spec_ctrl umip pku ospke vaes vpclmulqdq rdpid overflow_recov succor smca
bugs            : sysret_ss_attrs spectre_v1 spectre_v2 spec_store_bypass
bogomips        : 4866.04
TLB size        : 2560 4K pages
clflush size    : 64
cache_alignment : 64
address sizes   : 48 bits physical, 48 bits virtual
power management: ts ttp tm hwpstate cpb eff_freq_ro [13] [14]
</code></pre>

---

## Post #9 by @chir.set (2024-09-24 07:18 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="8" data-topic="38480">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I am not sure avx-512 specifically available outside of Intel CPUs.</p>
</blockquote>
</aside>
<p>avx-512 is available on recent AMD CPUs. You comment prompted me to check the previously available AMD CPUs in office, released 3 to 4 years ago: they list only avx and avx2. So it’s probably not worth investing in this direction for Slicer, not now, the more so that the benefit may be doubtful.</p>

---
