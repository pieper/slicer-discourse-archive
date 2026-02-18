# Streaming Red Slice to mobile device

**Topic ID**: 10927
**Date**: 2020-03-31
**URL**: https://discourse.slicer.org/t/streaming-red-slice-to-mobile-device/10927

---

## Post #1 by @mcfly3001 (2020-03-31 07:14 UTC)

<p>Hi,</p>
<p>I am currently trying to find out how I could stream one of Slicers slices (e.g. the red slice) to another device. There seem to be lots of options to receive image streams in Slicer (e.g. PlusToolkit, OpenIGTLink) though I could not find a tutorial how I could send the image data to another client.</p>
<p>First I tried to use the OpenIGTLink interface with python. So far I could not find the suitable vtkMRML…Node for sending an ImageMessage. If I understood correctly, I can use RegisterOutgoingMRMLNode on an vtkMRMLIGTLConnectorNode to send data to a client. Though it is not so clear for me, what kind of node to attach for sending the image of a slice.</p>
<p>My current approach now makes use of the pyIGTLink module which supports ImageMessages. Would this be the correct way to go?</p>
<p>Furthermore I have some concerns about the streaming performance. The receiver is a mobile device, so we use WLAN. Our goal is to implement a live streaming of the slice. Not sure whether this is possible by sending raw image data. The C++ build of OpenIGTLink has examples for video streaming. For example they are using the VP9 codec for compression. I assume this feature wont be available in any python implementation of OpenIGTLink.<br>
Could I implement video streaming in Slicer if I would build Slicer in C++ and extending it? So far I have only used the Python programming features of Slicer. If doable, I would switch to C++ to implement video streaming.</p>
<p>Thanks for any feedback!</p>

---

## Post #2 by @lassoan (2020-03-31 15:51 UTC)

<aside class="quote no-group" data-username="mcfly3001" data-post="1" data-topic="10927">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mcfly3001/48/6437_2.png" class="avatar"> mcfly3001:</div>
<blockquote>
<p>So far I could not find the suitable vtkMRML…Node for sending an ImageMessage</p>
</blockquote>
</aside>
<p>vtkMRMLScalarVolumeNode sends image messages.</p>
<aside class="quote no-group" data-username="mcfly3001" data-post="1" data-topic="10927">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mcfly3001/48/6437_2.png" class="avatar"> mcfly3001:</div>
<blockquote>
<p>My current approach now makes use of the pyIGTLink module which supports ImageMessages. Would this be the correct way to go?</p>
</blockquote>
</aside>
<p>Probably the C++ implementation is faster and it interferes less with the main application GUI.</p>
<aside class="quote no-group" data-username="mcfly3001" data-post="1" data-topic="10927">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mcfly3001/48/6437_2.png" class="avatar"> mcfly3001:</div>
<blockquote>
<p>Furthermore I have some concerns about the streaming performance. The receiver is a mobile device, so we use WLAN.</p>
</blockquote>
</aside>
<p>The bottleneck can be wifi bandwidth, which you may address by using a dedicated wifi access point with high-speed protocols.</p>
<p>You may drastically reduce the required bandwidth (by 90-99%) by using compression, but then you may run into performance issues due to the overhead of compression. h264 compression/decompression is hardware-accelerated on most platforms (even mobile), so that would be likely to work. However, there are inconveniences with licensing (you cannot ship h264 libraries to users without paying license fee or at least keeping track of the number of instances distributed to users). VP9 has no licensing issues but VP9 compression is very slow, and VP9 decompression is not very fast either, so there is a higher chance that it’ll limit your performance.</p>
<p>If you only need to stream video (no transforms, no metadata, etc.) then you might also look into consumer video streaming protocols.</p>
<p>We have been also successfully using VNC to allow clinicians to use Slicer in the operating room on a tablet. We even show live ultrasound video, but the main interaction happens on static images:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="90l0T1ADe_Y" data-video-title="Navigated breast conserving surgery" data-video-start-time="54" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=90l0T1ADe_Y&amp;t=54" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/90l0T1ADe_Y/maxresdefault.jpg" title="Navigated breast conserving surgery" width="" height="">
  </a>
</div>


---

## Post #3 by @mcfly3001 (2020-04-01 06:40 UTC)

