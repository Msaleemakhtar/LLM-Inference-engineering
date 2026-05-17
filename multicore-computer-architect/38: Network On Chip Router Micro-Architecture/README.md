# 38: Network On Chip Router Micro-Architecture

<p align="center">
  <b><a href="../37%3A%20Routing%20Techniques%20in%20Network%20On%20Chip/README.md">⏪ PREVIOUS TOPIC</a></b> &nbsp; | &nbsp; <b><a href="../README.md">📚 MAIN MENU</a></b> &nbsp; | &nbsp; <b><a href="../39%3A%20Concepts%20in%20Network%20on%20Chip/README.md">NEXT TOPIC ⏩</a></b>
</p>

---

![Screenshot From 2026-05-14 04-29-12.png](./Screenshot%20From%202026-05-14%2004-29-12.png)
![Screenshot From 2026-05-14 04-51-18.png](./Screenshot%20From%202026-05-14%2004-51-18.png)
![Screenshot From 2026-05-14 04-53-14.png](./Screenshot%20From%202026-05-14%2004-53-14.png)
![Screenshot From 2026-05-14 04-58-04.png](./Screenshot%20From%202026-05-14%2004-58-04.png)
![Screenshot From 2026-05-14 04-59-33.png](./Screenshot%20From%202026-05-14%2004-59-33.png)
![Screenshot From 2026-05-14 04-59-35.png](./Screenshot%20From%202026-05-14%2004-59-35.png)
![Screenshot From 2026-05-14 04-59-40.png](./Screenshot%20From%202026-05-14%2004-59-40.png)
![Screenshot From 2026-05-14 04-59-44.png](./Screenshot%20From%202026-05-14%2004-59-44.png)
![Screenshot From 2026-05-14 04-59-48.png](./Screenshot%20From%202026-05-14%2004-59-48.png)
![Screenshot From 2026-05-14 04-59-54.png](./Screenshot%20From%202026-05-14%2004-59-54.png)
![Screenshot From 2026-05-14 05-01-21.png](./Screenshot%20From%202026-05-14%2005-01-21.png)
![Screenshot From 2026-05-14 05-01-27.png](./Screenshot%20From%202026-05-14%2005-01-27.png)
![Screenshot From 2026-05-14 05-01-31.png](./Screenshot%20From%202026-05-14%2005-01-31.png)
![Screenshot From 2026-05-14 05-01-34.png](./Screenshot%20From%202026-05-14%2005-01-34.png)
![Screenshot From 2026-05-14 05-01-41.png](./Screenshot%20From%202026-05-14%2005-01-41.png)
![Screenshot From 2026-05-14 05-01-44.png](./Screenshot%20From%202026-05-14%2005-01-44.png)
![Screenshot From 2026-05-14 05-01-47.png](./Screenshot%20From%202026-05-14%2005-01-47.png)
![Screenshot From 2026-05-14 05-02-11.png](./Screenshot%20From%202026-05-14%2005-02-11.png)
![Screenshot From 2026-05-14 05-03-32.png](./Screenshot%20From%202026-05-14%2005-03-32.png)
![Screenshot From 2026-05-14 05-20-40.png](./Screenshot%20From%202026-05-14%2005-20-40.png)
![Screenshot From 2026-05-14 05-55-59.png](./Screenshot%20From%202026-05-14%2005-55-59.png)
![Screenshot From 2026-05-14 15-45-24.png](./Screenshot%20From%202026-05-14%2015-45-24.png)
![Screenshot From 2026-05-14 15-46-34.png](./Screenshot%20From%202026-05-14%2015-46-34.png)
![Screenshot From 2026-05-14 15-47-08.png](./Screenshot%20From%202026-05-14%2015-47-08.png)
![Screenshot From 2026-05-14 15-48-02.png](./Screenshot%20From%202026-05-14%2015-48-02.png)
![Screenshot From 2026-05-14 15-48-06.png](./Screenshot%20From%202026-05-14%2015-48-06.png)
![Screenshot From 2026-05-14 15-48-10.png](./Screenshot%20From%202026-05-14%2015-48-10.png)
![Screenshot From 2026-05-14 16-05-56.png](./Screenshot%20From%202026-05-14%2016-05-56.png)
![Screenshot From 2026-05-14 16-27-19.png](./Screenshot%20From%202026-05-14%2016-27-19.png)
![Screenshot From 2026-05-14 16-43-40.png](./Screenshot%20From%202026-05-14%2016-43-40.png)
![Screenshot From 2026-05-14 16-44-42.png](./Screenshot%20From%202026-05-14%2016-44-42.png)
![Screenshot From 2026-05-14 17-01-44.png](./Screenshot%20From%202026-05-14%2017-01-44.png)
![Screenshot From 2026-05-14 17-01-56.png](./Screenshot%20From%202026-05-14%2017-01-56.png)
![Screenshot From 2026-05-14 17-02-09.png](./Screenshot%20From%202026-05-14%2017-02-09.png)
![Screenshot From 2026-05-14 17-02-26.png](./Screenshot%20From%202026-05-14%2017-02-26.png)
![Screenshot From 2026-05-14 17-03-00.png](./Screenshot%20From%202026-05-14%2017-03-00.png)
![Screenshot From 2026-05-14 17-03-16.png](./Screenshot%20From%202026-05-14%2017-03-16.png)
![Screenshot From 2026-05-14 17-04-56.png](./Screenshot%20From%202026-05-14%2017-04-56.png)
![Screenshot From 2026-05-14 17-28-21.png](./Screenshot%20From%202026-05-14%2017-28-21.png)
![Screenshot From 2026-05-14 17-29-44.png](./Screenshot%20From%202026-05-14%2017-29-44.png)
![Screenshot From 2026-05-14 17-31-21.png](./Screenshot%20From%202026-05-14%2017-31-21.png)
![Screenshot From 2026-05-14 17-33-17.png](./Screenshot%20From%202026-05-14%2017-33-17.png)
![Screenshot From 2026-05-14 17-36-01.png](./Screenshot%20From%202026-05-14%2017-36-01.png)
![Screenshot From 2026-05-14 22-33-42.png](./Screenshot%20From%202026-05-14%2022-33-42.png)
![Screenshot From 2026-05-14 22-34-26.png](./Screenshot%20From%202026-05-14%2022-34-26.png)
![Screenshot From 2026-05-14 22-36-52.png](./Screenshot%20From%202026-05-14%2022-36-52.png)
![Screenshot From 2026-05-14 22-37-29.png](./Screenshot%20From%202026-05-14%2022-37-29.png)
![Screenshot From 2026-05-14 22-37-36.png](./Screenshot%20From%202026-05-14%2022-37-36.png)
![Screenshot From 2026-05-14 22-37-47.png](./Screenshot%20From%202026-05-14%2022-37-47.png)
![Screenshot From 2026-05-14 22-38-25.png](./Screenshot%20From%202026-05-14%2022-38-25.png)
![Screenshot From 2026-05-14 22-39-26.png](./Screenshot%20From%202026-05-14%2022-39-26.png)
![Screenshot From 2026-05-14 22-40-35.png](./Screenshot%20From%202026-05-14%2022-40-35.png)
![Screenshot From 2026-05-14 22-40-42.png](./Screenshot%20From%202026-05-14%2022-40-42.png)
![Screenshot From 2026-05-14 22-42-25.png](./Screenshot%20From%202026-05-14%2022-42-25.png)
![Screenshot From 2026-05-14 22-42-35.png](./Screenshot%20From%202026-05-14%2022-42-35.png)

---

<p align="center">
  <b><a href="../37%3A%20Routing%20Techniques%20in%20Network%20On%20Chip/README.md">⏪ PREVIOUS TOPIC</a></b> &nbsp; | &nbsp; <b><a href="../README.md">📚 MAIN MENU</a></b> &nbsp; | &nbsp; <b><a href="../39%3A%20Concepts%20in%20Network%20on%20Chip/README.md">NEXT TOPIC ⏩</a></b>
</p>
