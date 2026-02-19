---
topic_id: 23514
title: "Dcmtk Error When Building Slicer For Arm64 Macos Monterey"
date: 2022-05-20
url: https://discourse.slicer.org/t/23514
---

# DCMTK error when building Slicer for arm64 MacOS Monterey

**Topic ID**: 23514
**Date**: 2022-05-20
**URL**: https://discourse.slicer.org/t/dcmtk-error-when-building-slicer-for-arm64-macos-monterey/23514

---

## Post #1 by @maribernardes (2022-05-20 21:03 UTC)

<p>When trying to build the Slicer current source in my MacOS Monterey with M1 processor, I get this error message:</p>
<p>– Configuring incomplete, errors occurred!<br>
See also “/opt/s/DCMTK-build/CMakeFiles/CMakeOutput.log”.<br>
See also “/opt/s/DCMTK-build/CMakeFiles/CMakeError.log”.<br>
make[2]: *** [DCMTK-prefix/src/DCMTK-stamp/DCMTK-configure] Error 1<br>
make[2]: Target <code>CMakeFiles/DCMTK.dir/build' not remade because of errors. make[1]: *** [CMakeFiles/DCMTK.dir/all] Error 2 make[1]: Target </code>all’ not remade because of errors.<br>
make: *** [all] Error 2<br>
make: Target `default_target’ not remade because of errors.</p>
<p>Taking a look in CMakeError.log I have found:</p>
<p>Undefined symbols for architecture arm64:<br>
“_iconv”, referenced from:<br>
_main in src.cxx.o<br>
“_iconv_close”, referenced from:<br>
_main in src.cxx.o<br>
“_iconv_open”, referenced from:<br>
_main in src.cxx.o<br>
ld: symbol(s) not found for architecture arm64</p>
<p>Did someone have a similar problem? I would appreciate any light on how to overcome this issue.</p>

---

## Post #2 by @lassoan (2022-05-23 04:21 UTC)

<p>This issue seems very similar to this one:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/QIICR/dcmqi/issues/395">
  <header class="source">

      <a href="https://github.com/QIICR/dcmqi/issues/395" target="_blank" rel="noopener">github.com/QIICR/dcmqi</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/QIICR/dcmqi/issues/395" target="_blank" rel="noopener">Build fails on mac due to iconv undefined symbols</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-02-09" data-time="20:54:59" data-timezone="UTC">08:54PM - 09 Feb 20 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2020-02-12" data-time="19:54:53" data-timezone="UTC">07:54PM - 12 Feb 20 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/pieper" target="_blank" rel="noopener">
          <img alt="pieper" src="https://avatars.githubusercontent.com/u/126077?v=4" class="onebox-avatar-inline" width="20" height="20">
          pieper
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">While testing https://github.com/QIICR/dcmqi/issues/394, I also found that the c<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">urrent master isn't building on mac (10.14.6 mojave).  Same machine builds Slicer fine, so there's something off in the dcmqi superbuild configuration.

```
[  2%] Linking CXX executable ../../bin/ofstd_tests
Undefined symbols for architecture x86_64:
  "_iconv", referenced from:
      OFCharacterEncoding::Implementation::convert(OFString&amp;, char const*, unsigned long) in libofstd.a(ofchrenc.cc.o)
  "_iconv_close", referenced from:
      OFCharacterEncoding::Implementation::~Implementation() in libofstd.a(ofchrenc.cc.o)
  "_iconv_open", referenced from:
      OFCharacterEncoding::Implementation::create(OFString const&amp;, OFString const&amp;, OFCondition&amp;) in libofstd.a(ofchrenc.cc.o)
  "_iconvctl", referenced from:
      OFCharacterEncoding::Implementation::getConversionFlags() const in libofstd.a(ofchrenc.cc.o)
      OFCharacterEncoding::Implementation::setConversionFlags(unsigned int) in libofstd.a(ofchrenc.cc.o)
  "_locale_charset", referenced from:
      OFCharacterEncoding::Implementation::getLocaleEncoding() in libofstd.a(ofchrenc.cc.o)
ld: symbol(s) not found for architecture x86_64
clang: error: linker command failed with exit code 1 (use -v to see invocation)
make[5]: *** [bin/ofstd_tests] Error 1
make[4]: *** [ofstd/tests/CMakeFiles/ofstd_tests.dir/all] Error 2
make[3]: *** [all] Error 2
make[2]: *** [DCMTK-prefix/src/DCMTK-stamp/DCMTK-build] Error 2
make[1]: *** [CMakeFiles/DCMTK.dir/all] Error 2
make: *** [all] Error 2
```</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>There are some workarounds described, but a fix was also implemented, so if you build the latest Slicer master version then this issue should not occur.</p>

---
