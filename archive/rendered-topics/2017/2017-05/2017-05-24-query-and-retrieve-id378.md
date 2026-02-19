---
topic_id: 378
title: "Query And Retrieve"
date: 2017-05-24
url: https://discourse.slicer.org/t/378
---

# Query and Retrieve

**Topic ID**: 378
**Date**: 2017-05-24
**URL**: https://discourse.slicer.org/t/query-and-retrieve/378

---

## Post #1 by @neuroimage_analyst (2017-05-24 19:12 UTC)

<p>Operating system: Centos 7<br>
Slicer version: 4.6.2<br>
Expected behavior: Proper retrieveal<br>
Actual behavior: Nothing happens</p>
<p>Hi, Slicer Users and Developers</p>
<p>Please pardon my very simple question below:</p>
<p>I am trying to set up a local PACS server in my lab to access the data from the MRI/PET scanner. I have 2 questions and I am hoping that somebody can guide me to solve this problem.</p>
<p>Problem 1: I am able to run Query and see the subject that I want to retrieve the data of from MRI scanner. But, when I click retrieve, the log on the screen is</p>
<pre><code class="lang-auto">E: Failed receiveing DIMSE command: 0006:031 Peer aborted Association (or never connected)
GET responses report for study: 1.2.840.113696.376376.500.38586294.20170505170859
0 images transferred, and
0 images transferred with warning, and
2728 images transfers failed
Retrieve success
I: Releasing Association
E: Association Release Failed: 0006:0303 DUL Finite State Machine Error: No action defined, state 1 event 10
I: Aborting Association
E: Association Abort Failed: 0006:0303 DUL Finite State Machine Error: No action defined, state 1 event 14
</code></pre>
<p>Can anybody guide me as to what is the problem here?</p>
<p>Problem 2: How do I retrieve the data only using command line and not opening GUI everytime?</p>
<p>I will greatly appreciate any response.</p>
<p>Thanks</p>
<p>Regards</p>
<p>Virendra</p>

---

## Post #2 by @lassoan (2017-05-24 19:12 UTC)

<p>Could you please try if it works correctly with the latest nightly version?</p>

---

## Post #3 by @neuroimage_analyst (2017-05-24 19:29 UTC)

<p>Thank you for your reply, Andras. But I have the same error with 4.7.0-2017-05-23</p>
<p>On the scanner, I set the port 4054 , AE TILE: LOCALPACS, IP:xx.xx.xx.xx for the local PACS server on which Slicer is running</p>
<p>On Slicer DICOM window, should my storage Port be 4054 or 11112 (default)? Also, Storage AETitle be LOCALPACS or the default (CTKSTORE) is fine? I believe just change the Calling AE TITLE to LOCALPACS should suffice?</p>
<p>Also, where is the .cfg file for the DICOM window GUI called as FORM saved on my computer? I checked Slicer --settings-path but doesn’t have the exact dcmqrscp.cfg that is eventually being used by Slicer?</p>
<p>I will appreciate any suggestions.</p>
<p>Thanks</p>
<p>Regards</p>
<p>Virendra</p>

---

## Post #4 by @pieper (2017-05-24 20:28 UTC)

<p>A couple suggestions:</p>
<ul>
<li>
<p>check if CGET is supported on your scanner.  If not, you need to be running the Listener on the Slicer side and your scanner needs to be configured to be able to send to it.</p>
</li>
<li>
<p>the Slicer listener runs as an independent process (storescp) so you can use our OS tools to look at that process to see what the command line arguments are and use the DCMTK documentation to understand how those map to what your scanner expects.</p>
</li>
<li>
<p>Often debugging is easiest by using the command line tools independent of Slicer to confirm all the settings and then copy them to Slicer.</p>
</li>
</ul>
<p>Here are some notes about using dcmtk command line tools for storage, query:</p>
<p><a href="https://www.na-mic.org/Wiki/index.php/CTSC:ARRA:Mockup#PACS" class="onebox" target="_blank">https://www.na-mic.org/Wiki/index.php/CTSC:ARRA:Mockup#PACS</a></p>
<p>And a test at the CTK level that shows how the communication works and it might give you some clues:</p>
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


---
