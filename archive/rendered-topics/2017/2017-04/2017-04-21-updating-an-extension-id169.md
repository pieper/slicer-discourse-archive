---
topic_id: 169
title: "Updating An Extension"
date: 2017-04-21
url: https://discourse.slicer.org/t/169
---

# Updating an extension

**Topic ID**: 169
**Date**: 2017-04-21
**URL**: https://discourse.slicer.org/t/updating-an-extension/169

---

## Post #1 by @Lorensen (2017-04-21 18:29 UTC)

<p>It has been a LONG time since I worked with extensions. I have made changes to my extension SwissSkullStripper. I have tested it with my local Slicer build. Now I would like to replace the old version.</p>
<p>When I<br>
make ExperimentalUpload</p>
<p>I get the error:</p>
<pre><code class="lang-auto">Call Stack (most recent call first):
  /home/lorensen/ProjectsGIT/Slicer/Extensions/CMake/SlicerExtensionPackageAndUploadTarget.cmake:260 (midas_api_upload_extension)


CMake Error at /home/lorensen/ProjectsGIT/Slicer/Extensions/CMake/SlicerExtensionPackageAndUploadTarget.cmake:288 (message):
  Upload of
  [73236f9-linux-amd64-SwissSkullStripper-git307bf86-2017-04-21.tar.gz]
  failed !

  Check that:

  (1) you have been granted permission to upload

  (2) your email and api key are correct


 Size of output: 8K
Command exited with the value: 0
MakeCommand:/usr/bin/cmake --build . --config "Release" --target "packageupload" -- -i
Error(s) when building project
   1 Compiler errors
   2 Compiler warnings
SetCTestConfiguration:BuildDirectory:/home/lorensen/ProjectsGIT/SwissSkullStripperExtension/build
SetCTestConfiguration:SourceDirectory:/home/lorensen/ProjectsGIT/SwissSkullStripperExtension/build
SetCTestConfiguration:ProjectName:SwissSkullStripper
SetCTestConfiguration:DropMethod:http
SetCTestConfiguration:DropSite:
SetCTestConfiguration:DropLocation:/submit.php?project=Slicer4
SetCTestConfiguration:IsCDash:TRUE
Submit files (using http)
   Send to track: Extensions-Experimental
   Using HTTP submit method
   Drop site:http:///submit.php?project=Slicer4
   Upload file: /home/lorensen/ProjectsGIT/SwissSkullStripperExtension/build/Testing/20170421-1823/Build.xml to http:///submit.php?project=Slicer4&amp;FileName=___73236f9-SwissSkullStripper-git307bf86-g%2B%2B-64bits-Qt4.8-Release___20170421-1823-Extensions-Experimental___XML___Build.xml&amp;MD5=e6d1eb2838f4ac2a0e8f2037732b710f Size: 3890
   Error when uploading file: /home/lorensen/ProjectsGIT/SwissSkullStripperExtension/build/Testing/20170421-1823/Build.xml
   Error message was: Empty reply from server
   Problems when submitting via HTTP
Uploading package URL for extension SwissSkullStripper ...
make[3]: *** [CMakeFiles/ExperimentalUpload] Error 255
make[2]: *** [CMakeFiles/ExperimentalUpload.dir/all] Error 2
make[1]: *** [CMakeFiles/ExperimentalUpload.dir/rule] Error 2
make: *** [ExperimentalUpload] Error 2
[build(master)]
</code></pre>

---

## Post #2 by @lassoan (2017-04-21 18:38 UTC)

<p>You can test extension packaging and install locally: Build a package and install it in the Extension manager (click the small “wrench” icon in the top-right corner). If all works well then push the updated version and update the git hash in the ExtensionsIndex repository.</p>
<p>The ExperimentalUpload target is only for testing if the extension upload mechanism works correctly. As this mechanism is quite robust (I don’t remember the factory machines having any problem with uploading), you don’t need to test it. If you would like to test it anyway then you need to get an API key and pass it to CMake when you configure the extension (see details here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/BuildTestPackageDistributeExtensions">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/BuildTestPackageDistributeExtensions</a>).</p>

---

## Post #3 by @Lorensen (2017-04-21 18:40 UTC)

<p>I have an old API key. Should that still work.</p>

---

## Post #4 by @lassoan (2017-04-21 18:41 UTC)

<p>I think they have an expiry date. You can probably check it in Midas if it is still active.</p>

---

## Post #5 by @Lorensen (2017-04-21 18:48 UTC)

<p>Yes, it had expired…<br>
I deleted the old one, the the “Generate new API key” does nothing…</p>

---

## Post #6 by @Lorensen (2017-04-21 18:53 UTC)

<p>I see, it wanted an Application Name.</p>

---

## Post #7 by @Lorensen (2017-04-21 18:58 UTC)

<p>I still get the same error on the ExperimentalUpload. BTW, the documentaion mentions the target ExperimentalUploadOnly, but that target does not exist.</p>

---

## Post #8 by @jcfr (2017-04-21 21:59 UTC)

<aside class="quote no-group" data-username="Lorensen" data-post="6" data-topic="169" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lorensen/48/31_2.png" class="avatar"> Lorensen:</div>
<blockquote>
<p>I see, it wanted an Application Name.</p>
</blockquote>
</aside>
<p>Make sure application name is <code>Default</code></p>
<aside class="quote no-group" data-username="Lorensen" data-post="7" data-topic="169" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lorensen/48/31_2.png" class="avatar"> Lorensen:</div>
<blockquote>
<p>I still get the same error on the ExperimentalUpload. BTW, the documentaion mentions the target ExperimentalUploadOnly, but that target does not exist.</p>
</blockquote>
</aside>
<p>Good catch. We need to update the documentation. That target has been removed.</p>
<p>See <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=24289">http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=24289</a></p>
<p>You could instead do</p>
<pre data-code-wrap="bash"><code class="lang-bash">make uploadpackage
</code></pre>
<p>I will fix the corresponding documentation: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ/Extensions#What_are_the_extension_specific_targets:_ExperimentalUpload.2C_ExperimentalUploadOnly.2C_" class="inline-onebox">Documentation/Nightly/Developers/FAQ/Extensions - Slicer Wiki</a>…_.3F</p>

---

## Post #9 by @jcfr (2017-04-21 22:11 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="8" data-topic="169">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>I will fix the corresponding documentation</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/lorensen">@Lorensen</a> I updated the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ/Extensions#What_are_the_extension_specific_targets:_ExperimentalUpload.2C_ExperimentalUploadOnly.2C_..._.3F">developer documentation</a>. Would appreciate if could let me know if there are other currences.</p>

---
