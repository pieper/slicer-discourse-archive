---
topic_id: 30158
title: "Update 3D Visualization Programmatically"
date: 2023-06-20
url: https://discourse.slicer.org/t/30158
---

# Update 3D Visualization programmatically

**Topic ID**: 30158
**Date**: 2023-06-20
**URL**: https://discourse.slicer.org/t/update-3d-visualization-programmatically/30158

---

## Post #1 by @marm (2023-06-20 16:52 UTC)

<p>Hi,</p>
<p>First of all, thank you for your effort in developing 3DSlicer as it is a great platform.</p>
<p>I am developing a 3DSlicer module for surgical tool navigation. I want to update the 3D visualization of a model every time I get a new transform matrix of the tool geometrical model. I am getting a new transform from an OPCUA server periodically.</p>
<p>Currently, I am able to update the visualization as desired <strong>only</strong> when I actively hover the mouse over the multiplanar reconstruction slices (RGY).<br>
I suspect there is a connection with the DataProbe and the CrosshairNode events that are fired during this interaction with the slices, but I cannot identify what I potentially could use from <em>DataProbe.py</em>.<br>
Find the GIF attached as a clarification of what I explained above. The movement is kind of fast because I get a new transform every 100ms.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d2c7bfde8945d2d8b16e141dc3b566d105cf162.gif" alt="tool_moving" data-base62-sha1="difI8ZEs3OLY1ZDoJC8UqiBvbnc" width="690" height="468" class="animated"></p>
<p>Are there any events or event-related callbacks I can trigger for updating the 3D visualization as described? This is, every time I get a new transform. Which would be the “correct” way or the recommended practice for this? I would greatly appreciate your help <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>Thanks!</p>
<p>Marm.</p>

---

## Post #2 by @mikebind (2023-06-20 17:57 UTC)

<p>Take a look at Slicer IGT: <a href="https://www.slicerigt.org/wp/" class="inline-onebox" rel="noopener nofollow ugc">SlicerIGT | toolkit for navigated interventions</a></p>
<p>This displaying tracked objects is exactly what Slicer IGT is designed for.  Likely you can just use Slicer IGT directly, but even if you want to create your own version, you may find inspiration in how Slicer IGT gets the view to update.</p>

---

## Post #3 by @marm (2023-06-21 06:56 UTC)

<p>Hi mikebind,</p>
<p>Thank you for your reply. We already explored the possibility of utilizing SlicerIGT and SlicerIGTLink, but unfortunately, we are constrained to using an OPCUA protocol to communicate between Slicer and the rest of the elements of our application. This prevents us from using the alternative you suggested. I will look for any useful bits of code in the SlicerIGT codebase, but I think this will be excruciatingly slow until I come up with something.</p>
<p>I am still in search of a way to update the visualization automatically with native 3DSlicer functions, without relying on external modules.<br>
I forgot to add that I already tried with <code>slicer.app.processEvents()</code> but it does not do the trick for me.</p>

---

## Post #4 by @rbumm (2023-06-21 09:02 UTC)

<p>Does</p>
<pre><code class="lang-auto">yourSegmentation.CreateClosedSurfaceRepresentation()
</code></pre>
<p>not do the job?</p>

---

## Post #5 by @rbumm (2023-06-21 09:12 UTC)

