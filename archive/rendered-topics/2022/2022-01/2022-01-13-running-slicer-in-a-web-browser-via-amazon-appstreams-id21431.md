# Running Slicer in a web browser via Amazon AppStreams

**Topic ID**: 21431
**Date**: 2022-01-13
**URL**: https://discourse.slicer.org/t/running-slicer-in-a-web-browser-via-amazon-appstreams/21431

---

## Post #1 by @lassoan (2022-01-13 01:21 UTC)

<p>At today’s MONAILabel workshop 100+ people could see how amazingly well Slicer works in a web browser using Amazon AppStream. For those who missed, here is a short demo:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="u3t5twSV6NE" data-video-title="3D Slicer in a web browser - using Amazon AppStream" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=u3t5twSV6NE" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/u3t5twSV6NE/maxresdefault.jpg" title="3D Slicer in a web browser - using Amazon AppStream" width="" height="">
  </a>
</div>

<p>Questions are already coming in if this is generally available and about how this can be set up. <a class="mention" href="/u/pieper">@pieper</a> can you answer this question or ask someone from AWS to answer here?</p>

---

## Post #2 by @pieper (2022-01-13 16:28 UTC)

<p>That’s an excellent demo video <a class="mention" href="/u/lassoan">@lassoan</a>, thanks!</p>
<p>Yes, this is all just off-the-shelf <a href="https://aws.amazon.com/appstream2/">AWS AppStream 2.0</a> and the regular Slicer build.  Qing Liu from AWS and I have been testing this out for a while and have been planning to make a Slicer-specific blog post to explain the details.  Yesterday was the first time I had seen it scaling it up to so many users.</p>

---

## Post #3 by @Ross_Mitchell (2023-03-30 04:04 UTC)

<p><strong>Get Slicer Running on AWS AppStream 2.0 Under Amazon Linux</strong></p>
<p>Further to this thread… I spent quite a bit of time over the last several days figuring out how to get Slicer running on AWS AppStream 2.0 on an <em>Amazon Linux</em> instance (versus a Windows instance). I thought I’d post my solution here to help any others who might be interested in doing this.</p>
<ol>
<li>
<p>First, create an AppStream Image Builder instance. (If you need more details ping me, or post here. There are lots of instructions online). In my AWS zone (Canada Central), I had to opt for a stream.graphics-pro.4xlarge instance. <a href="https://aws.amazon.com/appstream2/pricing/" rel="noopener nofollow ugc">Pricing info</a>. (Make sure you check the “Internet Access” box in the Networking config panel to give your instance access to the internet). Launch this instance.</p>
</li>
<li>
<p>Next, <a href="https://stackoverflow.com/questions/48480143/installing-chromium-on-amazon-linux" rel="noopener nofollow ugc">install the Chromium Browser</a> on your instance</p>
</li>
<li>
<p>Use the browser to <a href="https://download.slicer.org/" rel="noopener nofollow ugc">download</a> the Slicer install package (.tar.gz). As of this writing that file is ‘Slicer-5.2.2-linux-amd64.tar.gz’ (you could also use wget or curl to download the file directly from the command line, and skip the browser install if you want)</p>
</li>
<li>
<p>Unpack this file eg: “tar xzvf Slicer-5.2.2-linux-amd64.tar.gz”. This will create a directory called ‘Slicer-5.2.2-linux-amd64’ with Slicer inside it. I’ll assume this in in your home folder.</p>
</li>
<li>
<p>Install the missing libraries Slicer needs to run:</p>
<ul>
<li>sudo yum install -y mesa-libGLU xcb-util-keysyms xcb-util-renderutil xcb-util-wm  xcb-util-image qt5-qtbase</li>
</ul>
</li>
</ol>
<p>That should do it. You should now be able to launch Slicer on your ImageBuilder instance:</p>
<ul>
<li>~/Slicer-5.2.2-linux-amd64/Slicer</li>
</ul>
<p>I hope this helps!</p>

---

## Post #4 by @jcfr (2023-03-30 04:22 UTC)

<p>Thanks for taking the time to write a detailed summary <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"></p>
<aside class="quote no-group quote-modified" data-username="Ross_Mitchell" data-post="3" data-topic="21431">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ross_mitchell/48/18076_2.png" class="avatar"> Ross_Mitchell:</div>
<blockquote>
<p>sudo yum install -y […] qt5-qtbase</p>
</blockquote>
</aside>
<p>Since we bundled qt libraries, do you know which Qt library or plugin was missing ? I would like to understand if there is anything we would need to fix on the packaging side.</p>

---

## Post #5 by @Ross_Mitchell (2023-04-04 18:40 UTC)

<p>Hello Jean:</p>
<p>I initially got the following error when launching Slicer on Amazon Linux:</p>
<blockquote>
<p>qt.qpa.plugin: Could not load the Qt platform plugin “xcb” in “” even though it was found.</p>
<p>This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.</p>
<p>Available platform plugins are: xcb.</p>
</blockquote>
<p>The key to finding the problems was to set the Qt debug environment variable:</p>
<ul>
<li>export QT_DEBUG_PLUGINS=1</li>
</ul>
<p>Then, launching Slicer produced Qt debug messages. These revealed that there were errors loading a library called “libqxcb.so"</p>
<p>This library is part of the Slicer build, and is located in "lib/QtPlugins/platforms” inside the Slicer install dir.</p>
<p>Next, I checked what dependencies this library had by executing the following from the Slicer install dir:</p>
<ul>
<li>ldd ./lib/QtPlugins/platforms/libqxcb.so</li>
</ul>
<p>This produced a lot of output. I’ve edited this to show only the missing dependencies…</p>
<p>libQt5XcbQpa.so.5 =&gt; not found<br>
libQt5Gui.so.5 =&gt; not found<br>
libQt5DBus.so.5 =&gt; not found<br>
libQt5Core.so.5 =&gt; not found<br>
libxcb-icccm.so.4 =&gt; not found<br>
libxcb-image.so.0 =&gt; not found<br>
libxcb-keysyms.so.1 =&gt; not found<br>
libxcb-render-util.so.0 =&gt; not found</p>
<p>So, I then installed these missing dependencies:</p>
<ul>
<li>sudo yum install xcb-util-keysyms</li>
<li>sudo yum install xcb-util-renderutil</li>
<li>sudo yum install xcb-util-wm</li>
<li>sudo yum install xcb-util-image</li>
<li>sudo yum install qt5-qtbase</li>
</ul>
<p>This allowed Slicer to launch and run!</p>
<p>I hope this helps.</p>

---

## Post #6 by @lassoan (2023-04-04 19:48 UTC)

<p>Thanks a lot, these are all very useful information and they make sense. The only thing that I don’t understand is why <code>qt5-qtbase</code> was needed.</p>
<p>Can you verify that everything works well without installing <code>qt5-qtbase</code>? (or if not, what is missing)</p>

---

## Post #7 by @Kening_Zhang (2023-12-10 07:00 UTC)

<p>I want to know how can I get Slicer in AppStreams, since I only see limited apps for chosen and there is no 3D Slicer now.</p>

---
