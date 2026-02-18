# How to Receive and Visualize PolyData from IGTLink

**Topic ID**: 25736
**Date**: 2022-10-17
**URL**: https://discourse.slicer.org/t/how-to-receive-and-visualize-polydata-from-igtlink/25736

---

## Post #1 by @Jack_Zhang (2022-10-17 19:48 UTC)

<p>Operating system: Windows 10<br>
Slicer version:5.0.3</p>
<p>I’ve written a program that sends a polydata message over IGTLink to Slicer. As a demo run, I just want to create a line between two points and add it to the 3D widget. I was wondering how to add the line to the scene once the message is sent. The program is able to establish a connection with Slicer using the OpenIGTLinkIF module just fine, and I think it is successfully sending the polydata in each loop. The device name I specified appears in the <em>Models</em> modules but I’m not sure what to do from here.</p>
<p>Here is the code I’m using to send the OpenIGTLink messages:</p>
<pre><code class="lang-auto">// include basic libraries
#include &lt;iostream&gt;
#include &lt;thread&gt;

// include igtlink headers 
#include "igtlOSUtil.h"
#include "igtlMessageHeader.h"
#include "igtlServerSocket.h"
#include "igtlPolyDataMessage.h"

std::atomic_bool StopFlag = false;

int SendPolyData(igtl::Socket::Pointer&amp; socket)
{   
    // Allocate Status Message Class
    igtl::PolyDataMessage::Pointer polyDataMsg;
    polyDataMsg = igtl::PolyDataMessage::New();
    // NOTE: the server should send a message with the same device name
    // as the received query message. 
    polyDataMsg-&gt;SetDeviceName("Fake Shapes");

    // Define points connected by line
    static igtlFloat32 pointsData[2][3] = { {0,0,0}, {100,100,100} };

    // Create point array
    igtl::PolyDataPointArray::Pointer pointArray;
    pointArray = igtl::PolyDataPointArray::New();

    // Add point data to point array
    for (unsigned int i = 0; i &lt; 2; i++)
    {
        pointArray-&gt;AddPoint(pointsData[i]);
    }

    // Add pointArray to PolyDataMessage
    polyDataMsg-&gt;SetPoints(pointArray);

    // Add lines
    static igtlUint32 lineData[2][3] = { {0,0,0}, {100,100,100} };


    // Add PolyDataCellArray and add lines
    igtl::PolyDataCellArray::Pointer cellArray;
    cellArray = igtl::PolyDataCellArray::New();
    for (unsigned int i = 0; i &lt; 2; i++)
    {
        cellArray-&gt;AddCell(3, lineData[i]);
    }

    // Add PolyDataCellArray to PolyDataMessage
    polyDataMsg-&gt;SetLines(cellArray);

    // Pack polyDataMsg and send via OpenIGTLink socket
    polyDataMsg-&gt;Pack();
    socket-&gt;Send(polyDataMsg-&gt;GetPackPointer(), polyDataMsg-&gt;GetPackSize());
    std::cout &lt;&lt; "Message sent" &lt;&lt; std::endl;
    return 1;
}

int LoopFunction() {
    // Create server socket
    igtl::ServerSocket::Pointer ServerSocket;
    ServerSocket = igtl::ServerSocket::New();
    int r = ServerSocket-&gt;CreateServer(18944);

    if (r &lt; 0)
    {
        std::cerr &lt;&lt; "Cannot create a server socket" &lt;&lt; std::endl;
        exit(0);
    }

    igtl::Socket::Pointer socket;

    // Wait for Connection
    socket = ServerSocket-&gt;WaitForConnection(10000); // Wait ten seconds for connection

    if (socket.IsNotNull()) // if client connected
    {
        std::cerr &lt;&lt; "Client connected." &lt;&lt; std::endl;

        while (!StopFlag)
        {
            //socket-&gt;Skip(HeaderMsg-&gt;GetPodySizeToRead(),0);
            SendPolyData(socket);
            igtl::Sleep(500);
        }

    }
    else
    {
        std::cerr &lt;&lt; "Client could not connect." &lt;&lt; std::endl;
    }
    // Close connect
    socket-&gt;CloseSocket();
    return 1;
}

int main() {
    // Create thread for loopFunction
    std::thread MessageThread(LoopFunction);

    // main function stops to listen for keyboard input. When input is detected,
    // loop in LoopFunction is broken, and the function quickly returns
    std::cout &lt;&lt; "Press any key to stop loop" &lt;&lt; std::endl;
    std::cin.get();
    StopFlag = true;
    MessageThread.join();

    // Send message when all threads are joined
    std::cout &lt;&lt; "All threads joined" &lt;&lt; std::endl;

    return EXIT_SUCCESS;
}
</code></pre>

---

## Post #2 by @Sunderlandkyl (2022-10-17 20:07 UTC)

<p>If the polydata appears in the Models module then it should work.</p>
<p>Have you recentered the 3D view so that the polydata is in the middle of the view?</p>
<p>Also can check that the data in the “Information” section of the Models module is correct for your polydata?</p>

