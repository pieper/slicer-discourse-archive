---
topic_id: 28277
title: "Add Data Dialog Box Appears Black The Second Time Its Opened"
date: 2023-03-10
url: https://discourse.slicer.org/t/28277
---

# Add Data dialog box appears black the second time it's opened

**Topic ID**: 28277
**Date**: 2023-03-10
**URL**: https://discourse.slicer.org/t/add-data-dialog-box-appears-black-the-second-time-its-opened/28277

---

## Post #1 by @ezemikulan (2023-03-10 13:48 UTC)

<p>Hi, I’ve noticed that in versions starting from 5.0 in Linux (Ubuntu 22.04) the Add Data dialog box appears completely black the second time it is opened. I’ve tested it in 5.0, 5.2.1, 5.2.2 and 5.3 (preview). The first time it’s opened it works fine, but after closing and re-opening it doesn’t show anymore. If being opened by dragging and dropping a file, even though it is black the file will be opened after pressing enter, so the functionality is still there but just isn’t displaying correctly. In version 4.8 it works fine.</p>
<p>Thanks for your help.</p>

---

## Post #2 by @pieper (2023-03-10 14:26 UTC)

<p>Hmm, that’s odd.  I mostly use Ubuntu 20.04 and have never seen that.  Perhaps it’s a driver issue or something.</p>
<p>Maybe someone else can comment if they have seen similar issues?</p>

---

## Post #3 by @ezemikulan (2023-03-13 09:36 UTC)

<p>Thanks for you reply. I updated the NVIDIA drivers to the latest version (525) on my computer (GeForce GTX 1070) and still have the issue. I also tried it on three other computers (2 desktops with HD Graphics 630 and a laptop with Iris XE) with freshly installed Ubuntu 22.04 (I had to install libxcb-xinerama0) and also found the same issue.</p>
<p>If there’s anything that I could try let me know. Thanks</p>

---

## Post #4 by @RafaelPalomar (2023-03-13 10:38 UTC)

<p>That’s strange. I can have a look in my systems  and get back to you (and eventually open an issue if I can reproduce this behavior).</p>

---

## Post #5 by @ezemikulan (2023-03-13 11:53 UTC)

<p>Thanks, I’ve found that the Python console shows this error four times when it fails to show the dialog box:</p>
<pre><code class="lang-auto">[Qt] QXcbConnection: XCB error: 8 (BadMatch), sequence: 7165, resource id: 94371965, major code: 130 (Unknown), minor code: 3
</code></pre>

---

## Post #6 by @RafaelPalomar (2023-03-13 12:30 UTC)

