---
topic_id: 25755
title: "Low Refresh Rate When Adding Model Using Openigtlink"
date: 2022-10-18
url: https://discourse.slicer.org/t/25755
---

# Low Refresh Rate When Adding Model Using OpenIGTLink

**Topic ID**: 25755
**Date**: 2022-10-18
**URL**: https://discourse.slicer.org/t/low-refresh-rate-when-adding-model-using-openigtlink/25755

---

## Post #1 by @Jack_Zhang (2022-10-18 14:33 UTC)

<p>I’m currently using the code below to feed Slicer some “dummy data” to visualize. The shape is a line connecting two randomly selected points. I’m doing this just so I can familiarize myself with how to do this with C++ programs because eventually we want to feed live data from a sensor machine and have what’s visualized in Slicer be in “real time” with what the sensor sees. However, while the program sends a new message over OpenIGTLink every 0.1 seconds, Slicer takes noticeably longer to update the 3D viewer. I’m guessing that generating the node or rendering the entire polydata takes time.</p>
<p>Note that I cannot simply rotate or shift the line being rendered because the object the sensor will be feeding data from will be deformed. For our line example, if it were connecting more points, this would mean the line curving. Thus, I need to be able to feed changes to some of the points with each message sent by OpenIGTLink.</p>
<p>Code:</p>
<pre><code class="lang-auto">// include basic libraries
#include &lt;iostream&gt;
#include &lt;thread&gt;
#include &lt;stdlib.h&gt; // srand, rand
#include &lt;ctime&gt; // clock 

// include igtlink headers 
#include "igtlOSUtil.h"
#include "igtlMessageHeader.h"
#include "igtlServerSocket.h"
#include "igtlPolyDataMessage.h"

std::atomic_bool StopFlag = false;

