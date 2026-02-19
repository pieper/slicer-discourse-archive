---
topic_id: 20085
title: "Slicer On Windows 11"
date: 2021-10-09
url: https://discourse.slicer.org/t/20085
---

# Slicer on Windows 11

**Topic ID**: 20085
**Date**: 2021-10-09
**URL**: https://discourse.slicer.org/t/slicer-on-windows-11/20085

---

## Post #1 by @jamesobutler (2021-10-09 21:57 UTC)

<p>Now that <a href="https://www.microsoft.com/en-us/windows/windows-11" rel="noopener nofollow ugc">Windows 11</a> has been publicly released, I have started to test out Slicer’s compatibility on the new version of the OS.</p>
<p>The latest Slicer stable 4.11.20210226 currently starts without issue on Windows 11, however the latest Slicer Preview is not starting and getting stuck at instantiating modules during the splash screen. I was using today’s preview build Slicer 4.13.0-2021-10-08.</p>
<p>I have currently only been able to start Slicer preview by doing the following to disable scripted modules.<br>
<code>Slicer.exe --disable-builtin-scripted-loadable-modules</code></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/88d04756e3102593e166607c80d2179cb11e5823.png" data-download-href="/uploads/short-url/jwjaBdxNnpoK0Rfcxm5bspiNETV.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/88d04756e3102593e166607c80d2179cb11e5823_2_690x388.png" alt="image" data-base62-sha1="jwjaBdxNnpoK0Rfcxm5bspiNETV" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/88d04756e3102593e166607c80d2179cb11e5823_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/88d04756e3102593e166607c80d2179cb11e5823_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/88d04756e3102593e166607c80d2179cb11e5823_2_1380x776.png 2x" data-dominant-color="62626A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 261 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2021-10-09 22:04 UTC)

<p>Thanks for testing <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=10" title=":+1:" class="emoji" alt=":+1:"></p>
<p>Do you think the failures are due to the preview binary not being signed or something else?</p>

---

## Post #3 by @jamesobutler (2021-10-09 22:21 UTC)

<p>Ok I’ve narrowed it down some more.</p>
<p>After launching Slicer 4.13.0-2021-10-08 successfully with <code>Slicer.exe --disable-builtin-scripted-loadable-modules</code>, Slicer will crash on <code>import numpy</code>. Some scripted modules were importing numpy which was why it was failing on start.</p>

---

## Post #4 by @lassoan (2021-10-10 00:10 UTC)

<p>Wow, I would not have expected this, and most likely Microsoft will fix this soon, but it is worth investigating this just in case.</p>
<p>Are there any useful information in the Windows Event log?</p>
<p>Does installing Visual Studio runtime libraries help?</p>
<p>Can you check if standard <a href="https://www.python.org/downloads/release/python-367/">Python 3.6.7</a> is similarly crashing, too?</p>

---

## Post #5 by @jamesobutler (2021-10-10 00:12 UTC)

<p>Importing <code>numpy</code> from PythonSlicer.exe works, but not with Slicer preview started and using the python console.</p>
<pre><code class="lang-auto">
PS C:\Users\james\AppData\Local\NA-MIC\Slicer 4.13.0-2021-10-08\bin&gt; ./PythonSlicer

Python 3.6.7 (default, Oct  8 2021, 23:20:41) [MSC v.1924 64 bit (AMD64)] on win32

Type "help", "copyright", "credits" or "license" for more information.

&gt;&gt;&gt; import numpy

&gt;&gt;&gt; numpy.__version__

'1.19.5'

</code></pre>
<p>Importing <code>numpy</code> from within Slicer 4.11.20210226 works perfectly.</p>

---

## Post #6 by @jamesobutler (2021-10-10 00:17 UTC)

<p>When importing <code>numpy</code> within Slicer preview console, the application locks up and becomes unresponsive which then the OS wants to close.</p>
<p>I’m currently using latest runtime (14.29.30135). The fact that <code>numpy</code> successfully imports from PythonSlicer, but not within Slicer preview makes me think it is a Slicer problem.</p>
<p>Nothing in the Windows Event Viewer since the app just becomes unresponsive. Just ultimately logged <code>The program SlicerApp-real.exe version 0.0.0.0 stopped interacting with Windows and was closed. </code></p>

---

## Post #7 by @lassoan (2021-10-10 00:28 UTC)

<p>The only thing I can think of is stdout/stderr redirection issue. Does it help if you launch Slicer.exe from the terminal?</p>
<p>What method Slicer gets stuck in? You don’t need to install a debugger, just right-click on SlicerApp-real.exe in ProcessExplorer, go to Threads tab, choose the main thread, and click on Stack button.</p>

