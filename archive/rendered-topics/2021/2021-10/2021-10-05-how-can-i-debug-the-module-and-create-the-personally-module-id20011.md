---
topic_id: 20011
title: "How Can I Debug The Module And Create The Personally Module"
date: 2021-10-05
url: https://discourse.slicer.org/t/20011
---

# How Can I debug the Module and create the personally Module?

**Topic ID**: 20011
**Date**: 2021-10-05
**URL**: https://discourse.slicer.org/t/how-can-i-debug-the-module-and-create-the-personally-module/20011

---

## Post #1 by @kookoo9999 (2021-10-05 06:53 UTC)

<p>Hello everyone.</p>
<p>I succeeded in building Slicer master branch without SimpleITK because I can’t to solve the fix error(MSB 8066 in SimpleITK.sln) during build Slicer.<br>
and I want to debug each module and I create the module that Augmented Reality module with Camera(3D,Stereo,Web,Usb,etc…).<br>
I build the Slicer.exe but I couldn’t debug the module…<br>
I want to debug each module(ex Volume,Markup,VolumeRendering,Segmentation,etc…) in Slicer because I don’t know how each module works.</p>
<p>Is it right to make a module using Qt Designer?? I am studying Qt.(I usually coded using only c++.)<br>
and I’m curious about the difference between SlicerIGT and OpenIGT and their installation and usage.</p>
<p>Thanks for reading.</p>

---

## Post #2 by @lassoan (2021-10-05 16:17 UTC)

<p>See debugging instructions here:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/debugging/index.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/debugging/index.html</a></p>

---

## Post #3 by @kookoo9999 (2021-10-06 01:18 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="20011">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>e debugging instructions here:</p>
</blockquote>
</aside>
<p>Thanks <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"><br>
I know that among the Add Module to Extension options, scripted is python is the base. Referring to <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/ExtensionWizard#Creating_Extensions" rel="noopener nofollow ugc">this</a>, I made it into a scripted type and modified the UI, but I couldn’t modify it because the console window was quickly opened and closed. (python3.7 is installed.) And then, I selected Add Module to Extension, and created the type to write c++. It’s made like a picture, but I don’t add and automatically load modules like type scripted, so what should I do? As you can see in the picture below, I tried to add a createable path through Extension in Edit-Application Setting, but it doesn’t come out. It doesn’t come up even if you do the Selection Extension of the Extension Wizard.Do I have to build a module separately through CMake?<br>
I want code correction and ui correction.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2eb9a8a105b74d61c655731932650c41c8a1f244.png" data-download-href="/uploads/short-url/6FlJBAIAtdWj7WxvjcSq3pLikZK.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2eb9a8a105b74d61c655731932650c41c8a1f244_2_689x425.png" alt="image" data-base62-sha1="6FlJBAIAtdWj7WxvjcSq3pLikZK" width="689" height="425" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2eb9a8a105b74d61c655731932650c41c8a1f244_2_689x425.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2eb9a8a105b74d61c655731932650c41c8a1f244_2_1033x637.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2eb9a8a105b74d61c655731932650c41c8a1f244.png 2x" data-dominant-color="C9C9E4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1290×795 48 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b4bc59579b1331f2caaf8b973424c179fc0a5c6c.png" data-download-href="/uploads/short-url/pMRtNbu2aXLTAKn030l47deZ3pW.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b4bc59579b1331f2caaf8b973424c179fc0a5c6c.png" alt="image" data-base62-sha1="pMRtNbu2aXLTAKn030l47deZ3pW" width="638" height="499" data-dominant-color="F5F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">776×608 27.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2021-10-06 01:21 UTC)

<p>If you develop a module in C++ then you need to <a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#build-an-extension">build your extension</a>. You can test your module by following <a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#test-an-extension">these instructions</a>.</p>

---

