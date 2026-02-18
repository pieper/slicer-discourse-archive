# General Registration Elastix extension Mac

**Topic ID**: 3791
**Date**: 2018-08-16
**URL**: https://discourse.slicer.org/t/general-registration-elastix-extension-mac/3791

---

## Post #1 by @Laura (2018-08-16 06:53 UTC)

<p>Good morning,</p>
<p>I am trying to download Elastix extension on Mac but I don’t succeed…<br>
I have read and tried through these explanations : <a href="https://github.com/SuperElastix/elastix/wiki/FAQ" rel="nofollow noopener">https://github.com/SuperElastix/elastix/wiki/FAQ</a> , <a href="https://discourse.slicer.org/t/error-with-new-extension-elastix/278">Error with new extension Elastix</a> and <a href="https://github.com/lassoan/SlicerElastix" rel="nofollow noopener">https://github.com/lassoan/SlicerElastix</a><br>
But it is as if I have done nothing…</p>
<p>Can someone explain me step by step what I have to do (I think that I download or load in Slicer in the bad way) ?</p>
<p>Thanks a lot in advance !</p>
<p>P.S. : Moreover, I have a little question : is it possible to save the outputvolume created with this module in a folder that I choose ?</p>
<p>Thanks a lot<br>
Laura</p>

---

## Post #2 by @lassoan (2018-08-16 11:42 UTC)

<p>What Slicer version did you use? Have you found the extension in the extension manager? Installed it? Restarted Slicer and found the module? Set inputs and started the module? Did you get any error messages?</p>

---

## Post #3 by @lassoan (2018-08-16 11:43 UTC)

<aside class="quote no-group" data-username="Laura" data-post="1" data-topic="3791">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/a4c791/48.png" class="avatar"> Laura:</div>
<blockquote>
<p>is it possible to save the outputvolume created with this module in a folder that I choose ?</p>
</blockquote>
</aside>
<p>Yes, if you open the Save data dialog, you can set filename and folder for each data set.</p>

---

## Post #4 by @Laura (2018-08-16 12:41 UTC)

<p>Good afternoon,</p>
<p>My 3D Slicer version is 4.9.0-2018-08-09<br>
In the extension manager, when I look for the “general registration elastix”, I have this message : " No extensions found for macosx:64-bit, revision: ‘27342’. Please try a different combination" with no extension.<br>
So I have tried to download the python script from github but I think that I am doing bad because it doesn’t detect…</p>
<p>But I have read on other posts and on the Internet that this extension exists on Mac so I don’t understand why I doesn’t work with me</p>
<p>Thanks a lot<br>
Laura</p>

---

## Post #5 by @mschumaker (2018-08-16 18:01 UTC)

<p>I just looked at the compiling and testing record for elastix with the Slicer nightly builds, and it appears that extension has not compiled on Mac since the nightly builds moved to using Qt5 and VTK9.<br>
<a href="http://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2018-08-10&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=elastix" class="onebox" target="_blank" rel="nofollow noopener">http://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2018-08-10&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=elastix</a><br>
Something about the extension is incompatible with those, but only on Mac.<br>
It looks like the stable build with Qt4, Slicer 4.8.1, has a functional elastix extension for Mac.</p>

---

## Post #6 by @Laura (2018-08-16 19:11 UTC)

<p>Thanks a lot, so I have to find a way to download the Slicer 4.8.1 version in order to use this extension module ?<br>
I am sorry to ask but I am new on Slicer and only using the last version on the slicer website <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"><br>
Thanks<br>
Laura</p>

---

## Post #7 by @mschumaker (2018-08-16 21:21 UTC)

<p>For now… yes. It’s not the only extension that didn’t make a smooth transition to Slicer 4.9. Usually, using the Nightly Build is a good idea, but not if the extension you want to use isn’t working.<br>
Go to <a href="https://download.slicer.org" rel="nofollow noopener">https://download.slicer.org</a>. Under the Installers heading, the top row is the “Stable Release”, version 4.8.1. It’s dated 2017-12-27.</p>

---

