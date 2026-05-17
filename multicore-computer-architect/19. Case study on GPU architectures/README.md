# 19. Case study on GPU architectures

<p align="center">
  <a href="../18.Introduction%20to%20GPU%20architectures/README.md"><img src="https://img.shields.io/badge/-PREVIOUS-black?style=for-the-badge&logo=arrow-left&logoColor=white" /></a>
  <a href="../README.md"><img src="https://img.shields.io/badge/-MAIN%20MENU-black?style=for-the-badge" /></a>
  <a href="../20.%20Superscalar%20processors%20and%20GPU/README.md"><img src="https://img.shields.io/badge/-NEXT-black?style=for-the-badge&logo=arrow-right&logoColor=white" /></a>
</p>

---

![Screenshot From 2026-04-27 15-46-59.png](./Screenshot%20From%202026-04-27%2015-46-59.png)
![Screenshot From 2026-04-27 15-56-02.png](./Screenshot%20From%202026-04-27%2015-56-02.png)
![Screenshot From 2026-04-27 15-57-32.png](./Screenshot%20From%202026-04-27%2015-57-32.png)
![Screenshot From 2026-04-27 15-58-47.png](./Screenshot%20From%202026-04-27%2015-58-47.png)
![Screenshot From 2026-04-27 15-58-58.png](./Screenshot%20From%202026-04-27%2015-58-58.png)
![Screenshot From 2026-04-27 16-00-48.png](./Screenshot%20From%202026-04-27%2016-00-48.png)
![Screenshot From 2026-04-27 17-36-09.png](./Screenshot%20From%202026-04-27%2017-36-09.png)
![Screenshot From 2026-04-27 17-59-09.png](./Screenshot%20From%202026-04-27%2017-59-09.png)
![Screenshot From 2026-04-28 00-00-58.png](./Screenshot%20From%202026-04-28%2000-00-58.png)
![Screenshot From 2026-04-28 00-03-18.png](./Screenshot%20From%202026-04-28%2000-03-18.png)
![Screenshot From 2026-04-28 00-18-38.png](./Screenshot%20From%202026-04-28%2000-18-38.png)
![Screenshot From 2026-04-28 00-21-58.png](./Screenshot%20From%202026-04-28%2000-21-58.png)
![Screenshot From 2026-04-28 00-31-37.png](./Screenshot%20From%202026-04-28%2000-31-37.png)
![Screenshot From 2026-04-28 00-33-52.png](./Screenshot%20From%202026-04-28%2000-33-52.png)
![Screenshot From 2026-04-28 00-36-33.png](./Screenshot%20From%202026-04-28%2000-36-33.png)
![Screenshot From 2026-04-28 01-11-47.png](./Screenshot%20From%202026-04-28%2001-11-47.png)
![Screenshot From 2026-04-28 01-14-01.png](./Screenshot%20From%202026-04-28%2001-14-01.png)
![Screenshot From 2026-04-28 01-19-03.png](./Screenshot%20From%202026-04-28%2001-19-03.png)
![Screenshot From 2026-04-28 02-21-17.png](./Screenshot%20From%202026-04-28%2002-21-17.png)
![Screenshot From 2026-04-28 02-27-46.png](./Screenshot%20From%202026-04-28%2002-27-46.png)
![Screenshot From 2026-04-28 03-02-04.png](./Screenshot%20From%202026-04-28%2003-02-04.png)
![Screenshot From 2026-04-28 03-03-57.png](./Screenshot%20From%202026-04-28%2003-03-57.png)
![Screenshot From 2026-04-28 03-07-18.png](./Screenshot%20From%202026-04-28%2003-07-18.png)
![Screenshot From 2026-04-28 03-08-45.png](./Screenshot%20From%202026-04-28%2003-08-45.png)
![Screenshot From 2026-04-28 03-28-55.png](./Screenshot%20From%202026-04-28%2003-28-55.png)
![Screenshot From 2026-04-28 03-29-23.png](./Screenshot%20From%202026-04-28%2003-29-23.png)
![Screenshot From 2026-04-28 03-30-04.png](./Screenshot%20From%202026-04-28%2003-30-04.png)
![Screenshot From 2026-04-28 03-31-40.png](./Screenshot%20From%202026-04-28%2003-31-40.png)
![Screenshot From 2026-04-28 03-31-53.png](./Screenshot%20From%202026-04-28%2003-31-53.png)
![Screenshot From 2026-04-28 03-32-09.png](./Screenshot%20From%202026-04-28%2003-32-09.png)
![Screenshot From 2026-04-28 03-32-16.png](./Screenshot%20From%202026-04-28%2003-32-16.png)
![Screenshot From 2026-04-28 03-33-20.png](./Screenshot%20From%202026-04-28%2003-33-20.png)
![Screenshot From 2026-04-28 03-34-33.png](./Screenshot%20From%202026-04-28%2003-34-33.png)
![Screenshot From 2026-04-28 03-34-37.png](./Screenshot%20From%202026-04-28%2003-34-37.png)
![Screenshot From 2026-04-28 03-35-06.png](./Screenshot%20From%202026-04-28%2003-35-06.png)
![Screenshot From 2026-04-28 03-35-36.png](./Screenshot%20From%202026-04-28%2003-35-36.png)
![Screenshot From 2026-04-28 03-37-26.png](./Screenshot%20From%202026-04-28%2003-37-26.png)
![Screenshot From 2026-04-28 03-40-06.png](./Screenshot%20From%202026-04-28%2003-40-06.png)
![Screenshot From 2026-04-28 03-40-13.png](./Screenshot%20From%202026-04-28%2003-40-13.png)
![Screenshot From 2026-04-28 03-40-42.png](./Screenshot%20From%202026-04-28%2003-40-42.png)
![Screenshot From 2026-04-28 03-42-08.png](./Screenshot%20From%202026-04-28%2003-42-08.png)
![Screenshot From 2026-04-28 03-42-11.png](./Screenshot%20From%202026-04-28%2003-42-11.png)
![Screenshot From 2026-04-28 03-42-17.png](./Screenshot%20From%202026-04-28%2003-42-17.png)
![Screenshot From 2026-04-28 03-43-01.png](./Screenshot%20From%202026-04-28%2003-43-01.png)
![Screenshot From 2026-04-28 03-44-06.png](./Screenshot%20From%202026-04-28%2003-44-06.png)
![Screenshot From 2026-04-28 03-45-44.png](./Screenshot%20From%202026-04-28%2003-45-44.png)
![Screenshot From 2026-04-28 04-20-09.png](./Screenshot%20From%202026-04-28%2004-20-09.png)
![Screenshot From 2026-04-28 04-21-00.png](./Screenshot%20From%202026-04-28%2004-21-00.png)
![Screenshot From 2026-04-28 04-21-47.png](./Screenshot%20From%202026-04-28%2004-21-47.png)
![Screenshot From 2026-04-28 04-34-31.png](./Screenshot%20From%202026-04-28%2004-34-31.png)
![bsp.png](./bsp.png)
![memory-coalescing.png](./memory-coalescing.png)

---

<p align="center">
  <a href="../18.Introduction%20to%20GPU%20architectures/README.md"><img src="https://img.shields.io/badge/-PREVIOUS-black?style=for-the-badge&logo=arrow-left&logoColor=white" /></a>
  <a href="../README.md"><img src="https://img.shields.io/badge/-MAIN%20MENU-black?style=for-the-badge" /></a>
  <a href="../20.%20Superscalar%20processors%20and%20GPU/README.md"><img src="https://img.shields.io/badge/-NEXT-black?style=for-the-badge&logo=arrow-right&logoColor=white" /></a>
</p>
