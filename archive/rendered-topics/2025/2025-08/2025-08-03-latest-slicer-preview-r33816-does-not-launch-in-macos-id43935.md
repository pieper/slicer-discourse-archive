# Latest slicer preview (r33816) does not launch in macos

**Topic ID**: 43935
**Date**: 2025-08-03
**URL**: https://discourse.slicer.org/t/latest-slicer-preview-r33816-does-not-launch-in-macos/43935

---

## Post #1 by @muratmaga (2025-08-03 05:13 UTC)

<p>Tested on two different macs (imac and macbook pro) with Sequoia 15.5. After entering the security exception, Slicer icon continues to bounce for about a minute and then quits. When launched from the terminal window from Slicer.app/Contents/MacOS/Slicer, this is the error message:</p>
<pre><code class="lang-auto">% pwd
/Users/murat

% /Users/murat/Desktop/Slicer.app/Contents/MacOS/Slicer
Could not find platform independent libraries 
Could not find platform dependent libraries &lt;exec_prefix&gt;
Python path configuration:
PYTHONHOME = (not set)
PYTHONPATH = (not set)
program name = ‘Slicer’
isolated = 0
environment = 1
user site = 0
safe_path = 0
import site = 1
is in build tree = 0
stdlib dir = ‘/Users/svc-dashboard/D/P/A/python-install/lib/python3.12’
sys.\_base_executable = ‘/Users/murat/Desktop/Slicer.app/Contents/MacOS/Slicer’
sys.base_prefix = ‘/Users/svc-dashboard/D/P/A/python-install’
sys.base_exec_prefix = ‘/Users/svc-dashboard/D/P/A/python-install’
sys.platlibdir = ‘lib’
sys.executable = ‘/Users/murat/Desktop/Slicer.app/Contents/MacOS/Slicer’
sys.prefix = ‘/Users/svc-dashboard/D/P/A/python-install’
sys.exec_prefix = ‘/Users/svc-dashboard/D/P/A/python-install’
sys.path = \[
‘/Users/svc-dashboard/D/P/A/python-install/lib/python312.zip’,
‘/Users/svc-dashboard/D/P/A/python-install’,
‘/Users/svc-dashboard/D/P/A/python-install/lib-dynload’,
‘/Users/svc-dashboard/D/P/A/python-install/plat-darwin’,
‘/Users/svc-dashboard/D/P/A/python-install/lib/python3.12’,
‘/Users/svc-dashboard/D/P/A/python-install/lib/python3.12/lib-dynload’,
‘/Users/svc-dashboard/D/P/A/python-install/lib-tk’,
‘/Users/svc-dashboard/D/P/A/python-install/lib/python3.12’,
‘/Users/svc-dashboard/D/P/A/python-install/lib/python3.12/lib-dynload’,
\]
Fatal Python error: init_fs_encoding: failed to get the Python codec of the filesystem encoding
Python runtime state: core initialized
ModuleNotFoundError: No module named ‘encodings’

Current thread 0x0000000200aaf200 (most recent call first):
</code></pre>

---

## Post #2 by @jamesobutler (2025-08-03 11:21 UTC)

<p>The same <code>ModuleNotFoundError: No module named 'encodings'</code> happens with Slicer 5.8.1 as you reported over in the other thread?</p>
<aside class="quote" data-post="2" data-topic="43847">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/designer-failing-to-launch-on-macos/43847/2">Designer failing to launch on MacOS</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
    </div>
  </div>
  <blockquote>
    Some error pops up with 5.8.1 as well.
  </blockquote>
</aside>


---

## Post #3 by @pieper (2025-08-03 12:34 UTC)

<p>I can replicate the same failure to launch (same error message) with Slicer Preview 2025-08-01 on a macbook air m3.  5.8.1 starts fine, as does the SlicerDesigner app from the Preview.</p>

---

## Post #4 by @muratmaga (2025-08-03 16:09 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="2" data-topic="43935">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p><code>ModuleNotFoundError</code></p>
</blockquote>
</aside>
<p>I think those are separate and i believe that error arose because i didnt launch the correct SlicerDesigner, but the Designer application, which didnt set the correct python environment as you mentioned in that thread.</p>
<p>This is the proper Slicer launcher that generates the error.</p>

---

## Post #5 by @pieper (2025-08-03 16:12 UTC)

