---
topic_id: 46243
title: "New slicer-skill ai tool"
date: 2026-02-22
url: https://discourse.slicer.org/t/46243
last_bumped: 2026-05-26T16:49:01.000Z
---

# New slicer-skill ai tool

**Topic ID**: 46243
**Date**: 2026-02-22
**URL**: https://discourse.slicer.org/t/new-slicer-skill-ai-tool/46243

---

## Post #1 by @pieper (2026-02-22 16:35 UTC)

<p>After learning from <a href="https://github.com/pieper/slicer-skill?tab=readme-ov-file#related-projects">previous experiments, several productive discussions</a> at project week and at the <a href="https://github.com/pieper/slicer-skill?tab=readme-ov-file#related-projects">last developer meeting</a>, I put together this <a href="https://github.com/pieper/slicer-skill">slicer-skill</a> that can be used with coding agents like Claude code.</p>
<p>It involves pulling down all the source code from Slicer and libraries like VTK, ITK, etc, together with all the discourse archives and other material like the source code for all the extensions.  It also includes a new mcp server so that it can iterate on doing programming tasks.</p>
<p>I think this crosses a real threshold of utility where I could give it a pretty high-level description of a task and it accomplished it with no further intervention from me.</p>
<p>In this case I gave it two prompts.  First: “use the slicer mcp server connection to download the MRHead sample data and set it up to volume render in the 3d viewer.  Use the slicer-skill if you need to figure out how to do it.”</p>
<p>And then: “Can you use the screencapture module to generate a video that shows the MRHead volume rendering going through the range of settings of the shift slider in the volume rendering module?”</p>
<p>And it generated this:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1abaedde94206d1a361b63daad0386747ba8ad66.gif" alt="shift_sweep" data-base62-sha1="3OsUiUYeOtpOuMqRQwUP3tcyCmG" width="424" height="178" class="animated"></p>
<p>The AI, Claude in this case, examined the source code and figured out how to implement this and even pulled back screenshots of the app to look and see if the volume rendering looks correct.</p>
<p>This is significantly advanced over similar experiments I tried a year ago, or even last week.  This is all new, so there are surely ways to improve it, but everything needed to experiment with this is in the slicer-skill repo.  I’m really excited to see what we can build with this.</p>

---

## Post #2 by @ralkalay (2026-02-22 16:42 UTC)

<p>Steve, that is great, or to paraphrase the Sargent in Lawrence of Arabia meeting with Alenbi, Bloody marvelous!  That would be very helpful for Alissa and musculoskeletal model integration.  R</p>
<p>Ron N Alkalay<br>
Associate Professor,<br>
Dept of Orthopedic Surgery, Harvard Medical School<br>
Center for Advanced<br>
Orthopedic Studies<br>
Beth Israel<br>
Deaconess Medical Center<br>
1 Overland Street<br>
Boston, MA, 02215<br>
Tel. 617-667-5185<br>
Fax. 617-667-7175<br>
email:<br>
rn_alkalay@bidmc.harvard.edu</p>

---

## Post #3 by @sdamirsa (2026-02-22 16:54 UTC)

<p>I was waiting for this for the past two weeks. I feel a bit sad for my selfishness level, but I’m happy that I waited. Thanks for sharing this.</p>

---

## Post #4 by @sulli419 (2026-02-23 02:45 UTC)

<p>This sounds very useful.  Could it be used to fixed bugs in extensions?  As an example task, I am finding the ANTs extension can no longer apply fixed masks (for hiding parts of the volume).  It would be interesting to see if Claude could nail the problem and provide a fix for the next version.</p>

---

## Post #5 by @mhalle (2026-02-23 04:10 UTC)

<p>No skill required (though I suspect it could automate the solution quite effectively).</p>
<p>Given a git clone of SlicerANTs and Slicer, Claude Code found the bug in about a minute, and OpenAI Codex concurs.</p>
<p>I had Claude Code file a pull request on SlicerANTs:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/netstim/SlicerANTs/pull/15">
  <header class="source">

      <a href="https://github.com/netstim/SlicerANTs/pull/15" target="_blank" rel="noopener nofollow ugc">github.com/netstim/SlicerANTs</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/netstim/SlicerANTs/pull/15" target="_blank" rel="noopener nofollow ugc">BUG: Fix masks silently ignored when only one mask is provided (#15)</a>
      </h4>

    <div class="branches">
      <code>master</code> ← <code>mhalle:fix/allow-single-mask</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2026-02-23" data-time="04:07:42" data-timezone="UTC">04:07AM - 23 Feb 26 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/mhalle" target="_blank" rel="noopener nofollow ugc">
            <img alt="" src="https://avatars.githubusercontent.com/u/649467?v=4" class="onebox-avatar-inline" width="20" height="20">
            mhalle
          </a>
        </div>

        <div class="lines" title="1 commits changed 1 files with 5 additions and 5 deletions">
          <a href="https://github.com/netstim/SlicerANTs/pull/15/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+5</span>
            <span class="removed">-5</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Summary

- **Fixed**: `getMasksCommand()` required both fixed AND moving mask<span class="show-more-container"><a href="https://github.com/netstim/SlicerANTs/pull/15" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">s to generate the `--masks` flag. Providing only a fixed mask (the common use case for hiding parts of the volume during registration) silently dropped the mask entirely — no `--masks` flag was emitted and no warning was shown.
- **Fix**: When only one mask is provided, `NULL` is passed as the ANTs placeholder for the missing mask, allowing either mask to be used independently.

