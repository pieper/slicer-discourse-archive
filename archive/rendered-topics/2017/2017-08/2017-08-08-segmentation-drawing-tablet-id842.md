---
topic_id: 842
title: "Segmentation Drawing Tablet"
date: 2017-08-08
url: https://discourse.slicer.org/t/842
---

# Segmentation - Drawing Tablet

**Topic ID**: 842
**Date**: 2017-08-08
**URL**: https://discourse.slicer.org/t/segmentation-drawing-tablet/842

---

## Post #1 by @Kserralde (2017-08-08 20:52 UTC)

<p>I’ve used 3D slicer for generating 3D models.  I’ve used the wacom stylus and tablet for drawing the segments.  Wacom has a tablet where you can draw directly on the screen, which I think would be really useful in the segmentation process, especially for students with no drawing experience, it would provide more control.  Obviously, the threshold tool is extremely useful, but having more control when drawing is always helpful.</p>
<p><a href="http://www.wacom.com/en-us/products/pen-computers/wacom-mobilestudio-pro-16" class="onebox" target="_blank" rel="nofollow noopener">http://www.wacom.com/en-us/products/pen-computers/wacom-mobilestudio-pro-16</a></p>
<p><a href="http://www.wacom.com/en-us/products/pen-displays/cintiq-13-hd" class="onebox" target="_blank" rel="nofollow noopener">http://www.wacom.com/en-us/products/pen-displays/cintiq-13-hd</a></p>

---

## Post #2 by @lassoan (2017-08-08 21:06 UTC)

<p>Segment editor works well on Windows computers with stylus (and Surface Dial, etc.). You can draw directly on the screen on all Windows touch-enabled PCs and modern stylii are fast, highly sensitive and support tilting. Do you still need Wacom pen? Does Wacom pen work differently?</p>

---

## Post #3 by @hherhold (2017-08-09 13:50 UTC)

<p>I use a medium-sized wacom tablet/stylus (Wacom Intuos PTH-651) with a Mac laptop to do segmentations and it works great. I’ve customized pen buttons and tablet buttons for specific functions so I can quickly switch between paint and island removal (for example) to do segmentations. When you switch between functions a few hundred times a day, saving even a couple of seconds per operation adds up.</p>
<p>I’d be curious to hear about what workflow ideas others have for segmentations.</p>

---

## Post #4 by @Kserralde (2017-08-09 14:08 UTC)

<p>Have you seen the Wacom Cintiq?  I was wondering if you could use 3D slicer on it… I</p>
<p>I’m working on a medical imaging elective and I want the students without an “artistic” background as much control as possible. Because i’m in  medical library, I need a drawing system that interfaces with PC and MaC, but I like the idea of using a touch screen…</p>
<p>I’m working on models that can be presented in parts.<br>
<a href="https://3dprint.nih.gov/users/kserralde" class="onebox" target="_blank" rel="nofollow noopener">https://3dprint.nih.gov/users/kserralde</a></p>

---

## Post #5 by @lassoan (2017-08-09 23:46 UTC)

<p>Also note there are a number of keyboard shortcuts that you can use in Segment Editor: <a href="http://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html">http://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html</a></p>
<p>For example, a very effective shortcut is <code>space</code> key, which switches between last two effects (for example: paint/erase) or activates/deactivates an effect (for example: activate scissors/deactivate scissors so you can rotate the 3D view).</p>
<p>Let me know if you have any other suggestion for additional keyboard shortcuts that would make your workflow more efficient.</p>

---

## Post #6 by @hherhold (2017-09-06 01:25 UTC)

<p>Thanks Andras,</p>
<p>Sorry for the very slow reply. I use the space key shortcut constantly.</p>
<p>I was wondering if there’s a way to make the “Editable intensity range” checkbox a shortcut key. I turn it on and off all the time for efficiency - for brush erase and island removal, it runs noticeably faster when Editable intensity range is unchecked (one less compare per voxel adds up).</p>
<p>Any thoughts? I’m sure that adding shortcut keys can rapidly turn into feature creep, with everyone wanting shortcut keys for anything and everything.</p>
<p>Thanks,</p>
<p>-Hollister</p>

---

## Post #7 by @lassoan (2017-09-06 03:43 UTC)

