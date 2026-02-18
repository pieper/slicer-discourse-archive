# Multiple startup errors and no SimpleITK in May 1 nightly on mac

**Topic ID**: 231
**Date**: 2017-05-01
**URL**: https://discourse.slicer.org/t/multiple-startup-errors-and-no-simpleitk-in-may-1-nightly-on-mac/231

---

## Post #1 by @fedorov (2017-05-01 13:44 UTC)

<p>Startup error:</p>
<pre><code class="lang-auto">code for hash md5 was not found.
Traceback (most recent call last):
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python2.7/hashlib.py", line 147, in &lt;module&gt;
    globals()[__func_name] = __get_hash(__func_name)
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python2.7/hashlib.py", line 97, in __get_builtin_constructor
    raise ValueError('unsupported hash type ' + name)
ValueError: unsupported hash type md5
code for hash sha1 was not found.
Traceback (most recent call last):
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python2.7/hashlib.py", line 147, in &lt;module&gt;
    globals()[__func_name] = __get_hash(__func_name)
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python2.7/hashlib.py", line 97, in __get_builtin_constructor
    raise ValueError('unsupported hash type ' + name)
ValueError: unsupported hash type sha1
code for hash sha224 was not found.
Traceback (most recent call last):
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python2.7/hashlib.py", line 147, in &lt;module&gt;
    globals()[__func_name] = __get_hash(__func_name)
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python2.7/hashlib.py", line 97, in __get_builtin_constructor
    raise ValueError('unsupported hash type ' + name)
ValueError: unsupported hash type sha224
code for hash sha256 was not found.
Traceback (most recent call last):
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python2.7/hashlib.py", line 147, in &lt;module&gt;
    globals()[__func_name] = __get_hash(__func_name)
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python2.7/hashlib.py", line 97, in __get_builtin_constructor
    raise ValueError('unsupported hash type ' + name)
ValueError: unsupported hash type sha256
code for hash sha384 was not found.
Traceback (most recent call last):
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python2.7/hashlib.py", line 147, in &lt;module&gt;
    globals()[__func_name] = __get_hash(__func_name)
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python2.7/hashlib.py", line 97, in __get_builtin_constructor
    raise ValueError('unsupported hash type ' + name)
ValueError: unsupported hash type sha384
code for hash sha512 was not found.
Traceback (most recent call last):
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python2.7/hashlib.py", line 147, in &lt;module&gt;
    globals()[__func_name] = __get_hash(__func_name)
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python2.7/hashlib.py", line 97, in __get_builtin_constructor
    raise ValueError('unsupported hash type ' + name)
ValueError: unsupported hash type sha512
</code></pre>
<p>SimpleITK import error:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; import SimpleITK
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python2.7/site-packages/SimpleITK/__init__.py", line 1, in &lt;module&gt;
    from .SimpleITK import *
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python2.7/site-packages/SimpleITK/SimpleITK.py", line 21, in &lt;module&gt;
    _SimpleITK = swig_import_helper()
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python2.7/site-packages/SimpleITK/SimpleITK.py", line 20, in swig_import_helper
    return importlib.import_module('_SimpleITK')
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python2.7/importlib/__init__.py", line 37, in import_module
    __import__(name)
ImportError: No module named _SimpleITK
</code></pre>

---

## Post #2 by @lassoan (2017-05-01 16:29 UTC)

<p>The dashboard looks quite good.<br>
<a href="http://slicer.cdash.org/index.php?project=Slicer4" class="onebox" target="_blank">http://slicer.cdash.org/index.php?project=Slicer4</a></p>
<p>Does this error come up on other computers, too?</p>

---

## Post #3 by @fedorov (2017-05-01 17:53 UTC)

<p>I confirm I am getting this error even after removing <code>~/.config</code>.</p>

---

## Post #4 by @lassoan (2017-05-01 18:12 UTC)