## Post #5 by @kookoo9999 (2021-10-06 01:25 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a><br>
Thanks!! I will try now  <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=10" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #6 by @kookoo9999 (2021-10-06 02:41 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a><br>
Hello,I built a building referring to here.and I added path.<br>
Edit-Application Settings-modules also added the path of qt-loadable-module-deubg of the path created by building a sln made of cmake. However, the module cannot be found on the Slicer.<br>
Did I do something wrong?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6013a2b5f2bec32a0100cf21416d7b914eabbba.png" data-download-href="/uploads/short-url/z6g5oBAVj2a3DMAl6NNEOx0rfce.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f6013a2b5f2bec32a0100cf21416d7b914eabbba_2_690x365.png" alt="image" data-base62-sha1="z6g5oBAVj2a3DMAl6NNEOx0rfce" width="690" height="365" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f6013a2b5f2bec32a0100cf21416d7b914eabbba_2_690x365.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f6013a2b5f2bec32a0100cf21416d7b914eabbba_2_1035x547.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f6013a2b5f2bec32a0100cf21416d7b914eabbba_2_1380x730.png 2x" data-dominant-color="54575A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1018 53.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3c5a8a4898c7c89c931619ffff11ba5e8eff4530.png" data-download-href="/uploads/short-url/8BUD2mwlgrHRglS0uTOK9plZi1y.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3c5a8a4898c7c89c931619ffff11ba5e8eff4530_2_690x426.png" alt="image" data-base62-sha1="8BUD2mwlgrHRglS0uTOK9plZi1y" width="690" height="426" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3c5a8a4898c7c89c931619ffff11ba5e8eff4530_2_690x426.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3c5a8a4898c7c89c931619ffff11ba5e8eff4530_2_1035x639.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3c5a8a4898c7c89c931619ffff11ba5e8eff4530.png 2x" data-dominant-color="EFEFF3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1300×803 57.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e9c690ec8beed351e1d32e9cab8f576ffddf6d06.png" data-download-href="/uploads/short-url/xm4FWCU1aeTEKDWbB8sdmXoqOge.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e9c690ec8beed351e1d32e9cab8f576ffddf6d06_2_690x424.png" alt="image" data-base62-sha1="xm4FWCU1aeTEKDWbB8sdmXoqOge" width="690" height="424" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e9c690ec8beed351e1d32e9cab8f576ffddf6d06_2_690x424.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e9c690ec8beed351e1d32e9cab8f576ffddf6d06_2_1035x636.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e9c690ec8beed351e1d32e9cab8f576ffddf6d06.png 2x" data-dominant-color="F1F1F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1298×799 57.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @lassoan (2021-10-06 02:56 UTC)

<p>Is your module DLL present in the Debug folder that you added?</p>

---

## Post #8 by @kookoo9999 (2021-10-06 03:37 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a><br>
yes, These are the files in the directory.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d61385c96cb1ac28582b6fe758768937cb54814.png" data-download-href="/uploads/short-url/b2x3CJiWZ2LkegrSHbiE9emzOew.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d61385c96cb1ac28582b6fe758768937cb54814.png" alt="image" data-base62-sha1="b2x3CJiWZ2LkegrSHbiE9emzOew" width="690" height="460" data-dominant-color="F3F3F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">816×544 38.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @lassoan (2021-10-06 03:56 UTC)

<p>It looks good, your module is loaded then. If not, then you can find an error message in the application log.</p>

---

## Post #10 by @kookoo9999 (2021-10-06 04:03 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a><br>
Test4 is scripted type. I created lodable type via extension wizard and added the path the picture above but I can’t find Test3 module, How can I check the application log??</p>

---

## Post #11 by @lassoan (2021-10-06 12:33 UTC)

<aside class="quote no-group" data-username="kookoo9999" data-post="10" data-topic="20011">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kookoo9999/48/12394_2.png" class="avatar"> kookoo9999:</div>
<blockquote>
<p>How can I check the application log?</p>
</blockquote>
</aside>
<p>See here: <a href="https://slicer.readthedocs.io/en/latest/user_guide/get_help.html?#i-need-help-in-using-slicer" class="inline-onebox">Get Help — 3D Slicer documentation</a></p>

---

## Post #12 by @kookoo9999 (2021-10-06 15:58 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="11" data-topic="20011">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>See here: <a href="https://slicer.readthedocs.io/en/latest/user_guide/get_help.html?#i-need-help-in-using-slicer" rel="noopener nofollow ugc">Get Help — 3D Slicer documentation</a></p>
</blockquote>
</aside>
<p>Thanks <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"><br>
When I try to debug only the module, if I enter this command on the path, it comes out like this, but how do I solve it?<br>
And what is SlicerRT??<br>
Here is It mentions SlicerRT <a href="https://slicer.readthedocs.io/en/latest/developer_guide/debugging/windowscpp.html#debugging-using-cross-platform-ides" rel="noopener nofollow ugc">here</a>…<br>
c:\D\S4D\Slicer-build&gt;Slicer.exe --VisualStudio --launcher-no-splah --launcher-additional-settings C:\Slicer_Module\bin\inner-build\AdditionalLauncherSettings.ini C:\Slicer_Module\bin\inner-build\Test3.sln<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e4e54d05eb0a5a55909258a88d01b93363ec45d5.png" data-download-href="/uploads/short-url/wEU8yUq9ZLCgGNdW6ANG0JJHrLL.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e4e54d05eb0a5a55909258a88d01b93363ec45d5.png" alt="image" data-base62-sha1="wEU8yUq9ZLCgGNdW6ANG0JJHrLL" width="554" height="500" data-dominant-color="181818"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">953×860 34.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #13 by @kookoo9999 (2021-10-07 06:31 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a>  .<br>
I succeeded to add extension that I made for test. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=10" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #14 by @kookoo9999 (2021-10-23 05:36 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a><br>
Hello lassoan ,<br>
I am making my module with Extension Wizard (type:default, loadable).<br>
If I make a module for Debug and add a module from a Slicer built with Debug, the module will be recognized normally, but it will not be built upon release from the solution of the same module.<br>
Conversely, when adding a module built with Debug, it adds and operates normally.<br>
Other test cases, modules built from Slicer to Release to Debug cannot be added.<br>
In addition, you can add the module created through the extension wizard in the Release Slicer after building it as release, but it is not recognized if you build the module with debug and add it.<br>
In order to develop a module that can be added to a typical user’s Slicer, what kind of environment and how do I set the type of module?</p>