<p>Thanks for the feedback. I’ve added a shortcut for toggling masking by master volume intensity by <code>i</code> key. It’ll be available in Thursday’s nightly build.</p>

---

## Post #8 by @hherhold (2017-09-07 13:28 UTC)

<p>Wow, this works GREAT!</p>
<p>I use a left-handed 3 button programmable mouse and a Wacom Intuos tablet. I’ve set up one pen button to select sphere brush and turn on Editable intensity range and a second to select remove islands and turn off Editable intensity range. This allows me to basically do all my editing functions with minimal mouse movement and I never have to reach for the keyboard (“HOTAS, or Hands On Throttle And Stick”, as they say in the aviation world - I have my mouse buttons customized for other functions to speed up workflow.)</p>
<p>This probably just saved me a couple of hours per week in just mouse movement and computation time (island removal with editable intensity range off is a lot faster than with it on).</p>
<p>Thanks again! You guys are awesome!</p>
<p>-Hollister</p>

---

## Post #13 by @guixia (2019-01-11 02:10 UTC)

<p>Zoom and rotation are possible on 3D view, and I will display sliders or arrow buttons to let the user translate the view.</p>
<p>To inform other users, I am using a XP-Pen Artist 12 drawing tablet with screen and Slicers is running perfectly, including volume rendering.</p>

---

## Post #14 by @lassoan (2019-01-11 03:09 UTC)

<aside class="quote no-group" data-username="guixia" data-post="13" data-topic="842">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/guixia/48/2853_2.png" class="avatar"> guixia:</div>
<blockquote>
<p>I will display sliders or arrow buttons to let the user translate the view</p>
</blockquote>
</aside>
<p>What do you mean? Display where?<br>
Using shift key, you should be able to translate the view.<br>
Does the tablet has programmable keys? If yes, then you can configure keyboard shortcuts for translating views.</p>

---

## Post #15 by @guixia (2019-01-11 03:26 UTC)

<p>xp-pen artist 12 display tablet has 6 programmable keys and I touch bar . 11.6 inch IPS Screen . 8192 levels of pen pressure . 5080LPI</p>

---

## Post #16 by @jcfr (2019-01-11 13:59 UTC)

<aside class="quote no-group" data-username="guixia" data-post="13" data-topic="842">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/guixia/48/2853_2.png" class="avatar"> guixia:</div>
<blockquote>
<p>Slicers is running perfectly, including volume rendering.</p>
</blockquote>
</aside>
<p>Could you share a video with Slicer running on the tablet ? This would be very informative.</p>

---

## Post #20 by @Leon (2019-05-15 18:07 UTC)

<p>From what I read here, many people use a drawing tablet in combination with Slicer. That also goes for me, but only when I’m working on a Windows machine.</p>
<p>At home my OS is with Linux Mint 19.1 and there I have an issue during segmentation.<br>
The cursor follows the pen nicely (although it’s appearance changes from a one-pointed arrow to a double-pointed arrow, and back again), but when I’m using to ‘paint’ or ‘erase’ tool, it starts to react veeeeeeery slow!<br>
I’ve tried two different Wacom drawing tablets (Volito and Intuos), but they both show the same problem.<br>
When I check my system settings, it just gives me the information whether I’m using the Volito, or the Intuos and the react normal to every action I take.</p>
<p>Other applications for which a drawing pen is very useful to use, like Gimp or Krita, don’t give any problems.</p>
<p>Is someone familiar with this problem on (other) Linux systems, or is only a Linux Mint issue?</p>

---

## Post #21 by @lassoan (2019-05-15 18:30 UTC)

<p>Can you post screenshots and/or videos? They could give some hints what could be the performance bottlenecks.</p>
<p>What graphics card so you have?</p>
<p>How is the performance if you use the same computer and tablets using Windows?</p>

---

## Post #22 by @Leon (2019-05-16 08:12 UTC)

