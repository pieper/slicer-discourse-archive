---
topic_id: 8382
title: "Fill Slice Views Without Changing Image Spacing"
date: 2019-09-11
url: https://discourse.slicer.org/t/8382
---

# Fill Slice Views without Changing Image Spacing

**Topic ID**: 8382
**Date**: 2019-09-11
**URL**: https://discourse.slicer.org/t/fill-slice-views-without-changing-image-spacing/8382

---

## Post #1 by @Jonathan_Lesage (2019-09-11 14:45 UTC)

<p>Hi,</p>
<p>I am using slicer to look at nondestructive testing data where volumes are typically sampled much more sparsely in the z (axial) direction than other directions (roughly 10 to 1). Additionally, the axial dimension is usually much larger than the other dimensions (i.e. we perform very long scans of components with a very tight imaging region). The volumes we are dealing with are like if we imaged at 10 cm x 10 cm square over the length of a human body in a CT scanner. I would like to be able to fill all slice view panes effectively changing the aspect ratio of the displayed image without changing the image spacing so that the measurements and slice positions read the correct positions. Commercial softwares for this type of applications routinely display the data with aspect ratios in each slice view which are not 1:1. Is this possible in slicer either by extension or python script or the like?</p>
<p>Any help with this would be greatly appreciated!</p>
<p>Thanks,</p>
<ul>
<li>Jon</li>
</ul>

---

## Post #2 by @lassoan (2019-09-11 15:03 UTC)

<p>You can change the field of view in a slice view, for example enlarge it by a factor of 10x along one axis:</p>
<pre><code class="lang-python">sliceNode = getNode('vtkMRMLSliceNodeYellow')
fov = sliceNode.GetFieldOfView()
sliceNode.SetFieldOfView(fov[0], fov[1]*10.0, fov[2])
</code></pre>
<p>This is not officially supported, so you might run into unexpected situations - mostly that the FOV is reset when you do certain operations (that you may address by adding an observer to the slice node and set the FOV back to your preferred FOV).</p>

---

## Post #3 by @Jonathan_Lesage (2019-09-11 15:15 UTC)

<aside class="quote no-group quote-modified" data-username="lassoan" data-post="2" data-topic="8382">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>sliceNode = getNode(‘vtkMRMLSliceNodeYellow’) fov = sliceNode.GetFieldOfView() sliceNode.SetFieldOfView(fov[0], fov[1]*10.0, fov[2])</p>
</blockquote>
</aside>
<p>Thank you so much! Works like a charm!</p>

---

## Post #4 by @Jonathan_Lesage (2019-09-13 15:41 UTC)

<p>Mr. Lassoan,</p>
<p>I am wondering if a similar set of commands can be used to set the field of view per axis on the volume view?</p>
<p>Many thanks,</p>
<ul>
<li>Jon</li>
</ul>

---

## Post #5 by @lassoan (2019-09-13 18:06 UTC)

<p>In 3D view, changing the view’s aspect ratio would not make sense (as the view’s aspect ratio is fixed in display space and the object can be rotated around). To display a deformed volume in 3D, you can apply a transform to it (Transforms module) or change its spacing (Volumes module).</p>

---

## Post #6 by @Jonathan_Lesage (2019-09-13 20:42 UTC)

<p>Hi Andras,</p>
<p>I have done as you’ve suggested in the past and of course I can distort the volume by changing the spacing or applying and transform, the issue is that the rulers and cursor positions do not read their true values afterwards which is critical for our industry. The volume view is not actually required so I can get by using the tips for changing the field of view in the slice panes.</p>
<p>Thanks!</p>
<ul>
<li>Jon</li>
</ul>

---

## Post #7 by @lassoan (2019-09-13 21:20 UTC)

<p>It would not be hard to add an option to markups to report measurements in the node’s coordinate system instead of the World coordinate system but yours would be the first use case. If we hear from many other users that they would need this, too, then we can add it to the plan. If you need this sooner then you can implement it yourself or contract Kitware or others to develop it for you.</p>

---

