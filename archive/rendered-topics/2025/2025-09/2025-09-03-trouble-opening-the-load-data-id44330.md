# Trouble Opening the Load Data

**Topic ID**: 44330
**Date**: 2025-09-03
**URL**: https://discourse.slicer.org/t/trouble-opening-the-load-data/44330

---

## Post #1 by @Megan_Weaver (2025-09-03 14:26 UTC)

<p>Hi! I am having difficulty opening the load data every time I try to launch the data I get this error message. Any advice?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b4d6b34603f35dcb7f88ed2e5db631da47ad199.png" data-download-href="/uploads/short-url/1BZ7vAlWWliSSrJ4btPPYx28P6p.png?dl=1" title="Screenshot (282)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b4d6b34603f35dcb7f88ed2e5db631da47ad199_2_690x459.png" alt="Screenshot (282)" data-base62-sha1="1BZ7vAlWWliSSrJ4btPPYx28P6p" width="690" height="459" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b4d6b34603f35dcb7f88ed2e5db631da47ad199_2_690x459.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b4d6b34603f35dcb7f88ed2e5db631da47ad199_2_1035x688.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b4d6b34603f35dcb7f88ed2e5db631da47ad199_2_1380x918.png 2x" data-dominant-color="E9E5E5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (282)</span><span class="informations">2400×1600 392 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @Amy_Morton (2025-09-03 14:34 UTC)

<p>Hi <a class="mention" href="/u/megan_weaver">@Megan_Weaver</a></p>
<p>Do you have an instance of Autoscoper launched? In order for the python api to establish a socket connection, an active instance of Autoscoper needs to be running.  You’ll see an additional icon on your task bar following ‘Launch Autoscoper’</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89ed48654f03a2f1166ede641553b27b8fa98020.png" data-download-href="/uploads/short-url/jG9MWPfcTVgvmMPp9daaRqvPTNe.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/89ed48654f03a2f1166ede641553b27b8fa98020_2_690x400.png" alt="image" data-base62-sha1="jG9MWPfcTVgvmMPp9daaRqvPTNe" width="690" height="400" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/89ed48654f03a2f1166ede641553b27b8fa98020_2_690x400.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/89ed48654f03a2f1166ede641553b27b8fa98020_2_1035x600.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/89ed48654f03a2f1166ede641553b27b8fa98020_2_1380x800.png 2x" data-dominant-color="959093"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1863×1080 187 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @Megan_Weaver (2025-09-03 15:20 UTC)

<p>Thank you. My Autoscoper won’t launch if I have the OpenCL settings on which I assume I need in order for the data to appear?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/856c421bc82e6959b132e4643b0630eb02fcc044.png" data-download-href="/uploads/short-url/j2jrDxQ8JWnH5C52H2x8qY2tpYw.png?dl=1" title="Screenshot (283)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/856c421bc82e6959b132e4643b0630eb02fcc044_2_690x459.png" alt="Screenshot (283)" data-base62-sha1="j2jrDxQ8JWnH5C52H2x8qY2tpYw" width="690" height="459" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/856c421bc82e6959b132e4643b0630eb02fcc044_2_690x459.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/856c421bc82e6959b132e4643b0630eb02fcc044_2_1035x688.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/856c421bc82e6959b132e4643b0630eb02fcc044_2_1380x918.png 2x" data-dominant-color="E9E5E5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (283)</span><span class="informations">2400×1600 383 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @Amy_Morton (2025-09-04 13:33 UTC)

<p>Could you please attach a gif or a step by step of what you attempted, followed by screenshots?</p>
<p>Thanks</p>

---

## Post #5 by @Megan_Weaver (2025-09-05 15:59 UTC)

