---
topic_id: 25432
title: "I Have A Trouble With Building Error Msb8066 Can You Help Me"
date: 2022-09-26
url: https://discourse.slicer.org/t/25432
---

# I have a trouble with building error MSB8066 , can you help me please?

**Topic ID**: 25432
**Date**: 2022-09-26
**URL**: https://discourse.slicer.org/t/i-have-a-trouble-with-building-error-msb8066-can-you-help-me-please/25432

---

## Post #1 by @clackch (2022-09-26 03:47 UTC)

<p>VS : 2022 17<br>
Cmake : 3.23.3<br>
3d slicer : lastest (26.09.2022 at github)<br>
Qt : 5.15.2<br>
Release</p>
<pre><code class="lang-auto">MSB8065	"C:\D\S4R\Slicer_BUILD\CTK-build\CMakeFiles\2f17416e874ad1f2a4f8e7019ffe3132\CTK-configure.rule" 항목에 대한 사용자 지정 빌드에 성공했지만 지정한 출력 "c:\d\s4r\slicer_build\ctk-build\ctk-prefix\src\ctk-stamp\release\ctk-configure"is not created. Incremental Build could not work correctly from this error

[C:\D\S4R\Slicer_BUILD\CTK-build\CTK.vcxproj]	CTK	C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Microsoft\VC\v170\Microsoft.CppCommon.targets	247	
경고	MSB8064	"C:\D\S4R\Slicer_BUILD\CTK-build\CMakeFiles\2f17416e874ad1f2a4f8e7019ffe3132\CTK-build.rule" 항목에 대한 사용자 지정 빌드에 성공했지만 지정한 종속성 "c:\d\s4r\slicer_build\ctk-build\ctk-prefix\src\ctk-stamp\release\ctk-configure"is not exist. Incremental Build could not work correctly from this error

[C:\D\S4R\Slicer_BUILD\CTK-build\CTK.vcxproj]	CTK	C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Microsoft\VC\v170\Microsoft.CppCommon.targets	247	
경고		sphinx-build not found: Python documentation will not be created	Slicer	C:\D\S4R\Slicer_BUILD\CUSTOMBUILD	1	

above all Warnings, 

next one is erorr 
-&gt; error MSB8066
'C:\D\S4R\Slicer_BUILD\CMakeFiles\7dc31b6ab96d1080ca2b4d8d149cb3e8\Slicer-configure.rule;C:\D\S4R\Slicer_BUILD\CMakeFiles\7dc31b6ab96d1080ca2b4d8d149cb3e8\Slicer-build.rule;C:\D\S4R\Slicer_BUILD\CMakeFiles\7dc31b6ab96d1080ca2b4d8d149cb3e8\Slicer-forceconfigure.rule;C:\D\S4R\Slicer_BUILD\CMakeFiles\7dc31b6ab96d1080ca2b4d8d149cb3e8\Slicer-install.rule;C:\D\S4R\Slicer_BUILD\CMakeFiles\e75765485e92c28d4a09b8bb403d6889\Slicer-complete.rule;C:\D\S4R\Slicer_BUILD\CMakeFiles\97d39e23b0fa6e15cfd5c11e8080f82e\Slicer.rule;C:\D\S4\Slicer_SOURCE\CMakeLists.txt' the build is quited (code 1).	Slicer	C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Microsoft\VC\v170\Microsoft.CppCommon.targets	247	

</code></pre>
<p>I have searched this error with someone who has same error in 3d slicer forum, but I cannot solve this problem <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=12" title=":wink:" class="emoji" alt=":wink:" loading="lazy" width="20" height="20"><br>
help me please someone who know this error… thank you !</p>
<p>Oh, the other libs are successfully constructed without slicer lib<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/57471ddaa164dfa670c77b587794e7a009abb16b.png" data-download-href="/uploads/short-url/cs5UcT8mAhDYoiXImt3K0vlCub9.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/57471ddaa164dfa670c77b587794e7a009abb16b_2_690x130.png" alt="image" data-base62-sha1="cs5UcT8mAhDYoiXImt3K0vlCub9" width="690" height="130" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/57471ddaa164dfa670c77b587794e7a009abb16b_2_690x130.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/57471ddaa164dfa670c77b587794e7a009abb16b_2_1035x195.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/57471ddaa164dfa670c77b587794e7a009abb16b_2_1380x260.png 2x" data-dominant-color="3A3333"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1427×270 46.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @clackch (2022-09-28 05:41 UTC)

<p>3d slicer patched after 28 SEP 2022, the problem is solved.</p>

---
