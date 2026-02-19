---
topic_id: 14413
title: "Problem Running Slicer On Centos8"
date: 2020-11-03
url: https://discourse.slicer.org/t/14413
---

# Problem running Slicer on CentOS8

**Topic ID**: 14413
**Date**: 2020-11-03
**URL**: https://discourse.slicer.org/t/problem-running-slicer-on-centos8/14413

---

## Post #1 by @Yuting_Deng (2020-11-03 18:16 UTC)

<p>I was having the same problems opening Slicer 4.11 with CentOS8. I have followed the methods mentioned above and made sure that all the missing libraries have been installed, but I still keep having the following errors:</p>
<pre><code>[hermioned@localhost Slicer-4.11.20200930-linux-amd64]$ ldd /home/hermioned/Slicer-4.11.20200930-linux-amd64/lib/QtPlugins/platforms/libqxcb.so | grep "not found"
/home/hermioned/Slicer-4.11.20200930-linux-amd64/lib/QtPlugins/platforms/libqxcb.so: /lib64/libQt5XcbQpa.so.5: version `Qt_5_PRIVATE_API' not found (required by /home/hermioned/Slicer-4.11.20200930-linux-amd64/lib/QtPlugins/platforms/libqxcb.so)

/home/hermioned/Slicer-4.11.20200930-linux-amd64/lib/QtPlugins/platforms/libqxcb.so: /lib64/libQt5Gui.so.5: version `Qt_5_PRIVATE_API' not found (required by /home/hermioned/Slicer-4.11.20200930-linux-amd64/lib/QtPlugins/platforms/libqxcb.so)

/home/hermioned/Slicer-4.11.20200930-linux-amd64/lib/QtPlugins/platforms/libqxcb.so: /lib64/libQt5Core.so.5: version `Qt_5.15' not found (required by /home/hermioned/Slicer-4.11.20200930-linux-amd64/lib/QtPlugins/platforms/libqxcb.so)
</code></pre>
<p>I installed and updated libqxcb.so using <code>updatedb &amp;&amp; locate libQt5XcbQpa.so.5</code> and then  and<code> "strings -d /usr/lib64/libQt5XcbQpa.so.5 | grep Qt.*API"</code>, I get the result <code>"Qt_5.12.5_PRIVATE_API"</code><br>
I see the problem here is: Slicer is looking for Qt_5_PRIVATE_API but I have “Qt_5.12.5_PRIVATE_API”, they just have different names/versions.<br>
Is there a way that I could tell Slicer to look for “Qt_5.12.5_PRIVATE_API”?</p>

---

## Post #2 by @lassoan (2020-11-03 20:38 UTC)

<p>Slicer package includes Qt (Slicer-4.11.20200930 uses Qt-5.15.1). When you run the application using the “launcher” (<code>./Slicer</code>), the launcher sets up LD library paths so that Qt bundled with Slicer is found. If you simply run <code>ldd</code> (not via the launcher) then you will get false alarms, as the correct paths are not set up.</p>
<p>What happens if you run Slicer using the launcher (<code>./Slicer</code>)?</p>

---

## Post #3 by @Yuting_Deng (2020-11-04 18:49 UTC)

<p>Now it works! Thanks so much!</p>

---

## Post #4 by @muratmaga (2020-11-04 19:22 UTC)

<p>Sorry, what was the solution?<br>
Or rather what was the original problem that ./Slicer didn’t work?</p>

---

## Post #5 by @Yuting_Deng (2020-11-04 19:37 UTC)

<p>After I installed all the missing libraries, using:</p>
<blockquote>
<pre><code>[hermioned@localhost Slicer-4.11.20200930-linux-amd64]$ ldd /home/hermioned/Slicer-4.11.20200930-linux-amd64/lib/QtPlugins/platforms/libqxcb.so | grep "not found"
    	libQt5XcbQpa.so.5 =&gt; not found
    	libQt5Gui.so.5 =&gt; not found
    	libQt5DBus.so.5 =&gt; not found
    	libQt5Core.so.5 =&gt; not found
    	libxcb-render-util.so.0 =&gt; not found
</code></pre>
</blockquote>
<p>Even though I still have the error message shown below, I am able to use <code>./Slicer</code> to open Slicer now</p>
<blockquote>
<p>[hermioned@localhost Slicer-4.11.20200930-linux-amd64]$ ldd /home/hermioned/Slicer-4.11.20200930-linux-amd64/lib/QtPlugins/platforms/libqxcb.so | grep “not found”</p>
<p>/home/hermioned/Slicer-4.11.20200930-linux-amd64/lib/QtPlugins/platforms/libqxcb.so: /lib64/libQt5XcbQpa.so.5: version `Qt_5_PRIVATE_API’ not found (required by /home/hermioned/Slicer-4.11.20200930-linux-amd64/lib/QtPlugins/platforms/libqxcb.so)</p>
<p>/home/hermioned/Slicer-4.11.20200930-linux-amd64/lib/QtPlugins/platforms/libqxcb.so: /lib64/libQt5Gui.so.5: version `Qt_5_PRIVATE_API’ not found (required by /home/hermioned/Slicer-4.11.20200930-linux-amd64/lib/QtPlugins/platforms/libqxcb.so)</p>
<p>/home/hermioned/Slicer-4.11.20200930-linux-amd64/lib/QtPlugins/platforms/libqxcb.so: /lib64/libQt5Core.so.5: version `Qt_5.15’ not found (required by /home/hermioned/Slicer-4.11.20200930-linux-amd64/lib/QtPlugins/platforms/libqxcb.so)</p>
</blockquote>

---

## Post #6 by @lassoan (2020-11-05 05:18 UTC)

<p>When you run <code>ldd</code> outside Slicer’s virtual environment (set up by the <code>./Slicer</code> launcher) then the “errors” that you listed are expected to appear, that’s the correct behavior. You will not see the errors if you execute ldd with the launcher (<code>./Slicer</code>).</p>

---