<p>Hi Amy,</p>
<p>Please let me know if this is not what you mean but this is my attempt to launch Autoscoper:</p>
<ol>
<li>Open AutoscoperM Extension on Slicer</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e037d84f96687b7b3274d0ef977fe043c4a809d8.png" data-download-href="/uploads/short-url/vZwBeXigLhZKg63a4saUIKl5TiU.png?dl=1" title="Screenshot (284)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e037d84f96687b7b3274d0ef977fe043c4a809d8_2_690x459.png" alt="Screenshot (284)" data-base62-sha1="vZwBeXigLhZKg63a4saUIKl5TiU" width="690" height="459" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e037d84f96687b7b3274d0ef977fe043c4a809d8_2_690x459.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e037d84f96687b7b3274d0ef977fe043c4a809d8_2_1035x688.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e037d84f96687b7b3274d0ef977fe043c4a809d8_2_1380x918.png 2x" data-dominant-color="DDDCDC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (284)</span><span class="informations">2400×1600 310 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ol start="2">
<li>Change CUDA to OpenCL</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3dda9ee7c70d05c9bd9a65b033abdc1dc3a2620.png" data-download-href="/uploads/short-url/uefEQfXkJFZRQKoTzEUCDItlpCw.png?dl=1" title="Screenshot (286)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3dda9ee7c70d05c9bd9a65b033abdc1dc3a2620_2_690x459.png" alt="Screenshot (286)" data-base62-sha1="uefEQfXkJFZRQKoTzEUCDItlpCw" width="690" height="459" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3dda9ee7c70d05c9bd9a65b033abdc1dc3a2620_2_690x459.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3dda9ee7c70d05c9bd9a65b033abdc1dc3a2620_2_1035x688.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3dda9ee7c70d05c9bd9a65b033abdc1dc3a2620_2_1380x918.png 2x" data-dominant-color="DCDBDB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (286)</span><span class="informations">2400×1600 316 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ol start="3">
<li>
<p>Launch Autoscoper (the tab to the left of OpenCL)</p>
</li>
<li>
<p>It begins to load (indicated by a blue circle beside the pointer) then crashes and provides me with this error message:</p>
</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/027e803b750cfecd7c69ea6a521987ea8ef1514f.png" data-download-href="/uploads/short-url/m3YSmCmzg9NmTCpOfgewAuZ539.png?dl=1" title="Screenshot (289)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/027e803b750cfecd7c69ea6a521987ea8ef1514f_2_690x459.png" alt="Screenshot (289)" data-base62-sha1="m3YSmCmzg9NmTCpOfgewAuZ539" width="690" height="459" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/027e803b750cfecd7c69ea6a521987ea8ef1514f_2_690x459.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/027e803b750cfecd7c69ea6a521987ea8ef1514f_2_1035x688.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/027e803b750cfecd7c69ea6a521987ea8ef1514f_2_1380x918.png 2x" data-dominant-color="E9E6E5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (289)</span><span class="informations">2400×1600 389 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you so much for providing any assistances.</p>

---

## Post #6 by @Megan_Weaver (2025-09-11 15:39 UTC)

<p>Hi Amy,</p>
<p>I have a quick follow-up. Autoscoper launches fine with CUDA enabled, but as soon as I click Load Sample Data I get an error. I’ve attached a screenshot. Any suggestions on what to try next?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/498d31b29f0b1db0d67ca1033348e0307d47311f.png" data-download-href="/uploads/short-url/auFmsY6NdHQ6wgyxQU5cB33VFOn.png?dl=1" title="Screenshot (299)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/498d31b29f0b1db0d67ca1033348e0307d47311f_2_690x459.png" alt="Screenshot (299)" data-base62-sha1="auFmsY6NdHQ6wgyxQU5cB33VFOn" width="690" height="459" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/498d31b29f0b1db0d67ca1033348e0307d47311f_2_690x459.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/498d31b29f0b1db0d67ca1033348e0307d47311f_2_1035x688.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/498d31b29f0b1db0d67ca1033348e0307d47311f_2_1380x918.png 2x" data-dominant-color="E9E5E5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (299)</span><span class="informations">2400×1600 401 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @John_Holtgrewe (2025-09-11 16:31 UTC)

