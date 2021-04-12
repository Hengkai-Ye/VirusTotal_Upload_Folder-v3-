import os
import shutil
 
def mv_file(img, num):
    list_ = os.listdir(img)
    if num > len(list_):
        print('length need to be less than：', len(list_))
        exit()
    num_file = int(len(list_)/num) + 1
    cnt = 0
    for n in range(1,num_file+1):
        new_file = os.path.join(img + '_' + str(n))
        if os.path.exists(new_file+'_'+str(cnt)):
            print('path exist: ', new_file)
            exit()
        print('init folder：', new_file)
        os.mkdir(new_file)
        list_n = list_[num*cnt:num*(cnt+1)]
        for m in list_n:
            old_path = os.path.join(img, m)
            new_path = os.path.join(new_file, m)
            shutil.copy(old_path, new_path)
        cnt = cnt + 1
    print('============task OK!===========')
if __name__ == "__main__":
    mv_file('./dataset2/00241', 100) # 00241 is a virusshare dataset, including 60k+ malware. 
    #devide the dataset into several sub dataset, each contains 100 malware