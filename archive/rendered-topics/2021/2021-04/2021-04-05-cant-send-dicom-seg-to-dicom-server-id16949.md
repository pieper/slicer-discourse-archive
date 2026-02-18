# Can't Send DICOM SEG to DICOM Server

**Topic ID**: 16949
**Date**: 2021-04-05
**URL**: https://discourse.slicer.org/t/cant-send-dicom-seg-to-dicom-server/16949

---

## Post #1 by @twloehfelm (2021-04-05 15:42 UTC)

<p>OS: MacOS Big Sur 11.2.3<br>
Slicer: 4.11.20210226<br>
Extensions: DCMQI, PETDICOMExtension, QuantitativeReporting, SlicerDevelopmentToolbox</p>
<p>I am hoping to reach the following workflow:</p>
<ul>
<li>Query/Retrieve DICOM and DICOM SEG objects into Slicer</li>
<li>clean up the segmentations</li>
<li>Export them as DICOM and DICOM SEG to a remote DICOM receiver</li>
</ul>
<p>Everything works except exporting to the DICOM receiver.</p>
<p>The error I get is:<br>
<code>DICOM sending failed: Could not send /{path}/03_Base Ax/liverseg.dcm to localhost:11113</code></p>
<p>The DCMTK storescu function that Slicer uses does not support the Segmentation Storage SOP Class: <a href="https://support.dcmtk.org/docs/storescu.html" class="inline-onebox" rel="noopener nofollow ugc">DCMTK: storescu: DICOM storage (C-STORE) SCU</a>.</p>
<p>I can see that Segmentation Storage abstract syntax is not part of the association negotiation between Slicer the the receiver.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/3068487881bf942e0345c128998807b471e43eb6.png" data-download-href="/uploads/short-url/6UelkBf1Bem2fYYn2ibYmxxxoNg.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/3068487881bf942e0345c128998807b471e43eb6.png" alt="image" data-base62-sha1="6UelkBf1Bem2fYYn2ibYmxxxoNg" width="535" height="500" data-dominant-color="5B3834"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1066×996 75.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Is there an alternative was I can DICOM send from from Slicer? The Segmentation SOP Class <strong>is</strong> supported by the DICOM Networking Query/Retrieve function of Slicer, just not the Export function.</p>

---

## Post #2 by @pieper (2021-04-05 18:42 UTC)

<p>Interesting - thanks for the debugging info.  This sounds like a reasonable use case and we’d like to see it supported.</p>
<p>I don’t know why SEG is not be supported.  Probably it’s just a legacy list of SOP classes that hasn’t been updated.  Probably we can implement a change in Slicer’s dcmtk build, but this seems like maybe something the dcmtk team would want to fix.  <a class="mention" href="/u/fedorov">@fedorov</a> do you have any thoughts on this?</p>

---

## Post #3 by @fedorov (2021-04-05 19:30 UTC)

<p><a class="mention" href="/u/twloehfelm">@twloehfelm</a> did you try asking on the DCMTK forum? <a href="https://forum.dcmtk.org/">https://forum.dcmtk.org/</a></p>

---

## Post #4 by @twloehfelm (2021-04-05 19:53 UTC)

<p>Thanks for the suggestion <a class="mention" href="/u/fedorov">@fedorov</a>. I tried just now but that forum is restricted to registered users, and the registration process requires emailing the team - I’ve sent the email and will post there once I have an account.</p>

---

## Post #5 by @twloehfelm (2021-04-06 06:25 UTC)

<p>An alternative to changing DCMTK (no luck getting on the forum yet) - can pynetdicom be included as a core python package? That would enable using this more up-to-date package for scripting and extensions in Slicer.</p>

---

## Post #6 by @pieper (2021-04-06 13:10 UTC)

<p>I have not tried pynetdicom myself, do you know if it’s reached the level of maturity to work reliably?  It would be good if you could try <code>pip_install("pynetdicom")</code> and see if the example code works for your use case.</p>

---

## Post #7 by @lassoan (2021-04-06 13:20 UTC)

<p>You can also use the DICOMweb extension to push segmentation objects to any server that supports DICOMweb protocol. (I’ve tested it and it works well.)</p>

---

## Post #8 by @pieper (2021-04-06 17:32 UTC)

<p>Also <a class="mention" href="/u/lassoan">@lassoan</a> suggested there’s probably a way to configure <code>storescu</code> to work with SEG if you provide a config file with the <code>--config-file</code> flag.</p>

---