<p>Thanks for the many hints. I will try to use the vtkMRMLScalarVolumeNode first and test how it performs.</p>
<blockquote>
<p>Probably the C++ implementation is faster and it interferes less with the main application GUI.</p>
</blockquote>
<p>By this you mean that building Slicer on my own and integrating the C++ OpenIGTLink will be faster, right? I assume OpenIGTLink is already somewhere in the build environment as Slicer already supports IGTL. Ideally I would extend the Slicer IGTL module to stream slices via video streaming.</p>
<blockquote>
<p>We have been also successfully using VNC to allow clinicians to use Slicer in the operating room on a tablet.</p>
</blockquote>
<p>The video looks really nice! Though I guess VNC won’t be an option for us as the mobile client will receive the stream in an application which is being developed.</p>

---

## Post #4 by @lassoan (2020-04-01 13:39 UTC)

<aside class="quote no-group" data-username="mcfly3001" data-post="3" data-topic="10927">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mcfly3001/48/6437_2.png" class="avatar"> mcfly3001:</div>
<blockquote>
<p>By this you mean that building Slicer on my own and integrating the C++ OpenIGTLink will be faster, right?</p>
</blockquote>
</aside>
<p>Slicer already has compressed streaming video support, so you don’t need to build Slicer. You can implement a scripted module that captures a view and saves it into a vtkMRMLScalarVolumeNode and OpenIGTLinkIF module takes care of the rest.</p>
<aside class="quote no-group" data-username="mcfly3001" data-post="3" data-topic="10927">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mcfly3001/48/6437_2.png" class="avatar"> mcfly3001:</div>
<blockquote>
<p>Though I guess VNC won’t be an option for us as the mobile client will receive the stream in an application which is being developed.</p>
</blockquote>
</aside>
<p>You can use VNC protocol to show (and interact with) Slicer in a webpage using noVNC. For example, this is how <a href="https://github.com/pieper/SlicerDockers">Slicer docker containers</a> work: Slicer runs on a cloud server and you interact with it in your web browser.</p>

---

## Post #5 by @mcfly3001 (2020-04-16 13:41 UTC)

<p>Hello again,</p>
<p>I did some testing with the vtkMRMLScalarVolumeNode and could finally send out a slice to my client. Unfortunately I found out that this feature works with Slicer 4.8 but is not yet working with the Slicer 4.11 version (did not test 4.10 yet).<br>
I am not so sure though whether this is a known issue or something which should be reported. Also not sure if this something for the OpenIGTLink Extension or the Slicer main app.<br>
Would it help to report the issue? If yes where? Or since this is about a nightly build it not of interest?</p>
<p>Thanks!</p>

---

## Post #6 by @lassoan (2020-04-17 15:17 UTC)

<p>It should work in latest Slicer-4.11. If not then submit a bug report at <a href="https://github.com/openigtlink/SlicerOpenIGTLink/issues">https://github.com/openigtlink/SlicerOpenIGTLink/issues</a>.</p>

---

## Post #7 by @mcfly3001 (2020-04-28 07:13 UTC)

<p>There was another bug in my code so the sending via OpenIGTLink now works correctly and I can receive the image message now.<br>
Unfortunately though, Slicer silently crashes if the image resolution increases. I assume that the copy process is taking too much time, such that the main thread somehow crashes.<br>
In cases where sending the red slice works, I also found that scrolling the MPRs in the red slice is much slower than usual. Would it be possible to shift the sending of the IGTL message to another thread such that scrolling works smoother again? This could also prevent the crash in case of a bigger image.</p>
<p>Here some code what I did to send the red slice. I am creating a vtkWindowToImageFilter and set the render-window ot the red slice as input. Then I create a vtkMRMLScalarVolumeNode and attach the output of the filter as image data. When the red slice was modified I have to manually call Update() and Modified() on the image filter, otherwise the data is not updated and sent. Maybe there is also some bug?</p>
<pre><code class="lang-python">    def _add_slice_view_observers(self, slice_view_name):
        slice_widget = self._layout_manager.sliceWidget(slice_view_name)
        self._slice_widgets[slice_view_name] = slice_widget
        slice_view = slice_widget.sliceView()

        render_window = slice_view.renderWindow()
        slice_logic = slice_widget.sliceLogic()
        self.addObserver(slice_logic, vtk.vtkCommand.ModifiedEvent, self._send_updated_slice)

        wti = vtk.vtkWindowToImageFilter()
        wti.SetInput(render_window)
        wti.Update()
        self._slice_image_data[slice_view_name] = wti

        volume_node = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode")
        self._slice_volume_nodes[slice_view_name] = volume_node
        self._igtl_stream_server.RegisterOutgoingMRMLNode(volume_node)
        volume_node.SetAndObserveImageData(wti.GetOutput())

    def _send_updated_slice(self, caller, event):
        slice_logic = caller  # type: MRMLLogicPython.vtkMRMLSliceLogic
        slice_name = slice_logic.GetName()
        if self._is_streaming and slice_name in self._streaming_slices:
            print('Sending slice:' + slice_logic.GetName())
            wti = self._slice_image_data[slice_name]
            wti.Update()
            wti.Modified()
