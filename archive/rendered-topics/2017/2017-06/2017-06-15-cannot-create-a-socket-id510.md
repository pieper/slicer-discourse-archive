# Cannot create a socket

**Topic ID**: 510
**Date**: 2017-06-15
**URL**: https://discourse.slicer.org/t/cannot-create-a-socket/510

---

## Post #1 by @f.cnunez (2017-06-15 17:02 UTC)

<p>Hi all,<br>
I was trying to communicate a software called ORB-SLAM2 with Slicer using OpenIGTLink library to pass the transform information of the camera movement to Slicer. I have the following code integrated in ORB-SLAM2:</p>
<pre><code class="lang-auto">igtl::ServerSocket::Pointer serverSocket;
  serverSocket = igtl::ServerSocket::New();
  int r = serverSocket-&gt;CreateServer(18944);
   
  igtl::TransformMessage::Pointer transMsg;
  transMsg = igtl::TransformMessage::New();
  transMsg-&gt;SetDeviceName("Tracker");

   if (r &lt; 0)
    {
    std::cerr &lt;&lt; "Cannot create a server socket." &lt;&lt; std::endl;
    exit(0);
    }

  igtl::Socket::Pointer socket;
  socket = serverSocket-&gt;WaitForConnection(1000);
  igtl::Matrix4x4 matrix;
        
        matrix[0][0]=Twc.m[0];
        matrix[1][0]=Twc.m[1];
        matrix[2][0]=Twc.m[2];
        matrix[3][0]=Twc.m[3];

        matrix[0][1]=Twc.m[4];
        matrix[1][1]=Twc.m[5];
        matrix[2][1]=Twc.m[6];
        matrix[3][1]=Twc.m[7];

        matrix[0][2]=Twc.m[8];
        matrix[1][2]=Twc.m[9];
        matrix[2][2]=Twc.m[10];
        matrix[3][2]=Twc.m[11];

        matrix[0][3]=Twc.m[12];
        matrix[1][3]=Twc.m[13];
        matrix[2][3]=Twc.m[14];
        matrix[3][3]=Twc.m[15];
	
	transMsg-&gt;SetMatrix(matrix);
        transMsg-&gt;Pack();
        socket-&gt;Send(transMsg-&gt;GetPackPointer(), transMsg-&gt;GetPackSize());
        socket-&gt;CloseSocket();
</code></pre>
<p>but when I run the code it gives me an error (segment violation). I think that the problem is in the creation of the socket, because when I comment this line “socket-&gt;Send(transMsg-&gt;GetPackPointer(), transMsg-&gt;GetPackSize());” it doesn’t give any error but It neither send the data. I would like to know if I am creating the socket in a wrong way or what could be the problem.</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2017-06-15 17:15 UTC)

<p>There are several examples in OpenIGTLink library: <a href="https://github.com/openigtlink/OpenIGTLink/tree/master/Examples/Tracker">https://github.com/openigtlink/OpenIGTLink/tree/master/Examples/Tracker</a>.</p>
<p>First just build those and see if they work, then choose one and modify it to fit your needs.</p>
<p>In general, we integrate these kind of algorithms and interfaces in the Plus toolkit (<a href="http://www.plustoolkit.org">www.plustoolkit.org</a>). For example, we’ve just added to Plus webcam-based tracking using ArUco.</p>

---

## Post #3 by @ihnorton (2017-06-15 17:16 UTC)

<p>If :18944 is already open in another process you won’t be able to create a new socket on that port.</p>

---

## Post #4 by @lassoan (2017-06-15 17:29 UTC)

<p>That’s a good point! Make sure one server communicates with one client (Slicer can be either a client or server).</p>

---

## Post #5 by @f.cnunez (2017-06-15 17:33 UTC)

<p>I have tried with the TrackerServer example and it works (also the socket in the port 18944). I tried to adapt the code from that example to use in my program (ORB-SLAM2), but in this program the socket doesn’t work correctly.</p>

---

## Post #6 by @lassoan (2017-06-15 17:48 UTC)

<p>Compare all the compiler and linker options of the working and non-working example.<br>
Do you use CMake?<br>
What operating system do you use?</p>

---

## Post #7 by @ihnorton (2017-06-15 18:28 UTC)

<ul>
<li>Use a debugger and step through the code, figure out exactly where is the segfault.</li>
<li>Add some print statements to tell whether it receives the connection (<code>WaitForConnection</code> will block).</li>
<li>Use <a href="https://www.wireshark.org/">wireshark</a> to monitor connections/traffic.</li>
</ul>

