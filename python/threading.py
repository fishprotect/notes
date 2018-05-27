##在多线程传函数参数时，一定要以元祖的形式传入，如下举例
import threading

def print_kws(kws):
  print(kws)
th_list_error=[]
th_list_correct = []
for i in range(100):
  #x = threading.Thread(target=print_kws,args=(i))    
  #错误的传参方式，args后面必须是元祖，而只有一个元素的元祖，必须在元素后面加逗号。
  #x = (1),则type(x)为：<class 'int'>；若x = (1,),则type(x)为：<class 'tuple'>
  x = threadinf.Thread(target=print_kws,args=(i,))
  th_list.append(x)