<p>Hello Andras,</p>
<p>First of all I’ve checked if it was up to the computer itself.</p>
<p>At home I’m using a machine with the following hardware configuration:</p>
<ul>
<li>AMD FX 4350 processor</li>
<li>AMD Radeon R7 graphical card</li>
<li>8Gb ram</li>
<li>Linux Mint 19.1</li>
</ul>
<p>When I boot up with Linux I’m facing the problem that, when using the ‘paint’ or ‘erase’ option, the cursor lags very much and it takes many seconds to build up the selection/erasion.</p>
<p>At home I also have an external hard drive with Windows 7 professional installed on it and when I boot from this drive, using  the same computer, then I don’t face this problem. So you could say that i’ts not a hardware issue, can you?</p>
<p>At work I’m using a computer with this configuration:</p>
<ul>
<li>Intel Xeon E5-2630 v2 processor</li>
<li>NVIDIA Quadro K5000 graphical card</li>
<li>48 Gb ram</li>
<li>Windows 7 professional</li>
</ul>
<p>When working in Windows everything works fine, but when I boot this machine up from a Live-USB with Linux Mint 19.1 and then install 3D Slicer I’m having the same problems.</p>
<p>From this I can say that it has  certainly nothing to do with hardware.</p>
<p>So my question is: Is this Linux (Mint) related, for I remember that I also had this when I was using a previous version of Linux Mint?</p>

---

## Post #23 by @lassoan (2019-05-16 15:04 UTC)

<p>Is slice browsing or Slicer’s performance in general is worse if you use Linux Mint?<br>
What do you show in the scene? Just a volume? Do you show anything in the 3D view?<br>
Are there any warnings or errors in the application log?<br>
Can you attach a profiler to see what methods take the most time?</p>

---

## Post #24 by @Leon (2019-05-17 09:31 UTC)

<p><em>Is slice browsing or Slicer’s performance in general is worse if you use Linux Mint?</em><br>
No, I see no difference compared to a Windows 7.</p>
<p><em>What do you show in the scene? Just a volume? Do you show anything in the 3D view?</em><br>
I have the ‘Four Up’ display on, showing the CTChest and ‘Show-3D’ is off.</p>
<p><em>Are there any warnings or errors in the application log?</em><br>
The error ‘VTK  No input data’ shows up when using the drawing pen, although not after every stroke.</p>
<p><em>Can you attach a profiler to see what methods take the most time?</em><br>
I don’t know what you mean by this, but all I can say is that when starting a penstroke, during the stroke the selection slows down; the cursor is already in it’s last position, but the trail of cirkels is not completed, if you know what I mean.</p>
<p>I think I will also try Slicer out on another Linux Distro to see if it might be LinuxMint-related.</p>

---

## Post #25 by @lassoan (2019-05-17 11:47 UTC)

<aside class="quote no-group" data-username="Leon" data-post="24" data-topic="842">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/leon/48/1468_2.png" class="avatar"> Leon:</div>
<blockquote>
<p>showing the CTChest</p>
</blockquote>
</aside>
<p>How do you show CTChest? Using volume rendering? Or just show the slices in the 3D view?</p>
<aside class="quote no-group" data-username="Leon" data-post="24" data-topic="842">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/leon/48/1468_2.png" class="avatar"> Leon:</div>
<blockquote>
<p><em>Can you attach a profiler to see what methods take the most time?</em><br>
I don’t know what you mean by this</p>
</blockquote>
</aside>
<p>I mean attach a performance profiler to SlicerApp-real process. I don’t use Linux, so I cannot recommend any particular software, but <a href="https://stackoverflow.com/questions/2717948/c-profiler-that-can-attach-to-a-running-process">this</a> may help.</p>

---

## Post #26 by @Leon (2019-05-17 19:55 UTC)

<p>Andreas,</p>
<p>I don’t show anything in the 3D view. I just download the CTChest that Slicer provides. Only the axial, sagital and coronal views are filled.</p>
<p>Sorry, but I’m not familiar with programming languages at all. I just push buttons, if you know what I mean. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>Maybe it would be an idea to build a live-usb-stick containing Linux Mint 19.1. Then boot your computer up from the USB-stick, download Slicer and unpack it. Plug in a drawing tablet and try it out.<br>
Hopefully you will experiënce what I mean.</p>
<p>Btw. Despite this Linux issue I’m beginning to appreciate Slicer more and more.</p>

---

## Post #27 by @cpinter (2019-05-17 20:05 UTC)

