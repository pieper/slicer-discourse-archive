---
topic_id: 23651
title: "Linux Opening Extension Manager Makes Slicer Stuck"
date: 2022-05-31
url: https://discourse.slicer.org/t/23651
---

# [Linux] Opening extension manager makes slicer stuck

**Topic ID**: 23651
**Date**: 2022-05-31
**URL**: https://discourse.slicer.org/t/linux-opening-extension-manager-makes-slicer-stuck/23651

---

## Post #1 by @SaraPoli22 (2022-05-31 13:42 UTC)

<p>Hi, I’m working with Slicer 5.0.2 on Linux, but when I try to open extension manager the program crashes.<br>
I looked at the topic <a href="https://discourse.slicer.org/t/opening-extension-manager-makes-slicer-crash-on-linux/7589" class="inline-onebox">Opening extension manager makes Slicer crash on Linux</a>, but couldn’t find a solution that works.</p>

---

## Post #2 by @pieper (2022-05-31 15:37 UTC)

<p>The extension manager works for me on Ubuntu 20.04.  Maybe you have a proxy or something?</p>

---

## Post #3 by @SaraPoli22 (2022-06-01 06:39 UTC)

<p>I apologize, but I’m a beginner; I’m using a pc from my university, how can I check if it has a proxy?</p>

---

## Post #4 by @pieper (2022-06-01 13:40 UTC)

<p>I don’t work in an institution that uses proxies so I don’t have personal experience either, but you may be able to ask around to see if others have faced issues like this.  From what I hear each configuration is a bit different and sometimes things need to be tweaked at the IT-team level.  This post may help:</p>
<aside class="quote quote-modified" data-post="1" data-topic="6545">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/using-slicer-behind-proxy/6545">Using slicer behind proxy</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    We are behind a corporate proxy, and more and more this creates issues with sample set downloads though slicer. E.g., this is the contents of the mrhead.nrrd when I use the sample data: 
This windows workstation is already configured to use specified proxy. Is there way to set this proxy explicitly from .slicerrc.py? 

Proxy Server Use Required



Internet Access requires the use of a web proxy server.





Please configure your web browser to automatically detect web proxy settings.
 
For assis…
  </blockquote>
</aside>


---

## Post #5 by @rbumm (2022-06-01 17:58 UTC)

<p>Hi Sara,<br>
we face similar problems here in a hospital network. There are firewall restrictions that disable the use of the extension manager, particularly in downloading and installing extensions as a normal user. You could contact an admin to ask for help (they could install the extensions for you or a user group)  or  use Slicer on a laptop in the public WLAN if there is one. Of course you need to take care not to take patient data to a public WLAN.<br>
Cheers &amp; good luck<br>
Rudolf</p>

---

## Post #6 by @muratmaga (2022-06-03 04:19 UTC)

<aside class="quote no-group" data-username="rbumm" data-post="5" data-topic="23651">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>we face similar problems here in a hospital network.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/rbumm">@rbumm</a> <a class="mention" href="/u/sarapoli22">@SaraPoli22</a><br>
We had this problem for about 10 years, and finally convinced the network admins to grant firewall exceptions for Slicer related domains. If you cannot get that exception granted, use the benefit of fully portable slicer by:</p>
<ol>
<li>On a personal laptop install slicer + all extensions you will need.</li>
<li>Zip this file and upload to a cloud file share,</li>
<li>Download and unzip on the hospital/restricted environment and use from there (or copy from USB drive, if you are allowed).</li>
</ol>
<p>Of course updating extensions is not possible without repackaging them, but I still found this an easier solution when I have to have Slicer on a dozen computers behind firewalls (and making sure we are all using the same version etc)…</p>

---

## Post #7 by @SaraPoli22 (2022-06-07 09:34 UTC)

<p>Thanks everyone for the answers.<br>
At the moment the extension manager opens correctly, but we encountered a new error while installing the jupyter extension. In fact, it is downloaded and installed, but Slicer no longer reopens after reboot to complete the extension.</p>

---
