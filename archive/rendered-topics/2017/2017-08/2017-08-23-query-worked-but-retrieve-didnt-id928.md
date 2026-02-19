---
topic_id: 928
title: "Query Worked But Retrieve Didnt"
date: 2017-08-23
url: https://discourse.slicer.org/t/928
---

# Query worked but retrieve didn't

**Topic ID**: 928
**Date**: 2017-08-23
**URL**: https://discourse.slicer.org/t/query-worked-but-retrieve-didnt/928

---

## Post #1 by @Ningrong_Ye (2017-08-23 04:30 UTC)

<p>Operating system: Windows7 and Linux Redhat7<br>
Slicer version: Slicer-4.7.0<br>
Expected behavior: query and retrieve<br>
Actual behavior: query work and retrieve not.<br>
first I install Slicer 4.7 in Linux Redhat7, use it to connect with hospital’s PACS,<br>
query work, I can receive all the patient data, but retrieve did.<br>
when I click “retrieve” terminal shown:<br>
About to retrieve 1.2.840.11****.523***.500.***<em><strong>.20170822132</strong></em> from PACS_IP<br>
Starting to retrieve<br>
Starting moveStudy<br>
Negotiating Association<br>
I: Requesting Association<br>
I: Association Accepted (Max Send PDV: 28660)<br>
Setting Retrieve Parameters<br>
Sending Move Request<br>
I: Sending C-MOVE Request (MsgID 1)<br>
I: Received C-MOVE Response (Failed: IdentifierDoesNotMatchSOPClass)<br>
setting value to 0<br>
E: Identifier does not match SOP class in C-MOVE response<br>
MOVE response receveid with status: Failed: IdentifierDoesNotMatchSOPClass<br>
MOVE request failed, server does report error<br>
MOVE request failed: Status Detail:<br>
# Dicom-Data-Set<br>
# Used TransferSyntax: Little Endian Implicit<br>
(0000,0901) AT (0000,0600)                              #   4, 1 OffendingElement<br>
(0000,0902) LO [MOVE_REQUEST_IMPROPERLY_FORMATED]       #  32, 1 ErrorComment’</p>
<p>then I try Steve Pieper’s suggestion:</p>
<aside class="quote no-group quote-modified" data-username="pieper" data-post="4" data-topic="378">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"><a href="https://discourse.slicer.org/t/query-and-retrieve/378/4">Query and Retrieve</a></div>
<blockquote>
<p>A couple suggestions:</p>
<p>check if CGET is supported on your scanner.  If not, you need to be running the Listener on the Slicer side and your scanner needs to be configured to be able to send to it.</p>
<p>the Slicer listener runs as an independent process (storescp) so you can use our OS tools to look at that process to see what the command line arguments are and use the DCMTK documentation to understand how those map to what your scanner expects.</p>
<p>Often debugging is easiest by using the command line tools independent of Slicer to confirm all the settings and then copy them to Slicer.</p>
<p>Here are some notes about using dcmtk command line tools for storage, query:</p>
<p><a href="https://www.na-mic.org/Wiki/index.php/CTSC:ARRA:Mockup#PACS" class="inline-onebox" rel="noopener nofollow ugc">CTSC:ARRA:Mockup - NAMIC Wiki</a></p>
<p>And a test at the CTK level that shows how the communication works and it might give you some clues:</p>
</blockquote>
</aside>
<p>I try both cget and cmove, both not work.<br>
then I install dcmtk,<br>
this time findscu also work well, but movescu didn’t, the script is as follow:<br>
<code>./movescu  --patient --key 0020,000d=1.2.840.113619.2.327.3.1695*****.707.15********.459 --output-directory /home1/try --write-file --aetitle My_NAME --call PACS_NAME PACS_IP PORT</code><br>
Result is:<br>
<code>W: Move response with error status (Failed: IdentifierDoesNotMatchSOPClass)</code></p>
<p>Then I try to use windows version: Slicer-4.7.0<br>
This time also install another software <strong>Radiant</strong> to test is there is something wrong with PACS server.<br>
But with the same setting, Radiant can query and retrieve all the image. but Slicer still can only query.<br>
When come to retrieve,<br>
Slicer the terminal shows:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7acc367963261f248706e69e7793b2d9a153bd28.png" data-download-href="/uploads/short-url/hwjM4aFVPSBiJ86hamNIPPutMcE.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7acc367963261f248706e69e7793b2d9a153bd28_2_486x500.png" alt="image" data-base62-sha1="hwjM4aFVPSBiJ86hamNIPPutMcE" width="486" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7acc367963261f248706e69e7793b2d9a153bd28_2_486x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7acc367963261f248706e69e7793b2d9a153bd28.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7acc367963261f248706e69e7793b2d9a153bd28.png 2x" data-dominant-color="1F2020"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">673×691 104 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I will greatly appreciate any response.</p>
<p>Thanks</p>
<p>Regards</p>
<p>Ningrong</p>

---

## Post #2 by @Ningrong_Ye (2017-08-23 04:32 UTC)

