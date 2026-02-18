# Problem with sequentiality when using loops

**Topic ID**: 27127
**Date**: 2023-01-09
**URL**: https://discourse.slicer.org/t/problem-with-sequentiality-when-using-loops/27127

---

## Post #1 by @laurabc (2023-01-09 13:12 UTC)

<p>Dear community,</p>
<p>I am working in a python script to load 4D images and then repeat the same operations in each time volume. Therefore, my script includes first the loading instructions and then a for loop. I am having trouble with the loop, as it is being executed before the images are completely loaded. If I remove the loop and perform the operations for one only volume, the loop is executed after loading the images, as desired.<br>
How can I solve this? I mean, how can I guarantee that the for loop is executed once the images are completely loaded?</p>
<p>(I am using Slicer 5.2.1 in linux.)</p>
<p>Regards,<br>
Laura</p>

---

## Post #2 by @pieper (2023-01-09 15:38 UTC)

<p>It would help if you could provide a short script that demonstrates the calls you are using.  Even better would be an example that replicates the issue using public data (e.g. from the SampleData module).</p>

---

## Post #4 by @pieper (2023-01-10 18:36 UTC)

<p>Thanks for posting the code.  It looks like the issue here is just that you need <code>range(n_time_volumes)</code> with the parentheses : )</p>

---

## Post #5 by @laurabc (2023-01-11 08:25 UTC)

<p>Thank you, I don’t know how I missed that, I’m so embarrased <img src="https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=12" title=":sweat_smile:" class="emoji" alt=":sweat_smile:" loading="lazy" width="20" height="20"></p>

---
