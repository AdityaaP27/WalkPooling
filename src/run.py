import subprocess

datasets = ["USAir", "NS Power", "Celegans", "Router", "PB", "Ecoli", "Yeast"]
embedding_dim = 16

for dataset in datasets:
    for data_split_num in range(1, 11):
        for drnl in [0, 1]:
            log_dir = f"d{drnl}_{data_split_num}"
            init_attribute = "ones"
            init_representation = "None"

            command = [
                "python",
                "src/main.py",
                "--data-split-num=" + str(data_split_num),
                "--log=" + log_dir,
                "--data-name=" + dataset,
                "--drnl=" + str(drnl),
                "--init-attribute=" + init_attribute,
                "--init-representation=" + init_representation,
                "--embedding-dim=" + str(embedding_dim)
            ]

            subprocess.run(command)
