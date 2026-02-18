# Problem of retrieve(query work but retrieve dead)

**Topic ID**: 929
**Date**: 2017-08-23
**URL**: https://discourse.slicer.org/t/problem-of-retrieve-query-work-but-retrieve-dead/929

---

## Post #1 by @Ningrong_Ye (2017-08-23 04:31 UTC)

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

## Post #2 by @lassoan (2017-08-23 04:32 UTC)

<p>A post was merged into an existing topic: <a href="/t/query-worked-but-retrieve-didnt/928">Query worked but retrieve didn’t</a></p>

---

## Post #3 by @lassoan (2017-08-23 04:32 UTC)



---
