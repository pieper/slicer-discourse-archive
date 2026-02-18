# Hardware: Is Apple M1 much faster as Intel CPU´s?

**Topic ID**: 21992
**Date**: 2022-02-16
**URL**: https://discourse.slicer.org/t/hardware-is-apple-m1-much-faster-as-intel-cpu-s/21992

---

## Post #1 by @norus (2022-02-16 12:52 UTC)

<p>Operating system: win 10<br>
Slicer version: 4.11.20200930<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hello,<br>
we are using 3D-slicer for Vet-OP-preparing. -very usefull software, thanks a lot to all, developing the SW.</p>
<p>This year our hardware will be renewed, and so the question poped up M1 or I7/9.</p>
<p>Tests say M1 is much faster, but can I use it with 3D-slicer?</p>
<p>Thanks a lot, stay save</p>
<p>norus</p>

---

## Post #2 by @lassoan (2022-02-18 20:34 UTC)

<p>The M1 is more power-efficient than other CPUs in its class. Also, a new M1 laptop is definitely better then a few-year old macbook.</p>
<p>However, benchmarks about absolute performance are not conclusive. As expected, Apple claims M1 is faster, <a href="https://www.pcworld.com/article/394051/intel-benchmarks-say-apples-m1-isnt-faster.html">Intel claims Intel Core i7 is faster</a>.</p>
<p>If you go for maximum raw power then you get that from a desktop system (not laptop) with a latest generation Intel Core i9 and a strong Nvidia GPU.</p>
<p>If you just want a modern, power-efficient laptop then M1 would probably work without issues. We did not do extensive testing, but got reports that Slicer works on the M1. No native Slicer release is available for ARM CPUs (so Rosetta emulation layer is used), and Slicer does not usually take advantage of multiple cores, so I would not expect any dramatic performance improvement.</p>
<p><strong>If anyone has an M1 laptop - please share your experience.</strong></p>
<p>(Just comparing your new laptop to your old laptop always result in “seems faster” experience, so for a meaningful comparison the best would be compare how Slicer works on the same data on an M1 laptop and a latest-generation Intel i7 laptop. But hearing about any experience, even if its subjective or biased could be still useful.)</p>

---

## Post #3 by @Chris_Rorden (2022-02-19 14:54 UTC)

<p>You may want to take a look at my <a href="https://github.com/neurolabusc/AppleSiliconForNeuroimaging" rel="noopener nofollow ugc">performance review for the M1 MacBooks</a>.</p>
<p>In brief, while Rosetta translated code is slower than native code, the performance of the M1 CPU running translated code will typically outperform the Intel MacBooks. In particular, programs like Slice are impacted by cache size, memory bandwidth and floating point performance - the three areas where the M1 excels.</p>
<p>Slicer uses OpenGL for rendering. For the M1 this the OpenGL driver translates OpenGL to Metal. The performance is far superior to the integrated graphics of Intel-based MacBooks, and I suspect the M1 Pro and M1 Max will outclass prior MacBook dedicated graphics.</p>
<p>A couple of rough edges for our field:</p>
<ul>
<li>Recent releases of ParaView are not supported (due to AVX instructions).</li>
<li>MRtrix OpenGL geometry shaders not supported (no Metal equivalent).</li>
<li>Several Numpy functions are not well tuned (will be fixed with the July 2022 1.23).</li>
<li>Apple requires code signing for native M1 executables, so you may need to use a lot of calls like <code>codesign -s - exename</code>  and <code>xattr -dr com.apple.quarantine *.dylib</code> to set up tools from scientists who do not have Apple Developer accounts or have been unable to decipher the complexities of Apple notarization.</li>
<li>My team has experienced a lot of issues getting our favorite R tools working on the M1.</li>
</ul>

---

## Post #4 by @norus (2022-02-19 15:30 UTC)

<p>thanks a lot for all these important informations. I´m not the hard computer guy, it has to work and if possible, fast.<br>
I think a solution around Intel I9 supported by NVIDIA GPU and memory is a reasonable solution to our purpose, as Andras Lasso described.<br>
With another CT (Canon) we got a higher resolution and our well working Dell M4800 with NVIDIA + 2G RAM needs a littlebit more time to finish the segmentation-jobs.</p>
<p>thanks again for your advice, your help and your development, stay save</p>

---
