lines = open('/home/moumita/Documents/YOLO/others/dataset/annotated_vdos_merged/data/train.txt').readlines()
new_file = open('/home/moumita/Documents/YOLO/others/dataset/annotated_vdos_merged/data/train_clean.txt', 'w')
all_lines = []
valid_lines = []
miss = 0
c = 0
c2 = 0
for line in lines:
    all_lines.append(line.replace('jpg','txt').replace('\n',''))
    
    try:
        tmp = (open(all_lines[c]).readline())
        # print(tmp)
        valid_lines.append(all_lines[c].replace('txt','jpg'))
        new_file.write(valid_lines[c2]+'\n')
        c2+=1
    except:
        print(line)
        miss+=1
        print(miss)
    c+=1
# new_file.close()