## Post #8 by @fbordignon (2021-09-30 12:36 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="8382">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>This is not officially supported, so you might run into unexpected situations - mostly that the FOV is reset when you do certain operations (that you may address by adding an observer to the slice node and set the FOV back to your preferred FOV).</p>
</blockquote>
</aside>
<p>I’ve ran into this today. I’ve set the FOV to make the volume slice occupy the whole width of the sliceview. Can I prevent FOV resetting in some way? I’ve added the observer to revert back the FOV but there is sort of a flickering effect that is unpleasant to the users.<br>
Thanks.</p>

---

## Post #9 by @lassoan (2021-09-30 13:16 UTC)

<p>Check all the places that can change the FOV and propose designs that would allow preserving a custom aspect ratio. Keep everything backward compatible and aim for the minimum number of changes and number of impacted classes.</p>
<p>Was it necessary to apply changes/workarounds to make a custom aspect ratio in slice views work correctly?</p>

---

## Post #10 by @fbordignon (2021-09-30 17:37 UTC)

<p>Thanks for the directions. I will take a look at this.</p>
<p>The custom aspect ratio is working fine. We are even applying segmentation tools with it. It is funny that the paint tool looks like an ellipse when we distort the aspect ratio but I believe it is the expected behavior. I will report if I find any issues, so far so good.</p>

---

## Post #11 by @lassoan (2021-09-30 17:47 UTC)

<aside class="quote no-group" data-username="fbordignon" data-post="10" data-topic="8382">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fbordignon/48/5269_2.png" class="avatar"> fbordignon:</div>
<blockquote>
<p>It is funny that the paint tool looks like an ellipse when we distort the aspect ratio but I believe it is the expected behavior. I will report if I find any issues, so far so good.</p>
</blockquote>
</aside>
<p>That is exactly the correct behavior and probably what you want.</p>
<p>If you have the time and it is not confidential then it would be nice if you could show a few screenshots how it all looks and works.</p>

---

## Post #12 by @fbordignon (2021-09-30 19:57 UTC)

<p>Hey Andras. I’ve recorded a quick demo of the current functionality we are working on. The video can be shared freely. I’ve used a screen cap from the internet as a volume, the real data is way larger on the SI direction. <a href="https://youtu.be/rBt-z9p9vVw" rel="noopener nofollow ugc">https://youtu.be/rBt-z9p9vVw</a><br>
Except for the part I resize the layout the responsiveness is great. I may be calling too many times the FOV repair function, I will look into that to call it always some time after the last resize event.</p>
<p>The goal is to make a panel like this one below. But for now, we are doing an MVP on the segmentation of this kind of data <a href="https://erlend-viggen.no/dlis-files/" rel="noopener nofollow ugc">https://erlend-viggen.no/dlis-files/</a><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/0214760c4e81f1cc8222b65782e7cf2786bacb61.png" data-download-href="/uploads/short-url/ioN98whevqVaeMmWkKqMtRRzwd.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/0214760c4e81f1cc8222b65782e7cf2786bacb61_2_400x500.png" alt="image" data-base62-sha1="ioN98whevqVaeMmWkKqMtRRzwd" width="400" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/0214760c4e81f1cc8222b65782e7cf2786bacb61_2_400x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/0214760c4e81f1cc8222b65782e7cf2786bacb61_2_600x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/0214760c4e81f1cc8222b65782e7cf2786bacb61_2_800x1000.png 2x" data-dominant-color="9CA78C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">800×1000 487 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #13 by @lassoan (2021-10-01 02:58 UTC)

<p>Thanks for sharing, this looks great!</p>

---

## Post #14 by @fbordignon (2021-10-01 16:26 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>, I’ve looked into the FOV resetting and found that the vtkMRMLSliceLogic is checking the aspect ratio of the window against the pane AR <a href="https://github.com/Slicer/Slicer/blob/1b21b7208594f3b6c1ed387ae648c3e9d757f1d0/Libs/MRML/Logic/vtkMRMLSliceLogic.cxx#L1778" rel="noopener nofollow ugc">here</a></p>
<p>How do you feel about the following modification proposal?</p>
<pre><code class="lang-cpp">  double windowAspect = (newWidth != 0. ? newHeight / newWidth : 1.);
  double planeAspect = (newFOV[0] != 0. ? newFOV[1] / newFOV[0] : 1.);
  double oldWindowAspect = (oldDimensions[0] != 0. ? oldDimensions[1] / oldDimensions[0] : 1.);
  double oldPlaneAspect = (oldFOV[0] != 0. ? oldFOV[1] / oldFOV[0] : 1.);
  if (windowAspect != planeAspect &amp;&amp; oldWindowAspect == oldPlaneAspect)
    {
    newFOV[0] = (windowAspect != 0. ? newFOV[1] / windowAspect : newFOV[0]);
    }
