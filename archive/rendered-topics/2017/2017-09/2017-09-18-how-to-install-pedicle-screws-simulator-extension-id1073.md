---
topic_id: 1073
title: "How To Install Pedicle Screws Simulator Extension"
date: 2017-09-18
url: https://discourse.slicer.org/t/1073
---

# How to install pedicle screws simulator extension?

**Topic ID**: 1073
**Date**: 2017-09-18
**URL**: https://discourse.slicer.org/t/how-to-install-pedicle-screws-simulator-extension/1073

---

## Post #1 by @kevincool98 (2017-09-18 01:08 UTC)

<p>Operating system:mac<br>
Slicer version:4.7<br>
Expected behavior: a new downloaded extension for pedicle screws simulator ,I saw the video about that on youtube, and expected it work in 3d slicer.<br>
Actual behavior:i found the extension in GitHub,and download the zip file directly.but it can’t be loaded into 3d slicer as an extension,the tip is as the follow:No extension description found in archive ‘/Users/gujiyong/Desktop/PedicleScrewSimulator-master.zip’.what is wrong with that and what should I do ?appreciate for your help! thank you!</p>

---

## Post #2 by @lassoan (2017-09-18 01:24 UTC)

<p>I’ve invited <a href="https://uwaterloo.ca/mechanical-mechatronics-engineering/about/people/s2mclach">Stewart McLachlin</a>, the author of the <a href="https://github.com/smclach/PedicleScrewSimulator">pedicle screw simulator module</a>, to answer this question here. I hope we’ll hear from him soon.</p>

---

## Post #3 by @kevincool98 (2017-09-18 03:37 UTC)

<p>It’s very kind of you to reply so soon,thank you professor lassoan.<br>
and the video link is :  <a href="https://youtu.be/XN3Tp8jaYdQ" rel="nofollow noopener">https://youtu.be/XN3Tp8jaYdQ</a><br>
It is amazing,isn’t it?</p>

---

## Post #4 by @smclachlin (2017-09-18 13:38 UTC)

<p>Thanks for your interest in this project. We are currently working towards getting this project ready for the Extension Manager and should have something available for you to use soon. There have been many improvements since the video of the Slicer 4.2 version was posted on youtube in 2014. This is the main reason why the module no longer works since there have been a number of big changes (vtk, markups, etc.) since 4.2 was released.</p>

---

## Post #5 by @kevincool98 (2017-09-18 14:11 UTC)

<p>oh, that is it. thanks for your reply,professor smclashlin,and I am looking forward your new project because that is very very amazing and wonderful!</p>

---

## Post #6 by @lassoan (2017-09-18 19:34 UTC)