<aside class="quote no-group" data-username="marm" data-post="1" data-topic="30158">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/marm/48/66504_2.png" class="avatar"> marm:</div>
<blockquote>
<p>I am developing a 3DSlicer module for surgical tool navigation. I want to update the 3D visualization of a model every time I get a new transform matrix of the tool geometrical model. I am getting a new transform from an OPCUA server periodically.</p>
<p>Currently, I am able to update the visualization as desired <strong>only</strong> when I actively hover the mouse over the multiplanar reconstruction slices (RGY).<br>
I suspect there is a connection with the DataProbe and the CrosshairNode events that are fired during this interaction with the slices, but I cannot identify what I potentially could use from <em>DataProbe.py</em>.<br>
Find the GIF attached as a clarification of what I explained above. The movement is kind of fast because I get a new transform every 100ms.</p>
</blockquote>
</aside>
<p>Maybe this GPT-4 response is interesting to you:</p>
<p>"<br>
In 3D Slicer, updating the visualization of a model usually involves two primary steps:</p>
<ol>
<li>Update the transform matrix associated with the model.</li>
<li>Invoke the render function to refresh the visualization.</li>
</ol>
<p>If your model only updates when you hover over the multiplanar reconstruction slices (RGB), it may indeed be related to events triggered by DataProbe.py or CrosshairNode interactions, which are likely causing a render update.</p>
<p>Here’s a hypothetical scenario: if your OPCUA server updates the transform every 100ms, but the render update happens less frequently (only when you interact with the slices), then the visualization will seem to only update during those interactions.</p>
<p>To solve this problem, you could consider the following approaches:</p>
<ol>
<li>
<p><strong>Manual Rendering:</strong> Whenever you receive a new transform matrix, not only should you update the matrix, but you should also explicitly call the render function to refresh the visualization. In VTK (the visualization library that 3D Slicer is built upon), this can typically be done using the <code>Render()</code> method.</p>
</li>
<li>
<p><strong>Observer Pattern:</strong> If your problem is indeed related to certain events, you can leverage the observer pattern. Create an observer that listens for changes in the transform matrix and calls the rendering function whenever an update is received. In VTK and 3D Slicer, this could be accomplished using the <code>AddObserver()</code> method with an appropriate event like <code>vtkCommand::ModifiedEvent</code> or <code>vtkMRMLTransformableNode::TransformModifiedEvent</code>.</p>
</li>
<li>
<p><strong>Check for DataProbe.py or CrosshairNode Events:</strong> If you suspect these components are causing the updates, review their event logic to see if there’s an event you can leverage to trigger the rendering of your model more frequently.</p>
</li>
</ol>
<p>Please keep in mind that calling the render function too frequently can consume considerable computational resources, potentially slowing down your module or even the whole 3D Slicer application. You’ll need to balance the need for fast updates with the performance requirements of your module and 3D Slicer.<br>
"</p>

---

## Post #6 by @marm (2023-06-22 11:36 UTC)

<p>Hi Rudolf,</p>
<p>Thank you so much for your reply.</p>
<p>I tried this approach:</p>
<blockquote>
<p>yourSegmentation.CreateClosedSurfaceRepresentation()</p>
</blockquote>
<p>Unfortunately, it does not work, because my tool is represented by a Model and thus it is not a LabelMap node. Thanks for the suggestion, though.</p>
<p>Regarding the GPT-4 response you provided, I tried the 3 possible solutions, but none of them worked for me.</p>
<p>I think I may have identified the origin of the problem but I do not know how to solve it. I’ll try to provide additional context so the problem is described more in-depth:</p>
<p>I am receiving the new tool transform via an OPCUA connection, using the <em>asyncua</em> Python library. My bad I forgot to mention that I am developing my module in Python.<br>
The transform is received in the 3DSlicer module by subscribing the client (3DSlicer) to a variable of the OPCUA Server, which holds the data I am interested in (the tool transform). Whenever this variable changes in the server, the client should enter a function called “datachange_notification” which is in charge of updating the model properties. I noticed that the execution does not enter “datachange_notification” until I manually interact with the mentioned slices by hovering the mouse over them.<br>
I suspect that <em>asyncua</em> has a thread being blocked, which cannot advance until I trigger some kind of event/interaction with the GUI. I want to unblock this automatically, without interacting with the GUI, so the 3D visualization is updated in real-time, automatically.</p>
<p>Find below attached a sample Python Interactor message whenever 3DSlicer detects a change in the variable which is subscribed to:</p>
<p>This is returned when I open the connection, no GUI interaction needed:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a9eef193f807ebfd8618d8cf01b0565fb25b0fe8.png" data-download-href="/uploads/short-url/ofiCRYAhhRijP0BLtJS62V12P7a.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a9eef193f807ebfd8618d8cf01b0565fb25b0fe8_2_690x110.png" alt="image" data-base62-sha1="ofiCRYAhhRijP0BLtJS62V12P7a" width="690" height="110" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a9eef193f807ebfd8618d8cf01b0565fb25b0fe8_2_690x110.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a9eef193f807ebfd8618d8cf01b0565fb25b0fe8_2_1035x165.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a9eef193f807ebfd8618d8cf01b0565fb25b0fe8_2_1380x220.png 2x" data-dominant-color="2A2A29"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1894×304 168 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>And this message is returned by the interaction after setting up the connection when I interact with the GUI:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d93042cce9b165d0e3be5217b4c20b7582b759a.png" data-download-href="/uploads/short-url/dlNnUMKUr8ZcvA7FNmMoRcrrWl4.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d93042cce9b165d0e3be5217b4c20b7582b759a_2_690x67.png" alt="image" data-base62-sha1="dlNnUMKUr8ZcvA7FNmMoRcrrWl4" width="690" height="67" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d93042cce9b165d0e3be5217b4c20b7582b759a_2_690x67.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d93042cce9b165d0e3be5217b4c20b7582b759a_2_1035x100.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d93042cce9b165d0e3be5217b4c20b7582b759a_2_1380x134.png 2x" data-dominant-color="323232"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1887×185 160 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>All the lines in the interactor without a “[Python]” are explicitly printed from my code.</p>
<p>I hope someone can help me with this problem, thanks in advance <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>Marm.</p>