</code></pre>
<p>This way the newFOV is corrected only if the user/dev did not change the aspect ratio of the slice view. If the aspect ratio is custom, there is no correction of the AR. While on a custom AR, if the user clicks center to volume on sliceviewcontroller, the AR returns to the original one.<br>
I find it minimally invasive and it keeps the current behavior for the standard not distorted AR. If you think is a good idea I can open a PR for this.<br>
This fix does not perform the behavior I want for the use case above, but the changes I need to apply to the FOV are less dramatic, improving the overall user experience.<br>
Thank you very much.</p>

---

## Post #15 by @lassoan (2021-10-01 17:42 UTC)

<p>If this is the only place where this causes problems then it should not be too hard to customize the behavior.</p>
<p>The window’s aspect ratio can change at any time and it would be hard to guarantee that the plane aspect ratio immediately follows it, so the check above might not be a robust solution.</p>
<p>Instead, what do you think about adding an experimental “AspectRatio” member to vtkMRMLSliceLogic, set to 1.0 by default. In the documentation of the get/set method it would be described that this is an experimental option only and only 1.0 value is tested. If you add sufficient amount of automatic testing that ensures that all important features work well with a non-default aspect ratio then we may consider making this a non-experimental, officially supported feature.</p>

---

## Post #16 by @fbordignon (2021-10-01 18:14 UTC)

<p>Ok thanks for the reply. I will consider working on your suggestion if I find any problems with the current one that I proposed.</p>
<p>One curious thing is that if the user sets the FOV via slice controller, the custom AR is kept when resizing the view. I did not look into how this is achieved.</p>

---

## Post #17 by @lassoan (2021-10-01 19:17 UTC)

<aside class="quote no-group" data-username="fbordignon" data-post="16" data-topic="8382">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fbordignon/48/5269_2.png" class="avatar"> fbordignon:</div>
<blockquote>
<p>I will consider working on your suggestion if I find any problems with the current one that I proposed</p>
</blockquote>
</aside>
<p>It is not likely that we would integrate the change proposed <a href="https://discourse.slicer.org/t/fill-slice-views-without-changing-image-spacing/8382/14">above</a> because it would introduce the risk of the aspect ratio of a view randomly changing. For example, if <code>vtkMRMLSliceLogic::ResizeSliceNode</code> is not called immediately after every slice resize (due to event compression, due to some views are being hidden, due to pausing the rendering, due to a change in how a view is created, etc.) then it could distort the view’s aspect ratio. It would also be important to let developers simply and reliably get/set the aspect ratio of a slice view anytime (even before a window has been created for it). In contrast, introducing an aspect ratio property to the logic is clean and simple, if it proves to be a solid solution and tests are added then it could be even made a property of the slice node.</p>

---

## Post #18 by @fbordignon (2021-10-02 13:30 UTC)

<p>Yes, I understand that my proposal is not ideal, but I will use it internally on our compiled version of slicer for now as it mitigates the issue I was having. As soon as I get the time, I will try to work on the suggestions you gave. I agree that they are better in all aspects. We always struggle with the share of time dedicated to the slicer base and the additional code we add to our client. There is always the feeling we are not contributing as much as we are getting help from the community. To be honest I am the only one messing with the slicer code. Next month a new project will kickoff and we will be adding 4 developers to the team, it should allow for more contributions to slicer <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=10" title=":+1:" class="emoji" alt=":+1:"><br>
Thanks for all the help and I personally appreciate your incentives to try to make us work on the code base.</p>

---

## Post #19 by @lassoan (2021-10-02 14:16 UTC)

<p>Thanks for the information, this sounds great!</p>
<p>If you want, you can add the AspectRatio property to the slice node. That will probably make your implementation simpler.</p>

---
