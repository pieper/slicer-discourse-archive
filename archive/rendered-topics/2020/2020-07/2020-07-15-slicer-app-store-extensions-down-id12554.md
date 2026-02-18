# Slicer App Store (extensions) down?

**Topic ID**: 12554
**Date**: 2020-07-15
**URL**: https://discourse.slicer.org/t/slicer-app-store-extensions-down/12554

---

## Post #1 by @hherhold (2020-07-15 13:53 UTC)

<p>I get the following error when I try to go to <a href="http://slicer.kitware.com/midas3/slicerappstore" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a></p>
<p>The system has encountered the following error:</p>
<h3><a name="p-43507-uncaught-exception-pdoexception-with-message-sqlstatehy000-1040-too-many-connections-in-projectssrcmidas3libraryzenddbadapterpdoabstractphp129-stack-trace-0-projectssrcmidas3libraryzenddbadapterpdoabstractphp129-pdo-__constructmysqldbnamemi-midas-midapa-array-1-projectssrcmidas3libraryzenddbadapterpdomysqlphp111-zend_db_adapter_pdo_abstract-_connect-2-projectssrcmidas3libraryzenddbadapterabstractphp460-zend_db_adapter_pdo_mysql-_connect-3-projectssrcmidas3libraryzenddbadapterpdoabstractphp238-zend_db_adapter_abstract-queryinsert-into-er-array-4-projectssrcmidas3libraryzenddbadapterabstractphp576-zend_db_adapter_pdo_abstract-queryinsert-into-er-array-5-projectssrcmidas3libraryzendlogwriterdbphp145-zend_db_adapter_abstract-inserterrorlog-array-6-projectssrcmidas3libraryzendlogwriterabstractphp85-zend_log_writer_db-_writearray-7-projectssrcmi-1" class="anchor" href="#p-43507-uncaught-exception-pdoexception-with-message-sqlstatehy000-1040-too-many-connections-in-projectssrcmidas3libraryzenddbadapterpdoabstractphp129-stack-trace-0-projectssrcmidas3libraryzenddbadapterpdoabstractphp129-pdo-__constructmysqldbnamemi-midas-midapa-array-1-projectssrcmidas3libraryzenddbadapterpdomysqlphp111-zend_db_adapter_pdo_abstract-_connect-2-projectssrcmidas3libraryzenddbadapterabstractphp460-zend_db_adapter_pdo_mysql-_connect-3-projectssrcmidas3libraryzenddbadapterpdoabstractphp238-zend_db_adapter_abstract-queryinsert-into-er-array-4-projectssrcmidas3libraryzenddbadapterabstractphp576-zend_db_adapter_pdo_abstract-queryinsert-into-er-array-5-projectssrcmidas3libraryzendlogwriterdbphp145-zend_db_adapter_abstract-inserterrorlog-array-6-projectssrcmidas3libraryzendlogwriterabstractphp85-zend_log_writer_db-_writearray-7-projectssrcmi-1" aria-label="Heading link"></a>Uncaught exception ‘PDOException’ with message ‘SQLSTATE[HY000] [1040] Too many connections’ in /projects/src/Midas3/library/Zend/Db/Adapter/Pdo/Abstract.php:129 Stack trace: <span class="hashtag-raw">#0</span> /projects/src/Midas3/library/Zend/Db/Adapter/Pdo/Abstract.php(129): PDO-&gt;__construct(‘mysql:dbname=mi…’, ‘midas’, ‘mida$pa$$’, Array) <span class="hashtag-raw">#1</span> /projects/src/Midas3/library/Zend/Db/Adapter/Pdo/Mysql.php(111): Zend_Db_Adapter_Pdo_Abstract-&gt;_connect() <span class="hashtag-raw">#2</span> /projects/src/Midas3/library/Zend/Db/Adapter/Abstract.php(460): Zend_Db_Adapter_Pdo_Mysql-&gt;_connect() <span class="hashtag-raw">#3</span> /projects/src/Midas3/library/Zend/Db/Adapter/Pdo/Abstract.php(238): Zend_Db_Adapter_Abstract-&gt;query(‘INSERT INTO <code>er...', Array) #4 /projects/src/Midas3/library/Zend/Db/Adapter/Abstract.php(576): Zend_Db_Adapter_Pdo_Abstract-&gt;query('INSERT INTO </code>er…’, Array) <span class="hashtag-raw">#5</span> /projects/src/Midas3/library/Zend/Log/Writer/Db.php(145): Zend_Db_Adapter_Abstract-&gt;insert(‘errorlog’, Array) <span class="hashtag-raw">#6</span> /projects/src/Midas3/library/Zend/Log/Writer/Abstract.php(85): Zend_Log_Writer_Db-&gt;_write(Array) <span class="hashtag-raw">#7</span> /projects/src/Mi</h3>
<p>In /projects/src/Midas3/library/Zend/Controller/Plugin/Broker.php, line: 336<br>
At 09:50:25 2020-07-15</p>
<p>Please notify your administrator with this information.</p>

---

## Post #2 by @jcfr (2020-07-15 14:51 UTC)

<p>To follow up on this (reported as issue <a href="https://github.com/Slicer/Slicer/issues/5022">#5022</a>),  we are actively working on finalizing the new infrastructure, more details are available <a href="https://www.slicer.org/wiki/Documentation/Labs/ExtensionsServer#Status">here</a>.</p>
<blockquote>
<p>The system has encountered the following error:</p>
</blockquote>
<p>See <a href="https://github.com/Slicer/Slicer/issues/5022#issuecomment-658802377">this comment</a></p>

---

## Post #3 by @hherhold (2020-07-15 17:18 UTC)

<p>Got it, I didn’t realize these were directly related.</p>
<p>Thanks JC! Hope you are well.</p>
<p>-Hollister</p>

---
