---
topic_id: 27683
title: "Installation Problem On Windows 11"
date: 2023-02-07
url: https://discourse.slicer.org/t/27683
---

# Installation problem on Windows 11

**Topic ID**: 27683
**Date**: 2023-02-07
**URL**: https://discourse.slicer.org/t/installation-problem-on-windows-11/27683

---

## Post #1 by @Aiqbal (2023-02-07 17:48 UTC)

<p>Hi,<br>
I am uable to install 3D Slicer on my Windows 11 operating system. I tried the older version as well, but it did not work. It showed that the installer’s integrity check failed. Can anyone help me to overcome this.<br>
Here is the screenshot.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e3606bd15a8276b9acaebdc63e39030b3d5e5c99.png" alt="Screenshot" data-base62-sha1="wrsXXQpzvlitvXYB4zDuMs3neL7" width="481" height="457"></p>

---

## Post #2 by @lassoan (2023-02-07 17:52 UTC)

<p>It indicates that the file have been corrupted. If it happens repeatedly then the most probable root cause is issues in your network, such as slow network connection (the file hosting server gives up on the transfer) or network restrictions (corporate firewall or proxy that intentionally or accidentally messes up the file content). File corruption may be caused by some third-party antivirus (nowadays most of them cause more problems than what they solve).</p>

---

## Post #3 by @lassoan (2023-02-08 13:18 UTC)

<p>You can verify that the downloaded installation package was indeed corrupted/manipulated during network transfer or after it was downloaded by checking its checksum.</p>
<p>For example, I computed the MD5 checksum for the Slicer-5.2.1 Windows installer by opening a command prompt and typing this command:</p>
<pre><code>powershell Get-FileHash c:\Users\andra\Downloads\Slicer-5.2.1-win-amd64.exe -Algorithm MD5
</code></pre>
<p>I got this result:</p>
<pre data-code-wrap="txt"><code class="lang-plaintext">c:\Users\andra\Downloads&gt;powershell Get-FileHash c:\Users\andra\Downloads\Slicer-5.2.1-win-amd64.exe -Algorithm MD5

Algorithm       Hash                                                                   Path
---------       ----                                                                   ----
MD5             35B2C7AC2E04AE0656A44EC340DBEEA2                                       C:\Users\andra\Downloads\Slic...
</code></pre>
<p>If you got a different checksum (hash) value then it means that the file is indeed corrupted. If the file size is shorter than 224738256 bytes then maybe just your network was too slow or you didn’t have enough disk space. If the file is larger then maybe some file manipulation occurred during network transfer or after download.</p>

---

## Post #4 by @Aiqbal (2023-02-08 15:26 UTC)

<p>Thank you all. I have installed it successfully. Actually, the problem was created by the download manager.###</p>

---
