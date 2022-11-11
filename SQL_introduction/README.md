<h1>SQL - Introduction</h1>
<div class="panel-heading">
<h3 class="panel-title">Concepts</h3>
</div>
<div class="panel-body">
<p><em>For this project, we expect you to look at this concept:</em></p>
<ul>
<li><a href="https://intranet.hbtn.io/concepts/864">Databases</a></li>
</ul>
<h2>Resources</h2>
<p><strong>Read or watch</strong>:</p>
<ul>
<li><a title="What is Database &amp; SQL?" href="https://intranet.hbtn.io/rltoken/jRAhwW4u4YvZtLtMGU2_6g" target="_blank" rel="noopener">What is Database &amp; SQL?</a></li>
<li><a title="A Basic MySQL Tutorial" href="https://intranet.hbtn.io/rltoken/m_0RMf4RcC5NrHyjY1xN3w" target="_blank" rel="noopener">A Basic MySQL Tutorial</a></li>
<li><a title="Basic SQL statements: DDL and DML" href="https://intranet.hbtn.io/rltoken/-Qrnbp5eKmo7ajPDZekjfg" target="_blank" rel="noopener">Basic SQL statements: DDL and DML</a>&nbsp;(<em>no need to read the chapter &ldquo;Privileges&rdquo;</em>)</li>
<li><a title="Basic queries: SQL and RA" href="https://intranet.hbtn.io/rltoken/wXN5s1qexSTMh--NkTF1_w" target="_blank" rel="noopener">Basic queries: SQL and RA</a></li>
<li><a title="SQL technique: functions" href="https://intranet.hbtn.io/rltoken/7khGjnehvjHnqNZ9yizggg" target="_blank" rel="noopener">SQL technique: functions</a></li>
<li><a title="SQL technique: subqueries" href="https://intranet.hbtn.io/rltoken/xnJcopQTZyUke3LdAkOwow" target="_blank" rel="noopener">SQL technique: subqueries</a></li>
<li><a title="What makes the big difference between a backtick and an apostrophe?" href="https://intranet.hbtn.io/rltoken/QEr3XcBPhIR-E8NSSn1nzg" target="_blank" rel="noopener">What makes the big difference between a backtick and an apostrophe?</a></li>
<li><a title="MySQL Cheat Sheet" href="https://intranet.hbtn.io/rltoken/mNcGgvhZNG0dbFe23E-EjA" target="_blank" rel="noopener">MySQL Cheat Sheet</a></li>
<li><a title="MySQL 8.0 SQL Statement Syntax" href="https://intranet.hbtn.io/rltoken/ePNUeloWxfiXwec7HeKe7Q" target="_blank" rel="noopener">MySQL 8.0 SQL Statement Syntax</a></li>
</ul>
<h2>Learning Objectives</h2>
<p>At the end of this project, you are expected to be able to&nbsp;<a title="explain to anyone" href="https://intranet.hbtn.io/rltoken/6bUOgrGi5Yd_I65Jp9bAfg" target="_blank" rel="noopener">explain to anyone</a>,&nbsp;<strong>without the help of Google</strong>:</p>
<h3>General</h3>
<ul>
<li>What&rsquo;s a database</li>
<li>What&rsquo;s a relational database</li>
<li>What does SQL stand for</li>
<li>What&rsquo;s MySQL</li>
<li>How to create a database in MySQL</li>
<li>What does&nbsp;<code>DDL</code>&nbsp;and&nbsp;<code>DML</code>&nbsp;stand for</li>
<li>How to&nbsp;<code>CREATE</code>&nbsp;or&nbsp;<code>ALTER</code>&nbsp;a table</li>
<li>How to&nbsp;<code>SELECT</code>&nbsp;data from a table</li>
<li>How to&nbsp;<code>INSERT</code>,&nbsp;<code>UPDATE</code>&nbsp;or&nbsp;<code>DELETE</code>&nbsp;data</li>
<li>What are&nbsp;<code>subqueries</code></li>
<li>How to use MySQL functions</li>
</ul>
<h2>Requirements</h2>
<h3>General</h3>
<ul>
<li>Allowed editors:&nbsp;<code>vi</code>,&nbsp;<code>vim</code>,&nbsp;<code>emacs</code></li>
<li>All your files will be executed on Ubuntu 20.04 LTS using&nbsp;<code>MySQL 8.0</code>&nbsp;(version 8.0.25)</li>
<li>All your files should end with a new line</li>
<li>All your SQL queries should have a comment just before (i.e. syntax above)</li>
<li>All your files should start by a comment describing the task</li>
<li>All SQL keywords should be in uppercase (<code>SELECT</code>,&nbsp;<code>WHERE</code>&hellip;)</li>
<li>A&nbsp;<code>README.md</code>&nbsp;file, at the root of the folder of the project, is mandatory</li>
<li>The length of your files will be tested using&nbsp;<code>wc</code></li>
</ul>
<h2>More Info</h2>
<h3>Comments for your SQL file:</h3>
<pre><code>$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
</code></pre>
<h3>Install MySQL 8.0 on Ubuntu 20.04 LTS</h3>
<pre><code>$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$
</code></pre>
<p>Connect to your MySQL server:</p>
<pre><code>$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql&gt;
mysql&gt; quit
Bye
$
</code></pre>
</div>
