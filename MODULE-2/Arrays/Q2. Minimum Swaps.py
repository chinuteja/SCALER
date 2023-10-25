'''
Given an array of integers A and an integer B, 
find and return the minimum number of swaps required to bring all the 
numbers less than or equal to B together.

Note: It is possible to swap any two elements, not necessarily consecutive.

A = [1, 12, 10, 3, 14, 10, 5]
 B = 8

Output 2
'''
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        k = 0
        for i in A:
            if i <= B:
                k += 1
        
        if (k == 0) or (k == 1):
            return 0
        bad = 0
        for i in range(k):
            if A[i] > B:
                bad += 1
        j = 0
        # s = 1
        # ans = bad
        # e = k
        # while (e<len(A)):
        # 	if A[s-1] > B:
        # 		bad = bad - 1
        # 	if A[e] > B:
        # 		bad = bad + 1 
        # 	ans = max(ans,bad)
        # 	e += 1
        # 	s += 1
        # return ans
        ans = bad
        for i in range(k,len(A)):
            if A[j]>B:
                bad -= 1
            if A[i]>B:
                bad += 1
            ans = min(ans,bad)
            j+=1
        return ans


sol = Solution()
A = [6414,-750,-8426,7656,8276,6890,1986,-5879,1066,-4306,695,5734,4795,8682,45,5132,9315,-9199,-7268,-2898,8918,9363,-1243,5294,3575,5826,8846,5885,5792,1385,4857,6651,7157,-5941,9323,-5823,-8130,3378,-3909,-566,-4101,259,1922,-7543,-136,4285,-5062,-9396,-8628,-1637,-14,-8344,-1759,1617,-6756,2979,-2126,-4635,-1158,-8981,-9943,-5819,8767,1616,527,-5744,4005,908,870,-5299,-335,-928,6704,-6095,9702,4684,-9497,-7308,7939,-3809,-1920,8793,-8777,8805,8440,3009,7828,50,5550,-3537,-361,-4714,-2409,440,204,5714,4293,5608,-7642,-4339,-3776,5745,-1049,-6562,-8753,2653,-1909,-9425,-7204,-6483,372,-2048,-7738,-244,-304,4177,-6518,-2716,-8391,-8529,-8825,-7910,3441,7416,7138,-7797,-875,7081,-1886,-2685,8193,9408,-2514,778,3235,-5883,-746,-4876,-6948,1012,-2722,-8043,9716,2216,-4678,9752,6949,-263,4195,9027,-5487,-4373,1095,3340,8702,-9854,3269,6674,2550,4477,3174,-6946,-8915,-1123,5568,2617,6663,4595,-1717,9827,7392,8433,-2068,-5800,-2329,2548,-624,1638,4011,-1122,3514,-4675,1610,7536,1802,9208,7565,-8418,-2115,-5873,5125,-3233,6803,7004,71,-5848,-9510,-3215,-4944,5979,4606,7440,700,-9311,6202,7838,3224,1725,4380,-8827,-2405,6521,6737,2426,-7571,-2924,3318,-8624,-1694,1533,-3279,-9177,4692,-2616,-7887,4885,-7669,-8733,4145,669,-2269,7727,-912,8099,4298,-110,9990,7273,713,-1293,257,552,1277,-5787,6781,7398,5276,-7786,7572,4007,2775,-7133,-9152,-3088,-7146,-6192,-7377,9996,6890,9807,-1962,-2315,4312,3365,8067,-6319,-8825,-3751,-2339,4131,2898,613,-5971,-3065,-8302,-9775,4435,4792,6547,7218,1777,8515,8836,7857,-6820,-652,-9457,-7962,-8110,-5754,-6700,-4499,6052,-3567,6549,-8790,9229,-4907,-9070,6931,7053,2671,9023,-312,1946,-4010,9750,-5350,3611,-1699,5050,-4116,-3186,-6638,-2191,9524,-27,-203,8586,6062,8136,-5805,5339,7829,-7806,-5138,5134,98,2491,4549,9717,9905,-530,195,-2114,-4719,6609,-9578,6766,-502,-8398,-2583,-8684,9765,-9393,-1157,-3088,-2010,-2665,7548,-6736,-7670,3877,-7921,-303,-7393,3356,9426,1518,98,5879,-7138,-4824,2783,-1303,-7542,5905,815,-893,3513,-4284,-6206,4335,-903,1920,1381,-3499,6864,-3298,-8173,-7274,-2575,-3105,9232,555,1857,-329,-403,7062,9248,-5275,-1759,-3597,-8270,6390,-3321,-5005,4080,-9823,-4241,6141,7654,7399,-6319,-3378,-5581,8792,-7548,-3357,-4272,-6483,-5602,-8537,-7307,-6618,1561,-1838,236,3855,5094,-5773,-4726,3173,-759,-4057,1016,8814,-4953,-5888,3950,-3441,2604,2153,7880,-8376,-2489,-2583,243,-6463,7118,364,-69,-3085,5211,-1778,-7026,-1206,9996,-125,2713,-170,-470,6908,4445,-8515,-8783,2123,1036,-5781,-2468,-8719,5644,-7280,8832,6458,-9595,3419,5946,-9930,-4129,6755,-9842,7550,-5067,2120,-3739,3546,7150,-3079,5565,1677,4608,2859,72,-8942,-1160,2312,-3582,4187,9843,5640,8819,-9771,-7168,6217,-6112,5370,-3835,-5796,7055,-2422,4709,-7654,-9780,-2973,6951,7457,-6617,-4655,-8723,9850,9128,6995,7097,-426,8217,-5715,-146,-6860,6942,3888,5515,7308,-7521,7178,9687,7554,1160,-669,-661,7997,6410,-7159,923,-3159,8034,-61,7743,-3201,2597,-4597,-8501,-6478,-4161,6320,8251,-3329,-7613,8596,7345,-1884,5460,1356,-6565,-403,9817,-154,-3705,-1745,-5059,-4958,-9106,2595,2188,-6083,1106,3706,9643,-1874,-5608,7009,1455,878,-8050,-1691,4627,1843,-932,-5400,-4463,-1841,3800,-5141,-9061,5985,-1416,-1036,3720,1459,9069,3929,2412,2590,7120,-4228,5266,4273,930,-7335,4621,7503,-5906,374,-4610,-9189,7671,-5428,-7337,-2921]
B = 45
print(len(A))
print(sol.solve(A,B))