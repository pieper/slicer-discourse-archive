# OSX Slicer Qt5 packaging error

**Topic ID**: 1468
**Date**: 2017-11-16
**URL**: https://discourse.slicer.org/t/osx-slicer-qt5-packaging-error/1468

---

## Post #1 by @danielbr (2017-11-16 15:28 UTC)

<p>Having trouble packaging a slicer build on my mac OSX high sierra machine.  I installed Qt 5.9.2 using the prebuilt binary installed using the Qt open-source download from the Qt website.  I successfully built the latest commit of slicer and slicer works great.  Now I want to package this build into a dmg install file, but I am having some trouble.  The build target steps work fine.  Then when it goes to the cpack steps it starts to complain repeatedly about finding Qt using the rpath.  Here is an example output:</p>
<p>warning: target ‘<span class="mention">@rpath</span>/Frameworks/QtCore.framework/Versions/5/QtCore’ is not absolute<br>
warning: target ‘’<span class="mention">@rpath</span>/Frameworks/QtCore.framework/Versions/5/QtCore’ does not exist<br>
’<span class="mention">@rpath</span>/Frameworks/QtCore.framework/Versions/5/QtCore’: No such file or directory</p>
<p>Since these are just warnings cpack continues, but then at the end the pack fails and says error converting to UDCO dmg for adding SLA.  hdiutil: convert failed - Resource temporarily unavailable.  Anyone else experience these issues and know how to remedy it?</p>

---

## Post #2 by @ihnorton (2017-11-16 16:02 UTC)

<p>Regarding the hdiutil error, you may have incorrectly unmounted the disk image during a previous run. Just google the message, see e.g.</p>
<aside class="onebox stackexchange">
  <header class="source">
      <a href="https://apple.stackexchange.com/questions/82214/hdiutil-convert-rsize-resource-temporarily-unavailable" target="_blank">apple.stackexchange.com</a>
  </header>
  <article class="onebox-body">
      <a href="https://apple.stackexchange.com/users/42951/reto" target="_blank">
    <img alt="reto" src="https://www.gravatar.com/avatar/bef8bd348b2e41def0bf92ba340c9326?s=128&amp;d=identicon&amp;r=PG" class="thumbnail onebox-avatar" width="128" height="128">
  </a>
<h4>
  <a href="https://apple.stackexchange.com/questions/82214/hdiutil-convert-rsize-resource-temporarily-unavailable" target="_blank">hdiutil convert/rsize resource temporarily unavailable</a>
</h4>

<div class="tags">
  <strong>dmg, disk-utility</strong>
</div>

<div class="date">
  asked by
  
  <a href="https://apple.stackexchange.com/users/42951/reto" target="_blank">
    reto
  </a>
  on <a href="https://apple.stackexchange.com/questions/82214/hdiutil-convert-rsize-resource-temporarily-unavailable" target="_blank">10:47AM - 15 Feb 13 UTC</a>
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>As far as the RPATH warnings, if they do cause the packaged application to fail to start, the quick fix is to manually add the appropriate RPATH to the slicer binary using otool or <code>install_name_tool</code>. For a general fix you’ll need to read up on RPATHs and how to tell CMake and CPack to set and use RPATH in the Slicer binary. Grep for <code>fixup</code> to see the existing logic.</p>

---

## Post #3 by @danielbr (2017-11-16 18:34 UTC)

<p>Thanks for the advice.  I tried the suggestions for hdiutil and I still can’t get it to run.  I manually attached the temp.dmg file then detached it and reran the hdiutil convert command and it still says resource temporarily unavailable.  Plus, if I rerun make package then it will clear out the temp.dmg and remake it.  So I still can’t get it to package…</p>

---

## Post #4 by @ihnorton (2017-11-17 16:12 UTC)

<p>Well, if you post the full build log maybe someone will see an issue (<a href="http://gist.github.com">gist.github.com</a>, pastebin, etc.). Generally speaking, Qt5 is still an experimental configuration, so probably some aspects of packaging remain to be addressed.</p>

