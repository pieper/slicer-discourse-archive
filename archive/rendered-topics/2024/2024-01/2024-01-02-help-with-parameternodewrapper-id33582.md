# Help with parameterNodeWrapper

**Topic ID**: 33582
**Date**: 2024-01-02
**URL**: https://discourse.slicer.org/t/help-with-parameternodewrapper/33582

---

## Post #1 by @jmhuie (2024-01-02 05:59 UTC)

<p>I am trying to familiarize myself with using a parameterNodeWrapper to save parameters for my custom modules. Based on the documentation and analyzing the exampled scripted modules from the Extension Wizard, I have a general understanding of how to connect the selected SegmentationNode from a qMRMLNodeComboBox to the parameterNode. However, I am currently using the qMRMLSegmentSelectorWidget and would like to set up parameters for the segmentationNode and the selected segments, but I’m not sure if that’s even possible. If it is, I’m not sure how to go about that. Help would be appreciated.</p>
<p>Thanks.</p>

---

## Post #2 by @lassoan (2024-01-03 06:02 UTC)

<p>Unfortunately, no GUI connector is available for qMRMLSegmentSelectorWidget yet. I’ve added an issue for this:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/7499">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/7499" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/7499" target="_blank" rel="noopener">ENH: Add Gui Connection support for a subset of ctk Widgets</a>
      </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>HarryDC:add-gui-wrappings</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2023-12-19" data-time="13:55:05" data-timezone="UTC">01:55PM - 19 Dec 23 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/HarryDC" target="_blank" rel="noopener">
            <img alt="HarryDC" src="https://avatars.githubusercontent.com/u/1878111?v=4" class="onebox-avatar-inline" width="20" height="20">
            HarryDC
          </a>
        </div>

        <div class="lines" title="1 commits changed 3 files with 125 additions and 51 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/7499/files" target="_blank" rel="noopener">
            <span class="added">+125</span>
            <span class="removed">-51</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Adds support for : `ctkCheckbox`, `ctkComboBox`, `ctkDoubleSlider`, `ctkDoubleSp<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/7499" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">inBox`, `ctkDoubleRangeSlider`

Depends on https://github.com/commontk/CTK/pull/1158  

Adds some of the widgets from #7308</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>There has been some progress recently in adding support for more widgets:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/7499">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/7499" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/7499" target="_blank" rel="noopener">ENH: Add Gui Connection support for a subset of ctk Widgets</a>
      </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>HarryDC:add-gui-wrappings</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2023-12-19" data-time="13:55:05" data-timezone="UTC">01:55PM - 19 Dec 23 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/HarryDC" target="_blank" rel="noopener">
            <img alt="HarryDC" src="https://avatars.githubusercontent.com/u/1878111?v=4" class="onebox-avatar-inline" width="20" height="20">
            HarryDC
          </a>
        </div>

        <div class="lines" title="1 commits changed 3 files with 125 additions and 51 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/7499/files" target="_blank" rel="noopener">
            <span class="added">+125</span>
            <span class="removed">-51</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Adds support for : `ctkCheckbox`, `ctkComboBox`, `ctkDoubleSlider`, `ctkDoubleSp<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/7499" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">inBox`, `ctkDoubleRangeSlider`

Depends on https://github.com/commontk/CTK/pull/1158  

Adds some of the widgets from #7308</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>qMRMLSegmentSelectorWidget is not included in this PR, but it gives you an example of how to write a GUI connector and you could consider implementing it and contributing it to Slicer core.</p>
<p>Without a GUI connector, you can still manually get/set values in the parameter node as it was done before in <a href="https://github.com/Slicer/Slicer/blob/8d1ff646c59379c9f13e90b026bef1a942e8611f/Utilities/Templates/Modules/Scripted/TemplateKey.py">earlier versions of the module template</a> and how it is still done in some modules (such as <a href="https://github.com/Slicer/Slicer/blob/9f4b50f95afed0542e8b63a0827ec2167073a4cd/Modules/Scripted/VectorToScalarVolume/VectorToScalarVolume.py#L197-L281">VectorToScalarVolume</a> module).</p>

---
