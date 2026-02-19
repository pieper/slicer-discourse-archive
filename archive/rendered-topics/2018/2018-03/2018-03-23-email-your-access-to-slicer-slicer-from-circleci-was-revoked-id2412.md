---
topic_id: 2412
title: "Email Your Access To Slicer Slicer From Circleci Was Revoked"
date: 2018-03-23
url: https://discourse.slicer.org/t/2412
---

# Email: Your access to Slicer/Slicer from CircleCI was revoked by GitHub

**Topic ID**: 2412
**Date**: 2018-03-23
**URL**: https://discourse.slicer.org/t/email-your-access-to-slicer-slicer-from-circleci-was-revoked-by-github/2412

---

## Post #1 by @jcfr (2018-03-23 19:13 UTC)

<p>Thanks <a class="mention" href="/u/fbudin69500">@fbudin69500</a> for reporting the problem.</p>
<p>If you got an email with the same title, just to let you know that we contacted CircleCI support.</p>
<p>I will post update here.</p>
<p>It may be related to this but I will know more later. See <a href="https://circleci.com/docs/1.0/github-3rdparty-app-restrictions/">https://circleci.com/docs/1.0/github-3rdparty-app-restrictions/</a></p>

---

## Post #2 by @jcfr (2018-03-23 19:30 UTC)

<p>Update from CircleCI support:</p>
<aside class="quote no-group">
<blockquote>
<p>Thanks for writing in. We’re currently experiencing a service disruption, and we’re sorry for the trouble.</p>
<p>The issue is currently being worked on by our engineers and we will update our status page as soon as we know more:<br>
<a href="https://status.circleci.com/">https://status.circleci.com/</a></p>
</blockquote>
</aside>

---

## Post #3 by @jcfr (2018-03-24 01:47 UTC)

<p>Update from CircleCI:</p>
<aside class="quote no-group">
<blockquote>
<p>Earlier today we experienced an <a href="https://status.circleci.com/incidents/dsv8gn7gkq3z?mkt_tok=eyJpIjoiTldaaVkyRTNNbUZsWXpFNCIsInQiOiJiS2s3c0duNm9kYjQ1SmdHR3FpVjhGdzZRS0w0Mm5YSEl1dEk2RnNRcW03YzNaZDlobWNnZlwvVXoyemt4T2E0T3NlajhjbGVoYUpVM0hGQytyc2tQZms1Z1Jnd0pIWVF2eExxTHNKSVlWd0Z2RUZEUVowQWZSQTBSdkVnYkRCY3oifQ%3D%3D">issue</a> that caused your GitHub project access to be revoked. This was caused by a <a href="https://status.github.com/messages?mkt_tok=eyJpIjoiTldaaVkyRTNNbUZsWXpFNCIsInQiOiJiS2s3c0duNm9kYjQ1SmdHR3FpVjhGdzZRS0w0Mm5YSEl1dEk2RnNRcW03YzNaZDlobWNnZlwvVXoyemt4T2E0T3NlajhjbGVoYUpVM0hGQytyc2tQZms1Z1Jnd0pIWVF2eExxTHNKSVlWd0Z2RUZEUVowQWZSQTBSdkVnYkRCY3oifQ%3D%3D">regression in GitHub’s API</a> that resulted in the loss of access to your GitHub projects on CircleCI.</p>
<p>We apologize for the confusion and downtime this may have caused for you and your team.</p>
<p>What happened:</p>
<p>Around 5:00PM UTC, GitHub pushed a change to their API that incorrectly omitted the <code>permissions</code> field of certain endpoints. This caused us to revoke permissions for many users.</p>
<p>Around 7:00PM UTC, GitHub deployed a fix of their API. This resolved issues for most customers. However, as an effect of the false-negatives on permissions, some users remained without access to a subset of projects. This subsequently caused some builds to appear to revert to CircleCI 1.0 configurations.</p>
<p>At 8:15PM UTC, we started deploying a fix which ensured users who lost access and now properly had access would automatically resume following projects on CircleCI. This fixed further issues regarding visibility and access to certain projects.</p>
<p>At 8:45PM UTC, we communicated through StatusPage that if our fix had not deployed to you yet, that a manual workaround involving resetting your GitHub webhooks existed.</p>
<p>What we’re doing to prevent this in the future: We are currently setting up systems to help us more closely monitor for changes to GitHub’s API that can cause these types of issues. Revoking access for users where we no longer see permissions present is the correct action for security purposes. Moving forward, we will maintain our focus on the security of your projects while also looking for ways to be more robust in the face of upstream changes.</p>
<p>Steps you can take: If your project continues to not build as expected, have your organization’s GitHub administrator take the following actions:</p>
<ol>
<li>Remove all CircleCI webhooks and services from your GitHub repo settings.</li>
<li>Tell the project to stop building on CircleCI through “Project settings.”</li>
<li>Add the project back on CircleCI.</li>
</ol>
<p>Self-hosted CircleCI customers using <a href="http://github.com">github.com</a> were also impacted and can use the steps described above to remove and re-add projects for builds to resume.</p>
<p>If you have any additional questions, please don’t hesitate to reach out. You can reach our support team here.</p>
<p>Sincerely,</p>
<p>The CircleCI Team</p>
</blockquote>
</aside>

---