</code></pre>

---

## Post #8 by @lassoan (2020-04-28 15:24 UTC)

<p>Do you mean crash or hang? Hang (or slowdown) is expected if you do a lot of work on the main thread. Crash should never happen.</p>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> Does OpenIGTLink module in latest master send data in the main thread or in a separate thread?</p>

---

## Post #9 by @Sunderlandkyl (2020-04-28 15:32 UTC)

<p>I believe that data from Slicer should be passed to/from OpenIGTLink on the main thread.</p>

---

## Post #10 by @lassoan (2020-04-28 15:55 UTC)

<p>We could implement background sending in OpenIGTLink module (make a copy of the data and send it on a separate thread), but implementing real-time broadcasting from Slicer is not a priority right now.</p>
<p>You have many options to choose to go forward:</p>
<ul>
<li>implement background sending of images in OpenIGTLink module in Slicer (we’ll be able to help you getting started)</li>
<li>implement your own sending mechanism as a C++ loadable module in Slicer</li>
<li>use/customize these <a href="https://github.com/pieper/SlicerWeb">Slicer web service implementation</a>
</li>
<li>use an existing screen sharing implementation (VNC even has C++, C#, javascript implementations, so it should not be hard to set it up even inside a mobile application)</li>
</ul>
<p>What is your end goal and the workflow that you are trying to implement now?</p>

---

## Post #11 by @mcfly3001 (2020-04-28 16:39 UTC)

<p>If the red slice has lower resolution, scrolling the MPR in the red slice hangs/slows down. If for example I choose red slice only layout, Slicer actually crashes.</p>
<p>Thanks for the many help and suggestions that you proposed. Aim of my project is to create a small prototype for navigation. We plan 3D positions in the MPRs and next want to navigate the surgeon to the planned positions via a tracked tool. Therefore we want to stream the MPRs to a mobile device which is attached to the tracked device.</p>
<p>Concerning my options:</p>
<ul>
<li>Slicer Web Service: Looks interesting to me. This would mean that the client regulary requests an image of a slice. Would this also run in the main thread leading to slow downs? Goal is to have some kind of a stream, so I would repeatedly request an updated image.</li>
<li>VNC: Still not so sure if this would make sense. We do not want to see the full slicer UI. For now we also dont want to use the UI. Would VNC allow to grab red, green or yellow slice only?</li>
</ul>
<p>The other two options might also be worth looking into it.</p>
<p>I also started looking into video streaming. Could you give me a hint how I can switch from sending IMAGE data to VIDEO data? In OpenIGTLinkIF there is a checkbox “UseStreamingVolume”, but this does not seem to change the message type.</p>

---

## Post #12 by @pieper (2020-04-28 17:57 UTC)

<aside class="quote no-group" data-username="mcfly3001" data-post="11" data-topic="10927">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mcfly3001/48/6437_2.png" class="avatar"> mcfly3001:</div>
<blockquote>
<p>Slicer Web Service: Looks interesting to me. This would mean that the client regulary requests an image of a slice. Would this also run in the main thread leading to slow downs? Goal is to have some kind of a stream, so I would repeatedly request an updated image.</p>
</blockquote>
</aside>
<p>Yes, with the current setup the client (browser or other software) requests the data when it wants it, so it can control the timing to match display and networking speeds.  The response does run in the main thread, but the network transmissions are event driven so generally it shouldn’t be too bad.</p>
<p>The other thing the offered by the SlicerWeb approach is structured access to loaded data (like the list of volumes) and the option to add hooks to control Slicer’s behavior from the remote device.</p>

---

## Post #13 by @lassoan (2020-04-28 18:42 UTC)

<aside class="quote no-group" data-username="mcfly3001" data-post="11" data-topic="10927">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mcfly3001/48/6437_2.png" class="avatar"> mcfly3001:</div>
<blockquote>
<p>Slicer actually crashes</p>
</blockquote>
</aside>
<p>Do you mean Slicer not responding or the process exits (does not show up anymore in task manager)?</p>
<aside class="quote no-group" data-username="mcfly3001" data-post="11" data-topic="10927">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mcfly3001/48/6437_2.png" class="avatar"> mcfly3001:</div>
<blockquote>
<p>We do not want to see the full slicer UI. For now we also dont want to use the UI.</p>
</blockquote>
</aside>
<p>It seems that you may be prematurely optimizing things and maybe not the most important ones. Over the years, we have implemented many treatment planning and navigation systems and learnt that in prototyping phase the most important is to be flexible: be able to quickly update your system based on what you learn by using it in practice, add new features, quickly try alternative approaches, etc. Prototyping phase is quite long, it lasts until you have worked out a good workflow, solid software and hardware, and validated their safety and efficacy on about 100 patients at a few sites.</p>
<p>During this phase, there is always an engineer in the room, who needs to be aware what’s happening, what exactly the system is doing, what is shown on the system’s each display, and react promptly to the surgeon’s requests (answer questions, assist with doing something when the surgeon asks for it, adjust views, discover potential issues before they cause any problem, etc.). For this, screen sharing is a good solution - you can use multiple screens, mirror screens or selected windows to remote monitors (surgeon’s console, overhead monitor) and allow control from some of them (e.g., you can allow the surgeon to press buttons on his console). This also comes for free, as you can find remote desktop applications for all platforms. You may even use hardware solutions if you prefer, such as wired or wireless touchscreen displays.</p>
<aside class="quote no-group" data-username="mcfly3001" data-post="11" data-topic="10927">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mcfly3001/48/6437_2.png" class="avatar"> mcfly3001:</div>
<blockquote>
<p>I also started looking into video streaming. Could you give me a hint how I can switch from sending IMAGE data to VIDEO data? In OpenIGTLinkIF there is a checkbox “UseStreamingVolume”, but this does not seem to change the message type.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> can we configure an image connection to send out compressed live image stream?</p>

---

## Post #14 by @Sunderlandkyl (2020-04-28 20:50 UTC)

<p>I’ll make a tutorial for how to configure an outgoing compressed video stream.</p>

---

## Post #15 by @mcfly3001 (2020-04-29 06:42 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="13" data-topic="10927">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Do you mean Slicer not responding or the process exits (does not show up anymore in task manager)?</p>
</blockquote>
</aside>
<p>Slicer process completely exits. The whole UI disappears and also in the task manager slicer.exe is removed. I tested once more by using the ImagerClient3.exe of the OpenIGTLink examples to make sure that the receiver side is as expected. Slicer still crashes if the ImagerClient connects and I change the layout to red slice only. The ImagerClient actually also shuts down with the error message “Message size information and actual data size dont’t match.”.<br>
Maybe during the resize of the red slice widget some inconsistencies occur which lead to the crash? The image renderer maybe also needs to be recreated?<br>
Another observation on this: Simply resizing the whole Slicer application also leads to a resize of the red slice. This works quite well until a certain size has been reached. At a certain size (which again means higher resolution of the red slice) Slicer crashes again.</p>
<aside class="quote no-group" data-username="lassoan" data-post="13" data-topic="10927">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It seems that you may be prematurely optimizing things and maybe not the most important ones.</p>
</blockquote>
</aside>
<p>Maybe that’s a good point. The mobile app already supports navigation features. Streaming the live MPR would be an additional feature which might be valuable for the surgeons. In fact the first step is to evaluate whether attaching a mobile device improves the usability of the navigation system.</p>

---

## Post #16 by @mcfly3001 (2020-04-29 06:42 UTC)

<p>This would be great! Thanks!</p>

---

## Post #17 by @lassoan (2020-04-30 20:30 UTC)

<aside class="quote no-group" data-username="mcfly3001" data-post="15" data-topic="10927">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mcfly3001/48/6437_2.png" class="avatar"> mcfly3001:</div>
<blockquote>
<p>The ImagerClient actually also shuts down with the error message “Message size information and actual data size dont’t match.”</p>
</blockquote>
</aside>
<p>This is useful information. Probably somewhere the error is not handled correctly and that causes the crash. It would be great if you could provide a step-by-step description of how to reproduce it and submit it as a bug report at <a href="https://github.com/openigtlink/SlicerOpenIGTLink/issues" class="inline-onebox">Issues · openigtlink/SlicerOpenIGTLink · GitHub</a>.</p>

---

## Post #18 by @cshreyas (2021-10-11 22:09 UTC)

<p>Hi <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> , was there a tutorial made for configuring outgoing compressed video stream? If so, can you please share the link?<br>
Thanks</p>

---

## Post #19 by @Sunderlandkyl (2021-10-13 13:52 UTC)

<p>Sorry there is no tutorial yet. I’ll make a note to work on it, but it will probably be a while before I can devote time to it.</p>

---

## Post #20 by @cshreyas (2021-10-13 16:22 UTC)

<p>Thanks again.</p>
<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="10927">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<ul>
<li>implement background sending of images in OpenIGTLink module in Slicer (we’ll be able to help you getting started)</li>
<li>implement your own sending mechanism as a C++ loadable module in Slicer</li>
</ul>
</blockquote>
</aside>
<p>I would be interested to implement a loadable module in C++ with one of the approach which was discussed earlier. Can you give me pointers to get started? I would like to send all the 3 planes to the edge device.</p>

---

## Post #21 by @lassoan (2021-10-13 18:27 UTC)

<p>Sending out of OpenIGTLink messages in response to MRML node changes are implemented here:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/openigtlink/SlicerOpenIGTLink/blob/7178920290c24efc88b22be91d6389e99451d214/OpenIGTLinkIF/MRML/vtkMRMLIGTLConnectorNode.cxx#L2239-L2258">
  <header class="source">

      <a href="https://github.com/openigtlink/SlicerOpenIGTLink/blob/7178920290c24efc88b22be91d6389e99451d214/OpenIGTLinkIF/MRML/vtkMRMLIGTLConnectorNode.cxx#L2239-L2258" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/openigtlink/SlicerOpenIGTLink/blob/7178920290c24efc88b22be91d6389e99451d214/OpenIGTLinkIF/MRML/vtkMRMLIGTLConnectorNode.cxx#L2239-L2258" target="_blank" rel="noopener">openigtlink/SlicerOpenIGTLink/blob/7178920290c24efc88b22be91d6389e99451d214/OpenIGTLinkIF/MRML/vtkMRMLIGTLConnectorNode.cxx#L2239-L2258</a></h4>



  <pre class="onebox">    <code class="lang-cxx">
      <ol class="start lines" start="2239" style="counter-reset: li-counter 2238 ;">
          <li>std::vector&lt;int&gt; clientIDs = this-&gt;Internal-&gt;IOConnector-&gt;GetClientIds();</li>
          <li>for (std::vector&lt;int&gt;::iterator clientIDIt = clientIDs.begin(); clientIDIt != clientIDs.end(); ++clientIDIt)</li>
          <li>{</li>
          <li>  int clientID = *clientIDIt;</li>
          <li>  if (clientID == incomingClientID)</li>
          <li>  {</li>
          <li>    // The message was originally received from this client.</li>
          <li>    // We don't need to send it back.</li>
          <li>    continue;</li>
          <li>  }</li>
          <li>
          </li>
<li>  if ((strcmp(node-&gt;GetClassName(), "vtkMRMLIGTLQueryNode") != 0))</li>
          <li>  {</li>
          <li>    this-&gt;Internal-&gt;IOConnector-&gt;SendMessage(key, igtlioDevice::MESSAGE_PREFIX_NOT_DEFINED, clientID);</li>
          <li>  }</li>
          <li>  else if (strcmp(node-&gt;GetClassName(), "vtkMRMLIGTLQueryNode") == 0)</li>
          <li>  {</li>
          <li>    this-&gt;Internal-&gt;IOConnector-&gt;SendMessage(key, device-&gt;MESSAGE_PREFIX_RTS, clientID);</li>
          <li>  }</li>
          <li>}</li>
      </ol>
    </code>
  </pre>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>You could probably leave this code mostly as is (just add an option to send output messages asynchronously), and update the <code>SendMessage</code> method implementation in OpenIGTLinkIO to support asynchronous sending (make a copy of the message buffer, put it in a queue, and in a separate thread get the items from the queue and send them).</p>
<p>Before you start this, you need to build Slicer and SlicerOpenIGTLink extension. It would also make sense to do some profiling and fix the crash before you start developing the asynchronous message sending, so probably a RelWithDebInfo mode build would make the most suitable.</p>

---

## Post #22 by @cshreyas (2021-10-13 18:36 UTC)

<p>Thanks Andras for the inputs. Will try it out.</p>

---
