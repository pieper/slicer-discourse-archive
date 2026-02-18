# Performance drop in slicer while receiving openigtlink messages as server

**Topic ID**: 3098
**Date**: 2018-06-06
**URL**: https://discourse.slicer.org/t/performance-drop-in-slicer-while-receiving-openigtlink-messages-as-server/3098

---

## Post #1 by @roozbehshams (2018-06-06 19:06 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.8.1<br>
Expected behavior: No significant performance drop (at least in 3D view) while receiving messages.<br>
Actual behavior:  significant performance drop</p>
<p>When using openigtlink module in slicer in server mode, if the received message rate exceeds 10 message/second there’s visible frame rate drop in the 3D view drops. I’ve been using a matlab script to connect to the server and send messages. (not sure if this extends to whole slicer performance or only the 3D view; I assume it’s the former). To reproduce this:</p>
<ol>
<li>Create an IGTLink server node in slicer and set check for CRC off with:</li>
</ol>
<pre><code class="lang-auto">getNode("IGTLCon*").SetCheckCRC(0)
</code></pre>
<ol start="2">
<li>You can use this script to rotate the 3D scene. The jitters can be seen while rotating with the mouse as well.</li>
</ol>
<pre><code class="lang-auto">layoutManager = slicer.app.layoutManager()
layoutManager.setLayout(4)  # 3D only

threeDWidget = layoutManager.threeDWidget(0)
threeDView = threeDWidget.threeDView()
threeDView.resetFocalPoint()

threeDController = threeDWidget.threeDController()
threeDController.spinView(True)
threeDView.setAnimationIntervalMs(5)
threeDView.setSpinIncrement(1)
</code></pre>
<ol start="3">
<li>Run the performance_drop_test_slicer.m script in this <a href="https://github.com/roozbehshams/MatlabOpenIGTLink/tree/NativeMatlabTCPIP/src" rel="noopener nofollow ugc">repo</a> or any other openigtlink client to send messages to the slicer server.</li>
</ol>
<p>There’s an FPS drop in the 3D viewer while the messages are being sent. As you can see here:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d7e60ec4de1d0c5d505d3704696695f98d02163e.gif" alt="slicer-performance-drop" data-base62-sha1="uNVyfIO3OH7DO3yQ1shx1c6jige" width="480" height="254"></p>
<p>On a side note, the SetCheckCRC function doesn’t work in the current nightly build (4.9.0-2018-06-05), is there a substitute for it?</p>

---

## Post #2 by @lassoan (2018-06-06 23:50 UTC)

<p>A related issue has been recently fixed. Could you please try the latest nightly version?</p>

---

## Post #3 by @roozbehshams (2018-06-08 23:08 UTC)

<p>A problem that I have with running this with the nightly is that I can’t turn off the CRC check of the IGTLink node. SetCheckCRC(0) doesn’t work in the nightly version.  ( I get an error saying the node doesn’t have a SetCRCCheck attribute).<br>
The node type seems to be different in nightly (vtkSlicerOpenIGTLinkIFModuleMRMLPython.vtkMRMLIGTLConnectorNode) vs stable (vtkCommonCorePython.vtkMRMLIGTLConnectorNode)</p>

---

## Post #4 by @lassoan (2018-06-09 13:11 UTC)

<p>I’ve checked the code and indeed, as a result of some recent refactoring, CRC check is not exposed in the MRML node interface. I’ve submitted a pull request that adds back this feature: <a href="https://github.com/openigtlink/SlicerOpenIGTLink/pull/37">https://github.com/openigtlink/SlicerOpenIGTLink/pull/37</a>. It’ll be probably integrated within a few days.</p>

---

## Post #5 by @leochan2009 (2018-06-11 17:42 UTC)

<p><a class="mention" href="/u/roozbehshams">@roozbehshams</a><br>
Thanks for your report<br>
pull request merged, you could check the nightly build tomorrow</p>

---

## Post #6 by @roozbehshams (2018-06-13 18:48 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/leochan2009">@leochan2009</a> . I tested the nightly, SetCheckCRC is exposed now but slicer crashes when it receives a message. There’s no error message, it’s just closed. I assume it can be reproduced with any openIGTLInk, but you can use the matlab script in my original post. It can be found here: <a href="http://github.com/roozbehshams/MatlabOpenIGTLink/tree/NativeMatlabTCPIP/src" rel="nofollow noopener">github.com/roozbehshams/MatlabOpenIGTLink/tree/NativeMatlabTCPIP/src</a> , the performance_drop_test_slicer script.</p>

