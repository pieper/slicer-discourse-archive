# Slicer does not respond while working on a code and after finishing the loop prints everything

**Topic ID**: 22277
**Date**: 2022-03-03
**URL**: https://discourse.slicer.org/t/slicer-does-not-respond-while-working-on-a-code-and-after-finishing-the-loop-prints-everything/22277

---

## Post #1 by @S_Arbabi (2022-03-03 08:50 UTC)

<p>Hello all,</p>
<p>I implemented a function that reads the DICOM data from a source on web (by looping over the API’s of the web service) and writes them on disk if needed. In the code I wrote "print"s in each iteration of loop to know where the current state is and which image it is fetching.<br>
But once running the function, Slicer does not respond and print nothing (but works in the background with fetching folders to disk) and once everything is done it prints everything it was about to print from beginning.</p>
<p>I was wondering what is the issue, and can I do a workaround for that?</p>
<p>Best wishes,<br>
Saeed</p>

---

## Post #2 by @cpinter (2022-03-03 09:10 UTC)

<p>The issue is that the GUI does not update while this is being done. If you do <code>slicer.app.processEvents()</code> calls between the print statements, they will appear.</p>

---
