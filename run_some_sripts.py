import subprocess
import string

# data1 = ["NS", "Ecoli"]
# for data in data1:
#     for i in range(1,2):
    
#         call = "python src/main.py --data-split-num " + str(i) + " --log d0_" + str(i) + " --data-name " + data + " --drnl 0 --init-attribute ones --init-representation None --embedding-dim 16"
#         cmd_call = call.split(' ')
#         # print(cmd_call)
#         subprocess.call(cmd_call, shell=True)
        
#         call1 = "python src/main.py --data-split-num " + str(i) + " --log d0_" + str(i) + " --data-name " + data + " --drnl 1 --init-attribute ones --init-representation None --embedding-dim 16"
#         cmd_call1 = call1.split(' ')
#         # print(cmd_call)
#         subprocess.call(cmd_call1, shell=True)
    
data2 = ["cora" ,"citeseer", "pubmed"]
feature_set = ["vgae", "gic", "argva"]
for data_name in data2:
    for feature in feature_set:
        for i in range(1,2):
        
            call2 = "python src/main.py --seed " + str(i) + " --log " + str(i) + " --data-name " + data_name + " --drnl 0 --init-attribute None --init-representation " + feature + " --embedding-dim 32"        
            cmd_call2 = call2.split(' ')
            subprocess.call(cmd_call2, shell=True)