class Solution(object):
    def deleteDuplicates(self, head):
        k = 0
        for i in range(len(head)):
            if head[i] != val :
                head[k] = head[i]
                k += 1
        return k 