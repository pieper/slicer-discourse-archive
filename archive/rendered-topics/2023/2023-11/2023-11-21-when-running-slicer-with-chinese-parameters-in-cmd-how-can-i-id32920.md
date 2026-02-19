---
topic_id: 32920
title: "When Running Slicer With Chinese Parameters In Cmd How Can I"
date: 2023-11-21
url: https://discourse.slicer.org/t/32920
---

# When running Slicer with Chinese parameters in CMD, how can I correctly pass and retrieve the Chinese parameters?

**Topic ID**: 32920
**Date**: 2023-11-21
**URL**: https://discourse.slicer.org/t/when-running-slicer-with-chinese-parameters-in-cmd-how-can-i-correctly-pass-and-retrieve-the-chinese-parameters/32920

---

## Post #1 by @yulaomao (2023-11-21 06:37 UTC)

<p>Hi, everyone. I would like to pass some Chinese parameters when launching Slicer, such as ‘Slicer.exe -f “你好！”’ so that I can read these parameters within Slicer. Currently, I have managed to read the parameters using <code>app.argument</code> , but Chinese characters are displayed as garbled text. Can anyone provide some suggestions? Thank you very much!</p>

---

## Post #2 by @yulaomao (2023-11-21 06:46 UTC)

<p>I saw on a forum that it is possible to modify the CTK code to achieve this, as mentioned in this link: <a href="https://github.com/commontk/AppLauncher/pull/127/commits/872e8df61f9bd69958a772c1da92fc191f755e85" class="inline-onebox" rel="noopener nofollow ugc">Fix passing of non-ASCII characters as command-line arguments by lassoan · Pull Request #127 · commontk/AppLauncher · GitHub</a>. I followed the instructions in that link to modify the relevant code and compiled it, but it didn’t work. The Chinese parameters still appear as garbled text. I also added some code inside the relevant function in ctkAppArguments.cpp to save the parameters to a local text file, but that code didn’t execute either, and no data was written to the text file. Am I using the correct method to compile CTKAppLauncher?</p>

---

## Post #3 by @yulaomao (2023-11-21 06:49 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/045b9c974d51691fa111b4623cff2e68aebbee7b.jpeg" data-download-href="/uploads/short-url/CybARrVPtkEa1ZGb3wSv3j8z6H.jpeg?dl=1" title="f101ddd77b3e7932c6cd9da73a2ca573" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/045b9c974d51691fa111b4623cff2e68aebbee7b_2_619x500.jpeg" alt="f101ddd77b3e7932c6cd9da73a2ca573" data-base62-sha1="CybARrVPtkEa1ZGb3wSv3j8z6H" width="619" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/045b9c974d51691fa111b4623cff2e68aebbee7b_2_619x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/045b9c974d51691fa111b4623cff2e68aebbee7b.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/045b9c974d51691fa111b4623cff2e68aebbee7b.jpeg 2x" data-dominant-color="F3F2F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">f101ddd77b3e7932c6cd9da73a2ca573</span><span class="informations">735×593 92.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
