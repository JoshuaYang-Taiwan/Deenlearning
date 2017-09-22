import matplotlib.pyplot as plt
import numpy as np

f = open("579.txt","r")
dataset = []
while 1:
    line = f.readline()
    lineData = []
    data = []
    label = []
    lineResult = []
    for i in line.split(" "):
        if(i != "" and i != "\r\n" ):
            lineData.append(i)
    if(line == ""):
        break
    data.append(1)
    data.append(float(lineData[0]))
    data.append(float(lineData[1]))
    label.append(lineData[2])
    if(lineData[2] == "1" or lineData[2] == "2"):
        lineResult.append(data)
        lineResult.append(1 if lineData[2] == "1" else -1)
        dataset.append(lineResult)
"""
#網路上找的dataset 可以線性分割

dataset = np.array([
((1, -0.4, 0.3), -1),
((1, -0.3, -0.1), -1),
((1, -0.2, 0.4), -1),
((1, -0.1, 0.1), -1),
((1, 0.9, -0.5), 1),
((1, 0.7, -0.9), 1),
((1, 0.8, 0.2), 1),
((1, 0.4, -0.6), 1)])
"""

#判斷有沒有分類錯誤，並列印錯誤率

def check_error(w, dataset):
    result = None
    error = 0
    for x, s in dataset:
        x = np.array(x)
        if int(np.sign(w.T.dot(x))) != s:
            result =  x, s
            error += 1
    print ("error=%s/%s" % (error, len(dataset)))
    return result


#作圖
fig = plt.figure()
plt.xlim((-2,5))
plt.ylim((-2,5))
ax = fig.add_subplot(1,1,1)
for item in dataset:
    ax.scatter(item[0][1],item[0][2],s=100,marker="o" if item[1]==1 else "x",color="blue"if item[1]==1 else "red")
plt.ion()
plt.show()

#PLA演算法實作
w = np.zeros(3)
while check_error(w, dataset) is not None:
    try:
            ax.lines.remove(lines[0])
    except Exception:
        pass

    x, s = check_error(w, dataset)
    w += s * x

    l = np.linspace(-2,5)
    a,b = -w[1]/w[2], -w[0]/w[2]
    lines = ax.plot(l, a*l + b, 'r-',lw=2)
    plt.pause(0.1)
plt.pause(10)