## Post #9 by @twloehfelm (2021-04-07 06:38 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a>: I’d say pynetdicom is as mature as pydicom and closely related to it. The documentation is excellent, the code actively maintained, and a good release cycle.</p>
<p>The least destructive way I can see to add basic pynetdicom c_store support is to:</p>
<ul>
<li>Change line 41 of Modules &gt; Scripted &gt; DICOMLib &gt; DICOMSendDialog.py to:</li>
</ul>
<pre><code class="lang-auto">self.protocolSelectorCombobox.addItems(["DIMSE","DICOMweb", "pynetdicom"])
</code></pre>
<ul>
<li>Insert the following after line 388 of Modules &gt; Scripted &gt; DICOMLib &gt; DICOMProcesses.py (i.e. in the send function of the DICOMSender class as an additional protocol selection choice):</li>
</ul>
<pre><code class="lang-auto">    elif self.protocol == "pynetdicom":
      # PYNETDICOM
      try:
        import pynetdicom
      except ModuleNotFoundError:
        logging.info("Installing pynetdicom for sending DICOM")
        pip_install('pynetdicom')
      from pydicom import dcmread
      from pynetdicom import (AE, StoragePresentationContexts)
      remoteAE = AE()
      remoteAE.requested_contexts = StoragePresentationContexts
      assoc = remoteAE.associate(self.destinationUrl.host(), self.destinationUrl.port())
      if not assoc.is_established:
        raise UserWarning('Could not establish SCU association')
      for file in self.files:
        if not self.progressCallback("Sending %s to %s using %s" % (file, self.destinationUrl.toString(), self.protocol)):
          raise UserWarning("Sending was cancelled, upload is incomplete.")
        ds = dcmread(file)
        assoc.send_c_store(ds)
        assoc.release()  # Release after the for loop cycles through all of the files
        remoteAE.shutdown()
</code></pre>
<p>Alternatively the contents of the pynetdicom elif block could simply replace the contents of the “DIMSE” else block and the original selector of “DIMSE”, “DICOMWeb” could remain unchanged.</p>
<p><a href="https://pydicom.github.io/pynetdicom/dev/reference/generated/pynetdicom.presentation.StoragePresentationContexts.html" rel="noopener nofollow ugc">StoragePresentationContexts</a> is a prebuilt list of presentation contexts for the first 128 SOP classes, including SegmentationStorage and confers to the AE the ability to negotiate storage of objects of those classes.</p>
<p>dcmtk store_scu only supports 64 SOP classes without the optional config file suggested above.</p>
<p>I don’t have a Slicer dev environment set up nor the developer chops to do it, but am happy to send the modified DICOMProcesses.py and DICOMSendDIalog.py to any willing devs.</p>

---

## Post #10 by @pieper (2021-04-07 13:53 UTC)

<p>That’s a pretty slick solution <a class="mention" href="/u/twloehfelm">@twloehfelm</a> <img src="https://emoji.discourse-cdn.com/twitter/clap.png?v=9" title=":clap:" class="emoji" alt=":clap:"></p>
<p>If we want to go the pynetdicom route we may rather install it at build time to avoid embedding the pip_install into the module logic.</p>
<p>Probably also we should provide something like a tooltip or other indication to future users about why they might need to pick this option.  For that matter, we may wish to make pynetdicom the default if fixes this important use case.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/cpinter">@cpinter</a> or others, any thoughts on this?</p>
<p>I’ve personally trying to remove DIMSE from my life, but I guess not everyone has that freedom.</p>

---

## Post #11 by @lassoan (2021-04-07 15:17 UTC)

<p>It is good to see that DICOM push is so simple to implement with pynetdicom. Although it is a quick fix to this specific issue, I would mostly consider it as a lateral step that not really moves things towards where we want to go. A better solution would be to create a DICOM conformance statement for Slicer and put its content to a configuration file (either for dcmtk or pynetdicom).</p>
<p>In the long term, we would need to implement DICOM sending in the background and add a queue manager in the GUI to be able to monitor the progress, cancel tasks, etc. If sending is done in a separate process then DCMTK and pynetdicom are about equally suitable for the job. If we implement this in background threads in the main process then DCMTK has an advantage, as we can manage threads much more cleanly in C++. DCMTK has been around for many years and used, developed, and tested by many people, so I would expect it has a more complete feature set than pynetdicom (just look at the <a href="https://support.dcmtk.org/docs/storescu.html">DCMTK C-store SCU’s extensive list of options</a>).</p>
<p>The effort to properly add pynetdicom to the Slicer package seems comparable to adding a config file for DCMTK. DCMTK is also more mature and better established. So, unless anything else comes up, I would lean towards just adding the config file now.</p>
<p>Overall, I feel the same as <a class="mention" href="/u/pieper">@pieper</a> that I tend to not use DIMSE in these years, because typically research applications do not get direct access to the hospital PACS and if a DICOM server or data sharing platform is set up for research, then that does not use DIMSE networking but DICOMweb or other modern web-based protocols.</p>

---

## Post #12 by @pieper (2021-04-07 15:46 UTC)

