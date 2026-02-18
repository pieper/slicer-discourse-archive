# Slicer builded version crash at startup, ntdll problem 

**Topic ID**: 12702
**Date**: 2020-07-23
**URL**: https://discourse.slicer.org/t/slicer-builded-version-crash-at-startup-ntdll-problem/12702

---

## Post #1 by @Zian_Fanti (2020-07-23 02:32 UTC)

<p>Operating system: Windows 10 Pro<br>
Slicer version: 4.11.0 commit 3d72c1f</p>
<p>I successfully build slicer using Visual Studio 19. But crashes when I try to run it. I got the following in the log file:</p>
<pre><code>[DEBUG][Qt] 22.07.2020 20:31:49 [] (unknown:0) - Session start time .......: 2020-07-22 20:31:49
[DEBUG][Qt] 22.07.2020 20:31:49 [] (unknown:0) - Slicer version ...........: 4.11.0-2020-07-06 (revision 29205 / 3d72c1f) win-amd64 - not installed release
[DEBUG][Qt] 22.07.2020 20:31:49 [] (unknown:0) - Operating system .........: Windows / 7 / (Build 7600, Code Page 65001) - 64-bit
[DEBUG][Qt] 22.07.2020 20:31:49 [] (unknown:0) - Memory ...................: 7999 MB physical, 20799 MB virtual
[DEBUG][Qt] 22.07.2020 20:31:49 [] (unknown:0) - CPU ......................: GenuineIntel , 8 cores, 8 logical processors
[DEBUG][Qt] 22.07.2020 20:31:49 [] (unknown:0) - VTK configuration ........: OpenGL2 rendering, TBB threading
[DEBUG][Qt] 22.07.2020 20:31:49 [] (unknown:0) - Qt configuration .........: version 5.15.0, with SSL, requested OpenGL 3.2 (compatibility profile)
[DEBUG][Qt] 22.07.2020 20:31:49 [] (unknown:0) - Developer mode enabled ...: no
[DEBUG][Qt] 22.07.2020 20:31:49 [] (unknown:0) - Prefer executable CLI ....: yes
[DEBUG][Qt] 22.07.2020 20:31:49 [] (unknown:0) - Application path .........: C:/3DS/3DSR/Slicer-build/bin/Release
[DEBUG][Qt] 22.07.2020 20:31:49 [] (unknown:0) - Additional module paths ..: (none)
[DEBUG][Python] 22.07.2020 20:31:53 [Python] (C:\3DS\3DSR\Slicer-build\lib\Slicer-4.11\qt-scripted-odules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations
[DEBUG][Python] 22.07.2020 20:31:55 [Python] (C:\3DS\3DSR\Slicer-build\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 22.07.2020 20:31:55 [Python] (C:\3DS\3DSR\Slicer-build\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Qt] 22.07.2020 20:31:55 [] (unknown:0) - Switch to module:  "Welcome"
</code></pre>
<p>After following the instructions mentioned at " Debugging Slicer application startup issues" I found the following error in the Start Event Viewer:</p>
<pre><code>Nombre de la aplicación con errores: SlicerApp-real.exe, versión: 0.0.0.0, marca de tiempo: 0x5f17e3fa
Nombre del módulo con errores: ntdll.dll, versión: 10.0.18362.815, marca de tiempo: 0xb29ecf52
Código de excepción: 0xc00000fd
Desplazamiento de errores: 0x000000000003c43a
Identificador del proceso con errores: 0x5c
Hora de inicio de la aplicación con errores: 0x01d66086ddb40c79
Ruta de acceso de la aplicación con errores: C:\3DS\3DSR\Slicer-build\bin\Release\SlicerApp-real.exe
Ruta de acceso del módulo con errores: C:\Windows\SYSTEM32\ntdll.dll
Identificador del informe: b439a091-725a-425c-9c26-f1644ffd5c8e
Nombre completo del paquete con errores: 
Identificador de aplicación relativa del paquete con errores: 
</code></pre>
<p>Sorry about the Spanish language in the error, but seems that the error is caused by C:\Windows\SYSTEM32\ntdll.dll.<br>
I tried some proposed solutions for other applications, but none of them works for me.<br>
I tried basically the solutions mentioned here, but without a success.<br>
<a href="https://answers.microsoft.com/en-us/windows/forum/all/app-crash-with-ntdlldll/9aa59f80-99a1-4f3c-b2f0-7eb72df05b2a" class="onebox" target="_blank" rel="nofollow noopener">https://answers.microsoft.com/en-us/windows/forum/all/app-crash-with-ntdlldll/9aa59f80-99a1-4f3c-b2f0-7eb72df05b2a</a></p>
<p>I appreciate if somebody have any suggestion.</p>
<p>Cheers</p>
<p>Zian Fanti</p>

---

## Post #2 by @lassoan (2020-07-23 02:36 UTC)

<p>Could you please build in debug mode and run it in a debugger? Then you can see exactly where the application crashes and why.</p>
<p>If the crash is not reproducible in debug mode then build it in RelWithDebInfo and run it in a debugger. Some symbols may be optimized out, but you should still find enough information about what went wrong.</p>

---

## Post #3 by @jamesobutler (2020-07-23 13:29 UTC)

<aside class="quote no-group" data-username="Zian_Fanti" data-post="1" data-topic="12702">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/zian_fanti/48/7577_2.png" class="avatar"> Zian_Fanti:</div>
<blockquote>
<p><code>Operating system .........: Windows / 7 / (Build 7600, Code Page 65001) - 64-bit</code></p>
</blockquote>
</aside>
<p>Your startup log is indicating that the system you are running it on is Windows 7? Though you built Slicer on Windows 10?</p>
<aside class="quote no-group" data-username="Zian_Fanti" data-post="1" data-topic="12702">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/zian_fanti/48/7577_2.png" class="avatar"> Zian_Fanti:</div>
<blockquote>
<p><code>Nombre del módulo con errores: ntdll.dll, versión: 10.0.18362.815</code></p>
</blockquote>
</aside>
<p>In the error it is indicating about Windows 10 18362 which is the Windows 10 May 2019 update version.</p>

---

## Post #4 by @Zian_Fanti (2020-07-23 17:19 UTC)

<p>Hello James, sorry here.<br>
I posted an erroneous log. The posted log was from a test that I made changing the compatibility properties from the generated Slicer.exe.</p>
<p>This is the correct log file.</p>
<pre><code>[DEBUG][Qt] 23.07.2020 12:08:43 [] (unknown:0) - Session start time .......: 2020-07-23 12:08:43
[DEBUG][Qt] 23.07.2020 12:08:43 [] (unknown:0) - Slicer version ...........: 4.11.0-2020-07-06 (revision 29205 / 3d72c1f) win-amd64 - not installed release
[DEBUG][Qt] 23.07.2020 12:08:43 [] (unknown:0) - Operating system .........: Windows /  Professional / (Build 18362, Code Page 65001) - 64-bit    [DEBUG][Qt] 23.07.2020 12:08:43 [] (unknown:0) - Memory ...................: 7999 MB physical, 20799 MB virtual
[DEBUG][Qt] 23.07.2020 12:08:43 [] (unknown:0) - CPU ......................: GenuineIntel , 8 cores, 8 logical processors
[DEBUG][Qt] 23.07.2020 12:08:43 [] (unknown:0) - VTK configuration ........: OpenGL2 rendering, TBB threading
[DEBUG][Qt] 23.07.2020 12:08:43 [] (unknown:0) - Qt configuration .........: version 5.15.0, with SSL, requested OpenGL 3.2 (compatibility profile)
[DEBUG][Qt] 23.07.2020 12:08:43 [] (unknown:0) - Developer mode enabled ...: no
[DEBUG][Qt] 23.07.2020 12:08:43 [] (unknown:0) - Prefer executable CLI ....: yes
[DEBUG][Qt] 23.07.2020 12:08:43 [] (unknown:0) - Application path .........: C:/3DS/3DSR/Slicer-build/bin/Release
[DEBUG][Qt] 23.07.2020 12:08:43 [] (unknown:0) - Additional module paths ..: (none)
[DEBUG][Python] 23.07.2020 12:08:50 [Python] (C:\3DS\3DSR\Slicer-build\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations
[DEBUG][Python] 23.07.2020 12:08:51 [Python] (C:\3DS\3DSR\Slicer-build\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 23.07.2020 12:08:51 [Python] (C:\3DS\3DSR\Slicer-build\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Qt] 23.07.2020 12:08:51 [] (unknown:0) - Switch to module:  "Welcome"</code></pre>

---

## Post #5 by @lassoan (2020-07-23 20:40 UTC)

<p>Could you build Slicer in Debug or Release with debug info mode and see what error message do you get?</p>

---

## Post #6 by @Zian_Fanti (2020-07-25 01:50 UTC)

<p>Hello Andras.</p>
<p>After several hours in the building process, I finally accomplish the building in debug mode.<br>
I needed to modify a little bit the files “archive_read_support_format_warc.c” and “archive_write_set_format_zip.c” at the LibArchive project, in order to have a successful build. The modification in both files was the same, specified all the options of the declared enums in the switch case statements when needed. Not specified all the options cause a C4061 Error.</p>
<p>So, after a successful build, the program runs without a problem in debug mode. At the moment I don’t know what is happening with the release build.</p>
<p>Cheers</p>

---

## Post #7 by @lassoan (2020-07-25 02:28 UTC)

<p>Thank you for the update, this is good progress. Since there is no crash in debug mode, you need to build and test in Release with debug info (RelWithDebInfo) mode as well.</p>

---

## Post #8 by @pieper (2020-07-26 18:44 UTC)

<aside class="quote no-group" data-username="Zian_Fanti" data-post="6" data-topic="12702">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/zian_fanti/48/7577_2.png" class="avatar"> Zian_Fanti:</div>
<blockquote>
<p>I needed to modify a little bit the files “archive_read_support_format_warc.c” and “archive_write_set_format_zip.c” at the LibArchive project, in order to have a successful build. The modification in both files was the same, specified all the options of the declared enums in the switch case statements when needed. Not specified all the options cause a C4061 Error.</p>
</blockquote>
</aside>
<p>Sorry you ran into to that - it’s been fixed upstream and needs to be added to Slicer’s fork.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/libarchive/pull/2">
  <header class="source">

      <a href="https://github.com/Slicer/libarchive/pull/2" target="_blank" rel="noopener">github.com/Slicer/libarchive</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/libarchive/pull/2" target="_blank" rel="noopener">COMP: explicitly handle all enum cases in switch</a>
      </h4>

    <div class="branches">
      <code>Slicer:slicer-v3.4.0-2019-06-11-614110e7</code> ← <code>pieper:fix-enum-cases</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2020-06-07" data-time="14:30:46" data-timezone="UTC">02:30PM - 07 Jun 20 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/pieper" target="_blank" rel="noopener">
            <img alt="pieper" src="https://avatars.githubusercontent.com/u/126077?v=4" class="onebox-avatar-inline" width="20" height="20">
            pieper
          </a>
        </div>

        <div class="lines" title="1 commits changed 2 files with 21 additions and 0 deletions">
          <a href="https://github.com/Slicer/libarchive/pull/2/files" target="_blank" rel="noopener">
            <span class="added">+21</span>
            <span class="removed">-0</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">In VisualStudio 2019 error C4061 happens if you don't
have a case statement for<span class="show-more-container"><a href="https://github.com/Slicer/libarchive/pull/2" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden"> every value of an enum.
The default condition is not enough.

This fix avoids error like this:

25&gt;C:\sq5\LibArchive\libarchive\archive_read_support_format_warc.c(344,2): error C4061: enumerator 'WT_NONE' in switch of enum 'warc_type_t' is not explicitly handled by a case label [C:\sq5\LibArchive-build\libarchive\archive.vcxproj]</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #9 by @Zian_Fanti (2020-07-28 01:30 UTC)

<p>Good to know that is already fixed</p>

---
