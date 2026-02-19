---
topic_id: 35111
title: "Should Slicer Dicom Storage Listener Respond To C Echo"
date: 2024-03-27
url: https://discourse.slicer.org/t/35111
---

# Should Slicer DICOM storage listener respond to C-ECHO?

**Topic ID**: 35111
**Date**: 2024-03-27
**URL**: https://discourse.slicer.org/t/should-slicer-dicom-storage-listener-respond-to-c-echo/35111

---

## Post #1 by @mikebind (2024-03-27 00:08 UTC)

<p>Could someone verify whether a Slicer DICOM storage listener should respond to a C-ECHO request?  When I try, I do not get a response, instead it immediately aborts (A-ABORT with Abort Source: service-user).</p>
<pre><code class="lang-auto"># Minimal C-ECHO test
from pynetdicom import AE, debug_logger  
debug_logger() # make logging messages verbose
storage_addr = "127.0.0.1" # localhost
storage_port = 11112 # port slicer dicom storage listener is on
ae = AE()  
ae.add_requested_context("1.2.840.10008.1.1")  # echo verification context
assoc = ae.associate(storage_addr, storage_port)
if assoc.is_established:
    print('Association successful')
    status = assoc.send_c_echo()
    assoc.release()
else:
    print('Association failed!')
</code></pre>
<p>In various guides around the internet, getting a successful C-ECHO response is the first step in troubleshooting because the requirements are minimal (e.g. no search parameters, just a successfully open communication channel), so I expected this to work.  In this case, the successful association suggests that the communication channel is open, but the C-ECHO request somehow triggers the connection aborting.  There is an idle network timeout which can also trigger a connection abort, but this happens much faster than that 60 second timeout.</p>
<p>For background, I am working with <a class="mention" href="/u/ezgimercan">@ezgimercan</a> and our hospital networking team to get DICOM networking communication from Slicer working.  Configuration has proceeded to the point that we are able to successfully query the clinical PACS, but retrieval fails (we get a “Success” message, but 0 images/files are transferred).  I am trying to figure out exactly where the breakdown is occurring. Using pynetdicom and verbose logging, I can see that association is successful, but sub-operations are failing.</p>
<p>Also, for reference, the same code above with the remote PACS IP address and port works returns a success status to the send_c_echo() call and does not abort.  Using an incorrect IP address yields a TCP connection error (as expected), and using an incorrect port yields a TCP connection actively refused error (as expected).  Both of those results are distinct from the results for the local Slicer storage listener (and for the clinical PACS).</p>
<p>I would appreciate any help or suggestions anyone can offer.<br>
Following the very helpful troubleshooting guide at <a href="https://github.com/pydicom/pynetdicom/issues/419" class="inline-onebox" rel="noopener nofollow ugc">Troubleshooting Query/Retrieve SCU **Start Here** · Issue #419 · pydicom/pynetdicom · GitHub</a>, one of the steps is to verify that connecting to the storage provider (SCP), the one running from Slicer, is working.  The simplest check is to send a C-ECHO and make sure that it responds.  However, when I try this, the communication aborts (A-ABORT with Abort Source: service-user).  This seems very odd to me because there are no errors shown in the association process (Verification SOP Class is accepted), only when the C-ECHO is sent.  Also, to be clear, the listener I am testing here is the Slicer DICOM storage listener, not the clinical PACS; there is no communication off of the local machine in this test.</p>
<p>The full verbose log of the association, request, and abort from running the code above in Slicer’s python interactor:</p>
<aside class="onebox githubgist" data-onebox-src="https://gist.github.com/mikebind/883ff050961c78ce0fe552b3f62407fb">
  <header class="source">

      <a href="https://gist.github.com/mikebind/883ff050961c78ce0fe552b3f62407fb" target="_blank" rel="noopener nofollow ugc">gist.github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://gist.github.com/mikebind/883ff050961c78ce0fe552b3f62407fb" target="_blank" rel="noopener nofollow ugc">https://gist.github.com/mikebind/883ff050961c78ce0fe552b3f62407fb</a></h4>

  <h5>Failed_C-ECHO.txt</h5>
  <pre><code class="Text">I: Requesting Association