---

## Post #8 by @f.cnunez (2017-06-15 20:05 UTC)

<p>Yes, I am using Cmake and Ubuntu 14.04</p>

---

## Post #9 by @f.cnunez (2017-06-16 16:19 UTC)

<p>Now, I have established connection between ORB-SLAM2 an Slicer using OpenIGTLink changing the socket code shown before, but when I make socket-&gt;Send(transMsg-&gt;GetPackPointer(), transMsg-&gt;GetPackSize()); I only send the first transformation correctly but this transformation doesn’t change like in trackerserver example. I’ve checked the matrix I employ (making a igtl::PrintMatrix(matrix); ) and this matrix works well (It changes in each iteration), but it seems that the part<br>
transMsg-&gt;SetMatrix(matrix);</p>
<pre><code>    transMsg-&gt;Pack();

    socket-&gt;Send(transMsg-&gt;GetPackPointer(), transMsg-&gt;GetPackSize());
</code></pre>
<p>does not update the message sent to Slicer. Any idea of what can be the problem?</p>
<p>Thanks</p>

---

## Post #10 by @lassoan (2017-06-16 17:01 UTC)

<p>Is memory content at transMsg-&gt;GetPackPointer() is changing?</p>

---

## Post #11 by @f.cnunez (2017-06-16 17:12 UTC)

<p>No, I have always the same memory content ( 0x7f1340603da0)</p>

---

## Post #12 by @lassoan (2017-06-16 17:42 UTC)

<p>The pointer itself is irrelevant, check the memory content at that location (up to GetPackSize() number of bytes). If you don’t see any change that’s great, it means that the error is not in the communication part.</p>
<p>Probably it’s some trivial issue. If you send a link to the source code then I can have a look.</p>

---

## Post #13 by @f.cnunez (2017-06-16 17:53 UTC)

<p>I have checked the GetPackSize and it´s also the same always. The code I am using is this(I have added the OpenIGTLink connection to pass the Twc.m information to Slicer):</p>
<pre><code>/**
* This file is part of ORB-SLAM2.
*
* Copyright (C) 2014-2016 Raúl Mur-Artal &lt;raulmur at unizar dot es&gt; (University of Zaragoza)
* For more information see &lt;https://github.com/raulmur/ORB_SLAM2&gt;
*
* ORB-SLAM2 is free software: you can redistribute it and/or modify
* it under the terms of the GNU General Public License as published by
* the Free Software Foundation, either version 3 of the License, or
* (at your option) any later version.
*
* ORB-SLAM2 is distributed in the hope that it will be useful,
* but WITHOUT ANY WARRANTY; without even the implied warranty of
* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
* GNU General Public License for more details.
*
* You should have received a copy of the GNU General Public License
* along with ORB-SLAM2. If not, see &lt;http://www.gnu.org/licenses/&gt;.
*/

#include "Viewer.h"
#include &lt;pangolin/pangolin.h&gt;

#include &lt;mutex&gt;

//includes added
#include &lt;iostream&gt;
#include &lt;math.h&gt;
#include &lt;cstdlib&gt;

#include "igtlOSUtil.h"
#include "igtlTransformMessage.h"
#include "igtlServerSocket.h"


