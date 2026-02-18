# When I add module path, unexpected errors have occured - "No module named ****"

**Topic ID**: 999
**Date**: 2017-09-04
**URL**: https://discourse.slicer.org/t/when-i-add-module-path-unexpected-errors-have-occured-no-module-named/999

---

## Post #1 by @shenziheng (2017-09-04 12:21 UTC)

<p>Hello,<br>
I use ExtensionWizard to create a loadable module, and then use Cmake &amp; Visual Studio to build it.<br>
Lastly, I add its path to Additional module paths in Slicer Setting.<br>
But, when I restart 3DSlcier,there are some errors in Python Interactor,like:</p>
<blockquote>
<blockquote>
<p>No module named vtkSlicerIGS_dev1ModuleLogicPython<br>
No module named qSlicerIGS_dev1ModuleWidgetsPythonQt<br>
I really don’t know why.<br>
I’d appreciate it if anyone can help me solve the problem.</p>
</blockquote>
</blockquote>

---

## Post #2 by @lassoan (2017-09-04 12:22 UTC)

<p>File name must exactly match the module class name.</p>

---

## Post #3 by @shenziheng (2017-09-04 14:57 UTC)

<p>I’m sure the file name exactly matches with the module classname.<br>
They are all named by ‘IGS_dev1’.<br>
I also make another try, and test a scripted module. It is OK.<br>
So, I really don’t know why this error just occures in loadable module.</p>

---

## Post #4 by @lassoan (2017-09-04 16:50 UTC)

<p>What directories have you added to the additional module paths?</p>

---

## Post #5 by @shenziheng (2017-09-05 09:30 UTC)

<p>lassoan, it’s really kind of you.<br>
Here, I introduce more detailed information about the error.<br>
Looking forward to your reply.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d50699b3731ab2ac0bb27b37a65037b54f7de3cb.png" data-download-href="/uploads/short-url/uovQevSSSXyQFqflpkurVMNYSZZ.png?dl=1" title="AdditionModulePath" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d50699b3731ab2ac0bb27b37a65037b54f7de3cb.png" alt="AdditionModulePath" data-base62-sha1="uovQevSSSXyQFqflpkurVMNYSZZ" width="690" height="135" data-dominant-color="FAFAFA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">AdditionModulePath</span><span class="informations">1050×206 3.17 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @lassoan (2017-09-05 16:11 UTC)

<p>Which Slicer version did you build?<br>
Did you try to load the module into the Slicer version that you built?<br>
Why your module build tree is inside a Slicer-build tree? (D:\Slicer4D\Slicer-build)<br>
Do you have any errors when you build your module?<br>
Do you have module logic and widget classes?<br>
If you build an existing extension (such as <a href="https://github.com/SlicerHeart/SlicerHeart">https://github.com/SlicerHeart/SlicerHeart</a>) do you get similar errors?</p>

---

## Post #7 by @jcfr (2017-09-05 16:59 UTC)

<p>On windows, simply adding module path is not enough to have the environment updated.</p>
<p>Waiting we address issue <a href="https://issues.slicer.org/view.php?id=4183">#4183</a>, I think possible way around are to:</p>
<ul>
<li>create an extension package and install it as explained in <a href="https://www.slicer.org/wiki/Documentation/4.6/SlicerApplication/ExtensionsManager#Installing_an_extension_without_network_connection">Installing an extension without network connection</a>
</li>
</ul>
<p>or</p>
<ul>
<li>update <code>PATH</code> and <code>PYTHONPATH</code> before starting Slicer</li>
</ul>

---

## Post #8 by @lassoan (2017-09-05 19:25 UTC)

<p>On Windows we always just add the Debug/Release directory to the additional module paths in Slicer application settings. I don’t recall ever seeing this error. Is updating Python paths a new requirement?</p>

---

## Post #9 by @jcfr (2017-09-05 19:30 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="999">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I don’t recall ever seeing this error. Is updating Python paths a new requirement?</p>
</blockquote>
</aside>
<p>No. This was a general remarks about paths.</p>
<p>Since the extension we are talking about doesn’t have any dependencies (beside of Slicer), you are right it should just work.</p>

---

## Post #10 by @lassoan (2017-09-05 19:49 UTC)

<p>I see, thanks.</p>
<p>For extensions that depend on other extensions, the generated “additional launcher settings” ini file takes care of all Python paths (it recursively collects all necessary paths and puts it into the ini file). I’ve implemented this 1-2 months ago.</p>

---

## Post #11 by @shenziheng (2017-09-06 03:53 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>  <a class="mention" href="/u/jcfr">@jcfr</a><br>
Thank you very much.<br>
I have solved the problem in another way.<br>
I adjusted my file path of MyExtension from D:/Slicer4D/Slicer-build/MyExtension to D:/MyExtension.<br>
Luckily,the extension/module worked.<br>
Though I don’t know why it works, I guess there maybe a limited length for file path in windows OS.</p>

---

## Post #12 by @shenziheng (2017-09-06 04:06 UTC)

<p>Slicer 4.7.0<br>
yes, I haved tried.<br>
I am sorry that I didn’t obey the suggestion that official manual give.<br>
No, the building process of Cmake and Visual Studio is OK.<br>
yes, I’m sure I have logic and widget classes.<br>
I ever built an extension - Slicer-IGT, but no errors occured.</p>

---
