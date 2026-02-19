---
topic_id: 6205
title: "How Can I Draw A Coordinate System On The Image"
date: 2019-03-19
url: https://discourse.slicer.org/t/6205
---

# How can I draw a coordinate system on the image?

**Topic ID**: 6205
**Date**: 2019-03-19
**URL**: https://discourse.slicer.org/t/how-can-i-draw-a-coordinate-system-on-the-image/6205

---

## Post #1 by @ZiyunLiang (2019-03-19 11:47 UTC)

<p>Hi everyone,</p>
<p>I am currently working on a project related to pelvic floor MRI images recognition. I have already recognized a feature point and a reference line in a scripted module. And I’m trying to build a new coordinate system by setting the point as origin and the line as x-axis.<br>
I want to draw the two-dimensional cartesian coordinate system on the image but I can’t find a way to plot it. Does anyone have any idea?<br>
Please help me out.</p>
<p>Thanks,<br>
Andrea</p>

---

## Post #2 by @lassoan (2019-03-19 12:39 UTC)

<p>You can enable coordinate system axes orientation marker in the slice view controller:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e5db1738d0be14edcdcc10bcd923312e56fcc1b7.png" data-download-href="/uploads/short-url/wNoJU9M4epPwK7fRpz3tm01QeRV.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e5db1738d0be14edcdcc10bcd923312e56fcc1b7.png" alt="image" data-base62-sha1="wNoJU9M4epPwK7fRpz3tm01QeRV" width="690" height="441" data-dominant-color="A8A7A6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">733×469 62.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @ZiyunLiang (2019-03-19 13:04 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="6205">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>axes orientation marke</p>
</blockquote>
</aside>
<p>Hi Andras,<br>
Thank you for the quick response! This is a function I haven’t noticed before and thanks for pointing out. However, I want to move the coordinate system’s origin to a specific point and also change the direction of the axis. If possible, I want to mark the coordinate value on the axis. Is there anyway to accomplish this?</p>
<p>Thank you for your time!<br>
Andrea</p>

---

## Post #4 by @lassoan (2019-03-19 13:14 UTC)

<p>I don’t remember this has ever come up as a need. What would you like to achieve with this? There may be alternative, more commonly used solutions for your problem.</p>

---

## Post #5 by @ZiyunLiang (2019-03-19 13:49 UTC)

<p>Hi  Andras,</p>
<p>Thanks for your answer. In this module I created, users can mark fiducial points according to their needs, and the points are given new coordinate values in a new coordinate system(by setting new coordinate system helps better diagnose of a disease). I want to help the users get a better view of the position. I’ll look for alternatives.  Do you have any recommendations?</p>
<p>Thanks<br>
Andrea</p>

---

## Post #6 by @cpinter (2019-03-19 14:01 UTC)

<p>Are you trying to find the relationship between two coordinate systems? If so, what are these two coordinate systems and what they are defined by? Would it make sense to perform registration such as landmark registration?</p>

---

## Post #7 by @ZiyunLiang (2019-03-19 14:58 UTC)

<p>Hi Csaba,<br>
Thanks for answering. I have found the relationship between the two coordinate systems. One of them is defined by the MRI image feature points (got from a deep learning model), the other one is the RAS coordinate Slicer-provided. So I think I have already used landmark registration.</p>
<p>Thanks for your time!<br>
Andrea</p>

---

## Post #8 by @lassoan (2019-03-19 15:44 UTC)

<p>Now I’m even more confused about what you would like to achieve. Visualize something, or get user input, register, … Anyway, there are many readily available tools in Slicer for doing such things, so if you can describe what you would like to do (not so much how exactly you would like to do it) then we should be able to help.</p>

---

## Post #9 by @ZiyunLiang (2019-03-20 03:12 UTC)

<p>Hi, Andras</p>
<p>Thanks for answering! Sorry for the confusion here. What I want to do is to visualize the new coordinate system I have already set on the image. If that is not possible, maybe I can draw something else as a replacement.<br>
Is there a way to draw a line between two fiducial points? (the points already existed)</p>
<p>Thank you for your time!<br>
Andrea</p>

---

## Post #10 by @lassoan (2019-03-20 04:54 UTC)

