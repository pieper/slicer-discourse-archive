# Can't launch Slicer on Linux - failed to obtain launcher executable name

**Topic ID**: 2694
**Date**: 2018-04-26
**URL**: https://discourse.slicer.org/t/cant-launch-slicer-on-linux-failed-to-obtain-launcher-executable-name/2694

---

## Post #1 by @MGM (2018-04-26 08:34 UTC)

<p>Hi</p>
<p>I can’t open Slicer on Ubuntu 16.04 64 bits :<br>
Linux  4.13.0-38-generic #43~16.04.1-Ubuntu SMP</p>
<p>I tried 2 releases :</p>
<p>1- “Slicer-4.9.0-2018-04-25-linux-amd64” and " , I got this error :<br>
error: Failed to obtain launcher executable name !</p>
<p>2- Slicer-4.0.0-linux-amd64/  ; got the following error :<br>
./bin/SlicerQT-real: error while loading shared libraries: libssl.so.0.9.8: cannot open shared object file: No such file or directory</p>
<p>Any idea !</p>
<p>Thank you</p>

---

## Post #2 by @MGM (2018-04-26 08:42 UTC)

<p>By the way,<br>
I already opened an topic regarding the same issue :</p><aside class="quote quote-modified" data-post="8" data-topic="2322">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/pre-build-or-locally-build-3dslicer-under-ubuntu-16-04-does-not-start-failed-to-obtain-launcher-executable-name/2322/8">Pre-build or Locally-build 3dSlicer under Ubuntu 16.04 does NOT start: Failed to obtain launcher executable name!</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    The error message indicates that the following code path (associated with the function ctkAppLauncherPrivate::extractLauncherNameAndDir) is executed in the launcher: 


The input to that function is obtained here using argv[0]: 


I suspect that on newer Ubuntu, the path the program needs to be obtained from /proc as it is done in qapplication: 


Few days ago, within Slicer itself (and not the launcher) the needed a function allowing to get the path of the application on all platforms before in…
  </blockquote>
</aside>

<p>I still can’t use Slicer, and I need this software on Linux.</p>
<p>Thank again</p>

---

## Post #3 by @brhoom (2018-04-26 09:36 UTC)

<p>Try deleting the Slicer folder setting in your home(rename it if you still need it)</p>
<p><code>rm -rf ~/.config/NA-MIC</code></p>
<p>Or</p>
<p><code>mv ~/.config/NA-MIC ~/.config/SlicerBK</code></p>
<p>Then run Slicer again.</p>

---

## Post #4 by @MGM (2018-04-26 11:56 UTC)

<p><a class="mention" href="/u/brhoom">@brhoom</a><br>
thank you for your feedback</p>
<p>in fact, there is no folder on my home directory</p>

---

## Post #5 by @chir.set (2018-04-26 12:49 UTC)

<aside class="quote no-group" data-username="MGM" data-post="4" data-topic="2694">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/ebca7d/48.png" class="avatar"> MGM:</div>
<blockquote>
<p>there is no folder on my home directory</p>
</blockquote>
</aside>
<p>Try lo locate the NA-MIC directory :</p>
<p>find $HOME -type d -name “NA-MIC”</p>
<p>Some distros don’t put config files in $HOME/.config/</p>

---

## Post #6 by @brhoom (2018-04-26 12:52 UTC)

<p>it is a hidden folder, you just need to run one of the commands I mentioned above then run slicer again. copy paste the command in the terminal and let us know what message you got. No messages means the command run without problem.</p>

---

## Post #7 by @MGM (2018-04-26 12:58 UTC)

<p><a class="mention" href="/u/chir.set">@chir.set</a> <a class="mention" href="/u/brhoom">@brhoom</a><br>
yes, i searched in hidden folder, can’t find</p>

---

## Post #8 by @brhoom (2018-04-26 12:59 UTC)

<p>what is the path of your Slicer. Did you build it yourself or just downloaded the binary from Slicer website?</p>

---

## Post #9 by @MGM (2018-04-26 13:00 UTC)

<p>I placed in ~/Software/Slicer</p>

---

## Post #10 by @brhoom (2018-04-26 13:09 UTC)

<p>The path looks ok. When Slicer run it should create NA-MIC folder in .config. I suggest you try to <a href="https://download.slicer.org/bitstream/738960" rel="nofollow noopener">download</a> the stable version 4.8.1 then <strong>extract</strong> it in ~/Software  then run Slicer in a terminal like this</p>
<pre><code>  ~/Software/Slicer-4.8.1-linux-amd64/Slicer
</code></pre>
<p>if it does not work please write your terminal output here.</p>

---

## Post #11 by @MGM (2018-04-27 08:06 UTC)

<p>Hi <a class="mention" href="/u/brhoom">@brhoom</a></p>
<p>Thank you, this release work fine <img src="https://emoji.discourse-cdn.com/twitter/slightly_smiling_face.png?v=5" title=":slightly_smiling_face:" class="emoji" alt=":slightly_smiling_face:"></p>
<p>Have a good day</p>

---

## Post #12 by @brhoom (2018-04-27 16:12 UTC)

<p>Try also to re-download the nightly build. Sometimes, the downloaded file is corrupted.</p>

---

## Post #13 by @lassoan (2021-06-23 15:14 UTC)

<p>A post was split to a new topic: <a href="/t/cannot-start-slicer-on-linux-cannot-connect-to-x-server/18302">Cannot start Slicer on LInux - cannot connect to X server</a></p>

---
