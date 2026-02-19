---
topic_id: 6615
title: "I Cannot Find Some Config File While Running Slicervirtualre"
date: 2019-04-26
url: https://discourse.slicer.org/t/6615
---

# I cannot find some config file while running SlicerVirtualReality tests

**Topic ID**: 6615
**Date**: 2019-04-26
**URL**: https://discourse.slicer.org/t/i-cannot-find-some-config-file-while-running-slicervirtualreality-tests/6615

---

## Post #1 by @JaceYang (2019-04-26 02:27 UTC)

<p>I want to run qSlicerVirtualRealityModuleCxxTests but it says<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c4345c663ceb9596e135a68211e9f29d6f3701ca.png" data-download-href="/uploads/short-url/rZHLyk80OXBZvb4vssT0ehGzKxI.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c4345c663ceb9596e135a68211e9f29d6f3701ca_2_690x379.png" alt="image" data-base62-sha1="rZHLyk80OXBZvb4vssT0ehGzKxI" width="690" height="379" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c4345c663ceb9596e135a68211e9f29d6f3701ca_2_690x379.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c4345c663ceb9596e135a68211e9f29d6f3701ca_2_1035x568.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c4345c663ceb9596e135a68211e9f29d6f3701ca_2_1380x758.png 2x" data-dominant-color="C5C8CA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2560×1408 310 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
I already build Slicer and SlicerVirtualReality successfully.<br>
I cannot find qSlicerVirtualRealityModuleGenericCxxTestsLauncherSettings.ini in the SlicerVirtualReality source directory nor SlicerVirtualReality build directory.<br>
And the python error is annoying too.</p>

---

## Post #2 by @lassoan (2019-04-26 02:54 UTC)