<p>Hi Megan,</p>
<p>Can you confirm that the Sample data has successfully downloaded? You can find the sample data on this file path: C:\Users\ Your_UserID\AppData\Local\slicer.org\Slicer\cache\SlicerIO</p>

---

## Post #8 by @Megan_Weaver (2025-09-11 16:40 UTC)

<p>Yes the sample data has been successfully downloaded.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a2625c0190312da24d0187c5313b84f2d151e9f.png" data-download-href="/uploads/short-url/azX3VBVzFzs7CkaIjIfDSJid3XN.png?dl=1" title="Screenshot (300)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4a2625c0190312da24d0187c5313b84f2d151e9f_2_690x246.png" alt="Screenshot (300)" data-base62-sha1="azX3VBVzFzs7CkaIjIfDSJid3XN" width="690" height="246" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4a2625c0190312da24d0187c5313b84f2d151e9f_2_690x246.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4a2625c0190312da24d0187c5313b84f2d151e9f_2_1035x369.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4a2625c0190312da24d0187c5313b84f2d151e9f_2_1380x492.png 2x" data-dominant-color="FAFBFB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (300)</span><span class="informations">1993×713 40.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @John_Holtgrewe (2025-09-11 19:25 UTC)

<p>Are you able to load the sample data manually? i.e. Launching Autoscoper, clicking “Open Trial” and then finding the .cfg file for the sample data, rather than clicking “Load Sample Data”?</p>

---

## Post #10 by @Megan_Weaver (2025-09-11 19:54 UTC)

<p>I continue to get the same error. It keeps saying a CUDA driver version is insufficient.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/60ca003439a3336a09124335336219c334271133.png" data-download-href="/uploads/short-url/dOeCyu66XwVL9YTLtI1MBgX3Nzt.png?dl=1" title="Screenshot (301)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/60ca003439a3336a09124335336219c334271133_2_690x459.png" alt="Screenshot (301)" data-base62-sha1="dOeCyu66XwVL9YTLtI1MBgX3Nzt" width="690" height="459" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/60ca003439a3336a09124335336219c334271133_2_690x459.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/60ca003439a3336a09124335336219c334271133_2_1035x688.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/60ca003439a3336a09124335336219c334271133_2_1380x918.png 2x" data-dominant-color="E7E4E4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (301)</span><span class="informations">2400×1600 381 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #11 by @John_Holtgrewe (2025-09-12 15:15 UTC)

<p>Thanks for trying this! Could you provide specs for your computer’s GPU, integrated and dedicated? Also, can check which version of CUDA Toolkit you have?</p>

---

## Post #12 by @Megan_Weaver (2025-09-12 15:53 UTC)

<p>My system has an integrated Intel(R) Iris(R) Xe Graphics GPU and no dedicated NVIDIA GPU. From my understanding, this means CUDA is not applicable on my computer. I attempted to troubleshoot using OpenCL earlier, but I’m still unable to launch Autoscoper that way.</p>

---

## Post #13 by @Megan_Weaver (2025-09-24 16:30 UTC)

<p>Hi John and Amy,</p>
<p>I was wondering if you have any updates on advice to help troubleshoot this issue!</p>
<p>Thanks!</p>

---

## Post #14 by @Megan_Weaver (2025-12-16 16:58 UTC)

<p>Hi all, I’m circling back to this thread and was wondering if there have been any updates or new suggestions for running Autoscoper on a personal computer. Thanks in advance!</p>

---

## Post #15 by @allemangd (2026-01-28 17:17 UTC)

<p>I pushed <a href="https://github.com/BrownBiomechanics/SlicerAutoscoperM/pull/193" rel="noopener nofollow ugc">a fix</a> yesterday that ought to resolve this issue; it seems to be unique to Intel graphics. Please update the extension and test again. If you still encounter issues, please provide logs (accessible via “Help” &gt; “Report a Bug” in the toolbar).</p>

---