---

## Post #15 by @kookoo9999 (2021-10-23 05:43 UTC)

<p>I checked that module(build-release) is added to stable  Slicer4.13, but not added to Slicer Debug Solution(S4D\slicer-build\Slicer.exe).</p>

---

## Post #16 by @lassoan (2021-11-16 06:54 UTC)

<p>You need to have a completely different build tree for release and debug mode builds.</p>
<p>During development, I mostly use debug builds, which run slower but allow me to step through the code using a debugger. Release are useful for testing the application at full speed and to deployable to end users.</p>

---

## Post #17 by @kookoo9999 (2021-11-16 13:57 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="16" data-topic="20011">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>During development, I mostly use debug builds, which run slower but allow me to step through the code using a debugger. Release are useful for testing the application at full speed and to deployable to end users.</p>
</blockquote>
</aside>
<p>I understood that developing it as Debug when developing and Reesae when distributing it.<br>
When I use debug, Can I debug basic module is VS studio??</p>

---

## Post #18 by @lassoan (2021-11-16 13:58 UTC)

<p>Yes, you debug all the Slicer core modules and your custom modules the same way. Detailed instructions are available here: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/debugging/windowscpp.html" class="inline-onebox">C++ debugging on Windows — 3D Slicer documentation</a></p>

---

## Post #19 by @kookoo9999 (2021-11-16 14:11 UTC)

<p>Slicer Debug Directory : S4D\slicer-build</p>
<p>If I want to debug the Segmentation or Segmentation Editor following this comment…</p>
<blockquote>
<p>.\S4D\Slicer-build\Slicer.exe --VisualStudio --launcher-no-splash --launcher-additional-settings<br>
./SlicerRT_D/inner-build/AdditionalLauncherSettings.ini c:\d_Extensions\SlicerRT_D\inner-build\SlicerRT.sln</p>
</blockquote>
<p>I can find my moudle.sln in my module directory but I can’t find any other loadable-module .sln and Segmentation.sln and  in loadable-module dirctory…</p>

---

## Post #20 by @lassoan (2021-11-16 14:13 UTC)

<aside class="quote no-group" data-username="kookoo9999" data-post="19" data-topic="20011">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kookoo9999/48/12394_2.png" class="avatar"> kookoo9999:</div>
<blockquote>
<p>I can find my moudle.sln in my module directory but I can’t find any other loadable-module .sln and Segmentation.sln and in loadable-module dirctory…</p>
</blockquote>
</aside>
<p>That’s fine, it does not matter which files you see in the project tree in Visual Studio. You can load any of the .cxx files add breakpoints in them, and execution will stop at the breakpoints.</p>

---

## Post #21 by @kookoo9999 (2021-11-16 14:49 UTC)

<blockquote>
<p>That’s fine, it does not matter which files you see in the project tree in Visual Studio. You can load any of the .cxx files add breakpoints in them, and execution will stop at the breakpoints.</p>
</blockquote>
<p>oh…Thanks I understand you comment.<br>
and I have another question…<br>
Ex) in mymoudle.sln build -tree.<br>
mymodulewidget.cxx<br>
mymodule.cxx<br>
What’s the difference between the two?<br>
2. What should I do when I want to add ui that comes out of Slicker’s moudle’s ui by pressing the arrow below?<br>
3. Is there a separate example of using Slicer’s MRML node in Visual Studio? (Sorry for asking this question because I couldn’t find the case for c++)<br>
Is it necessary to modify and develop the logic in the module according to the case of c++?</p>

---

## Post #22 by @kookoo9999 (2021-11-17 15:11 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a><br>
In the code, do member variables like vtkMRML need to be hard-coded separately from ui?<br>
After the ui design, do you tend to directly add files to the functions suitable for ui and implement class constructors and extinction, and other member function member variables? Or is it possible to connect it directly from ui and write it in Visual Studio?</p>

---

## Post #23 by @lassoan (2021-11-17 17:23 UTC)

<p>I don’t understand these questions. I would suggest to follow practices that are used in all the Slicer modules and modules of larger extensions, such as SlicerRT and SlicerIGT.</p>

---
