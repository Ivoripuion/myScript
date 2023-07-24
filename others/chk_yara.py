import yara
import os

# 设置规则和样本文件夹路径
rules_folders = ['rules\\Metasploit','rules\\CobaltStrike', 'rules\\rules', 'rules\\signature_yara', 'rules\\CN_phishing','rules\\silver']
samples_folder = 'C:\\Users\\andycylin\\Desktop\\workstation\\linux'

# 收集样本文件
sample_files = []

for root, _, files in os.walk(samples_folder):
    for file_name in files:
        file_path = os.path.join(root, file_name)
        sample_files.append(file_path)

total_samples = len(sample_files)

# 收集所有文件夹中的YARA规则文件并编译规则
yara_rules = []
for rules_folder in rules_folders:
    for root, _, files in os.walk(rules_folder):
        for file_name in files:
            if file_name.endswith('.yar') or file_name.endswith('.yara'):
                rule_file_path = os.path.join(root, file_name)
                try:
                    rule = yara.compile(filepath=rule_file_path)
                    yara_rules.append((rule, rule_file_path))  # 添加规则和文件路径的元组到列表中
                except yara.Error as e:
                    print(f"Error ({str(e)}) while compiling YARA rule '{rule_file_path}', skipping this file.")

# 遍历样本并使用所有YARA规则检测
matched_samples_count = 0
missed_samples = []

for sample_file in sample_files:
    is_matched = False
    for rule, rule_file_path in yara_rules:  # 解包元组获取规则和文件路径
        matches = rule.match(sample_file)
        if matches:
            is_matched = True
            print(f"File '{sample_file}' matched with the following rule in '{rule_file_path}': {', '.join([match.rule for match in matches])}")
            break

    if is_matched:
        matched_samples_count += 1
    else:
        missed_samples.append(sample_file)

# 计算总体检出率并输出
detection_rate = 100 * matched_samples_count / total_samples
print(f"Detection rate: {detection_rate}% ({matched_samples_count}/{total_samples})")

# 将未检出的样本文件名输出到missed.txt文件中
with open('missed.txt', 'w') as output_file:
    for missed_sample in missed_samples:
        output_file.write(missed_sample + '\n')

print(f"Missed samples are written to 'missed.txt'")