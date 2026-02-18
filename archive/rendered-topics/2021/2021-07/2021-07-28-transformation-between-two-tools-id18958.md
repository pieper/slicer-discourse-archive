# Transformation Between Two Tools

**Topic ID**: 18958
**Date**: 2021-07-28
**URL**: https://discourse.slicer.org/t/transformation-between-two-tools/18958

---

## Post #1 by @jasmine-lou (2021-07-28 19:41 UTC)

<p>Hello!</p>
<p>Is there any way in Slicer to easily obtain the transform between two tools? I am using the NDI Aurora Tracker with two coils, and can currently obtain transforms between each of the coils and the Aurora tracker, but cannot get a transform between one tool to the other. I also tried adding a transform from tool 1 to tool 2 in the configuration file but that did not seem to do what I intended. Is there a module I can use for this? Thanks!</p>

---

## Post #2 by @pieper (2021-07-28 21:17 UTC)

<p>You probably want <code>vtkMRMLTransformNode::GetTransformBetweenNodes</code> which you can use on either node.  See: <a href="http://apidocs.slicer.org/master/classvtkMRMLTransformNode.html" class="inline-onebox">Slicer: vtkMRMLTransformNode Class Reference</a></p>

---

## Post #3 by @jasmine-lou (2021-07-29 11:57 UTC)

<p>Thank you so much for the response! I don’t think I quite understand the explanation; is there any way I could get that transform via the Slicer App? Or by changing some things in the Plus configuration file?</p>

---

## Post #4 by @pieper (2021-07-29 13:14 UTC)

<p>I’m not sure you can do this at the Plus level, but if you have a custom Python script (or C++ module) you could get the <code>vtkMRMLTransformNode</code> for each of the tools and then get the relative transform that could be used to map coordinates between the two spaces.</p>

---

## Post #5 by @ungi (2021-07-29 17:30 UTC)

<p>In PLUS, you can list any transform (between any two tools) in the PlusOpenIGTLinkServer, TransformNames section of the config file. E.g. if you add this line<br>
<code>&lt;Transform Name="StylusToReference"/&gt;</code><br>
then PLUS will automatically concatenate StylusToTracker and TrackerToReference transforms and send it to Slicer. In Slicer, it will show up as a transform node called “StylusToReference”.</p>

---

## Post #6 by @jasmine-lou (2021-07-29 18:12 UTC)

<p><a class="mention" href="/u/ungi">@ungi</a> is there any scenario where this method would fail? This is what I did initially which was that I had a transform called Tool1ToTool2. However, when I examined the transform while holding my two tools fixed in relation to one another, I was noticing that the translation portion of the transform was changing as I was moving the two tools in unison which made me think that I was doing something incorrectly</p>

---

## Post #7 by @slicer365 (2023-08-14 13:48 UTC)

<p>Hi ,Mr Ungi,I have bought the Aurora device,</p>
<p>I  want to connect it to slicer with Plus,</p>
<p>Now I want to send 2 tools’ position to slicer ,</p>
<p>How should I change the XML file.</p>
<p>I have 2 sensors.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/85b79736c13e50f8e486f618e6995c589eb191c1.png" data-download-href="/uploads/short-url/j4UQnm8LTy0sAu1XdjTaBMmSSFb.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/85b79736c13e50f8e486f618e6995c589eb191c1.png" alt="image" data-base62-sha1="j4UQnm8LTy0sAu1XdjTaBMmSSFb" width="318" height="500" data-dominant-color="EFEFEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">591×927 16.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @ungi (2023-08-14 13:52 UTC)

<p>Hi, here is the PLUS user manual page for Aurora tracker: <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/DeviceNDI.html" class="inline-onebox" rel="noopener nofollow ugc">Plus applications user manual: NDI Vega, Polaris and Aurora pose trackers</a></p>
<p>If you are not familiar with PLUS, you may need to read about the configuration file in general: <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/Configuration.html" class="inline-onebox" rel="noopener nofollow ugc">Plus applications user manual: Device set configuration</a></p>
<p>I hope this helps.</p>

---
