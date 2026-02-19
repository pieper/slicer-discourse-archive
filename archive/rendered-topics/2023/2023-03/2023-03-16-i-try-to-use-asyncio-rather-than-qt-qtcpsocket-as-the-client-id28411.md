---
topic_id: 28411
title: "I Try To Use Asyncio Rather Than Qt Qtcpsocket As The Client"
date: 2023-03-16
url: https://discourse.slicer.org/t/28411
---

# I try to use asyncio rather than qt.QTcpSocket as the client, but the socket can receive msgs only if the mouse is hovering the the Slicer UI

**Topic ID**: 28411
**Date**: 2023-03-16
**URL**: https://discourse.slicer.org/t/i-try-to-use-asyncio-rather-than-qt-qtcpsocket-as-the-client-but-the-socket-can-receive-msgs-only-if-the-mouse-is-hovering-the-the-slicer-ui/28411

---

## Post #1 by @derekcbr (2023-03-16 07:43 UTC)

<pre><code class="lang-auto">import asyncio

async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888)

    print(f'Send: {message!r}')
    writer.write(message.encode())
    await writer.drain()

    data = await reader.read(100)
    print(f'Received: {data.decode()!r}')

    print('Close the connection')
    writer.close()
    await writer.wait_closed()

asyncio.run(tcp_echo_client('Hello World!'))
</code></pre>
<p>But this seems not be able to automatically get the messages from the server side.</p>
<pre><code class="lang-auto">loop = qt.QEventLoop()
asyncio.set_event_loop(loop)
</code></pre>
<p>Can I use the above to get qt eventloop to get the messages from the server automatically? Thanks!</p>

---

## Post #2 by @pieper (2023-03-16 13:21 UTC)

<p>I haven’t seen a general purpose way to use our Qt event loop with asyncio, so if you or anyone here has a good solution please post it.</p>
<p>The <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/webserver.html">WebServer</a> module in Slicer <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/WebServer/WebServer.py#L492">uses</a> the <a href="https://doc.qt.io/qt-5/qsocketnotifier.html">QSocketNotifier</a> class to add a python socket’s file number to the Qt event loop so that everything is event driven.  I find this to be a good solution.</p>
<p>There should be a way to do something similar with asyncio such that events from Qt can be used to trigger event handling in asyncio code, but when I looked a few years ago it seemed that the core event loops in asyncio were not set up for this use case.  Maybe there are good solutions by now.</p>

---

## Post #3 by @derekcbr (2023-03-16 13:27 UTC)

<p>Thanks a lot! Indeed helpful! Will try QSocketNotifier.</p>

---

## Post #4 by @lassoan (2023-03-16 13:45 UTC)

<p>You may consider using the WebServer module in Slicer. Commonly needed features are exposed via the <code>slicer</code> endpoint, it has an <code>exec</code> option to allow full access to the entire Slicer Python API, and you can also start a SlicerHTTPServer with your own <code>RequestHandler</code> to support any custom requests. So, you actually don’t need to go down to the asincio or QSocketNotifier level or deal with any communication stuff at all, just implement a simple Python class that has <code>canHandleRequest</code> and <code>handleRequest</code> methods (<a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/WebServer/WebServerLib/SlicerRequestHandler.py">Slicer’s default request handler</a> can serve as an example).</p>

---

## Post #5 by @derekcbr (2023-03-17 01:02 UTC)

<p>Thank you very much for the help! That is really great! Will try with it!</p>

---
