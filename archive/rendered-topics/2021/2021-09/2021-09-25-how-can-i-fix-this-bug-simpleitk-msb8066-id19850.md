---
topic_id: 19850
title: "How Can I Fix This Bug Simpleitk Msb8066"
date: 2021-09-25
url: https://discourse.slicer.org/t/19850
---

# How Can I fix this bug SimpleITK (MSB8066)

**Topic ID**: 19850
**Date**: 2021-09-25
**URL**: https://discourse.slicer.org/t/how-can-i-fix-this-bug-simpleitk-msb8066/19850

---

## Post #1 by @kookoo9999 (2021-09-25 13:23 UTC)

<p>I fixed the error of LibArchive for delete line in C:\D\S4R\LibArchive\libarchive\archive_read_support_format_rar5.c line 74.</p>
<p>And now, I can’t fix this error (MSB8066 , when I build the SimpleITK)<br>
I read <a href="https://github.com/Slicer/Slicer/issues/5498" rel="noopener nofollow ugc">here</a> and I try to fix but I can’t understand add these and can’t find the External_SimpleITK.cmake.<br>
Do you mean to add these before configure via CMake-GUI ??<br>
I can find External_SImpleITKExamples.cmake in directory C:\D\S4R\SimpleITK\SuperBuild .</p>
<pre><code class="lang-auto"> if(Slicer_VTK_VERSION_MAJOR STREQUAL "9")
      list(APPEND EXTERNAL_PROJECT_OPTIONAL_CMAKE_CACHE_ARGS
        # Required by FindPython3 CMake module used by VTK
        -DPython3_ROOT_DIR:PATH=${Python3_ROOT_DIR}
        -DPython3_INCLUDE_DIR:PATH=${Python3_INCLUDE_DIR}
        -DPython3_LIBRARY:FILEPATH=${Python3_LIBRARY}
        -DPython3_LIBRARY_DEBUG:FILEPATH=${Python3_LIBRARY_DEBUG}
        -DPython3_LIBRARY_RELEASE:FILEPATH=${Python3_LIBRARY_RELEASE}
        -DPython3_EXECUTABLE:FILEPATH=${Python3_EXECUTABLE}
        )
    endif()
</code></pre>
<div class="md-table">
<table>
<thead>
<tr>
<th>심각도</th>
<th>코드</th>
<th>설명</th>
<th>프로젝트</th>
<th>파일</th>
<th>줄</th>
<th>비표시 오류(Suppression) 상태</th>
</tr>
</thead>
<tbody>
<tr>
<td>오류</td>
<td>MSB8066</td>
<td>'C:\D\S4R\CMakeFiles\b2bcbfa553be6b76f5311151bbb771b6\SimpleITK-configure.rule;C:\D\S4R\CMakeFiles\b2bcbfa553be6b76f5311151bbb771b6\SimpleITK-build.rule;C:\D\S4R\CMakeFiles\b2bcbfa553be6b76f5311151bbb771b6\SimpleITK-install.rule;C:\D\S4R\CMakeFiles\d0fbb327fb5d8976f542b004b1325aa2\SimpleITK-complete.rule;C:\D\S4R\CMakeFiles\dbe9d635f197b17f63b9c895eaab2164\SimpleITK.rule’에 대한 사용자 지정 빌드가 종료되었습니다(코드 1).</td>
<td>SimpleITK</td>
<td>C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Microsoft\VC\v160\Microsoft.CppCo</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
</div>

---

## Post #2 by @lassoan (2021-09-26 04:03 UTC)

<p>This build error and solution (workaround) is discussed <a href="https://github.com/Slicer/Slicer/issues/5498">here</a>.</p>

---
