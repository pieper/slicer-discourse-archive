---
topic_id: 48679
title: "Use torchvulkan to enable gpu segmentations in totalsegmentator"
date: 2026-11-02
url: https://discourse.slicer.org/t/48679
last_bumped: 2026-11-11T22:24:30.959Z
---

# Use torchvulkan to enable gpu segmentations in totalsegmentator

**Topic ID**: 48679
**Date**: 2026-11-02
**URL**: https://discourse.slicer.org/t/use-torchvulkan-to-enable-gpu-segmentations-in-totalsegmentator/48679

---

## Post #1 by @Alex_Vergara (2026-11-02 20:35 UTC)

<p>This is very specific to totalsegmentator, please <a class="mention" href="/u/wasserth">@wasserth</a> read the following</p>
<p>Currently, Total Segmentator uses torch that can use a nvidia card, if the user doesn’t have it it default to slow CPU. But there is a marvelous package <a href="https://github.com/zainsharief/torchvulkan" class="inline-onebox" rel="noopener nofollow ugc">GitHub - zainsharief/torchvulkan: Cross-Platform Vulkan Backend for PyTorch · GitHub</a> that I have tested it works really good, that adds Vulkan computation capabilities to torch, ENABLING ALL GPUs, not just nvidia. Two changes required:</p>
<pre data-code-wrap="python"><code class="lang-python">import torchvulkan
device = torch.device("vulkan" if torchvulkan.is_available() else "cpu")
</code></pre>
<p>That’s it, it would run a lot faster in AMD cards for instance, it also allows the use of MoltenVk in macos.</p>

---

## Post #2 by @philippepellerin (2026-11-03 10:29 UTC)

<p>Hi Alex, it looks good.  I have no skills in working with the terminal; thus, practically, what would I do to install Vulkan on my Mac. I went to GitHub, but I have no clue what to do now. Some of your guidance would be helpful.Best regards.</p>

---

## Post #3 by @Alex_Vergara (2026-11-03 10:50 UTC)

<p>on intel macs (MacPorts) → sudo port install MoltenVK<br>
on Silicon Apple (HomeBrew) → brew install MoltenVK</p>
<p>Now you have Vulkan drivers on your mac!</p>

---

## Post #4 by @philippepellerin (2026-11-03 10:58 UTC)

<p>Thank you so much for your fast answer. Shall I do that from the terminal or from the Slicer Python console?</p>

---

## Post #5 by @Alex_Vergara (2026-11-03 12:38 UTC)

<p>that is a system driver package, you must do that from iTerm2</p>
<ol>
<li>Install iTerm2 <a href="https://iterm2.com/" rel="noopener nofollow ugc">https://iterm2.com/</a></li>
<li>Install HomeBrew <a href="https://brew.sh/" rel="noopener nofollow ugc">https://brew.sh/</a> or MacPorts <a href="https://www.macports.org/install.php" rel="noopener nofollow ugc">https://www.macports.org/install.php</a> accordingly to your Mac type</li>
<li>Now you can install MoltenVK</li>
</ol>

---

## Post #6 by @philippepellerin (2026-11-03 14:54 UTC)

<p>I have installed iterm2, as required.<br>
I have a Mac mini with a M2 pro chip, thus ,I take, silicone<br>
I tried both lines which you sent, and then I got those answers<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc1ef36be2b237f7779dc85fe26dc5893006b49b.png" data-download-href="/uploads/short-url/qQc4JykQ0yoQLvuHW3ZFITBGFdN.png?dl=1" title="PastedGraphic-1.png" rel="noopener nofollow ugc"><img width="321" alt="PastedGraphic-1.png" src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc1ef36be2b237f7779dc85fe26dc5893006b49b.png" data-base62-sha1="qQc4JykQ0yoQLvuHW3ZFITBGFdN" height="139"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">PastedGraphic-1.png</span><span class="informations">642×279 42.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @philippepellerin (2026-11-03 15:05 UTC)

<p>Sorry, I did the second step by copying a line of code at the Homebrew address, which seems to have worked quite well. For step 3 I went to Molten VK but I don’t know what to do next. Sorry</p>

---

## Post #8 by @Alex_Vergara (2026-11-04 10:55 UTC)

<p>for homebrew the right command is <code>brew install molten-vk</code></p>
<p>Reminder, this only adds the driver, we need extra steps to make slicer use it</p>

---

## Post #9 by @philippepellerin (2026-11-04 15:36 UTC)

<p>Thanks for your help. î must look dumb to you…I tried the line of code in term and got an error: here after a screen grab<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d2fd1cb193ee581976fc86ada1aed6172edc2bb2.png" data-download-href="/uploads/short-url/u6uyExLjsAu8Gz4eUYZnuY8HECS.png?dl=1" title="PastedGraphic-1.png" rel="noopener nofollow ugc"><img width="320" alt="PastedGraphic-1.png" src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d2fd1cb193ee581976fc86ada1aed6172edc2bb2.png" data-base62-sha1="u6uyExLjsAu8Gz4eUYZnuY8HECS" height="157"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">PastedGraphic-1.png</span><span class="informations">640×315 87.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @Alex_Vergara (2026-11-05 09:43 UTC)