---

## Post #8 by @jamesobutler (2021-10-10 00:36 UTC)

<p>Launching the applauncher from powershell has the same results as if I was to launch with a desktop shortcut.</p>
<p>I don’t believe I have used ProcessExplorer before. Is this the type of output you’re looking for?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/146d30be0270dbcb5e49ca42857e333501e5ebd2.png" data-download-href="/uploads/short-url/2UHuiNkOsjAOCBI2lQQLhL01b3k.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/146d30be0270dbcb5e49ca42857e333501e5ebd2.png" alt="image" data-base62-sha1="2UHuiNkOsjAOCBI2lQQLhL01b3k" width="500" height="500" data-dominant-color="ECEDEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">771×771 40.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @lassoan (2021-10-10 01:41 UTC)

<p>Yes, this is the call stack. Usually the main thread is the topmost, but its call stack does not look like usual (it should start with some memory addresses in SlicerApp-real.exe and qSlicerBaseQTCore.dll!qSlicerCoreApplication::exec). Maybe the application was already shutting down.</p>
<p>You might need a debug-mode build to make it easier to see where the application is hanging.</p>

---

## Post #10 by @jamesobutler (2021-10-10 14:26 UTC)

<p>With my debug build of Slicer, here is the stack at startup using <code>./Slicer.exe --disable-builtin-scripted-loadable-modules</code>.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de9e11e11ff49f617dee0eefa13ca83a6c20873a.png" data-download-href="/uploads/short-url/vLmF0R3FOvFTtPvqWeo1xJ38VlM.png?dl=1" title="stack-call-debug-startup" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de9e11e11ff49f617dee0eefa13ca83a6c20873a.png" alt="stack-call-debug-startup" data-base62-sha1="vLmF0R3FOvFTtPvqWeo1xJ38VlM" width="503" height="500" data-dominant-color="EBEBEB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">stack-call-debug-startup</span><span class="informations">767×762 52.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Then the stack after doing <code>import numpy</code>.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c499ae297cbd46e786e714f434d42ff793b81448.png" data-download-href="/uploads/short-url/s3cQfDbaA6Y0fGOprwCvlzqBvNm.png?dl=1" title="stack-call-debug-numpy" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c499ae297cbd46e786e714f434d42ff793b81448.png" alt="stack-call-debug-numpy" data-base62-sha1="s3cQfDbaA6Y0fGOprwCvlzqBvNm" width="500" height="500" data-dominant-color="F1F1F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">stack-call-debug-numpy</span><span class="informations">767×766 39.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>When attached to process, after <code>import numpy</code> I only see that it loaded a few more things before locking up. Note that my “S5R” is actually a debug build.</p>
<pre><code class="lang-auto">'SlicerApp-real.exe' (Win32): Loaded 'C:\S5R\python-install\Lib\lib-dynload\_ctypes.pyd'. Module was built without symbols.
'SlicerApp-real.exe' (Win32): Loaded 'C:\S5R\python-install\Lib\site-packages\numpy\.libs\libopenblas.WCDJNK7YVMPZQ2ME2ZZHJJRJ3JIKNDB7.gfortran-win_amd64.dll'.
</code></pre>

---

## Post #11 by @lassoan (2021-10-10 20:25 UTC)

<p>The call stack after numpy import looks like the application is already shutting down, so does not tell anything about the underlying error.</p>
<p>I’ve started a Windows11 build on an Azure VM. While setting up things, I already experienced a number of regressions in the operating system (some applications, such as Anydesk installer don’t start, download and run from Edge browser breaks after a few downloads, drag-and-drop to the taskbar does not bring the application to the top). Overall, it does not feel like a finished product, which I have not experienced since Windows Vista.</p>

---

## Post #12 by @jamesobutler (2021-10-10 20:47 UTC)

<p>So far I haven’t noticed any issues with how I use Windows. Overall, my first impression is it isn’t much different from my last transition from Windows 7 to Windows 10. Requires some learning of the updated UI, but nothing I don’t already have to do when I update my iPhone to the latest iOS each year. I’m sure the next Windows update this upcoming Tuesday (patch Tuesday) will resolve some issues and other issues will be tuned over the coming months.</p>

---

## Post #13 by @jamesobutler (2021-10-11 16:46 UTC)

<p>A release build generated on Windows 11 with the latest Windows SDK (10.0.22000) and Visual Studio 2022 v143 toolset, packaged successfully and runs successfully on a Windows 10 machine. <code>import numpy</code> is successful. When running on Windows 11 the same <code>import numpy</code> lock up issue is present.</p>

