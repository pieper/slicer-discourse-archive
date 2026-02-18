# Replace scripted module template by scripteddesigner

**Topic ID**: 10736
**Date**: 2020-03-18
**URL**: https://discourse.slicer.org/t/replace-scripted-module-template-by-scripteddesigner/10736

---

## Post #1 by @lassoan (2020-03-18 14:46 UTC)

<p>We have two scripted module templates now: scripted and scripteddesigner. The “scripted” template has several limitations: GUI widgets are created from code, parameter node is not used (user choices are not saved in the scene), logic is not created in the widget (so it is not accessible from other modules).</p>
<p>What do you think about replacing “scripted” template by the new “scripteddesigner” template?</p>

---

## Post #2 by @pieper (2020-03-18 15:03 UTC)

<p>It would be nice to have just one template that supported both approaches.</p>

---

## Post #3 by @lassoan (2020-03-18 15:05 UTC)

<p>I can certainly add an example in the template that shows how to add a widget using Python code.</p>

---

## Post #4 by @cpinter (2020-03-18 15:11 UTC)

<p>I think it is a good idea to retire the old scripted module template. I don’t see any advantages for using that. Besides, it tends to confuse people at bootcamps, so I imagine that it would confuse any non-expert Slicer developer as well. Better to not have any obsolete options exposed.</p>

---

## Post #5 by @lassoan (2020-03-19 00:01 UTC)

<p>Pull request submitted:</p>
<aside class="onebox githubpullrequest">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/pull/4744" target="_blank">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/pull/4744" target="_blank">ENH: Replace old "scripted" module template by the new "scripteddesigner" template</a>
    </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>lassoan:replace-scripted-module-template</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-03-18" data-time="23:55:09" data-timezone="UTC">11:55PM - 18 Mar 20 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank">
          <img alt="lassoan" src="https://avatars0.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>

      <div class="lines" title="1 commits changed 8 files with 235 additions and 481 deletions">
        <a href="https://github.com/Slicer/Slicer/pull/4744/files" target="_blank">
          <span class="added">+235</span>
          <span class="removed">-481</span>
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


---

## Post #6 by @szhang (2020-04-28 20:45 UTC)

<p>Now under Extension Wizards there are all 4 options of scripted, scriptededitoreffect, scriptedsegmenteditoreffect, and scripteddesigner. If scripteddesigner is recommended, is there a tutorial link for this? Thank you.</p>

---

## Post #7 by @lassoan (2020-04-28 21:02 UTC)

<p>You can find Slicer scripted module development tutorial here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials">https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials</a></p>

---

## Post #8 by @Jack_Zhang (2022-09-12 20:45 UTC)

<p>I’m sorry if this is a dumb question but I can’t seem to find the scripteddesigner template. Can someone offer a hand by any chance?</p>

---

## Post #9 by @jamesobutler (2022-09-12 23:18 UTC)

<p>The “scripteddesigner” template has been replaced by just the “scripted” template. There are currently the following module template options when using the Extension Wizard:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/1971d90bb7833e43fed4edc9cb1cb0c22af1d54a.png" alt="image" data-base62-sha1="3D5QZaypcvrJTmpDOmrVAh6EQgq" width="260" height="203"></p>
<p>Also see <a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#where-can-i-find-the-extension-templates" rel="noopener nofollow ugc">where-can-i-find-the-extension-templates</a>.</p>

---

## Post #10 by @Jack_Zhang (2022-09-13 15:51 UTC)

<p>Oh okay thanks. There’s this one section of code that comes with the template that I’d like clarification on:</p>
<pre><code class="lang-auto">uiWidget = slicer.util.loadUI(self.resourcePath('UI/DisplayData.ui'))
self.layout.addWidget(uiWidget)
self.ui = slicer.util.childWidgetVariables(uiWidget)
</code></pre>
<p>There’s a <a href="https://youtu.be/njoTEisxAJ4?t=149" rel="noopener nofollow ugc">tutorial</a> on youtube that doesn’t seem to be using the same template, and doesn’t have three lines of code above. Is the code above required, or is it a place holder that I can replace by writing something similar to what’s shown in the video?</p>

---

## Post #11 by @jamesobutler (2022-09-13 16:03 UTC)

<p>Coding up user interface in python was the old recommendation, but using a UI file which you can manipulate using the Qt Designer is the easier and the current recommendation. The above code that you wrote is the current recommendation so you should continue with that.</p>

---

## Post #12 by @Jack_Zhang (2022-09-13 16:42 UTC)

<p>I’m very new to this (this is my second week of using 3D Slicer) so I apologize if these questions sound dumb. I googled Qt Designer and it appears to be a separate program. Do I install this, create a widget app, and then specify the file path where <code>'UI/DisplayData.ui'</code> currently is in the first line of the code I pasted above? Do I then need to add a folder named “UI” inside the directory for the module?</p>

---

## Post #13 by @lassoan (2022-09-15 18:11 UTC)

<p>For developers convenience, Qt Designer is bundled with Slicer. You can find a Slicer programming tutorial that uses the designer <a href="https://github.com/PerkLab/PerkLabBootcamp/blob/master/Doc/day3_2_SlicerProgramming.pptx?raw=true">here</a>.</p>

---

## Post #14 by @Jack_Zhang (2022-09-19 15:00 UTC)

<p>Thanks so much! This helps a lot.</p>

---
