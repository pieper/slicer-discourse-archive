# Feature modification of Fiducial Registration wizard

**Topic ID**: 15400
**Date**: 2021-01-08
**URL**: https://discourse.slicer.org/t/feature-modification-of-fiducial-registration-wizard/15400

---

## Post #1 by @11141 (2021-01-08 07:17 UTC)

<p>Hi, all.<br>
I am a student working at KIST(Korea Institute of Science and Technology).</p>
<p>I have a question. I wanted to find out through internet search, but I failed.</p>
<ol>
<li>Although the Fiducial Registration Wizard is a C++ module, can I add some features to this module using Python? if possible, please tell me method… ㅠ.ㅠ</li>
</ol>
<ul>
<li>detail : I want to add a my own’s detailed feature to “From fiducials” feature.</li>
</ul>
<p>I should be very grateful to you if you might help me.<br>
Thanks for all <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<ul>
<li>Daehyeon Kim.</li>
</ul>

---

## Post #2 by @lassoan (2021-01-08 16:20 UTC)

<aside class="quote no-group" data-username="11141" data-post="1" data-topic="15400">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/11141/48/9442_2.png" class="avatar"> 11141:</div>
<blockquote>
<p>Although the Fiducial Registration Wizard is a C++ module, can I add some features to this module using Python?</p>
</blockquote>
</aside>
<p>You cannot make changes to C++ classes in Python. Instead, you can use the module’s logic (registration agorithms, without using the modue’s GUI) from your own python script.</p>
<aside class="quote no-group" data-username="11141" data-post="1" data-topic="15400">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/11141/48/9442_2.png" class="avatar"> 11141:</div>
<blockquote>
<p>detail : I want to add a my own’s detailed feature to “From fiducials” feature.</p>
</blockquote>
</aside>
<p>What would you like to do exactly? If it is a trivial change that can be generally useful then we may be able to make that change for you.</p>

---

## Post #3 by @11141 (2021-01-11 03:00 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="15400">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>What would you like to do exactly? If it is a trivial change that can be generally useful then we may be able to make that change for you.</p>
</blockquote>
</aside>
<p>Thank you for your reply.<br>
My grammar might be wrong because I’m not good at English yet. sorry.</p>
<p>More specifically, when I want to place a markup point “From-1”, I click the “Place a markup point” button and then place it wherever I want. In my project, markup points should be placed at the end of the needle pointing to where the Stylus tip is recognized. I have to hold the Stylus with one hand and place these points by clicking the mouse two times with the other, but it’s so uncomfortable that I’d like to place markup points by clicking the “Label” box only once. such as, nose and ears are so blunt that Stylus is very unstable and placing the markup point by clicking directly on end-point of needle where the Stylus tip is recognized will result slight error. that’s why when I just click on the “Label” box, I’d like to modify this feature so that the “From-1” point is placed  automatically on the coordinate indicating the  end of the needle.</p>
<p>So I maybe need below.</p>
<ul>
<li>
<p>Real-time coordinate indicating end of needle that keep moving.</p>
</li>
<li>
<p>how to add some features to module(Fiducial Registration Wizard). T.T</p>
</li>
</ul>
<p>Thanks.</p>

---

## Post #4 by @lassoan (2021-01-11 06:09 UTC)

<aside class="quote no-group" data-username="11141" data-post="3" data-topic="15400">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/11141/48/9442_2.png" class="avatar"> 11141:</div>
<blockquote>
<p>I have to hold the Stylus with one hand and place these points by clicking the mouse two times with the other</p>
</blockquote>
</aside>
<p>If you need to acquire more than a few landmarks or you need to capture landmark points regularly then there are several much better options. Without knowing your constraints - how often you need to do this, how many points, how much time you have, how reliable your tools are, do you need to do it during a surgery or just in a lab, etc. - I cannot make a recommendation, just list a few techniques that we used over the years.</p>
<p>First of all, the “two clicks”. You can capture any number of transforms (and images, and state of any other nodes) using snapshot feature of Sequences module. Once you captured the transforms you need, you can either step through your recording and place points manually, or write a few-line Python script that does this automatically.</p>
<p>If Fiducial registration wizard module is already almost exactly what you need and the only problem is that you need to click twice then we could add a “Place From and To” button to capture both positions a the same time (I remembered that we added this button already, but I’ve just checked the module and apparently it is not there).</p>
<p>Reaching for a mouse and clicking it while holding tools is certainly inconvenient, but there are several easier ways to trigger capturing of transforms or landmarks.</p>
<ol>
<li>Foot switch or handheld wireless button</li>
</ol>
<p>If you need to acquire a lot of points with both hands holding instruments then you can use a <a href="https://www.amazon.com/s?k=usb+foot+switch">USB foot switch</a> that can simulate keypress or mouse click events. Alternatively, you can attach a presentation clicker to the stylus or use a ring mouse so that you can trigger a snapshot while holding the tool.</p>
<ol start="2">
<li>Automatic landmark point detection</li>
</ol>
<p>If you only have a limited landmarks points to acquire (so they need to have higher accuracy and you have more time to record them) or foot pedal or ring mouse is not usable (e.g., due to sterility requirements) then you can use an automatic landmark point detection algorithm. We developed one that detects when you pivot the stylustip around a point for a certain amount of time and records it as a new point (if you move the stylustip or you just keep the stylus stationary then it does not record a point). The implementation is available <a href="https://github.com/PlusToolkit/PlusLib/blob/master/src/PlusCalibration/vtkPhantomLandmarkRegistrationAlgo/vtkPlusLandmarkDetectionAlgo.cxx">here</a>. If you want to use it in Slicer then probably the easiest way would be to move it to <a href="https://github.com/IGSIO/IGSIO">IGSIO library</a> and expose it as a Slicer module, similarly to the volume reconstructor module.</p>
<ol start="3">
<li>Record and replay</li>
</ol>
<p>In recent years, we often use Sequences module to record a live video feed with a webcam, live ultrasound images, and all tracking transforms, etc. After this we can put down all the tools and just replay the data, find the frame we need (where we saw the stylus was held at the right location), and add landmarks there. It is also a good way of documenting the data collection, which is useful for quality control later (e.g., if accuracy is not good then you can go back and review everything to figure out what went wrong). See the <a href="http://www.slicerigt.org/wp/user-tutorial/">U-37 SlicerIGT tutorial</a> and associated sample data sets for an example.</p>

---