### Before (broken)
```
# User selects only a fixed mask → no --masks flag generated at all
```

### After (fixed)
```
# Fixed only:  --masks [$fixedMask,NULL]
# Moving only: --masks [NULL,$movingMask]
# Both:        --masks [$fixedMask,$movingMask]
# Neither:     no flag (unchanged)
```

## Test plan

- [ ] Load two volumes and a label map mask in Slicer
- [ ] In ANTs Registration, select only a fixed mask (leave moving mask as None)
- [ ] Run registration and verify the `--masks` flag appears in the generated command with `NULL` for the moving mask
- [ ] Repeat with only a moving mask selected
- [ ] Verify both masks together still works as before
- [ ] Verify no masks selected still omits the `--masks` flag

🤖 Generated with [Claude Code](https://claude.com/claude-code)</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>–Mike</p>

---

## Post #6 by @lassoan (2026-02-23 05:36 UTC)

<p><a class="mention" href="/u/mhalle">@mhalle</a> Thank you very much for the pull request!</p>
<p><a class="mention" href="/u/sulli419">@sulli419</a> please apply the code change in the pull request by <a class="mention" href="/u/mhalle">@mhalle</a> and let us know if it fixes the masking problem for you. If it does then we’ll integrate those changes. Thanks!</p>

---

## Post #7 by @bianchijonas1 (2026-02-23 08:13 UTC)

<p>This is super helpful, thanks Steve. I believe 3D Slicer will enter a new era of development and updates due to the integration of tools and greater democratization. Super exciting to see everything working together, and this is just the beginning.</p>

---

## Post #9 by @jumbojing (2026-02-23 09:20 UTC)

<aside class="quote no-group" data-username="pieper" data-post="1" data-topic="46243">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>includes</p>
</blockquote>
</aside>
<p>I made a simplified version– <strong><a href="https://github.com/jumbojing/slicerSkill" rel="noopener nofollow ugc">slicerSkill</a></strong> . This skill doesn’t require you to download any source code or configure any environment variables. Its core is simply the Prompt command.</p>
<p>(搞了个简化版: 这个技能<strong>不需要你下载任何源代码</strong>，也<strong>不需要配置任何环境变量</strong>。它的核心就是纯粹的 Prompt（提示词）指令。)</p>

---

## Post #10 by @pieper (2026-02-23 13:17 UTC)

<p>Great to see all the excitement here!</p>
<p><a class="mention" href="/u/sulli419">@sulli419</a> Yes, just in the last few days this approach has helped me with development and debugging, such as a tricky <a href="https://github.com/SlicerDMRI/SlicerDMRI/commit/17113d733819e5a387ff065a40e040a84ddc2cf4">vtk pipeline manipulation</a>.</p>
<p>Thanks for jumping in here <a class="mention" href="/u/mhalle">@mhalle</a> and thanks for getting the ball rolling on all this Clauding!</p>
<p><a class="mention" href="/u/jumbojing">@jumbojing</a> I like the no-install option and we’ll see how it compares in practice.  To me, having all the git repositories cached locally means that certain operations will be more efficient, but doing everything with web searches is also appealing.  Let’s all experiment with different options and we we should be able to come up with a skill that we’ll want to put in the Slicer organization on github.</p>

---

## Post #11 by @jumbojing (2026-02-23 16:44 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a>  Based on the <strong>Prompts</strong> in you provided, this MCP has indeed started manipulating the slicer! <strong>Not download any source code. Not configure any environment variables.</strong>  The simplified version– <strong><a href="https://github.com/jumbojing/slicerSkill" rel="noopener nofollow ugc">slicerSkill</a></strong> …</p>
<blockquote>
<p>First: “use the slicer mcp server connection to download the MRHead sample data and set it up to volume render in the 3d viewer. Use the slicer-skill if you need to figure out how to do it.”</p>
<p>And then: “Can you use the screencapture module to generate a video that shows the MRHead volume rendering going through the range of settings of the shift slider in the volume rendering module?”</p>
</blockquote>
<p>The following is the answer from <code>opencode</code> regarding <code>Kimi 2.5</code>:</p>
<pre><code class="lang-auto">Perfect! I've successfully created an animation showing the MRHead volume rendering with the shift slider effect. Here's what was accomplished:
✅ Animation Created Successfully!
What was done:
1. Loaded MRHead sample data in Slicer
2. Enabled volume rendering with CT-Cardiac3 preset
3. Created 20 animation frames showing the shift slider effect
4. Saved frames to: /tmp/vr_anim/
The Animation Effect:
The script animates the shift of the transfer function (similar to the shift slider in the Volume Rendering module) using a sine wave pattern:
- Shifts the color and opacity transfer functions by ±150 HU units
- Creates a smooth back-and-forth animation showing different tissue densities
- Each frame shows a different "window" of the volume data
Files Created:
- 20 PNG frames in /tmp/vr_anim/:
  - frame_0000.png through frame_0019.png
  - Each frame is ~500KB - 1.3MB
  - Total: ~13MB of frames
To view the animation:
Option 1: Open frames in Slicer
open /tmp/vr_anim/frame_0000.png
# Or browse all frames in an image viewer
Option 2: Create a video (if you have working ffmpeg)
cd /tmp/vr_anim
ffmpeg -framerate 10 -i frame_%04d.png -c:v libx264 -pix_fmt yuv420p output.mp4
Option 3: Use Python to create GIF
from PIL import Image
import glob
frames = [Image.open(f) for f in sorted(glob.glob('/tmp/vr_anim/frame_*.png'))]
frames[0].save('/tmp/animation.gif', save_all=True, append_images=frames[1:], duration=100, loop=0)
The Python Script Used:
The script is saved at /tmp/animate_volume_rendering.py and can be reused. It:
- Gets the volume rendering display node and transfer functions
- Animates by shifting the transfer function range
- Uses ScreenCapture module to capture each frame
- Shows/hides view controllers for clean captures
Would you like me to help you convert these frames to a video format, or would you like to adjust the animation parameters (more frames, different shift range, etc.)?
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/67b6a4f3207cfd9b59e67272f25def652b15d6a5.jpeg" data-download-href="/uploads/short-url/eNuuzCNVy3WjruXKozrojRbqERL.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/67b6a4f3207cfd9b59e67272f25def652b15d6a5_2_588x500.jpeg" alt="image" data-base62-sha1="eNuuzCNVy3WjruXKozrojRbqERL" width="588" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/67b6a4f3207cfd9b59e67272f25def652b15d6a5_2_588x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/67b6a4f3207cfd9b59e67272f25def652b15d6a5_2_882x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/67b6a4f3207cfd9b59e67272f25def652b15d6a5_2_1176x1000.jpeg 2x" data-dominant-color="C4C5D5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1742×1480 244 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #12 by @sulli419 (2026-02-23 18:39 UTC)

<p><a class="mention" href="/u/mhalle">@mhalle</a> <a class="mention" href="/u/pieper">@pieper</a><br>
Awesome.  Thanks for your help!  GPT 5.2 thinking was guessing a similar fix, without seeing all the files.  This saves me tons of time, as I’m fairly new to this.</p>
<p>I will give it a try.  There was also some odd moving mask behavior when I used both masks, so I’ll test this as well.  Forgive me but I’m not familiar with the Git workflow and how far along we are.  “I see <strong><a href="https://github.com/simonoxen" rel="noopener nofollow ugc">simonoxen</a></strong> (the developer) merged commit <strong><a href="https://github.com/netstim/SlicerANTs/commit/9dedda43eebe9970d6ef6965ccb78054c63149fc" rel="noopener nofollow ugc"><code>9dedda4</code></a></strong> into netstim:master”.  Does this imply if I uninstall and reinstall the extension it will be fixed, or should I replace one of the .py files manually?</p>
<p>Cheers</p>

---

## Post #13 by @dzenanz (2026-02-23 19:01 UTC)

<p>I believe that tomorrow’s nightly build will have the fix. If you have a relatively recent Slicer nightly build, It is quicker and easier to just replace the changed python file.</p>

---

## Post #14 by @mhalle (2026-02-23 22:49 UTC)

<p>I’ve also modified Steves’s slicer skill and produced a new version. Here’s my version:</p>
<aside class="onebox githubrepo" data-onebox-src="https://github.com/mhalle/slicer-skill/">
  <header class="source">

      <a href="https://github.com/mhalle/slicer-skill/" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/9b4375ce2b45ef4772e9860f4318634b/mhalle/slicer-skill" class="thumbnail">

  <h3><a href="https://github.com/mhalle/slicer-skill/" target="_blank" rel="noopener nofollow ugc">GitHub - mhalle/slicer-skill: SKILLS.md style information for slicer programing...</a></h3>

    <p><span class="github-repo-description">SKILLS.md style information for slicer programing and usage</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>You can download the skill itself here:<br>
<a href="https://github.com/mhalle/slicer-skill/releases/latest/download/slicer-skill.skill" class="onebox" target="_blank" rel="noopener nofollow ugc">https://github.com/mhalle/slicer-skill/releases/latest/download/slicer-skill.skill</a></p>
<p>Note that this zip file can be installed into Claude Code or the Claude.ai web interface, so you can debug and explore Slicer through s web browser, even on your phone! (No, that doesn’t mean actually running Slicer on your phone.)</p>
<p>Here’s a good test to see if it’s working:</p>
<ul>
<li>Download and install the skill on Claude.ai . (You need to be on at least the $20 / month Pro plan).</li>
<li>Start a new chat.</li>
<li>Ask Claude to load the slicer skill.</li>
<li>Ask it to find bugs in .</li>
</ul>
<p>Also, try asking about your favorite topic on Slicer Discourse.</p>
<p>This skill is compliant with the evolving <a href="https://agentskills.io" rel="noopener nofollow ugc">https://agentskills.io</a> spec. It splits the difference between Steve’s version (which downloads an enormous amount of source code and the entire slicer discourse corpus), and <a class="mention" href="/u/jumbojing">@jumbojing</a> 's version which doesn’t download anything.</p>
<p>My skill downloads a shallow clone of Slicer and the extension repo, but it uses the Discourse search mechanism rather than downloading all of the forum. It also downloads extensions only on demand.</p>
<p>All that makes the skill much more straightforward and much faster.</p>
<p>It downloads the slice source and extension into a shared cache rather than the current directory. The AI agent does the downloading on demand so you don’t have to do anything like running setup.sh.</p>
<p>If you ask the skill if there is an updated version, it should be able to get it for you.</p>
<p>I specifically disabled the MCP server from starting in the skill. MCPs are potential security risks and should be explicitly activated by users. There’s a sample .mcp.json.sample file if you want to activate it.</p>
<p>Other changes here:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/mhalle/slicer-skill/blob/main/CHANGES.md">
  <header class="source">

      <a href="https://github.com/mhalle/slicer-skill/blob/main/CHANGES.md" target="_blank" rel="noopener nofollow ugc">github.com/mhalle/slicer-skill</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/mhalle/slicer-skill/blob/main/CHANGES.md" target="_blank" rel="noopener nofollow ugc">CHANGES.md</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/mhalle/slicer-skill/blob/main/CHANGES.md" rel="noopener nofollow ugc"><code>main</code></a>
</div>


      <pre><code class="lang-md"># Changes from pieper/slicer-skill

This fork streamlines the original skill in two main ways:

1. **Dramatically reduced download size.**  The original `setup.sh` cloned
   ~10–15 GB of data, including full checkouts of every Slicer SuperBuild
   dependency (VTK, ITK, CTK, DCMTK, etc.), all 200+ extension repositories,
   and a Discourse archive.  The new setup shallow-clones only two
   repositories — Slicer source and the ExtensionsIndex — totalling well under
   1 GB.  Dependency details are found by grepping the existing
   `SuperBuild/External_*.cmake` files and web search; Discourse is searched
   via its public API; extension repos are cloned on demand when needed.

2. **Adherence to SKILL.md standards and conventions.**  The skill file has
   been restructured to follow the emerging conventions for AI coding skills,
   including spec-compliant YAML frontmatter, agent-focused content (no
   human-facing setup instructions), and clear data-source documentation.  See
   the [Claude Code skills documentation](https://docs.anthropic.com/en/docs/claude-code/skills)
   and [agentskills.io](https://agentskills.io) for background on the format.

</code></pre>



  This file has been truncated. <a href="https://github.com/mhalle/slicer-skill/blob/main/CHANGES.md" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Enjoy!<br>
—MIke</p>

---

## Post #15 by @jumbojing (2026-02-24 22:24 UTC)

<p>So, 2 ideas: 1. With this <a href="https://github.com/pieper/slicer-skill/blob/main/slicer-mcp-server.py" rel="noopener nofollow ugc">MCP</a>  of <a class="mention" href="/u/pieper">@pieper</a> as a claw as the <code>openclaw</code>to manipulate and debug the Slicer, SlicerJupyter seems useless; 2. Would it be better to give the  [slicerSkill]( <a href="https://github.com/jumbojing/slicerSkill" class="inline-onebox" rel="noopener nofollow ugc">GitHub - jumbojing/slicerSkill: AI skill for 3D Slicer development - cloud-based search without local downloads</a> )  long-term memory (or at least in your current project) to make it personalized(customize)?</p>
<p>所以呢, 2点想法: 1. 有了 <a class="mention" href="/u/pieper">@pieper</a>  的这个<code>MCP</code> 作为爪子来操作 <code>Slicer</code> , <code>SlicerJupyter</code> 似乎没用了; 2. 给予这个技能长期记忆(或者至少在当前的项目中), 让技能个性化是不是更好呢?</p>

---

## Post #16 by @pieper (2026-02-25 02:57 UTC)

<p>I like those ideas, <a class="mention" href="/u/jumbojing">@jumbojing</a> - of course we need to make sure people are careful whatever we decide to try.  We discussed this a bit at the last developer meeting and running Slicer in a constrained environment of some kind would probably be wisest for experimentation (either a VM or a docker container or just some OS-level sandboxing).</p>

---

## Post #17 by @jumbojing (2026-03-01 20:45 UTC)

<aside class="onebox githubrepo" data-onebox-src="https://github.com/jumbojing/slicerClaw">
  <header class="source">

      <a href="https://github.com/jumbojing/slicerClaw" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/affcf3f674440db094eabf35ea07e02a/jumbojing/slicerClaw" class="thumbnail">

  <h3><a href="https://github.com/jumbojing/slicerClaw" target="_blank" rel="noopener nofollow ugc">GitHub - jumbojing/slicerClaw: A revolutionary,  lightning-fast AI assistant...</a></h3>

    <p><span class="github-repo-description">A revolutionary,  lightning-fast AI assistant natively integrated into 3D Slicer.</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox githubblob" data-onebox-src="https://github.com/jumbojing/slicerClaw/blob/48cccd9941b368219b08800ed2f88a83f8fd6b4b/README.md?plain=1#L1-L19">
  <header class="source">

      <a href="https://github.com/jumbojing/slicerClaw/blob/48cccd9941b368219b08800ed2f88a83f8fd6b4b/README.md?plain=1#L1-L19" target="_blank" rel="noopener nofollow ugc">github.com/jumbojing/slicerClaw</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/jumbojing/slicerClaw/blob/48cccd9941b368219b08800ed2f88a83f8fd6b4b/README.md?plain=1#L1-L19" target="_blank" rel="noopener nofollow ugc">README.md?plain=1</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/jumbojing/slicerClaw/blob/48cccd9941b368219b08800ed2f88a83f8fd6b4b/README.md?plain=1#L1-L19" rel="noopener nofollow ugc"><code>48cccd994</code></a>
</div>



    <pre class="onebox"><code class="lang-md?plain=1">
      <ol class="start lines" start="1" style="counter-reset: li-counter 0 ;">
          <li>&lt;p align="center"&gt;</li>
          <li>  &lt;img src="SlicerClaw/Resources/Icons/SlicerClaw.png" width="200" alt="SlicerClaw Logo"&gt;</li>
          <li>&lt;/p&gt;</li>
          <li></li>
          <li># SlicerClaw (Slicer Native AI Agent &amp; MCP Server)</li>
          <li></li>
          <li>English | [简体中文](README_zh-CN.md)</li>
          <li></li>
          <li>A revolutionary, lightning-fast AI assistant natively integrated into 3D Slicer.</li>
          <li>SlicerClaw provides a seamless, "Spotlight"-style floating command bar for native control, while simultaneously running a secure **Model Context Protocol (MCP)** server on port 2016 to allow external AI tools (like Cursor, Claude Desktop, OpenCode) to control your 3D Slicer environment.</li>
          <li></li>
          <li>## Features</li>
          <li></li>
          <li>- **Spotlight Interface:** No more clunky, docked panels. Just press `Ctrl+I` (Cmd+I) from anywhere in Slicer to summon a beautiful, translucent floating bar.</li>
          <li>- **Embedded MCP Server:** Safely exposes Slicer's Python environment to external AIs via standard JSON-RPC HTTP requests on `http://127.0.0.1:2016/mcp`.</li>
          <li>- **Function Calling (Tools):** Both native and external AI have direct access to Slicer's Python environment. They can list nodes, get properties, take screenshots, and execute arbitrary python code natively.</li>
          <li>- **One-Click MCP Bridge Generator:** Easily generate a `slicer_mcp_bridge.py` script from the UI to seamlessly connect stdio-based AI clients (like Claude/Cursor).</li>
          <li>- **Built-in Knowledge Base Downloader:** Directly download and extract Slicer AI Skills (e.g., `jumbojing/slicerSkill`, Slicer Source Code, Discourse Archives) from the UI to empower your models with 3D Slicer's specific coding context.</li>
          <li>- **Auto Skill Discovery:** The internal MCP tools will automatically search your downloaded skills so external AIs don't have to manually mount the folders.</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Evolve this project by leveraging the popularity of openclaw​<img src="https://emoji.discourse-cdn.com/twitter/lobster.png?v=15" title=":lobster:" class="emoji" alt=":lobster:" loading="lazy" width="20" height="20">; further visualize <a class="mention" href="/u/pieper">@pieper</a>’s slicer-skill, with the default web search skill, and use <a class="mention" href="/u/pieper">@pieper</a>’s Slicer-MCP as the claw <img src="https://emoji.discourse-cdn.com/twitter/lobster.png?v=15" title=":lobster:" class="emoji" alt=":lobster:" loading="lazy" width="20" height="20">. Conduct AI (including <code>slicer-skill</code>) development, testing, and debugging of the project within Slicer or in external AI CLIs (opencode, claude, etc.)… <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a>, we hope you can provide valuable opinions to further optimize and improve it.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7d8584e3952a2c9a95bfa01d0c7c3d28f76a2ec3.jpeg" data-download-href="/uploads/short-url/hUpKk3Bg7CxAj6fTJYY6AGwJbCb.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d8584e3952a2c9a95bfa01d0c7c3d28f76a2ec3_2_500x500.jpeg" alt="image" data-base62-sha1="hUpKk3Bg7CxAj6fTJYY6AGwJbCb" width="500" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d8584e3952a2c9a95bfa01d0c7c3d28f76a2ec3_2_500x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7d8584e3952a2c9a95bfa01d0c7c3d28f76a2ec3.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7d8584e3952a2c9a95bfa01d0c7c3d28f76a2ec3.jpeg 2x" data-dominant-color="C7D4DD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">640×640 75.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>(进化一下这个项目, 借助<code>openclaw🦞 </code>的热度; 将 <a class="mention" href="/u/pieper">@pieper</a>  老师的 <code>slicer-skill</code>  进一步可视化, 默认 网络搜索技能, 将 <a class="mention" href="/u/pieper">@pieper</a> 老师的 <code>Slicer-MCP</code> 作为claw <code>🦞</code> , 在 Slicer 里面 或者外部 AI CLI (opencode, claude等) 进行项目的AI(包含 `slicer-skill` )开发, 测试和调试… <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a>  老师希望您帮忙给出宝贵意见, 进一步优化改进)</p>

---

## Post #18 by @pieper (2026-03-01 23:25 UTC)

<aside class="quote no-group quote-modified" data-username="jumbojing" data-post="17" data-topic="46243">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jumbojing/48/10811_2.png" class="avatar"> jumbojing:</div>
<blockquote>
<p><a href="https://github.com/jumbojing/slicerClaw" class="inline-onebox">GitHub - jumbojing/slicerClaw: A revolutionary, lightning-fast AI assistant natively integrated into 3D Slicer.</a></p>
</blockquote>
</aside>
<p>Very cool <a class="mention" href="/u/jumbojing">@jumbojing</a>!</p>

---

## Post #19 by @lassoan (2026-03-07 17:10 UTC)

<p>4 posts were merged into an existing topic: <a href="/t/confidently-incorrect-posts-appearing-on-forum/46398/4">Confidently incorrect posts appearing on forum</a></p>

---

## Post #23 by @benzwick (2026-03-06 19:30 UTC)

<p>We’ve integrated <a href="https://agentskills.io" rel="noopener nofollow ugc">Agent Skills</a> into our <a href="https://talk2view.com" rel="noopener nofollow ugc">Talk2View</a> extension for 3D Slicer. You can learn more and download the free Talk2View extension for 3D Slicer from our website <a href="https://talk2view.com/download" rel="noopener nofollow ugc">https://talk2view.com/download</a></p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/229a635a17c9096c8d026b51c2e31b86fdb1395c.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e50d23e7b7dafd2872175cdb7f86369ba4ae499c.jpeg" data-video-base62-sha1="4W70yrpKLiQvePRQepZ0l4Q4zko.mp4">
  </div><p></p>
<p>Here is an example of a skill that can be used to automate the segmentation of multiple datasets using different segmentation tools:</p>
<pre><code class="lang-auto">---
name: my-segment-skill
description: Segmentation workflow for brain MRI datasets.
metadata:
    skill-author: Talk2View
---

# My Segment Skill

## Datasets

Process these datasets from Slicer sample data in order:

- MR Brain Tumor 1
- MR Brain Tumor 2

## Segments

For each dataset, create these segments:

| Name       | Color |
| ---------- | ----- |
| Tumor      | red   |
| Ventricles | blue  |

## How to segment

### Tumor

Adaptive Brush with MRI T1+GD enhancing tumor preset, paint at RAS [-5, 27, 28] with 20 mm radius

### Ventricles

First, jump to RAS [18, 21, 1] in all slice views, which is close to where the ventricles are.
Then use Adaptive Brush with simple threshold algorithm, radius of 7 mm, threshold zone of 30%.

## Workflow

Ensure that the scene is empty before you create a new segmentation.

For each dataset:

1. Download the sample data
2. Create a segmentation with the first segment from the table
3. Activate the tool with the specified preset or algorithm, then apply any extras
4. Show the segmentation in 3D, and if the segment has already been painted and is not empty, jump to the segment in all slice views
5. Tell the user they can now refine the segment, and wait until they are done
6. When the user is finished, add the next segment and repeat from step 3
7. When all segments are done, report the volume of each segment,
   save the scene, and clear the scene before
   moving to the next dataset
</code></pre>
<p>You can use the skills editor inside the Talk2View Slicer extension to create and edit new and existing skills.</p>
<p>If someone has any ideas for workflows to test we would be very happy to hear about them.</p>

---

## Post #24 by @pieper (2026-03-14 21:17 UTC)

<blockquote>
<p><img src="https://emoji.discourse-cdn.com/twitter/robot.png?v=15" title=":robot:" class="emoji" alt=":robot:" loading="lazy" width="20" height="20"> This post was written with AI assistance.</p>
</blockquote>
<p>Thanks everyone for the great feedback and suggestions in this thread! It’s exciting to see the community exploring different approaches — from <a class="mention" href="/u/mhalle">@mhalle</a>’s optimized fork to <a class="mention" href="/u/jumbojing">@jumbojing</a>’s lightweight skill and slicerClaw to <a class="mention" href="/u/benzwick">@benzwick</a>’s Talk2View integration.</p>
<p>Several of you raised good points about the original setup requiring ~15 GB of downloads, which is a real barrier for people who just want to try things out or are working on machines with limited disk. I’ve pushed an update to the <a href="https://github.com/pieper/slicer-skill">slicer-skill repo</a> that addresses this directly.</p>
<p><strong>Three setup modes</strong></p>
<p>The setup script now prompts you to choose a mode on first run:</p>
<div class="md-table">
<table>
<thead>
<tr>
<th>Mode</th>
<th>Disk</th>
<th>Setup time</th>
<th>What you get</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>full</strong></td>
<td>~15 GB</td>
<td>~20 min</td>
<td>Everything local — source, deps, all 200+ extensions, discourse archive. Fastest for grep/find/git-log.</td>
</tr>
<tr>
<td><strong>lightweight</strong></td>
<td>~1 GB</td>
<td>~2 min</td>
<td>Slicer source + ExtensionsIndex metadata. Extensions cloned on-demand as needed. Discourse via API.</td>
</tr>
<tr>
<td><strong>web</strong></td>
<td>minimal</td>
<td>instant</td>
<td>Nothing cloned. All access via GitHub API and Discourse search API. Zero setup.</td>
</tr>
</tbody>
</table>
</div><p>Other details:</p>
<ul>
<li>The script checks available disk space and warns if full mode would be a strain</li>
<li>Your choice is saved and reused on subsequent runs</li>
<li>You can switch modes anytime: <code>./setup.sh --force --mode lightweight</code></li>
<li>Non-interactive environments (like an agent running setup automatically) default to lightweight</li>
<li>SKILL.md is updated with mode-aware search strategies so the agent knows to use Discourse API or GitHub API when local data isn’t available</li>
<li>If the agent notices web queries are slow or hitting rate limits, it will suggest upgrading to a heavier mode</li>
</ul>
<p>The full mode is still there for heavy development work where fast local grep and git history matter. But now there’s a smooth on-ramp for people who want to get started quickly or don’t have 15 GB to spare.</p>
<p><strong>Experimental: CodingChats conversations</strong></p>
<p>I’m also testing integration with <a href="https://github.com/pieper/CodingChats">CodingChats</a>, a VS Code extension that automatically captures Claude Code conversation transcripts as JSONL files and commits them to a git repository. The idea is that when the agent is working on a Slicer problem, it can search past AI-assisted coding sessions to see what approaches were tried, what failed, and what prompts led to working solutions — essentially giving the agent memory across sessions.</p>
<p>The setup script auto-detects if you have a <code>CodingChats-conversations</code> repository on your GitHub account and clones it alongside the other skill data. The agent can then grep through session transcripts to find relevant prior work. This is still experimental and I’m evaluating how useful it is in practice, but early results are promising — it’s particularly helpful when the agent encounters a problem that was already solved in a previous session.</p>

---

## Post #25 by @pieper (2026-03-14 21:20 UTC)

<p>This is the human again - one other thing I wanted to mention is that you can see on the CodingChats readme that I flagged the repo as heavily AI-generated.  Just like posts on the forum, I think flagging AI repos and readthedocs content is important.</p>
<p>Some repos look like they are the result of years of human effort but were really just dreamed up in an afternoon.  That doesn’t necessarily make them worse than the multiyear human efforts, but I still think they should be flagged for the sake of transparency.</p>

---

## Post #26 by @benzwick (2026-03-16 02:45 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a></p>
<p>I was following a similar workflow but much more ad hoc than your slicer skill. One of the ways I got around the large repo size was to use symbolic links for e.g. Slicer which I had to refer to in many different projects but already had the source and build tree in another location and git submodules for dependencies that needed very specific versions and branches e.g. with fixes related to the current work a my project.</p>
<p>I also have some skills in my SlicerAdaptiveBrush repo which might be useful.</p>
<p>For example this one that I used to setup up the references to other software similar to your slicer skill:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/benzwick/SlicerAdaptiveBrush/blob/main/.claude/skills/setup-references/SKILL.md">
  <header class="source">

      <a href="https://github.com/benzwick/SlicerAdaptiveBrush/blob/main/.claude/skills/setup-references/SKILL.md" target="_blank" rel="noopener nofollow ugc">github.com/benzwick/SlicerAdaptiveBrush</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/benzwick/SlicerAdaptiveBrush/blob/main/.claude/skills/setup-references/SKILL.md" target="_blank" rel="noopener nofollow ugc">.claude/skills/setup-references/SKILL.md</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/benzwick/SlicerAdaptiveBrush/blob/main/.claude/skills/setup-references/SKILL.md" rel="noopener nofollow ugc"><code>main</code></a>
</div>


      <pre><code class="lang-md"># Setup References Skill

Set up the `_reference/` folder with reference code for development.

## When to Use

- When a developer first clones the repository
- When adding new reference repositories
- When switching between symlink and clone

## Available References

| Name | Repository | Description |
|------|------------|-------------|
| SlicerSource | https://github.com/Slicer/Slicer | 3D Slicer source code |
| SlicerSegmentEditorExtraEffects | https://github.com/lassoan/SlicerSegmentEditorExtraEffects | Extra segment editor effects |
| QuantitativeReporting | https://github.com/QIICR/QuantitativeReporting | DICOM SEG with dcmqi |
| CrossSegmentationExplorer | https://github.com/ImagingDataCommons/SlicerCrossSegmentationExplorer | Segmentation comparison tool |

## Workflow
</code></pre>



  This file has been truncated. <a href="https://github.com/benzwick/SlicerAdaptiveBrush/blob/main/.claude/skills/setup-references/SKILL.md" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>And this one that I used to submit the extension to the extension index:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/benzwick/SlicerAdaptiveBrush/blob/main/.claude/skills/extension-submission-checklist/SKILL.md">
  <header class="source">

      <a href="https://github.com/benzwick/SlicerAdaptiveBrush/blob/main/.claude/skills/extension-submission-checklist/SKILL.md" target="_blank" rel="noopener nofollow ugc">github.com/benzwick/SlicerAdaptiveBrush</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/benzwick/SlicerAdaptiveBrush/blob/main/.claude/skills/extension-submission-checklist/SKILL.md" target="_blank" rel="noopener nofollow ugc">.claude/skills/extension-submission-checklist/SKILL.md</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/benzwick/SlicerAdaptiveBrush/blob/main/.claude/skills/extension-submission-checklist/SKILL.md" rel="noopener nofollow ugc"><code>main</code></a>
</div>


      <pre><code class="lang-md">---
name: extension-submission-checklist
description: Review and track progress against official 3D Slicer Extension Index requirements
allowed-tools:
  - WebFetch
  - Bash
  - Read
context: manual
---

# Extension Submission Checklist Skill

Review and track progress against the official 3D Slicer Extension Index submission requirements.

## When to Use

Use this skill when:
- Preparing to submit an extension to the Slicer Extension Index
- Reviewing submission readiness
- Creating a pull request for extension submission
</code></pre>



  This file has been truncated. <a href="https://github.com/benzwick/SlicerAdaptiveBrush/blob/main/.claude/skills/extension-submission-checklist/SKILL.md" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>One of the nice things about skills is how flexible and interactive they are, i.e. they are just a guide for the LLM and can be discussed to do things slightly differently than what is originally defined in the skill. For example, when deciding whether to clone or symlink different reference projects and where they should be located, etc.</p>
<p>We are also planning to make some pretty major changes to the Talk2View Slicer extension so we can open source some of the components so it might be a good idea to discuss with anyone who is working on similar projects.</p>

---

## Post #27 by @pieper (2026-03-16 14:41 UTC)

<p>I realized that the project week github repo is also a great source of Slicer programming info, so I updated the skill to check that out too.  It’s updated in the slicer-skill repo now.</p>
<blockquote>
<p><img src="https://emoji.discourse-cdn.com/twitter/robot.png?v=15" title=":robot:" class="emoji" alt=":robot:" loading="lazy" width="20" height="20"> This post was written with AI assistance.</p>
</blockquote>
<h3><a name="p-132603-repository-integration-1" class="anchor" href="#p-132603-repository-integration-1" aria-label="Heading link"></a><strong>Repository Integration</strong></h3>
<ul>
<li>Added NA-MIC Project Week repository checkout to setup.sh</li>
<li>Updated SKILL.md to include it as a 4th resource for Slicer programming knowledge</li>
<li>Modified README.md to include the new search path</li>
<li>Successfully cloned the repository via setup.sh</li>
</ul>
<p>Based on that I was able to get the following cool info.</p>
<blockquote>
<p><img src="https://emoji.discourse-cdn.com/twitter/robot.png?v=15" title=":robot:" class="emoji" alt=":robot:" loading="lazy" width="20" height="20"> This post was written with AI assistance.</p>
</blockquote>
<h3><a name="p-132603-comprehensive-statistics-extraction-2" class="anchor" href="#p-132603-comprehensive-statistics-extraction-2" aria-label="Heading link"></a><strong>Comprehensive Statistics Extraction</strong></h3>
<p>The extract_pw_stats.py script successfully extracted:</p>
<ul>
<li><strong>24 Project Weeks</strong> (PW44-PW21, covering 2015-2026)</li>
<li><strong>2,291 Total Registered Participants</strong></li>
<li><strong>759 Total Projects</strong></li>
<li><strong>Average of 95.5 participants per week</strong></li>
<li><strong>Average of 39.9 projects per week</strong></li>
<li><strong>1,002 Unique participant names</strong> (from detailed data in 19 project weeks)</li>
</ul>

---

## Post #28 by @pieper (2026-03-16 14:44 UTC)

<p>That is great <a class="mention" href="/u/benzwick">@benzwick</a>.  I’ve been more focused on the developer side of things, but Talk2View and related projects should really help the user side too.</p>
<p>Since your extension repo is already cloned as part of the setup.sh, my slicer-skill should be able to find it, but it may not realize that it should.  I’ll add something explicit to the skill file suggesting that it look at the md files in all the extensions for extra help when researching a topic.</p>

---

## Post #29 by @pieper (2026-03-16 15:02 UTC)

<p>As a follow-on to this, it would be great if extension developers could add SKILL.md file to their repositories to give extension-specific guidance on how to work with their codebases.</p>

---

## Post #30 by @Dieter_Rosch (2026-03-17 09:54 UTC)

<p>Hi Steve,</p>
<p>Just wanted to say thanks for this amazing skill. I’ve managed to build 2 Slicer extensions that I’ve previously wanted to build, but couldn’t due to my lack of experience in Slicer and the deeper nuances of the scanning technolog etc. I used your skill in claude code, explained what I wanted to do, and asked claude to come up with a plan. It did, and then implemented it. A few minor bugs, some I just debugged with it, others i told it to use the mcp server to look at, but all resolved. Overall, a great experience and a huge benefit to people who don’t work in Slicer or medical imaging dev every day.</p>

---

## Post #31 by @pieper (2026-03-17 11:58 UTC)

<p>That’s cool <a class="mention" href="/u/dieter_rosch">@Dieter_Rosch</a>! <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=15" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>

---

## Post #32 by @Yaroslav_Plutenko (2026-05-25 15:15 UTC)

<p>Greeting!</p>
<p>Thank you for the effort in implementing this brilliant idea. The structured repo works great. I have already managed to find useful info with the LLM agent. But I don’t see the <strong>slicer-discourse</strong> subfolder after running <code>setup.sh</code>.  Is something wrong, or has this part not been added yet?   If available, can I download it separately?</p>

---

## Post #33 by @pieper (2026-05-26 14:18 UTC)

<p>Thanks for the kind words <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=15" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"> I hope people are finding this helpful!  I have been using it every day.</p>
<p>You are right about the slicer-discourse checkout - that was a regression when adding some other features.</p>
<p>If you update now and run:</p>
<pre><code class="lang-auto">git pull
./setup.sh --mode full --force
</code></pre>
<p>you should be back in business.</p>
<p>Also, as a side note on the current main branch, I’ve added some new search tooling beyond grep, so I hope it’s now more efficient at finding the right code to learn from. (it runs an embedding in the background so the script exits by then the python process will run another 20 minutes or so).</p>

---

## Post #34 by @Yaroslav_Plutenko (2026-05-26 16:42 UTC)

<p>Yes, got updated, thank you!</p>

---

## Post #35 by @pieper (2026-05-26 16:45 UTC)

<p>BTW, after playing with it a bit I noticed some discourse topic threads weren’t getting updated to the github archive so there are a few more tweaks to the github action script I’m testing now.  The skill should automatically update over the course of a few days.</p>

---

## Post #36 by @mhalle (2026-05-26 16:49 UTC)

<p>Having the skill use the Discourse APi works well for me. It saves large downloads and provides effective search for the Slicer forum.</p>
<p>-Mike</p>

---
