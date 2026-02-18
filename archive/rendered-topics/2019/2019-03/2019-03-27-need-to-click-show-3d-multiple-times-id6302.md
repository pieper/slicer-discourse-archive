# Need to click "Show 3D" multiple times

**Topic ID**: 6302
**Date**: 2019-03-27
**URL**: https://discourse.slicer.org/t/need-to-click-show-3d-multiple-times/6302

---

## Post #1 by @ishan_45 (2019-03-27 08:27 UTC)

<p>Hello everyone,</p>
<p>I have been experiencing a small issue while using the “Show 3D” button in Segment Editor module. During manual segmentation and repair process for hip bones, I need to switch on and off the 3D view multiple times using this button. However, after working fine for the first time (i.e. opening the 3D view when clicked once), after closing it, the next time requires two pushes of the button to show the 3D view. Has anyone else experienced something similar?</p>
<p>Slicer Build: 4.11.0-2018-12-26<br>
OS: Windows 10</p>

---

## Post #2 by @lassoan (2019-03-27 12:22 UTC)

<p>Thank you for reporting this.</p>
<p>It should not be necessary to disable “Show 3D”. If you click the arrow button on the “Show 3D” button and disable smoothing then there should be no noticeable delays due to 3D updates.</p>
<p>I haven’t experienced this issue of requiring two clicks to synchronize the button state with the actual 3D display state. Can you reproduce it with latest stable (4.10.1) or latest nightly (4.11.0-2019.03.26) version? If yes, could you give an exact list of steps to reproduce it (starting from launching the application, describe which buttons to click).</p>

---

## Post #3 by @ishan_45 (2019-03-27 13:08 UTC)

<p>Hi,<br>
Yes, I tried disabling smoothing, but since I need to see the smoothened results quite often and the option to turn off smoothing is in a drop-down list, I found turning off the 3D view each time more easier.</p>
<p>And I get the same results on the latest nightly build (4.11.0-2019.03.26). Here are the step I followed:</p>
<ol>
<li>Lauch the application.</li>
<li>Load the mrml scene.</li>
<li>Select the Segment Editor Module.</li>
<li>Turn off the 3D view by clicking on the “Show 3D button”</li>
<li>On clicking it once to turn the view off, the button stays in the pressed (ON) state, you need to click it once more to get to the OFF state.</li>
<li>Now click once more to turn on the 3D view.</li>
</ol>

---

## Post #4 by @lassoan (2019-03-27 13:31 UTC)

<p>Thank you for the step-by-step instructions. I’ve tested this and it works fine for me: at step 5, after clicking the button it does <em>not</em> stay pressed (ON) state. What operating system do you use? Can you try if you can reproduce it with this <a href="https://1drv.ms/u/s!Arm_AFxB9yqHt5JifWf9FFsrtMVK6w">simple scene</a> (this is what I used when I could not reproduce your steps).</p>
<aside class="quote no-group" data-username="ishan_45" data-post="3" data-topic="6302">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/i/9de0a6/48.png" class="avatar"> ishan_45:</div>
<blockquote>
<p>I tried disabling smoothing, but since I need to see the smoothened results quite often</p>
</blockquote>
</aside>
<p>The non-smoothened results match exactly what you see in slice views, therefore it should not be necessary to see smoothened results <em>during</em> editing.</p>

---

## Post #5 by @ishan_45 (2019-03-27 14:22 UTC)

<p>Hi,<br>
For the example scene you provided, I also don’t face any issues. Here is an <a href="https://drive.google.com/open?id=1WOAqZSFsANHanuEvIm38Wmnpdnhf6Sgc" rel="nofollow noopener">example</a> of the scene that I am using where you should be able to reproduce the results.</p>
<p>I am using Windows 10 currently.</p>

---

## Post #6 by @lassoan (2019-03-27 15:58 UTC)

<p>Thanks a lot, with this data set I was able to reproduce the problem. I have a fix that will be available in tomorrow’s nightly version.</p>

---
