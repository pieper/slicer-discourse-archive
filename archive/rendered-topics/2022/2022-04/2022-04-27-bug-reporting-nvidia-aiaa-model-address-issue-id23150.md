---
topic_id: 23150
title: "Bug Reporting Nvidia Aiaa Model Address Issue"
date: 2022-04-27
url: https://discourse.slicer.org/t/23150
---

# [Bug reporting] Nvidia AIAA model address issue 

**Topic ID**: 23150
**Date**: 2022-04-27
**URL**: https://discourse.slicer.org/t/bug-reporting-nvidia-aiaa-model-address-issue/23150

---

## Post #1 by @LeonLin (2022-04-27 15:05 UTC)

<p>Hi all</p>
<p>I keep getting this error while I try to use the Nvidia AIAA extension in Slicer.<br>
<em>Failed to fetch models from remote server. Make sure server address is correct and &lt;server_uri&gt;/v1/models is accessible in browser</em></p>
<p>The model address I used is <strong><a href="http://perklabseg.asuscomm.com:5000/v1/models" rel="noopener nofollow ugc">http://perklabseg.asuscomm.com:5000/v1/models</a></strong>.</p>
<p>I use my phone’s internet so there shouldn’t have a firework problem. I also try the latest version of Slicer which is <strong>Slicer-4.13.0-2022-04-26</strong>  also not working.</p>
<p>In the end, the problem is just solved by leaving the blank in the server field.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a5e74928c7a8e1350b37c864c88a42d2198da7c7.jpeg" alt="AIAA" data-base62-sha1="nFEje65ivJt3ayGmAFWIQKTYkQf" width="454" height="94"></p>
<p>I think this is a bug and I wish this can be fixed in the future</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2022-04-27 15:31 UTC)

<p>Everything looks correct and works as expected.</p>
<aside class="quote no-group" data-username="LeonLin" data-post="1" data-topic="23150">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/leonlin/48/15107_2.png" class="avatar"> LeonLin:</div>
<blockquote>
<p>The model address I used is <strong><a href="http://perklabseg.asuscomm.com:5000/v1/models">http://perklabseg.asuscomm.com:5000/v1/models</a></strong> .</p>
</blockquote>
</aside>
<p>The address of this server is not public information. It is not a secret (can be found in the extension’s source code without encryption), but it is subject to change and in general users should not use this address, but just leave the server address field empty. Where did you find this address? Was there any tutorial that instructed you to type it there?</p>
<p>That said, you can type the address manually and it works well. However, as the error message describes, the address that must be accessible in the browser is <code>&lt;server_uri&gt;/v1/models</code>. In your case this was <code>http://perklabseg.asuscomm.com:5000/v1/models/v1/models</code>. This address was incorrect, because you included <code>v1/models</code> in the server URI. The correct server address is <code>http://perklabseg.asuscomm.com:5000</code>, but again, if you want to use the default Slicer segmentation server then please don’t type the server address but leave the server address field empty.</p>
<p>Also note that developers of NVIDIA-AIAA have changed their focus on working on MONAILabel instead. You can do both training and inference using the <a href="https://github.com/Project-MONAI/MONAILabel/#monai-label">MONAILabel extension of Slicer</a>. I would recommend you to try it.</p>

---

## Post #3 by @LeonLin (2022-06-16 06:50 UTC)

<p>Hi,</p>
<p>Thanks for your reply.</p>
<p>I still cannot get a satisfactory result by using Nvidia AIAA.</p>
<p>I found the default server address <a href="http://skull.cs.queensu.ca:8123" rel="noopener nofollow ugc">http://skull.cs.queensu.ca:8123</a> in <a href="https://github.com/NVIDIA/ai-assisted-annotation-client" rel="noopener nofollow ugc">the source code</a>, but it doesn’t work on my browser.</p>
<p>Is there any new server address now?</p>
<p>Thanks for the information about MONAI, I will try it.</p>

---

## Post #4 by @lassoan (2022-06-17 19:39 UTC)

<p>The server address you are seeing is very, very old. Please use the current Slicer Stable Release or current Slicer Preview Release.</p>

---

## Post #5 by @LeonLin (2022-06-27 07:18 UTC)

<p>Ok, got it. Thanks for your help.</p>

---
