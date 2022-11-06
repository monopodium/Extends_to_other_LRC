import math

def Azure_LRC_1(code,debug=0,alg1=0):
    #parameters
    n = code[0] #number of blocks
    k = code[1] #number of data blocks
    r = code[2] #number of data blocks in each group
    l = math.ceil(k/r) + 1 #number of local parity blocks
    g = n - k - l #number of global parity blocks
    if g == 0:
        print("Invalid parameters!")
        exit(0)
    b = g + 1 #fault tolerance

    node = []
    for i in range(k):
        node_id = 'D' + str(i)
        node.append(node_id)
    for i in range(g):
        node_id = 'G' + str(i)
        node.append(node_id)
    for i in range(l):
        node_id = 'L' + str(i)
        node.append(node_id)
    if debug:
        print(node)

    dict = {}
    for each_node in node:
        #获取blocks编号
        if(len(each_node)>2):
            id = int(each_node[1])*10 + int(each_node[2])
        else:
            id = int(each_node[1])
        if each_node[0] == 'D':
            dict[each_node] = math.floor(id/r)
        elif each_node[0] == 'L':
            dict[each_node] = id
        else:
            dict[each_node] = math.ceil(k/r)
    if debug:
        print(dict)

    #分组
    rank_group = []
    for i in range(l):
        rank_group.append([])
    for each_node in node:
        rank_group[dict[each_node]].append(each_node)
    if debug:
        print(rank_group)

    #划分集群
    rank = []
    if alg1 == 0: #每个组划分成math.ceil(len(group)/b)个集群，一个集群只放一个分组
        for each_group in rank_group:
            if b >= len(each_group):
                rank.append(each_group)
            else:
                for eg in range(0,len(each_group),b):
                    rank.append(each_group[eg:eg+b])
    else: #尽可能将数据存到最少数量的集群中，条件允许情况下一个集群可放多个分组（保持分组不分割）
        remain_tail = []
        index = 0
        for each_group in rank_group:
            len1 = len(each_group)
            if b >= len1:
                if index > 0:
                    len0 = len(rank[index - 1])
                    if b - len0 >= len1: #如果放得下，尽可能的把多个组放到一个集群
                        for block in each_group:
                            rank[index-1].append(block)
                    else:
                        rank.append(each_group)
                        index += 1
                else:
                    rank.append(each_group)
                    index += 1
            else:
                for eg in range(0,len(each_group),b):
                    if eg+b > len(each_group):
                        remain_tail.append(each_group[eg:])
                    else:
                        rank.append(each_group[eg:eg+b])
                        index += 1
        if len(remain_tail) > 0: #整合所有组的尾巴，用最少数量的集群存储，同时保持每个尾巴不再被分割
            for each_tail in remain_tail:
                len1 = len(each_tail)
                len0 = len(rank[index-1])
                if b - len0 >= len1:
                    for block in each_tail:
                        rank[index-1].append(block)
                else:
                    rank.append(each_tail)
                    index += 1
    if debug:
        print(rank)

    cost = {}
    for cluster in rank:
        for each_node in cluster:
            cost[each_node] = 0
            rank1 = rank.copy()
            rank1.remove(cluster)
            group_id = dict[each_node]
            for helper_cluster in rank1:
                for other_node in helper_cluster:
                    if dict[other_node] == group_id:
                        cost[each_node] += 1
                        break
    if debug:
        print(cost)

    sum_DRC = 0
    for each_node in node:
        if each_node[0] == 'D':
            sum_DRC += cost[each_node]
    DRC = sum_DRC/k
    sum_NRC = 0
    for each_node in node:
        sum_NRC += cost[each_node]
    NRC = sum_NRC/k

    return DRC,NRC

code = [14,8,4]
# code = [21,10,2]
drc,nrc = Azure_LRC_1(code,1,1)
print(drc,nrc)
