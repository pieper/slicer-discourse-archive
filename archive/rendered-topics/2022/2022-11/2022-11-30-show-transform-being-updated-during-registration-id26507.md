# Show transform being updated during registration

**Topic ID**: 26507
**Date**: 2022-11-30
**URL**: https://discourse.slicer.org/t/show-transform-being-updated-during-registration/26507

---

## Post #1 by @jay1987 (2022-11-30 12:43 UTC)

<p>hi community<br>
can i set a callback function to brainsfit or elastix when brainsfit or elastix running on each iteration?</p>

---

## Post #3 by @lassoan (2022-12-01 01:48 UTC)

<p>Brainsfit is a CLI module. <a href="https://vtkSlicerCLIModuleLogic.cxx">CLI module output is collected during execution</a> and made accessible when execution ends. If the process output contains specially formatted “progress output” text (information about what stage the processing is in and what is the progress within that stage and what is the overall progress) then that information is displayed during execution in the module GUI. However, I don’t think Brainsfit module provides progress output. You would need to modify it to gather progress input during execution and print it on the process output with that special formatting.</p>
<p>Elastix is a Python scripted module. You can change the part of the Python script that displays the process output in the Python console to print it in a GUI widget or interpret it and use it any way you want (display it as a progress bar, show current metric value, etc.).</p>
<p>What is your overall goal? Would you like to display progress information during registration?</p>

---

## Post #4 by @jay1987 (2022-12-02 02:49 UTC)

<p>thank you very much lassoan<br>
your advice is very helpful , i think i know what to do in next step<br>
yes,my boss want to display registration moving image in each iteration step , he says “it’s owesome to show registration progress on renderwindow when the registration button is pressed”</p>

---

## Post #5 by @lassoan (2022-12-02 15:50 UTC)

<p>I see. Yes, the videos showing the evolution of the registration in time are very cool. During time when you start experimenting with new registration tools it may be actually useful to see this, because you could abort the registration if you see that it is not converging at all.</p>
<p>However, during normal the disadvantage of slowdown (caused by exporting the transformation parameters, applying them, and update the rendering) could be significant, and there would be not much advantage in seeing the evolving transformation.</p>
<p>Implementation for linear transforms could be relatively easy, but it would require some changes in the registration tool (to display transform parameters), a small changes in Slicer core to continuously make the process output available (not just when the registration is finished), and development of a small script that observes the process output and updates the transform in the scene. For warping transforms, passing the transform parameters and applying the transform could be time-consuming, so it could significantly slow down the registration, therefore probably the feature would be very rarely used.</p>
<p>Still, if you are interested in developing this then we can guide you through the process.</p>

---

## Post #6 by @jay1987 (2022-12-05 03:13 UTC)

<p>thank you very much lassoan<br>
thank you for reply so detail<br>
Our use scenario is to register images of different modal of the same patient, so rigid registration is most often used, which is also the reason why similar manufacturers use video to show the registration process<br>
i am  interested in developing this,I hope I can get your guidance !</p>

---

## Post #7 by @lassoan (2022-12-05 13:00 UTC)

<p>The first step is to update the CLI module execution class to save process output into the CLI node during execution (not just at the end, when execution is completed). For this you need to <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/index.html">build Slicer</a>. Let us know if you have managed to build Slicer or you have run into errors that you cannot solve.</p>

---

## Post #8 by @jay1987 (2022-12-06 02:19 UTC)

<p>thank you lassoan<br>
i have managed to build Slicer and understand the code of main module in Slicer<br>
i am trying to start to update the CLI module and wait for the second step <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=12" title=":smile:" class="emoji" alt=":smile:" loading="lazy" width="20" height="20"></p>

---

## Post #9 by @pieper (2022-12-06 17:04 UTC)

<aside class="quote no-group" data-username="jay1987" data-post="8" data-topic="26507">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jay1987/48/16183_2.png" class="avatar"> jay1987:</div>
<blockquote>
<p>i have managed to build Slicer and understand the code of main module in Slicer</p>
</blockquote>
</aside>
<p><img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji only-emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<aside class="quote no-group" data-username="jay1987" data-post="8" data-topic="26507">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jay1987/48/16183_2.png" class="avatar"> jay1987:</div>
<blockquote>
<p>the second step</p>
</blockquote>
</aside>
<p>You may want to use the debugger to go through the code in <code>vtkSlicerCLIModuleLogic.cxx</code> in <a href="https://github.com/Slicer/Slicer/blob/main/Base/QTCLI">this directory</a> to see how progress is handled.  I believe Andras is suggesting that you can extend the progress notification code to include a matrix that would update the transform for a real-time update.</p>

---

## Post #10 by @jay1987 (2022-12-07 00:58 UTC)

<p>thank you pieper!<br>
your suggestion is very detail i think i understand what to do next now</p>

---

## Post #11 by @lassoan (2022-12-07 21:52 UTC)

<p>Congratulations <a class="mention" href="/u/jay1987">@jay1987</a>, successfully building Slicer is already an accomplishment.</p>
<p>I’ve made an improvement in Slicer core (<a href="https://github.com/Slicer/Slicer/pull/6721">pull request</a> is expected to be integrated tonight), which allows continuously monitoring process output. This allows getting transforms from BRAINS and ANTs registration (Elastix output can be captured <a href="https://github.com/lassoan/SlicerElastix/blob/c2e33b8aba51b877bc7e8765ac52f82692c39223/Elastix/Elastix.py#L708">here</a>).</p>
<p>Now, the next step is to check if the registration tool that you want to use has an option to print the current rigid transform parameters on its output. If you cannot find such option, then ask on the forum/support site of the tool to confirm that the tool cannot print the transform parameters and ask advice on how to implement it.</p>
<p>Once you have the transform parameters on the output then you can add a simple scripted module that observes the output of BRAIN, ANTs, or Elastix output and updates a transform node accordingly.</p>

---

## Post #12 by @jay1987 (2022-12-08 01:56 UTC)

<p>thank you lassoan !<br>
thank you for made such work for the question .<br>
i think i can find the way to print the rigid transform parameters on the output<br>
I need some time to complete this function with your help, and then I will share this script for everyone to use.</p>

---
