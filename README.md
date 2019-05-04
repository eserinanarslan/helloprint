# helloprint

This project was developed for "HELLOPRINT"

HelloPrint project is a streaming data architecture that collects events from JSON files and persists events on targets (SQLITE).

When the project was developed, it was observed that the parameters of continuous data were increased and the data structure was developed accordingly.

Architucture:

<img width="518" alt="Screen Shot 2019-05-03 at 19 49 25" src="https://user-images.githubusercontent.com/25620152/57152609-a3cf1100-6ddc-11e9-96bf-77e5f0bb31b4.png">

Tool Used:
Pycharm Community 2019.1
SQLITE
Python 3.6

Asistant Tools:
"watch" for controlling DB. You have to install "watch" to your computer. (brew install watch)

Execution:

- First of all you have to install requirements by using below command under HelloPrint project.
pip install -r requirement.txt 

- Secondly you have to put source json files under with below hierarchy:

![Screen Shot 2019-05-03 at 19 46 42](https://user-images.githubusercontent.com/25620152/57152501-5ce11b80-6ddc-11e9-8681-9c7f06b7c64a.png)


This code is organized into two steps. First step is that reading messages from JSON data files.A multi-thread structure was created at this stage. While processing, it will create threads acording to your machine core count. This threads are working in parallel.

" process_pool = pool.Pool(mp.cpu_count())" in app.py

Also you can control THREAD_POOL_SIZE from config.json .


- Then you can run "app.py" file in terminal.
Python src/app.py

![Screen Shot 2019-05-03 at 19 35 17](https://user-images.githubusercontent.com/25620152/57152322-d75d6b80-6ddb-11e9-9b18-43fa5a709db6.png)

You can observe the process while the code is running.

1) In first step (reading files and getingt lines) On your compıuter, you can run < HTOP > command to watch your machine cores' load.

2)In second step,You can open terminal and under "HelloPrint" project, run < watch -n 3 "du -hs sqlite" >.This watch mode shows you DB size in three seconds period.

3)After execution, you can execute your SQL statements by following below instructions.
  a) Under HelloPrint/sqlite/db path, you can run "sqlite3 sqlite.db". It is ready for execution.

****************************************************************************************************************************

You can also analyze results report folder after first execution. It includes favourite and command paramaters results. Moreover, process execution times are writen in this TXT file which is called "HelloPrintReport.txt"

 NOTE-1 :I wanted to create a unique constraint when creating a database. First I wanted to specify the "request_id" parameter as unique constraint. Then I observed that request_id is not unique. I didn't want to deal any more because the parameter that should be unique like "token" is not included in every file.
 
 NOTE-2 :I didn't need to install the facebook-backup file because when I reviewed the file, I noticed that the backup was successful. For this reason, "Back-up" file has not been uploaded to the database.


