# Problem with enabling remote debugging for both c++ and python

**Topic ID**: 398
**Date**: 2017-05-29
**URL**: https://discourse.slicer.org/t/problem-with-enabling-remote-debugging-for-both-c-and-python/398

---

## Post #1 by @zp12132016 (2017-05-29 12:36 UTC)

<p>Operating system:windows10<br>
Slicer version:slicer 4.6.2<br>
Expected behavior: Expect the  debug working for both c++ and python scripts<br>
Actual behavior: the remote Debug is not working</p>
<p>Hi Slicer supporters, firstly I would like to ask some questions regarding the possibility of using slicer for my application, then I would ask some thing about setting the debug working.</p>
<p>I would like to use slicer in 3d application. In such application, I need to do the following:</p>
<p>-I would like to change the layout of 3D volume “Dual 3D” in to full screen, which means I need to change all the GUI and only show the left and right rendered volume without R, Y, G and any other panels. Is possible to do this and could you give some suggestions where I have to modify inside the slicer scripts?</p>
<p>-Then  I would like to synchronize the the two views of the “Dual 3D”, currently only one is active and I have read in slicer 3 that is the limitation of the Slicer software. Here I have another question: Is possible to make the two view synchronized or two camera synchronized?</p>
<p>ISSUES WITH REMOTE DEBUGGING:<br>
1.I have followed the build instructions to build Qt 4.8.7 debug mode successfully by using the following information :</p>
<p>Visual Studio 2013 with Update 5, as of commit 7160260: Slicer compilation is successful, with some caveats.<br>
CMake &gt;= 3.3.1<br>
Build Qt 4.8.7 with SSL support using qt-easy-build.<br>
For Debug mode, disable Slicer_USE_SimpleITK in CMake.</p>
<ol start="2">
<li>
<p>Then I did the 3 steps listed in the checkout slicer source files<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions</a></p>
</li>
<li>
<p>then followed Per-platform instructions (windows) to build the “ALL_BUILD” project  successfully with debug mode.<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions</a></p>
</li>
<li>
<p>Then I open Slicer.sln in visual studio and select debug as build configure, and build again, everything is fine.</p>
</li>
</ol>
<p>Then use liclipse 3.6.0 with java 8, and Eclipse to Neon.3 (4.6.3). to set the debug tool by doing the following</p>
<ol>
<li>Slicer-&gt;Edit-&gt;Application settings-&gt;Modules-&gt;Additional module paths:<br>
1a. Add location of your .py file(s)<br>
1b. Restart Slicer</li>
<li>In LiClipse, Start Debug Server (see module wiki page for instructions)</li>
<li>In Slicer-&gt;Modules-&gt;Developer tools-&gt;Python debugger-&gt;Connect</li>
<li>In LiClipse, Open the debug window: in the menu Window &gt; Open Perspective &gt; Other &gt; Debug<br>
4a. MAKE SURE DEBUG TAB IS SHOWING!!!</li>
<li>Resume when it pauses</li>
<li>Open .py file(s) from Additional module paths: above in LiClipse</li>
<li>Debug</li>
</ol>
<p>However, I tried  the HelloPython module from the slicer tutorial, it worked a couple of time, then does not work any more.</p>
<p>For Debugging in C++, I used the right version of pip, and ptvsd, and I also set TCP port (5678) of slicer.exe in fire wall, then I followed the following steps:<br>
In Visual Studio, select Debug &gt; Attach to Process to display the Attach to Process window, then:<br>
Choose Python remote (ptvsd) as the Transport.<br>
Enter “tcp://slicer@localhost” as the Qualifier. Here, “slicer” should match the secret specified in enable_attach().<br>
Press Enter or click Refresh. The Slicer process should appear in the list below. Select the Slicer process and click Attach.</p>
<p>Once the debugger attaches, you can use breakpoints, step through the code, and examine variables in the Watch window.</p>
<p>However, the problem is that the debugger is never attached because the Slicer process did not appear in the list and the Attach button is not active.</p>
<p>I really hope you can help me with my first two questions and the debug issues.</p>
<p>Thanks !!</p>
<p>Best regards</p>
<p>zen</p>

---

## Post #2 by @lassoan (2017-05-29 12:50 UTC)

