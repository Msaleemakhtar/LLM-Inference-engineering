# 21. Introduction to Cache Memory

<p align="center">
  <b><a href="../20.%20Superscalar%20processors%20and%20GPU/README.md">⏪ PREVIOUS TOPIC</a></b> &nbsp; | &nbsp; <b><a href="../README.md">📚 MAIN MENU</a></b> &nbsp; | &nbsp; <b><a href="../22%3A%20Block%20Replacement%20Techniques%20%26%20Write%20Strategy/README.md">NEXT TOPIC ⏩</a></b>
</p>

---

![Screenshot From 2026-04-29 10-22-55.png](./Screenshot%20From%202026-04-29%2010-22-55.png)
![Screenshot From 2026-04-29 10-23-03.png](./Screenshot%20From%202026-04-29%2010-23-03.png)
![Screenshot From 2026-04-29 10-24-56.png](./Screenshot%20From%202026-04-29%2010-24-56.png)
![Screenshot From 2026-04-29 10-30-53.png](./Screenshot%20From%202026-04-29%2010-30-53.png)
![Screenshot From 2026-04-29 10-33-11.png](./Screenshot%20From%202026-04-29%2010-33-11.png)
![Screenshot From 2026-04-29 10-33-50.png](./Screenshot%20From%202026-04-29%2010-33-50.png)
![Screenshot From 2026-04-29 10-51-05.png](./Screenshot%20From%202026-04-29%2010-51-05.png)
![Screenshot From 2026-04-29 11-15-25.png](./Screenshot%20From%202026-04-29%2011-15-25.png)
![Screenshot From 2026-04-29 11-19-08.png](./Screenshot%20From%202026-04-29%2011-19-08.png)
![Screenshot From 2026-04-29 11-32-02.png](./Screenshot%20From%202026-04-29%2011-32-02.png)
![Screenshot From 2026-04-29 11-32-26.png](./Screenshot%20From%202026-04-29%2011-32-26.png)
![Screenshot From 2026-04-29 11-40-07.png](./Screenshot%20From%202026-04-29%2011-40-07.png)
![Screenshot From 2026-04-29 11-42-02.png](./Screenshot%20From%202026-04-29%2011-42-02.png)
![Screenshot From 2026-04-29 12-14-56.png](./Screenshot%20From%202026-04-29%2012-14-56.png)
![Screenshot From 2026-04-29 12-15-42.png](./Screenshot%20From%202026-04-29%2012-15-42.png)
![Screenshot From 2026-04-29 12-18-49.png](./Screenshot%20From%202026-04-29%2012-18-49.png)
![Screenshot From 2026-04-29 14-47-39.png](./Screenshot%20From%202026-04-29%2014-47-39.png)
![Screenshot From 2026-04-29 14-50-01.png](./Screenshot%20From%202026-04-29%2014-50-01.png)
![Screenshot From 2026-04-29 14-52-50.png](./Screenshot%20From%202026-04-29%2014-52-50.png)
![Screenshot From 2026-04-29 14-56-26.png](./Screenshot%20From%202026-04-29%2014-56-26.png)
![Screenshot From 2026-04-29 15-00-46.png](./Screenshot%20From%202026-04-29%2015-00-46.png)
![Screenshot From 2026-04-29 15-01-18.png](./Screenshot%20From%202026-04-29%2015-01-18.png)
![Screenshot From 2026-04-29 15-02-35.png](./Screenshot%20From%202026-04-29%2015-02-35.png)
![Screenshot From 2026-04-29 15-03-10.png](./Screenshot%20From%202026-04-29%2015-03-10.png)
![Screenshot From 2026-04-29 15-03-37.png](./Screenshot%20From%202026-04-29%2015-03-37.png)
![Screenshot From 2026-04-29 15-04-08.png](./Screenshot%20From%202026-04-29%2015-04-08.png)
![Screenshot From 2026-04-29 15-04-17.png](./Screenshot%20From%202026-04-29%2015-04-17.png)
![Screenshot From 2026-04-29 15-05-19.png](./Screenshot%20From%202026-04-29%2015-05-19.png)
![Screenshot From 2026-04-29 15-05-46.png](./Screenshot%20From%202026-04-29%2015-05-46.png)
![Screenshot From 2026-04-29 15-06-15.png](./Screenshot%20From%202026-04-29%2015-06-15.png)
![Screenshot From 2026-04-29 15-07-01.png](./Screenshot%20From%202026-04-29%2015-07-01.png)
![Screenshot From 2026-04-29 15-07-12.png](./Screenshot%20From%202026-04-29%2015-07-12.png)
![Screenshot From 2026-04-29 15-07-24.png](./Screenshot%20From%202026-04-29%2015-07-24.png)
![Screenshot From 2026-04-29 15-08-09.png](./Screenshot%20From%202026-04-29%2015-08-09.png)
![Screenshot From 2026-04-29 15-08-38.png](./Screenshot%20From%202026-04-29%2015-08-38.png)
![Screenshot From 2026-04-29 15-10-10.png](./Screenshot%20From%202026-04-29%2015-10-10.png)
![Screenshot From 2026-04-29 15-12-42.png](./Screenshot%20From%202026-04-29%2015-12-42.png)
![Screenshot From 2026-04-30 02-54-04.png](./Screenshot%20From%202026-04-30%2002-54-04.png)
![cash memory.png](./cash%20memory.png)
![index & offset calculaion.png](./index%20%26%20offset%20calculaion.png)

---

<p align="center">
  <b><a href="../20.%20Superscalar%20processors%20and%20GPU/README.md">⏪ PREVIOUS TOPIC</a></b> &nbsp; | &nbsp; <b><a href="../README.md">📚 MAIN MENU</a></b> &nbsp; | &nbsp; <b><a href="../22%3A%20Block%20Replacement%20Techniques%20%26%20Write%20Strategy/README.md">NEXT TOPIC ⏩</a></b>
</p>
