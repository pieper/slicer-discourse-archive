# Volume rendering preset for 3D transthoracic echocardiography

**Topic ID**: 15330
**Date**: 2021-01-04
**URL**: https://discourse.slicer.org/t/volume-rendering-preset-for-3d-transthoracic-echocardiography/15330

---

## Post #1 by @Giulia_Spigariol (2021-01-04 12:28 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.11<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Good morning,<br>
I’m interested in doing a volume rendering of a 3D transtoracic echocardiography. I was wondering where I can find presets (there are none in the selection box) and which have I would have to use.</p>
<p>Thanks so much<br>
Giulia</p>

---

## Post #2 by @cpinter (2021-01-04 14:00 UTC)

<p>There should be many presets in the selection combobox. If you try the latest preview version is it also empty?</p>

---

## Post #3 by @Giulia_Spigariol (2021-01-04 14:16 UTC)

<p>Yes, I have the latest version but no presets at all! Is there a place where I can download them?</p>

---

## Post #4 by @cpinter (2021-01-04 14:31 UTC)

<p>You shouldn’t need to download anything, they are part of the Slicer installer. The presets combobox should look like this:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/38a7ff5ec3dd64984755dd2b50aad0a7763cf6b6.jpeg" alt="image" data-base62-sha1="85cFCULSDvQDeYxQcZOb6iN137M" width="549" height="263"></p>
<p>What operating system do you use? How did you install Slicer? What does the preset list look like?</p>

---

## Post #5 by @Giulia_Spigariol (2021-01-04 14:49 UTC)

<p>I managed to find them just downloading and installing Slicer again, thank you so much!</p>
<p>Do you know which preset I should use for a transtoracic echocardiography?</p>

---

## Post #6 by @lassoan (2021-01-04 16:01 UTC)

<p>Ultrasound presets have not been released publicly yet. Moreover, we switched to using special depth-encoded coloring for rendering echo volume to match how they are displayed on the cart:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a85ccbec2e6238945de6e188cb01a4cd511fb741.jpeg" data-download-href="/uploads/short-url/o1p1UiBWjxvShB8cNdXdSEYnmVj.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a85ccbec2e6238945de6e188cb01a4cd511fb741_2_536x500.jpeg" alt="image" data-base62-sha1="o1p1UiBWjxvShB8cNdXdSEYnmVj" width="536" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a85ccbec2e6238945de6e188cb01a4cd511fb741_2_536x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a85ccbec2e6238945de6e188cb01a4cd511fb741.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a85ccbec2e6238945de6e188cb01a4cd511fb741.jpeg 2x" data-dominant-color="848B7E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">601×560 111 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
(source: <a href="https://www.onlinejase.com/action/showPdf?pii=S0894-7317%2820%2930033-X">Nam et al., JASE 2020</a>)</p>
<p>I’ll ask when the presets are planned to be released and report back here.</p>

---

## Post #7 by @FloCo (2022-06-15 12:58 UTC)

<p>Hello <a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>I am also interested in those presets, do you have any news on this topic ?</p>

---

## Post #8 by @lassoan (2022-06-16 13:28 UTC)

<p>We’ll release the heart echo volume renderer, leaflet segmentation, etc. modules when our paper describing the platform gets accepted. The paper was rejected from a few journals the reviews we got from the last one is quite promising, so I see a good chance that the paper will be accepted soon and the modules will go public within a few months.</p>

---

## Post #9 by @FloCo (2022-06-16 13:41 UTC)

<p>Thank you for your answer ! can’t wait to see this module !</p>

---

## Post #10 by @Tommaso (2022-09-12 09:58 UTC)

<p>Hello <a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>I noticed that the article has been published, congratulations <img src="https://emoji.discourse-cdn.com/twitter/partying_face.png?v=12" title=":partying_face:" class="emoji" alt=":partying_face:" loading="lazy" width="20" height="20"> !</p>
<p>When are you planning the release of all those interesting modules?<br>
I am looking forward to use them!</p>
<p>Tommaso</p>

---

## Post #11 by @lassoan (2022-09-12 13:58 UTC)

