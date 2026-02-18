# Using slicer behind proxy

**Topic ID**: 6545
**Date**: 2019-04-19
**URL**: https://discourse.slicer.org/t/using-slicer-behind-proxy/6545

---

## Post #1 by @muratmaga (2019-04-19 18:09 UTC)

<p>We are behind a corporate proxy, and more and more this creates issues with sample set downloads though slicer. E.g., this is the contents of the mrhead.nrrd when I use the sample data:<br>
This windows workstation is already configured to use specified proxy. Is there way to set this proxy explicitly from .slicerrc.py?</p>
<blockquote>
Proxy Server Use Required

<table>
<tbody><tr>
<td><b>Internet Access requires the use of a web proxy server.</b></td><td>
</td></tr>
</tbody></table>
<p>
Please configure your web browser to automatically detect web proxy settings.
<br>
For assistance, please refer to the <a>Proxy Configuration page</a>.
</p><p>
In some cases it may be necessary to re-apply the settings.  To do this in Internet Explorer, go in to 
Tools, Internet Options, Connections, LAN Settings.  Uncheck "Automatically detect settings", hit Ok, then go 
back in and re-check the box.
</p><p>
</p><p>
For additional questions, please contact Service Desk at x71111.

&lt;/HT</p></blockquote>

---

## Post #2 by @pieper (2019-04-20 15:21 UTC)

<p>Is your <code>http_proxy</code> environment variable set?  I’ve never had to use a proxy, but from what I can tell that’s <a href="https://docs.python.org/3.6/library/urllib.request.html" rel="nofollow noopener">what’s needed</a> so that the proxy would be used <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/SampleData/SampleData.py#L653" rel="nofollow noopener">in SampleData</a>.</p>

---

## Post #3 by @muratmaga (2019-04-21 05:42 UTC)

<p>I never had to set the http_proxy on windows boxes, only on Linux. But I can give it a try and report back.</p>

---

## Post #4 by @muratmaga (2019-04-22 16:23 UTC)

<p>Worked great. Thank you!</p>

---