---

## Post #7 by @rbumm (2023-06-22 12:22 UTC)

<p>An approach would be (my brain <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> ) to use a QTimer in your main thread that periodically checks for updates in your tool transform and refreshes the GUI. <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#show-volume-rendering-automatically-when-a-volume-is-loaded">See a QTimer example here</a>.</p>

---

## Post #8 by @rbumm (2023-06-22 12:24 UTC)

<p>Or (suggested by GPT-4) you could define a Qt signal in your main thread that’s connected to a slot function responsible for updating the model in the GUI. You emit this signal from your asyncua callback function, and thanks to Qt’s queued connections, the slot function will be executed in the main thread. Qt’s signal-slot system is thread-safe, and it ensures that the GUI updates are performed in the correct thread.</p>
<p>Probably not working, GPT ! … if the asyncua callback function does not work.</p>
<p>So I would try the Timer.</p>

---

## Post #9 by @pieper (2023-06-22 13:36 UTC)

<p>I agree with <a class="mention" href="/u/rbumm">@rbumm</a> that a QTimer based solution should work.  Ideally though the application should be fully event driven so that operating system level activity wakes up the application when there’s work to be done.  Timers are a kind of “busy loop” that can be inefficient.</p>
<p>Slicer uses Qt’s event loop, while python’s asyncio introduces a different event loop.  Generally Qt’s is sufficient and you might be able to use something like <a href="https://doc.qt.io/qt-5/qsocketnotifier.html">QSocketNotifier</a> if you’re getting your data via a network connection.  If you really need to use both event loops you may explore something like <a href="https://github.com/CabbageDevelopment/qasync">qasync</a> but I don’t know if it’s been used in Slicer.</p>
<p>Report back and let us know what you figure out.</p>

---

## Post #10 by @cpinter (2023-06-22 13:40 UTC)

<p>Based on the gif you attached the parent transform of the model is changed as expected. So what I assume is that the needle model node has a parent transform, the matrix of which is updated from the data received from OPCUA. This transform modification should be enough to trigger rendering I think. As a test and possible workaround, can you call <code>Modified()</code> on the needle model’s display node?</p>

---

## Post #11 by @lassoan (2023-06-25 17:48 UTC)

<p>I would recommend to write a small component that converts from OPCUA to OpenIGTLink. The simplest is probably to write it in Python - receive messages using python-opcua and send them using <a href="https://pypi.org/project/pyigtl/">pyigtl</a>. The entire implementation may be just 5-10 lines. Since this bridge runs in simple while loop in a separate process, you don’t need to deal with events, timers, multithreading, etc.</p>

---

## Post #12 by @marm (2023-07-06 18:31 UTC)

