# Fail to Run Slicer.sln in debug mode

**Topic ID**: 11224
**Date**: 2020-04-21
**URL**: https://discourse.slicer.org/t/fail-to-run-slicer-sln-in-debug-mode/11224

---

## Post #1 by @kobidk (2020-04-21 10:17 UTC)

<p>Operating system:Windows 10<br>
Slicer version:4.10.<br>
Expected behavior: Loading the Slicer App using Slicer.slh in debug mode<br>
Actual behavior: Fails to load some Dlls files integrated into the Slicer project.</p>
<p>I’m trying to run slicer.sln (Start Debugging) after building it successfully for debug mode. I get the following errors.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cdfe85cff6caeffc6182690b5c30d8a9778407bd.png" data-download-href="/uploads/short-url/tojc136rct6bQLJ8gwGd4MVTU6h.png?dl=1" title="ErrorRunDebug_Slicer_sln" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cdfe85cff6caeffc6182690b5c30d8a9778407bd_2_690x367.png" alt="ErrorRunDebug_Slicer_sln" data-base62-sha1="tojc136rct6bQLJ8gwGd4MVTU6h" width="690" height="367" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cdfe85cff6caeffc6182690b5c30d8a9778407bd_2_690x367.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cdfe85cff6caeffc6182690b5c30d8a9778407bd.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cdfe85cff6caeffc6182690b5c30d8a9778407bd.png 2x" data-dominant-color="F2F3F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ErrorRunDebug_Slicer_sln</span><span class="informations">867×462 91.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>It seems to me that the project doesn’t copy the dependency projects DLLs in the Slicer.sln into the folder Slicer-build\bin\debug.<br>
Do I need to copy <strong>manually</strong> all these the projects dlls in that are included in the Slicer.slh to the Slicer-build\bin\debug? or I missed something in the project definition/options.</p>
<p>In addition -<br>
When I run the Slicer.exe directly outside the Slicer.sln It runs but I get the following error.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/15274e5d30027cef8329cea6b0d23bd17e142d51.png" data-download-href="/uploads/short-url/318eRUjZgJhxLktH2EZ7dJKrAaJ.png?dl=1" title="SlicerInitialLoadGUI" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/15274e5d30027cef8329cea6b0d23bd17e142d51_2_690x208.png" alt="SlicerInitialLoadGUI" data-base62-sha1="318eRUjZgJhxLktH2EZ7dJKrAaJ" width="690" height="208" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/15274e5d30027cef8329cea6b0d23bd17e142d51_2_690x208.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/15274e5d30027cef8329cea6b0d23bd17e142d51_2_1035x312.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/15274e5d30027cef8329cea6b0d23bd17e142d51_2_1380x416.png 2x" data-dominant-color="C7C7C6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SlicerInitialLoadGUI</span><span class="informations">1436×434 14.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @cpinter (2020-04-21 10:30 UTC)

<p>You need to start Visual Studio using the launcher like this:<br>
<code>.\S4D\Slicer-build\Slicer.exe --VisualStudio --launcher-no-splash</code></p>
<p>See more information about debugging here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Debug_Instructions#Using_Visual_Studio">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Debug_Instructions#Using_Visual_Studio</a></p>

---

## Post #3 by @kobidk (2020-04-22 07:30 UTC)

<p>Thanks. It’s working. I wonder why we need to work in that way?<br>
Could you please refer to my second question regarding python error that appears in the command line.<br>
Thanks<br>
Kobi</p>

---

## Post #4 by @cpinter (2020-04-22 08:56 UTC)

<p>When starting the latest Slicer version, there are no python errors. If you use any custom modules that may be the reason. If you use an older version of Slicer, then please try the latest.</p>

---
