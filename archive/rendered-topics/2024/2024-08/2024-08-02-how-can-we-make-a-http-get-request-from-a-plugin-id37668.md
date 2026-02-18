# How can we make a http get request from a plugin

**Topic ID**: 37668
**Date**: 2024-08-02
**URL**: https://discourse.slicer.org/t/how-can-we-make-a-http-get-request-from-a-plugin/37668

---

## Post #1 by @maniron (2024-08-02 11:25 UTC)

<p>Hi,<br>
I am trying to hit my backend flask python server from the plugin which is integrated with 3D slicer but due to some reasons its not working. Kindly help me out how I can achieve it</p>

---

## Post #2 by @pieper (2024-08-02 11:36 UTC)

<p>You can use the <code>requests</code> package from python to access http endpoints.</p>

---

## Post #3 by @maniron (2024-08-02 11:38 UTC)

<p>I tried , as I am working from an organization I guess I am not able to hit the end point, but the same URL works fine when I perform curl</p>

---

## Post #4 by @pieper (2024-08-02 12:09 UTC)

<p>Maybe there’s a proxy or other special case.  You can debug this with python outside of slicer using various http packages or options and then whatever you find that works should also work inside Slicer.</p>

---

## Post #5 by @maniron (2024-08-05 05:19 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a> I tried the URL from browser and through curl command, both worked fine, but through slicer its not hitting the URL</p>

---

## Post #6 by @pieper (2024-08-05 11:37 UTC)

<p>You should use the same python packages outside of slicer for testing and then use that same approach inside slicer.</p>

---

## Post #7 by @maniron (2024-08-09 04:13 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a> The issue was with VPN which was sorted and the HTTP get request is working thanks</p>

---