I: Association Accepted
Association successful
I: Sending Echo Request: MsgID 1
I: Releasing Association
I: Association Aborted
D: Request Parameters:
D: ======================= OUTGOING A-ASSOCIATE-RQ PDU ========================
D: Our Implementation Class UID:      1.2.826.0.1.3680043.9.3811.2.0.2
D: Our Implementation Version Name:   PYNETDICOM_202</code></pre>
   This file has been truncated. <a href="https://gist.github.com/mikebind/883ff050961c78ce0fe552b3f62407fb" target="_blank" rel="noopener nofollow ugc">show original</a>

<p>
</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #2 by @pieper (2024-03-27 15:08 UTC)

<p>The traditional storage provider (listener) in the Slicer release is implemented using <a href="https://support.dcmtk.org/docs/storescp.html">dcmtk’s storescp</a> and yes, it responds to echo for me:</p>
<pre><code class="lang-auto">$ echoscu -v localhost 11112
I: Requesting Association
I: Association Accepted (Max Send PDV: 16372)
I: Sending Echo Request (MsgID 1)
I: Received Echo Response (Success)
I: Releasing Association
</code></pre>
<p>If you use <code>ps</code> on linux I can see the listener running with these arguments.  You can just run the same or similar commands outside of Slicer for debugging.</p>
<pre><code class="lang-auto">.../Slicer-5.5.0-2023-11-15-linux-amd64/bin/../bin/storescp 11112 --accept-all --output-directory /mnt/timc-batch2/data/db2/incoming --exec-sync --exec-on-reception /mnt/timc-batch2/Slicer-5.5.0-2023-11-15-linux-amd64/bin/../bin/dcmdump --load-short --print-short --print-filename --search PatientName "/mnt/timc-batch2/data/db2/incoming/#f"
</code></pre>
<p>You could try <a href="https://support.dcmtk.org/docs/echoscu.html">echoscu</a> like this from localhost or from a different machine to see if the ports are working.</p>
<p>If pynetdicom had existed when Slicer’s dicom networking was implemented we might have used that, but it’s also kind of nice that these kind of connection issues can be debugged independently with just the command line tools, and also using the separate process makes it event driven (networking doesn’t block the UI).  I see that pynetdicom also provides a way to run it’s <a href="https://pydicom.github.io/pynetdicom/stable/apps/storescp.html">storescp as a command</a> line tool so that might help for testing.  It should also be possible to install pynetdicom directly in Slicer’s python.</p>
<p>Things may be different too with the new <a href="https://discourse.slicer.org/t/new-feature-visual-dicom-browser/33874">dicom browser</a> that’s available in the Preview version of Slicer.</p>
<p>Good luck - debugging these dimse connections can be a pain so ask follow-ups as needed and report back what you find so it will help others in the future.</p>

---

## Post #3 by @Davide_Punzo (2024-03-28 09:27 UTC)