<p>Hello,</p>
<p>Thanks to everyone that participated in the topic trying to provide solutions to the issue. I tried many of your suggestions but I could not make any of them work. Sorry for the late reply, I have been on a long-awaited vacation.</p>
<aside class="quote no-group" data-username="rbumm" data-post="7" data-topic="30158">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>An approach would be (my brain <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> ) to use a QTimer in your main thread</p>
</blockquote>
</aside>
<p>Regarding QTimers, conceptually they do not meet the requirements of our use case, as they need to match the refresh rate of the server. We did not contemplate using them and another side project that used them brought problems to our application. In addition, we want to work fully event-driven, so as <a class="mention" href="/u/pieper">@pieper</a> pointed out, this could be inefficient.</p>
<aside class="quote no-group" data-username="cpinter" data-post="10" data-topic="30158">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>As a test and possible workaround, can you call <code>Modified()</code> on the needle model’s display node?</p>
</blockquote>
</aside>
<p>I tried it but it did not work, thank you for your suggestion though!</p>
<aside class="quote no-group" data-username="pieper" data-post="9" data-topic="30158">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Generally Qt’s is sufficient and you might be able to use something like <a href="https://doc.qt.io/qt-5/qsocketnotifier.html" rel="noopener nofollow ugc">QSocketNotifier</a> if you’re getting your data via a network connection. If you really need to use both event loops you may explore something like <a href="https://github.com/CabbageDevelopment/qasync" rel="noopener nofollow ugc">qasync</a> but I don’t know if it’s been used in Slicer.</p>
</blockquote>
</aside>
<p>As for using QSocketNotifier, I could not achieve the object to “listen” to the server socket. The app does not show any render changes until I manually interact with the slice views. Perhaps I did not correctly configure the QSocketNotifier.</p>
<aside class="quote no-group" data-username="lassoan" data-post="11" data-topic="30158">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I would recommend to write a small component that converts from OPCUA to OpenIGTLink.</p>
</blockquote>
</aside>
<p>We found this as the best fit for our use case, but we did not fully comprehend your suggestion, <a class="mention" href="/u/lassoan">@lassoan</a>. Is the component running in our custom Slicer module? How are OPCUA messages translated to OpenIGTLink? We are constrained to using OPCUA as the main communication protocol between our system and the Slicer module. Could you extend on your answer please? <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>After some thought, we arrived at a possible solution. We could launch a <em>separate process</em> from our custom Slicer module that receives the OPCUA messages and translates them to OpenIGTLink, so they can be forwarded to the main process of the Slicer application. Using pyigtl, we could receive these messages. Is this close to what you were trying to convey? Do you find it feasible?</p>
<p>Again, thank you all for your help!</p>
<p>Marm</p>

---

## Post #13 by @lassoan (2023-07-06 18:44 UTC)

<aside class="quote no-group" data-username="marm" data-post="12" data-topic="30158">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/marm/48/66504_2.png" class="avatar"> marm:</div>
<blockquote>
<p>Is the component running in our custom Slicer module?</p>
</blockquote>
</aside>
<p>It is simpler if it runs in a separate Python process (it can be PythonSlicer.exe, started by your Slicer module).</p>
<aside class="quote no-group" data-username="marm" data-post="12" data-topic="30158">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/marm/48/66504_2.png" class="avatar"> marm:</div>
<blockquote>
<p>How are OPCUA messages translated to OpenIGTLink?</p>
</blockquote>
</aside>
<p>You receive an OPCUA message, create an OpenIGTLink message from its content, and send it.</p>
<aside class="quote no-group" data-username="marm" data-post="12" data-topic="30158">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/marm/48/66504_2.png" class="avatar"> marm:</div>
<blockquote>
<p>Using pyigtl, we could receive these messages. Is this close to what you were trying to convey? Do you find it feasible?</p>
</blockquote>
</aside>
<p>I meant exactly this. It is not just feasible but really simple, too. The script is probably 10-20 lines of Python code.</p>

---

## Post #14 by @marm (2023-07-06 18:48 UTC)

<p>Thanks again for the quick reply and for extending the explanation. Now we have a better idea of the implementation. It looks very promising.</p>
<p>We will work on this and report back with the results.</p>

