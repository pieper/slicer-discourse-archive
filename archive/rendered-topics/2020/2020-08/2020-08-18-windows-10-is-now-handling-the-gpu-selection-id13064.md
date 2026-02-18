# WIndows 10 is now handling the gpu selection

**Topic ID**: 13064
**Date**: 2020-08-18
**URL**: https://discourse.slicer.org/t/windows-10-is-now-handling-the-gpu-selection/13064

---

## Post #1 by @muratmaga (2020-08-18 05:55 UTC)

<p>During the workshop presentation for SlicerMorph I encountered lots of Nvidia driver crashes (unrelated to Slicer). Going through the settings in my laptop, which has dual GPUs (intel + Geforce), I just noticed this message from Nvidia control panel. This must have been a recent change. Does anyone observed issues with this new setting? More importantly is it possible to bring back the old setting (i.e., Nvidia driver handling GPU selection).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c67323b96bb91264814b0341a55ffcdc7085ba1d.png" data-download-href="/uploads/short-url/sjzdUWWy80tFz3CqRTPAQ9pFovj.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c67323b96bb91264814b0341a55ffcdc7085ba1d_2_580x500.png" alt="image" data-base62-sha1="sjzdUWWy80tFz3CqRTPAQ9pFovj" width="580" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c67323b96bb91264814b0341a55ffcdc7085ba1d_2_580x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c67323b96bb91264814b0341a55ffcdc7085ba1d_2_870x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c67323b96bb91264814b0341a55ffcdc7085ba1d_2_1160x1000.png 2x" data-dominant-color="F5F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1192×1027 46.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @jamesobutler (2020-08-18 12:56 UTC)

<p>The Windows 10 graphics setting area for selecting the power saving (integrated) or the high performance (discrete) graphics option has been around since the Windows 10 April 2018 update.</p>
<p>I’m not sure what else would’ve changed. Maybe building with the latest a Windows 10 SDK and something uses some selection differently now?</p>
<p>I still have the option selection in NVidia control panel, but which specification gets used, I’m unsure.</p>

---

## Post #3 by @jamesobutler (2020-08-18 13:06 UTC)

<p>Here is a link describing when the Windows app graphics setting is used versus when the NVidia control panel setting used.</p>
<p><a href="https://www.nvidia.com/content/Control-Panel-Help/vLatest/en-us/mergedProjects/nv3d/Setting_the_Preferred_Graphics_Processor.htm" class="onebox" target="_blank" rel="nofollow noopener">https://www.nvidia.com/content/Control-Panel-Help/vLatest/en-us/mergedProjects/nv3d/Setting_the_Preferred_Graphics_Processor.htm</a></p>
<p>Essentially it seems like if there is an application specification in the Windows 10 graphics setting area it will use that first and if there isn’t one, it will use the NVidia control panel setting.</p>

---

## Post #4 by @lassoan (2020-08-18 13:38 UTC)

<p>I confirm that changing preferred graphics card in Windows settings is not a very recent thing (I had it on a Surface book years ago).</p>
<p>If there are rendering issues or crashes (not unusual for Intel graphics drivers, especially for combined Intel/NVidia) then you may need to wait for a new driver version (if the problems are tolerable) or downgrade to an older driver.</p>

---

## Post #5 by @muratmaga (2020-08-18 18:44 UTC)

<p>Just to be clear, yes the graphics control panel setting has been there for a while, but the actual handling was done through Nvidia control panel, AFAIK. But it appears since May update (which I just got couple weeks ago), that’s no longer the case. So if you are user like me and have been using Nvidia control panel to have Slicer run explicitly on Nvidia card, that will no longer be the case.</p>
<p><a href="https://nvidia.custhelp.com/app/answers/detail/a_id/5035/~/run-with-graphics-processor-missing-from-context-menu%3A-change-in-process-of" class="onebox" target="_blank" rel="nofollow noopener">https://nvidia.custhelp.com/app/answers/detail/a_id/5035/~/run-with-graphics-processor-missing-from-context-menu%3A-change-in-process-of</a></p>
<p>We just have to update what we tell people about running Slicer on multiple GPUs.</p>

---

## Post #6 by @jamesobutler (2020-08-18 22:19 UTC)

<p>Based on the link I posted above it is just that with the recent May 2020 Windows 10 update that if there is a specification in the Windows graphics settings for the Slicer app it will then override that NVidia control panel specification. If there is no specification for it there it will continue to use whatever you specified in the NVidia control panel.</p>
<p>So there shouldn’t be any need for yourself or users to change anything.</p>

---

## Post #7 by @lassoan (2020-08-19 05:06 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="5" data-topic="13064">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>We just have to update what we tell people about running Slicer on multiple GPUs</p>
</blockquote>
</aside>
<p>It would be nice if you could add a note to <a href="https://github.com/Slicer/Slicer/edit/master/Docs/user_guide/modules/volumerendering.md">Volume rendering module documentation</a> about this. Just edit the file and create a pull request when you are asked.</p>

---

## Post #8 by @lassoan (2024-08-01 06:46 UTC)

<p>A post was split to a new topic: <a href="/t/mulri-gpu-inference-with-monailabel/37650">Mulri-GPU inference with MONAILabel</a></p>

---
