# 43: QoS of NoC and Caches in TCMP Systems

<p align="center">
  <a href="../42%3A%20Concepts%20in%20Deflection%20Routers%20%5BT%5D/README.md"><img src="https://img.shields.io/badge/-PREVIOUS-black?style=for-the-badge&logo=arrow-left&logoColor=white" /></a>
  <a href="../README.md"><img src="https://img.shields.io/badge/-MAIN%20MENU-black?style=for-the-badge" /></a>
  <a href="../44%3A%20Emerging%20Trends%20in%20Network%20On%20Chips/README.md"><img src="https://img.shields.io/badge/-NEXT-black?style=for-the-badge&logo=arrow-right&logoColor=white" /></a>
</p>

---

![Screenshot From 2026-05-17 04-56-09.png](./Screenshot%20From%202026-05-17%2004-56-09.png)
![Screenshot From 2026-05-17 04-58-10.png](./Screenshot%20From%202026-05-17%2004-58-10.png)
![Screenshot From 2026-05-17 05-00-17.png](./Screenshot%20From%202026-05-17%2005-00-17.png)
![Screenshot From 2026-05-17 05-01-06.png](./Screenshot%20From%202026-05-17%2005-01-06.png)
![Screenshot From 2026-05-17 05-05-22.png](./Screenshot%20From%202026-05-17%2005-05-22.png)
![Screenshot From 2026-05-17 05-19-02.png](./Screenshot%20From%202026-05-17%2005-19-02.png)
![Screenshot From 2026-05-17 05-20-41.png](./Screenshot%20From%202026-05-17%2005-20-41.png)
![Screenshot From 2026-05-17 05-31-36.png](./Screenshot%20From%202026-05-17%2005-31-36.png)
![Screenshot From 2026-05-17 05-31-43.png](./Screenshot%20From%202026-05-17%2005-31-43.png)
![Screenshot From 2026-05-17 05-35-59.png](./Screenshot%20From%202026-05-17%2005-35-59.png)
![Screenshot From 2026-05-17 05-36-54.png](./Screenshot%20From%202026-05-17%2005-36-54.png)
![Screenshot From 2026-05-17 05-40-36.png](./Screenshot%20From%202026-05-17%2005-40-36.png)
![Screenshot From 2026-05-17 16-25-52.png](./Screenshot%20From%202026-05-17%2016-25-52.png)
![Screenshot From 2026-05-17 16-26-33.png](./Screenshot%20From%202026-05-17%2016-26-33.png)
![Screenshot From 2026-05-17 16-26-48.png](./Screenshot%20From%202026-05-17%2016-26-48.png)
![Screenshot From 2026-05-17 16-27-09.png](./Screenshot%20From%202026-05-17%2016-27-09.png)
![Screenshot From 2026-05-17 16-27-38.png](./Screenshot%20From%202026-05-17%2016-27-38.png)
![Screenshot From 2026-05-17 16-27-51.png](./Screenshot%20From%202026-05-17%2016-27-51.png)
![Screenshot From 2026-05-17 16-28-14.png](./Screenshot%20From%202026-05-17%2016-28-14.png)
![Screenshot From 2026-05-17 16-49-02.png](./Screenshot%20From%202026-05-17%2016-49-02.png)
![Screenshot From 2026-05-17 16-49-54.png](./Screenshot%20From%202026-05-17%2016-49-54.png)
![Screenshot From 2026-05-17 16-50-13.png](./Screenshot%20From%202026-05-17%2016-50-13.png)
![Screenshot From 2026-05-17 16-54-15.png](./Screenshot%20From%202026-05-17%2016-54-15.png)
![Screenshot From 2026-05-17 16-55-16.png](./Screenshot%20From%202026-05-17%2016-55-16.png)
![Screenshot From 2026-05-17 17-08-43.png](./Screenshot%20From%202026-05-17%2017-08-43.png)
![Screenshot From 2026-05-17 17-11-34.png](./Screenshot%20From%202026-05-17%2017-11-34.png)
![Screenshot From 2026-05-17 17-37-19.png](./Screenshot%20From%202026-05-17%2017-37-19.png)
![Screenshot From 2026-05-17 17-38-08.png](./Screenshot%20From%202026-05-17%2017-38-08.png)
![Screenshot From 2026-05-17 17-40-05.png](./Screenshot%20From%202026-05-17%2017-40-05.png)
![Screenshot From 2026-05-17 18-17-12.png](./Screenshot%20From%202026-05-17%2018-17-12.png)
![Screenshot From 2026-05-17 18-17-47.png](./Screenshot%20From%202026-05-17%2018-17-47.png)
![Screenshot From 2026-05-17 18-20-07.png](./Screenshot%20From%202026-05-17%2018-20-07.png)
![Screenshot From 2026-05-17 18-20-28.png](./Screenshot%20From%202026-05-17%2018-20-28.png)
![Screenshot From 2026-05-17 18-20-59.png](./Screenshot%20From%202026-05-17%2018-20-59.png)
![Screenshot From 2026-05-17 18-21-06.png](./Screenshot%20From%202026-05-17%2018-21-06.png)
![Screenshot From 2026-05-17 18-21-17.png](./Screenshot%20From%202026-05-17%2018-21-17.png)
![Screenshot From 2026-05-17 18-29-39.png](./Screenshot%20From%202026-05-17%2018-29-39.png)
![Screenshot From 2026-05-17 18-29-50.png](./Screenshot%20From%202026-05-17%2018-29-50.png)
![Screenshot From 2026-05-17 18-30-07.png](./Screenshot%20From%202026-05-17%2018-30-07.png)
![Screenshot From 2026-05-17 18-32-48.png](./Screenshot%20From%202026-05-17%2018-32-48.png)
![Screenshot From 2026-05-17 18-32-53.png](./Screenshot%20From%202026-05-17%2018-32-53.png)
![Screenshot From 2026-05-17 18-33-03.png](./Screenshot%20From%202026-05-17%2018-33-03.png)
![Screenshot From 2026-05-17 18-33-14.png](./Screenshot%20From%202026-05-17%2018-33-14.png)
![Screenshot From 2026-05-17 18-34-06.png](./Screenshot%20From%202026-05-17%2018-34-06.png)
![Screenshot From 2026-05-17 18-34-45.png](./Screenshot%20From%202026-05-17%2018-34-45.png)
![Screenshot From 2026-05-17 18-36-05.png](./Screenshot%20From%202026-05-17%2018-36-05.png)
![Screenshot From 2026-05-17 18-37-51.png](./Screenshot%20From%202026-05-17%2018-37-51.png)
![Screenshot From 2026-05-17 18-38-55.png](./Screenshot%20From%202026-05-17%2018-38-55.png)
![Screenshot From 2026-05-17 18-41-09.png](./Screenshot%20From%202026-05-17%2018-41-09.png)
![Screenshot From 2026-05-17 18-42-12.png](./Screenshot%20From%202026-05-17%2018-42-12.png)
![Screenshot From 2026-05-17 18-42-28.png](./Screenshot%20From%202026-05-17%2018-42-28.png)
![Screenshot From 2026-05-17 18-42-33.png](./Screenshot%20From%202026-05-17%2018-42-33.png)
![Screenshot From 2026-05-17 18-42-56.png](./Screenshot%20From%202026-05-17%2018-42-56.png)
![Screenshot From 2026-05-17 18-43-10.png](./Screenshot%20From%202026-05-17%2018-43-10.png)
![Screenshot From 2026-05-17 18-44-06.png](./Screenshot%20From%202026-05-17%2018-44-06.png)
![Screenshot From 2026-05-17 18-45-15.png](./Screenshot%20From%202026-05-17%2018-45-15.png)
![Screenshot From 2026-05-17 18-45-21.png](./Screenshot%20From%202026-05-17%2018-45-21.png)
![Screenshot From 2026-05-17 18-45-38.png](./Screenshot%20From%202026-05-17%2018-45-38.png)
![Screenshot From 2026-05-17 18-46-34.png](./Screenshot%20From%202026-05-17%2018-46-34.png)
![Screenshot From 2026-05-17 18-46-48.png](./Screenshot%20From%202026-05-17%2018-46-48.png)
![Screenshot From 2026-05-17 18-47-28.png](./Screenshot%20From%202026-05-17%2018-47-28.png)
![Screenshot From 2026-05-17 18-47-32.png](./Screenshot%20From%202026-05-17%2018-47-32.png)
![Screenshot From 2026-05-17 18-47-45.png](./Screenshot%20From%202026-05-17%2018-47-45.png)
![Screenshot From 2026-05-17 18-48-31.png](./Screenshot%20From%202026-05-17%2018-48-31.png)
![Screenshot From 2026-05-17 18-48-38.png](./Screenshot%20From%202026-05-17%2018-48-38.png)
![Screenshot From 2026-05-17 18-50-02.png](./Screenshot%20From%202026-05-17%2018-50-02.png)
![Screenshot From 2026-05-17 18-50-11.png](./Screenshot%20From%202026-05-17%2018-50-11.png)
![Screenshot From 2026-05-17 18-51-06.png](./Screenshot%20From%202026-05-17%2018-51-06.png)
![Screenshot From 2026-05-17 18-51-27.png](./Screenshot%20From%202026-05-17%2018-51-27.png)
![Screenshot From 2026-05-17 18-51-56.png](./Screenshot%20From%202026-05-17%2018-51-56.png)
![Screenshot From 2026-05-17 18-52-05.png](./Screenshot%20From%202026-05-17%2018-52-05.png)

---

<p align="center">
  <a href="../42%3A%20Concepts%20in%20Deflection%20Routers%20%5BT%5D/README.md"><img src="https://img.shields.io/badge/-PREVIOUS-black?style=for-the-badge&logo=arrow-left&logoColor=white" /></a>
  <a href="../README.md"><img src="https://img.shields.io/badge/-MAIN%20MENU-black?style=for-the-badge" /></a>
  <a href="../44%3A%20Emerging%20Trends%20in%20Network%20On%20Chips/README.md"><img src="https://img.shields.io/badge/-NEXT-black?style=for-the-badge&logo=arrow-right&logoColor=white" /></a>
</p>
