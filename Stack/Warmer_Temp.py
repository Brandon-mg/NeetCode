def dailyTemp(temperatures):
    s=[]
    res = [0 for i in range(len(temperatures))]
    for i in range(len(temperatures)-1, -1, -1):
        while s and temperatures[s[-1]] <= temperatures[i]:
            s.pop()
        res[i] = 0 if len(s) == 0 else s[-1] - i
        s.append(i)
        print(s)
    return res


if __name__ == '__main__':
    temperatures = [73,74,75,71,72,73,76,73]
    print('temperatures = [73,74,75,71,69,72,76,73]')
    print(dailyTemp(temperatures))