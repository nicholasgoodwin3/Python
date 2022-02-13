def countdown(num):
    output = []
    for i in range(num,-1,-1):
        output.append(i)
    return output

print(countdown(5))

def p_and_r(list):
    print(list[0])
    return list[1]

print(p_and_r([1,2]))

def f_p_l(list):
    return list[0] + len(list)

print(f_p_l([1,2,3,4,5]))

def v_g_t_s(list):
    if len(list) < 2:
        return False
    output = []
    for i in range(0,len(list)):
        if list[i] > list[1]:
            output.append(list[i])
    print(len(output))
    return output


print(v_g_t_s([5,2,3,2,1,4]))
print(v_g_t_s([3]))

def l_and_v(size,value):
    output = []
    for i in range(0, size):
        output.append(value)
    return output

print(l_and_v(4,7))
print(l_and_v(6,2))