<aside class="quote no-group" data-username="zp12132016" data-post="1" data-topic="398">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/z/ec9cab/48.png" class="avatar"> zp12132016:</div>
<blockquote>
<p>I would like to change the layout of 3D volume “Dual 3D” in to full screen, which means I need to change all the GUI and only show the left and right rendered volume without R, Y, G and any other panels. Is possible to do this and could you give some suggestions where I have to modify inside the slicer scripts</p>
</blockquote>
</aside>
<p>See this example how to switch between showing a single module / showing the usual Slicer user interface: <a href="https://github.com/SlicerIGT/SlicerIGT/blob/master/Guidelet/GuideletLib/Guidelet.py#L415-L439" class="inline-onebox">SlicerIGT/Guidelet/GuideletLib/Guidelet.py at master · SlicerIGT/SlicerIGT · GitHub</a></p>
<aside class="quote no-group" data-username="zp12132016" data-post="1" data-topic="398">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/z/ec9cab/48.png" class="avatar"> zp12132016:</div>
<blockquote>
<p>Is possible to make the two view synchronized or two camera synchronized?</p>
</blockquote>
</aside>
<p>Use the same camera node for both views: Go to Cameras module. Select View: View2, Camera: the first “Default Scene Camera” in the list (unfortunately, by default both camera views have the same name).</p>
<aside class="quote no-group" data-username="zp12132016" data-post="1" data-topic="398">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/z/ec9cab/48.png" class="avatar"> zp12132016:</div>
<blockquote>
<p>However, I tried  the HelloPython module from the slicer tutorial, it worked a couple of time, then does not work any more.</p>
</blockquote>
</aside>
<p>If you need help with this then you have to describe what steps you do, what you expect, and what happens actually.</p>
<aside class="quote no-group" data-username="zp12132016" data-post="1" data-topic="398">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/z/ec9cab/48.png" class="avatar"> zp12132016:</div>
<blockquote>
<p>However, the problem is that the debugger is never attached because the Slicer process did not appear in the list and the Attach button is not active.</p>
</blockquote>
</aside>
<p>For Debugging in C++, you don’t need pip, ptvsd, etc. It will not be a remote debugging but a direct attachment to the process. In Visual Studio menu select: Debug / Attach process. In the window that is displayed all processes that are running on your computer are listed in “Available processes”, so if Slicer is running then you’ll see it. There are two processes for Slicer: Slicer.exe and SlicerApp-real.exe. Select SlicerApp-real.exe.</p>

---

## Post #3 by @zp12132016 (2017-05-29 13:41 UTC)