<p>Yes, the <a href="https://www.frontiersin.org/articles/10.3389/fcvm.2022.886549/pdf">SlicerHeart paper</a> has been published, and all the stable modules along with it. They are all in SlicerHeart extension, for Slicer-5.0.3 and later. If you don’t find any particular feature then let us know.</p>

---

## Post #12 by @Tommaso (2022-09-14 07:54 UTC)

<p>Hello <a class="mention" href="/u/lassoan">@lassoan</a>, I started using SlicerHeart with Slicer 5.0.3 and I am having the following issues:</p>
<ol>
<li>
<p>I can’t import the data from a GE Vivid 3 US machine. In Slicer 4.11 I had a GE dll to import them, but know it doesn’t seem to work now.<br>
I obtain the following warning:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/50c31bf33d46f71cacbfe2cfbc8566c8650746a8.png" alt="image" data-base62-sha1="bwsdsDoE2eNHuRdmRYpm0ThEyBW" width="372" height="210"><br>
and when I check the imported file this is what appears:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/447df96ffe08138aa68eec645c7c591e1aba06e1.png" data-download-href="/uploads/short-url/9LUmK4ctnYEJ6XPyCDkArVi6e8F.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/447df96ffe08138aa68eec645c7c591e1aba06e1_2_517x181.png" alt="image" data-base62-sha1="9LUmK4ctnYEJ6XPyCDkArVi6e8F" width="517" height="181" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/447df96ffe08138aa68eec645c7c591e1aba06e1_2_517x181.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/447df96ffe08138aa68eec645c7c591e1aba06e1_2_775x271.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/447df96ffe08138aa68eec645c7c591e1aba06e1_2_1034x362.png 2x" data-dominant-color="100E0B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1277×449 72 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>I can create the smoothed volume using the Echo Volume Render, but then I do not have any response from the other parameters of the command:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a704a37982124ef609021e50319ed6fbfa8b50dc.png" data-download-href="/uploads/short-url/nPvFTf27hbNxxgUmGl60e2ng82g.png?dl=1" title="3D Slicer Issue" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a704a37982124ef609021e50319ed6fbfa8b50dc_2_322x375.png" alt="3D Slicer Issue" data-base62-sha1="nPvFTf27hbNxxgUmGl60e2ng82g" width="322" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a704a37982124ef609021e50319ed6fbfa8b50dc_2_322x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a704a37982124ef609021e50319ed6fbfa8b50dc_2_483x562.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a704a37982124ef609021e50319ed6fbfa8b50dc.png 2x" data-dominant-color="3F3C3D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3D Slicer Issue</span><span class="informations">635×738 31.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Moreover, I can’t find the US preset depicted in the article in the Volume Render preset:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/853a0a25f5e4bf411ffa7249728301d0adb89d53.jpeg" data-download-href="/uploads/short-url/j0zQSEMbgg3CaqsfsjegBNN8PU7.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/853a0a25f5e4bf411ffa7249728301d0adb89d53_2_404x375.jpeg" alt="image" data-base62-sha1="j0zQSEMbgg3CaqsfsjegBNN8PU7" width="404" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/853a0a25f5e4bf411ffa7249728301d0adb89d53_2_404x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/853a0a25f5e4bf411ffa7249728301d0adb89d53_2_606x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/853a0a25f5e4bf411ffa7249728301d0adb89d53.jpeg 2x" data-dominant-color="524F56"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">621×576 127 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
</ol>
<p>Would you please help me?</p>
<p>Thank you very much,</p>
<p>Tommaso</p>

---

## Post #13 by @lassoan (2022-09-15 16:40 UTC)