<p>If you are using Slicer preview you can use the new class in ctk (<code>ctkDICOMEcho</code>) that I have introduced for C-ECHO (which uses directly <code>DcmSCU</code> from <code>DCMTK</code>). You can use it directly from the Slicer python console as:</p>
<pre><code class="lang-auto">import ctk
echoer = ctk.ctkDICOMEcho()
echoer.host = "localhost"
echoer.calledAETitle = "CTKSTORE"
echoer.port = 11112
echoer.echo()
</code></pre>
<p>I have tested it and it works for me, both using the DICOM module storage listener (Python implementation) and the visual DICOM browser one (C++ implementation):</p>
<ul>
<li>visual DICOM browser</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/33b821231ef53f96ad3c8194d7331ca1f42d4698.png" data-download-href="/uploads/short-url/7nwQtXrueMHkSRPYaESueBIDlbO.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33b821231ef53f96ad3c8194d7331ca1f42d4698_2_690x116.png" alt="image" data-base62-sha1="7nwQtXrueMHkSRPYaESueBIDlbO" width="690" height="116" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33b821231ef53f96ad3c8194d7331ca1f42d4698_2_690x116.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33b821231ef53f96ad3c8194d7331ca1f42d4698_2_1035x174.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33b821231ef53f96ad3c8194d7331ca1f42d4698_2_1380x232.png 2x" data-dominant-color="F7F7F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1843×312 21.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ul>
<li>DICOM module UI</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a3d8ff23f4fec2722c94639cc8843cb6e7130bf9.png" data-download-href="/uploads/short-url/nnsJVOcBCMANe4i6kIshonUgEnD.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a3d8ff23f4fec2722c94639cc8843cb6e7130bf9_2_690x88.png" alt="image" data-base62-sha1="nnsJVOcBCMANe4i6kIshonUgEnD" width="690" height="88" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a3d8ff23f4fec2722c94639cc8843cb6e7130bf9_2_690x88.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a3d8ff23f4fec2722c94639cc8843cb6e7130bf9_2_1035x132.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a3d8ff23f4fec2722c94639cc8843cb6e7130bf9_2_1380x176.png 2x" data-dominant-color="F5F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2485×317 47.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If you have any issue, please let us know.</p>

---

## Post #4 by @lassoan (2024-03-28 16:02 UTC)

<p>Most clinical PACS only supports C-MOVE and not C-GET, so the IP address of your computer must be set in the PACS configuration (you cannot retrieve from some random IP address; unless you use the proxy feature of the new DICOM browser). When you retrieve an image using C-MOVE you actually just ask the PACS to do a C-STORE sometime in the future. It is not a synchronous operation, so it is normal that the retrieve request returns with success but no files are transferred. Whenever it is convenient for the server, it will start a C-STORE and if that fails you may only see any errors in the PACS logs.</p>
<p>I would not bother with C-ECHO. Instead, I would test if you can successfully perform a DICOM push (C-STORE) initiated from the PACS. Once you configure C-STORE, C-MOVE will work correctly, too.</p>
<p>I would recommend using the new DICOM browser, it implements query/retrieve with a convenient user interface, thumbnails, etc. everything is done in the background (without blocking the application GUI), and C-STORE configuration is properly implemented (I think in the old version you had to set the AE title manually in the Slicer.ini file).</p>

---

## Post #5 by @mikebind (2024-03-28 16:22 UTC)

<p>Thanks <a class="mention" href="/u/pieper">@pieper</a>, using echoscu worked fine, so I’m not sure what was going wrong trying from pynetdicom.</p>

---

## Post #6 by @mikebind (2024-03-28 16:31 UTC)

<p>Thanks for the advice, I will try the approach you suggest of sending a C-STORE from the PACS.  I also now suspect that the PACS may not support C-GET, despite accepting association and accepting a GETStudyRootQueryRetrieveInformationModel as a presentation context.</p>
<p>Regarding the new DICOM browser, I was planning to try to work up to that by getting the basic connection working first with the older browser, on the assumption that some people had gotten the old version to work with clinical PACS, whereas I was not clear whether anyone had even tried yet with the new version.  The introduction of the new DICOM browser was the initial motivation for starting the process of trying to get the connection working, but I wasn’t sure how mature that code was.</p>

---

## Post #7 by @lassoan (2024-03-28 18:34 UTC)

<p>The new browser should be much more robust in query/retrieve from PACS. It is tested in hospital environment.</p>

---

## Post #8 by @Davide_Punzo (2024-03-28 20:23 UTC)

<p>We are also actively refining the UI/adding new features to the new browser.<br>
Your feedback would be very welcome too.</p>
<p>For reference, I link here the current <a href="https://github.com/commontk/CTK/issues/1162" rel="noopener nofollow ugc">roadmap</a>.</p>

---

## Post #9 by @mikebind (2024-04-16 18:10 UTC)

