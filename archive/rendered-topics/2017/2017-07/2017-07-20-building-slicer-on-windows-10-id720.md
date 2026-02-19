---
topic_id: 720
title: "Building Slicer On Windows 10"
date: 2017-07-20
url: https://discourse.slicer.org/t/720
---

# Building Slicer on Windows 10

**Topic ID**: 720
**Date**: 2017-07-20
**URL**: https://discourse.slicer.org/t/building-slicer-on-windows-10/720

---

## Post #1 by @sandra (2017-07-20 07:24 UTC)

<p>Hi everyone !</p>
<p>I would like to build Slicer on Windows 10. To do so, I’m using Microsoft Visual Studio 2013 and as a prerequisite I built Qt 5.9.1 (the latest).<br>
Then I use cmake to build Slicer, as option I set QT_QMAKE_EXECUTABLE to the path to qmake and I change Slicer_REQUIRED_QT_VERSION to 5.9.1</p>
<p>I got the following error: “Qt 5.9.1 was not found on your system. You probably need to set the QT_QMAKE_EXECUTABLE variable”. I’ve already set this variable to the right path to qmake …</p>
<p>Any idea ?</p>
<p>Thanks,</p>
<p>Sandra.</p>

---

## Post #2 by @finetjul (2017-07-20 08:03 UTC)

<p>Hi Sandra,</p>
<p>While docs do not expressively mention that Qt 5 is supported by Slicer, it does not say either that you can compile with Qt 5.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions/Prerequisites/Qt#Windows" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions/Prerequisites/Qt#Windows</a></p>
<p>You might want to give a try with the recommended version for Visual Studio 2013 aka Qt 4.8.7</p>
<p>Hth,<br>
Julien.</p>

---

## Post #3 by @pieper (2017-07-20 12:30 UTC)

<p>Hi Sandra -</p>
<p>Julien is right that only the versions of Qt and VisualStudio described on the wiki can be expected to work.</p>
<p>There is experimental work to compile with newer versions but there are still several issues to resolve as described at the link below.  Any help with the port would be very welcome!</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Labs/Qt5" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Labs/Qt5</a></p>
<p>-Steve</p>

---

## Post #4 by @adamrankin (2017-07-23 13:39 UTC)

<p>From</p>
<p><a href="https://sourceforge.net/projects/qt64ng/" rel="nofollow noopener">https://sourceforge.net/projects/qt64ng/</a></p>
<p>download</p>
<p><a href="https://sourceforge.net/projects/qt64ng/files/qt/x86-64/4.8.7/msvc2013/qt-4.8.7-x64-msvc2013.exe/download" rel="nofollow noopener">https://sourceforge.net/projects/qt64ng/files/qt/x86-64/4.8.7/msvc2013/qt-4.8.7-x64-msvc2013.exe/download</a></p>
<p>to save yourself a ton of time.</p>

---

## Post #5 by @lassoan (2017-07-23 14:04 UTC)

<p>I think this downloadable Qt package doesn’t include OpenSSL, so a couple of things will be broken. For example, download of any data from https sites will not work, therefore no sample data can be downloaded, extension manager and some Python packages will not work, etc.</p>
<p>Jc’s one-liner Qt build script works very well, it doesn’t require any user interaction, but it certainly takes a couple of hours of your computer to build.</p>

---

## Post #6 by @adamrankin (2017-07-23 14:06 UTC)

<p>Ooohhh… if we build our own Qt we can enable Slicer_Python_…_OpenSSL?</p>

---

## Post #7 by @jcfr (2017-07-23 17:17 UTC)

<aside class="quote no-group" data-username="adamrankin" data-post="6" data-topic="720">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/adamrankin/48/155_2.png" class="avatar"> adamrankin:</div>
<blockquote>
<p>if we build our own Qt we can enable Slicer_Python_…_OpenSSL?</p>
</blockquote>
</aside>
<p>Yes, this will work nicely on all platforms</p>

---

## Post #8 by @sandra (2017-07-24 07:23 UTC)

<p>Ok, that’s what I thought … So I’m trying to build Qt 4.8.7, not successfully for now.</p>
<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="720" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Jc’s one-liner Qt build script works very well, it doesn’t require any user interaction, but it certainly takes a couple of hours of your computer to build.</p>
</blockquote>
</aside>
<p>I didn’t understand which script you’re talking about (if it is working well I don’t mind if it requires several hours to run)</p>

---

## Post #9 by @lassoan (2017-07-24 11:03 UTC)

<p>It’s described on Slicer build instructions page:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions/Prerequisites/Qt#Windows" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions/Prerequisites/Qt#Windows</a></p>

---

## Post #10 by @sandra (2017-07-25 09:48 UTC)

<p>Yes ok</p>
<p>I tried to build Qt a first time with this script about a week ago and had an error I couldn’t solve.</p>
<p>I tried again yesterday and now it’s working, don’t know why but it’s working !</p>
<p>Thanks</p>

---

## Post #11 by @lassoan (2017-07-25 12:42 UTC)

<p>I and other lab members used the script on several computers without problems. Maybe you haven’t executed the script with sufficient privileges or copy-pasted an incomplete command line. Next time, if you find any errors, report the used command line and displayed error messages immediately.</p>

---

## Post #12 by @Saima (2018-12-19 03:53 UTC)

<p>Hi,<br>
How can I build slicer 4.10 on windows 10. what visual studio is required and what are the other requirements.</p>
<p>Thank you</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #13 by @lassoan (2018-12-19 03:56 UTC)

<p>See this page: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions</a></p>
<p>Follow the instructions very accurately. Let us know if anything is unclear or you run into any issues.</p>

---