---

## Post #3 by @Jack_Zhang (2022-10-17 20:10 UTC)

<p>I’m guessing I just formatted my lines incorrectly, since there should only be one line connecting two points. This is what I see with the server active:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c1cce85b6e847c7720facb5e94f7ec52e620df60.png" data-download-href="/uploads/short-url/rErabXwiL5lUVycEUYGuiy3Qg5q.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c1cce85b6e847c7720facb5e94f7ec52e620df60_2_690x343.png" alt="image" data-base62-sha1="rErabXwiL5lUVycEUYGuiy3Qg5q" width="690" height="343" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c1cce85b6e847c7720facb5e94f7ec52e620df60_2_690x343.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c1cce85b6e847c7720facb5e94f7ec52e620df60_2_1035x514.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c1cce85b6e847c7720facb5e94f7ec52e620df60_2_1380x686.png 2x" data-dominant-color="6A6B72"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1915×952 47.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @Sunderlandkyl (2022-10-17 20:20 UTC)

<p>I think your line cell is not composed correctly. You should only call AddCell once, and it should contain 2 values, {0, 1}.</p>

---

## Post #5 by @Jack_Zhang (2022-10-17 20:35 UTC)

<p>Got it, thanks! Here is the fixed code for future reference:</p>
<pre><code class="lang-auto">// include basic libraries
#include &lt;iostream&gt;
#include &lt;thread&gt;

// include igtlink headers 
#include "igtlOSUtil.h"
#include "igtlMessageHeader.h"
#include "igtlServerSocket.h"
#include "igtlPolyDataMessage.h"

std::atomic_bool StopFlag = false;

int SendPolyData(igtl::Socket::Pointer&amp; socket)
{   
    // Allocate Status Message Class
    igtl::PolyDataMessage::Pointer polyDataMsg;
    polyDataMsg = igtl::PolyDataMessage::New();
    // NOTE: the server should send a message with the same device name
    // as the received query message. 
    polyDataMsg-&gt;SetDeviceName("Fake Shapes");

    // Define points connected by line
    static igtlFloat32 pointsData[2][3] = { {0,0,0}, {100,100,100} };

    // Create point array
    igtl::PolyDataPointArray::Pointer pointArray;
    pointArray = igtl::PolyDataPointArray::New();

    // Add point data to point array
    for (unsigned int i = 0; i &lt; 2; i++)
    {
        pointArray-&gt;AddPoint(pointsData[i]);
    }

    // Add pointArray to PolyDataMessage
    polyDataMsg-&gt;SetPoints(pointArray);


    // Add lines
    static igtlUint32 lineData[2] = {0,1}; // equivalent to SetId with vtk's PolyLine

    // Create PolyDataCellArray and add lines
    igtl::PolyDataCellArray::Pointer cellArray;
    cellArray = igtl::PolyDataCellArray::New();
    cellArray-&gt;AddCell(2, lineData);

    // Add PolyDataCellArray to PolyDataMessage
    polyDataMsg-&gt;SetLines(cellArray);

    // Pack polyDataMsg and send via OpenIGTLink socket
    polyDataMsg-&gt;Pack();
    socket-&gt;Send(polyDataMsg-&gt;GetPackPointer(), polyDataMsg-&gt;GetPackSize());
    std::cout &lt;&lt; "Message sent" &lt;&lt; std::endl;
    return 1;
}

int LoopFunction() {
    // Create server socket
    igtl::ServerSocket::Pointer ServerSocket;
    ServerSocket = igtl::ServerSocket::New();
    int r = ServerSocket-&gt;CreateServer(18944);

    if (r &lt; 0)
    {
        std::cerr &lt;&lt; "Cannot create a server socket" &lt;&lt; std::endl;
        exit(0);
    }

    igtl::Socket::Pointer socket;

    // Wait for Connection
    socket = ServerSocket-&gt;WaitForConnection(10000); // Wait ten seconds for connection

    if (socket.IsNotNull()) // if client connected
    {
        std::cerr &lt;&lt; "Client connected." &lt;&lt; std::endl;

        while (!StopFlag)
        {
            //socket-&gt;Skip(HeaderMsg-&gt;GetPodySizeToRead(),0);
            SendPolyData(socket);
            igtl::Sleep(500);
        }

    }
    else
    {
        std::cerr &lt;&lt; "Client could not connect." &lt;&lt; std::endl;
    }
    // Close connect
    socket-&gt;CloseSocket();
    return 1;
}

int main() {
    // Create thread for loopFunction
    std::thread MessageThread(LoopFunction);

    // main function stops to listen for keyboard input. When input is detected,
    // loop in LoopFunction is broken, and the function quickly returns
    std::cout &lt;&lt; "Press any key to stop loop" &lt;&lt; std::endl;
    std::cin.get();
    StopFlag = true;
    MessageThread.join();

    // Send message when all threads are joined
    std::cout &lt;&lt; "All threads joined" &lt;&lt; std::endl;

    return EXIT_SUCCESS;
}
</code></pre>

---