<p>Hi all,<br>
I’m using Redhat7, installed Slicer-4.7.0-2017-08-16-linux-amd64</p>
<p>Here is my problem,<br>
I try to query from our hospital’s server.<br>
I work, I can get all patients data.<br>
But, I can’t retrieve any from the server.(I try both C-get and C-move both are not work )<br>
from terminal I found:</p>
<pre><code>I: Requesting Association
I: Association Accepted (Max Send PDV: 28660)
Setting Retrieve Parameters
Sending Move Request
I: Sending C-MOVE Request (MsgID 1)
I: Received C-MOVE Response (Failed: IdentifierDoesNotMatchSOPClass)
setting value to 0
E: Identifier does not match SOP class in C-MOVE response
MOVE response receveid with status: Failed: IdentifierDoesNotMatchSOPClass
MOVE request failed, server does report error
MOVE request failed: Status Detail: 
# Dicom-Data-Set
# Used TransferSyntax: Little Endian Implicit
(0000,0901) AT (0000,0600)                              #   4, 1 OffendingElement
(0000,0902) LO [MOVE_REQUEST_IMPROPERLY_FORMATED]       #  32, 1 ErrorComment
</code></pre>
<p>then I try to use Steve Pieper’s advice</p>
<aside class="quote no-group quote-modified" data-username="pieper" data-post="4" data-topic="378">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"><a href="https://discourse.slicer.org/t/query-and-retrieve/378/4">Query and Retrieve</a></div>
<blockquote>
<p>A couple suggestions:</p>
<p>check if CGET is supported on your scanner.  If not, you need to be running the Listener on the Slicer side and your scanner needs to be configured to be able to send to it.</p>
<p>the Slicer listener runs as an independent process (storescp) so you can use our OS tools to look at that process to see what the command line arguments are and use the DCMTK documentation to understand how those map to what your scanner expects.</p>
<p>Often debugging is easiest by using the command line tools independent of Slicer to confirm all the settings and then copy them to Slicer.</p>
<p>Here are some notes about using dcmtk command line tools for storage, query:</p>
<p><a href="https://www.na-mic.org/Wiki/index.php/CTSC:ARRA:Mockup#PACS" class="inline-onebox" rel="noopener nofollow ugc">CTSC:ARRA:Mockup - NAMIC Wiki</a></p>
<p>And a test at the CTK level that shows how the communication works and it might give you some clues:</p>
</blockquote>
</aside>
<p>I download and install dcmtk,<br>
Also findscu works, but movescu not;<br>
here is the script:<br>
<code> movescu  --patient --key 0020,000d=1.2.840.113619.2.327.3.1695170825.707.1503019605.111 --output-directory /home1/try --write-file --aetitle MYAT --call SERVER IP_address Port</code><br>
result is:<br>
<code> W: Move response with error status (Failed: IdentifierDoesNotMatchSOPClass)</code></p>
<p>I will appreciate any suggestions.<br>
Thanks<br>
Ningrong</p>

---

## Post #3 by @pieper (2017-08-23 20:50 UTC)

<p>Hi Ningrong -</p>
<p>Were you also running <code>storescp</code>?  The way these DIMSE commands work is that the <code>movescu</code> (move user) requests that the data be sent to a <code>storescp</code> (store provider).</p>
<p>Slicer runs a <code>storescp</code> process (controlled by the Listener button) and configured in the query dialog.  But your server (the move provider) needs to be appropriately configured to allow it to send to Slicer’s <code>storescp</code>.</p>
<p>Diagnosing these things is notoriously painful.</p>
<p>there are some hopefully helpful resources on the wiki:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM#References" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM#References</a></p>
<p>This is a great book on the topic:<br>
<aside class="onebox amazon">
  <header class="source">
      <a href="https://www.amazon.com/Digital-Imaging-Communications-Medicine-DICOM/dp/3642108490/ref=dp_ob_title_bk" target="_blank">amazon.com</a>
  </header>
  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:264/400;"><img src="https://images-na.ssl-images-amazon.com/images/I/41c3rJi8bVL._AC_SY400_.jpg" class="thumbnail" width="264" height="400"></div>

<h3><a href="https://www.amazon.com/Digital-Imaging-Communications-Medicine-DICOM/dp/3642108490/ref=dp_ob_title_bk" target="_blank">Digital Imaging and Communications in Medicine (DICOM): A Practical Introduction and Survival Guide

</a></h3>


<p>
  4.6 out of 5 stars, 
  
  
  
  <strong>$118.99</strong>
</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>Hope that helps,<br>
Steve</p>

---

## Post #4 by @timeanddoctor (2020-01-17 11:22 UTC)

<p>I  succeed connect the GEPACS and but nothing happon when click the retrieve. And the erro information was “no valid presetation contexts”. What should I do next step for retrieve and never installing other software for security?</p>

---

## Post #5 by @lassoan (2020-01-17 14:29 UTC)

<p>Query-retrieve can go wrong at many levels. I would recommend to debug with DCMTK’s standalone command-line applications first (<a href="https://support.dcmtk.org/docs/mod_dcmnet.html">https://support.dcmtk.org/docs/mod_dcmnet.html</a>) and once everything works, we can help transferring that configuration to work within Slicer.</p>

---