<aside class="quote no-group" data-username="Leon" data-post="26" data-topic="842">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/leon/48/1468_2.png" class="avatar"> Leon:</div>
<blockquote>
<p>Plug in a drawing tablet and try it out</p>
</blockquote>
</aside>
<p>Do you only have this issue if you use the tablet, or it is slow even if it’s disconnected and you use only the mouse?</p>

---

## Post #28 by @Leon (2019-05-17 20:34 UTC)

<p>Only when I use the pen. The mouse works ok, but I prefer using a pen to prevent rsi-risk and it’s also much faster. I draw left (I’m lefthanded) and mouse right.</p>
<p>A few years ago when I started working with segmentation software, within a week I started to feel muscle pain in my lower arm. Since then I’m using a drawing tablet.</p>
<p>I also prefer Linux over Windows, because it’s safer and needs less maintenance. Just try it!</p>

---

## Post #29 by @cpinter (2019-05-17 20:38 UTC)

<p>Thanks! It indeed sounds like a nice workflow!</p>
<p>I was wondering because I cannot think of why the different input device would cause slowdown. Is it also slower when you use the pen to rotate the 3D view as opposed to using the mouse for that? If unsure you can show the FPS in the 3D view settings.</p>

---

## Post #30 by @Leon (2019-05-17 20:51 UTC)

<p>I also have no idea what is slowing down the pen. But it only happens in the paint or erase mode and not in draw! That’s what makes it so strange. You would think that everything would be affected.<br>
Maybe there are more issues that I haven noticed because I also use the mouse and keyboard a lot. For rotating I normally use the mouse, I’ve tested it just now and that works ok.</p>
<p>What do you mean by “show the FPS in the 3D View setting”?</p>

---

## Post #31 by @lassoan (2019-05-17 21:10 UTC)

<p>Only a few percent of Slicer users are on Linux and even less own a graphic tablet. Maybe you are the only Slicer user in the world who uses Linux AND a graphic tablet. If we find out what’s the root cause of the performance problem and there is a trivial fix then we can help. For example, I can imagine that the tablet generates too many events due to its higher resolution. Try to lower the resolution setting and see if performance is satisfactory then. If it is, then we might be able to add a filter that limits the events to the display resolution.</p>
<p>If we cannot find an easy solution, then you might need to switch to a bit more main-stream technologies: Windows or Mac OS instead of Linux; active pen instead of drawing tablet. We are improving Windows pen and touchscreen and Mac touchpad support (a big update is expected within a month). I’m not aware of any plans for improving tablet support.</p>

---

## Post #32 by @Leon (2019-05-17 21:26 UTC)

<p>I consider this as a compliment being “the only Slicer user in the world who uses Linux AND a graphic tablet”!<br>
<img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji only-emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>Thanks for your help for sofar. I will try to fix it by lowering the resolution (although I have to figure out how to do this).</p>
<p>About Linux not being main-stream:</p>
<ul>
<li>Mac OS and Linux are both Unix-based.</li>
<li>Most servers in the world run on Linux (because of it’s stability and reliability)</li>
<li>Androïd is Linux.</li>
<li>There is Linux in your TV, car and many more things.</li>
</ul>
<p>So Linux is there where you don’t expect it to be!<br>
Just give it a change and I’m sure that at the end you’ll begin to like it.<br>
<img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji only-emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>I’ll Be Back!</p>

---

## Post #33 by @lassoan (2019-05-17 21:44 UTC)

<p>I mean Linux desktop is a small niche. It is reflected in Slicer download counts, too.</p>

---

## Post #34 by @Leon (2019-05-17 23:08 UTC)

<p>I don’ t mind being part of a small niche. It give me the feeling of being special.</p>
<p>Just for your interest. I’m now in another Linux Distro and tried out Slicer again and also there I have the same problems with my graphic tablet. Guess I just have to learn to live with it and hope that maybe in future it will be resolved.</p>
<p>Thanks for your help anyway.</p>

---

## Post #35 by @cpinter (2019-05-18 00:46 UTC)

