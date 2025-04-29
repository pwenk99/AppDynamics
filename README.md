# AppDynamics
Some AppDynamics things

GetCpuCores.ps1 polls WMI every X seconds ($wait_time) to retrieve usage metrics for each CPU core, then sends the data to the machine agent. This metric was not available OOTB in AppDynamics when I wrote it.

If you have many cores/CPUs to monitor, be careful of API rate limits when sending data from the machine agent.

ma_api_commented.py does the same but with python (and is a little more fleshed out). Instructions:

1. Install python 3

2. Install dependencies (based on requirements.txt)
certifi==2023.7.22
charset-normalizer==3.2.0
idna==3.4
psutil==5.9.5
requests==2.31.0
urllib3==2.0.4
pip -r install <file_name>

3. Create API subfolder in machine agent dir

4. Copy ma_api_commented.py file into folder
Note: AppDynamics machine agent host (line 7) must match port number in machineagentservice.vmoptions file

5. Edit machineagentservice.vmoptions file to include the following:
-Dmetric.http.listener=true
-Dmetric.http.listener.port=8293
-Dmetric.http.listener.host=127.0.0.1

6. Restart machine agent