---

## Post #15 by @marm (2023-07-10 12:28 UTC)

<p>Hello again, <a class="mention" href="/u/lassoan">@lassoan</a><br>
<br>
I created a small IGTL server-client pair based on the examples of <code>pyigtl</code>.</p>
<p>Server side code:</p>
<pre><code class="lang-auto">import pyigtl

from time import sleep
import numpy as np

server = pyigtl.OpenIGTLinkServer(port=18944, local_server=False)
print(f"Starting server at: {server.host}:{server.port}")

timestep = 0
while True:
    if not server.is_connected():
        # Wait for client to connect
        sleep(0.1)
        continue
    print("Server connected")
    # Generate transform
    timestep += 1

    # Send transform
    transform = np.random.rand(4, 4) @ np.eye(4)
    print(f"time: {timestep}   transform: ({transform.ravel()})")
    transform_message = pyigtl.TransformMessage(transform, device_name="MyTransform")
    server.send_message(transform_message, wait=True)
    sleep(1)
    # Since we wait until the message is actually sent, the message queue will not be flooded
</code></pre>
<p><br>
<br>
And client-side code:</p>
<pre><code class="lang-auto">import pyigtl  # pylint: disable=import-error
import socket


client = pyigtl.OpenIGTLinkClient(host=socket.gethostbyname(socket.gethostname()), port=18944)
# Get transform
input_message = client.wait_for_message("MyTransform", timeout=-1)
print(input_message)
</code></pre>
<p><br>
<br>
My intention was to construct the communication like so, as we previously discussed:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fb4a637f8574980fe82dfb20dee035b68c802cf1.png" data-download-href="/uploads/short-url/zR1dLBtzUzzXex88nDKBni5S25j.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fb4a637f8574980fe82dfb20dee035b68c802cf1_2_690x232.png" alt="image" data-base62-sha1="zR1dLBtzUzzXex88nDKBni5S25j" width="690" height="232" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fb4a637f8574980fe82dfb20dee035b68c802cf1_2_690x232.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fb4a637f8574980fe82dfb20dee035b68c802cf1_2_1035x348.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fb4a637f8574980fe82dfb20dee035b68c802cf1.png 2x" data-dominant-color="DFE0E7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1241×418 44.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<br>
After starting the server and client pair, each in a different Python process, on the client side, the execution gets halted in the line that defines <code>input_message</code>. If I adjust the timeout to a value other than <code>-1</code>, the client receives the message once, and the execution finishes. In 3DSlicer, I want to update the transform every time I get the message, and I do not wish the module to hang in the line that defines <code>input_message</code>.<br>
In addition, I do not want to use 3DSlicer’s IGTLinkF module, I would like to manage the connection entirely from the code of my module. Can IGTLinkF’s logic be replicated using <code>pyigtl</code>?</p>
<p>Thank you,</p>
<p>Marm</p>

---

## Post #16 by @lassoan (2023-07-10 13:08 UTC)

<aside class="quote no-group" data-username="marm" data-post="15" data-topic="30158">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/marm/48/66504_2.png" class="avatar"> marm:</div>
<blockquote>
<p>In addition, I do not want to use 3DSlicer’s IGTLinkF module, I would like to manage the connection entirely from the code of my module. Can IGTLinkF’s logic be replicated using <code>pyigtl</code>?</p>
</blockquote>
</aside>
<p>I don’t think it is feasible to match the performance of the OpenIGTLinkIF module in Slicer using Python scripting. OpenIGTLinkIF module is a result of over 15 years of development, usage, and optimization on many projects, on all supported operating systems. You can decide to implement a new Python scripted module for this, but then of course we won’t be able to help you with that.</p>

---

## Post #17 by @marm (2023-07-11 08:29 UTC)

<p>I understand. Thank you for your reply.</p>
<p>On the other hand, is there any way to access the IGTLinkF logic from Python? This way I could use its functionality from my code. The ultimate objective would be to eliminate the user interaction with the IGTLinkF module, and only use our custom module.</p>
<p>Sorry that I formulated my question poorly in my previous post, this is what I meant.</p>

