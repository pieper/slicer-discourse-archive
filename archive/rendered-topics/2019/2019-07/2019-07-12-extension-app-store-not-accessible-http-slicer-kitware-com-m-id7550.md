# Extension app store not accessible (http://slicer.kitware.com/midas3/slicerappstore)

**Topic ID**: 7550
**Date**: 2019-07-12
**URL**: https://discourse.slicer.org/t/extension-app-store-not-accessible-http-slicer-kitware-com-midas3-slicerappstore/7550

---

## Post #1 by @dittothat (2019-07-12 15:28 UTC)

<p><a href="http://slicer.kitware.com/midas3/slicerappstore" rel="nofollow noopener">http://slicer.kitware.com/midas3/slicerappstore</a> is not accessible to me by multiple methods (multiple computers, networks, browsers). I need this to manually install an extension.</p>
<p>After a long wait in Chrome:</p>
<h1>This Page Cannot Be Displayed</h1>
<p>The system cannot communicate with the external server ( <a href="http://slicer.kitware.com" rel="nofollow noopener">slicer.kitware.com</a> ). The Internet server may be busy, may be permanently down, or may be unreachable because of network problems.</p>
<p>Please check the spelling of the Internet address entered. If it is correct, try this request later.</p>
<p>If you have questions, please contact your organization’s network administrator and provide the codes shown below.</p>
<p>Date: Fri, 12 Jul 2019 15:02:13 GMT<br>
Username:<br>
Source IP: 10.72.76.203<br>
URL: GET <a href="http://slicer.kitware.com/midas3/slicerappstore" rel="nofollow noopener">http://slicer.kitware.com/midas3/slicerappstore</a><br>
Category: Computers and Internet<br>
Reason: UNKNOWN<br>
Notification: GATEWAY_TIMEOUT</p>

---

## Post #2 by @jcfr (2019-07-12 15:41 UTC)

<p>Short answer: Use this link and enter relevant information. See <a href="http://slicer.kitware.com/midas3/slicerappstore/?os=win&amp;arch=amd64&amp;revision=&amp;search=&amp;layout=layout" rel="nofollow noopener">http://slicer.kitware.com/midas3/slicerappstore/?os=win&amp;arch=amd64&amp;revision=&amp;search=&amp;layout=layout</a></p>
<p>Long answer:</p>
<ul>
<li>The landing page is trying to find the most recent Slicer revision … but this is not done efficiently.</li>
<li>We have plan to modernize the infrastructure and address issue like the one you reported. See <a href="https://www.slicer.org/wiki/Documentation/Labs/ExtensionsServer" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Labs/ExtensionsServer</a>
</li>
</ul>

---

## Post #3 by @dittothat (2019-07-12 15:45 UTC)

<p>That new link is golden. Thanks.</p>

---
