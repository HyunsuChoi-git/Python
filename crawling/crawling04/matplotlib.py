import matplotlib.pyplot as pyplot

# matplotlib : 그래프를 만들어주는 라이브러리
# pyplot.plot([1,2,3,4])
# pyplot.show()

x = range(100)
y = [v*v for v in x]
pyplot.plot(x,y)
pyplot.show()