import matplotlib.pyplot as plt
import numpy as np

#data1 = np.array([((1,0,0),-1),((1,1,0),-1),((1,0,1),1),((1,1,1),1)])
#data_label = np.array([-1,-1,1,1])

data = np.array([(0,0),(1,0),(0,1),(1,1)])
data_label = np.array([-1,-1,1,1])

def dataset(data,data_label):
    result = []
    point_1 = []
    for point in data:
        asdf = [1]
        for x in point:
            asdf.append(x)
        point_1.append(asdf)

    for index,i in enumerate(point_1):
        j = []
        j.append(i)
        j.append(data_label[index])
        result.append(j)
    return np.array(result)      

def check_error(w, dataset):
    result = None
    error = 0
    for x, s in dataset:
        x = np.array(x)
        if int(np.sign(w.dot(x))) != s:
            result =  x, s
            error += 1
            print("error:%s" % x)
    print("w=%s" % w)
    print  ("error=%s/%s" % (error, len(dataset)))
    return result

#作圖
fig = plt.figure()
plt.xlim((-0.5,1.5))
plt.ylim((-0.5,1.5))
ax1 = fig.add_subplot(1,1,1)
for index,item in enumerate(data):
    plt.scatter(item[0],item[1],s=100,marker="o" if data_label[index]==1 else "x",color="blue"if data_label[index]==1 else "red")
    #print("o" if data_label[index]==1 else "x")
plt.legend(loc='upper left')
plt.ion()
plt.show()


w = np.array([1,0,0])
datas = dataset(data,data_label)
while check_error(w, datas) is not None:
        x, s = check_error(w, datas)
        w += s * x
        #作圖
        try:
            ax1.lines.remove(lines[0])
        except Exception:
            pass
        l = np.linspace(-2, 2)
        a, b = -w[1] / w[2], -w[0] / w[2]
        lines = ax1.plot(l, a * l + b, 'b-',lw = 2)
        plt.pause(0.5)
print(w)
plt.pause(10)