<p><a class="mention" href="/u/twloehfelm">@twloehfelm</a> did you look into the config file option?  I have never used it but <a href="https://book.orthanc-server.com/faq/dcmtk-tricks.html">this page</a> seems to describe pretty much the same scenario.</p>

---

## Post #13 by @twloehfelm (2021-04-07 16:15 UTC)

<p>Thank you <a class="mention" href="/u/pieper">@pieper</a> - I can see how to use the config file outside of Slicer but am not clear how I would add the dcmtk config file within Slicer.</p>
<p>To be clearer about my use case, I don’t need options for sending the DICOM objects outside of Slicer - I can handle that just fine with a number of other tools.</p>
<p>I am specifically looking for a way to solve it on the Slicer platform, because if Slicer could easily transact SEG objects that would enable me to host a set of studies on a Staging server, recruit users to pull studies from there, segment in Slicer, and push them back to a Completed server - achieving an entire distributed pure DICOM segmentation pipeline.</p>
<p>DICOMWeb is a possibility - I would have to change the Staging and Completed servers I am currently using (currently based on pynetdicom as it is just as easy to stand up a SCP as the SCU in the example I included above).</p>

---

## Post #14 by @pieper (2021-04-07 18:38 UTC)

<p>Thanks for the extra context <a class="mention" href="/u/twloehfelm">@twloehfelm</a> .   <a class="mention" href="/u/lassoan">@lassoan</a> and I are thinking that there could be a config file bundled as a resource as part of slicer that would include all the SOP classes that Slicer is able to generate so that <code>storescu</code> would propose them at negotiation time.  It would be a pretty small change, maybe even simpler than your <code>pynetdicom</code> implementation since it would be just one file and a command line option.</p>
<p>Regarding the option of DICOMweb servers, it seems like <a href="https://www.dcm4che.org/">dcm4chee</a> could be a good option for you.  It’s been heavily tested and is known to be robust and scalable for both DIMSE and DICOMweb.</p>

---

## Post #15 by @twloehfelm (2021-04-07 19:26 UTC)

<p>The dcmtk config file option seems like it should do the trick too and I really like <a class="mention" href="/u/lassoan">@lassoan</a> direction of a formal DICOM conformance statement for Slicer and appropriate config files for dcmtk.</p>
<p>FWIW - I didn’t realize I could simply swap out the .py files in my Slicer app Package Contents (macOS). I’ve done that now and tested the pynetdicom solution I proposed earlier and it works great! I agree that it is a lateral move and may not be in keeping with the long term goals of Slicer, and have full respect and deference to you all as the designers and stewards of the application. Thanks for all that you do.</p>

---

## Post #16 by @lassoan (2021-04-07 19:48 UTC)

<blockquote>
<p>I am specifically looking for a way to solve it on the Slicer platform, because if Slicer could easily transact SEG objects that would enable me to host a set of studies on a Staging server, recruit users to pull studies from there, segment in Slicer, and push them back to a Completed server - achieving an entire distributed pure DICOM segmentation pipeline.</p>
</blockquote>
<p>This is becoming an increasingly common use case and I think DICOMweb already provides more tools and flexibility than DIMSE.</p>
<p>DICOMweb browser module in Slicer (provided by DICOMwebBrowser extension) is better than the DIMSE Query/Retrieve feature of the DICOM module and there are more research tools, servers, and viewers that use DICOMweb. <a class="mention" href="/u/pieper">@pieper</a> already mentioned dcm4che, but there is also the very lightweight <a href="https://github.com/dcmjs-org/dicomweb-server">dcmjs DICOMweb server</a>, <a href="https://docs.ohif.org/">OHIF viewer</a>, <a href="https://kheops.online/">Kheops</a> (“dropbox” for DICOM), which all work great together.</p>
<p>For example, if you install very latest Slicer Preview Release on Windows then you can click on the Slicer icon in Kheops in your browser and it launches Slicer automatically and loads that study (downloads it automatically from Kheops via DICOMweb and imports to the database). We have not implemented automatic upload of data back to the server, but it should not be hard (it already works manually, by specifying the same access token as Slicer got for downloading the data).</p>

---

## Post #17 by @twloehfelm (2021-04-08 00:05 UTC)

<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a> - Kheops looks amazing and I will definitely check it out.</p>
<p>I do hope you will still consider adding the dcmtk config file to Slicer to patch the existing dimse sender - she may not look like much but she’s got it where it counts! There’s still a place for the old basic sender and receiver!</p>
<p>There’s a sample <a href="https://github.com/InsightSoftwareConsortium/DCMTK/blob/master/dcmnet/etc/storescu.cfg" rel="noopener nofollow ugc">storescu.cfg</a> file from dcmtk that seems like it would be a good place to start - line 265 especially should be added to the list <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=9" title=":wink:" class="emoji" alt=":wink:"></p>

---
