# Terminate DICOMRetrieve move/get following an event

**Topic ID**: 24639
**Date**: 2022-08-04
**URL**: https://discourse.slicer.org/t/terminate-dicomretrieve-move-get-following-an-event/24639

---

## Post #1 by @dvbower (2022-08-04 12:00 UTC)

<p>In a python script, I would like to terminate <code>ctk.ctkDICOMRetrieve.moveSeries(studyinstanceUID, seriesinstanceUID)</code> when an event is triggered.  In short, I can trigger the event within <code>slicer.dicomListener.fileAddedCallback</code>, but the question is then how to terminate the call to <code>moveSeries</code>.  Multiprocessing within slicer does not behave as expected (see <a href="https://discourse.slicer.org/t/inconsistent-handling-of-multiprocessing-by-slicer/24623/3" class="inline-onebox">Inconsistent handling of multiprocessing by slicer - #3 by dvbower</a>) and I’m trying to build on existing infrastructure provided in <code>DICOMLib</code> etc. to avoid re-inventing the wheel and also to minimise code maintenance.</p>
<p>I’ve dug around in the ctk library (<code>ctkDICOMRetrieve.cpp</code>) but I currently don’t fully understand the python wrapping well enough to know if it is possible to send a terminate command whilst a wrapped DICOM command is running.  DICOMRetrieve, DICOMQuery seem to be wrapping the cpp library directly, whereas the DICOMListener class lives in DICOM.py.  Thanks.</p>

---

## Post #2 by @pieper (2022-08-04 15:51 UTC)

<p>The dicom networking (dimse) support in CTK and Slicer only handle a set of common use cases and canceling a move never came up before that I know of.  The underlying dcmtk code has a <code>DcmSCU::sendCANCELRequest</code> method that could be added to the CTK code if your use case motivates you or anyone to dig in at that level.  Cancel was only implemented in CTK for CGET and CSTORE because in those cases the CTK code handles the full transaction whereas in CMOVE the transaction is initiated but then handled by the server.  The cancel operation would require keeping track of the context ID to issue the cancel request. There would need to be some details to work out but implementing the feature would be pretty mechanical. It would take a while to implement, test, update Slicer, etc.</p>
<p>You are correct that the listener is implemented differently for a few reasons.  For example, the <code>storescp</code> executable already provided all the needed functionality, the slicer integration could be done in python, and keeping the networking isolated in a separate process is more robust, easier to debug, and avoids blocking the application during network operations.</p>
<p>Another option might be for you to use CGET if you need to be able to cancel the operation.  It used to be that CMOVE was more universally supported but I believe CGET is pretty common these days.</p>
<p>Working with CMOVE, and dimse in general, is always a challenge, but it’s a robust standard that has held up well in the field so if you can work this out it should be reliable.  If you have flexibility in terms of the server you work with then you may prefer DICOMweb which is a lot easier for most programmers to work with.  If you describe your constraints maybe we can give more specific advice.</p>

---

## Post #3 by @dvbower (2022-08-05 07:59 UTC)

<p>Thanks Steve for the detailed response.  I will certainly look into these options for a long-term solution.  In the short-term, however, I’m wondering if I can simply raise a custom exception in <code>slicer.dicomListener.fileAddedCallback</code> to return programme control back to python <code>main</code>.  But I worry this might result in orphaned or zombie processes (associated with CMOVE) that won’t get cleared until the python script completes (exits).  Nevertheless, maybe this will suffice in the short-term.</p>

---

## Post #4 by @pieper (2022-08-05 12:42 UTC)

<p>I think the key problem is that a CMOVE request tells the dicom server to start a transfer operation and unless you tell it to cancel it may do multiple retries or otherwise get in a bad state if you stop the listener.  I suppose it would eventually time out and just log an error but that’s probably not preferred.  Maybe it’s easier to just let it send the data but ignore everything when it’s no longer useful to you.</p>
<p>I’m not clear on the control flow issues you mentioned since the process should be all be event-driven.</p>
<p>Can you describe a bit more about the scenario you are trying to support?</p>

---

## Post #5 by @dvbower (2022-08-05 12:50 UTC)

<p>The main objective is to only download one instance associated with a given Study ID and Series ID.  This is because the dicom metadata in any one instance will determine the next course of action (download all instances in that series, or skip that series, which I would perform as a separate loop once the single DICOM samples from each series have been interrogated with pydicom).</p>
<p>I had also thought about allowing C-MOVE to proceed but somehow mute the listener to avoid downloading any more files after the event has tripped.  I’m not sure how to do this elegantly though, without effectively forcing C-MOVE to error out (which seems to happen if I corrupt the listener attributes, which is not elegant, as you rightly point out).</p>

---

## Post #6 by @pieper (2022-08-05 13:25 UTC)

<p>Since you are doing custom programming anyway and need to make sure it works with the functions of the particular server you are using, maybe instead of using <code>ctkDICOMRetrieve</code> you could use <a href="https://support.dcmtk.org/docs/movescu.html"><code>movescu</code></a> directly to request a single instance.  Using these command line tools can help debug the basic operations and make it easier to implement a robust user interface in Slicer.</p>
<p>Regarding the control flow issues keep in mind that all of these networking operations are asynchronous and you may need to handle responses that come in any order.</p>

---