<aside class="quote no-group" data-username="Leon" data-post="30" data-topic="842">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/leon/48/1468_2.png" class="avatar"> Leon:</div>
<blockquote>
<p>What do you mean by “show the FPS in the 3D View setting”?</p>
</blockquote>
</aside>
<p>I mean turning this on:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/94e918748ff3311b78c40206a143ff5cfe0fe1a3.png" alt="image" data-base62-sha1="lfk4mYw0oY4V9uqMFQPLPdMgsgP" width="481" height="169"></p>
<p>Everything you reported points to the fact that updating the temporary labelmap when painting/erasing is what takes so long. So I don’t think FPS will be different but it’s worth a shot.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> might be right about the too many events. To verify this we could create a custom installer for you that will measure the number of events when painting and you could compare mouse and pen.<br>
However if you can reduce the sampling resolution that might just solve the problem.</p>

---

## Post #36 by @Leon (2019-05-18 08:45 UTC)

<p><span class="mention">@Csaba</span>.<br>
Thanks. I will try if this will be of any help</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a>.<br>
If found a simple workaround for my problem.<br>
I’ll just ignore both the ‘paint’ and ‘erase’ tool and only focus myself on the ‘draw’ and ‘scissors’ tool.<br>
With ‘draw’ I can sketch the path of my selection with pen (or mouse) and press enter to confirm and with the scissors tool I’ll draw my deselection path. Because I mostly work on the 2D planes, I just have to change the setting for the scissors to a <strong>symmetric slicecut</strong> at level <strong>0,00mm</strong>, so that it only affects the plane I’m working on.<br>
Simple but effective. <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=12" title=":wink:" class="emoji" alt=":wink:" loading="lazy" width="20" height="20"></p>
<p>I just have an extra adjustment tip for the ‘draw’ tool.<br>
Now you always have to confirm before the selection action takes place. I know that’s because you need to be able to build up the path by clicking on several points. You can also draw the path by <strong>clicking and holding</strong> the left mouse button, release it and then confirm, but wouldn’t it be a good idea to build in <strong>an extra option</strong> so that, when you release the LMB (or take the pen from the tablet) the selection is automatically confirmed. Saves an extra click.<br>
I think that many user would appreciate this function.</p>

---

## Post #37 by @lassoan (2019-05-19 13:34 UTC)

<aside class="quote no-group" data-username="Leon" data-post="36" data-topic="842">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/leon/48/1468_2.png" class="avatar"> Leon:</div>
<blockquote>
<p>wouldn’t it be a good idea to build in <strong>an extra option</strong> so that, when you release the LMB (or take the pen from the tablet) the selection is automatically confirmed</p>
</blockquote>
</aside>
<p>Scissors effect can draw and erase in a slice and does not require confirmation by right-click, so you can use that instead of Draw effect.</p>
<p>I’ve added two experimental options to Paint and Erase effects that will probably solve your performance issue. You can set a minimum distance for mouse move events, so if your tablet generates many superfluous events, you can ignore them by setting the appropriate threshold. In addition to this, I’ve exposed a flag to enable/disable delayed paint, i.e., if you modify the segmentation immediately when you move the mouse or only when the moues button is released. This might make the performance worse, but if your computer is fast enough then you may get more rich immediate feedback during painting.</p>
<p>How to adjust these options? Download Slicer revision 28260 or later (should be available tomorrow). Open Python interactor (Ctrl+3) and copy-paste the code below. You can change the numbers to find a good combination that works the best for you.</p>
<pre><code class="lang-auto">paint=slicer.modules.segmenteditor.widgetRepresentation().self().editor.effectByName("Paint")
paint.delayedPaint=False
paint.minimumPaintPointDistance=3
</code></pre>
<p>If you find that changing these setting help then copy the code into your <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#How_to_systematically_execute_custom_python_code_at_startup_.3F">Slicer startup (.slicerrc) file</a>.</p>

---

## Post #38 by @Leon (2019-05-19 18:09 UTC)

<p>You’re great!</p>
<p>I’ll try it out tomorrow.</p>

---

## Post #39 by @Leon (2019-05-20 17:43 UTC)

<p>Sorry lassoan, you did your best but it didn’t solve my problem.<br>
But don’t mind, I’ll just stick to my own solution for that works fine for me.</p>
<p>Regards,<br>
Léon</p>

---

## Post #40 by @lassoan (2019-05-20 17:58 UTC)