<aside class="quote no-group" data-username="ZiyunLiang" data-post="9" data-topic="6205">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/z/5daacb/48.png" class="avatar"> ZiyunLiang:</div>
<blockquote>
<p>Is there a way to draw a line between two fiducial points?</p>
</blockquote>
</aside>
<p>Yes. You can use MarkupsToModel extension to draw lines between markup fiducials (enable slice intersection display to show in slice views). In recent nightly versions of Slicer, there are curve and line markups that you can use, but this part of the code is still actively developed, so it is not that stable.</p>

---

## Post #11 by @ZiyunLiang (2019-03-20 13:05 UTC)

<p>Hi Andras<br>
Thank you for answering. I tried to use MarkupsToModel extension. But when I use the code<br>
<code>markupsToModel = slicer.mrmlScene.AddNode(slicer.vtkMRMLMarkupsToModelNode())</code><br>
I got the error</p>
<pre><code>Traceback (most recent call last):File "&lt;console&gt;" line 1, in &lt;module&gt;

AttributeError: 'module' object has no attribute 'vtkMRMLMarkupsToModelNode'
</code></pre>
<p>Do you know how to fix this bug?</p>
<p>Thank you for your time!<br>
Andrea</p>

---

## Post #12 by @lassoan (2019-03-20 13:17 UTC)

<p>The line above works well for me. You need to install MarkupsToModel extension and restart Slicer.</p>

---

## Post #13 by @ZiyunLiang (2019-03-20 13:22 UTC)

<p>Hi Andras, after restarting the Slicer, it worked. Thank you for your help!</p>

---

## Post #14 by @ZiyunLiang (2019-03-20 13:51 UTC)

<p>Hi, sorry to bother you again, but I want to know if there is a way to stop updating the line even after I keep adding new fiducial points.</p>
<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="6205">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>In recent nightly versions of Slicer, there are curve and line markups that you can use, but this part of the code is still actively developed, so it is not that stable.</p>
</blockquote>
</aside>
<p>And I’m sorry I didn’t understand this. Do you mean there are changes in MarkupsToModel in the recent nighty version?</p>
<p>Thanks!<br>
Andrea</p>

---

## Post #15 by @lassoan (2019-03-20 13:57 UTC)

<aside class="quote no-group" data-username="ZiyunLiang" data-post="14" data-topic="6205">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/z/5daacb/48.png" class="avatar"> ZiyunLiang:</div>
<blockquote>
<p>if there is a way to stop updating the line even after I keep adding new fiducial points.</p>
</blockquote>
</aside>
<p>You can disable automatic updates or delete the MarkupsToModel and your input markups completely if you don’t want to allow your lines to be moved anymore.</p>
<aside class="quote no-group" data-username="ZiyunLiang" data-post="14" data-topic="6205">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/z/5daacb/48.png" class="avatar"> ZiyunLiang:</div>
<blockquote>
<p>Do you mean there are changes in MarkupsToModel in the recent nighty version?</p>
</blockquote>
</aside>
<p>Yes. Huge changes, tons of new features. For example, you can display a “markups line”, which you can position programmatically or by interacting on the GUI. It can be also locked if you don’t want to allow the user to move it.</p>

---

## Post #16 by @cpinter (2019-03-20 14:58 UTC)

<p>It would help to know why you want to “display the coordinate system”.<br>
Usually it is not needed because everything is brought to a common coordinate system using registration. So if you explain your use case from a higher level, then we may offer a solution that does not require implementing something that otherwise would not be needed.</p>

---

## Post #17 by @ZiyunLiang (2019-03-21 09:28 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="15" data-topic="6205">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Huge changes</p>
</blockquote>
</aside>
<p>I looked over the new version and these are indeed awesome changes. Thanks for pointing it out.</p>
<aside class="quote no-group" data-username="lassoan" data-post="15" data-topic="6205">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can disable automatic updates or delete the MarkupsToModel and your input markups completely if you don’t want to allow your lines to be moved anymore.</p>
</blockquote>
</aside>
<p>These works for me. Thanks for  your answer.</p>

---

## Post #18 by @ZiyunLiang (2019-03-21 09:46 UTC)

<p>Hi Csaba,<br>
Thanks for your time. I want to display a new coordinate system for the following reasons:</p>
<ol>
<li>in pelvic floor POP diagnose, a new system(PICS system)  would help a lot. To implement this, there will be a new x-axis with every image. So there will be a new coordinate system and the coordinate system will be at different position every time.</li>
<li>I  want to  plot is because I want to visualize  the new coordinate system and it can give users a better understanding of where does the coordinates came from.</li>
</ol>

