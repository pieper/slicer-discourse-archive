---
topic_id: 29144
title: "How To Change Placeholder Text In Ctkcheckablecombobox"
date: 2023-04-26
url: https://discourse.slicer.org/t/29144
---

# How to change placeholder text in ctkCheckableComboBox

**Topic ID**: 29144
**Date**: 2023-04-26
**URL**: https://discourse.slicer.org/t/how-to-change-placeholder-text-in-ctkcheckablecombobox/29144

---

## Post #1 by @Mauricio_Cespedes (2023-04-26 14:55 UTC)

<p>Hi, I’m currently building an extension and I’m using a few ctkCheckableComboBox widgets, which I’m creating in a .ui file and then loading on my Python script for the extension I’m building. I’m wondering if there’s any way to change the text of the widget when no option is selected. By default it say ‘None’ but I wanted to change it. Tried with the attribute placeholderText but didn’t work. I’d appreciate any help. Thanks in advance!</p>

---

## Post #2 by @jamesobutler (2023-04-26 15:06 UTC)

<p>The text associated with the None selection of a ctkCheckableComboBox appears to be hardcoded at the following location so it is not something modifiable from a UI file. What were you hoping to change the text to be?</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/commontk/CTK/blob/b6b2c584651ba725d3a7b64c7afe352a661ee756/Libs/Widgets/ctkCheckableComboBox.cpp#L388-L392">
  <header class="source">

      <a href="https://github.com/commontk/CTK/blob/b6b2c584651ba725d3a7b64c7afe352a661ee756/Libs/Widgets/ctkCheckableComboBox.cpp#L388-L392" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/commontk/CTK/blob/b6b2c584651ba725d3a7b64c7afe352a661ee756/Libs/Widgets/ctkCheckableComboBox.cpp#L388-L392" target="_blank" rel="noopener nofollow ugc">commontk/CTK/blob/b6b2c584651ba725d3a7b64c7afe352a661ee756/Libs/Widgets/ctkCheckableComboBox.cpp#L388-L392</a></h4>



    <pre class="onebox"><code class="lang-cpp">
      <ol class="start lines" start="388" style="counter-reset: li-counter 387 ;">
          <li>else if (this-&gt;noneChecked())</li>
          <li>  {</li>
          <li>  opt.currentText = tr("None");</li>
          <li>  opt.currentIcon = QIcon();</li>
          <li>  }</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Mauricio_Cespedes (2023-04-26 15:18 UTC)

<p>Yeah, I saw that part of the C++ code, I guess I was just hoping that perhaps there was a workaround haha. So I’m currently building an extension that will help with some file conversion, so I have a list of files from which the user could select which to import/convert:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fce13686c001b6ded46e34750a39b73546ee4903.png" data-download-href="/uploads/short-url/A54Q1KUrqJGbOgw2akyipV26vD5.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fce13686c001b6ded46e34750a39b73546ee4903_2_690x200.png" alt="image" data-base62-sha1="A54Q1KUrqJGbOgw2akyipV26vD5" width="690" height="200" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fce13686c001b6ded46e34750a39b73546ee4903_2_690x200.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fce13686c001b6ded46e34750a39b73546ee4903.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fce13686c001b6ded46e34750a39b73546ee4903.png 2x" data-dominant-color="ECECEC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">801×233 35.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
So I created some ComboBoxes with the options All/None so that it’s easier to select/deselect all files at once (the widgets that say ‘All’ are the ctkCheckableComboBox widgets, which have two QCheckBox items: ‘All’ and ‘None’). So as you can see, I have two ‘None’ options. When I select the ‘None’ from my option, the ctkCheckableComboBox shows ‘None’ but when I have no option selected (when not all files are selected but some are) it also shows ‘None’.<br>
Then I was expecting to change the placeholder to something like ‘—’ or so.</p>

---

## Post #4 by @jamesobutler (2023-04-26 16:07 UTC)

<p>It seems like you desire the checkable functionality as used in the File Name column of the Add Data and Save Data (see image below) dialogs within Slicer.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1c6b3439b189209eb2c20e056262642a0cd709f.png" alt="image" data-base62-sha1="tVLvhRt0yaJitBZjz4ShdDaMIAT" width="165" height="239"></p>
<p>Since you are using a QTableWidget, you may want to look into using a ctkCheckableHeaderView which is that type of functionality where it is checked to display that All items are checked, unchecked when all items are unchecked, and the tristate display when some items are checked and some are unchecked.</p><aside class="onebox githubblob" data-onebox-src="https://github.com/commontk/CTK/blob/master/Libs/Widgets/ctkCheckableHeaderView.h">
  <header class="source">

      <a href="https://github.com/commontk/CTK/blob/master/Libs/Widgets/ctkCheckableHeaderView.h" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/commontk/CTK/blob/master/Libs/Widgets/ctkCheckableHeaderView.h" target="_blank" rel="noopener nofollow ugc">commontk/CTK/blob/master/Libs/Widgets/ctkCheckableHeaderView.h</a></h4>


      <pre><code class="lang-h">/*=========================================================================

  Library:   CTK

  Copyright (c) Kitware Inc.

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0.txt

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.

=========================================================================*/
/*=========================================================================
</code></pre>



  This file has been truncated. <a href="https://github.com/commontk/CTK/blob/master/Libs/Widgets/ctkCheckableHeaderView.h" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