---

## Post #18 by @lassoan (2023-07-11 11:34 UTC)

<p>Yes, if course your can use OpenIGTLinkIF from Python. Typically all you need to do is to add a connector node to the scene and adjust its properties.</p>

---

## Post #19 by @marm (2023-08-11 11:15 UTC)

<p>Hi again,</p>
<p>We finally managed to get the communication up and running fluently, and it runs super smoothly! I would like to express my biggest gratitude to all the people that contributed to solving our problem <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>In case anyone faces the same problem (or a similar one) find below a summarized description of how we implemented the solution:</p>
<p>The architecture is described in a diagram in one of my previous replies:</p>
<aside class="quote no-group" data-username="marm" data-post="15" data-topic="30158">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/marm/48/66504_2.png" class="avatar"> marm:</div>
<blockquote>
<p>My intention was to construct the communication like so, as we previously discussed:</p>
</blockquote>
</aside>
<ul>
<li>
<p>Every time a new connection is requested to be opened from the custom 3DSlicer module, a new process that runs the <code>OPCUAtoIGTL</code> translator is launched from it, using <code>slicer.util.launchConsoleProcess(commandOfInterest)</code>.<br>
<code>commandOfInterest</code> is built concatenating the PythonSlicer.exe path (in the case of Windows systems), the absolute path to the <code>OPCAtoIGTL</code> translator script, and the necessary CLI arguments that are fed to it.</p>
</li>
<li>
<p>The <code>OPCUAtoIGTL</code> translator does the following:<br>
–It receives the OPCUA ServerIP and port, and the IGTL Server port as CLI arguments. Then it parses them.<br>
– After parsing, an OPCUA client is set up (not connected yet) to connect to the OPCUA Server.<br>
– The IGTLink Server is initiated in <code>127.0.0.1:&lt;parsedPortNumber&gt;</code><br>
– Only, and only when the IGTLink Server is connected to the IGTLink client (which is set up in the Custom 3DSlicer Module), the OPCUA Client connects to the OPCUA Server.<br>
– The OPCUA Client subscribes to a variable of interest, which the OPCUA Server is constantly updating. The variable value is processed in the OPCUAtoIGTL translator (so, actually, it is translated)<br>
– To avoid flooding any buffers and 3DSlicer hanging without updating the transform, (this happened to me), the IGTL Server sends an update every 100ms, which is an acceptable frame rate for navigation purposes.</p>
</li>
</ul>
<p>If the user wants to close the connection, the OPCUAtoIGTL process is killed, and the IGTL Client is deleted in the 3DSlicer scene. This way the process list and the scene node tree remain clean.</p>
<p>Feel free to message me in case you need more details. Special thanks again to <a class="mention" href="/u/lassoan">@lassoan</a> for the help <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>Marm</p>

---

## Post #20 by @lassoan (2023-08-11 13:27 UTC)

<p>Thanks for the update, it is great to hear that everything worked out well!</p>
<p>In case someone else wants to connect Slicer to OPCUA (or similar protocol) - could you post here the link to the github repository of your OPCUAtoIGTL translator Python script?</p>

---

## Post #21 by @marm (2023-08-31 10:37 UTC)

<p>Thank you again for your help and replies!</p>
<p>For privacy reasons, I am not allowed to share the whole repository. I am sorry <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=12" title=":frowning:" class="emoji" alt=":frowning:" loading="lazy" width="20" height="20"><br>
However, I can provide a piece of code that could serve as a guideline for anyone interested. The OpcuaCommProxy is just a wrapper for using <em>asyncua</em> OPCUA connections with less verbosity.</p>
<p>The code is not clean, not optimum and it is also not efficient because this was created for a prototype, so feel free to criticize it as it has a lot of room to improve <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<pre><code class="lang-auto">#
# Description: Creates a OPCUA client that gets messages from a given OPCUA host, translates them to the IGTLink protocol and sends them to Slicer.
# via a IGTLink server.
#
import sys
import argparse
from time import sleep
import socket

import numpy as np
import pyigtl
from asyncua import Node