---

## Post #7 by @leochan2009 (2018-06-13 19:41 UTC)

<p>Thanks for reporting, i will debug immediately</p>

---

## Post #8 by @leochan2009 (2018-06-13 20:35 UTC)

<p>Hi,<br>
I tested the OpenIGTLinkIF module using the <a href="https://github.com/openigtlink/OpenIGTLink/blob/master/Examples/Tracker/TrackerServer.cxx" rel="nofollow noopener">TrackerServer program</a> in OpenIGTLink library.<br>
The receiving message is working well and Set/GetCheceCRC functions are working as well.<br>
Unfortunately i don’t have Matlab, so i could not check your code.<br>
Probably Andras could check this issue at the same time <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Best,<br>
Longquan</p>

---

## Post #9 by @roozbehshams (2018-06-13 20:39 UTC)

<p>Thanks for looking into it. The problem happens when slicer is used in server mode. I think you should be able to reproduce it if you use the TrackerClient.</p>

---

## Post #10 by @leochan2009 (2018-06-13 22:38 UTC)

<p>Hi,</p>
<p>I just checked with TrackerClient, slicer doesn’t crash either.<br>
When you use the trackerClient for testing, just add one line to set the device name.<br>
transMsg-&gt; SetDeviceName(“Tracker”);<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/openigtlink/OpenIGTLink/blob/master/Examples/Tracker/TrackerClient.cxx#L77" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/openigtlink/OpenIGTLink/blob/master/Examples/Tracker/TrackerClient.cxx#L77" target="_blank" rel="nofollow noopener">openigtlink/OpenIGTLink/blob/master/Examples/Tracker/TrackerClient.cxx#L77</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="67" style="counter-reset: li-counter 66 ;">
<li>ts = igtl::TimeStamp::New();</li>
<li>
</li>
<li>//------------------------------------------------------------</li>
<li>// loop</li>
<li>while (1)</li>
<li>  {</li>
<li>  igtl::Matrix4x4 matrix;</li>
<li>  GetRandomTestMatrix(matrix);</li>
<li>  ts-&gt;GetTime();</li>
<li>  transMsg-&gt;InitPack();</li>
<li class="selected">  transMsg-&gt;SetMatrix(matrix);</li>
<li>  transMsg-&gt;SetTimeStamp(ts);</li>
<li>  transMsg-&gt;Pack();</li>
<li>  socket-&gt;Send(transMsg-&gt;GetPackPointer(), transMsg-&gt;GetPackSize());</li>
<li>  igtl::Sleep(interval); // wait</li>
<li>  }</li>
<li>
</li>
<li>//------------------------------------------------------------</li>
<li>// Close connection</li>
<li>
</li>
<li>socket-&gt;CloseSocket();</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
<br>
otherwise, in slicer you will received bunch of transformation nodes.</p>
<p>Best,<br>
Longquan</p>

---

## Post #11 by @lassoan (2018-06-14 02:22 UTC)

<p>I’ve managed to reproduce the crash, it was due to incorrect receiving of STRING message in OpenIGTLinkIF. I’ve pushed a fix (<a href="https://github.com/openigtlink/SlicerOpenIGTLink/pull/38">https://github.com/openigtlink/SlicerOpenIGTLink/pull/38</a>).</p>

---

## Post #12 by @lassoan (2018-06-14 02:53 UTC)

<p>I could not reproduce the performance drop with latest nightly version of Slicer. Update rate of 3D view on my computer is about 150FPS - with and without continuously streaming messages from Matlab using your script (I’ve changed <code>for t=0:0</code> to <code>for t=0:1000</code> to send many messages).</p>

---

## Post #13 by @roozbehshams (2018-06-14 14:06 UTC)

<p>Thanks Longquan, Andras!<br>
Out of curiosity, how can I check the fps of the 3D view ?</p>

---

## Post #14 by @lassoan (2018-06-14 21:10 UTC)

<aside class="quote no-group" data-username="roozbehshams" data-post="13" data-topic="3098">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/roozbehshams/48/1544_2.png" class="avatar"> roozbehshams:</div>
<blockquote>
<p>how can I check the fps of the 3D view ?</p>
</blockquote>
</aside>
<p>Click push-pin icon in the top-left corner of the 3D view, click the <code>...</code> button, click <code>Show/hide frames per second (FPS)</code>.</p>

---

## Post #15 by @roozbehshams (2018-06-18 14:17 UTC)

<p>Thanks! I also checked with the latest nightly and the performance is as expected.</p>

---
