---
topic_id: 423
title: "Slicer Compile Behind Proxy Clone Into Dcmtk Through Http"
date: 2017-06-02
url: https://discourse.slicer.org/t/423
---

# Slicer compile behind proxy (clone into dcmtk through http)

**Topic ID**: 423
**Date**: 2017-06-02
**URL**: https://discourse.slicer.org/t/slicer-compile-behind-proxy-clone-into-dcmtk-through-http/423

---

## Post #1 by @tpenzkofer (2017-06-02 08:27 UTC)

<p>Operating system: Ubuntu 16.04<br>
Slicer version: Git<br>
Expected behavior: compiles<br>
Actual behavior: does not compile (does not clone into dcmtk through http)</p>
<p>Hi all,</p>
<p>I just set up a new development environment which sits behind a http/https proxy, no full internet access, especially no git access. I tried to compile Slicer but it stops at the Cloning into ‘DCMTK’ step. When setting the Slicer_USE_GIT_PROTOCOL option to ‘NO’ the error looks like this (with yes it stops at any git:// link).</p>
<p>Cloning into ‘DCMTK’…<br>
fatal: repository ‘<a href="http://git.dcmtk.org/dcmtk/" rel="nofollow noopener">http://git.dcmtk.org/dcmtk/</a>’ not found</p>
<p>Thank you,<br>
Tobias</p>

---

## Post #2 by @lassoan (2017-06-02 13:41 UTC)

<p>See discussion here: <a href="https://discourse.slicer.org/t/building-slicer-behind-a-firewall/385">Building Slicer behind a firewall</a></p>

---

## Post #3 by @ihnorton (2017-06-02 13:57 UTC)

<p>Is there some reason not to switch to github by default, and update our branch as-needed? We aren’t tracking master anyway.</p>

---

## Post #4 by @jcfr (2017-06-02 14:42 UTC)

<p>Waiting we hear back from <a class="mention" href="/u/fedorov">@fedorov</a>  , I will switch back to our github fork</p>

---

## Post #5 by @jcfr (2017-06-02 15:20 UTC)

<p><a class="mention" href="/u/tpenzkofer">@tpenzkofer</a> Et voila, following <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26069">http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26069</a> clone of DCMTK should work behing proxy.</p>
<p>Hth<br>
Jc</p>

---