<p>Hi Andras,</p>
<p>Thanks very much for your kind reply and detail explain.</p>
<p>For synchronizing the camera, I tried like this, go to module Cameras-&gt; select view2, camera “I use Default Scene camera”, however, when I move one of the rendered volume, the other one is not moving. I expect the other one moves identically when I move one of them, such as rotating, zooming.</p>
<p>For the python debug:</p>
<p>What I did as follows:<br>
1.Set remote debug in LiClipse by go to : Window-&gt; Perspective-&gt;customize perspective-Action Set Availablity-&gt;tick python debug<br>
2. Then Window-&gt;Perspective-&gt;Open perspective-&gt;Other…-&gt;Select Debug<br>
3. Then I go to Edit-&gt;application setting-&gt;Module-&gt;add the fold directory contain the HelloPython script<br>
4. go to LiClipse -&gt;start the pydev server<br>
5. go to Slicer-&gt;develop tool-&gt;python debugger<br>
6. in the settings, I selete Eclise (since there are only two options, the other is Pycharm<br>
7. then find the pydevd.py directory<br>
8. the default port is 5678<br>
9. then click connect to Eclipse debugger<br>
10, then I open helloPython.py in LiClipse<br>
11. add a break point<br>
12. then I go to slicer, select the HelloPython from the example category, it happened one time, slicer paused and I see all debugged variables and slicer code completion. However, when I close the computer and I repeat again, it doesn’t work anymore.</p>
<p>If I did mistake or you have stable version that allow to debug python code, could you let me know?</p>
<p>Best regards</p>
<p>Zen</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/52e3d8429dc9df354e80745a95a85b3abf8eb09e.jpg" width="20" height="20"></p>

---

## Post #4 by @zp12132016 (2017-05-29 14:39 UTC)

<p>Hi Andras,</p>
<p>I have tried your suggestion in slicer for c++ debugging but I did not see slicer pause, or variables. The steps I did as follows:</p>
<p>I kept slicer open, then open VS 2013, then follow your instructions: go to Debug-&gt;attach to process-&gt;choose SlicerApp-real.exe, however I only saw some small watch window pop out and I do not see any variables and also slicer is not pause at all. I expect it will pause and show some variable values if I using  a module.</p>
<p>Then for the camera synchronizing:</p>
<p>I did the following as you said but  one of the camera is always static when I am moving the other one, the are not moving together and identically.</p>
<p>Best regards</p>
<p>Zhen</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/52e3d8429dc9df354e80745a95a85b3abf8eb09e.jpg" width="20" height="20"></p>

---

## Post #5 by @lassoan (2017-05-29 16:51 UTC)

<aside class="quote no-group" data-username="zp12132016" data-post="4" data-topic="398">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/z/ec9cab/48.png" class="avatar"> zp12132016:</div>
<blockquote>
<p>I kept slicer open, then open VS 2013, then follow your instructions: go to Debug-&gt;attach to process-&gt;choose SlicerApp-real.exe, however I only saw some small watch window pop out and I do not see any variables and also slicer is not pause at all. I expect it will pause and show some variable values if I using  a module.</p>
</blockquote>
</aside>
<p>Put a breakpoint in your code. When Slicer executes that line it’ll pause and show all variables.</p>
<aside class="quote no-group" data-username="zp12132016" data-post="4" data-topic="398">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/z/ec9cab/48.png" class="avatar"> zp12132016:</div>
<blockquote>
<p>I did the following as you said but  one of the camera is always static when I am moving the other one, the are not moving together and identically.</p>
</blockquote>
</aside>
<p>Can you record a screen capture video of how you do this and send a link to the video? On Windows, you can use PowerPoint to capture video of your screen (menu: Insert / Screen Recording).</p>

---

## Post #6 by @zp12132016 (2017-06-01 15:25 UTC)

<p>Hi Slicer developers,</p>
<p>Sorry to bother you with the python remote debug question as I build my  slicer again, it still has the same problem. Here I have a couple of questions:</p>
<p>-If anybody has made the remote debug working in LiClipse, could you tell me which Qt, Visual studio, and LiClipse version are you using?<br>
-If the remote debug can not work in LiClipse, could you tell me any other tool that you are using makes the debug successful?<br>
-If remote debug will not work with any tool, could you tell me how to effectively find the error of the scripted python module?</p>
<p>Best regards</p>
<p>Zen</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/52e3d8429dc9df354e80745a95a85b3abf8eb09e.jpg" width="20" height="20"></p>

---

## Post #7 by @pieper (2017-06-01 16:53 UTC)

<p>Hi Zen -</p>
<p>I don’t use any of the IDE or remote debugging options - to debug python code in Slicer I start with a scripted module from the extension wizard, then with Slicer in developer mode I use the Reload and Test  buttons and incrementally add functionality.</p>
<p>You can also use slicer.modules.Widget to access the module’s gui and from there you can typically inspect any variables and call any methods needed for debugging.</p>
<p>Hope that helps,<br>
Steve</p>

---

## Post #8 by @lassoan (2017-06-01 17:10 UTC)

<p>First of all: do you want to debug Python or C++ code? Python code is not visible to C++ debuggers, C++ code is not visible to Python debuggers.</p>
<ul>
<li>For C++ follow these instructions: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Debug_Instructions">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Debug_Instructions</a>
</li>
<li>For Python follow these instructions: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#How_can_I_use_a_visual_debugger_for_step-by-step_debugging">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#How_can_I_use_a_visual_debugger_for_step-by-step_debugging</a>
</li>
</ul>
<p>You need to follow the instructions very accurately. If you run into any issue, then please create a screen capture of what you did, upload to dropbox/onedrive/gdrive and attach the link and we can then tell what went wrong.</p>

---

## Post #9 by @zp12132016 (2017-06-01 21:13 UTC)

<p>Hi Steve,</p>
<p>Thanks very much! I am very new to slicer, what do you mean slicer in developer mode?</p>
<p>Do I still need to build slicer with Qt, visual studio or just download the slicer from official website is enough?</p>
<p>However, I will try your suggestion soon !</p>
<p>Thanks very much !</p>
<p>Zen</p>
<p>Get Outlook for iOS<a href="https://aka.ms/o0ukef" rel="nofollow noopener">https://aka.ms/o0ukef</a></p>

---

## Post #10 by @pieper (2017-06-01 22:39 UTC)

<p>Hi Zen -</p>
<p>In the Application Settings dialog (from the Edit menu):</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/606552aca646fd9cd736cf5ac9d829f8538f90b6.png" data-base62-sha1="dKKV4GY2RFNxFQgnSHXqLWDsEoS" width="427" height="213"></p>
<p>Then your scripted modules will have these options:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a942c736c46f9d71804a83a3e2866fdecee9381.png" data-base62-sha1="jLVlN3XK3I9q0r4we4Wof9p3m8x" width="640" height="173"></p>

---

## Post #11 by @pieper (2017-06-01 22:40 UTC)

<p>Of course this is only for the python code, but you can use this with any Slicer, either a binary download or one you build yourself.</p>
<p>If you want/need to debug C++ code then you need to build your Slicer from source.</p>

---

## Post #12 by @zp12132016 (2017-06-02 03:30 UTC)

<p>Hi Steve,</p>
<p>Thanks very much for your detail explain <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>Best regards</p>
<p>Zen</p>
<p>Get Outlook for iOS<a href="https://aka.ms/o0ukef" rel="nofollow noopener">https://aka.ms/o0ukef</a></p>

---

## Post #13 by @lassoan (2017-09-19 14:58 UTC)

<p>A post was split to a new topic: <a href="/t/how-reload-module-button-works/1085">How reload module button works?</a></p>

---