## Post #8 by @Laura (2018-08-17 13:04 UTC)

<aside class="quote no-group" data-username="mschumaker" data-post="7" data-topic="3791">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mschumaker/48/1395_2.png" class="avatar"> mschumaker:</div>
<blockquote>
<p><a href="https://download.slicer.org" rel="noopener nofollow ugc">https://download.slicer.org</a></p>
</blockquote>
</aside>
<p>So many many thank you ! It works perfectly !!!<br>
Laura</p>

---

## Post #9 by @Laura (2018-08-08 06:45 UTC)

<p>Good morning,</p>
<p>I am trying to download Elastix extension on Mac but I don’t succeed…<br>
I have read and tried through these explanations : <a href="https://github.com/SuperElastix/elastix/wiki/FAQ" class="inline-onebox-loading" rel="nofollow noopener">https://github.com/SuperElastix/elastix/wiki/FAQ</a> , <a href="https://discourse.slicer.org/t/error-with-new-extension-elastix/278" class="inline-onebox-loading">https://discourse.slicer.org/t/error-with-new-extension-elastix/278</a> and <a href="https://github.com/lassoan/SlicerElastix" class="inline-onebox-loading" rel="nofollow noopener">https://github.com/lassoan/SlicerElastix</a><br>
But it is as if I have done nothing…</p>
<p>Can someone explain me step by step what I have to do (I think that I download or load in Slicer in the bad way) ?</p>
<p>Thanks a lot in advance !</p>
<p>P.S. : Moreover, I have a little question : is it possible to save the outputvolume created with this module in a folder that I choose ?</p>
<p>Thanks a lot<br>
Laura</p>

---

## Post #10 by @pieper (2019-02-08 16:10 UTC)

<p>Hi Laura -</p>
<p>Thanks for reporting this - I have been able to reproduce this.  There are some cryptic build errors on the factory.  Hopefully it’s something easy to resolve, but I haven’t looked in detail yet.</p>
<pre><code class="lang-auto">Error	
/.../SlicerElastix-build/elastix/Components/FixedImagePyramids/FixedSmoothingPyramid/elxFixedSmoothingPyramid.cxx                          ^:
21:18: note: in instantiation of template class 'elastix::FixedSmoothingPyramid&lt;elastix::ElastixTemplate&lt;itk::Image&lt;float, 3&gt;, itk::Image&lt;float, 3&gt; &gt; &gt;' requested here
elastix/Components/ImageSamplers/Full/elxFullSampler.h:63:16: noteelxInstallMacro( FixedSmoothingPyramid );
:                  ^
in instantiation of member function 'elastix::FullSampler&lt;elastix::ElastixTemplate&lt;itk::Image&lt;float, 2&gt;, itk::Image&lt;float, 2&gt; &gt; &gt;::FullSampler' requested here
elastix/Components/FixedImagePyramids/FixedSmoothingPyramid/elxFixedSmoothingPyramid.cxx:21  itkNewMacro( Self );:
               ^
1: note: in instantiation of member function 'FixedSmoothingPyramid_install&lt;3&gt;::DO' requested here
elxInstallMacro( FixedSmoothingPyramid );
^
</code></pre>
<p><a href="http://slicer.cdash.org/viewBuildError.php?buildid=1508555" class="onebox" target="_blank" rel="nofollow noopener">http://slicer.cdash.org/viewBuildError.php?buildid=1508555</a></p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> or <a class="mention" href="/u/lassoan">@lassoan</a> any ideas?</p>

---

## Post #11 by @cpinter (2019-02-08 16:23 UTC)

<p>I just merged her duplicate message from last August when I was looking for similar posts now related to <a href="https://discourse.slicer.org/t/elastix-extension-for-mac-osx-not-available/5692">this new post</a>. We have done some investigation in October, see <a href="https://discourse.slicer.org/t/slicerelastix-extension-not-available-on-mac/4531" class="inline-onebox">SlicerElastix extension not available on Mac</a></p>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> managed to build it back then. Not sure about the errors you found now, but of the 1000+ errors on the dashboard most of them are just warnings.</p>

---
