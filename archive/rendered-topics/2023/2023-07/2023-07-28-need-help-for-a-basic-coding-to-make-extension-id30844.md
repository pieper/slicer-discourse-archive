# Need help for a basic coding to make extension

**Topic ID**: 30844
**Date**: 2023-07-28
**URL**: https://discourse.slicer.org/t/need-help-for-a-basic-coding-to-make-extension/30844

---

## Post #1 by @telomere (2023-07-28 01:46 UTC)

<p>Hi, I’m using 3d slicer for repeated works so I want to make my own menu to do it faster.<br>
I have only a basic knowledge of a python language and don’t understand the structure of 3d slicer.<br>
I’m trying to learn through searching but if someone gives me an example, it would be really helpful to understand the basic structure of coding.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d0ee256c84610743d734d4e61922a0f710bbc229.png" alt="image" data-base62-sha1="tOhxsD4Lstl8MqyubPA4Haodjdv" width="437" height="372"><br>
Let’s say I want to make a menu like the image above.<br>
Please show me a code and where to put that code.<br>
(Of course not only a button or a tap for a visual thing but also need a code for functions(making point list, placing a point and linking the functions to the buttons…etc)</p>
<p>Thanks.</p>

---

## Post #2 by @darabi (2023-07-28 11:59 UTC)

<p>Hi telomere,</p>
<p>these are good starting points:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/index.html" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/index.html</a></p>
<p><a href="https://www.slicer.org/w/index.php?title=Documentation/Nightly/Developers" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.slicer.org/w/index.php?title=Documentation/Nightly/Developers</a></p>
<p>Cheers</p>
<p>Kambiz</p>

---

## Post #3 by @ebrahim (2023-07-28 14:00 UTC)

<p>Particularly these parts:<br>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html" rel="noopener nofollow ugc">Extensions section of developer guide</a><br>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#frequently-asked-questions" rel="noopener nofollow ugc">FAQ section</a><br>
<a href="https://slicer.readthedocs.io/en/latest/user_guide/extensions_manager.html" rel="noopener nofollow ugc">User guide for exensions</a></p>
<p>The extension wizard is the way to start. You can use it to just make an extension with one scripted module, no C++. Then the extension would be distributed as python source files only and there’s no building process for it.</p>
<p>You can see the scripted modules that come with Slicer for examples: <a href="https://github.com/Slicer/Slicer/tree/main/Modules/Scripted" rel="noopener nofollow ugc">https://github.com/Slicer/Slicer/tree/main/Modules/Scripted</a><br>
E.g. the endoscopy module is a nice example: <a href="https://github.com/Slicer/Slicer/tree/main/Modules/Scripted/Endoscopy" rel="noopener nofollow ugc">https://github.com/Slicer/Slicer/tree/main/Modules/Scripted/Endoscopy</a><br>
And the script repository has lots of useful sippets: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a></p>

---

## Post #4 by @telomere (2023-07-29 06:47 UTC)

<p>Thanks for the answer.<br>
As you said Endoscopy module is a nice example to study.<br>
And the github link is also very helpful.</p>
<p>Would you mind if i ask some more…<br>
Scripts of some modules like endoscopy are shown in the link but many built-in modules like Volume rendering, Segmentation or Markups are not given as scripts but as a more complicated way…</p>
<p>If it’s very easy for you, could you tell me what should I do, for example, to take volume rendering into my own extension?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5e09052dc414b9909faefd0991f26b0dd586936c.png" data-download-href="/uploads/short-url/dpScTsfVEo2MtZARP7PFpAbi108.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5e09052dc414b9909faefd0991f26b0dd586936c.png" alt="image" data-base62-sha1="dpScTsfVEo2MtZARP7PFpAbi108" width="593" height="500" data-dominant-color="F7F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">835×704 11.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @ebrahim (2023-07-31 12:53 UTC)

<blockquote>
<p>many built-in modules like Volume rendering, Segmentation or Markups are not given as scripts but as a more complicated way</p>
</blockquote>
<p>Right, see the difference between <em>scripted</em> and <em>loadable</em> modules here: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/module_overview.html" class="inline-onebox" rel="noopener nofollow ugc">Module Overview — 3D Slicer documentation</a></p>
<blockquote>
<p>take volume rendering into my own extension</p>
</blockquote>
<p>What does this mean exactly?</p>
<p>Do you mean you want to include the volume rendering module widgets as part of your own module?<br>
I think that’s not advisable – the Slicer way of doing things is to split things across individual modules that each do their own thing well, and to have the user switching between those modules for their overall workflow.</p>

---

## Post #6 by @telomere (2023-08-01 12:18 UTC)

<p>Ah…okay. As you guessed, I wanted to include the volume rendering module widgets as a part of my own module, because I’m doing repeated works so I have to switch modules to often and it makes me too tired…<br>
I think making buttons that go to the modules needed and making a shortcut that comes back to my modules is the most possible solution in my situation.<br>
Thanks.</p>

---