<p>I can’t reproduce this error on my Ubuntu 22.04 (nvidia drivers). I have tried both latest stable and preview (are you running on Wayland?). I would think the best candidate for this problem is a dependent package missing :</p>
<ol>
<li>
<p>Make sure you have all the dependencies required for Slicer installed (<a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#debian-ubuntu" class="inline-onebox" rel="noopener nofollow ugc">Getting Started — 3D Slicer documentation</a>)</p>
</li>
<li>
<p>If this does not work, I would suggest that you install the packages we normally use for development (this may pull whatever dependency is missing (<a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/linux.html#ubuntu-21-10-impish-indri" class="inline-onebox" rel="noopener nofollow ugc">GNU/Linux systems — 3D Slicer documentation</a>), this is  a difference between my Ubuntu 22.04 and a fresh install:</p>
</li>
</ol>
<pre><code class="lang-bash">sudo apt update &amp;&amp; sudo apt install git subversion build-essential cmake cmake-curses-gui cmake-qt-gui \
  qtmultimedia5-dev qttools5-dev libqt5xmlpatterns5-dev libqt5svg5-dev qtwebengine5-dev qtscript5-dev \
  qtbase5-private-dev libqt5x11extras5-dev libxt-dev libssl-dev
</code></pre>
<ol start="3">
<li>
<p>If none of these works. You can scan through (<a href="https://discourse.slicer.org/t/cant-start-latest-stable-on-ubuntu-20-04/14029/18" class="inline-onebox">Can't start latest stable on ubuntu 20.04 - #18 by manjula</a>), which was a long discussion around xcb-related problems. Perhaps some of the answer could be useful.</p>
</li>
<li>
<p>If none of this works, I could try to reproduce this in a fresh installation.</p>
</li>
</ol>
<p>Let us know how this goes.</p>

---

## Post #7 by @ezemikulan (2023-03-13 15:49 UTC)

<p>Thanks for the suggestions. All computers were on X11 but one. I’ve now realized that the issue appears only if the Add Data dialog box is closed using the “x” from the window. If I load some data or if I close it using “Cancel” it works fine. I have all dependencies and installing the development packages didn’t fix it. I’ll have look at the link you provided.</p>
<p>Thanks again.</p>

---

## Post #8 by @pieper (2023-03-13 16:48 UTC)

<p>You might also try building from source to see if this is an issue with the packages or something at the Qt or window manager level.  You could also try different window manager environments to see if that makes a difference.</p>

---

## Post #9 by @Suhaim (2025-11-20 07:02 UTC)

<p>Hi all,<br>
I am having the same issue with both Slicer built from source and the official pre-built binary. I followed the first two steps mentioned by <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> here :-</p>
<aside class="quote no-group" data-username="RafaelPalomar" data-post="6" data-topic="28277">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/rafaelpalomar/48/1436_2.png" class="avatar"> RafaelPalomar:</div>
<blockquote>
<ol>
<li>Make sure you have all the dependencies required for Slicer installed (<a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#debian-ubuntu" rel="noopener nofollow ugc">Getting Started — 3D Slicer documentation</a>)</li>
<li>If this does not work, I would suggest that you install the packages we normally use for development (this may pull whatever dependency is missing (<a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/linux.html#ubuntu-21-10-impish-indri" rel="noopener nofollow ugc">GNU/Linux systems — 3D Slicer documentation</a>), this is a difference between my Ubuntu 22.04 and a fresh install:</li>
</ol>
<pre><code class="lang-auto">sudo apt update &amp;&amp; sudo apt install git subversion build-essential cmake cmake-curses-gui cmake-qt-gui \
  qtmultimedia5-dev qttools5-dev libqt5xmlpatterns5-dev libqt5svg5-dev qtwebengine5-dev qtscript5-dev \
  qtbase5-private-dev libqt5x11extras5-dev libxt-dev libssl-dev
</code></pre>
</blockquote>
</aside>
<p>This is my environment details :-<br>
Slicer version: 5.10.0<br>
Operating system: Ubuntu 22.04<br>
Desktop environment: ubuntu:GNOME<br>
Session type: x11<br>
GPU hardware: Mesa Intel® UHD Graphics (TGL GT1)</p>
<p>Steps to reproduce:</p>
<ol>
<li>Open slicer’s pre-built binary or slicer built from source</li>
<li>Click on the “Data” widget</li>
<li>Close the window by clicking on “x“</li>
<li>Click on “Data“ widget again</li>
<li>The “Add Data” widget only has a blank black screen and the following errors are logged</li>
</ol>
<p>Error log :<br>
<code>QXcbConnection: XCB error: 8 (BadMatch), sequence: 2194, resource id: 44040286, major code: 130 (Unknown), minor code: 3</code><br>
<code>QXcbConnection: XCB error: 8 (BadMatch), sequence: 2197, resource id: 44040286, major code: 130 (Unknown), minor code: 3</code><br>
<code>QXcbConnection: XCB error: 8 (BadMatch), sequence: 2213, resource id: 44040286, major code: 130 (Unknown), minor code: 3</code><br>
<code>QXcbConnection: XCB error: 8 (BadMatch), sequence: 2214, resource id: 44040286, major code: 130 (Unknown), minor code: 3</code><br>
<code>QXcbConnection: XCB error: 8 (BadMatch), sequence: 2235, resource id: 44040286, major code: 130 (Unknown), minor code: 3</code><br>
<code>QXcbConnection: XCB error: 8 (BadMatch), sequence: 2241, resource id: 44040286, major code: 130 (Unknown), minor code: 3</code></p>
<p>Was anyone able to find a solution for this?</p>

---

## Post #10 by @Suhaim (2025-11-20 07:16 UTC)

<p>Found this post linking to the <a href="https://github.com/Slicer/Slicer/issues/8579" rel="noopener nofollow ugc">tracked issue</a> :-</p>
<aside class="quote quote-modified" data-post="1" data-topic="44557">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/victor_wayne/48/80778_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/the-add-data-button-is-not-working-properly/44557">The Add Data button is not working properly</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category --style-square " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
    </div>
  </div>
  <blockquote>
    So, when I click the Add Data button, it opens the file dialog box and I am able to load MRIs perfectly. But if I close the file dialog box without loading any MRML or MRI files and then try to open it again the file dialog box just goes full black and nothing is showing. The title bar of that window and the close button is working perfectly fine but it is not showing any files or folders to load. Just a black window. How can I fix it? Thanks for you help. 
(P.S This is problem exists in both pr…
  </blockquote>
</aside>


---