<aside class="quote no-group" data-username="Tommaso" data-post="12" data-topic="15330">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/e9c0ed/48.png" class="avatar"> Tommaso:</div>
<blockquote>
<p>I can’t import the data from a GE Vivid 3 US machine. In Slicer 4.11 I had a GE dll to import them, but know it doesn’t seem to work now.</p>
</blockquote>
</aside>
<p>I’ve just tested this in Slicer-5.0.3 and it still works well.<br>
Have you registered the GE loader by running <code>regsvr32 Image3dLoaderGe.dll</code>?</p>
<aside class="quote no-group" data-username="Tommaso" data-post="12" data-topic="15330">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/e9c0ed/48.png" class="avatar"> Tommaso:</div>
<blockquote>
<p>I can create the smoothed volume using the Echo Volume Render, but then I do not have any response from the other parameters of the command:</p>
</blockquote>
</aside>
<p>I’ve tested this and it works well for me. Do you see any errors in the application log?</p>
<aside class="quote no-group" data-username="Tommaso" data-post="12" data-topic="15330">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/e9c0ed/48.png" class="avatar"> Tommaso:</div>
<blockquote>
<p>Moreover, I can’t find the US preset depicted in the article in the Volume Render preset:</p>
</blockquote>
</aside>
<p>Slicer core Volume Rendering module can do basic rendering without depth-dependent coloring. Some presets are created for this and you can see them in your screenshot (4 presets in the first row in the right; two presets in the second row in the left).</p>

---

## Post #14 by @Tommaso (2022-09-16 12:45 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>I checked the reg variable and it seems ok. Can it be some kind of error due to the fact that I have both version 4.11 and 5.0.3 on my machine?<br>
Moreover I get this errors when I import the US data:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a212cd6934e62e0ac3f1a1e5c5c2d30b5312dd02.png" data-download-href="/uploads/short-url/n7LDjDmDp75cvrP3ilnKpJQdF3I.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a212cd6934e62e0ac3f1a1e5c5c2d30b5312dd02.png" alt="image" data-base62-sha1="n7LDjDmDp75cvrP3ilnKpJQdF3I" width="690" height="56" data-dominant-color="2D2D2D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1897×155 11.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/052860a3bc7597ae4a5ef316dabe3e1f50dbad4b.png" data-download-href="/uploads/short-url/JCTxeMP2WMetlMl9A2nhNKuXZ9.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/052860a3bc7597ae4a5ef316dabe3e1f50dbad4b_2_690x13.png" alt="image" data-base62-sha1="JCTxeMP2WMetlMl9A2nhNKuXZ9" width="690" height="13" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/052860a3bc7597ae4a5ef316dabe3e1f50dbad4b_2_690x13.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/052860a3bc7597ae4a5ef316dabe3e1f50dbad4b_2_1035x19.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/052860a3bc7597ae4a5ef316dabe3e1f50dbad4b_2_1380x26.png 2x" data-dominant-color="58A6EB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1880×36 6.46 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Can you help me?</p>
<p>P.s. the US Render now works properly (I don’t know why <img src="https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=12" title=":sweat_smile:" class="emoji" alt=":sweat_smile:" loading="lazy" width="20" height="20">)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/9245af24f69f25329ac4e483075750704ecf914b.png" data-download-href="/uploads/short-url/kRZ0vVjNQOzOhXZ400urEqqY359.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/9245af24f69f25329ac4e483075750704ecf914b_2_345x183.png" alt="image" data-base62-sha1="kRZ0vVjNQOzOhXZ400urEqqY359" width="345" height="183" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/9245af24f69f25329ac4e483075750704ecf914b_2_345x183.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/9245af24f69f25329ac4e483075750704ecf914b_2_517x274.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/9245af24f69f25329ac4e483075750704ecf914b_2_690x366.png 2x" data-dominant-color="4B4B5A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1911×1019 168 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #15 by @lassoan (2022-09-16 13:44 UTC)

<aside class="quote no-group" data-username="Tommaso" data-post="14" data-topic="15330">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/e9c0ed/48.png" class="avatar"> Tommaso:</div>
<blockquote>
<p>Can it be some kind of error due to the fact that I have both version 4.11 and 5.0.3 on my machine?</p>
</blockquote>
</aside>
<p>That is not a problem, it is completely fine to have any number of Slicer version on your machine.</p>
<aside class="quote no-group" data-username="Tommaso" data-post="14" data-topic="15330">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/e9c0ed/48.png" class="avatar"> Tommaso:</div>
<blockquote>
<p>Moreover I get this errors when I import the US data:</p>
</blockquote>
</aside>
<p>The error message indicates that the GE image loader is installed and the image passed basic content check by Slicer (seems to be a GE 4D US image), but the loader fails to load the image (cannot decode it). Maybe you can try a different version of the loader. If none of them work then I would recommend to contact GE.</p>

---
