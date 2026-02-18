# Slicer 4.10.2 Not responding on Windows 10 (blank screen on older laptop)

**Topic ID**: 7469
**Date**: 2019-07-08
**URL**: https://discourse.slicer.org/t/slicer-4-10-2-not-responding-on-windows-10-blank-screen-on-older-laptop/7469

---

## Post #1 by @sim.zanoni (2019-07-08 17:24 UTC)

<p>Hi All,</p>
<p>After having used Slicer 4.8.1 on Mac OS X for about 2 years, I recently had the need to move to Windows 10. I choose to download the latest version 4.10.2, however, as soon as I run it, it crash displaying a blank white screen and not responding.<br>
Is there any log file I can check? Am I ignoring any incompatibility between Windows 10 and Slicer?</p>
<p>Thanks</p>

---

## Post #2 by @pieper (2019-07-08 17:49 UTC)

<p>Hi - It should work fine on windows 10 (it does for me).  The log files are stored in your windows user account under AppData/Local/Temp/Slicer.  It might be something to do with your graphics driver.  You could also try the preview build.</p>

---

## Post #3 by @sim.zanoni (2019-07-08 23:21 UTC)

<p>Hi Steve,</p>
<p>Thanks for your reply. This is my log.</p>
<pre><code class="lang-auto">*[DEBUG][Qt] 09.07.2019 08:49:55 [] (unknown:0) - Session start time .......: 2019-07-09 08:49:55*
*[DEBUG][Qt] 09.07.2019 08:49:55 [] (unknown:0) - Slicer version ...........: 4.10.2 (revision 28257) win-amd64 - installed release*
*[DEBUG][Qt] 09.07.2019 08:49:55 [] (unknown:0) - Operating system .........: Windows /  Professional /  (Build 9200) - 64-bit*
*[DEBUG][Qt] 09.07.2019 08:49:55 [] (unknown:0) - Memory ...................: 32611 MB physical, 37475 MB virtual*
*[DEBUG][Qt] 09.07.2019 08:49:55 [] (unknown:0) - CPU ......................: GenuineIntel , 16 cores, 16 logical processors*
*[DEBUG][Qt] 09.07.2019 08:49:55 [] (unknown:0) - VTK configuration ........: OpenGL2 rendering, TBB threading*
*[DEBUG][Qt] 09.07.2019 08:49:55 [] (unknown:0) - Developer mode enabled ...: no*
*[DEBUG][Qt] 09.07.2019 08:49:55 [] (unknown:0) - Prefer executable CLI ....: yes*
*[DEBUG][Qt] 09.07.2019 08:49:55 [] (unknown:0) - Additional module paths ..: (none)*
*[DEBUG][Python] 09.07.2019 08:50:01 [Python] (C:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations*
*[DEBUG][Python] 09.07.2019 08:50:02 [Python] (C:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor*
*[DEBUG][Python] 09.07.2019 08:50:02 [Python] (C:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics*
*[DEBUG][Qt] 09.07.2019 08:50:02 [] (unknown:0) - Switch to module:  "Welcome"*
</code></pre>
<p>However, in switching to “Welcome” module it actually turns to a blank white screen and, if I click on it, it goes to “Not Responding” status and it doesn’t append any log in the file.<br>
I tried with the preview release, but the behaviour is the same.</p>
<p>If it can help, my graphics card is Intel(R) UHD Graphics 630 and these are the drivers:</p>
<ul>
<li><code>igdumdim64.dll</code></li>
<li><code>igd10iumd64.dll</code></li>
<li><code>igd10iumd64.dll</code></li>
<li><code>igd12umd64.dll</code></li>
</ul>
<p>Is there any other check I could do?</p>

---

## Post #4 by @lassoan (2019-07-08 23:55 UTC)

<p>Try latest Preview release of Slicer and these instructions: <a href="https://discourse.slicer.org/t/slicer-nightly-version-does-not-launch-on-windows/2758" class="inline-onebox">Slicer nightly version does not launch on windows</a> and let us know what you find.</p>

---

## Post #5 by @sim.zanoni (2019-07-09 01:40 UTC)

<p>I’ve erased Slicer.ini and Slicer-NNN.ini files and downloaded the latest preview. At first run of Slicer, it doesn’t crash. However, at this stage Slice put new Slicer.ini and Slicer-NNN.ini back and if I try to open it again it crashes. Basically, I need to erase those files to be able to run it again.</p>
<p>I haven’t tried to install Paraview yet. If you think it could help in understanding the issue, I can do that.</p>

---

## Post #6 by @sim.zanoni (2019-07-09 02:47 UTC)

<p>I’ve installed ParaView 5.7.0 anyway and it works properly.</p>

---

## Post #7 by @lassoan (2019-07-09 03:17 UTC)

<p>Do you have multiple monitors connected? Have you installed any extensions or Python packages? Is there any error/warning in the application log? (you can find log of previous sessions in menu: Help / Report a bug - then select a session in the listbox).</p>

---

## Post #8 by @sim.zanoni (2019-07-09 03:49 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="7469">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Do you have multiple monitors connected?</p>
</blockquote>
</aside>
<p>Yes, actually I have and I’ve just noticed that if I keep it on my main monitor I don’t need to erase .ini files to run it again. Is there anyway a way around that?</p>
<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="7469">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Have you installed any extensions or Python packages?</p>
</blockquote>
</aside>
<p>Not yet, but I possibly will.</p>
<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="7469">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Is there any error/warning in the application log?</p>
</blockquote>
</aside>
<p>All the logs look like the one I pasted above. When I tried to access the Extension Manager from the second monitor a ’ <em>[DEBUG][Qt] 09.07.2019 13:35:37 [] (unknown:0) - Switch to module:  “”</em> ’ has been appended.</p>

---

## Post #9 by @lassoan (2019-07-09 03:54 UTC)

<aside class="quote no-group" data-username="sim.zanoni" data-post="8" data-topic="7469">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sim.zanoni/48/2983_2.png" class="avatar"> sim.zanoni:</div>
<blockquote>
<p>Yes, actually I have and I’ve just noticed that if I keep it on my main monitor I don’t need to erase .ini files to run it again. Is there anyway a way around that?</p>
</blockquote>
</aside>
<p>This is very useful hint. Most probably Qt has issues restoring Slicer main window size. Probably you have somewhat unusual configuration, such as one monitor is HiDPI and the other is not; or their size is very different. Could you give us some information about resolution and physical size of your displays?</p>
<p>As a workaround, you can disable saving/restoring of window position in menu: Edit / Application settings / Appearance / Save user interface size and position on exit.</p>

---

## Post #10 by @sim.zanoni (2019-07-09 04:28 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="7469">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Could you give us some information about resolution and physical size of your displays?</p>
</blockquote>
</aside>
<p>The main one is 1920x1080 23’‘; the second is 1680x1050 22’'. I’m happy to give more details, if needed.</p>
<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="7469">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>As a workaround, you can disable saving/restoring of window position in menu: Edit / Application settings / Appearance / Save user interface size and position on exit.</p>
</blockquote>
</aside>
<p>This will definitely help.</p>
<p>Thank you very much for your help.</p>

---

## Post #11 by @Sci-Fi (2020-10-19 18:10 UTC)

<p>I’ve been having the same problem, it does seem to be an issue with one of my monitors (I have 3, all 1920x1080).  Slic3r 1.3.0, windows 10.<br>
On my main monitor, everything works fine.  If the window opens on the right monitor I get “Not Responding”.  Haven’t tried the left one, thats my netflix monitor <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"><br>
I’ve been using slic3r for a long time, but this issue seems new to me.  I will disable saving/restoring of window position for now, but hopefully it can get resolved at some point.</p>

---

## Post #12 by @lassoan (2020-10-19 18:13 UTC)

<p>Which application are you referring to: <a href="https://slic3r.org/">slic3r</a> or <a href="https://slicer.org">3D Slicer</a>?</p>

---

## Post #13 by @muratmaga (2020-10-19 18:27 UTC)

<p>Sorry this forum is for 3D Slicer not for Slic3r.</p>

---

## Post #14 by @Andres (2021-05-20 23:41 UTC)

<p>Hi there. I am having exactly the same issue with preview release 4.13.0 2021-05-19.  after starting the program, it appears a blank white screen and do no more.</p>
<p>I have installed the program in Windows 10 home version 1709 (64 bit), in my laptop dell inspiron n411z.</p>
<p>But, what is even more curious.  All the menus, toolboxes and modules are there, just that they do not appear on screen. I noticed it when started clicking on the blank white screen. have a look in the attached image.</p>
<p>What could I check to solve this?   regards<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/4635fac4ee38d2dcf3178334cd6cf4ad485bd84c.jpeg" data-download-href="/uploads/short-url/a174z00t561y9PoyMF0UQXZHIiE.jpeg?dl=1" title="screen" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4635fac4ee38d2dcf3178334cd6cf4ad485bd84c_2_690x386.jpeg" alt="screen" data-base62-sha1="a174z00t561y9PoyMF0UQXZHIiE" width="690" height="386" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4635fac4ee38d2dcf3178334cd6cf4ad485bd84c_2_690x386.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4635fac4ee38d2dcf3178334cd6cf4ad485bd84c_2_1035x579.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4635fac4ee38d2dcf3178334cd6cf4ad485bd84c_2_1380x772.jpeg 2x" data-dominant-color="F7F5F2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">screen</span><span class="informations">1422×796 36.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #15 by @jamesobutler (2021-05-21 00:11 UTC)

<p>Hi <a class="mention" href="/u/andres">@Andres</a> the latest Slicer Preview requires a newer set of hardware. Generally Slicer works well on hardware that is 5 years or newer. See<br>
<a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#system-requirements" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#system-requirements</a></p>
<p>Unfortunately I suspect your computer which is originally from 2011 to be too old to run Slicer. At this point that would make it 10 years old which is twice as old as what is recommended to use the latest Slicer version.</p>
<p>Do you have access to a newer computer to use the latest Slicer versions?</p>
<p>Have you tried Slicer 4.11.20210226 ?</p>

---

## Post #16 by @Andres (2021-05-21 00:22 UTC)

<p>Hi James.</p>
<p>I have updated my post.   As you can see, all is there but simply do not appear on screen.  Do you think I still need to install the older version?  or is maybe something else?  Unfortunately  right now I do not have access to a newer computer and I really need this latest Slicer release since as far as I know this is the one that can open scanco CT files (.isq).</p>
<p>Looking forward to your reply</p>

---

## Post #17 by @lassoan (2021-05-21 04:10 UTC)

<p>Until you can get a more recent computer, you can run Slicer on the cloud and access it from your web browser. There are computers that can run the latest version of Slicer and available to use for free, for anyone.</p>
<p>See link that opens Slicer on Binder (a free Jupyter notebook hosting provider) <a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html?highlight=Jupyter%20notebook#system-requirements">here</a>. This uses a Jupyter notebook image that was created a year ago, so it cannot open .isq files. However, you can build a new docker image by updating <a href="https://github.com/Slicer/SlicerDocker/tree/master/slicer-notebook">this dockerfile</a>.</p>
<p>If you don’t know and don’t want to learn using docker then you can find other cloud providers that allow accessing a regular desktop interface where you can download and install the latest Slicer version.</p>

---

## Post #18 by @muratmaga (2021-05-23 17:10 UTC)

<p><a class="mention" href="/u/andres">@Andres</a><br>
If your usage need is short-term, we are hosting a cloud instance based on the latest stable version of Slicer (along with a bunch of other extensions). If that works for you, please sign up here:</p><aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://ssl.gstatic.com/docs/spreadsheets/forms/favicon_qp2.png" class="site-icon" width="16" height="16">

      <a href="https://forms.gle/qdTerFcKEDYadYh69" target="_blank" rel="noopener">Google Docs</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:126/66;"><img src="https://lh6.googleusercontent.com/Rm7qsSvcxT8U2d1zZt9H8my_RPVGpLNNrN1PMgZuNO58plc8n47fFbaAcK1fe7Vsfzelmq9BkaA=w1200-h630-p" class="thumbnail" width="126" height="66"></div>

<h3><a href="https://forms.gle/qdTerFcKEDYadYh69" target="_blank" rel="noopener">SlicerMorphCloud user request</a></h3>

  <p>We will be running SlicerMorph on the Microsoft Azure as a short pilot. Please complete this form as best as you can to request an account. Make sure your email address is correct, so that we can get back to you with your account and access...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>and then I can create an account for you and send you the instructions.<br>
This is only available until end of June.</p>

---

## Post #19 by @Andres (2021-06-01 09:58 UTC)

<p>Hi Muratmaga.  Thanks for your support.  I have solved the issue by installing the software in a newer laptop. Thanks anyway.</p>

---

## Post #20 by @Yun_Chen (2022-05-02 10:22 UTC)

<p>Hi everyone, I had the same issue. When I open 3D Slicer, after the flashes loading all the modules and poping up the Slicer interface, the window white out and title shows “3D Slicer 4.11.20210226 (Not Responding)” no matter how long I wait. I have tried uninstall it, clear all the Slicer reigistries in “regedit” and reinstall the version 4.11 or 4.13. However the problem still exist.</p>
<p>It looks like the multiple monitor issue as mentioned above. When I disable a monitor and use only one, the 3D Slicer can open property. Then if I connect back to dual monitor, the already-opened 3D Slicer works fine. Not sure how to solve the issue better</p>

---

## Post #21 by @cpinter (2022-05-02 11:11 UTC)

<p>Please try 5.0, it will out this week.</p>
<p>Also, deleting the registry is a good idea, and along those lines, it may be useful trying to delete the <code>ini</code> file. It is located in <code>c:\Users\[YourUser]\AppData\Roaming\NA-MIC\</code></p>

---

## Post #22 by @zulfihaneef (2022-08-11 01:35 UTC)

<p>Thanks guys - this discussion helped me. For me the problem was my main monitor which had too high resolution 3840 x 2160 (new Windows 11 machine, good hardware specs). To resolve, I disconnected main monitor from display settings, opened 3D slicer, and reconnected display, and everything worked fine. Hope that helps somebody.</p>

---

## Post #23 by @juliangallaun (2022-10-13 09:50 UTC)

<p>I know this thread is older, but the problem also persists in version 5.1. But I fixed it as already mentioned, just switch to one screen, open 3DSlicer and then close it. Reconfigure your previous multi-window installation and when you open 3DSlicer again, it will open on your screen 1 without problem. I assume the problem occurred to begin with, when I started 3DSlicer on screen 1 and dragged the window to screen 2, worked there and closed it there. Reopening it again, the white non-responding window opened instantly on screen 2 and not as previous at screen 1.</p>

---

## Post #24 by @pieper (2022-10-13 14:27 UTC)

<p>Perhaps related to <a href="https://github.com/Slicer/Slicer/issues/6568">this issue</a>.</p>

---
