---
topic_id: 16531
title: "Slicer Opens With Black Screen On Windows With Slicer 4 11 2"
date: 2021-03-14
url: https://discourse.slicer.org/t/16531
---

# Slicer opens with black screen on Windows with Slicer-4.11.20210226

**Topic ID**: 16531
**Date**: 2021-03-14
**URL**: https://discourse.slicer.org/t/slicer-opens-with-black-screen-on-windows-with-slicer-4-11-20210226/16531

---

## Post #1 by @Hapietsch (2021-03-14 13:36 UTC)

<p>Hi. I had two versions of Slicer on my PC - older stable and preview versions. I downloaded the latest preview build and the latest stable build. I realized that the latest stable build now includes the area measure for closed loop markups that I need and decided to save myself the confusion, so I wanted to keep only the latest stable version.</p>
<p>So, I uninstalled all other versions except the 4.11.20210226. Now when I try to open Slicer.exe, it just gives me a black screen instead of the welcome module.</p>
<p>I have done a restart. I have uninstalled everything related to Slicer and re-downloaded again. And it still gives me the black screen.</p>
<p>How can I get myself back up and running? I should not have tried to update to the latest version.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0fbe882fcbbb2386983513231ca56ac05b17c20a.png" data-download-href="/uploads/short-url/2fhnfgDBNzeSEaOMaPT1NVd3fTA.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0fbe882fcbbb2386983513231ca56ac05b17c20a_2_690x496.png" alt="image" data-base62-sha1="2fhnfgDBNzeSEaOMaPT1NVd3fTA" width="690" height="496" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0fbe882fcbbb2386983513231ca56ac05b17c20a_2_690x496.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0fbe882fcbbb2386983513231ca56ac05b17c20a.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0fbe882fcbbb2386983513231ca56ac05b17c20a.png 2x" data-dominant-color="0A0A0A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">836×602 4.12 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @Hapietsch (2021-03-14 15:10 UTC)

<p>Update: When I downloaded today’s preview version again, that version of slicer does open with the standard screens. Slicer 4.13.0-2021-03-09</p>
<p>I noted that there are some forum issues previously showing that older hardware or drivers could be the issue. My confusion is that it worked when I checked it before uninstalling the extra versions of slicer that I had, and it does work on the latest preview, so it may not just be the old hardware. Unless preview and stable versions have different rules for hardware that is supported, I guess.</p>
<p>For now I’ll go forward with the preview version. However, I would generally rather use the stable version, so if there is an answer to the black screen there, I appreciate the comments.<br>
Thank you.</p>

---

## Post #3 by @lassoan (2021-03-14 15:57 UTC)

<p>We don’t actively investigate issues or make fixes for old hardware, but as side effect of various changes in the application problems may get introduced or fixed. In latest Slicer Preview Release, we replaced the VTK rendering toolkit to a completely new version, which may explain why some things work better.</p>
<p>It is also possible that your application settings got corrupted. Follow instructions <a href="https://slicer.readthedocs.io/en/latest/user_guide/get_help.html#slicer-application-does-not-start">here</a> to reset your application settings.</p>

---

## Post #4 by @Hapietsch (2021-03-14 18:17 UTC)

<p>Thanks for your comments, I understand you can’t fix a hardware issue. I was hoping it was something that had gone wrong in the install/uninstall that caused the issue since it did seem to work on at least some versions earlier today. Unfortunately, resetting the application settings did not help.</p>
<p>Actually, since I wrote the update where the preview worked, my computer did another automatic windows update, and now both versions have black screen.  Can I go back to the previous version that I had working? Slicer version 4.13.0-2021-02-19.</p>
<p>I don’t see a way to download 4.13.0-2021-02-19</p>

---

## Post #5 by @lassoan (2021-03-15 05:14 UTC)

<p>You can go back and download earlier Slicer versions as described <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/General#Where_can_I_download_Slicer.3F">here</a>.</p>

---

## Post #6 by @Sorin_Acela (2021-11-24 19:03 UTC)

<p>Wrong answers!<br>
I solved the black home screen by launching the app with “Run as Administrator”. It worked smoothly. You can also go to program’s PROPERTIES/ Shortcut/ Advanced…/ Run as Administrator. This way you don’t have to click “Run as Administrator” each time.</p>

---

## Post #7 by @lassoan (2021-11-24 19:41 UTC)

<aside class="quote no-group" data-username="Sorin_Acela" data-post="6" data-topic="16531">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sorin_acela/48/13240_2.png" class="avatar"> Sorin_Acela:</div>
<blockquote>
<p>Wrong answers!</p>
</blockquote>
</aside>
<p>What do you mean? Have you tried older Slicer versions and they required “Run as administrator”, too? Which Slicer versions did you try?</p>
<p>What Windows version do you use? What folder did you install Slicer into?</p>

---

## Post #8 by @Sorin_Acela (2021-12-09 17:45 UTC)

<ol>
<li>No older version. I’m new to it.<br>
2.Latest two versions: the stable one and the next.</li>
<li>Windows 10 professional.</li>
<li>The default folder targeted by the installer.</li>
</ol>
<p>I’ve offered a simple solution. Didn’t specified that on that black screen the mouse could push up the tooltips. That told me that Windows is blocking certain features of the program. I solved such blockage before by running the persecuted app as an administrator. That should be known to the app developers since they didn’t choose the default Program Files folder for the installation. They didn’t know how to evade the Windows restrictions.</p>

---

## Post #9 by @lassoan (2021-12-10 19:51 UTC)

<p>Thanks for sharing your experience. It is most likely a different issue what the user asked about above (as it appears to be related to graphics capabilities and not Windows blocking features of the program), but your tip may help others.</p>
<p>It should not be necessary to run Slicer as an administrator and we would like to learn more about your system configuration where this seems to be required.</p>
<p>Could you take a screenshot of the error message that Windows displays when you attempt to start Slicer as a regular user?</p>
<p>Did you install Slicer in the default location that the installer offered? Is that location within your user folder (<code>c:\Users\yourusername\AppData\Local\NA-MIC\Slicer...</code>)?</p>

---

## Post #10 by @Sorin_Acela (2022-06-21 17:37 UTC)

<p>Another solution is to run Slicer in compatibility mode Windows 8.</p>

---
