---
topic_id: 2012
title: "Dicom Pacs Does Retrieve But Series Do Not Show In Browser"
date: 2018-02-02
url: https://discourse.slicer.org/t/2012
---

# DICOM PACS does retrieve, but series do not show in browser

**Topic ID**: 2012
**Date**: 2018-02-02
**URL**: https://discourse.slicer.org/t/dicom-pacs-does-retrieve-but-series-do-not-show-in-browser/2012

---

## Post #1 by @stephan (2018-02-02 16:01 UTC)

<p>Hello,<br>
after importing DICOM data from the local disk so far, I tried to set up the PACS retrieve functionality of Slicer today. I am able to perform queries (log says “C-FIND successful” and the patient shows up in the query list) and retrieve (message box “retrieve process finished”). But the data does not show up in the DICOM browser after I close the PACS client form.<br>
Where do I have to look for the retrieved images?</p>
<p>Thank you so much for any guidance on that.<br>
Stephan</p>

---

## Post #2 by @pieper (2018-02-02 23:32 UTC)

<p>Hi Stephan -<br>
Did you set up the listener on the Slicer side?  You after the C-FIND you need to do the C-MOVE from the PACS to Slicer’s C-STORE which needs to be running and configured as a destination for the PACS.  (Or you can use C-GET if supported by the PACS).  Once this is all working the studies should show up in the DICOM database and browser.</p>
<p>The code uses CTK classes - this test implements the steps and also shows how to do each of the steps (both the client and the server side) using the dcmtk command line tools and that might help you debug.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/commontk/CTK/blob/master/Applications/Testing/Cpp/ctkDICOMApplicationTest1.cpp" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/commontk/CTK/blob/master/Applications/Testing/Cpp/ctkDICOMApplicationTest1.cpp" target="_blank" rel="nofollow noopener">commontk/CTK/blob/master/Applications/Testing/Cpp/ctkDICOMApplicationTest1.cpp</a></h4>
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

  This file has been truncated. <a href="https://github.com/commontk/CTK/blob/master/Applications/Testing/Cpp/ctkDICOMApplicationTest1.cpp" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>-Steve</p>
<p>p.s. while the DICOM networking features do work in Slicer I don’t know if they are actually widely used.  DICOM networking is notoriously tricky to debug.</p>

---

## Post #3 by @stephan (2018-02-03 23:37 UTC)

<p>Thank you. I can only give it another try on Monday at work, but then I will make sure the Listener is on.</p>

---

## Post #4 by @timeanddoctor (2020-01-17 11:22 UTC)

<p>Did you deal with it now?</p>

---

## Post #5 by @stephan (2020-01-20 20:55 UTC)

<p>Sorry for never getting back to this topic. It turned out to be an issue with the PACS server and the rights I had there. So nothing Slicer related.</p>

---
