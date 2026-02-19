---
topic_id: 17662
title: "Simple Installation Of 3D Slicer Source Code Ubuntu 20 0"
date: 2021-05-17
url: https://discourse.slicer.org/t/17662
---

# Simple installation of 3D Slicer (Source code ubuntu 20.0)

**Topic ID**: 17662
**Date**: 2021-05-17
**URL**: https://discourse.slicer.org/t/simple-installation-of-3d-slicer-source-code-ubuntu-20-0/17662

---

## Post #1 by @Soufiyan-Yachou (2021-05-17 19:54 UTC)

<p>Hello i am a new user of 3D Slicer and ubuntu systeme i need easy file how to install 3D slicer with all libraries . Thanks</p>

---

## Post #2 by @pieper (2021-05-17 19:59 UTC)

<p>This should have everything you need.  Let us know if you run into anything unexpected.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/linux.html#ubuntu-20-04-focal-fossa" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/linux.html#ubuntu-20-04-focal-fossa</a></p>

---

## Post #3 by @Soufiyan-Yachou (2021-05-17 20:14 UTC)

<p>Hello sir thanks for your answer when i use the first command it’s look like :<br>
Reading package lists… Done<br>
Building dependency tree<br>
Reading state information… Done<br>
W: Target Packages (non-free/binary-amd64/Packages) is configured multiple times in /etc/apt/sources.list:58 and /etc/apt/sources.list.d/opera-stable.list:4<br>
W: Target Packages (non-free/binary-i386/Packages) is configured multiple times in /etc/apt/sources.list:58 and /etc/apt/sources.list.d/opera-stable.list:4<br>
W: Target Packages (non-free/binary-all/Packages) is configured multiple times in /etc/apt/sources.list:58 and /etc/apt/sources.list.d/opera-stable.list:4<br>
W: Target Translations (non-free/i18n/Translation-en_US) is configured multiple times in /etc/apt/sources.list:58 and /etc/apt/sources.list.d/opera-stable.list:4<br>
W: Target Translations (non-free/i18n/Translation-en) is configured multiple times in /etc/apt/sources.list:58 and /etc/apt/sources.list.d/opera-stable.list:4<br>
W: Target DEP-11 (non-free/dep11/Components-amd64.yml) is configured multiple times in /etc/apt/sources.list:58 and /etc/apt/sources.list.d/opera-stable.list:4<br>
W: Target DEP-11 (non-free/dep11/Components-all.yml) is configured multiple times in /etc/apt/sources.list:58 and /etc/apt/sources.list.d/opera-stable.list:4<br>
W: Target DEP-11-icons-small (non-free/dep11/icons-48x48.tar) is configured multiple times in /etc/apt/sources.list:58 and /etc/apt/sources.list.d/opera-stable.list:4<br>
W: Target DEP-11-icons (non-free/dep11/icons-64x64.tar) is configured multiple times in /etc/apt/sources.list:58 and /etc/apt/sources.list.d/opera-stable.list:4<br>
W: Target DEP-11-icons-hidpi (non-free/dep11/icons-64x64@2.tar) is configured multiple times in /etc/apt/sources.list:58 and /etc/apt/sources.list.d/opera-stable.list:4<br>
W: Target CNF (non-free/cnf/Commands-amd64) is configured multiple times in /etc/apt/sources.list:58 and /etc/apt/sources.list.d/opera-stable.list:4<br>
W: Target CNF (non-free/cnf/Commands-all) is configured multiple times in /etc/apt/sources.list:58 and /etc/apt/sources.list.d/opera-stable.list:4<br>
E: Unable to locate package qt5multimedia-dev<br>
E: Unable to locate package lqtbase5-private-dev</p>

---

## Post #4 by @lassoan (2021-05-17 20:35 UTC)

<p>If you just need to run Slicer (you don’t want to build it from source code) then you can follow <a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#linux">these steps</a>.</p>

---

## Post #5 by @Soufiyan-Yachou (2021-05-17 20:39 UTC)

<p>hello sir , when i run it from this he closed when i cut anything in 3D</p>

---

## Post #6 by @lassoan (2021-05-17 20:43 UTC)

<p>The Slicer version that you build from source should behave exactly the same as the pre-built version that you download. If you have questions about what options you have for cutting models (with or without capping) then please post it in a separate topic. Keep this topic on installing/building Slicer on Ubuntu 20.</p>

---

## Post #7 by @pieper (2021-05-17 21:20 UTC)

<p>If you still need to build from source, try running <code>sudo apt update</code> before the <code>sudo apt install ...</code> command.  Also, double check that you have 20.04 since ubuntu 21.04 version appears to have changed the dependencies and we don’t have a recipe yet.</p>

---

## Post #8 by @issakomi (2021-05-18 04:58 UTC)

<aside class="quote no-group">
<blockquote>
<p>E: Unable to locate package qt5multimedia-dev<br>
E: Unable to locate package lqtbase5-private-dev</p>
</blockquote>
</aside>
<p>typos in docs (for Debian 10):<br>
qt5multimedia-dev → qtmultimedia5-dev<br>
lqtbase5-private-dev → qtbase5-private-dev</p>

---