<p>your homebrew is NOT installed, please follow the guide in <a href="https://brew.sh/" rel="noopener nofollow ugc">https://brew.sh/</a></p>

---

## Post #11 by @Philipp_G (2026-11-05 10:29 UTC)

<aside class="quote no-group" data-username="Alex_Vergara" data-post="1" data-topic="48679">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<pre><code class="lang-auto">import torchvulkan
device = torch.device("vulkan" if torchvulkan.is_available() else "cpu")
</code></pre>
</blockquote>
</aside>
<p>I am another novice - I managed to install MoltenVK via brew terminal. If I follow the instructions from the project website “pip install torchvulkan” I get the error “torchvulkan not found” either in terminal (“brew install torchvulkan”) or slicer python console (“pip install torchvulkan”) or (import torchvulkan<br>
device = torch.device(“vulkan” if torchvulkan.is_available() else “cpu”))</p>

---

## Post #12 by @Alex_Vergara (2026-11-05 10:31 UTC)

<p>hello, you need torch&gt;=2.15 for torchvulkan to be available<br>
Also, torchvulkan should be accesible first from your iterm2 console, slicer is still not ready for it yet</p>

---

## Post #13 by @philippepellerin (2026-11-09 09:32 UTC)

<p>Thanks, I installed Homebrew through .vtk, then ran the line of code ,which you sent previously. I ran 3DSlicer; total segmentator, but could not find a difference with its usual processing time…I have a Mac mini, chio M2 pro, 16GBmemory, Mac Os Tahoe</p>

---

## Post #14 by @Alex_Vergara (2026-11-10 16:19 UTC)

<p>Hello, Slicer needs two merge requests I have already sent for torchvulkan to be enabled:</p>
<ol>
<li><a href="https://github.com/fepegar/SlicerPyTorch/pull/27" class="inline-onebox" rel="noopener nofollow ugc">Add torchvulkan fallback by BishopWolf · Pull Request #27 · fepegar/SlicerPyTorch · GitHub</a></li>
<li><a href="https://github.com/lassoan/SlicerTotalSegmentator/pull/87" class="inline-onebox" rel="noopener nofollow ugc">add vulkan capability by BishopWolf · Pull Request #87 · lassoan/SlicerTotalSegmentator · GitHub</a></li>
</ol>
<p>These two PR enables vulkan device in totalsegmentator (at least for me)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8cfaf676ff2d720ab30554c8b1b69630124ad376.jpeg" data-download-href="/uploads/short-url/k7awVtGUvfcB6FWqPu4cwQIBHUy.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8cfaf676ff2d720ab30554c8b1b69630124ad376_2_690x372.jpeg" alt="image" data-base62-sha1="k7awVtGUvfcB6FWqPu4cwQIBHUy" width="690" height="372" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8cfaf676ff2d720ab30554c8b1b69630124ad376_2_690x372.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8cfaf676ff2d720ab30554c8b1b69630124ad376_2_1035x558.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8cfaf676ff2d720ab30554c8b1b69630124ad376_2_1380x744.jpeg 2x" data-dominant-color="989597"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1916×1034 327 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #15 by @zainsharief (2026-11-11 09:50 UTC)

<p>Hi, just a couple things to clear up confusion.</p>
<ol>
<li>torchvulkan comes with moltenvk shipped, so no need to install that <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=16" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></li>
<li><a class="mention" href="/u/philipp_g">@Philipp_G</a> It seems like you might have an Intel Mac - which unfortunately torchvulkan is unable to support due to the lack of pytorch support on them.</li>
<li>the correct backend order should be cuda/mps → vulkan → CPU since we currently have parity performance with mps which is more stable, hence why <a class="mention" href="/u/philippepellerin">@philippepellerin</a> didn’t notice much of a difference.</li>
</ol>

---

## Post #16 by @philippepellerin (2026-11-11 10:12 UTC)

<p>I downloaded the latest release of Slicer: 2026.11.09, and TotalSegmentator runs much faster. I don’t know whether it is because I previously installed Homebrew, since I can’t see any specific message when I launch the task…</p>

---

## Post #17 by @Alex_Vergara (2026-11-11 22:24 UTC)

<p>I have made a lot of tests but I can’t get MPS to work at all</p>
<pre><code class="lang-auto"># MPS (Apple GPU) must not be used: 3D convolutions (aten::conv3d / convtranspose3d), which nnUNet
# relies on, are not implemented on the MPS backend and fail with a hard error
# ("RuntimeError: Conv3D is not supported on MPS") that PYTORCH_ENABLE_MPS_FALLBACK cannot fix.
# Therefore the CPU is used on Macs (unless Vulkan is usable), even when an MPS device is available.
# Tracking: pytorch/pytorch#130256 (ConvTranspose3D FP32) was closed May 2026 as supported in
# torch&gt;=2.8 (via #154696/#145366); FP16/BF16 ConvTranspose3D is still unsupported (#160739, PR #188732
# open) and aten::slow_conv3d_forward (#117949) is still open. Re-enable only after testing
# "--device mps" end-to-end with the Slicer PyTorch version in FP32 (no AMP/autocast).
# Set this to True to try the MPS device again. PYTORCH_ENABLE_MPS_FALLBACK=1 is set for the
# TotalSegmentator process when the MPS device is used.
ENABLE_MPS = False
</code></pre>

---
