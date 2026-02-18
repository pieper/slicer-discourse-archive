# MacOS Catalina 10.15.5 compilation error

**Topic ID**: 12807
**Date**: 2020-07-31
**URL**: https://discourse.slicer.org/t/macos-catalina-10-15-5-compilation-error/12807

---

## Post #1 by @che85 (2020-07-31 15:08 UTC)

<p>Hi everyone,</p>
<p>I am experiencing compilation errors.</p>
<pre><code class="lang-auto">herzc@54ee75c68e2e ~/D/S4D&gt; /Library/Developer/CommandLineTools/usr/bin/gcc --version
Configured with: --prefix=/Library/Developer/CommandLineTools/usr --with-gxx-include-dir=/usr/include/c++/4.2.1
Apple clang version 11.0.3 (clang-1103.0.32.62)
Target: x86_64-apple-darwin19.5.0
Thread model: posix
InstalledDir: /Library/Developer/CommandLineTools/usr/bin
</code></pre>
<p>cmake version 3.18.1</p>
<p>Here some preview of the error messages:</p>
<pre><code class="lang-auto">/usr/local/include/stdlib.h:141:26: error: pointer is missing a nullability type specifier (_Nonnull, _Nullable, or _Null_unspecified) [-Werror,-Wnullability-completeness]
void    *bsearch(const void *__key, const void *__base, size_t __nel,
                            ^
/usr/local/include/stdlib.h:141:26: note: insert '_Nullable' if the pointer may be null
void    *bsearch(const void *__key, const void *__base, size_t __nel,
                            ^
                              _Nullable 
/usr/local/include/stdlib.h:141:26: note: insert '_Nonnull' if the pointer should never be null
void    *bsearch(const void *__key, const void *__base, size_t __nel,
                            ^
                              _Nonnull 
/usr/local/include/stdlib.h:141:45: error: pointer is missing a nullability type specifier (_Nonnull, _Nullable, or _Null_unspecified) [-Werror,-Wnullability-completeness]
void    *bsearch(const void *__key, const void *__base, size_t __nel,
                                               ^
/usr/local/include/stdlib.h:141:45: note: insert '_Nullable' if the pointer may be null
void    *bsearch(const void *__key, const void *__base, size_t __nel,
                                               ^
                                                 _Nullable 
/usr/local/include/stdlib.h:141:45: note: insert '_Nonnull' if the pointer should never be null
void    *bsearch(const void *__key, const void *__base, size_t __nel,
                                               ^
                                                 _Nonnull 
fatal error: too many errors emitted, stopping now [-ferror-limit=]

</code></pre>
<p>I uploaded a gist here <a href="https://gist.github.com/che85/9cec7d8e0b2a4ada61ff553e51f3c567" rel="nofollow noopener">https://gist.github.com/che85/9cec7d8e0b2a4ada61ff553e51f3c567</a></p>
<p>Does anyone know how to fix these issues? I haven’t seen any recent changes which could have affected the build process and even tried older versions.</p>

---

## Post #2 by @che85 (2020-07-31 15:26 UTC)

<p>I already removed XCode and reinstalled CommandLineTools, but nothing changed.</p>

---

## Post #3 by @lassoan (2020-07-31 15:40 UTC)

<p>There were some libarchive related fixes réce tly that might not have made it into Slicer yet. <a class="mention" href="/u/pieper">@pieper</a> can you confirm? Is there a quick fix?</p>

---

## Post #4 by @pieper (2020-07-31 15:56 UTC)

<p>I don’t get these errors on my mac build.  How do you configure?</p>
<p>This is what I did:</p>
<pre><code class="lang-auto">cmake \
	-DCMAKE_OSX_DEPLOYMENT_TARGET=10.15 \
	Qt5_VERSION:STRING=5.15 \
	Qt5_DIR:PATH=/usr/local/Cellar/qt/5.15.0/lib/cmake/Qt5 \
	/Users/pieper/slicer/latest/Slicer
</code></pre>

---

## Post #5 by @che85 (2020-07-31 16:05 UTC)

<aside class="quote no-group" data-username="pieper" data-post="4" data-topic="12807">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<pre><code class="lang-auto">cmake \
	-DCMAKE_OSX_DEPLOYMENT_TARGET=10.15 \
	Qt5_VERSION:STRING=5.15 \
	Qt5_DIR:PATH=/usr/local/Cellar/qt/5.15.0/lib/cmake/Qt5 \
</code></pre>
</blockquote>
</aside>
<p>Similar to yours:</p>
<pre><code class="lang-auto">cmake \
-DCMAKE_OSX_DEPLOYMENT_TARGET=10.15 \
-DQt5_VERSION:STRING=5.15 \
-DQt5_DIR:PATH=/usr/local/Cellar/qt/5.15.0/lib/cmake/Qt5 \
~/sources/cpp/Slicer
</code></pre>

---

## Post #6 by @che85 (2020-07-31 16:15 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> What are you getting when entering <code>ls -la /usr/local/include/stdlib.h</code></p>
<pre><code class="lang-auto">herzc@54ee75c68e2e ~/s/c/l/bld&gt; ls -la /usr/local/include/stdlib.h
lrwxr-xr-x  1 root  admin  72 Jul 23 23:53 /usr/local/include/stdlib.h -&gt; /Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/stdlib.h
</code></pre>

---

## Post #7 by @che85 (2020-07-31 16:21 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> Do you have the same clang version?</p>

---

## Post #8 by @che85 (2020-07-31 16:50 UTC)

<p>I think there were some headerfiles messsed up on my mac. I think it’s working now. I removed all headerfiles from <code>/usr/local/include</code> that were pointing to <code>/Library/Developer/CommandLineTools</code></p>

---

## Post #9 by @pieper (2020-07-31 18:44 UTC)

<p>Glad it worked <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:"></p>
<p>In case anyone looks in the future, I’ve got a brand new mac (like a week old) with the latest OS and Xcode and the build went smoothly.</p>
<pre><code class="lang-auto">% ls -la /usr/local/include/stdlib.h     
ls: /usr/local/include/stdlib.h: No such file or directory
</code></pre>

---
