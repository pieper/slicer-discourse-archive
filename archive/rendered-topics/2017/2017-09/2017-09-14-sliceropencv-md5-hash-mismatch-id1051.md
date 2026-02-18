# SlicerOpenCV MD5 hash mismatch

**Topic ID**: 1051
**Date**: 2017-09-14
**URL**: https://discourse.slicer.org/t/sliceropencv-md5-hash-mismatch/1051

---

## Post #1 by @tdiprima (2017-09-14 21:07 UTC)

<p>Hello Folks <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>I’m building SlicerOpenCV.  And I’m getting an error that says that the MD5 hash of SlicerOpenCV-build/OpenCV-prefix/src/3.1.0.tar.gz does not match expected value.</p>
<pre><code>expected: '70e1dd07f0aa06606f1bc0e3fa15abd3'
  actual: 'a0669e22172dfc3225835b180744c9f0'
</code></pre>
<p>So it can’t download OpenCV.</p>
<p>And I think this is why my nightly build is failing.  I’m not sure what to do… should I be contacting the OpenCV folks?</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2017-09-15 00:38 UTC)

<p>Most probably it was a interrupted or corrupted download. Deleting the corrupted file should fix the problem.</p>

---

## Post #3 by @tdiprima (2017-09-15 13:26 UTC)

<p>Andras, I did that twice yesterday.  Tried again today, and still no luck.<br>
Checked Google.  Seems to be a recurring issue.  Thanks for your response.</p>

---

## Post #4 by @lassoan (2017-09-15 15:08 UTC)

<p>What’s in your .tar.gz file? Is it a truncated version of the file that you can download from <a href="https://github.com/Itseez/opencv/archive/3.1.0.tar.gz">https://github.com/Itseez/opencv/archive/3.1.0.tar.gz</a>? Or does it contain an error message (maybe your firewall blocks it…)?</p>

---

## Post #5 by @tdiprima (2017-09-15 15:11 UTC)

<p>Hi guys,</p>
<p>SlicerPathology depends on SlicerOpenCV… I hope you can help me out.</p>
<p>Here’s <a href="http://slicer.cdash.org/viewBuildError.php?buildid=1097176" rel="nofollow noopener">the build error</a>.</p>
<p>And it says:</p>
<pre><code class="lang-auto">-- MD5 hash of
    /.../SlicerOpenCV-build/OpenCV-prefix/src/3.1.0.tar.gz
  does not match expected value
    expected: '70e1dd07f0aa06606f1bc0e3fa15abd3'
      actual: 'a0669e22172dfc3225835b180744c9f0'

 Each download failed!
</code></pre>
<p>Google search indicates a recurring issue that could possibly be resolved with a different CMake version.</p>
<p>Can you guys please help?</p>
<p>Thanks!</p>

---

## Post #6 by @lassoan (2017-09-15 15:16 UTC)

<p>I’ve downloaded the file manually from <a href="https://github.com/Itseez/opencv/archive/3.1.0.tar.gz">https://github.com/Itseez/opencv/archive/3.1.0.tar.gz</a> and the file’s MD5 sum is in fact ‘a0669e22172dfc3225835b180744c9f0’. So, it seems that the package has actually changed. It is not likely that the change is malicious or introduces errors, but it’s quite unusual that a release package is changed many months after it was released.</p>
<p><span class="mention">@tidiprima</span> Could you check if you can find another trustworthy source for OpenCV 3.1.0 source code and compare them to make sure the package we use (<a href="https://github.com/Itseez/opencv/archive/3.1.0.tar.gz">https://github.com/Itseez/opencv/archive/3.1.0.tar.gz</a>) is valid?</p>

---

## Post #7 by @tdiprima (2017-09-15 15:21 UTC)

<p>Nope.  The problem is in SlicerOpenCV code.  Hard-coded MD5.  <a href="https://github.com/SBU-BMI/SlicerOpenCV/blob/master/SuperBuild/External_OpenCV.cmake#L33" rel="nofollow noopener">https://github.com/SBU-BMI/SlicerOpenCV/blob/master/SuperBuild/External_OpenCV.cmake#L33</a></p>

---

## Post #8 by @lassoan (2017-09-15 15:49 UTC)

<p>The value is supposed to be hardcoded (a release package is never supposed to be changed. I would suggest to have a look what is the new content, but ultimately it’s up to the maintainers of that extension to decide if they accept the new version as is or want to do some digging. I saw that you’ve already submitted an issue (<a href="https://github.com/SBU-BMI/SlicerOpenCV/issues/41">https://github.com/SBU-BMI/SlicerOpenCV/issues/41</a>), so that should be enough - maintainers will make the necessary fix soon.</p>

---

## Post #9 by @thewtex (2017-09-17 19:23 UTC)

<p>In conversations with Francois Budin the other day, he noted that the hashes on files hosted on GitHub had the property of not being consistent.</p>
<p>Hosting the data on Midas or Girder may address the issue.</p>

---

## Post #10 by @lassoan (2017-09-17 20:19 UTC)

<p>md5 hash may only differ if the file content is changed. It would be really odd if GitHub would arbitrarily change release files.</p>
<p>Line endings of text files may be translated differently depending on git settings, so maybe that is what you are referring to?</p>

---

## Post #11 by @thewtex (2017-09-18 17:35 UTC)

<p>No, this was for release files instead of Git repository files, which have natural hash checks due to the way Git works.</p>

---