<p>On mac there’s no launcher in the distribution, so this is something with the app packaging or startup process itself.</p>

---

## Post #6 by @jamesobutler (2025-08-03 16:39 UTC)

<p>Does a Slicer preview build from May have the same problem specifically on macOS 15.5? Just wondering if related to changes in macOS security impacting the unsigned Slicer preview builds (Slicer 5.8.1 is a signed version) is a cause here or something in recent Slicer commits.</p>

---

## Post #7 by @muratmaga (2025-08-03 18:37 UTC)

<p>No this is new. I have been using preview through out july on the same computer</p>

---

## Post #8 by @muratmaga (2025-08-04 04:47 UTC)

<p>So is this a minor issue that can be fixed fairly quickly or should I open an issue on GH? As of right now, today’s build also not usable.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #9 by @lassoan (2025-08-04 05:03 UTC)

<p>Failure to launch is a serious issue, so submitting an issue on github makes sense; and then this discussion should continue there.  Peobably <a class="mention" href="/u/jcfr">@jcfr</a> knows most about potential root causes and fixes, but maybe you can help the investigation if you determine which is the first date where the Slicer Preview Release started to fail (you can use the offset option on thr download page to get previous releases, for example <a href="http://download.slicer.org/?offset=-7" class="inline-onebox">Download 3D Slicer | 3D Slicer</a>).</p>

---

## Post #10 by @muratmaga (2025-08-04 05:26 UTC)

<p>Will do but there is something weird with the offset parameters. This is what I get when i put in <strong>?offset=-3</strong></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d2e3c6b5259ab9d9ff257c1188839c3b88e66fd0.png" data-download-href="/uploads/short-url/u5Chb05t7HnHXo38VjuziASQYaQ.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d2e3c6b5259ab9d9ff257c1188839c3b88e66fd0_2_690x353.png" alt="image" data-base62-sha1="u5Chb05t7HnHXo38VjuziASQYaQ" width="690" height="353" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d2e3c6b5259ab9d9ff257c1188839c3b88e66fd0_2_690x353.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d2e3c6b5259ab9d9ff257c1188839c3b88e66fd0.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d2e3c6b5259ab9d9ff257c1188839c3b88e66fd0.png 2x" data-dominant-color="F5F7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1022×524 46.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Not sure why it is showing random stable versions, which are clearly dated wrong. Also when I click the 5.9.0 from July 30, the downloaded package shows as <strong>Slicer-5.9.0-2025-07-25-macosx-amd64.dmg</strong></p>
<p>because it doesn’t launch, I can’t confirm whether it is indeed the revision 33809 or a different revision number.</p>

---

## Post #11 by @muratmaga (2025-08-04 05:47 UTC)

<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/8618">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/8618" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/8618" target="_blank" rel="noopener">Slicer preview does not launch in MacOS.</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2025-08-04" data-time="05:46:53" data-timezone="UTC">05:46AM - 04 Aug 25 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/muratmaga" target="_blank" rel="noopener">
          <img alt="" src="https://avatars.githubusercontent.com/u/21285140?v=4" class="onebox-avatar-inline" width="20" height="20">
          muratmaga
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Summary
As I reported on the forum https://discourse.slicer.org/t/latest-slic<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">er-preview-r33816-does-not-launch-in-macos/43935/10
When the preview dmg package is opened and launched (and after entering the security exception), the icon bounces for a while and then abruptly gets killed. When launched from the terminal window, this is the output:

```
MLSSC40183:~ amaga$ /Users/amaga/Desktop/Slicer.app/Contents/MacOS/Slicer
Could not find platform independent libraries &lt;prefix&gt;
Could not find platform dependent libraries &lt;exec_prefix&gt;
Python path configuration:
  PYTHONHOME = (not set)
  PYTHONPATH = (not set)
  program name = 'python3'
  isolated = 0
  environment = 1
  user site = 0
  safe_path = 0
  import site = 1
  is in build tree = 0
  stdlib dir = '/Users/svc-dashboard/D/P/A/python-install/lib/python3.12'
  sys._base_executable = '/Users/amaga/Desktop/Slicer.app/Contents/MacOS/Slicer'
  sys.base_prefix = '/Users/svc-dashboard/D/P/A/python-install'
  sys.base_exec_prefix = '/Users/svc-dashboard/D/P/A/python-install'
  sys.platlibdir = 'lib'
  sys.executable = '/Users/amaga/Desktop/Slicer.app/Contents/MacOS/Slicer'
  sys.prefix = '/Users/svc-dashboard/D/P/A/python-install'
  sys.exec_prefix = '/Users/svc-dashboard/D/P/A/python-install'
  sys.path = [
    '/Users/svc-dashboard/D/P/A/python-install/lib/python312.zip',
    '/Users/svc-dashboard/D/P/A/python-install',
    '/Users/svc-dashboard/D/P/A/python-install/lib-dynload',
    '/Users/svc-dashboard/D/P/A/python-install/plat-darwin',
    '/Users/svc-dashboard/D/P/A/python-install/lib/python3.12',
    '/Users/svc-dashboard/D/P/A/python-install/lib/python3.12/lib-dynload',
    '/Users/svc-dashboard/D/P/A/python-install/lib-tk',
    '/Users/svc-dashboard/D/P/A/python-install/lib/python3.12',
    '/Users/svc-dashboard/D/P/A/python-install/lib/python3.12/lib-dynload',
  ]
Fatal Python error: init_fs_encoding: failed to get the Python codec of the filesystem encoding
Python runtime state: core initialized
ModuleNotFoundError: No module named 'encodings'
```
The last known version that works for me is 5.9.0-2025-07-12 r33764 / d6c7975
 For me all packages downloaded after that date, shows the same error. 

@jcfr</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The last version that I can download and get it to work on my mac is:</p>
<p>5.9.0-2025-07-12 r33764 / <a href="https://github.com/Slicer/Slicer/commit/d6c79751ed3e79693d76550d6ce5fb245258a878">d6c7975</a></p>

---

## Post #12 by @jcfr (2025-08-06 14:43 UTC)

<p>To follow-up on this, the root cause has been identified.</p>
<p>Waiting it is addressed, consider running Slicer using the following helper script: <a href="https://gist.github.com/jcfr/4eca5ab7d5d0da9706ad4099a07c6949">slicer-macos-launch.sh</a></p>
<hr>
<p>Download the script:</p>
<pre data-code-wrap="bash"><code class="lang-bash">curl -LO https://gist.githubusercontent.com/jcfr/4eca5ab7d5d0da9706ad4099a07c6949/raw/slicer-macos-launch.sh
chmod u+x slicer-macos-launch.sh
</code></pre>
<p>Run Slicer:</p>
<pre data-code-wrap="bash"><code class="lang-bash">slicer-macos-launch.sh /path/to/Slicer.app
</code></pre>

---

## Post #13 by @jcfr (2025-08-08 18:04 UTC)

<p>Et voila. Corresponding fix has just been integrated <img src="https://emoji.discourse-cdn.com/twitter/rocket.png?v=14" title=":rocket:" class="emoji" alt=":rocket:" loading="lazy" width="20" height="20"></p>
<p>Thanks <a class="mention" href="/u/pieper">@pieper</a> for the review <img src="https://emoji.discourse-cdn.com/twitter/folded_hands.png?v=14" title=":folded_hands:" class="emoji" alt=":folded_hands:" loading="lazy" width="20" height="20"></p>
<p>And if you curious about the details …</p>
<hr>
<p><a href="https://github.com/Slicer/Slicer/pull/8632">PR-8632</a> introduces <code>initializeEnvironmentFromLauncher()</code> and ensures it runs before argument parsing and Python interpreter initialization. The method reads launcher <code>.ini</code> settings, discovers Slicer home, and sets environment variables required by early subsystems (e.g Python).</p>
<p>In the context of macOS installer where no launcher is used (only launcher settings file is provided along side the “real” executable), the previous init order could start Python with a partial environment, causing early import failures.</p>
<p>Follow-up to <a href="https://github.com/Slicer/Slicer/commit/fa915a03fc472618fdaa65a3815ebfdec2f92429">Slicer@fa915a03fc</a> (“BUG: Fix improper Python initialization causing inconsistent interpreter state”) introduced through <a href="https://github.com/Slicer/Slicer/pull/8582">PR-8582</a>.</p>

---

## Post #14 by @muratmaga (2025-08-09 20:28 UTC)

<p>Confirmed it is working. Thanks everyone who helped fix it.</p>

---