<p>Thanks for all the help and suggestions.  We now have DICOM Query and Retrieve working from Slicer as long as we are on a static IP address within the hospital network. I am typically operating over a VPN, so I am still exploring whether we can make that work also.</p>
<p>The most helpful avenue for troubleshooting was to try pushing from our PACS to the Slicer DICOM listener, as <a class="mention" href="/u/lassoan">@lassoan</a> suggested above.  That allowed our network team to identify the remaining barriers to communication.  Once that was working, initiating C-MOVE requests from Slicer was successful (achieved by unchecking the C-GET column in the DICOM Q/R dialog box).  We did not find the newer DICOM browser immediately helpful in troubleshooting, but do plan to explore using it in the future now that we have some basic communication verified.</p>

---

## Post #10 by @lassoan (2024-04-16 18:54 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="9" data-topic="35111">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>I am typically operating over a VPN, so I am still exploring whether we can make that work also.</p>
</blockquote>
</aside>
<p>The good news is that we have already implemented a solution for this in the new DICOM browser. All you need is to set up a proxy server that supports C-GET and ask IT admins to enable Query/Retrieve for it. In the DICOM configuration settings, you select this proxy server to be used by the hospital PACS.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4fcbea74f1aa6e4f948ade87ca8fed1474ec1442.png" data-download-href="/uploads/short-url/bnUBGAikK17SOoxxUmYjbZGlQAy.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4fcbea74f1aa6e4f948ade87ca8fed1474ec1442_2_690x99.png" alt="image" data-base62-sha1="bnUBGAikK17SOoxxUmYjbZGlQAy" width="690" height="99" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4fcbea74f1aa6e4f948ade87ca8fed1474ec1442_2_690x99.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4fcbea74f1aa6e4f948ade87ca8fed1474ec1442_2_1035x148.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4fcbea74f1aa6e4f948ade87ca8fed1474ec1442_2_1380x198.png 2x" data-dominant-color="2C3338"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">3792×548 96.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I would recommend using Orthanc as proxy, it is well established, free, very easy to set up on either Windows or Linux, either running natively or in docker.</p>
<p>How this works is that your laptop queries the hospital PACS for what images are available for the selected patient. If there are any images that are not already on your laptop then Slicer retrieves it from the proxy server (using C-GET, which works well with dynamic IP). If the image is not on the proxy server then Slicer asks the hospital PACS to send the image to the proxy server (using C-MOVE, which all hospital servers support) and then Slicer can retrieve the image from the proxy server. All this communication is performed automatically, seamlessly, in the background.</p>

---

## Post #11 by @mikebind (2024-04-16 19:14 UTC)

<p>Thanks for this idea.  Would the proxy server be set up on a machine inside the hospital network then?</p>

---

## Post #12 by @lassoan (2024-04-16 19:29 UTC)

<p>Yes, on any computer within the hospital network with a static IP address.</p>

---

## Post #13 by @ezgimercan (2024-04-19 21:16 UTC)

<p>Thanks for all the support troubleshooting our DICOM networking. I am reporting back with the most bizarre observation.</p>
<p>I have both the stable version (5.6.1) and preview version (5.7.0-2024-04-11) of Slicer. As <a class="mention" href="/u/mikebind">@mikebind</a> said above, we can query/retrieve using the old DICOM browser. With the preview/advanced version, I cannot query the same PACS. It says: “The query provided no results. Please refine your filters.” I can send DICOM from PACS to the preview OK, but things get interesting here: once one study of a patient is in the local DICOM database (through DICOM send), then the preview can query and retrieve ALL studies of the same patient. But not before the patient is in the database somehow.</p>
<p>We are perfectly happy using the old DICOM browser / python scripts to do our query/retrieve jobs. This is more out of curiosity, do you have an idea what’s happening here? How can I receive data, query other studies of the existing patients but cannot query other patients/studies on the PACS?</p>

---

## Post #14 by @lassoan (2024-04-20 00:08 UTC)

<p>There are a number of fixes and improvements for the new browser that will be integrated early next week. If you find any issues in the new browser after that then please report them and they will be fixed.</p>
<p>I dont think anybody will touch the old query/retrieve, it is just very slow and clunky and does not work in a usual research workflow in a hospital environment (the application is running in a docker container or on a laptop, so static IP is not an option).</p>

---