<p>Do other Mac users have this problem, too?</p>
<p>Have you installed Python or OpenSSL lately? (it might be related, see <a href="https://github.com/Homebrew/legacy-homebrew/issues/22816">https://github.com/Homebrew/legacy-homebrew/issues/22816</a>)</p>
<p>Does it work with earlier Slicer versions? There were Python packaging related changes and OpenSSL library install location change in the past few weeks.</p>

---

## Post #5 by @fedorov (2017-05-01 18:16 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> I have not changed anything in OpenSSL (not to my knowledge, at least!). I did install python via pyenv recently.</p>
<p>I do not use homebrew.</p>
<p>If I disable the new python I installed (it is no longer in my path), I still get the same startup errors.</p>

---

## Post #6 by @lassoan (2017-05-01 20:49 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> and other Mac users: can you reproduce this, too?</p>
<p><a class="mention" href="/u/fedorov">@Fedorov</a> Does the problem occur only with the latest version or earlier nightly or stable version, too?</p>

---

## Post #7 by @fedorov (2017-05-02 01:25 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="231">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Does the problem occur only with the latest version or earlier nightly or stable version, too?</p>
</blockquote>
</aside>
<p>Stable works fine for me. Never had this problem with nightlies before. I tried on another Mac system, different (latest) macOS version, no updates to system python, and I am getting exact same errors.</p>
<p>Remarkable how with all the glorious downloads we get every day not a single Mac user to test this anywhere else.</p>

---

## Post #8 by @fedorov (2017-05-02 02:24 UTC)

<p>It seems that something happened between r25945 (2017-04-25 nightly, works) and r25971 (2017-04-26 nightly, doesn’t work).</p>
<p>As part of this process, I also discovered a new “feature” of macOS + Slicer: apparently, it is no longer possible to allow launching apps from unidentified developers, so every time new Slicer is installed, it has to be launched twice, second time allowing to launch in the security panel. Quite annoying, considering initial launch of Slicer on mac is super slow, and macOS verifies package on each of the 2 launches…</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/176ea84ea65426409c0350396d7f14069a798417.png" alt="image" data-base62-sha1="3li3ZdLDiYdNDHvnRyRZFZZmw5x" width="597" height="166"></p>

---

## Post #9 by @lassoan (2017-05-02 02:44 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> this regression may be related to your Python updates/packaging changes between 25945 and 25971. Could you please check what could be the problem?</p>

---

## Post #10 by @jcfr (2017-05-02 02:58 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="231">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Could you please check what could be the problem?</p>
</blockquote>
</aside>
<p>I see. It may be related to the following commit done between 2.7.11 and 2.7.13.</p>
<p>There is a big storm going on in the area and I lost the ssh connection to the macosx. I will have a look later.</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/python/cpython/commit/c2fc7c4f53">
  <header class="source">

      <a href="https://github.com/python/cpython/commit/c2fc7c4f53" target="_blank" rel="noopener">github.com/python/cpython</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/python/cpython/commit/c2fc7c4f53069558b52d7a497fc195efebe8b4db" target="_blank" rel="noopener">Issue #26470: Port ssl and hashlib module to OpenSSL 1.1.0.</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2016-09-05" data-time="21:37:13" data-timezone="UTC">09:37PM - 05 Sep 16 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/tiran" target="_blank" rel="noopener">
          <img alt="tiran" src="https://avatars.githubusercontent.com/u/444071?v=4" class="onebox-avatar-inline" width="20" height="20">
          tiran
        </a>
      </div>

      <div class="lines" title="changed 6 files with 342 additions and 135 deletions">
        <a href="https://github.com/python/cpython/commit/c2fc7c4f53069558b52d7a497fc195efebe8b4db" target="_blank" rel="noopener">
          <span class="added">+342</span>
          <span class="removed">-135</span>
        </a>
      </div>
    </div>
  </div>
</div>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #11 by @pieper (2017-05-02 11:18 UTC)

<p>I tested the May 1 nightly on a mac with 10.9.5 and it started with no<br>
problem (right click icon and pick open from menu).  I can try other macs<br>
later.</p>

---

## Post #12 by @pieper (2017-05-02 11:48 UTC)

<p>I get the same failures to import hashlib on max os 10.12.4.  Otherwise the<br>
startup process is the same as on older macs (only need to open from menu<br>
and pick okay) probably because I already have the security preference<br>
selected.</p>

---

## Post #13 by @fedorov (2017-05-02 12:13 UTC)

<p>Fails for me on older mac too.</p>

---

## Post #14 by @pieper (2017-05-02 15:37 UTC)

<p>Discussed this with Jc today and he will try going back on python version to use the older OpenSSL for now.</p>

---

## Post #15 by @fedorov (2017-05-02 16:04 UTC)

<aside class="quote no-group" data-username="pieper" data-post="12" data-topic="231">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Otherwise the<br>
startup process is the same as on older macs</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/pieper">@pieper</a> no, startup process is not the same, since in the older mac you could choose “allow from anywhere” (as shown below), and in the newer macs this option is gone (as shown in a post above).</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/56d421b63b80598e4a55647775f8ad8f49352520.jpg" width="375" height="126"></p>

---

## Post #16 by @ihnorton (2017-05-02 16:13 UTC)

<p>Right-click+Open (or Ctrl-click+Open) still works fine for any application. You can restore the “Anywhere” setting in Gatekeeper with a command line switch, see: <a href="http://www.imore.com/how-open-apps-unidentified-developers-mac">http://www.imore.com/how-open-apps-unidentified-developers-mac</a> (not really recommended…)</p>

---

## Post #17 by @fedorov (2017-05-02 16:20 UTC)

<aside class="quote no-group" data-username="ihnorton" data-post="16" data-topic="231">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ihnorton/48/9_2.png" class="avatar"> ihnorton:</div>
<blockquote>
<p>Right-click+Open (or Ctrl-click+Open) still works fine for any application.</p>
</blockquote>
</aside>
<p>I had no idea. I guess this proves that I remain a novice Mac user!</p>

---

## Post #18 by @ihnorton (2017-05-02 17:54 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a> I took a quick look at the 5/1 nightly, and the underlying issue is the failure to <code>import hashlib</code>:</p>
<details>
<summary>
error message</summary>
<pre><code class="lang-auto">import _hashlib
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
ImportError: dlopen(/opt/worksw/Slicer-4.7.0-20170501.app/Contents/lib/Python/lib/python2.7/lib-dynload/_hashlib.so, 2): Library not loaded: libcrypto.dylib
  Referenced from: /opt/worksw/Slicer-4.7.0-20170501.app/Contents/lib/Python/lib/python2.7/lib-dynload/_hashlib.so
  Reason: Incompatible library version: _hashlib.so requires version 1.0.0 or later, but libcrypto.0.9.8.dylib provides version 0.9.8
&gt;&gt;&gt; 
</code></pre>
</details>
<p>There is a <a href="https://github.com/python/cpython/blob/2.7/Lib/hashlib.py#L133-L139"><code>try</code> block around this import</a>, when it fails then Python falls back to looking for the generic versions of the hash functions (which aren’t compiled/available) instead of using the ones from OpenSSL.</p>
<p>Looking at vmmap and dyld debug trace, Slicer is loading both the Slicer version and the system version (/usr/lib/libcrypto.0.9.8.dylib) of libcrypto (and libssl). Slicer version of libcrypto/libssl is opened first, but the system version is preferred when later dlopen’ing the Python <code>_hashlib</code>. (maybe Slicer version is only opened RTLD_LOCAL, while system version is opened RTLD_GLOBAL. no simple way to check this)</p>
<p>It can be fixed locally by correcting the dependency paths, e.g. <code>install_name_tool -change /Users/kitware/Dashboards/Nightly/Slicer-0-build/OpenSSL/libssl.dylib /opt/worksw/Slicer-4.7.0-20170501.app/Contents/lib/Slicer-4.7/libssl.dylib /opt/worksw/Slicer-4.7.0-20170501.app/Contents/lib/Python/lib/python2.7/lib-dynload/_hashlib.so</code> (and likewise for libcrypto).</p>
<p>So possible fixes would be</p>
<ul>
<li>correct ®PATHs for _hashlib on the build system</li>
<li>figure out why we are loading/preferring the system libcrypto at all.</li>
</ul>

---

## Post #19 by @jcfr (2017-05-02 18:20 UTC)

<p><a class="mention" href="/u/ihnorton">@ihnorton</a>  Thanks for the detailed report</p>
<aside class="quote no-group" data-username="ihnorton" data-post="18" data-topic="231">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ihnorton/48/9_2.png" class="avatar"> ihnorton:</div>
<blockquote>
<p>correcting the dependency paths</p>
</blockquote>
</aside>
<p>The following code is/was intended to take care of this, it basically ensures the full path is associated with the libraries which then allow the fixup script to work as expected.</p>
<p><a href="https://github.com/Slicer/Slicer/blob/fba6424b7d48fb4418295105894e317de6e850bf/SuperBuild/External_OpenSSL.cmake#L123-L131" class="onebox" target="_blank" rel="noopener">https://github.com/Slicer/Slicer/blob/fba6424b7d48fb4418295105894e317de6e850bf/SuperBuild/External_OpenSSL.cmake#L123-L131</a></p>
<p>I suspect the regression was introduced here:</p>
<p><a href="https://github.com/Slicer/Slicer/blob/1e9cc24cb026db42f36da9914308366a2d643405/CMake/SlicerCPackBundleFixup.cmake.in#L186-L192" class="onebox" target="_blank" rel="noopener">https://github.com/Slicer/Slicer/blob/1e9cc24cb026db42f36da9914308366a2d643405/CMake/SlicerCPackBundleFixup.cmake.in#L186-L192</a></p>

---

## Post #21 by @jcfr (2017-05-02 19:04 UTC)

<p>I think I identified the issue.</p>
<p>After installing the module into <code>&lt;root&gt;/python-install/lib/python2.7.lib-dynload</code> the full path to the module is stripped and this prevent the fixup package from working.</p>
<p>It was not an issue until now because I suspect the version 0.9.8 of ssl was available on the target system.</p>
<p>Currently working on a fix.</p>

---

## Post #22 by @jcfr (2017-05-02 21:20 UTC)

<p>Issue should be fixed in <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=25996">http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=25996</a></p>
<p>It basically fix a regression introduced in <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=25947">r25947</a>.</p>
<p>Thanks everyone for their help.</p>

---

## Post #23 by @fedorov (2017-05-03 14:00 UTC)

<p>I confirm the issue is fixed in today’s nightly. Thank you!</p>

---

## Post #24 by @lassoan (2017-05-03 21:48 UTC)

<p>We had a full-day Slicer training for about 20 new students, including several Mac users, so this fix has come just in time! (it was great that I could just tell them to install the latest version)</p>

---

## Post #25 by @fedorov (2017-05-03 22:07 UTC)

<p>Would be nice to post-mortem revise how things work on the factories, to see if this kind of issue can be caught automatically next time.</p>

---

## Post #26 by @jcfr (2017-05-03 22:32 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="25" data-topic="231">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>caught automatically next time</p>
</blockquote>
</aside>
<p>Agreed. Our test are all executed on a build tree. Which make sense for “regular” development.</p>
<p>That said, it would be sensible to also execute the tests (e.g the self test) after the package has been generated.</p>
<p>One option would be to have appveyor, travis and circleci triggered after the packaging is completed. They would download the latest package … run few python test and push back the summary in a new entry on Cdash.</p>

---

## Post #27 by @lassoan (2017-05-03 22:36 UTC)

<p>I think the only solution would be to have more build machines, with different OS versions, submitting nightly build&amp;test results.</p>
<p>If we provided easy-to-follow instructions/scripts to do this, who could set it up on his/her computer?<br>
(nightly Slicer core build&amp;test takes 2-4 hours, extensions may take a few hours in addition)</p>

---

## Post #28 by @jcfr (2017-05-04 01:57 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="27" data-topic="231">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>only solution would be to have more build machines</p>
</blockquote>
</aside>
<p>In that case, the issue was specific to the generated  installer and having other build machine wouldn’t have really to detect that problem.</p>
<p>That said, it is generally good to have build and testing on more system.</p>
<p>Otherwise, instructions are currently available here:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/DashboardSetup" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/DashboardSetup</a></p>

---

## Post #29 by @fedorov (2017-05-04 12:47 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="26" data-topic="231">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>One option would be to have appveyor, travis and circleci triggered after the packaging is completed. They would download the latest package … run few python test and push back the summary in a new entry on Cdash.</p>
</blockquote>
</aside>
<p>That would be an interesting experiment. Is there anything in ctest et al to support testing of packaged binaries, or this would need to be scripted from scratch?</p>

---

## Post #30 by @pieper (2017-05-04 23:47 UTC)

<p>Typically Ron downloads the nightlies and lets us know if things don’t start, but since there are many things to test and he’s increasingly busy we should automate the process.</p>
<p>That’s why I suggest we name the script AutomatRon  (get it?!? wink)</p>

---

## Post #31 by @fedorov (2017-05-05 00:17 UTC)

<p>I still think “iRon” is better! <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=5" title=":smile:" class="emoji" alt=":smile:"></p>

---

## Post #32 by @pieper (2017-05-06 18:09 UTC)

<p>Whoever writes the script can name it!</p>

---