<p>Do all the tests pass if you build the “RUN_TESTS” project?</p>
<aside class="quote no-group" data-username="JaceYang" data-post="1" data-topic="6615">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jaceyang/48/3686_2.png" class="avatar"> JaceYang:</div>
<blockquote>
<p>And the python error is annoying too.</p>
</blockquote>
</aside>
<p>Please run Slicer using a Python debugger (as explained <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/DebuggingTools">here</a>) to find what causes the error and send us a pull request with a proposed fix. We’ll review and integrate it quickly.</p>

---

## Post #3 by @cpinter (2019-04-26 02:58 UTC)

<p>You need to start Visual Studio like this:</p>
<p><code>Path\to\debug\build\Slicer-build\Slicer.exe --VisualStudio --launcher-no-splash --launcher-additional-settings ./SlicerVirtualReality_D/inner-build/AdditionalLauncherSettings.ini c:\d\_Extensions\SlicerVirtualReality_D\inner-build\SlicerVirtualReality.sln</code></p>

---

## Post #4 by @JaceYang (2019-04-26 06:51 UTC)

<p>Um,No tests were found…<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7b7f6e4790f40092a6fa0995c5dd84680612fc8.png" data-download-href="/uploads/short-url/x3Sr8gnSV9GJJBXmV0Ob8TsxCEE.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e7b7f6e4790f40092a6fa0995c5dd84680612fc8_2_690x379.png" alt="image" data-base62-sha1="x3Sr8gnSV9GJJBXmV0Ob8TsxCEE" width="690" height="379" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e7b7f6e4790f40092a6fa0995c5dd84680612fc8_2_690x379.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e7b7f6e4790f40092a6fa0995c5dd84680612fc8_2_1035x568.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e7b7f6e4790f40092a6fa0995c5dd84680612fc8_2_1380x758.png 2x" data-dominant-color="E3E6EA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2560×1408 154 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
I downloaded the SlicerVirtualReality-master.zip.Did miss something?</p>

---

## Post #5 by @lassoan (2019-04-26 12:38 UTC)

<p>There are no tests at the superbuild solution (that builds all dependencies). Open the inner-build solution (…\inner-build\SlicerVirtualReality.sln) instead.</p>

---

## Post #6 by @JaceYang (2019-04-28 01:23 UTC)

<p>All tests passed.But I still cannot find the config files.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3da7c01b6d66930f660ca02c0295039aabfa528c.png" data-download-href="/uploads/short-url/8NqwOFKu8bfu8Vw52Q6Bwh6B23O.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3da7c01b6d66930f660ca02c0295039aabfa528c_2_690x379.png" alt="image" data-base62-sha1="8NqwOFKu8bfu8Vw52Q6Bwh6B23O" width="690" height="379" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3da7c01b6d66930f660ca02c0295039aabfa528c_2_690x379.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3da7c01b6d66930f660ca02c0295039aabfa528c_2_1035x568.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3da7c01b6d66930f660ca02c0295039aabfa528c_2_1380x758.png 2x" data-dominant-color="E8ECEF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2560×1408 259 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/8903ae8db83d3252f77dbfe22d431961cc8a740c.png" data-download-href="/uploads/short-url/jy5iI2juV6VZxdR7ZeujZksgh9q.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8903ae8db83d3252f77dbfe22d431961cc8a740c_2_690x379.png" alt="image" data-base62-sha1="jy5iI2juV6VZxdR7ZeujZksgh9q" width="690" height="379" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8903ae8db83d3252f77dbfe22d431961cc8a740c_2_690x379.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8903ae8db83d3252f77dbfe22d431961cc8a740c_2_1035x568.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8903ae8db83d3252f77dbfe22d431961cc8a740c_2_1380x758.png 2x" data-dominant-color="FCFCFD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2560×1408 166 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #7 by @JaceYang (2019-04-28 08:39 UTC)

<p>I download the lastest source code of SlicerDebuggingTools and build it with VS2015x64.<br>
Then I launch the SlicerWithDebuggingTools.exe but it occurred an error which said “Slicer must be restarted after switching between VisualStudio debugger versions.”<br>
I restarted the Slicer(generated from source code) many times but it still not work.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba6d9d909d055bb2eb6fa75df25bba05c8fcfb63.png" data-download-href="/uploads/short-url/qBdETvUbY6qO8fqQs0XSIMJ4GBl.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/ba6d9d909d055bb2eb6fa75df25bba05c8fcfb63_2_690x340.png" alt="image" data-base62-sha1="qBdETvUbY6qO8fqQs0XSIMJ4GBl" width="690" height="340" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/ba6d9d909d055bb2eb6fa75df25bba05c8fcfb63_2_690x340.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/ba6d9d909d055bb2eb6fa75df25bba05c8fcfb63_2_1035x510.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/ba6d9d909d055bb2eb6fa75df25bba05c8fcfb63_2_1380x680.png 2x" data-dominant-color="FCFCFC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2400×1184 243 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fadd3cf0dbf64b4b462142698c7915c50a18a694.jpeg" data-download-href="/uploads/short-url/zNfmOov0sO3WnIbLVqx9Ga8kpU0.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fadd3cf0dbf64b4b462142698c7915c50a18a694_2_690x436.jpeg" alt="image" data-base62-sha1="zNfmOov0sO3WnIbLVqx9Ga8kpU0" width="690" height="436" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fadd3cf0dbf64b4b462142698c7915c50a18a694_2_690x436.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fadd3cf0dbf64b4b462142698c7915c50a18a694_2_1035x654.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fadd3cf0dbf64b4b462142698c7915c50a18a694_2_1380x872.jpeg 2x" data-dominant-color="9EA1B3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2053×1298 331 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But the pythonDebuggingTools(installed in the Slicer by extension manager) works successfully in the Slicer which is installed from an executable binary file.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/3938f05450c1dbbf5a6a73e11e6acda721956390.png" data-download-href="/uploads/short-url/8adcObjPap5GrONMxpykNAhafEA.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3938f05450c1dbbf5a6a73e11e6acda721956390_2_690x465.png" alt="image" data-base62-sha1="8adcObjPap5GrONMxpykNAhafEA" width="690" height="465" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3938f05450c1dbbf5a6a73e11e6acda721956390_2_690x465.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3938f05450c1dbbf5a6a73e11e6acda721956390_2_1035x697.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3938f05450c1dbbf5a6a73e11e6acda721956390_2_1380x930.png 2x" data-dominant-color="ABACBF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1915×1292 171 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @cpinter (2019-04-29 00:03 UTC)

<p>It would help if you described what your overall goal is.</p>

---

## Post #9 by @JaceYang (2019-04-29 01:10 UTC)

<p>We are going to implement some functions which can let doctors manipulate organ models using mouse in Slicer at the same time the 3D view of SlicerVirtualReality will update synchronously and the patients can observe the same view with HTC VIVE  equipped.<br>
But now I cannot use extension manager maybe due to openssl problem?(I’m not sure).And compiling openssl source code is complicated So I install SlicerDebuggingTool from source code(but it can’t work) aiming to solve the python error while running SlicerVirtualReality tests.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2b2a54fbf77fac9404479bda3ec773af37045f60.png" data-download-href="/uploads/short-url/69Re4NPA9xnV5Uz3mEltlCwSnjq.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2b2a54fbf77fac9404479bda3ec773af37045f60_2_690x498.png" alt="image" data-base62-sha1="69Re4NPA9xnV5Uz3mEltlCwSnjq" width="690" height="498" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2b2a54fbf77fac9404479bda3ec773af37045f60_2_690x498.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2b2a54fbf77fac9404479bda3ec773af37045f60_2_1035x747.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2b2a54fbf77fac9404479bda3ec773af37045f60_2_1380x996.png 2x" data-dominant-color="BEBFBF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1787×1292 150 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/379f1a15e5974f60614a901246ac999af8e27f62.png" data-download-href="/uploads/short-url/7W38nnX25BzRPtqJV8xiqwA9rqO.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/379f1a15e5974f60614a901246ac999af8e27f62_2_690x377.png" alt="image" data-base62-sha1="7W38nnX25BzRPtqJV8xiqwA9rqO" width="690" height="377" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/379f1a15e5974f60614a901246ac999af8e27f62_2_690x377.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/379f1a15e5974f60614a901246ac999af8e27f62_2_1035x565.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/379f1a15e5974f60614a901246ac999af8e27f62_2_1380x754.png 2x" data-dominant-color="C5C7CA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2560×1400 274 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #10 by @cpinter (2019-04-29 14:03 UTC)

<p>Thanks for the explanation.</p>
<aside class="quote no-group" data-username="JaceYang" data-post="9" data-topic="6615">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jaceyang/48/3686_2.png" class="avatar"> JaceYang:</div>
<blockquote>
<p>solve the python error while running SlicerVirtualReality tests</p>
</blockquote>
</aside>
<p>This is the part I do not understand. If the build was successful and you can use SlicerVR, then why bother with the tests? Also if the build failed, or SlicerVR doesn’t work in some way then that should be addressed, not the tests.</p>

---

## Post #11 by @JaceYang (2019-04-30 01:43 UTC)

<p>Thank you very much for the suggestions.Now I start to search the frame redraw function in Slicer source code and I want to add the SlicerVR updateViewFromReferenceViewCamera code into it.Could you give some advices one more time?<img src="https://emoji.discourse-cdn.com/twitter/joy.png?v=12" title=":joy:" class="emoji" alt=":joy:" loading="lazy" width="20" height="20"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b415dccf30fd43cc4a533023ba0282b4cca0028.jpeg" data-download-href="/uploads/short-url/d1huNinVcr6tECmatC6aHG8Ygs0.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b415dccf30fd43cc4a533023ba0282b4cca0028_2_690x456.jpeg" alt="image" data-base62-sha1="d1huNinVcr6tECmatC6aHG8Ygs0" width="690" height="456" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b415dccf30fd43cc4a533023ba0282b4cca0028_2_690x456.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b415dccf30fd43cc4a533023ba0282b4cca0028_2_1035x684.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b415dccf30fd43cc4a533023ba0282b4cca0028_2_1380x912.jpeg 2x" data-dominant-color="9EA7D4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2023×1339 246 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #12 by @cpinter (2019-04-30 12:55 UTC)

<aside class="quote no-group" data-username="JaceYang" data-post="11" data-topic="6615">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jaceyang/48/3686_2.png" class="avatar"> JaceYang:</div>
<blockquote>
<p>frame redraw function</p>
</blockquote>
</aside>
<p>Not sure what this is.</p>
<aside class="quote no-group" data-username="JaceYang" data-post="11" data-topic="6615">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jaceyang/48/3686_2.png" class="avatar"> JaceYang:</div>
<blockquote>
<p>add the SlicerVR updateViewFromReferenceViewCamera code into it</p>
</blockquote>
</aside>
<p>Sorry but again I don’t understand what you’d like to achieve. Please give us a bit more info so that we don’t have to do guesswork.<br>
To reset the VR view you just need to call this function: <a href="https://github.com/KitwareMedical/SlicerVirtualReality/blob/master/VirtualReality/Widgets/qMRMLVirtualRealityView.h#L98" class="inline-onebox">SlicerVirtualReality/VirtualReality/Widgets/qMRMLVirtualRealityView.h at master · KitwareMedical/SlicerVirtualReality · GitHub</a></p>

---

## Post #13 by @JaceYang (2019-05-05 01:43 UTC)

<p>I want to complete this:<br>
When I rotate the model(or scene) by left button click or move it by wheel click or zoom it by scrolling the wheel ,Slicer can automatically call the “Set virtual reality view to match reference view”（match view for short） function instead of I clicking the virtualReality toolbar button.<br>
I guess the scene will rerender when it is changed.So I want to add the match view code into the scene rerender function.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4bc3e533a6311ad72ea6fb4db4730c7f1adc2103.jpeg" data-download-href="/uploads/short-url/aOfvS5devGC7S4BYk69uFcfpiAr.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4bc3e533a6311ad72ea6fb4db4730c7f1adc2103_2_690x406.jpeg" alt="image" data-base62-sha1="aOfvS5devGC7S4BYk69uFcfpiAr" width="690" height="406" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4bc3e533a6311ad72ea6fb4db4730c7f1adc2103_2_690x406.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4bc3e533a6311ad72ea6fb4db4730c7f1adc2103_2_1035x609.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4bc3e533a6311ad72ea6fb4db4730c7f1adc2103_2_1380x812.jpeg 2x" data-dominant-color="8FA1D1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2016×1189 295 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Thanks again for your attention!  I just return from the holiday.<img src="https://emoji.discourse-cdn.com/twitter/joy.png?v=12" title=":joy:" class="emoji" alt=":joy:" loading="lazy" width="20" height="20"></p>

---

## Post #14 by @JaceYang (2019-05-06 07:06 UTC)

<p>We have found the functions that we are going to modify.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e9bc5729465ea748e1025860172e2c4209d3316.png" data-download-href="/uploads/short-url/mD7b596JCn8nf11nVFAl5oTgc98.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9e9bc5729465ea748e1025860172e2c4209d3316_2_690x290.png" alt="image" data-base62-sha1="mD7b596JCn8nf11nVFAl5oTgc98" width="690" height="290" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9e9bc5729465ea748e1025860172e2c4209d3316_2_690x290.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9e9bc5729465ea748e1025860172e2c4209d3316_2_1035x435.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9e9bc5729465ea748e1025860172e2c4209d3316_2_1380x580.png 2x" data-dominant-color="F4F5F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2520×1062 276 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c90fdb28484928b5a4c3612e2059ecaf1fc3e525.png" data-download-href="/uploads/short-url/sGFWt89hlZggFOjQlhBF2Jd1PG5.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c90fdb28484928b5a4c3612e2059ecaf1fc3e525_2_690x370.png" alt="image" data-base62-sha1="sGFWt89hlZggFOjQlhBF2Jd1PG5" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c90fdb28484928b5a4c3612e2059ecaf1fc3e525_2_690x370.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c90fdb28484928b5a4c3612e2059ecaf1fc3e525_2_1035x555.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c90fdb28484928b5a4c3612e2059ecaf1fc3e525_2_1380x740.png 2x" data-dominant-color="F8F8F9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2003×1076 179 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
What we are going to do is this:<br>
Adding function “updateViewFromReferenceViewCamera” into function “ProcessMRMLEvents” so that every time I click and drag mouse in the Slicer 3D View, the code in the “ProcessMRMLEvents” function will execute and then the view in HTC VIVE will update immediately.<br>
So the problem we are facing is this:<br>
Integrating the SlicerVirtualReality into Slicer so that we can call function “updateViewFromReferenceViewCamera” in function “ProcessMRMLEvents”.But how can we do that?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d28222aeb98081c1feeea4c05cdb8dc9485681a6.png" data-download-href="/uploads/short-url/u2f58aItmppyzY7xypP9MQrb6Ki.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d28222aeb98081c1feeea4c05cdb8dc9485681a6_2_690x417.png" alt="image" data-base62-sha1="u2f58aItmppyzY7xypP9MQrb6Ki" width="690" height="417" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d28222aeb98081c1feeea4c05cdb8dc9485681a6_2_690x417.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d28222aeb98081c1feeea4c05cdb8dc9485681a6_2_1035x625.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d28222aeb98081c1feeea4c05cdb8dc9485681a6_2_1380x834.png 2x" data-dominant-color="FBFBFB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1710×1034 59.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
