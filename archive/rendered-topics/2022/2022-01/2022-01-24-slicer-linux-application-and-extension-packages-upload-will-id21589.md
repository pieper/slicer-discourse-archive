# Slicer Linux application and extension packages upload will be restored Jan 24th 2022

**Topic ID**: 21589
**Date**: 2022-01-24
**URL**: https://discourse.slicer.org/t/slicer-linux-application-and-extension-packages-upload-will-be-restored-jan-24th-2022/21589

---

## Post #1 by @jcfr (2022-01-24 03:42 UTC)

<p>To summarize, preview Linux build for Slicer application and associated extensions will not be available until we address this (*)</p>
<p>In the meantime, thanks for your patience <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=15" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"></p>
<p>(*) <em>Note that we will also add regression tests to the relevant continuous integration to avoid this specific issue from happening again</em></p>
<h2><a name="p-72795-background-1" class="anchor" href="#p-72795-background-1" aria-label="Heading link"></a>Background</h2>
<p>While working on updating CMake and compilers (See [1]) used on the different “factories” (aka build machine responsible to build application and extension packages), we also updated the docker images used generate the Linux packages (See [2]).</p>
<p>To be specific, we first updated the <a href="https://github.com/dockbuild/dockbuild">dockbuild/dockbuild</a> and then updated the <code>slicer/buildenv-qt5-centos7:latest</code> image specific to Slicer and maintained at <a href="https://github.com/Slicer/SlicerBuildEnvironment">Slicer/SlicerBuildEnvironment</a>.</p>
<p>The problem is that simply bumping the python version used in the script <a href="https://github.com/dockbuild/dockbuild/blob/master/imagefiles/build-and-install-python.sh">imagefiles/build-and-install-python.sh</a> was not sufficient and the python version installed in the image is lacking modules like <code>_ctypes</code> that are required to use the <a href="https://github.com/girder/slicer_package_manager#readme">slicer_package_manager</a> python client.</p>
<p>[1] <a href="https://github.com/Slicer/DashboardScripts/pull/43">https://github.com/Slicer/DashboardScripts/pull/43</a><br>
[2] <a href="https://github.com/dockbuild/dockbuild/pull/78">https://github.com/dockbuild/dockbuild/pull/78</a></p>

---

## Post #2 by @jcfr (2022-01-25 02:13 UTC)

<p>Update:</p>
<p>Root cause has been fixed in the following pull request:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/dockbuild/dockbuild/pull/79">
  <header class="source">

      <a href="https://github.com/dockbuild/dockbuild/pull/79" target="_blank" rel="noopener">github.com/dockbuild/dockbuild</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/dockbuild/dockbuild/pull/79" target="_blank" rel="noopener">Fix python build ensuring ctypes/lzma/readline/sqlite3 deps are available</a>
    </h4>

    <div class="branches">
      <code>dockbuild:master</code> ← <code>dockbuild:install-python-dependencies</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-01-25" data-time="01:25:38" data-timezone="UTC">01:25AM - 25 Jan 22 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/jcfr" target="_blank" rel="noopener">
          <img alt="jcfr" src="https://avatars.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
          jcfr
        </a>
      </div>

      <div class="lines" title="2 commits changed 6 files with 43 additions and 4 deletions">
        <a href="https://github.com/dockbuild/dockbuild/pull/79/files" target="_blank" rel="noopener">
          <span class="added">+43</span>
          <span class="removed">-4</span>
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

<p>Relevant Slicer docker image is being rebuilt.</p>

---

## Post #3 by @jcfr (2022-01-25 03:25 UTC)

<p>Issue has been addressed:</p>
<ul>
<li>Image <code>slicer/buildenv-qt5-centos7:latest</code> has been updated</li>
<li>Update from the linux “factory” has been manually triggered</li>
<li>Download site now show the linux package is available for download (see screenshot below)</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f5a265b64270b064f7114b164cbc55b7d6988f7b.png" data-download-href="/uploads/short-url/z2YUIRzfbLESUy6AhA8RlZtfXxp.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f5a265b64270b064f7114b164cbc55b7d6988f7b.png" alt="image" data-base62-sha1="z2YUIRzfbLESUy6AhA8RlZtfXxp" width="690" height="84" data-dominant-color="FEF9EE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">886×109 6.71 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
