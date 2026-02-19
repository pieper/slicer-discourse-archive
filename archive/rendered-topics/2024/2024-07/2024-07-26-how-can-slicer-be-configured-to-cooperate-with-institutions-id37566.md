---
topic_id: 37566
title: "How Can Slicer Be Configured To Cooperate With Institutions"
date: 2024-07-26
url: https://discourse.slicer.org/t/37566
---

# How can Slicer be configured to cooperate with institutions that enforces SSL bumping and use self-signed certificates at the Firewall?

**Topic ID**: 37566
**Date**: 2024-07-26
**URL**: https://discourse.slicer.org/t/how-can-slicer-be-configured-to-cooperate-with-institutions-that-enforces-ssl-bumping-and-use-self-signed-certificates-at-the-firewall/37566

---

## Post #1 by @TL00104 (2024-07-26 04:22 UTC)

<p>How can Slicer be configured to cooperate with institutions that enforces SSL bumping and use self-signed certificates at the Firewall?</p>

---

## Post #2 by @lassoan (2024-07-26 04:28 UTC)

<p>This topic is discussed extensively here:</p>
<aside class="quote" data-post="31" data-topic="33809">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/sandbox-module-cannot-be-downloaded-via-extension-manager-today/33809/31">Sandbox module cannot be downloaded via extension manager today?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    At the time it was implemented, it was the simplest way to have certificates across all platform. The Slicer.crt is generated from the Mozilla certificates similarly to the ones distributed through <a href="https://github.com/certifi/python-certifi">python-certifi</a>. They are also automatically maintained up-to-date using the <a href="https://github.com/Slicer/Slicer/blob/main/.github/workflows/update-slicer-certificate-bundle.yml">update-slicer-certificate-bundle.yml</a> GitHub workflow. 
We could revisit this so that Python, CURL and Qt all use certificates when from the system store on platform supporting it.
  </blockquote>
</aside>


---

## Post #3 by @TL00104 (2024-08-01 16:44 UTC)

<p>A coworker that’s well versed in this language figured it out. Here’s what we had to do:</p>
<ol>
<li>Start slicer and open the extensions manager<br>
This created the folder <code>~/.pki/nssdb</code></li>
<li><code>cd</code> into <code>~/.pki/nssdb</code> and run:<br>
<code>certutil -d sql:. -A -n "File" -i "PathToCertificates/File.crt" -t "C,,"</code><br>
for each File in <code>PathToCertificates</code> (replace File in two places in the line above)<br>
This configures the root and intermediate SSL certificates for the Chromium browser that the extensions manager is built on</li>
<li><code>cd</code> into the folder that contains <code>Slicer.crt</code> (e.g. <code>share/Slicer-5.6</code>)</li>
</ol>
<pre><code class="lang-auto">mv Slicer.crt Slicer.crt.old  # make a backup of the original
ln -s PathToCaCertificates/ca-certificates.crt Slicer.crt
</code></pre>
<p>This effectively replaces <code>Slicer.crt</code> with the system certificate store that needs to be used so that Slicer will trust downloading extensions.<br>
4. <code>export REQUESTS_CA_BUNDLE="PathToCaCertificates/ca-certificates.crt"</code><br>
This will allow the Slicer Python environment to trust downloading Python packages.</p>

---

## Post #4 by @TL00104 (2024-08-01 20:10 UTC)

<p>not sure why “C,” (quote capital C comma comma end quote) rendered with only one comma</p>

---

## Post #5 by @lassoan (2024-08-02 10:10 UTC)

<p>Thank you for sharing. This was very useful information and can solve the certificate problem when certificates rarely change.</p>
<p>Unfortunately, ZScaler and similar aggressive cybersecurity tools may generate new temporary SSL certificates frequently (every couple of days or so) and you would need to repeat all the steps when it happens. Usually the final solution is that your IT staff adds exceptions. The exact steps IT takes are usually kept confidential, so there are unfortunately no common best practices to share beyond what is described in the topic I referenced above.</p>
<aside class="quote no-group" data-username="TL00104" data-post="4" data-topic="37566" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/e47c2d/48.png" class="avatar"> TL00104:</div>
<blockquote>
<p>not sure why “C,” (quote capital C comma comma end quote) rendered with only one comma</p>
</blockquote>
</aside>
<p>It is some markdown formatting. To print verbatim text, you can <a href="https://www.markdownguide.org/basic-syntax/#code">put them between backticks</a>.</p>

---
