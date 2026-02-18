# Extensions Manager install

**Topic ID**: 37466
**Date**: 2024-07-19
**URL**: https://discourse.slicer.org/t/extensions-manager-install/37466

---

## Post #1 by @lirongyaoper (2024-07-19 05:29 UTC)

<p>Hello teacher, after I successfully installed 3D Slicer, I encountered a problem about “Extensions Manager install”.</p>
<ol>
<li>The operating system I use is “ubuntu 24.04”; the version of the 3D Slicer software I installed is “Slicer-5.7.0-2024-07-15-linux-amd64”.</li>
<li>When I install the relevant extension, the icon of the relevant extension cannot be loaded normally, and the download speed is extremely slow.</li>
<li>When returning to the “python console” interface, I found the following error message:<br>
[Qt] An OpenGL Core Profile was requested, but it is not supported on the current platform. Falling back to a non-Core profile. Note that this might cause rendering issues.<br>
[Qt] Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32947/linux" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://wiki.slicer.org/slicerWiki" rel="noopener nofollow ugc">http://wiki.slicer.org/slicerWiki</a> /images/f/f6/IntensitySegmenterIcon.png’. This content should also be served over HTTPS.<br>
[Qt] A cookie associated with a cross-site resource at <a href="http://www.nitrc.org/" rel="noopener nofollow ugc">http://www.nitrc.org/</a> was set without the <code>SameSite</code> attribute. A future release of Chrome will only deliver cookies with cross-site requests if they are set with <code>SameSite=None</code> and <code>Secure</code>. You can review cookies in developer tools under Application&gt;Storage&gt;Cookies and see more details at <a href="https://www.chromestatus.com/feature/5088147346030592" class="inline-onebox" rel="noopener nofollow ugc">Chrome Platform Status</a> and <a href="https://www.chromestatus" rel="noopener nofollow ugc">https://www.chromestatus</a> .com/feature/5633521622188032.</li>
</ol>
<p>I would like to understand the cause of this error and find the correct installation method.</p>
<p>Thanks, good luck, and looking forward to replying.</p>

---

## Post #2 by @lassoan (2024-07-19 23:26 UTC)

<p>Extension packages are quite small (few hundred kilobytes to a frw ten megabytes), so it should be possible to install over a very slow connection.</p>
<p>Most often extension downloads fail due to restrictions on institutional networks. Some security security suites use man-in-the-middle attacks to inspect internet traffic of each user, use heuristics to block certain network activities, or mess with SSL certificates. Do you connect to the internet directly or through an institutional firewall/proxy server?</p>

---

## Post #3 by @lirongyaoper (2024-07-20 03:36 UTC)

<p>I connect to the internet through proxy server。<br>
But when I used this network connection method (proxy server) to download and install Extension packages and pytorch applications, I never had such a problem. If I don’t use a proxy service to connect to the Internet, some applications cannot be installed.</p>

---