###################################
from opcua_robot_comm.opcuacommproxy import OpcuaCommProxy ##(I CANNOT SHARE THIS)
###################################

ras2lps = np.identity(4)
ras2lps[0, 0] = -1.0
ras2lps[1, 1] = -1.0
lps2ras = np.linalg.inv(ras2lps)
# Hardcoded registration matrix from A to B
lps_a_t_b = np.array(#some 4x4 homogeneous matrix)
ras_a_t_b = ras2lps @ lps_a_t_b @ lps2ras


# Define SubscriptionHandler
class SubscriptionHandler:
    """
    The SubscriptionHandler is used to handle the data that is received for the subscription.
    """

    val = None

    def __init__(self, igtl_server):
        self.igtl_server = igtl_server

    def datachange_notification(self, node: Node, val, data):
        """
        Callback for asyncua Subscription.
        This method will be called when the Client received a data change message from the Server.
        """
        self.val = val
        # Send transform matrix
        self._update_tool_transform()

    def _updateg_tool_transform(self):
        """
        Sends a tool transform to the IGTLink server.
        """
        # Send transform matrix
        try:
            mat = np.array(self.val)
            mat = np.reshape(mat, (4, 4))
            self.mat = mat
        except KeyboardInterrupt:
            print("Program terminated by User")
            sys.exit()


if __name__ == "__main__":
    # Define arguments for the OPCUA-IGTL bridge
    argparser = argparse.ArgumentParser()
    default_opcua_address = socket.gethostbyname(socket.gethostname())
    default_igtl_address = "127.0.0.1"
    argparser.add_argument("--opcua_host", default=default_opcua_address, help="OPCUA Host to connect to")
    argparser.add_argument("--opcua_port", default=4840, help="OPCUA Port to connect to")

    argparser.add_argument("--igtl_port", default=18944, help="IGTL Port to connect to")

    # Parse arguments and organize them
    args = argparser.parse_args()
    opcua_host = args.opcua_host
    opcua_port = args.opcua_port
    igtl_port = args.igtl_port

    # Create the OPCUA Client
    opcua_client = OpcuaCommProxy("opc.tcp://" + opcua_host + ":" + str(opcua_port))

    # Create the IGTLink server and connect to the client
    igtl_server = pyigtl.OpenIGTLinkServer(
        igtl_port,
        local_server=True,
    )

    print(f"Started IGTL server at: {igtl_server.host}:{igtl_server.port}")
    sig = True

    # Wait for IGTL client to connect to our server
    while not igtl_server.is_connected():
        sleep(0.1)

    # Connect to the OPCUA server once the IGTL client is connected
    opcua_client.connect()
    subs_handler = SubscriptionHandler(igtl_server=igtl_server)
    opcua_client.subscribe_to_var("ns=YourNameSpaceNumber;s=YourOPCUAVariableName", subs_handler)

    print("[IGTL Translator] Server connected to client")

    # Keep running as long as the server is connected or the user interrupts the program with Ctrl+C
    while sig:
        try:
            if igtl_server.is_connected():
                try:
                    mat = subs_handler.mat
                except AttributeError:
                    mat = np.eye(4)

                # Transform LPS to RAS
                mat = np.linalg.inv(lps2ras @ ras_a_t_b) @ mat

                # Send tool transform
                # This is not in the datachange notification to prevent too many events from being sent in the OPCUA
                # event loop. We send it every 0.1 seconds instead.
                transform_message = pyigtl.TransformMessage(mat, device_name=r"tool_transform") # The device name has a limit of 20 characters, be careful with this, or you will receive cut names at the 20th character.
                # print(f"Sending transform: {mat}")
                igtl_server.send_message(transform_message, wait=False)
                print(f"Sent message {mat}")
                sleep(0.1)

            else:
                sig = False
                print("Connection interrupted")
        except KeyboardInterrupt:
            sig = False
            print("Program terminated by User")

    print("Terminated")
    # Force program termination
    sys.exit()
</code></pre>

---

## Post #22 by @lassoan (2023-09-01 12:19 UTC)

<p>Thank you, this script can be very useful for others who want to interface with OPC UA components in Slicer.</p>

---
