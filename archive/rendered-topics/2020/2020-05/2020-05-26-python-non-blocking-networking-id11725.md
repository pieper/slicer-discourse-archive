---
topic_id: 11725
title: "Python Non Blocking Networking"
date: 2020-05-26
url: https://discourse.slicer.org/t/11725
---

# Python non-blocking networking

**Topic ID**: 11725
**Date**: 2020-05-26
**URL**: https://discourse.slicer.org/t/python-non-blocking-networking/11725

---

## Post #1 by @talmazov (2020-05-26 23:45 UTC)

<p>Hey all,<br>
I’ve been pretty successful writing this socket client on slicer. it works but it is not responsive receiving the data, i imagine it is an issue with threading and blocking<br>
i start my client via a thread</p>
<pre><code>def start():
    asyncore.loop()
    
def init_thread(run):
    new_thread = threading.Thread() # create a new thread object.
    new_thread.run = run
    new_thread.start()

class EchoClient(asyncore.dispatcher): ...

socket_obj = EchoClient(address[0], address[1])
init_thread(start)
</code></pre>
<p>but this doesn’t seem to be working very well, which i anticipated but hoped to not be the case. I am using asyncore for networking, and starting the client/server in a threaded loop. Any recommendation on how to do multiprocessing/threading or asynchronous networking in 3d slicer?</p>
<p>Thanks!</p>

---

## Post #2 by @pieper (2020-05-27 00:04 UTC)

<p>Hi -</p>
<p>I looked at async python, but didn’t see a good way to integrate it cleanly with the Qt event loop.</p>
<p>Fortunately Qt provides a QSocketNotifier class, which provides a signals/slots interface to socket events for connections, readable, and writable state changes.  I’ve been using it for a while in the <a href="https://github.com/pieper/SlicerWeb/blob/master/WebServer/WebServer.py#L1479">SlicerWeb/WebServer.py code</a>.  I think this is the cleanest way to do it.</p>

---

## Post #3 by @lassoan (2020-05-27 00:24 UTC)

<p>If you want to send/receive images, transforms, models or control remote hardware/software in real-time then another option is OpenIGTLink (via SlicerOpenIGTLink extension). We have interfaces implemented for real-time data exchange with various medical imaging devices, surgical navigation systems, position trackers, sensors, haptic devices, etc. If OpenIGTLink interface is not yet available for all the external device/software that you want to use then it is not hard to implement it, as OpenIGTLink is a very simple simple socket-based protocol. We already have many modules (mainly in <a href="http://www.slicerigt.org/wp/">SlicerIGT extension</a>) that works very nicely with OpenIGTLink - you can reslice a volume with positions you receive from an external position tracker, reconstruct volume from tracked slices, display information for real-time surgical tool navigation, etc.</p>
<p>What is your use case? What information you would like to exchange, with what hardware/software?</p>

---

## Post #4 by @talmazov (2020-05-29 02:41 UTC)

<p>the WebServer example was amazing, just what I needed. I managed to work this out [lines 19-90]<br>
</p><aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/dentsoft-foundation/linkSlicerBlender/blob/socket/slicer_link/slicer_module/comm/asyncsock.py" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/dentsoft-foundation/linkSlicerBlender/blob/socket/slicer_link/slicer_module/comm/asyncsock.py" target="_blank" rel="nofollow noopener">dentsoft-foundation/linkSlicerBlender/blob/socket/slicer_link/slicer_module/comm/asyncsock.py</a></h4>
<pre><code class="lang-py"># REFERENCES:
# https://pymotw.com/2/asynchat/
# tuple unpacking https://stackoverflow.com/questions/1993727/expanding-tuples-into-arguments
# https://pymotw.com/2/asyncore/

import asyncore

import logging
import socket
import threading #would multiprocessing be better?
import time


packet_terminator = '\nEND_TRANSMISSION\n\n'
socket_obj = None
thread = None
address = ('localhost', 5959)

class SlicerComm():
    #https://github.com/pieper/SlicerWeb/blob/master/WebServer/WebServer.py#L1479 adapted from, using QSocketNotifier class
</code></pre>

  This file has been truncated. <a href="https://github.com/dentsoft-foundation/linkSlicerBlender/blob/socket/slicer_link/slicer_module/comm/asyncsock.py" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>something i noticed that i am not sure is normal or not. When i create the socket and start it then connecting QSocketNotifier Read to activate seems to put the socket thread in some kind of a loop that puts one of my CPU core utilization 100%, slicer runs on a separate core well. the core utilization goes down when i disconnect QSocketNotifier read but then i can’t poll for incoming data…<br>
am i not using QSocketNotifier correctly? am i suppose to connect/activate the event manually? if so how can i poll for incoming data without putting the CPU core to 100% utilization?</p>
<p>thanks!</p>

---

## Post #5 by @lassoan (2020-05-29 03:05 UTC)

<p>Probably you need to put in a short sleep in the polling loop. See for example <a href="https://stackoverflow.com/questions/22423625/python-asyncore-using-100-cpu-after-client-connects">here</a>.</p>

---

## Post #6 by @talmazov (2020-05-30 00:53 UTC)

<p>i found QTcpSocket() to work really well!!!<br>
here is the final implementation, CPU utilization is great as well as response time <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=9" title=":smiley:" class="emoji" alt=":smiley:"><br>
thanks for all your help guys!</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/dentsoft-foundation/linkSlicerBlender/blob/socket/slicer_link/slicer_module/comm/asyncsock.py" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/dentsoft-foundation/linkSlicerBlender/blob/socket/slicer_link/slicer_module/comm/asyncsock.py" target="_blank" rel="nofollow noopener">dentsoft-foundation/linkSlicerBlender/blob/socket/slicer_link/slicer_module/comm/asyncsock.py</a></h4>
<pre><code class="lang-py"># REFERENCES:
# https://pymotw.com/2/asynchat/
# tuple unpacking https://stackoverflow.com/questions/1993727/expanding-tuples-into-arguments
# https://pymotw.com/2/asyncore/

import asyncore

import logging
import socket
import threading #would multiprocessing be better?
import time


packet_terminator = '\nEND_TRANSMISSION\n\n'
socket_obj = None
thread = None
address = ('localhost', 5959)

class SlicerComm():
    #https://github.com/pieper/SlicerWeb/blob/master/WebServer/WebServer.py#L1479 adapted from, using QSocketNotifier class
</code></pre>

  This file has been truncated. <a href="https://github.com/dentsoft-foundation/linkSlicerBlender/blob/socket/slicer_link/slicer_module/comm/asyncsock.py" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