<p>I’ve fixed trivial issues in my fork and converted the module to a full extension that works with latest version of Slicer.</p>
<p>If you merge [this pull request] (<a href="https://github.com/smclach/PedicleScrewSimulator/pull/4">https://github.com/smclach/PedicleScrewSimulator/pull/4</a>) and update the icon and description of the extension then I can submit it to the extension manager.</p>

---

## Post #7 by @kevincool98 (2017-09-19 00:43 UTC)

<p>thank you for your help. however I download your fixed extension,but the problem is not solved.maybe my work step is not right, can you help me with that? I downloaded your zip file in GitHub,and open 3d slicer—extension manager–install extension from file–the downloaded zip file, but the same problem appeared:No extension description found in archive ‘/Users/gujiyong/Desktop/PedicleScrewSimulator-master.zip.shall I downloaded other extension first?thank you!</p>

---

## Post #8 by @lassoan (2017-09-19 00:58 UTC)

<p>Extension package is not generated yet - it needs merging of pull request and improving icon and documentation. It is not a lot of work, so I hope it’ll be done soon.</p>
<p>In the meantime, if you want a preview of how the extension will work then you can download all the files (clone the repository; or download as a zip and unzip to a local folder) and in <code>Application settings</code> / <code>Modules</code> add the directory that contains <a href="http://PedicleScrewSimulator.py">PedicleScrewSimulator.py</a> to <code>Additional module paths</code>.</p>

---

## Post #9 by @kevincool98 (2017-09-19 05:08 UTC)

<p>got it, i will try to do it.thank you.best wish to you,i hope the extension will be done and used soon.</p>

---

## Post #10 by @kevincool98 (2017-09-23 05:25 UTC)

<p>hello professor smclachlin, i saw the files about this extension have been updated in GitHub，does it mean that I can use it in 3d-slicer? thank you</p>

---

## Post #11 by @lassoan (2017-09-23 18:59 UTC)

<p>It’ll be improved but you can use it already. For now you have to download and add the extension to the module paths as described above.</p>

---

## Post #12 by @kevincool98 (2017-09-24 03:25 UTC)

<p>yeah,it works! it is incredible to me! thank you both!<br>
however, what should I do if I need some other  screws with different scales? for example screws with length 30mm.35mm.40mm.45mm,and width 50mm,55mm,60mm,65mm,70mm,75mm.<br>
further more,i appreciate if add some size of screws  for cervical vertebra.thank you very much!</p>

---

## Post #13 by @lassoan (2017-09-24 04:33 UTC)

<p>You have the full source code of the module. Feel free to edit it and add the models you need. If you make any improvements to the module, please consider contributing back those by sending pull requests.</p>

---

## Post #14 by @kevincool98 (2017-09-24 06:22 UTC)

<p>ok, i see,thank you again.<img src="https://emoji.discourse-cdn.com/twitter/grin.png?v=5" title=":grin:" class="emoji" alt=":grin:"><img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=5" title=":grinning:" class="emoji" alt=":grinning:"></p>

---

## Post #15 by @ezproxy (2018-08-12 17:43 UTC)

<p>It is  very good for us.</p>
<p>Thanks,everyone.<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/96f7847b118fb041268418a884113d8fe1200bf7.gif" alt="PedicleScrewSimulator" data-base62-sha1="lxvVjhCryWe0dijv90tL43OAClF" width="488" height="370"></p>

---

## Post #16 by @Saha_Saha (2018-08-14 17:14 UTC)

<p>Could someone tell me what this module is not working properly in my PC? When I try to load screw it is giving me the error message attached below. I can’t load screw. What Shoul I do?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b8edb2bf723dc6d987344446abe39ddb16ecb63.png" data-download-href="/uploads/short-url/mc84HkcjBXQHU3EHzr2wNmzlRmP.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9b8edb2bf723dc6d987344446abe39ddb16ecb63_2_690x460.png" alt="image" data-base62-sha1="mc84HkcjBXQHU3EHzr2wNmzlRmP" width="690" height="460" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9b8edb2bf723dc6d987344446abe39ddb16ecb63_2_690x460.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9b8edb2bf723dc6d987344446abe39ddb16ecb63_2_1035x690.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9b8edb2bf723dc6d987344446abe39ddb16ecb63_2_1380x920.png 2x" data-dominant-color="C6C4C6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2256×1504 530 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #17 by @lassoan (2018-08-14 22:54 UTC)

<p>I’ve fixed the issue, see the updated extension here: <a href="https://github.com/lassoan/PedicleScrewSimulator">https://github.com/lassoan/PedicleScrewSimulator</a></p>
<p>I’ve also submitted it to the extension manager, so it may be available in the extension manager from tomorrow.</p>

---

## Post #18 by @Saha_Saha (2018-08-15 15:25 UTC)

<p>Thank you very much.</p>
<p>I am still getting error to load sample CT. Inaddition, it is loading screw in opposite direction (from anterior to the direction of posterior). Please find attached picture for your consideration.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e8a876179439a83a48554a73f3b37092b5e7869d.png" data-download-href="/uploads/short-url/xcbHo45xolnCVZa3nY2JszRrUO9.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e8a876179439a83a48554a73f3b37092b5e7869d_2_690x460.png" alt="image" data-base62-sha1="xcbHo45xolnCVZa3nY2JszRrUO9" width="690" height="460" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e8a876179439a83a48554a73f3b37092b5e7869d_2_690x460.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e8a876179439a83a48554a73f3b37092b5e7869d_2_1035x690.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e8a876179439a83a48554a73f3b37092b5e7869d_2_1380x920.png 2x" data-dominant-color="AEABAD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2256×1504 406 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e4b4af1e6db0a9caffe8f2113c9efd009facfc96.png" data-download-href="/uploads/short-url/wDdYzRts0VQgQ2fZ2R9DjO541uu.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e4b4af1e6db0a9caffe8f2113c9efd009facfc96_2_690x460.png" alt="image" data-base62-sha1="wDdYzRts0VQgQ2fZ2R9DjO541uu" width="690" height="460" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e4b4af1e6db0a9caffe8f2113c9efd009facfc96_2_690x460.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e4b4af1e6db0a9caffe8f2113c9efd009facfc96_2_1035x690.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e4b4af1e6db0a9caffe8f2113c9efd009facfc96_2_1380x920.png 2x" data-dominant-color="C2C3DD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2256×1504 404 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #19 by @pieper (2018-08-15 17:57 UTC)

<aside class="quote no-group quote-modified" data-username="Saha_Saha" data-post="18" data-topic="1073">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/3d9bf3/48.png" class="avatar"> Saha_Saha:</div>
<blockquote>
<p>I still getting error to load sample CT.</p>
</blockquote>
</aside>
<p>It could be the download was incomplete or corrupted - try deleting the file (path is in the python output) and trying again.</p>

---

## Post #20 by @JoeCrozier (2018-08-17 15:47 UTC)

<p>I know you just said this two days ago, but I’m eager to install this and I can’t find it in the extension manager yet.  I also tried downloading it from the git, then going to application settings-&gt;modules-&gt;add module path to do it that way but Slicer just won’t seem to recognize that there is anything there.  Any idea what I might be doing wrong?</p>
<p>Running slicer 4.9.0</p>

---

## Post #21 by @lassoan (2018-08-18 07:48 UTC)

<p>PedicleScrewInsertion extension is now available in the extension manager for latest nightly builds, in Training category (or by entering “pedicle” in the search box).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3eea4b47f6190133fe9532e34669b784fdf331d.png" data-download-href="/uploads/short-url/ueQ2jyJEkzn4h895oiiNd5nt39X.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d3eea4b47f6190133fe9532e34669b784fdf331d_2_571x500.png" alt="image" data-base62-sha1="ueQ2jyJEkzn4h895oiiNd5nt39X" width="571" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d3eea4b47f6190133fe9532e34669b784fdf331d_2_571x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d3eea4b47f6190133fe9532e34669b784fdf331d_2_856x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d3eea4b47f6190133fe9532e34669b784fdf331d_2_1142x1000.png 2x" data-dominant-color="F5F7F9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1637×1432 168 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #23 by @Saha_Saha (2018-08-19 20:21 UTC)

<p>Thanks to all. I found the solution. I changed the transformation matrix.</p>

---

## Post #24 by @JoeCrozier (2018-08-20 12:01 UTC)

<p>Ah, didn’t realize I would need absolutely latest nightly build.  I had 4.9.0 from a previous build and it wasn’t showing up in there.  Thank you.</p>

---

## Post #25 by @juandp77 (2019-04-17 16:04 UTC)

<p>Hello I’m getting this error. Can somebody help me?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e47e0594391438102fda008666c088cce0d019a.png" data-download-href="/uploads/short-url/fJAw03MnmtMX6LN9txdEE2qnb7k.png?dl=1" title="40" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e47e0594391438102fda008666c088cce0d019a_2_690x109.png" alt="40" data-base62-sha1="fJAw03MnmtMX6LN9txdEE2qnb7k" width="690" height="109" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e47e0594391438102fda008666c088cce0d019a_2_690x109.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e47e0594391438102fda008666c088cce0d019a_2_1035x163.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e47e0594391438102fda008666c088cce0d019a_2_1380x218.png 2x" data-dominant-color="FEEAEA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">40</span><span class="informations">2216×352 81.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #26 by @lassoan (2019-04-17 16:14 UTC)

<p>Thanks for reporting the error. We’ll soon update this extension to work with Slicer-4.11 (that is switched to Python3). Until it is done, please use the latest stable version (Slicer-4.10.1).</p>

---

## Post #27 by @lassoan (2019-04-17 20:51 UTC)

<p>Pedicle screw simulator extension is now updated for Slicer-4.11. If you download the nightly build tomorrow or later then you should not see the error anymore.</p>

---

## Post #28 by @CHRIS_HUYNH (2020-03-28 17:18 UTC)

<p>Hi,</p>
<p>Im curious about getting the orthogonal slice views when im adjusting the positioning of the pedicle screws? I seem to only have access to the 3D Modelled view.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/49600485535b38b9b1776476fe69132718be0a02.jpeg" data-download-href="/uploads/short-url/at6ztEfQx2BwJIXKeY3ofnSg5xM.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/49600485535b38b9b1776476fe69132718be0a02_2_690x378.jpeg" alt="image" data-base62-sha1="at6ztEfQx2BwJIXKeY3ofnSg5xM" width="690" height="378" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/49600485535b38b9b1776476fe69132718be0a02_2_690x378.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/49600485535b38b9b1776476fe69132718be0a02_2_1035x567.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/49600485535b38b9b1776476fe69132718be0a02_2_1380x756.jpeg 2x" data-dominant-color="A6A6BB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1903×1044 466 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>theres no option to view the CT scanned orthogonal sliced views. I’d like to be able to adjust the position of the pedicle screw in the other views as it would be easier to visualize.</p>

---

## Post #29 by @lassoan (2020-03-28 17:52 UTC)

<p>The goal of the simulator is to teach surgeons assessing screw placement by looking at exposed bones. That’s why slice views are not shown by default in the screw placement step.</p>
<p>You can switch to 4-up view (orthogonal slice views + 3D view) anytime. I think this view is offered by default in the evaluation step. Since this is a Python scripted module, you can also very easily change the default behavior (just edit the Python files with a text editor and restart Slicer).</p>

---

## Post #30 by @CHRIS_HUYNH (2020-03-29 06:28 UTC)

<p>Hi lassoan,</p>
<p>Thank you for your reponse. I was thinking about using this for a thesis project on robotic assitance with pedicle screw fixation. Would you be able to help me set up these orthogonal views in python to allow adjustments of these pedicle screws in these orthognal sliced views.</p>
<p>Similar to how it is shown in this video <a href="https://youtu.be/XN3Tp8jaYdQ?t=104" rel="nofollow noopener">https://youtu.be/XN3Tp8jaYdQ?t=104</a></p>

---

## Post #31 by @lassoan (2020-03-30 05:04 UTC)

<p>You can switch to 4-up layout (3 slice views+3D view) by <code>slicer.app.layoutManager().setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutFourUpView)</code>. You can find many more examples in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository">Slicer script repository</a> and Slicer Python scripting tutorials <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials">here</a>.</p>
<p>Sounds like an interesting project. Slicer is quite often used for planning and real-time visualization of robot-assisted procedures, so you will find that all the infrastructure has been already developed and you just need to configure it for your project. Of course this customization is not that simple, but still much simpler than redeveloping everything from scratch. You can also very easily customize and extend existing features to do exactly what you need and how you need.</p>
<p>For pedicle screw insertion interventions, the pedicle screw simulator extension is a good starting point. Since it is implemented in Python, it is easy to customize/extend it. For example, you can add a patient calibration step to register your robot coordinate system to the image coordinate system using landmarks or surface registration. I would also recommend to have a look at <a href="http://www.slicerigt.org/wp/user-tutorial/">SlicerIGT tutorials</a> to learn about all the calibration and real-time visualization tools. You can connect Slicer with ROS nodes (to receive real-time robot position information or send target positions) using <a href="http://openigtlink.org/">OpenIGTLink protocol</a>.</p>

