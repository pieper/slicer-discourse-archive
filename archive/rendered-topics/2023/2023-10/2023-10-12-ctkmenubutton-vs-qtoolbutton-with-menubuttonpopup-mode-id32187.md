# ctkMenuButton vs QToolButton with MenuButtonPopup mode

**Topic ID**: 32187
**Date**: 2023-10-12
**URL**: https://discourse.slicer.org/t/ctkmenubutton-vs-qtoolbutton-with-menubuttonpopup-mode/32187

---

## Post #1 by @jamesobutler (2023-10-12 13:21 UTC)

<p>Does anyone know why one might use a ctkMenuButton over a QToolButton with MenuButtonPopup mode set?</p>
<p>They appear to be virtually the same so I was curious why ctkMenuButton might have been created and what advantages it has that I might be missing.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c2bcd0a870a6bc289c405fd75aeaacb43c254fb2.png" alt="image" data-base62-sha1="rMJa9dKdgNNNAOjBudzFOAivueK" width="402" height="339"></p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/commontk/CTK/blob/b9ef9b8aa1938676ce0ac105a3deb0e1bfc235a1/Libs/Widgets/ctkMenuButton.cpp">
  <header class="source">

      <a href="https://github.com/commontk/CTK/blob/b9ef9b8aa1938676ce0ac105a3deb0e1bfc235a1/Libs/Widgets/ctkMenuButton.cpp" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/commontk/CTK/blob/b9ef9b8aa1938676ce0ac105a3deb0e1bfc235a1/Libs/Widgets/ctkMenuButton.cpp" target="_blank" rel="noopener nofollow ugc">commontk/CTK/blob/b9ef9b8aa1938676ce0ac105a3deb0e1bfc235a1/Libs/Widgets/ctkMenuButton.cpp</a></h4>


      <pre><code class="lang-cpp">/*=========================================================================

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

</code></pre>



  This file has been truncated. <a href="https://github.com/commontk/CTK/blob/b9ef9b8aa1938676ce0ac105a3deb0e1bfc235a1/Libs/Widgets/ctkMenuButton.cpp" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://doc.qt.io/qt-5/qtoolbutton.html#ToolButtonPopupMode-enum">
  <header class="source">
      <img src="https://d33sqmjvzgs8hq.cloudfront.net/wp-content/themes/oneqt/assets/images/favicon.ico.gzip" class="site-icon" width="32" height="32">

      <a href="https://doc.qt.io/qt-5/qtoolbutton.html#ToolButtonPopupMode-enum" target="_blank" rel="noopener nofollow ugc">doc.qt.io</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://doc.qt.io/qt-5/qtoolbutton.html#ToolButtonPopupMode-enum" target="_blank" rel="noopener nofollow ugc">QToolButton Class | Qt Widgets 6.6.0</a></h3>

  <p>The QToolButton class provides a quick-access button to commands or options, usually used inside a QToolBar.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #2 by @jamesobutler (2023-10-12 21:04 UTC)

<p>Although QToolButton has more options to have Icon Only or the text next to it below it, etc, maybe the reason for ctkMenuButton is to have the icon and button text centered in the object? The QToolButton seems to only support left aligned text+icon.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f49d66c8732bd21f431aac09cf1e62ed58999d60.png" alt="image" data-base62-sha1="yTXJvgnSrMcw9KMHcTq3d8GdVv2" width="419" height="129"></p>

---