int SendPolyData(igtl::Socket::Pointer&amp; socket)
{   
    // Get time before message is created
    auto start = std::clock();

    // Allocate Status Message Class
    igtl::PolyDataMessage::Pointer polyDataMsg;
    polyDataMsg = igtl::PolyDataMessage::New();
    // NOTE: the server should send a message with the same device name
    // as the received query message. 
    polyDataMsg-&gt;SetDeviceName("Fake Shapes");

    // Define points connected by line
    static igtlFloat32 pointsData[6][3] = { {0,0,0}, {100,100,100}, {30,-50,30}, {-100,-100,-100}, {36,93,-25}, {-43,91,-64} };

    // Create point array
    igtl::PolyDataPointArray::Pointer pointArray;
    pointArray = igtl::PolyDataPointArray::New();

    // Add random consecutive pair of point data cells to point array
    srand(std::time(nullptr));
    int FirstIndex = rand() % 5; // Random integeger [0..4]
    for (unsigned int i = FirstIndex; i &lt; FirstIndex + 2; i++)
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

    // Get time when message is sent and print CPU time elapsed
    auto end = std::clock();
    std::cout &lt;&lt; "Time: " &lt;&lt; (std::clock() - start) / (double)(CLOCKS_PER_SEC / 1000) &lt;&lt; " ms" &lt;&lt; std::endl;
    
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
            igtl::Sleep(100);
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
</code></pre>

---

## Post #2 by @lassoan (2022-10-19 04:49 UTC)

<p>Update of models from OpenIGTLink messages is very quick (dozens of frames per second for small models). You can try this using <a href="https://pypi.org/project/pyigtl/">pyigtl Python package</a>. For example:</p>
<pre><code class="lang-python">import numpy as np
import pyigtl
import vtk

reader = vtk.vtkPLYReader()
reader.SetFileName("/path/to/some/mesh.ply")
reader.Update()
polydata = reader.GetOutput()

client = pyigtl.OpenIGTLinkClient(host="127.0.0.1", port=18944)

output_message = pyigtl.PolyDataMessage(polydata, device_name='mesh')

while True:
    client.send_message(output_message)
    output_message.points += 0.1  # Translate the model by 0.1mm along every axis in each iteration
</code></pre>
<p>If this does not result on your computer in continuous updates (20+ fps) with a small model (like this <a href="https://1drv.ms/u/s!Arm_AFxB9yqHyoMd47YCkYykMn-y5w?e=2s0ZDr">cylinder.ply</a>) then maybe rendering is slowed down by content in your scene (maybe there is a volume-rendered image, large models, etc.).</p>
<p>It may be even lighter weight operation if you update markup point list, using POINT message:</p>
<pre><code class="lang-auto">import numpy as np
import pyigtl

client = pyigtl.OpenIGTLinkClient(host="127.0.0.1", port=18945)
while True:
    newPositions = np.random.rand(2,3)
    output_message = pyigtl.PointMessage(device_name='F', positions=newPositions)
    client.send_message(output_message)
</code></pre>

---

## Post #3 by @Jack_Zhang (2022-11-01 20:25 UTC)

<p>Using the FPS viewer, I’m getting 9 frames per second. I have nothing else loaded.</p>

---

## Post #4 by @lassoan (2022-11-01 21:51 UTC)

<p>Do you send the small cylinder.ply model?<br>
If not, what is the number of points and cells in your mesh?<br>
What operating system, CPU, and graphics card do you use?</p>

---

## Post #5 by @Jack_Zhang (2022-11-01 23:57 UTC)

<p>I’m using the code in my original post. The mesh being sent has two points and one cell. There is about a millisecond delay between messages being sent, but the 3D viewer is being updated roughly once every 100ms.</p>
<p>OS: Windows 10 (OS Build: 19044.2130)<br>
CPU: i7-10510U (Integrated graphics)</p>
<p>Build: Lenovo ThinkPad T14s Gen 1<br>
Type Number: 20T0 0023US</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://www.colamco.com/product/lenovo-thinkpad-t14s-gen-1-20t00023us-notebook-20t00023us-2027553">
  <header class="source">
      <img src="https://www.colamco.com/Portals/0/favicon.ico?ver=HMwSeUADONE3_6v2l0OFJw%3d%3d" class="site-icon" width="32" height="32">

      <a href="https://www.colamco.com/product/lenovo-thinkpad-t14s-gen-1-20t00023us-notebook-20t00023us-2027553" target="_blank" rel="noopener nofollow ugc">COLAMCO.com</a>
  </header>

  <article class="onebox-body">
    <img src="https://services.colamco.com/resources/v1/images/https%3a%7c%7ccontent.etilize.com%7cRightMaximum%7c1066805267.jpg%3fnoimage%3dlogo/auto/600?cdv=1200" class="thumbnail onebox-avatar" width="500" height="500">

<h3><a href="https://www.colamco.com/product/lenovo-thinkpad-t14s-gen-1-20t00023us-notebook-20t00023us-2027553" target="_blank" rel="noopener nofollow ugc">Lenovo ThinkPad T14s Gen 1 20T00023US 14" Notebook - Full HD - 1920 x 1080 -...</a></h3>

  <p>Buy Lenovo ThinkPad T14s Gen 1 20T00023US 14" Notebook - Full HD - 1920 x 1080 - Intel Core i7 (10th Gen) i7-10510U Quad-core (4 Core) 1.80 GHz - 16 GB RAM - 512 GB SSD - Black 20T00023US at COLAMCO.com: WORLD-RENOWNED BUSINESS TOOLSPerformance and...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #6 by @lassoan (2022-11-07 19:36 UTC)

<aside class="quote no-group" data-username="Jack_Zhang" data-post="5" data-topic="25755">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jack_zhang/48/16328_2.png" class="avatar"> Jack_Zhang:</div>
<blockquote>
<p>I’m using the code in my original post.</p>
</blockquote>
</aside>
<p>Please use the code snippet that I provided (install python, pip install pyigtl, and run the script). If that has no performance issues then we know that the problem is in your code. For example, you have <code>igtl::Sleep(100);</code> in the C++ code snippet that prevents you from ever going above 10fps.</p>

---

## Post #7 by @Jack_Zhang (2022-11-07 19:53 UTC)

<p>I’ll try to run your code snippet, but I’ll have to install an older version of python first since vtk isn’t working with the most recent release. From the testing that I’ve done, the <code>igtl::Sleep(100)</code> doesn’t do anything since the “message sent” message gets printed just as fast, easily outpacing the updates to the Slicer scene. I.e. messages are being sent over IGTLink that aren’t updating the scene in Slicer.</p>
<p>Anyways, I’ll get back to you when I have tested your code snippet.</p>

---

## Post #8 by @lassoan (2022-11-07 20:12 UTC)

<p><code>igtl::Sleep(100)</code> waits 100ms after sending a message to Slicer, therefore in best case you send messages at the rate of 10fps, so the update rate in the 3D viewer in Slicer will be 10fps.</p>
<p>If you don’t want to install Python-3.9 then the first thing I would try is to change <code>igtl::Sleep(100)</code> to <code>igtl::Sleep(0)</code>.</p>

---

## Post #9 by @Jack_Zhang (2022-11-07 20:14 UTC)

<p>I’ve already tried setting it to zero. Same effect. I’ll install python 3.9 when I get off work tonight. I should be able to reply with an update by tomorrow.</p>

---

## Post #10 by @Jack_Zhang (2022-11-10 15:28 UTC)

<p>I never got around to installing an older version of Python, but I’ve been working on another C++ app for sending a PolyData message over OpenIGTLink and I’m not getting the same issue. I used the same format as my previous code, printing an indicator to the command prompt every time a new message is sent over the socket. With the previous code, messages were being sent without being updated, but the app itself was able to send messages 60 times per second without issue. In the new code, which I’ll include a snippet of below, despite the fact that the line has 1000 points, Slicer can keep up up to 30 FPS even with my lousy integrated graphics processor. The new code reads from a binary file I’ve made rather than generate a line from two randomly selected points. I’ll be moving forward with the new code, so the issue is moot.</p>
<pre><code class="lang-auto">int SceneParser(std::string&amp; file_name) {
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
    std::cout &lt;&lt; "Establishing connection" &lt;&lt; std::endl;

    // Wait for Connection
    socket = ServerSocket-&gt;WaitForConnection(10000); // Wait ten seconds for connection

    if (socket.IsNotNull()) // if client connected
    {
        std::cerr &lt;&lt; "Client connected." &lt;&lt; std::endl;
        std::cout &lt;&lt; "Begin sending data by pressing any key followed by ENTER" &lt;&lt; std::endl;
        std::cin.get();

        // Open stream to read file into string
        std::ifstream dataFile(file_name, std::ios::binary | std::ios::ate);

        // print error message if file could not be opened
        if (dataFile.is_open() == false)
        {
            std::cout &lt;&lt; "Couldn't open file" &lt;&lt; std::endl;
            return -1;
        }


        // Parse scene string and pass each delimited frame to SendPolydata if file is open
        
        // Get size of file.
        auto file_size = dataFile.tellg();
        dataFile.seekg(0);

        // Read entire file into array.
        uint32_t left_to_read = static_cast&lt;uint32_t&gt;(file_size);
        char* file_data = static_cast&lt;char*&gt;(malloc(left_to_read));
        if (!dataFile.read(file_data, file_size))
        {
            free(file_data);
            std::cout &lt;&lt; "Unable to read file data\n";
            return -1;
        }
        // close data file after file_data is extracted and passed to buffer
        char* buffer = file_data;
        dataFile.close();

        // Read the header.
        // Unpack tag
        auto id = unpack_string(&amp;buffer, left_to_read, FILE_ID.length() + 1);
        if (id != FILE_ID)
        {
            free(file_data);
            std::cout &lt;&lt; "Unsupported file format.\n";
            return -1;
        }

        // Unpack version number
        auto version = unpack_number&lt;uint8_t&gt;(&amp;buffer, left_to_read);
        if (version != FILE_VERSION)
        {
            free(file_data);
            std::cout &lt;&lt; "Unsupported file version.\n";
            return -1;
        }

        // Unpack frame number
        auto FrameCount = unpack_number&lt;uint16_t&gt;(&amp;buffer, left_to_read);

        // Read data for each frame and send OpenIGTLink message
        for (unsigned int i = 0; i &lt; FrameCount; i++)
        {
            // Allocate Status Message Class
            igtl::PolyDataMessage::Pointer polyDataMsg;
            polyDataMsg = igtl::PolyDataMessage::New();
            // NOTE: the server should send a message with the same device name as the received query message. 
            polyDataMsg-&gt;SetDeviceName("Simulated Line");

            // Create PolyDataCellArray (stores lines)
            igtl::PolyDataCellArray::Pointer cellArray;
            cellArray = igtl::PolyDataCellArray::New();

            // Create PolyDataPointArray (stores points)
            igtl::PolyDataPointArray::Pointer pointArray;
            pointArray = igtl::PolyDataPointArray::New();

            // Unpack number of points
            int PointCount = unpack_number&lt;uint16_t&gt;(&amp;buffer, left_to_read);

            // Declare line, an array of indices for the vertices in the line
            auto lines = new igtlUint32[PointCount];

            // Fill in values for line and point arrays
            for (igtlUint32 j = 0; j &lt; PointCount; j++)
            {
                // Add index to lines
                lines[j] = j;

                // Declare array for coordinates of each point
                igtlFloat32 point[3];

                // Unpack three coordiantes for each point
                for (unsigned int j = 0; j &lt; 3; j++)
                {
                    igtlFloat32 coord = unpack_number&lt;float&gt;(&amp;buffer, left_to_read);
                    point[j] = coord;
                }

                // Add point to pointarray
                pointArray-&gt;AddPoint(point);

            }
            
            // Add pointArray to PolyDataMessage
            polyDataMsg-&gt;SetPoints(pointArray);

            // Add lines to cellArray and then deallocate memory for lines
            cellArray-&gt;AddCell(PointCount, lines);
            delete[] lines;
            
            // Add PolyDataCellArray to polyDataMessage
            polyDataMsg-&gt;SetLines(cellArray);
            
            // Pack polyDataMsg and send via OpenIGTLink socket
            polyDataMsg-&gt;Pack();
            socket-&gt;Send(polyDataMsg-&gt;GetPackPointer(), polyDataMsg-&gt;GetPackSize());
            std::cout &lt;&lt; "Message sent" &lt;&lt; std::endl;
            igtl::Sleep(1000/45);
        }

        // free memory allocated to file_data
        free(file_data);

        // Close stream
        dataFile.close();
    }
    else
    {
        std::cerr &lt;&lt; "Client could not connect." &lt;&lt; std::endl;
    }
    // Close connect
    socket-&gt;CloseSocket();
}
</code></pre>
<p>Note that unpack_string and unpack_number are just functions I’ve defined elsewhere for unpacking strings and numbers from binary files.</p>

---

## Post #11 by @lassoan (2022-11-10 16:06 UTC)

<p>Thanks for the update. It’s great to hear that everything seems to work as expected with your new code.</p>

---