---

## Post #32 by @CHRIS_HUYNH (2020-03-30 06:17 UTC)

<p>Hi Mr Lasso,</p>
<p>Thank you so much for your reply and thank you for directing me towards the correct path. I definitely do feel like 3D Slicer would be beneficial to use for the project that I’m working on and I’ll definitely look into it further. If I have any questions regarding the project would you be the first line of contact?</p>
<p>Also greetings from Australia! hope you and your family are safe and well.</p>
<p>Regards,</p>
<p>Christopher</p>

---

## Post #33 by @lassoan (2020-03-30 20:17 UTC)

<aside class="quote no-group" data-username="CHRIS_HUYNH" data-post="32" data-topic="1073">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chris_huynh/48/6392_2.png" class="avatar"> CHRIS_HUYNH:</div>
<blockquote>
<p>If I have any questions regarding the project would you be the first line of contact?</p>
</blockquote>
</aside>
<p>Feel free to send any questions to this forum.</p>
<aside class="quote no-group" data-username="CHRIS_HUYNH" data-post="32" data-topic="1073">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chris_huynh/48/6392_2.png" class="avatar"> CHRIS_HUYNH:</div>
<blockquote>
<p>Also greetings from Australia! hope you and your family are safe and well.</p>
</blockquote>
</aside>
<p>So far we are OK here - Canada has not been hit very hard yet.</p>

---