---

## Post #5 by @danielbr (2017-11-18 20:02 UTC)

<p>Some pointers for others that are having these same issues.  You must install Qt using homebrew because that build has the rpath turned off.  Using that build gets rid of all of the complaints about the rpath.  Then came the complaints about finding libqcocoa.  I manually resolved this by copying it from qt/5.9.2/plugins/platforms/libqcocoa.dylib to Slicer-build/_CPack_Packages/macosx-amd64/DragNDrop/Slicer-4.9.0-2017-11-16-macosx-amd64/Slicer.app/Contents/lib/Slicer-4.9/ after that folder is created during packaging.</p>
<p>That solved those problems.  Now onto the hdiutil error.  When cpack runs the command to convert temp.dmg to UDZO format creating the filename temp-udzo.dmg hdiutil fails everytime saying Resource temporarily unavailable.  I have tried attaching the temp.dmg and then detaching it but it doesn’t remedy the problem.  What works is if I rename temp.dmg to temp2.dmg and then copy temp2.dmg to temp.dmg and then run the hdiutil convert it works perfectly.</p>
<p>The problem I have is I do not know what the next steps are after that.  If I rerun make package then it just starts over from the beginning clearing out the _CPack_Packages.  Where do I find what the next steps are for packaging so I can manually perform them?</p>

---

## Post #6 by @ihnorton (2017-12-09 13:24 UTC)

<aside class="quote no-group" data-username="danielbr" data-post="5" data-topic="1468">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/c2a13f/48.png" class="avatar"> danielbr:</div>
<blockquote>
<p>You must install Qt using homebrew because that build has the rpath turned off.  Using that build gets rid of all of the complaints about the rpath.</p>
</blockquote>
</aside>
<p>Not sure if you got further along here, but I ran in to some issues while packaging Homebrew (qt4) and have submitted a few fixes:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/856">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/856" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/856" target="_blank" rel="noopener">Re: issue 283 - crash at end of EMSegment</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-03-12" data-time="22:33:17" data-timezone="UTC">10:33PM - 12 Mar 20 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2020-03-12" data-time="22:33:18" data-timezone="UTC">10:33PM - 12 Mar 20 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/slicerbot" target="_blank" rel="noopener">
          <img alt="slicerbot" src="https://avatars.githubusercontent.com/u/10277015?v=4" class="onebox-avatar-inline" width="20" height="20">
          slicerbot
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">_This issue was created automatically from an original [Mantis Issue](https://ma<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ntisarchive.slicer.org/view.php?id=856). Further discussion may take place here._</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/857">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/857" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/857" target="_blank" rel="noopener">After loading a scene, volumes won't appear/scroll</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-03-12" data-time="22:33:18" data-timezone="UTC">10:33PM - 12 Mar 20 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2020-03-12" data-time="22:33:19" data-timezone="UTC">10:33PM - 12 Mar 20 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/slicerbot" target="_blank" rel="noopener">
          <img alt="slicerbot" src="https://avatars.githubusercontent.com/u/10277015?v=4" class="onebox-avatar-inline" width="20" height="20">
          slicerbot
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">_This issue was created automatically from an original [Mantis Issue](https://ma<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ntisarchive.slicer.org/view.php?id=857). Further discussion may take place here._</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #7 by @ihnorton (2018-01-19 16:33 UTC)

<p>Just to follow up here – after these fixes I got a package built, but the resulting Slicer would not start on another computer because of missing dependencies. Later I found some comments in the homebrew github saying they very explicitly do not support this separate re-packaging use-case (they do support linking Qt as a dependency when building/distributing an app via homebrew, of course). IIRC one issue is they don’t build with RPATH at all, and there was also an issue with the version of SSL they link against. I think both issues were not <em>technically</em> infeasible to overcome, but don’t seem worth the time to fix compared to just building Qt from scratch.</p>

---
