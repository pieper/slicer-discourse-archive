# I want to boot up with my very own color map and a black background

**Topic ID**: 16383
**Date**: 2021-03-05
**URL**: https://discourse.slicer.org/t/i-want-to-boot-up-with-my-very-own-color-map-and-a-black-background/16383

---

## Post #1 by @Fishguy (2021-03-05 00:36 UTC)

<p>Operating system:OSX<br>
Slicer version:4.11.20200930<br>
Hoped for behavior: Boots with black background in Volume Rendering and either has VolumeProperty_MINE loaded up or on the default list of Presets.<br>
Actual behavior:Boots with medical maps and gradient blue background</p>

---

## Post #2 by @lassoan (2021-03-05 00:38 UTC)

<p>How did you specify the black background and custom volume rendering presets?</p>

---

## Post #3 by @Fishguy (2021-03-05 00:44 UTC)

<p>Andras, I am not finding an option in Settings to do these two things. I can turn off the 3d cube, but not set the background color in Settings&gt;Views, but there is nowhere to pick a default background even from among the three on offer in the pull down for the 3d view. I also cannot find a place to add my volume property.</p>

---

## Post #4 by @lassoan (2021-03-05 01:00 UTC)

<p>We only expose very commonly used settings on the GUI. You can change more settings by opening your application startup script (menu: Edit → Application Settings / General → Application startup script) and specify any additional settings there. For example, copy-paste <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Change_3D_view_background_color">this</a> to change 3D view background color, and copy-paste (and adjust) <a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/volumerendering.html#how-to-register-custom-volume-rendering-presets">this</a> to specify custom volume rendering presets.</p>
<p>If you would like to access these features via GUI then you can <a href="https://github.com/Slicer/Slicer/issues/new?assignees=&amp;labels=type%3Aenhancement&amp;template=feature_request.md">submit feature requests</a>, include links to those issues here, and wait for others to add “thumbs-up” to those issues. We’ll make sure that most frequently asked issues will be implemented.</p>

---

## Post #5 by @Fishguy (2021-03-05 01:20 UTC)

<p>Andras, you have solved my problem! Thanks so much. I am sorry that I could not track this down in the manual or wiki.</p>

---

## Post #6 by @lassoan (2021-03-05 01:53 UTC)

<p>Where did you look? What keywords were you searching for? Maybe we can improve the documentation to make these easier to find.</p>

---

## Post #7 by @Fishguy (2021-03-05 17:18 UTC)

<p>I tried “set default background color”, “change volume background at startup”, “load volume property at startup” and “load custom colormap at startup”.  The background color change was easy. The directions for custom presets are more sparse. I am working my way through them and hope to have some suggestions.</p>
<p>And thanks again for getting a good answer so quickly. Little things make a difference to old people learning new stuff.</p>
<p>-Adam</p>

---

## Post #8 by @Fishguy (2021-03-05 17:34 UTC)

<p>Ok…I have hit a roadblock. I am following the guidance here:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/volumerendering.html#how-to-register-custom-volume-rendering-presets" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/modules/volumerendering.html#how-to-register-custom-volume-rendering-presets</a></p>
<p>I have a new file called MyPresets.mrml in my Slicer Scene Location directory along with a PNG thumbnail.</p>
<p>Now I come to this instruction…<br>
" Use the following code to read all the custom presets from <em>MyPresets.mrml</em> and load it into the scene:"</p>
<p>I do not know how to ‘use’ the code. I pasted it in the Python interpreter window. That did not work. I am betting I have to add to some file…but I do not know which one.</p>
<p>-Adam</p>

---

## Post #9 by @lassoan (2021-03-05 17:45 UTC)

<aside class="quote no-group" data-username="Fishguy" data-post="8" data-topic="16383">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fishguy/48/7337_2.png" class="avatar"> Fishguy:</div>
<blockquote>
<p>I do not know how to ‘use’ the code. I pasted it in the Python interpreter window.</p>
</blockquote>
</aside>
<p>That’s correct. Replace “MyPresets.mrml” by the full path of your presets mrml file and copy-paste it into the Python console (pay attention to <a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#how-to-type-file-paths-in-python">this</a> if you are on Windows). If this all works then you can either add the code to the startup script or add it to a scripted module (as it is done <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/VesselnessFiltering/VesselnessFiltering.py#L31-L49">here</a>).</p>
<aside class="quote no-group" data-username="Fishguy" data-post="7" data-topic="16383">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fishguy/48/7337_2.png" class="avatar"> Fishguy:</div>
<blockquote>
<p>And thanks again for getting a good answer so quickly. Little things make a difference to old people learning new stuff.</p>
</blockquote>
</aside>
<p>No problem at all - it is great to have you here “Fabulous Fish Guy”.</p>
<p>For those who haven’t seen <em>Finding Nemo</em> (or did not pay close attention to the credits):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/acbef31c85e3a6ab2d35f2756335f53808f4c10f.jpeg" data-download-href="/uploads/short-url/oEbeqmmSb236gZLKYQ70dgAV5Gn.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/acbef31c85e3a6ab2d35f2756335f53808f4c10f_2_690x492.jpeg" alt="image" data-base62-sha1="oEbeqmmSb236gZLKYQ70dgAV5Gn" width="690" height="492" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/acbef31c85e3a6ab2d35f2756335f53808f4c10f_2_690x492.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/acbef31c85e3a6ab2d35f2756335f53808f4c10f_2_1035x738.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/acbef31c85e3a6ab2d35f2756335f53808f4c10f.jpeg 2x" data-dominant-color="498AC0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1052×751 157 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @muratmaga (2021-03-06 16:39 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="16383">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>That’s correct. Replace “MyPresets.mrml” by the full path of your presets mrml file and copy-paste it into the Python console (pay attention to <a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#how-to-type-file-paths-in-python">this </a> if you are on Windows). If this all works then you can either add the code to the startup script or add it to a scripted module (as it is done <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/VesselnessFiltering/VesselnessFiltering.py#L31-L49">here </a>).</p>
</blockquote>
</aside>
<p>This works very well. However, is there any way to show my custom presets at the top of the list, as oppose to get appended to the very last?</p>
<p>In fact, is there any way to remove (or at least not displayed) some of those Slicer presets?</p>

---

## Post #11 by @lassoan (2021-03-06 21:26 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="10" data-topic="16383">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>This works very well. However, is there any way to show my custom presets at the top of the list, as oppose to get appended to the very last?</p>
</blockquote>
</aside>
<p>I’ve added an <a href="https://github.com/Slicer/Slicer/pull/5509">option to allow inserting preset to the first or last position</a> (will be available in tomorrow’s Slicer Preview Release).</p>
<aside class="quote no-group" data-username="muratmaga" data-post="10" data-topic="16383">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>In fact, is there any way to remove (or at least not displayed) some of those Slicer presets?</p>
</blockquote>
</aside>
<p>You can call <code>vrLogic.RemovePreset()</code> to remove any of the built-in presets.</p>
<p>Since volume rendering has hundreds of parameters (3 transfer functions with many points, material parameters, lighting parameters, quality settings, custom shaders with many parameters, etc.) the general-purpose Volume Rendering module cannot expose all of these and remain simple and easy-to-use. There will be volume rendering modules optimized for certain applications (for example, we have one for 4D cardiac echo volume rendering). You may consider creating specialized volume rendering module(s) for your applications.</p>

---