---

## Post #19 by @pieper (2019-03-21 12:27 UTC)

<aside class="quote no-group" data-username="ZiyunLiang" data-post="18" data-topic="6205">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/z/5daacb/48.png" class="avatar"> ZiyunLiang:</div>
<blockquote>
<p>display a new coordinate system</p>
</blockquote>
</aside>
<p>Can you describe what you’d like the display to look like?  Is it the three orthogonal arrows like the axis display in the lower right corner?  You could create a Model node that has those same kinds of arrows and just move it where you want, for example using the transform you calculate.  Or maybe it would be clearer to your uses if you make some other kind of model, like a grid (like graph paper).  In any case, you can either write a small program to generate the model using slicer/vtk or you can make a model in an external program like Blender.</p>

---

## Post #20 by @lassoan (2019-03-21 12:54 UTC)

<p>Yes, and you can do this by just using existing modules: You may generate a coordinate system model by using SlicerIGT extension’s CreateModels module. Then apply a transform to this coordinate system model using Transforms module and visualize it in slice views as projection using Models module.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/3353e20652133d9e67cd0fdcd1853370db95d0b3.jpeg" data-download-href="/uploads/short-url/7k44inhPOf4li3GjYYnBZZrmoSv.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/3353e20652133d9e67cd0fdcd1853370db95d0b3_2_690x373.jpeg" alt="image" data-base62-sha1="7k44inhPOf4li3GjYYnBZZrmoSv" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/3353e20652133d9e67cd0fdcd1853370db95d0b3_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/3353e20652133d9e67cd0fdcd1853370db95d0b3_2_1035x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/3353e20652133d9e67cd0fdcd1853370db95d0b3_2_1380x746.jpeg 2x" data-dominant-color="9C9CA3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1040 289 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/42fb02be75ca7b773b9cd6caee3bcaca0010937f.png" data-download-href="/uploads/short-url/9yxiFaScKxqu1TYMMcXThtzERHN.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/42fb02be75ca7b773b9cd6caee3bcaca0010937f_2_690x472.png" alt="image" data-base62-sha1="9yxiFaScKxqu1TYMMcXThtzERHN" width="690" height="472" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/42fb02be75ca7b773b9cd6caee3bcaca0010937f_2_690x472.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/42fb02be75ca7b773b9cd6caee3bcaca0010937f_2_1035x708.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/42fb02be75ca7b773b9cd6caee3bcaca0010937f.png 2x" data-dominant-color="CDCED0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1241×849 221 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #21 by @ZiyunLiang (2019-03-21 13:43 UTC)

<p>Hi, thanks so much for the advice! This seems like an awesome idea, I’ll definitely try it in the next couple days.</p>

---

## Post #22 by @ZiyunLiang (2019-03-24 08:42 UTC)

<p>Hi, when writing this in python, I run into some problems.</p>
<blockquote>
<p>Blockquote</p>
</blockquote>
<p>I don’t know how to write this in python. Can you help with this?</p>
<p>Thanks for your time!</p>

---

## Post #23 by @lassoan (2019-03-24 13:56 UTC)

<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Programming_Tutorial" rel="nofollow noopener">Slicer programming tutorial</a> and examples in <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository" rel="nofollow noopener">Slicer script repository</a> may be a good starting points. Let us know if you have any specific questions.</p>

---

## Post #24 by @ZiyunLiang (2019-03-24 15:30 UTC)

<p>Hi, something went wrong with my quote in my last post.<br>
What I’m trying to say is how to write  <em>visualize it in slice views as projection using Models module</em> in python. I tried some functions myself, but they didn’t work.<br>
Thanks for your help!</p>

---

## Post #25 by @lassoan (2019-03-24 18:22 UTC)

<p>To show the model as projection on the slice, call <a href="http://apidocs.slicer.org/master/classvtkMRMLModelDisplayNode.html#a20839b43f4c88cd2258fb0afdee25a85" rel="nofollow noopener"><code>SetSliceDisplayModeToProjection()</code></a> method of the model’s display node.</p>

---

## Post #26 by @ZiyunLiang (2019-03-25 09:39 UTC)

<p>Awesome, it  works. Thanks.<img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=9" title=":smiley:" class="emoji" alt=":smiley:"></p>

---
