---
topic_id: 8747
title: "Registration Ants Syn"
date: 2019-10-11
url: https://discourse.slicer.org/t/8747
---

# Registration ANTs SyN

**Topic ID**: 8747
**Date**: 2019-10-11
**URL**: https://discourse.slicer.org/t/registration-ants-syn/8747

---

## Post #1 by @Cincy (2019-10-11 13:41 UTC)

<p>Operating system:win10 X64<br>
Slicer version:4.10.0<br>
Expected behavior:I want to use SyN registration,Interface prompt build ANTs,so I build the slicer,and I check the option of "USE_ANTS ",but when  I finished it,retry the module(General registration(Brain)),the same error occured.I don’t know how to solve it now.<br>
Looking forward to your reply.Thank you!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/5189039ca4992d92b2af7d9560ac1850b4634c6b.png" data-download-href="/uploads/short-url/bDie2AK6wfI0awVsvHpFllPBzjt.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/5189039ca4992d92b2af7d9560ac1850b4634c6b.png" alt="image" data-base62-sha1="bDie2AK6wfI0awVsvHpFllPBzjt" width="690" height="124" data-dominant-color="070707"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">923×166 1.46 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @Cincy (2019-10-11 13:44 UTC)

<p>And I can run the slicer.exe successfully,but it still prompt build   ANTs</p>

---

## Post #3 by @muratmaga (2019-10-11 15:24 UTC)

<p>You have locally build slicer with ants support. While it shows as an option, it is not enabled by default</p>

---

## Post #4 by @Cincy (2019-10-12 01:27 UTC)

<p>But I have checked the option( USE_ANTS)in  cmake to configure，and would you like to give me some suggestions about  solving it? I want to use SyN of the General registration module.<br>
And thanks for your reply!</p>

---

## Post #5 by @muratmaga (2019-10-12 03:10 UTC)

<p>I might be wrong but my understanding is that option is only going to work if you locally build Ants on your machine. I believe ANTs it’s not part of the Slicer superbuild.</p>

---

## Post #6 by @Cincy (2019-10-12 04:00 UTC)

<p>Ok,I will try.Thanks for your help !</p>

---

## Post #7 by @lassoan (2019-10-12 04:13 UTC)

<p>You may also try Elastix registration library (available via SlicerElastix extension).</p>

---