<p>Try setting paint.delayedPaint=True and use larger paint.minimumPaintPointDistance values (5, 10, 20, 30, …). You should see that less circles are drawn, so there should be no slowdown. Can you confirm that you observe this? As you increase the number, circles will noticeably jump, so the final value will be a trade-off between performance and size of these jumps.</p>
<p>If you have trouble tuning this then please record a few screen capture videos (and upload somewhere and post the link here) so that we can see what’s happening.</p>

---

## Post #41 by @Leon (2019-05-20 19:13 UTC)

<p>Lassoan,</p>
<p>Setting paint.delayedPaint=<strong>True</strong> and changing PaintPointDistance value to <strong>20</strong> enormously improves the paint function, but the erase function is uneffected (which means it’s still slow and lagging), so maybe we’re almost there.</p>
<p>But now I just discovered that the contrast/brightness setting with LMB doesn’t work in this nightly built version. I don’t know if this has something to do with your adjustments. To check if it was not due to the extra code I pasted in, I restarted Slicer, but also after this fresh restart the contrast/brightness adjustment isn’t working.<br>
In version 4.10 though it works fine.</p>

---

## Post #42 by @jamesobutler (2019-05-20 19:18 UTC)

<p><a class="mention" href="/u/leon">@Leon</a> Review the following post regarding how contrast/brightness works in the recent Slicer nightly builds.  It is now different compared to Slicer 4.10 <a href="https://discourse.slicer.org/t/feedback-requested-how-to-improve-mouse-interaction-in-views/6420" class="inline-onebox">Feedback requested: How to improve mouse interaction in views?</a></p>

---

## Post #43 by @Leon (2019-05-20 19:28 UTC)

<p>OK!<br>
That’s a nice feature, thanks!</p>

---

## Post #44 by @lassoan (2019-05-20 20:57 UTC)

<aside class="quote no-group" data-username="Leon" data-post="41" data-topic="842">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/leon/48/1468_2.png" class="avatar"> Leon:</div>
<blockquote>
<p>erase function is uneffected</p>
</blockquote>
</aside>
<p>The example that I wrote is for the paint effect. Replace “Paint” by “Erase” to adjust erase effect parameters.</p>

---

## Post #45 by @Marco (2021-01-16 19:57 UTC)

<aside class="quote no-group" data-username="Leon" data-post="41" data-topic="842">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/leon/48/1468_2.png" class="avatar"> Leon:</div>
<blockquote>
<p>so maybe we’re almost there.</p>
</blockquote>
</aside>
<p>Did you eventually solve your problems? I am thinking about joining you in the small niche of Slicer users that want Linux AND graphic tablet.</p>

---

## Post #46 by @ni5h (2021-10-07 14:08 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="842">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Also note there are a number of keyboard shortcuts that you can use in Segment Editor: <a href="http://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html" rel="noopener nofollow ugc">http://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html </a></p>
<p>For example, a very effective shortcut is <code>space</code> key, which switches between last two effects (for example: paint/erase) or activates/deactivates an effect (for example: activate scissors/deactivate scissors so you can rotate the 3D view).</p>
</blockquote>
</aside>
<p>Hi Andras - this link no longer works. I have now got a wacom tablet - i find the space shortcut particularly effective though would prefer if it was not the last 2 effects but just paint/erase, how can I add a few more, such as switching on/off scissors (switching back to None), enabling/disabling 3d and a useful threshold shortcut - i feel this would save me plenty of time?<br>
Thanks</p>

---

## Post #47 by @lassoan (2021-10-07 14:24 UTC)

<p>Here is the updated link: <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#keyboard-shortcuts" class="inline-onebox">Segment editor — 3D Slicer documentation</a></p>
<p>You can create any number of keyboard shortcuts and connect them to any Slicer feature - see examples <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#customize-keyboard-shortcuts">here</a>. If you cannot figure out how to access a specific function from Python then you can ask here.</p>
<aside class="quote no-group" data-username="ni5h" data-post="46" data-topic="842">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/839c29/48.png" class="avatar"> ni5h:</div>
<blockquote>
<p>I have now got a wacom tablet</p>
</blockquote>
</aside>
<p>Some users complained about <a href="https://discourse.slicer.org/t/delays-in-paint-function-using-wacom-cintiq22/19952">Wacom tablet performance</a> in latest Slicer Preview Release. Do you see any performance issue? What tablet do you use on what operating system?</p>

---
