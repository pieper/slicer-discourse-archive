---
topic_id: 23235
title: "Slicer Not Responding On Windows11"
date: 2022-05-02
url: https://discourse.slicer.org/t/23235
---

# Slicer Not Responding on Windows11

**Topic ID**: 23235
**Date**: 2022-05-02
**URL**: https://discourse.slicer.org/t/slicer-not-responding-on-windows11/23235

---

## Post #1 by @Yun_Chen (2022-05-02 12:21 UTC)

<p>Dear friends,</p>
<p>I upgraded my system to Windows 11 recently, and the 3D Slicer no longer working.</p>
<p>When I open 3D Slicer, after the flashes loading all the modules and poping up the Slicer interface, the window white out and title shows “3D Slicer 4.11.20210226 (Not Responding)” no matter how long I wait. I have tried uninstall it, clear all the Slicer reigistries in “regedit” and reinstall the version 4.11 or 4.13. However the problem still exist.</p>
<p>Is there anything could help me with this? Greatly appreciate your assistance!</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/40f40b6fa939b3bc2a890726fbf00df7c8187aeb.png" alt="image" data-base62-sha1="9gBq7TooSseRtCZFU7RiRG4UooX" width="328" height="120"></p>

---

## Post #2 by @lassoan (2022-05-02 12:31 UTC)

<p>I’ve just tried Slicer-4.11.20210226 and the <a href="https://download.slicer.org/bitstream/626ea8a5e8408647b3911e1c">latest Slicer Preview Release</a> and they both started up without issues. Check out these <a href="https://slicer.readthedocs.io/en/latest/user_guide/get_help.html#slicer-application-does-not-start">troubleshooting instructions</a> and let us know what you find.</p>

---

## Post #3 by @jamesobutler (2022-05-02 12:55 UTC)

<p>Is this the same issue as you what you posted at the following? There you seem to suggest 3D Slicer loads normally when you have 1 monitor, but then does not open normally when you have 2 monitors. This was on Windows 11 using Slicer 4.11.20210226?</p>
<aside class="quote quote-modified" data-post="20" data-topic="7469">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/yun_chen/48/15171_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/slicer-4-10-2-not-responding-on-windows-10/7469/20">Slicer 4.10.2 Not responding on Windows 10 (blank screen on older laptop)</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi everyone, I had the same issue. When I open 3D Slicer, after the flashes loading all the modules and poping up the Slicer interface, the window white out and title shows “3D Slicer 4.11.20210226 (Not Responding)” no matter how long I wait. I have tried uninstall it, clear all the Slicer reigistries in “regedit” and reinstall the version 4.11 or 4.13. However the problem still exist. 
It looks like the multiple monitor issue as mentioned above. When I disable a monitor and use only one, the 3D…
  </blockquote>
</aside>


---

## Post #4 by @Yun_Chen (2022-05-03 01:34 UTC)

<p>Thank you my friend. I found that it might be the dual monitor issue mentioned in another post. I will delete this post. Thank you for your help!</p>

---

## Post #5 by @Yun_Chen (2022-05-03 01:35 UTC)

<p>Yes I think so. One monitor worked fine. Thank you for mention this. I may delete this post and discuss this matter in the other post.</p>

---

## Post #6 by @H_Tai (2024-07-03 20:04 UTC)

<p>I had the same issue, it appears that Slicer has an issue with booting up when two monitors are used.</p>

---

## Post #7 by @muratmaga (2024-07-03 20:11 UTC)

<p>That thread is over two years old and for an older version of Slicer. Have you tried with the latest stable? Do you still have the issue.</p>
<p>We routinely use Slicer on Windows 10/11 with dual monitor setups without any hiccup. It is also a possibility with your graphics driver or monitor setup.</p>

---

## Post #8 by @lassoan (2024-07-03 20:44 UTC)

<p>I think older Windows versions had issues with restoring application window positions when the same computer is used sometimes with one, sometimes with multiple monitors.</p>
<p>You can reset the application settings by removing the <code>Slicer.ini</code> file. You can do that by typing this into Windows Command Prompt (this actually saves a backup copy as <code>Slicer.ini.backup</code>, in case you want to restore the settings later) :</p>
<pre><code>move %appdata%\slicer.org\Slicer.ini %appdata%\slicer.org\Slicer.ini.backup
</code></pre>

---