namespace ORB_SLAM2
{

Viewer::Viewer(System* pSystem, FrameDrawer *pFrameDrawer, MapDrawer *pMapDrawer, Tracking *pTracking, const string &amp;strSettingPath):
    mpSystem(pSystem), mpFrameDrawer(pFrameDrawer),mpMapDrawer(pMapDrawer), mpTracker(pTracking),
    mbFinishRequested(false), mbFinished(true), mbStopped(true), mbStopRequested(false)
{
    cv::FileStorage fSettings(strSettingPath, cv::FileStorage::READ);

    float fps = fSettings["Camera.fps"];
    if(fps&lt;1)
        fps=30;
    mT = 1e3/fps;

    mImageWidth = fSettings["Camera.width"];
    mImageHeight = fSettings["Camera.height"];
    if(mImageWidth&lt;1 || mImageHeight&lt;1)
    {
        mImageWidth = 640;
        mImageHeight = 480;
    }

    mViewpointX = fSettings["Viewer.ViewpointX"];
    mViewpointY = fSettings["Viewer.ViewpointY"];
    mViewpointZ = fSettings["Viewer.ViewpointZ"];
    mViewpointF = fSettings["Viewer.ViewpointF"];
}

void Viewer::Run()
{
  //parte anadida
  igtl::TransformMessage::Pointer transMsg;
  transMsg = igtl::TransformMessage::New();
  transMsg-&gt;SetDeviceName("TrackerORB");

  igtl::ServerSocket::Pointer serverSocket;
  serverSocket = igtl::ServerSocket::New();
  int r = serverSocket-&gt;CreateServer(18944);
   
  

   if (r &lt; 0)
    {
    std::cerr &lt;&lt; "Cannot create a server socket." &lt;&lt; std::endl;
    exit(0);
    }

  igtl::Socket::Pointer socket1;
  //socket1= igtl::Socket::New();
  igtl::Matrix4x4 matrix;

//final parte anadida
    mbFinished = false;
    mbStopped = false;

    pangolin::CreateWindowAndBind("ORB-SLAM2: Map Viewer",1024,768);

    // 3D Mouse handler requires depth testing to be enabled
    glEnable(GL_DEPTH_TEST);

    // Issue specific OpenGl we might need
    glEnable (GL_BLEND);
    glBlendFunc (GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);

    pangolin::CreatePanel("menu").SetBounds(0.0,1.0,0.0,pangolin::Attach::Pix(175));
    pangolin::Var&lt;bool&gt; menuFollowCamera("menu.Follow Camera",true,true);
    pangolin::Var&lt;bool&gt; menuShowPoints("menu.Show Points",true,true);
    pangolin::Var&lt;bool&gt; menuShowKeyFrames("menu.Show KeyFrames",true,true);
    pangolin::Var&lt;bool&gt; menuShowGraph("menu.Show Graph",true,true);
    pangolin::Var&lt;bool&gt; menuLocalizationMode("menu.Localization Mode",false,true);
    pangolin::Var&lt;bool&gt; menuReset("menu.Reset",false,false);

    // Define Camera Render Object (for view / scene browsing)
    pangolin::OpenGlRenderState s_cam(
                pangolin::ProjectionMatrix(1024,768,mViewpointF,mViewpointF,512,389,0.1,1000),
                pangolin::ModelViewLookAt(mViewpointX,mViewpointY,mViewpointZ, 0,0,0,0.0,-1.0, 0.0)
                );

    // Add named OpenGL viewport to window and provide 3D Handler
    pangolin::View&amp; d_cam = pangolin::CreateDisplay()
            .SetBounds(0.0, 1.0, pangolin::Attach::Pix(175), 1.0, -1024.0f/768.0f)
            .SetHandler(new pangolin::Handler3D(s_cam));

    pangolin::OpenGlMatrix Twc;
    Twc.SetIdentity();

    cv::namedWindow("ORB-SLAM2: Current Frame");

    bool bFollow = true;
    bool bLocalizationMode = false;

    while(1)
    {
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

        mpMapDrawer-&gt;GetCurrentOpenGLCameraMatrix(Twc);
	socket1 = serverSocket-&gt;WaitForConnection(1);

if (socket1.IsNotNull()) // if client connected
      {
	std::cerr &lt;&lt; "A client is connected." &lt;&lt; std::endl;

        
	matrix[0][0]=Twc.m[0];
        matrix[1][0]=Twc.m[1];
        matrix[2][0]=Twc.m[2];
        matrix[3][0]=0;//Twc.m[3];

        matrix[0][1]=Twc.m[4];
        matrix[1][1]=Twc.m[5];
        matrix[2][1]=Twc.m[6];
        matrix[3][1]=0;//Twc.m[7];

        matrix[0][2]=Twc.m[8];
        matrix[1][2]=Twc.m[9];
        matrix[2][2]=Twc.m[10];
        matrix[3][2]=0;//Twc.m[11];

        matrix[0][3]=Twc.m[12];
        matrix[1][3]=Twc.m[13];
        matrix[2][3]=Twc.m[14];
        matrix[3][3]=1;//Twc.m[15];


	transMsg-&gt;SetMatrix(matrix);

	igtl::PrintMatrix(matrix);

        transMsg-&gt;Pack();

        socket1-&gt;Send(transMsg-&gt;GetPackPointer(), transMsg-&gt;GetPackSize());
	igtl::Sleep(1);

	std::cerr &lt;&lt; "Size of pack: " &lt;&lt;  transMsg-&gt;GetPackSize()&lt;&lt; std::endl;
	
	}
        if(menuFollowCamera &amp;&amp; bFollow)
        {
            s_cam.Follow(Twc);
        }
        else if(menuFollowCamera &amp;&amp; !bFollow)
        {
            s_cam.SetModelViewMatrix(pangolin::ModelViewLookAt(mViewpointX,mViewpointY,mViewpointZ, 0,0,0,0.0,-1.0, 0.0));
            s_cam.Follow(Twc);
            bFollow = true;
        }
        else if(!menuFollowCamera &amp;&amp; bFollow)
        {
            bFollow = false;
        }

        if(menuLocalizationMode &amp;&amp; !bLocalizationMode)
        {
            mpSystem-&gt;ActivateLocalizationMode();
            bLocalizationMode = true;
        }
        else if(!menuLocalizationMode &amp;&amp; bLocalizationMode)
        {
            mpSystem-&gt;DeactivateLocalizationMode();
            bLocalizationMode = false;
        }

        d_cam.Activate(s_cam);
        glClearColor(1.0f,1.0f,1.0f,1.0f);
        mpMapDrawer-&gt;DrawCurrentCamera(Twc);
        if(menuShowKeyFrames || menuShowGraph)
            mpMapDrawer-&gt;DrawKeyFrames(menuShowKeyFrames,menuShowGraph);
        if(menuShowPoints)
            mpMapDrawer-&gt;DrawMapPoints();

        pangolin::FinishFrame();

        cv::Mat im = mpFrameDrawer-&gt;DrawFrame();
        cv::imshow("ORB-SLAM2: Current Frame",im);
        cv::waitKey(mT);

        if(menuReset)
        {
            menuShowGraph = true;
            menuShowKeyFrames = true;
            menuShowPoints = true;
            menuLocalizationMode = false;
            if(bLocalizationMode)
                mpSystem-&gt;DeactivateLocalizationMode();
            bLocalizationMode = false;
            bFollow = true;
            menuFollowCamera = true;
            mpSystem-&gt;Reset();
            menuReset = false;
        }

        if(Stop())
        {
            while(isStopped())
            {
                std::this_thread::sleep_for(std::chrono::microseconds(3000));
            }
        }

        if(CheckFinish())
	{//parte anadida
	   // socket1-&gt;CloseSocket();
            break;
	}
    }

    SetFinish();
}

void Viewer::RequestFinish()
{
    unique_lock&lt;mutex&gt; lock(mMutexFinish);
    mbFinishRequested = true;
}

bool Viewer::CheckFinish()
{
    unique_lock&lt;mutex&gt; lock(mMutexFinish);
    return mbFinishRequested;
}

void Viewer::SetFinish()
{
    unique_lock&lt;mutex&gt; lock(mMutexFinish);
    mbFinished = true;
}

bool Viewer::isFinished()
{
    unique_lock&lt;mutex&gt; lock(mMutexFinish);
    return mbFinished;
}

void Viewer::RequestStop()
{
    unique_lock&lt;mutex&gt; lock(mMutexStop);
    if(!mbStopped)
        mbStopRequested = true;
}

bool Viewer::isStopped()
{
    unique_lock&lt;mutex&gt; lock(mMutexStop);
    return mbStopped;
}

bool Viewer::Stop()
{
    unique_lock&lt;mutex&gt; lock(mMutexStop);
    unique_lock&lt;mutex&gt; lock2(mMutexFinish);

    if(mbFinishRequested)
        return false;
    else if(mbStopRequested)
    {
        mbStopped = true;
        mbStopRequested = false;
        return true;
    }

    return false;

}

void Viewer::Release()
{
    unique_lock&lt;mutex&gt; lock(mMutexStop);
    mbStopped = false;
}

}</code></pre>

---

## Post #14 by @lassoan (2017-06-16 18:18 UTC)

<p>Without timestamp updates, Slicer may reject messages as duplicates. Keep timestamp up-to-date, as it is shown in OpenIGTLink examples.</p>
<pre><code>  igtl::TimeStamp::Pointer ts = igtl::TimeStamp::New();
  ...

  ts-&gt;GetTime();
  transMsg-&gt;SetTimeStamp(ts);</code></pre>

---

## Post #15 by @f.cnunez (2017-06-16 18:26 UTC)

<p>Now it works, thank you very much. I do what you say and also I created a new transmsg for each iteration</p>

---
