# Using async socket network

**Topic ID**: 35654
**Date**: 2024-04-22
**URL**: https://discourse.slicer.org/t/using-async-socket-network/35654

---

## Post #1 by @dael0207 (2024-04-22 09:58 UTC)

<p>Hello Slicer community.<br>
I’d like to incorporate a function within Slicer that asynchronously waits for reception.<br>
What I want is for the function to execute when Slicer is turned on, asynchronously wait for reception, and if received, send the corresponding value.<br>
I’d like this function to continue running asynchronously independently of other functions.<br>
My function looks like</p>
<pre><code class="lang-auto">async def ServerOpen(self):
        HOST = '127.0.0.1'
        PORT = 65432
        print("server open")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()

            print(f"{HOST}:{PORT}")

            while True:
                conn, addr = await loop.sock_accept(s)
                await self.receive_data(conn) 

    async def receive_data(self, conn):
        def convert_to_doubles(input_string):
            length = len(input_string)
            result = []

            for i in range(0, length, 2):
                substring = input_string[i:i+2]  
                num = float(substring)  
                result.append(num)  

            return result

        while True:
            data = await loop.sock_recv(conn, 1024)
            if not data:
                break

            received_message = data.decode()
            
            await loop.sock_sendall(conn, data)

            numbers = convert_to_doubles(received_message)
            print( numbers[0], numbers[1], numbers[2])
         

            center = [numbers[0], numbers[1], numbers[2]] 
            radius = 6.0 

          
            sphereSource = vtk.vtkSphereSource()
            sphereSource.SetCenter(center[0], center[1], center[2])
            sphereSource.SetRadius(radius)
            sphereSource.SetPhiResolution(30)
            sphereSource.SetThetaResolution(30)
            sphereSource.Update()

           
            sphere = sphereSource.GetOutput()

           
            renderer = slicer.app.layoutManager().threeDWidget(0).threeDView().renderWindow().GetRenderers().GetFirstRenderer()
            mapper = vtk.vtkPolyDataMapper()
            mapper.SetInputData(sphere)
            actor = vtk.vtkActor()
            actor.SetMapper(mapper)
            renderer.AddActor(actor)
            renderer.ResetCamera()

            
            slicer.app.layoutManager().threeDWidget(0).threeDView().renderWindow().Render()
</code></pre>
<p>Where and how should I insert this Python code? Thank you very much as always.</p>

---

## Post #2 by @pieper (2024-04-22 14:12 UTC)

<p>Slicer uses Qt’s event loop, not python’s asyncio.  You can look at the code for OpenIGTLink, which I believe uses a timer to periodically check for events, or the WebServer, which uses <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/WebServer/WebServer.py#L347">QSocketNotifier</a> so that events are generated when the network is active.</p>

---

## Post #3 by @dael0207 (2024-04-24 03:21 UTC)

<p>Dear pieper, Thanks to you, it helped me solve the problem<br>
But there’s another problem with the lack of modules</p>
<pre><code class="lang-auto">os.system("pip install PyQt5")
from PyQt5.QtNetwork import QTcpServer
</code></pre>
<p>I tried to solve it with this code, but when I run the executable, the module doesn’t install</p>
<pre><code class="lang-auto">from PyQt5.QtNetwork import QTcpServer
ModuleNotFoundError: No module named 'PyQt5'
</code></pre>
<p>error is like this, How do I add the code to install the module?<br>
thanks to you every time! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #4 by @pieper (2024-04-24 12:37 UTC)

<p>Slicer’s architecture is different, so you can’t use PyQt, but instead use PythonQt, which is pre-loaded in the Slicer python environment in the <code>qt</code> package.  So you would use a line like <code>qt.QTcpServer()</code>.  It’ll help you to go through the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Tutorials_for_software_developers">developer tutorials</a> to learn some of the specifics of the Slicer environment.</p>

---

## Post #5 by @dael0207 (2024-05-12 14:25 UTC)

<p>Thank you so much sir. I made a code based on your advice.<br>
There’s a little bit of a problem with the code. The function seems to work, but when I run the executives, it only runs cmd and the Slicer UI doesn’t. I want to make the function of this wait for reception similar to Asynco and send a specific code if it gets it after doing something else. I always appreciate it so much and I’d really appreciate any advice.</p>
<p>My code is as follows `self.server = MyTcpServer()<br>
self.server.listen(qt.QHostAddress(“127.0.0.1”), 65432)</p>
<pre><code>    # Timer setting
    self.timer = qt.QTimer()
    self.timer.timeout.connect(self.checkClientData)
    self.timer.start(1000)
    print("connect")
</code></pre>
<pre><code class="lang-auto">Init MyTcpServer is in NavigationWidget's sepup Method and
</code></pre>
<pre><code>def checkClientData(self):
    for socket in self.server.children():
        if isinstance(socket, qt.QTcpSocket):
            if socket.bytesAvailable():
                data = socket.readAll()
                print("Received data from client:", bytes(data).decode())
            else:
                pass`
</code></pre>
<p>and my Class is</p>
<pre><code class="lang-auto">class MyTcpServer(qt.QTcpServer):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.newConnection.connect(self.handleConnection)

    def handleConnection(self):
        client_socket = self.nextPendingConnection()
        client_socket.readyRead.connect(self.readData)

    def readData(self):
        client_socket = self.sender()
        if client_socket is not None:
            data = client_socket.readAll()
            print("Received data from client:", bytes(data).decode())   
</code></pre>
<p>always thanks very much</p>

---

## Post #6 by @pieper (2024-05-12 15:50 UTC)

<aside class="quote no-group" data-username="dael0207" data-post="5" data-topic="35654">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dael0207/48/70087_2.png" class="avatar"> dael0207:</div>
<blockquote>
<p>The function seems to work, but when I run the executives, it only runs cmd and the Slicer UI doesn’t</p>
</blockquote>
</aside>
<p>I don’t understand exactly what you mean here.  Can you describe more?</p>
<p>It should happen that QSocketNotifier, as I mentioned earlier, make the entire process event-driven and efficient and generally doesn’t require timers or UI blockage.  Try the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/webserver.html">WebServer</a> and look at the <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/WebServer/WebServer.py#L510">implementation</a>.</p>

---

## Post #7 by @pieper (2024-05-12 15:51 UTC)

<p>Also if you still need help debugging, make a <a href="http://www.sscce.org/">self-contained</a> example so that others can see exactly what you are trying to do.</p>

---