---

## Post #14 by @lassoan (2021-10-11 19:43 UTC)

<p>I’ve built Slicer on Windows11 yesterday with v142 toolset in debug mode and it works well on that Windows11 computer. I’ll test a release-mode build soon.</p>

---

## Post #15 by @lassoan (2021-10-11 20:49 UTC)

<p>Unfortunately, release-mode build hangs at startup, debug-mode build starts normally. This is the worst combination, because it makes debugging harder. I’ve now started a RelWithDebInfo build.</p>

---

## Post #16 by @jamesobutler (2021-10-11 20:55 UTC)

<p>I’m surprised that debug-mode build starts normally for you as it did not start for me for both release and debug on Windows 11.</p>

---

## Post #17 by @Chris_Rorden (2021-10-12 11:48 UTC)

<p>I think it might be worth deferring developmental time into this issue for a few weeks while Microsoft sorts out some of their regressions. Microsoft has noted a number of issues <a href="https://docs.microsoft.com/en-us/windows/release-health/status-windows-11-21h2" rel="noopener nofollow ugc">including non-ASCII characters in registry keys</a>. After seeing this message, I installed Windows 11 and replicated the issues of <a class="mention" href="/u/jamesobutler">@jamesobutler</a>. I was concerned, as my own <a href="https://github.com/rordenlab/MRIcroGL/releases" rel="noopener nofollow ugc">MRIcroGL</a> uses embedded Python. Recently, I have changed the way my software links to the Python dll files. I found that old versions of my software worked, while the most recent release did not. Since my software is much simpler than Slicer3D, I thought this might allow me to track down the issue. However, after Windows updated itself all my software seemed to work. I removed initialization files and reinstalled the latest version of my software and it seems to work out of the box now. My best explanation is that some Windows update resolved my own issue. Based on this anecdotal experience, it might be worth waiting a while until Microsoft gets their shop in order. I actually like the user interface changes, but agree with <a class="mention" href="/u/lassoan">@lassoan</a> that Windows 11 feels unfinished and rushed to market.</p>

---

## Post #18 by @lassoan (2021-10-12 23:42 UTC)

<p>Thanks for the useful additional information <a class="mention" href="/u/chris_rorden">@Chris_Rorden</a>.</p>
<p>I did some more debugging and it turned out that (as expected) that the hang is related to output redirection. An easy workaround is to import numpy once early (before output redirection is set up). See more details in this issue:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/5945">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/5945" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/5945" target="_blank" rel="noopener">Slicer-4.13 hangs at startup on Windows11</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-10-12" data-time="22:30:30" data-timezone="UTC">10:30PM - 12 Oct 21 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          type:bug
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Slicer does not start up (hangs, then the operating system terminates it) on Win<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">dows11

See discussion here:
https://discourse.slicer.org/t/slicer-on-windows-11/20085/11

## Environment
- Slicer version: Slicer 4.13.0-2021-10-08
- Operating system: Windows 11 Pro, Version: 21H2, OS build: 22000.194</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p><a href="https://github.com/Slicer/Slicer/pull/5947">Pull request</a> with the proposed fix is submitted.</p>

---

## Post #19 by @jamesobutler (2021-10-13 13:23 UTC)

<p>Updating Windows 11 from OS Build 22000.194 to 22000.258 with yesterday’s Patch Tuesday release did not fix the Slicer startup issues. It did resolve other unrelated issues with using the OS such as poor performance on VPN.</p>
<p>I can confirm that <a class="mention" href="/u/lassoan">@lassoan</a> 's workaround fix did resolve the issue for me. I confirmed by using the latest Slicer Preview (4.13.0-20211012) built by the factory build machine (It also worked for my local build). Here is a Slicer scripted module that I’m now able to load with Slicer running on Windows 11.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f344b78f30c9d3dafaec874ce19174edbeab577e.jpeg" data-download-href="/uploads/short-url/yI3fymj4hodY9fh4IhAKI2igp78.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f344b78f30c9d3dafaec874ce19174edbeab577e_2_690x388.jpeg" alt="image" data-base62-sha1="yI3fymj4hodY9fh4IhAKI2igp78" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f344b78f30c9d3dafaec874ce19174edbeab577e_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f344b78f30c9d3dafaec874ce19174edbeab577e_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f344b78f30c9d3dafaec874ce19174edbeab577e_2_1380x776.jpeg 2x" data-dominant-color="82838B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 138 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I will continue to provide updates if I find any compatibility issues on Windows 11 with Slicer.</p>

---
