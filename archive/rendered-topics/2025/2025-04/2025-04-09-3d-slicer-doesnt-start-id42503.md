# 3D Slicer doesn't start

**Topic ID**: 42503
**Date**: 2025-04-09
**URL**: https://discourse.slicer.org/t/3d-slicer-doesnt-start/42503

---

## Post #1 by @Daniela_Vicuna (2025-04-09 14:05 UTC)

<p>Hello. I downloaded and installed 3D Slicer, but it doesn’t work. I’ve tried opening it many times, but nothing.<br>
How can I fix this?</p>

---

## Post #2 by @muratmaga (2025-04-09 15:25 UTC)

<p>What is your operating system, and computer specs? And what do you mean specifically by “it doesn’t start”? What folder did you install the slicer? When you double-clcik on it the executable, what happens?</p>

---

## Post #3 by @Daniela_Vicuna (2025-04-09 15:43 UTC)

<p>Problem solved! I unistall the slicer and donwloaded again. To reinstall I exceute like an administrator and then it works.</p>

---

## Post #4 by @muratmaga (2025-04-09 15:48 UTC)

<p>I would not advise installing Slicer with administrator priviledges. If you do it that way, and not RUN slicer with that admin account, you will not be able to install or packages.</p>
<p>And you also shouldn’t need administrator priviledges. Are you on Windows, and trying to install C:/Program Files?</p>
<p>If so try installing it to a place like your Desktop or localapp (which is what Slicer should default to). That way you can install packages and extensions, and everything should be fine.</p>

---

## Post #5 by @cpinter (2025-04-11 11:03 UTC)

<p>What is the Slicer version you installed? There was this issue not long ago, which should be fixed in the latest previews:</p><aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/8229">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/8229" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/8229" target="_blank" rel="noopener">Slicer does not start if installed in folder with special characters</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2025-02-17" data-time="13:23:25" data-timezone="UTC">01:23PM - 17 Feb 25 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/cpinter" target="_blank" rel="noopener">
          <img alt="" src="https://avatars.githubusercontent.com/u/1325980?v=4" class="onebox-avatar-inline" width="20" height="20">
          cpinter
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          Type: Bug
        </span>
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          Priority: High
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Summary

I installed both 5.8.0 and the latest 5.9.0 to the default path, whi<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ch, in my case are
"c:\Users\CsabaPintér\AppData\Local\slicer.org\Slicer 5.8.0"
and
"c:\Users\CsabaPintér\AppData\Local\slicer.org\Slicer 5.9.0-2025-02-14",
respectively.

When I want to start either of these, nothing happens at all. If I copy the installation folder to e.g. `c:\Utils\Slicer 5.9.0-2025-02-14`, it starts alright.

There is nothing in the console either:
```
c:\Users\CsabaPintér\AppData\Local\slicer.org\Slicer 5.9.0-2025-02-14&gt;Slicer.exe

c:\Users\CsabaPintér\AppData\Local\slicer.org\Slicer 5.9.0-2025-02-14&gt;
```

Nothing appears in the Application log either.

## Steps to reproduce

See summary.

## Environment
- Slicer version: See summary
- Operating system: Windows 11</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
